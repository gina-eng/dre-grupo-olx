// Acessos necessários ao DR-E do Grupo OLX.
// Fontes: 01-cliente/acessos-e-ferramentas.md, 02-diagnostico/auditorias-contratadas.md e
// PENDENCIAS.md (itens 6 e 11). O campo "v" registra como o status foi apurado.
var ACESSOS_KEY = "dre-olx-acessos-v4";
var ACESSOS_STATUS = ["concedido", "parcial", "pendente", "inexistente"];
var ACESSOS_ROTULO = {
  concedido: "concedido",
  parcial: "parcial",
  pendente: "pendente",
  inexistente: "não existe"
};

// Agrupado por conta: uma liberação costuma resolver tudo que está dentro dela.
// "itens" é o que precisamos dentro daquela conta.
var ACESSOS_SEED = [
  {o:"Google", f:"Mídia, rastreamento, SEO", r:"Michelle Morais", p:"", s:"pendente",
   itens:[
     "Google Ads, contas B2B em leitura",
     "Google Ads, VR09 ZAP+ MCC VivaReal (526-656-0190): convite enviado, falta a V4 aceitar",
     "GA4, propriedades dos domínios B2B, nível analista",
     "Google Tag Manager, contêineres publicados",
     "Google Search Console de cada propriedade B2B"
   ],
   n:"Uma liberação por produto, mas tudo sob a mesma conta gina@v4company.com. Alimenta as auditorias (ii), (vi) e (vii), e os blocos G e H, os dois prioritários."},

  {o:"Meta", f:"Mídia, redes sociais", r:"Michelle Morais", p:"", s:"pendente",
   itens:[
     "Meta Ads, VR ZAP+ (612188193108418)",
     "Meta Ads, OLX | Autos | B2B (1742214902479721)",
     "Business Manager, acesso de parceiro",
     "Business Suite, nível analista"
   ],
   v:"verificado em 24/08: nenhuma das duas contas aparece na conta Meta conectada",
   n:"As duas contas de anúncio estão pendentes de aprovação do lado da OLX. Alimenta as auditorias (iv), (v) e (vi)."},

  {o:"Conta corporativa @olxbr.com", f:"Data room", r:"Michelle Morais", p:"", s:"pendente",
   itens:[
     "Contas para Rafael Corazza, Anselmo Bueno e Guilherme Monteiro",
     "Pasta do data room no Google Drive"
   ],
   v:"verificado em 24/08: a pasta do data room não abre com a conta Google conectada",
   n:"Chamado aberto pela Michelle. É pré-requisito da fase Identificar: o Drive restringe os arquivos a e-mail corporativo."},

  {o:"Salesforce", f:"CRM e pré-vendas", r:"", p:"", s:"pendente",
   itens:[
     "Marketing Cloud, visualização: jornadas, bases e métricas de e-mail",
     "CRM comercial, leitura: pipeline, estágios e motivos de perda"
   ],
   n:"Confirmar no kick-off se o CRM comercial também é Salesforce ou outra ferramenta. Alimenta as auditorias (i) e (ix), e o bloco J, prioritário."},

  {o:"Sales engagement e telefonia", f:"Pré-vendas", r:"", p:"", s:"pendente",
   itens:[
     "Plataforma de cadência e discagem",
     "Gravações de calls de qualificação, 10 a 15 recentes"
   ],
   n:"Auditoria (ix). As gravações envolvem consentimento e LGPD, então é a de prazo mais imprevisível."},

  {o:"Domínios B2B", f:"CRO, SEO e conversão", r:"", p:"", s:"pendente",
   itens:[
     "CMS dos domínios B2B",
     "Ferramenta de comportamento (Hotjar, Clarity ou similar)",
     "Ferramenta de SEO (SEMrush, Ahrefs ou similar)"
   ],
   n:"Auditorias (ii) e (viii). As duas ferramentas podem não existir: se não existirem, isso já é achado de maturidade."},

  {o:"Demais canais sociais", f:"Redes sociais", r:"", p:"", s:"pendente",
   itens:[
     "LinkedIn, páginas da empresa",
     "YouTube, TikTok e outros canais ativos"
   ],
   n:"Auditoria (v). Levantar no kick-off quais estão de fato ativos no B2B."},

  {o:"Dados internos", f:"Dados", r:"", p:"", s:"pendente",
   itens:[
     "BI ou fonte única de verdade",
     "ERP e financeiro: custo variável e margem"
   ],
   n:"Bloco A. Se não houver fonte única, isso já é sintoma da Trava de Cegueira."},

  {o:"V4MOS", f:"Dados", r:"Guilherme Monteiro", p:"", s:"parcial",
   itens:[
     "Workspace do Grupo OLX: credencial e organização",
     "Ingestão das contas de mídia no workspace"
   ],
   v:"verificado em 24/08: autenticação OK nos seis endpoints, com secret inválido devolvendo 401 e organização inexistente devolvendo 403",
   n:"O acesso funciona, mas o workspace não tem nenhum dado de mídia ingerido, o que depende das contas Google e Meta. Ver PENDENCIAS 11."}
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
  var c = {concedido: 0, parcial: 0, pendente: 0, inexistente: 0, total: l.length, itens: 0};
  l.forEach(function (x) {
    c[x.s] = (c[x.s] || 0) + 1;
    c.itens += (x.itens || []).length;
  });
  c.faltando = c.pendente + c.parcial;
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
