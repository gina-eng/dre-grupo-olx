// Estado compartilhado da lista de acessos.
// GET  devolve dados/acessos.json do repositório.
// POST grava de volta, com um commit. Só o login "v4" pode gravar.
//
// O token vive na variável de ambiente GITHUB_TOKEN_ACESSOS do projeto Vercel e
// nunca chega ao navegador: quem fala com o GitHub é esta função, no servidor.

const REPO = process.env.GITHUB_REPO || 'gina-eng/dre-grupo-olx';
const CAMINHO = 'dados/acessos.json';
const RAMO = process.env.GITHUB_BRANCH || 'main';
const API = 'https://api.github.com';

function usuarioDoPedido(req) {
  const h = req.headers.authorization || '';
  const [esquema, codificado] = h.split(' ');
  if (esquema !== 'Basic' || !codificado) return null;
  try {
    const texto = Buffer.from(codificado, 'base64').toString('utf8');
    const i = texto.indexOf(':');
    return i === -1 ? null : texto.slice(0, i);
  } catch {
    return null;
  }
}

async function github(caminho, opcoes = {}) {
  const token = process.env.GITHUB_TOKEN_ACESSOS;
  if (!token) throw Object.assign(new Error('GITHUB_TOKEN_ACESSOS não configurada'), { status: 500 });
  const r = await fetch(API + caminho, {
    ...opcoes,
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
      'Content-Type': 'application/json',
      'User-Agent': 'portal-dre-grupo-olx',
      ...(opcoes.headers || {}),
    },
  });
  const corpo = await r.text();
  let json = null;
  try { json = corpo ? JSON.parse(corpo) : null; } catch {}
  if (!r.ok) {
    throw Object.assign(new Error((json && json.message) || `GitHub ${r.status}`), { status: r.status });
  }
  return json;
}

async function ler() {
  const d = await github(`/repos/${REPO}/contents/${encodeURIComponent(CAMINHO)}?ref=${RAMO}`);
  const texto = Buffer.from(d.content, 'base64').toString('utf8');
  return { doc: JSON.parse(texto), sha: d.sha };
}

function valida(acessos) {
  if (!Array.isArray(acessos)) return 'esperava uma lista de acessos';
  if (acessos.length > 200) return 'lista longa demais';
  const status = ['concedido', 'parcial', 'pendente', 'inexistente'];
  for (const a of acessos) {
    if (!a || typeof a !== 'object') return 'linha inválida';
    for (const c of ['o', 'f', 'r', 'p', 'n']) {
      if (a[c] != null && typeof a[c] !== 'string') return `campo ${c} deve ser texto`;
      if (typeof a[c] === 'string' && a[c].length > 2000) return `campo ${c} longo demais`;
    }
    if (!status.includes(a.s)) return `status inválido: ${a.s}`;
    if (a.itens != null) {
      if (!Array.isArray(a.itens) || a.itens.length > 40) return 'itens inválidos';
      for (const x of a.itens) {
        if (typeof x !== 'string' || x.length > 500) return 'item inválido';
      }
    }
  }
  return null;
}

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  try {
    if (req.method === 'GET') {
      const { doc, sha } = await ler();
      return res.status(200).json({ ...doc, sha });
    }

    if (req.method === 'POST') {
      if (usuarioDoPedido(req) !== 'v4') {
        return res.status(403).json({ erro: 'Somente o login v4 pode alterar a lista.' });
      }
      const corpo = typeof req.body === 'string' ? JSON.parse(req.body) : req.body || {};
      const problema = valida(corpo.acessos);
      if (problema) return res.status(400).json({ erro: problema });

      const atual = await ler();
      // Sem o sha do que o navegador leu, ou com sha antigo, alguém gravou no meio.
      if (corpo.sha && corpo.sha !== atual.sha) {
        return res.status(409).json({
          erro: 'A lista foi alterada por outra pessoa enquanto você editava.',
          atual: { ...atual.doc, sha: atual.sha },
        });
      }

      const doc = {
        _comment: atual.doc._comment,
        atualizado_em: new Date().toISOString().slice(0, 10),
        atualizado_por: corpo.autor && String(corpo.autor).slice(0, 60) || 'portal (v4)',
        acessos: corpo.acessos,
      };
      const contagem = corpo.acessos.filter(a => a.s === 'concedido').length;
      await github(`/repos/${REPO}/contents/${encodeURIComponent(CAMINHO)}`, {
        method: 'PUT',
        body: JSON.stringify({
          message: `Atualiza acessos pelo portal: ${contagem} de ${corpo.acessos.length} concedidos`,
          content: Buffer.from(JSON.stringify(doc, null, 2) + '\n', 'utf8').toString('base64'),
          sha: atual.sha,
          branch: RAMO,
        }),
      });
      const novo = await ler();
      return res.status(200).json({ ...novo.doc, sha: novo.sha });
    }

    res.setHeader('Allow', 'GET, POST');
    return res.status(405).json({ erro: 'Método não permitido' });
  } catch (e) {
    const status = e.status && e.status >= 400 && e.status < 600 ? e.status : 500;
    return res.status(status).json({ erro: e.message || 'Falha ao falar com o repositório' });
  }
}
