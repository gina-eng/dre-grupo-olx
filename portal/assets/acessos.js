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
  {o:"Google", f:"Mídia, rastreamento, SEO", r:"Michelle Morais", p:"", s:"parcial",
   itens:[
     "Google Ads, VR09 ZAP+ MCC VivaReal (526-656-0190): CONCEDIDO, aceite feito em gina@v4company.com",
     "Google Ads, demais contas B2B em leitura",
     "GA4, propriedades dos domínios B2B, nível analista",
     "Google Tag Manager, contêineres publicados",
     "Google Search Console de cada propriedade B2B"
   ],
   v:"verificado em 24/08: o V4MOS passou a devolver 655 registros de campanha do Google Ads, então a ingestão está funcionando",
   n:"O MCC entrou. Falta GA4, GTM e Search Console, que são o bloco H e o diagnóstico (vii), o prioritário. Atenção: as 8 campanhas visíveis têm sufixo pf e falam de aluguel e compra de imóvel, ou seja, parecem ser pessoa física, não o B2B do escopo. Confirmar no kick-off se a conta B2B é outra. Desde 24/08 existe conta de domínio OLX (rafael.corazza-ext@olxbr.com): GA4, GTM e Search Console passam a ser pedidos para ela. O aceite do MCC, que já saiu, continua em gina@v4company.com."},

  {o:"Meta", f:"Mídia, redes sociais", r:"Michelle Morais", p:"", s:"pendente",
   itens:[
     "Meta Ads, VR ZAP+ (612188193108418)",
     "Meta Ads, OLX | Autos | B2B (1742214902479721)",
     "Business Manager, acesso de parceiro",
     "Business Suite, nível analista"
   ],
   v:"verificado em 24/08: nenhuma das duas contas aparece na conta Meta conectada, e os seis endpoints do Facebook no V4MOS devolvem vazio",
   n:"As duas contas de anúncio seguem pendentes de aprovação do lado da OLX. É o que falta para fechar o diagnóstico (vi), já que o lado Google destravou. Alimenta também (iv) e (v). Se a aprovação continuar travada, testar pela conta de domínio OLX (rafael.corazza-ext@olxbr.com), que dispensa aprovação de parceiro externo."},

  {o:"Conta corporativa @olxbr.com", f:"Data room", r:"Michelle Morais", p:"", s:"parcial",
   itens:[
     "Conta de Rafael Corazza (rafael.corazza-ext@olxbr.com): CONCEDIDA, credenciais recebidas em 24/08 de ga-account@olxbr.com",
     "Conta para Anselmo Bueno",
     "Conta para Guilherme Monteiro",
     "Pasta do data room no Google Drive: ABERTA e testada em 24/08, primeiro lote baixado"
   ],
   v:"verificado em 24/08: o data room abriu com a conta nova e o primeiro lote foi baixado, 9 arquivos dos blocos E e I (457 MB). Índice em assets/originais/README.md.",
   n:"Decisão de 24/08: por enquanto a V4 opera pelo domínio OLX através desta única conta, compartilhada dentro do time. Isso destrava o data room e o que mais o Grupo OLX restringe a e-mail corporativo. Três consequências a tratar: trocar a senha no primeiro acesso e ligar 2FA, já que ela circulou por e-mail e por chat; seguir cobrando as contas de Anselmo Bueno e Guilherme Monteiro, porque login compartilhado não deixa rastro de quem leu o quê e enfraquece o controle de LGPD; e pedir todo acesso novo do lado da OLX para esta conta, não mais para gina@v4company.com. A senha não fica no repositório: gerenciador de senhas da V4. O data room deixou de ser bloqueio em 24/08: o primeiro lote entrou. O que sobra do bloqueio é a carga sobre uma pessoa só, porque só o Rafael tem login para ir buscar material novo lá."},

  {o:"Salesforce", f:"CRM e pré-vendas", r:"", p:"", s:"pendente",
   itens:[
     "Marketing Cloud, visualização: jornadas, bases e métricas de e-mail",
     "CRM comercial, leitura: pipeline, estágios e motivos de perda"
   ],
   n:"Confirmar no kick-off se o CRM comercial também é Salesforce ou outra ferramenta. Alimenta os diagnósticos (i) e (ix), e o bloco J, prioritário."},

  {o:"Sales engagement e telefonia", f:"Pré-vendas", r:"", p:"", s:"pendente",
   itens:[
     "Plataforma de cadência e discagem",
     "Gravações de calls de qualificação, 10 a 15 recentes"
   ],
   n:"Diagnóstico (ix). As gravações envolvem consentimento e LGPD, então é o de prazo mais imprevisível."},

  {o:"Domínios B2B", f:"CRO, SEO e conversão", r:"", p:"", s:"pendente",
   itens:[
     "CMS dos domínios B2B",
     "Ferramenta de comportamento (Hotjar, Clarity ou similar)",
     "Ferramenta de SEO (SEMrush, Ahrefs ou similar)"
   ],
   n:"Diagnósticos (ii) e (viii). As duas ferramentas podem não existir: se não existirem, isso já é achado de maturidade."},

  {o:"Demais canais sociais", f:"Redes sociais", r:"", p:"", s:"pendente",
   itens:[
     "LinkedIn, páginas da empresa",
     "YouTube, TikTok e outros canais ativos"
   ],
   n:"Diagnóstico (v). Levantar no kick-off quais estão de fato ativos no B2B."},

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
