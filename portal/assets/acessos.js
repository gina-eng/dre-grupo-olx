// Acessos necessários ao DR-E do Grupo OLX.
// Fontes: 01-cliente/acessos-e-ferramentas.md, 02-diagnostico/auditorias-contratadas.md e
// PENDENCIAS.md (itens 6 e 11). O campo "v" registra como o status foi apurado.
var ACESSOS_KEY = "dre-olx-acessos-v3";
var ACESSOS_STATUS = ["concedido", "pendente", "inexistente"];
var ACESSOS_ROTULO = {concedido: "concedido", pendente: "pendente", inexistente: "não existe"};

var ACESSOS_SEED = [
  {o:"Contas @olxbr.com para Rafael Corazza, Anselmo Bueno e Guilherme Monteiro",
   f:"Data room", r:"Michelle Morais", p:"", s:"pendente",
   n:"Chamado aberto pela Michelle, aguardando criação. Pré-requisito da fase Identificar."},
  {o:"Google Drive, pasta do data room",
   f:"Data room", r:"Michelle Morais", p:"", s:"pendente",
   v:"verificado em 24/08: a pasta não abre com a conta Google conectada",
   n:"Restrita a e-mail @olxbr.com, depende das contas acima."},

  {o:"Google Ads, VR09 ZAP+ MCC VivaReal (526-656-0190)",
   f:"Mídia paga", r:"Operações V4", p:"23/08", s:"pendente",
   n:"Convite enviado pela OLX. Falta a V4 dar o aceite em gina@v4company.com. Prazo vencido."},
  {o:"Meta Ads, VR ZAP+ (612188193108418)",
   f:"Mídia paga", r:"Michelle Morais", p:"", s:"pendente",
   v:"verificado em 24/08: não aparece entre as contas da conta Meta conectada",
   n:"Pendente de aprovação do lado da OLX."},
  {o:"Meta Ads, OLX | Autos | B2B (1742214902479721)",
   f:"Mídia paga", r:"Michelle Morais", p:"", s:"pendente",
   v:"verificado em 24/08: não aparece entre as contas da conta Meta conectada",
   n:"Pendente de aprovação do lado da OLX."},
  {o:"Google Ads, demais contas B2B (leitura)", f:"Mídia paga", r:"", p:"", s:"pendente",
   n:"Auditoria (vi). Bloco G, prioritário."},
  {o:"Meta Business Manager, acesso de parceiro", f:"Mídia paga", r:"", p:"", s:"pendente",
   n:"Necessário para ver estrutura de campanhas e públicos."},

  {o:"GA4, propriedades dos domínios B2B, nível analista", f:"Rastreamento", r:"", p:"", s:"pendente",
   n:"Auditoria (vii). Bloco H, prioritário: sem isto nenhum outro dado é confiável."},
  {o:"Google Tag Manager, contêineres publicados", f:"Rastreamento", r:"", p:"", s:"pendente",
   n:"Auditoria (vii). Bloco H, prioritário."},
  {o:"Google Search Console de cada propriedade B2B", f:"CRO e SEO", r:"", p:"", s:"pendente",
   n:"Auditoria (ii)."},

  {o:"Salesforce Marketing Cloud (visualização)", f:"CRM Marketing", r:"", p:"", s:"pendente",
   n:"Auditoria (i). Jornadas ativas, bases e métricas de e-mail."},
  {o:"CRM comercial, pipeline e motivos de perda (leitura)", f:"Pré-vendas", r:"", p:"", s:"pendente",
   n:"Auditoria (ix). Bloco J, prioritário."},
  {o:"Ferramenta de sales engagement e telefonia", f:"Pré-vendas", r:"", p:"", s:"pendente",
   n:"Auditoria (ix). Cadências e taxa de conexão."},
  {o:"Gravações de calls de qualificação, 10 a 15 recentes", f:"Pré-vendas", r:"", p:"", s:"pendente",
   n:"Camada experiencial do diagnóstico. Verificar consentimento e LGPD."},

  {o:"Meta Business Suite (analista)", f:"Redes sociais", r:"", p:"", s:"pendente", n:"Auditoria (v)."},
  {o:"LinkedIn, páginas da empresa", f:"Redes sociais", r:"", p:"", s:"pendente", n:"Auditoria (v)."},
  {o:"Demais canais ativos (YouTube, TikTok)", f:"Redes sociais", r:"", p:"", s:"pendente", n:"Auditoria (v)."},

  {o:"CMS dos domínios B2B", f:"CRO e SEO", r:"", p:"", s:"pendente",
   n:"Auditorias (ii) e (viii). Necessário para auditar LPs e fluxos."},
  {o:"Ferramenta de comportamento (Hotjar, Clarity ou similar)", f:"LPs e conversão", r:"", p:"", s:"pendente",
   n:"Auditoria (viii). Pode não existir."},
  {o:"Ferramenta de SEO (SEMrush, Ahrefs ou similar)", f:"CRO e SEO", r:"", p:"", s:"pendente",
   n:"Pode não existir."},

  {o:"V4MOS, workspace do Grupo OLX", f:"Dados", r:"Guilherme Monteiro", p:"", s:"concedido",
   v:"verificado em 24/08: autenticação OK nos seis endpoints, secret inválido devolve 401 e organização inexistente devolve 403",
   n:"Acesso funciona, mas o workspace não tem nenhum dado de mídia ingerido. Ver PENDENCIAS 11."},
  {o:"BI interno ou fonte única de verdade", f:"Dados", r:"", p:"", s:"pendente",
   n:"Bloco A. Se não existir, é sintoma da Trava de Cegueira."},
  {o:"ERP e financeiro, custo variável e margem", f:"Dados", r:"", p:"", s:"pendente",
   n:"Bloco A. Insumo de margem de contribuição e unit economics."}
];

function acessosLer() {
  var l = null;
  try { l = JSON.parse(localStorage.getItem(ACESSOS_KEY)); } catch (e) {}
  if (!Array.isArray(l)) l = ACESSOS_SEED.map(function (x) { return Object.assign({}, x); });
  return l;
}
function acessosSalvar(l) {
  try { localStorage.setItem(ACESSOS_KEY, JSON.stringify(l)); } catch (e) {}
}
function acessosContagem(l) {
  l = l || acessosLer();
  var c = {concedido: 0, pendente: 0, inexistente: 0, total: l.length};
  l.forEach(function (x) { c[x.s] = (c[x.s] || 0) + 1; });
  c.faltando = c.pendente;
  return c;
}

// ---------- Estado compartilhado ----------
// A fonte da verdade é dados/acessos.json no repositório, servido por /api/acessos.
// O localStorage vira apenas rascunho local: se a rede falhar, nada se perde.
var acessosSha = null;

async function acessosBuscarRemoto() {
  var r = await fetch("/api/acessos", {headers: {Accept: "application/json"}});
  if (!r.ok) throw new Error("HTTP " + r.status);
  var d = await r.json();
  acessosSha = d.sha || null;
  return d;
}

async function acessosGravarRemoto(lista, autor) {
  var r = await fetch("/api/acessos", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({acessos: lista, sha: acessosSha, autor: autor})
  });
  var d = null;
  try { d = await r.json(); } catch (e) {}
  if (r.status === 409) {
    var err = new Error((d && d.erro) || "conflito");
    err.conflito = true; err.atual = d && d.atual;
    throw err;
  }
  if (!r.ok) throw new Error((d && d.erro) || ("HTTP " + r.status));
  acessosSha = d.sha || null;
  return d;
}
