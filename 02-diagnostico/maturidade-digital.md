# Maturidade Digital · Grupo OLX

**POP 7 · Análise Diagnóstica · Ciclo 1**

> Produzido em **04/09/2026**, com a evidência disponível **antes** do desbloqueio de acesso
> previsto para 08/09. É leitura parcial e datada: o que está `null` está `null` por falta de dado,
> não por omissão, [regra 1 do repositório](../CLAUDE.md).
>
> Par de máquina: [`dados/outputs/dre-maturidade-digital.json`](../dados/outputs/dre-maturidade-digital.json)


---

> O POP é explícito: avaliação baseada em **evidências objetivas e práticas reais, não discurso**.
> Um grupo do porte da OLX parece maduro no discurso; o que segue pontua pelo que a ferramenta mostra.

| Dimensão | Nível |
|---|---|
| **Canais Digitais** | 2 · 2 · Em estruturação (provisório: apurado sobre 6 contêineres de GTM, de 11 exports, em 2 das 4 contas do grupo; exports de workspace, não confirmados em produção) |
| **Processos e Automação** | 2 · 2 · Em estruturação (provisório: mesmo perímetro, 6 contêineres, exports de workspace) |
| **Uso de Dados e Inteligência** | 2 · 2 · Em estruturação (provisório: a nota depende de dois artefatos que a V4 nunca viu, o BI de funil B2B e os exports de duas contas inteiras de GTM) |

---

## Leitura sistêmica

**Veredito: nível 2 · Em estruturação, nas três dimensões, em caráter provisório e com perímetro
declarado.**

O perímetro é parte da nota, não rodapé: 6 contêineres de GTM auditados, de 11 exports, em 2 das 4
contas do grupo; 5 exports já no repositório e não lidos (Buyer Journey 124 tags, VAS 48, Unbounce
40, Login 5, Wallet 3); duas contas inteiras, `Checkout Unificado - PRO` (`6326134112`) e
`VivaReal` (`4412254379`), com zero contêineres recebidos; e todos os exports são de *workspace*,
não de versão publicada. O "22+ contêineres" é piso de **uma** conta (PENDENCIAS 17).

**A régua do POP 7 é classificação por dimensão, não média.** As três dimensões coincidem em 2 por
caminhos diferentes, e a coincidência esconde a dispersão interna. Como o escopo contratado é B2B,
a nota de registro é a do perímetro B2B; o que se observa do lado consumidor entra como contexto e
não é somado nem promediado. Nenhum número da escala 1–4 deve circular fora dessas três dimensões.

**A hipótese de estratificação, "madura no consumidor, imatura no B2B", não se sustenta e foi
abandonada.** As fontes do próprio repositório a refutam: a medição do anunciante profissional
**não** roda em tier gratuito nem sem evento-chave, ela cai em `OLX App + Web`, tier 360, com
`begin_checkout` e `purchase` marcados como chave (auditoria (vii), achado 1 e box "Onde o dado
cai"; PENDENCIAS 16). E o lado consumidor carrega defeitos próprios e graves (`session_start` como
conversão, UA vivo, gatilho escutando evento inexistente, dupla contagem de conversão de
`ad_insertion`). A propriedade gratuita, `GA4 Grupo OLX`, é a que **não recebe de nenhum contêiner
auditado**: é sinal de propriedade órfã e de mapa errado no onboarding. Se a estratificação for
retomada algum dia, será como hipótese, e o que a testaria é uma varredura equivalente do lado
consumidor, que não foi feita.

**Isso confirma a pré-condição, não a restrição.** Pelo método, Cegueira é pré-condição e não
restrição de receita (00-playbook/02-travas-de-receita.md §3). A leitura de maturidade diz que a
pré-condição não está atendida no escopo B2B: com os achados 1 e 3 confirmados no export, e o 4 e
o 5 ainda condicionais, o funil B2B derivável do GA4 tem conversão contaminada e numerador
inexistente. A regra 8, receita derivada do funil bate com a declarada, tolerância 5%, não é
executável hoje, e não passa a ser só corrigindo os achados: falta o Bloco A inteiro (A1–A3, zero
itens recebidos), que é entrega de dado e não concessão de acesso. A regra 3 fica intacta:
maturidade é avaliação paralela, não uma segunda restrição concorrendo com a que a CRT vai
determinar.

**A causa-raiz é hipótese, com uma fonte, e está escrita no formato exigido.** *A empresa opera
sob a política implícita de que a medição é responsabilidade de quem implementa cada superfície, e
não de quem responde pela receita, o que gera convenções e regimes divergentes entre contêineres,
duas grafias do mesmo conceito em `GTM-KGFGVFC` e dois regimes opostos de consentimento entre o
Master e `GTM-PZ733B5`, limitando a capacidade de saber se o número que sai corresponde ao
negócio.* Três ressalvas viajam com ela. Primeira: a fonte é uma só, a auditoria (vii), sobre um
único corpo de export, lido num único dia. Não há três evidências independentes; ler o mesmo
export por três ângulos não são três confirmações, e a evidência de Canais (a prospecção fora do
diagrama) é propriedade de um slide feito pelo time comercial, não de uma superfície implementada,
não decorre da política nem a testa. Segunda: a política nunca foi observada. Não há
organograma, RACI, nem pergunta feita sobre quem responde pela medição de cada superfície; o
acesso ao GA4 é Leitor e nenhuma tela de Administração abre. **A pergunta que converteria a
inferência em evidência, "quem responde pela medição de cada superfície, e quem confere se o
número bate com o negócio?", não tem DRI nem prazo em PENDENCIAS.md.** Terceira: a validação
final é da CRT (POP 14), como manda o playbook. Nenhuma dessas leituras é falha de pessoa.

**Ressalvas que precisam viajar com esta nota para qualquer material de comitê.** (1) Nada aqui
está confirmado como estando no ar: exports de workspace, sem o print da aba Versões (item 1.7 da
coleta, `[ ]`, com `assets/originais/H-rastreamento-gtm/telas/` vazia). (2) A cobertura é menor do
que parece, ver perímetro acima; como o nome `Checkout Unificado - PRO` junta as duas palavras do
escopo contratado, é possível que a medição B2B correta viva ali e que o contêiner auditado seja o
legado; se for, Uso de Dados sobe. Isso é leitura de nomenclatura, a mesma armadilha da pendência
12. (3) Dois achados centrais seguem **condicionais** e assim devem ser apresentados:
`seller_category` só fica vazio se o site não gravar `user_olx` por código próprio (achado 4), e
não se sabe se o Braze pausado é implantação em espera ou projeto abandonado (achado 14). (4) A
régua efetiva da operação B2B pode não ser o GA4: os dashboards de funil que a Lu Machim mostrou
em 28/08 são um BI que a V4 ainda não viu (links = lacuna 1 da ata, sem prazo). **Enquanto o BI
não for aberto, a maturidade de Uso de Dados não pode ser fechada.**

**Consequência prática.** Esta avaliação não deve ser apresentada como nota de desempenho da OLX.
Deve ser apresentada como o mapa do que precisa ser destravado antes de qualquer número entrar em
forecast, e como o argumento concreto do pedido: não se pede acesso genérico, pedem-se os exports
de duas contas nomeadas, o mapa propriedade × measurement ID × superfície, a lista completa de
eventos-chave, os links dos dashboards, e o Bloco A. Registre-se, por fim, que este POP se apoia
num repositório com quatro inconsistências abertas que precisam ser corrigidas na fonte antes do
Comitê 1: o achado 12 da auditoria (vii) localiza a tag 364 no Master, e ela está em `GTM-
KGFGVFC`; o achado 14 conta quatorze tags do Braze, e o export devolve 22 pausadas mais 4 ativas;
o checklist H4 conclui "sem contêiner server-side" quando existe endpoint server-side declarado no
parque; e `dados/client.json` está uma rodada atrás do documento humano, além de registrar uma
conta de GTM quando o repositório já mapeou quatro.

### O paradoxo

**A OLX mede muito e não consegue dizer se o número corresponde ao negócio.**

Não é o paradoxo de quem comprou ferramenta e não usa. As quatro contas de GTM do grupo têm selo
360 (PENDENCIAS 17; coleta-pendente.md); das cinco propriedades de GA4 cujo tier foi lido, quatro
estão em `GOOGLE_ANALYTICS_360` (client.json, `ga4.service_level`); os 11 exports somam 367 tags,
295 gatilhos e 668 variáveis (assets/originais/README.md, bloco H); a propriedade onde a medição
B2B efetivamente cai, `OLX App + Web`, `152644854`, tem 219 nomes de evento, tier 360, e tem
`begin_checkout` e `purchase` **marcados como evento-chave** (auditoria (vii), box "Onde o dado
cai" e achado 1). Existe ainda um endpoint server-side declarado no parque, `https://gtm-server-
side.track.olx.com.br`, configurado em 19/09/2025 num contêiner que ninguém leu. E há uso de
indicador na operação: dashboards de funil B2B com MQL, SQL, vendas, taxa de qualificação e
conversão, cortados por vertical, canal e time, sobre 12 meses, processados em batch diário às 3h
(Lu Machim, 00:05:42–00:08:59).

O defeito não é ausência de medição. É **configuração**. Na superfície de receita B2B, o
`purchase` do GA4 é disparado pelo gatilho de `begin_checkout` (achado 1); `lead_b2b` registra
zero evento em agosto com a tag montada e ativa (achado 3); a chave que separaria anunciante
profissional de particular depende de uma tag pausada, e isso ainda é condicional, porque ninguém
verificou se o site grava `user_olx` por código próprio (achado 4, "a confirmar"); os parâmetros
de item são lidos sem índice de array, com consequência provável de `purchase` sem valor, não
confirmada no Preview (achado 5). No lado consumidor os defeitos são de outra natureza e não
menores: `session_start` marcado como evento-chave em `GA4 VivaReal`, 13,27 mi/mês; Universal
Analytics disparando dois anos depois da desativação; um gatilho escutando `ads_remove`, evento
que não existe, contra 157.632 `ad_remove` reais. **Os defeitos atravessam as duas superfícies.**
O que distingue o perímetro contratado é que ali eles atingem exatamente o funil que o projeto
precisa derivar.

O irmão operacional do descompasso: **parte da automação foi montada e não foi ligada, mas não
toda, e a exceção importa.** Vinte e duas tags do Braze estão pausadas nos três contêineres da
conta `94905`, e quatro estão **ativas** em `GTM-PZ733B5`, do lado Imóveis (contagem direta sobre
os exports). Noventa e três das 367 tags do parque estão pausadas, e parte disso é higiene:
conferi seis casos em `GTM-PZ733B5` que são consolidação bem executada, com o gatilho absorvido
pela tag ativa equivalente. Ninguém na OLX declarou qual pausa é qual, e é essa indefinição, não
o percentual, que é o achado.

E há o contraste que a auditoria usa como prova de política, e que **não sustenta esse peso**. Em
`GTM-PZ733B5` seis tags do funil comercial foram unificadas em três com cobertura preservada; em
`GTM-KGFGVFC` a mesma classe de operação produziu o achado 1. Só que os exports datam as duas
coisas: as tags da consolidação impecável têm fingerprint de 21/10/2025 e a `426 [TAG] GA4 -
Purchase`, que produziu o achado 1, é de 11/02/2025, oito meses antes, **e em outra conta de
GTM** (`2971905372` contra `94905`). No par de View Promotion é o mesmo: a versão com teste de
nulo é de 31/07/2024, em `GTM-KGFGVFC`, e a que quebra é de 06/11/2024, em `GTM-MJX9PG4`, dois
contêineres **irmãos**, e a defeituosa é a **posterior**. A leitura banal, prática que melhorou
com o tempo, contêineres de eras e contas diferentes, não foi excluída. O que se pode afirmar é o
mínimo: **a capacidade de fazer certo existe na casa e não está distribuída por igual. Se isso
decorre de política ou de cronologia é hipótese a testar na CRT, não conclusão desta avaliação.**

---

## Canais Digitais

**Nível 2 · 2 · Em estruturação (provisório: apurado sobre 6 contêineres de GTM, de 11 exports, em 2 das 4 contas do grupo; exports de workspace, não confirmados em produção)**

### O que sustenta

- Parque de canais amplo e ativo, com peso declarado por canal: CRM 29% · Direto 36% · Pago 16% ·
Orgânico 5% · Outros 11% [D], anotação transcrita do slide FLUXOS apresentado em 28/08,
registrada em 02-diagnostico/lacunas-do-fluxo-de-receita.md §1. As barras medem mix de MQL por
canal (L7). O arquivo-fonte não está versionado (L28): a citação ainda não é evidência formal no
sentido da regra 5.
- Quatro canais de entrada com peso declarado: WhatsApp 42 · Formulário 44 · Telefone 3 · Outros 8
[D] (mesma fonte, mesma ressalva). A aritmética fecha em 97% por dois caminhos independentes, a
conferência é da V4 (lacunas §1), não número do cliente; faltam 3 pontos (L29).
- Canal online transacional existe e vende: 25% da receita de Autos e 10% da de Imóveis [D],
02-diagnostico/jornada-do-cliente-profissional.md, etapa 2 (Carolina Dallolio, 00:12:41).
- Áreas logadas operando como canal próprio de expansão: Canal Pro (Imóveis) e MyPlan (Autos), mais
eventos/trade [D], Michelle Morais, 00:35:02 e 00:36:13 (L11, L12). Michelle descreve o Canal Pro
originando upgrade: "A pessoa entra lá para ver o plano dela, ela clica lá e é direcionada para
fazer um upgrade" (transcrição de 28/08, linha 797).
- Superfície de captação de anunciante Imóveis montada e efetivamente lida: `GTM-PZ733B5` (5.
ZapImóveis - Container ANUNCIE), 48 tags, 9 pausadas, assets/originais/README.md bloco H, e
auditado na segunda rodada de 02/09 (auditoria (vii), achados 18–21).
- Mídia paga em pelo menos cinco plataformas, contadas diretamente nos exports versionados de
assets/originais/H-rastreamento-gtm/ (6 contêineres auditados): Google Ads, 4 IDs de conversão
distintos (`AW-10947843670` em GTM-MJX9PG4; `963385983` em GTM-MXQKDG3; `AW-791128603` e
`AW-10779204119` em GTM-PZ733B5); Meta, 5 pixels distintos (`592658194155317` em MXQKDG3;
`818079879779548` e `935989184453347` em MJX9PG4; `328237602412769` e `191084528414847` em
PZ733B5); TikTok `CO25OBRC77U47AMPJES0`; Floodlight advertiser `14127847`; e **Kwai**
`266675679118322` (tag 344 `[PXL] Kwai - Base Code`, GTM-PZ733B5, ativa). A auditoria (vii),
achado 17, nomeia só 3 pixels e 2 IDs de Google Ads, o restante é contagem direta sobre o export.
- App com adoção declarada assimétrica: "na casa dos 70, 60% que usa OLX autos aplicativo" contra
"20% só usa o app, eh, 30%" em Zap/Viva [D], Leonardo Costa, 00:38:26 (L25). Citado na faixa como
o falante disse.
- Automação de canal existente e não trivial: a tag `448 [TAG] Mensagens Dinâmicas WhatsApp`
personaliza a mensagem conforme o canal de origem, lendo os cookies `sf_utm_*`. Está em **`GTM-
KGFGVFC`**, não no Master (conferido no export `gtm-kgfgvfc_workspace131.json`; auditoria (vii),
achado 15).

### O que contradiz

- Um caminho de entrada que responde por 50% [D] não está desenhado no mapa de canais. A unidade
está em disputa: Carolina Dallolio diz "50% da base que chega por prospecção comercial"
(transcrição de 28/08, linha 337, 00:05:42) e o slide da jornada diz "50% da receita nasce da
prospecção comercial" (jornada-do-cliente-profissional.md, etapa 1, ambiguidade 5). Nenhum dos
dois é comparável ao mix de canais, que mede MQL, por isso a prospecção **não pode ser ordenada**
contra WhatsApp ou Formulário. A lacuna é a ausência do caminho no mapa (L1), não o seu tamanho
relativo.
- O maior canal do mapa é artefato de mensuração. Anotação do próprio cliente no slide FLUXOS:
"teste de campanha paga para WhatsApp: entra tudo como Direto" e "perde atribuição: entra tudo
como Direto" (lacunas §2). Direto (36%) está inflado e Pago (16%) subestimado, o quanto não está
dimensionado (L15/F12, DRI a definir, sem prazo).
- A superfície digital origina expansão mas não a transaciona: "a gente não tem upgrade, por
exemplo, self service hoje", Leonardo Costa, transcrição de 28/08, linha 909, bloco **00:39:34**
[D]. Todo up, down e cancelamento passa pelo time comercial (slide etapa 2, Carolina 00:12:41).
(L22 no caderno de lacunas atribui a fala a Michelle em 00:41:15; a transcrição não sustenta nem o
falante nem o minuto, corrigir L22.)
- O canal online só vende planos de anúncio, "Canal online (só planos de anúncios)", redação
literal de 02-diagnostico/jornada-do-cliente-profissional.md, etapa 2. A superfície digital não
cobre o portfólio.
- O handoff para WhatsApp, provável ponto de passagem do lead B2B ao comercial, não emite nenhum
evento de GA4 ao acontecer (auditoria (vii), achado 15). O canal de maior peso de entrada
declarado é invisível na medição.
- A OLX confirma que não há incentivo à adoção do app no B2B: Michelle Morais, "Não é incentivado
hoje", e Leonardo Costa, "para B2B", transcrição de 28/08, linhas 965–971, bloco **00:40:31** [D]
(L25). A hipótese foi levantada por Gustavo Figueiredo, que é Sócio & COO da **V4**
(dados/client.json, `stakeholders.sponsor_v4`), e por isso não entra como evidência sobre o
cliente.
- Três plataformas de relacionamento comprovadas no código e uma quarta indicada apenas por nome de
contêiner: Salesforce Marketing Cloud (a única prevista no contrato), **Insider** (`10007563`,
ativa), **Braze**, pausado nos três contêineres da conta `94905` e **ativo** em `GTM-PZ733B5`
(tags 434, 439, 441, 442, `paused: false`, conferido no export, o achado 18 da auditoria também
registra o Braze entre o que dispara ali), e **RD Station**, cuja única evidência é o nome do
contêiner `OLX - RD Station | LP` (`GTM-MVQWQJFB`, host `materiais.olx.com.br`), sem export e sem
nenhuma tag vista. O bloco B do checklist foi desenhado para uma ferramenta e o GTM mostrou
quatro. **Qual é a oficial e o que as outras fazem é pergunta ainda não feita**, a nota do bloco
B termina em "Perguntar", e não há linha em PENDENCIAS.md com DRI e prazo.
- As propriedades GA4 nominalmente B2B do onboarding não têm tráfego: `OLX PRO` (382768600) registra
119 sessões em três meses, só direto, e `OLX Pro Landing` (382776122) registra zero evento no
período (PENDENCIAS 13). São propriedades órfãs ou desligadas, e não se sabe qual.
- Na superfície de captação de anunciante Imóveis a ferramenta de comportamento está desligada:
`[TAG] Mouseflow` (id `139`) em `GTM-PZ733B5` está pausada, com projeto diferente do Master
(auditoria (vii), achado 21; fingerprint 08/01/2026 no export).
- O arquivo original do slide FLUXOS não está no repositório (L28), `find -iname "*fluxos*"` não
retorna nada, e `assets/originais/A-visao-de-negocio-e-fluxo-de-receita/` contém um único arquivo,
`jornada-do-cliente-profissional.png`. Todo o mix de canais existe em prosa de anotação de
reunião, sem fonte conferível.

### O que falta para subir de nível

Para sustentar nível 3 ("canais claros e integrados") seria preciso (a) o desenho da prospecção
ativa dentro do mapa de canais, com etapas próprias (L1); (b) dimensionar a mídia paga que cai em
Direto (L15/F12), sem isso o mix de 5 canais é estimativa, não mapa; (c) a resposta a qual das
quatro plataformas de relacionamento é a oficial, pergunta ainda não formulada à OLX; (d) o
arquivo-fonte do slide FLUXOS versionado (L28), sem o qual nenhum percentual de canal é evidência
formal. Nada disso tem DRI nem prazo em PENDENCIAS.md hoje. Fora do rol de evidências, e
registrado aqui: as 247.694 sessões atribuídas a "AI Assistant" no VivaReal em jun–ago/2026
(dados/client.json, achados preliminares) **não podem ser usadas**, o próprio campo instrui que
"nenhum número acima foi usado ainda em diagnóstico. São leituras de verificação de acesso"
(`ga4.nota`, coleta de 31/08), a propriedade é de consumidor e a auditoria (iii) GEO só começa em
21–23/09 (auditorias-contratadas.md).

---

## Processos e Automação

**Nível 2 · 2 · Em estruturação (provisório: mesmo perímetro, 6 contêineres, exports de workspace)**

### O que sustenta

- Qualificação automatizada em produção e recém-melhorada [D]: Michelle Morais, 00:44:38, o fluxo
de qualificação "agora tá automatizado com o time", e o histórico de cliente inativo é
reaproveitado (L10). Declaração em reunião, não verificada no produto.
- MQL e SQL têm definição declarada e critério objetivo de elegibilidade [D]: MQL = nome, e-mail,
telefone e em alguns canais documento; SQL = lead elegível, exige CNPJ do setor (em Imóveis só se
vende para imobiliária e corretor), **Carolina Dallolio, 00:46:02**, respondendo à pergunta de
Rafael Corazza (V4) feita no fim do bloco 00:44:38. Fecha o bloco 04 do formulário de kick-off.
(L10 cita "Carolina e Michelle, 00:44:38", corrigir o minuto no caderno.)
- Dashboards de funil B2B existem e são operados [D]: MQL, SQL, vendas, taxa de qualificação e
conversão, com filtro por vertical, pelos cinco canais, por time comercial e por período;
histórico padrão de 12 meses; **base processada em batch diário, no horário das 3h**, Lu Machim,
00:05:42–00:08:59 ("como são 3 horas, gente, é o momento que roda e processa os dados de
marketing"; "as nossas bases elas rodam as 3 horas"), registrado como "processamento diário às 3h"
em 06-reunioes/2026-08-28-jornada-do-cliente.md linha 157 e como "processados às 3h" em lacunas
§06. É latência D-1, não dado quase em tempo real. A V4 ainda não viu os dashboards: os links são
a lacuna 1 da ata, sem prazo acordado (L6).
- A casa sabe fazer consolidação de tag corretamente: em `GTM-PZ733B5`, seis tags do funil comercial
foram unificadas em três, com as antigas pausadas e cada gatilho absorvido pela ativa equivalente
(`purchase Privado` 227→317; `add_to_cart` 243/267/303→258; `begin_checkout` 248/256→308),
auditoria (vii), seção Contraponto, conferida gatilho por gatilho. As nove tags têm fingerprint de
21/10/2025 no export.
- Mudança estrutural de jornada declarada como **em curso**, não concluída: "a gente acabou de mudar
essa jornada porque antes a pessoa podia fazer login na plataforma antes de pagar o boleto e agora
não" **e**, na mesma fala, "Então, a gente tá mudando essa jornada" [D], Leonardo Costa,
00:26:33, transcrição de 28/08 linha 689 (L2). Não verificada no produto.
- Automação de atribuição client-side deliberada e documentada em código: tag `162 [TAG] Settings -
UTM Cookies` no Container Master grava `sf_utm_*` em `.olx.com.br`, last-click não-direto, janela
de 90 dias, com o comentário do próprio autor "Atribuição client-side. Não substitui dados do
GA4." (auditoria (vii), achado 15; tag 162 conferida no export `gtm-546n2jv_workspace206.json`).
- Existe arquitetura de carregamento centralizada: o Container Master (`GTM-546N2JV`, 13 tags) serve
os 5 domínios B2B por zonas e é por essas zonas que se descobriram os contêineres filhos `GTM-
PZ733B5`, `GTM-5WWRGTQ`, `GTM-KP8QMDH`, `GTM-T2H3VFL` e `GTM-PWP7Z4C` (auditoria (vii), achado
17).

### O que contradiz

- 93 das 367 tags do parque exportado estão pausadas (25,3%), assets/originais/README.md, bloco H.
**Isso não é, por si, degradação**: conferi 6 casos em `GTM-PZ733B5` que são consolidação correta,
com cobertura preservada. Outra parte é automação nunca ligada. O repositório não sabe a proporção
e ninguém na OLX declarou qual é qual, essa é a lacuna, não o percentual.
- Automação de CRM montada e não ligada na conta principal: contagem direta sobre os exports
(critério: tags cujo nome começa por `[TAG] Braze -`) devolve **22 tags do Braze pausadas** nos
três contêineres da conta `94905`, Master 3 (214, 228, 229), `GTM-KGFGVFC` 7 (433, 435, 437, 439,
443, 444, 445) e `GTM-MXQKDG3` 12 (523–550), cobrindo inicialização, page view, begin checkout,
purchase e ad insertion/edition/remove. **Mas em `GTM-PZ733B5` quatro tags do Braze estão ativas**
(434, 439, 441, 442). Logo, não se pode dizer que "a instrumentação de CRM inteira não entrou em
operação": ela opera do lado Imóveis e está desligada do lado OLX. O achado 14 da auditoria pede
exatamente a pergunta que ninguém fez, "implantação em espera ou projeto abandonado?". ⚠️ O
achado 14 registra "quatorze tags"; a contagem sobre o export devolve 22 pausadas + 4 ativas.
**Reconciliar a divergência antes do comitê**: a auditoria (vii) precisa ser corrigida ou o
critério de contagem explicitado.
- A mesma correção existe num contêiner e não no outro, mas a geografia e a cronologia não são as
que a auditoria conta. A tag `364 [TAG] DataLayer - View Promotion`, que testa nulo (`links[i] &&
links[i].getAttribute("href") &&`), está em **`GTM-KGFGVFC`** e **não no Master**, o export
`gtm-546n2jv_workspace206.json` tem 13 tags (ids 27, 57, 153, 158, 162, 164, 171, 180, 205, 208,
214, 228, 229) e não contém a 364. A tag `54`, que quebra em qualquer `<a>` sem `href`, está em
`GTM-MJX9PG4`. Os dois são **contêineres irmãos** carregados por zonas do Master, não pai e filho.
E os fingerprints invertem a narrativa: a corrigida é de **31/07/2024** e a defeituosa de
**06/11/2024**: a tag nova foi escrita sem o cuidado que já existia em outro contêiner, o que é
diferente de uma correção que deixou de ser propagada. **O erro nasce no achado 12 da auditoria
(vii) e precisa ser corrigido lá, senão volta.**
- Não existe plano de mensuração nem taxonomia documentada. O item H3 do checklist registra: não
recebido, a taxonomia teve de ser reconstruída a partir do export. Sem documento de referência,
não há processo repetível contra o qual comparar a implementação.
- A taxonomia praticada tem duas grafias para o mesmo conceito em `GTM-KGFGVFC`: `plano-
profissional` (gatilhos 306 e 434) contra `planos-profissionais` (436 e 441), achado 9. **Nenhum
dos quatro gatilhos alimenta hoje uma tag ativa**: conferi no export `gtm-
kgfgvfc_workspace131.json` que o 306 não é usado por tag nenhuma (a própria auditoria diz isso no
achado 1), o 434 dispara só as tags 435 e 439 (Braze, pausadas), o 436 só a 437 (pausada) e o 441
só a 445 (pausada). A divergência vive inteiramente na camada Braze desligada, e precisa ser
resolvida antes da correção do achado 1, porque o 306 é o gatilho de destino.
- Um gatilho ativo escuta um nome de evento que não existe: gatilho `377` de `GTM-MXQKDG3` escuta
`ads_remove`; o evento real é `ad_remove`, com 157.632 ocorrências em agosto e `ads_remove` em
zero (achado 8). A tag web de remoção de anúncio nunca dispara, e a origem dos 157 mil não foi
apurada.
- Código de depuração e erro de JavaScript em produção: `console.log(el)` na tag `349` de `GTM-
KGFGVFC`, disparando a cada clique; e a tag `405` usa `search.searchParams` com `search` fora de
escopo, quebrando exatamente no tráfego Intercom que ela existe para medir (achados 3 e 12).
- Universal Analytics ainda instalado e disparando dois anos após a desativação da plataforma
(`UA-70177409-2`, em `GTM-KGFGVFC` e `GTM-MJX9PG4`), e em Conecta Autos as visualizações de seção
existem só na propriedade morta, com a equivalente GA4 pausada (achado 6). Não há rotina de
manutenção do parque.
- Sobre tagueamento server-side, o repositório afirma mais do que apurou e menos do que o export
mostra. O checklist H4 conclui "sem contêiner server-side", mas a verificação é de 01/09, sobre os
**5** contêineres da primeira rodada, `GTM-PZ733B5`, auditado em 02/09, não foi coberto e o
checklist não foi reescrito. Verifiquei os 11 exports por `server_container_url`/`transport_url`:
nenhum dos 6 contêineres auditados envia para contêiner server-side, **mas existe um endpoint
declarado no parque**, a variável `1259 [VAR] ServerSideTaggingConfig` de `GTM-TNX8FDS` (Buyer
Journey, export no repositório, marcado "⚪ pendente / não lido") aponta para `https://gtm-server-
side.track.olx.com.br`, com fingerprint de **19/09/2025**, e nenhuma tag daquele contêiner a
referencia. Ou seja: a OLX tem infraestrutura server-side declarada e não em uso naquele export.
**Corrigir H4 e a frase "não há tagueamento server-side" antes de qualquer comitê.**
- No lado Imóveis o processo de consentimento não roda: as duas tags de inicialização do AdOpt (338
e 340) estão pausadas em `GTM-PZ733B5` enquanto 17 tags do contêiner declaram `consentSettings:
NEEDED` (achado 18). No Master, o mesmo processo roda concedendo tudo por padrão, com o botão de
recusa oculto por CSS e o injetor com 4s de atraso (achado 2). Dois defeitos distintos, na mesma
obrigação de LGPD, em dois lados do grupo.
- Alavanca de processo reconhecida e não usada: metade da base paga por boleto, ~40% cartão e o
restante Pix, **sem nenhuma diferenciação de preço por meio de pagamento**, "a gente sabe que
deveria, mas hoje não" [D] (Carolina Dallolio, **00:21:16**, L20). Separadamente e em outra fala:
o **esquecimento** responde por 20% dos atrasos, "mas não do churn" [D] (Carolina, **00:22:16**,
L19). **A fração de atraso atribuível ao boleto não está medida em fonte nenhuma**, L19 existe
justamente para impedir essa conflação.
- O investimento de mídia não está no dashboard de funil, vive num controle mantido fora dele, na
área de mídia: "isso é outro controle que a gente tem" (Mirella Mendonça, 00:10:08, L9). É falha
de integração entre dois controles, não de pessoa. Sem essa integração, não há CAC por canal.

### O que falta para subir de nível

Para nível 3 ("processos documentados e repetíveis") falta o que o próprio checklist marca como
não recebido: plano de mensuração e taxonomia de eventos (H3), sem o qual não existe padrão contra
o qual conferir implementação. Falta rotina de manutenção, nada explica UA vivo dois anos depois,
25% do parque pausado sem classificação, e a mesma verificação de nulo presente num contêiner e
ausente num irmão. E falta confirmação do que está no ar: os 11 exports são de *workspace*
(`workspace392`, `workspace131`, `workspace206`…), não de versão publicada; nenhum achado foi
confrontado com produção; o print da aba Versões do `GTM-KGFGVFC` (item 1.7 da coleta) segue `[ ]`
e `assets/originais/H-rastreamento-gtm/telas/` está vazia, sem ele não se sabe desde quando o
`purchase` está preso ao gatilho de `begin_checkout`, ou seja, que janela do histórico de
conversão está contaminada.

---

## Uso de Dados e Inteligência

**Nível 2 · 2 · Em estruturação (provisório: a nota depende de dois artefatos que a V4 nunca viu, o BI de funil B2B e os exports de duas contas inteiras de GTM)**

### O que sustenta

- Capacidade instalada em tier pago, com o perímetro da leitura declarado: das **5** propriedades
cujo tier foi lido, 4 estão em `GOOGLE_ANALYTICS_360` (`GA4 VivaReal`, `GA4 ZapImóveis`, `OLX App
+ Web`, `Autos 360`) e 1 em `GOOGLE_ANALYTICS_STANDARD` (`GA4 Grupo OLX`), dados/client.json,
`ga4.service_level`, leitura de 01/09. O tier das outras 21 das 26 propriedades **não foi
apurado**. Em GTM, as **quatro** contas do grupo têm selo 360, fonte: PENDENCIAS 17 e
02-diagnostico/coleta-pendente.md, **não** `ga4.service_level` (que não contém dado de GTM) e
**não** `dados/client.json → gtm.conta`, que ainda registra uma só conta e está desatualizado.
- **A medição B2B existe e mora em propriedade paga com conversão declarada.** Os 5 contêineres da
primeira rodada escrevem em `G-50C013M2CC`, que é `OLX App + Web` (`152644854`), tier 360, 219
nomes de evento, box "Onde o dado cai" da auditoria (vii) e PENDENCIAS 16. E `begin_checkout`
(2.686.897) e `purchase` (565.258) estão "os dois marcados como evento-chave" (auditoria (vii),
achado 1; volumes também em client.json, `ga4.propriedade_da_medicao_b2b.volumes_agosto_2026`). O
diagnóstico correto não é "não medem", é "medem em outro lugar" (PENDENCIAS 16).
- Volume e granularidade de evento reais na propriedade da medição B2B, agosto/2026:
`qualified_lead_autos_pro` 4.680.465, `ad_insertion` 4.602.128, `ad_edition` 4.140.566,
`ad_remove` 157.632 (auditoria (vii), **achado 13**); `begin_checkout` 2.686.897 e `purchase`
565.258 (**achado 1** e client.json). ⚠️ **O que esses eventos medem não foi confirmado**, são
contagens de eventos com nome sugestivo, não leads apurados. Comparar 4,68 mi de "qualified leads"
profissionais por mês com as "414 vendas" que Leonardo Costa cita no canal online (00:11:03)
mostra que a leitura não pode ser oferecida a um Board sem essa ressalva.
- Onde há conversão definida no lado consumidor, ela é usada: `GA4 VivaReal` marca `generate_lead`
(830.116) e `generate_lead_pro` (661.144) em agosto (PENDENCIAS 13). ⚠️ PENDENCIAS 13 classifica
`generate_lead_pro` como "o primeiro indicador **possivelmente** B2B" e mantém aberta a ação 1,
"confirmar o que `generate_lead_pro` mede". Sem resposta, é evidência de que há conversão nomeada,
não de que ela mede o funil de anunciante.
- A operação lê o funil com corte e série [D]: taxa de qualificação (MQL→SQL) e conversão em vendas
(SQL→venda), por vertical, canal, time e período, sobre 12 meses de histórico, com processamento
diário às 3h, Lu Machim, 00:05:42–00:08:59 (L6). **Esse é o uso de indicador que sustenta o 2 e
não o 1** (ver `o_que_falta`).
- Proxy de entrega ao cliente formalizado em uma vertical [D]: "a proxy que a gente usa é três leads
em 7 dias para OLX", Leonardo Costa, transcrição de 28/08 linha 1159, bloco **00:53:50** (L26).
- Autoconsciência analítica registrada pelo próprio cliente: a anotação "perde atribuição: entra
tudo como Direto" vem do slide FLUXOS apresentado pela OLX em 28/08 [D]. **Não é evidência formal
no sentido da regra 5 enquanto o arquivo-fonte não estiver versionado (L28)**, vira, quando o
original entrar no repositório. Resolver L28 antes de qualquer score de trava, porque lacunas §2
já usa o termo "evidência formal" para sustentar nota acima de 3.
- Existe camada de gravação de sessão instalada e ativa: Mouseflow no Master (tag `27`, projeto
`b837e449-83ee-457f-9ef5-8f976953f2bc`), em todas as páginas web (checklist I4; tag conferida no
export, não pausada).

### O que contradiz

- Quatro propriedades não têm nenhum evento marcado como chave: `GA4 Grupo OLX` (2,47 mi de sessões
jun–ago), `Autos 360` (1,14 mi de sessões e 449 nomes de evento distintos), `ANAPRO` (11,19 mi de
`page_view`) e `OLX PRO` (PENDENCIAS 13). **Das quatro, só a `GA4 Grupo OLX` tem domínios
levantados**, e mesmo esses vêm de reconstrução da V4 no GA4, não de entrega da OLX: o checklist
C1 está 🟡 e termina em "Confirmar com a OLX antes de fixar o escopo: a leitura é de tráfego, não
de negócio". O pertencimento de `Autos 360`, `ANAPRO` e `OLX PRO` ao recorte contratado **não pode
ser afirmado** enquanto o mapa propriedade × measurement ID × superfície não for entregue
(PENDENCIAS 16). E `OLX PRO`, com 119 sessões em três meses, não é propriedade de alto volume: é
propriedade órfã.
- Onde a conversão foi declarada no lado consumidor, foi declarada errado: `GA4 VivaReal` marca
`session_start` como evento-chave, 13,27 mi em agosto (PENDENCIAS 13). Contamina toda taxa de
conversão relatada e, **se** importada no Google Ads, treina o Smart Bidding para comprar sessão.
Se está importada é a ação 2 da PENDENCIAS 13, sem resposta, é ela que decide a gravidade.
- A propriedade nominalmente B2B do onboarding é a única, entre as 5 lidas, no tier gratuito, `GA4
Grupo OLX` (`503925542`, `GOOGLE_ANALYTICS_STANDARD`), que carrega `ads.grupoolx.com.br`,
`imoveis.`, `autos.`, o institucional e `vender.olx.com.br`, **e não recebe de nenhum dos 6
contêineres auditados**. Isso é sinal de propriedade órfã e de mapa errado no onboarding, não
prova de subinvestimento no perímetro contratado: a medição B2B efetiva roda em propriedade 360. O
tier das outras 21 propriedades não foi apurado, e a frase "a única no tier gratuito" em
PENDENCIAS 13 precisa ganhar esse recorte.
- No perímetro B2B o funil derivável do GA4 está quebrado por configuração: `lead_b2b` = **0 eventos
em agosto** apesar da tag `429` estar montada e ativa, numerador inexistente (achado 3); e
`purchase` está pendurado no gatilho `215` de `begin_checkout`, conversão contaminada (achado 1).
**A parcela B2B contaminada dentro dos 565.258 `purchase` não foi isolada**: nenhum percentual de
contaminação pode ser afirmado.
- **Provavelmente** o denominador não é segmentável, e isso segue condicional: `seller_category`
fica vazio se `user_olx` não for gravado, a única tag do material exportado que grava essa chave
(tag `57`, Master) está pausada, e 8 propriedades de usuário a leem em três contêineres (achado
4). ⚠️ **A confirmar antes de comitê:** se o site grava `user_olx` por código próprio, fora do
GTM. "Se gravar, o problema não existe" (achado 4, e Ressalva de leitura 2 da auditoria). Não há
registro de verificação no site publicado nem de pergunta feita à OLX.
- Os parâmetros de item de e-commerce são lidos sem índice de array (`ecommerce.items.item_id`,
`.price`, `.quantity`), quando o próprio contêiner prova que a forma correta é conhecida (`[VAR]
E-commerce - Items` usa `ecommerce.items.0`), achado 5. Consequência provável: `purchase` sem
valor. **Não confirmada no Preview**, como o próprio documento exige.
- Duas fontes de verdade de atribuição operam ao mesmo tempo, com modelos e janelas diferentes: o
GA4 e os cookies `sf_utm_*` (last-click não-direto, 90 dias) alimentando o Salesforce, achado 15.
Toda divergência de números entre marketing e comercial provavelmente nasce aí.
- A medição B2B está espalhada por pelo menos três propriedades identificadas por engenharia reversa
dos contêineres (`G-50C013M2CC`, `G-6TV9FSHYVM`, `G-ZBYP2KJ7L9`) mais quatro Google Tags soltas
(`GT-K8GV5GMK`, `G-W39KX3CBHX`, `AW-791128603`, `AW-10779204119`), e o mapa propriedade ×
measurement ID × superfície nunca foi entregue (PENDENCIAS 16, achado 19).
- O mesmo lead é contado duas vezes em duas propriedades no lado Imóveis: o gatilho `[208] lead_dbm`
dispara `generate_lead` para `G-6TV9FSHYVM` (tag 209) e para `G-ZBYP2KJ7L9` (tag 356), achado 20.
Qual das duas é a de referência não foi confirmado, e sem isso `generate_lead` não serve de
numerador.
- A causa declarada do churn não é medida onde o churn dói: baixa performance é o principal motivo
de churn [D], performance é medida por proxy, e "a gente não tem um número mágico para real
estate", Leonardo Costa, 00:53:50 (L26).
- Nenhuma das seis taxas da jornada tem denominador, volume absoluto, período de apuração ou tempo
de passagem; quatro das seis vêm somadas sobre Autos e Imóveis, que têm modelos de anúncio e de
cobrança diferentes. Pelo POP, as seis etapas estão **narradas, não mapeadas**.
- O mesmo número circula em duas unidades sem que ninguém tenha decidido qual vale: o slide diz "50%
da receita" (jornada-do-cliente-profissional.md, etapa 1) e Carolina diz "50% da base" (00:05:42).
Receita e base não são o mesmo denominador, e o repositório carrega as duas versões em documentos
diferentes (ambiguidade 5, aberta).
- O churn de 8–10% [D] não tem unidade declarada (logo ou receita). O que está na fonte é que **o
net** foi lido em receita: "net negativo é em receita, as nossas entradas não estão compensando o
churn mais downgrade", Iuna Scheffler, kick-off de 24/08, **01:07:38**, sem nomear vertical. O
recorte por Imóveis vem da leitura da V4 em jornada-do-cliente-profissional.md §UDE #1, não da
fala. Ambiguidade 4, aberta.
- Não há CAC por canal: o investimento de mídia está fora do dashboard de funil (L9) e o canal
Direto está inflado por mídia paga sem atribuição (L15). Mesmo integrando os dois controles, o CAC
não fecha enquanto L15 não for dimensionada.
- O acesso concedido ao GA4 é **Leitor**, coerente com `can_edit=false` nas 26 propriedades. Nenhuma
tela de Administração abre, fluxos de dados, regras de evento, definições personalizadas,
retenção, filtros e consentimento (checklist H1/H4). Os cinco itens do Bloco 2 da coleta-pendente
(2.1 BigQuery, 2.2 retenção, 2.3 fluxos de dados, 2.4 lista completa de eventos-chave, 2.5
gerenciamento de acesso) seguem `[ ]`.
- O Bloco A do checklist (A1 receita 24 meses por linha de negócio, A2 funil com volumes e taxas
12–24 meses, A3 ticket médio/ciclo/CAC) segue com **zero itens recebidos**, todos ⚪. Não é
acesso, é entrega de dado, e sem ele a regra 8 do repositório não é executável nem depois de
corrigidos os achados 1, 3 e 4.

### O que falta para subir de nível

**Por que 2 e não 1.** O nível 1 da régua é "presença digital básica, processos informais, baixo
uso de dados" (00-playbook/02-travas-de-receita.md §7), e as contra-evidências do perímetro B2B
são compatíveis com ele. O que sustenta o 2 é uso de indicador demonstrado em tela: dashboards de
funil B2B com MQL, SQL, vendas, taxa de qualificação e conversão, cortados por vertical, pelos
cinco canais, por time comercial e por período, sobre 12 meses de histórico, com batch diário às
3h (Lu Machim, 00:05:42–00:08:59); MQL e SQL com definição declarada e critério de elegibilidade
(Carolina Dallolio, 00:46:02); e uma propriedade de GA4 em tier 360 com 219 nomes de evento e
evento-chave declarado. Isso não é ausência de dados: é dado usado reativamente, que é a definição
do nível 2.

**O que faria a nota mudar, com critério objetivo.** Sobe para 3 se, cumulativamente: (a) o Bloco
A (A1–A3) for entregue e a receita derivada do funil bater com a declarada dentro de 5% (regra 8);
(b) existir plano de mensuração/taxonomia documentado (H3) e o mapa propriedade × measurement ID ×
superfície (PENDENCIAS 16); (c) `lead_b2b`, `purchase` e `seller_category` forem corrigidos e
confirmados em produção. Desce para 1 se, ao abrir o BI, ficar demonstrado que os dashboards se
apoiam nas mesmas contagens contaminadas do GA4, hoje não se sabe, porque os links são a lacuna 1
da ata de 28/08, sem prazo acordado.

**O que falta materialmente:** a lista completa de eventos-chave da `OLX App + Web` (item 2.4 da
coleta, `[ ]`); o mapa propriedade × measurement ID (PENDENCIAS 16, não entregue); a confirmação
do que `generate_lead_pro` mede (ação 1 da PENDENCIAS 13, sem resposta); a resposta sobre qual
propriedade é a de referência para `generate_lead` no lado Imóveis (achado 20); a verificação de
`user_olx` (achado 4); a confirmação no Preview dos achados 5 e 11; e o Bloco A completo.
Registre-se ainda que o estado de máquina está uma rodada atrás do documento humano,
`gtm.export_recebido` em dados/client.json registra 5 contêineres, 5 críticos e 12 relevantes
quando o `.md` já traz 22 achados sobre 6 contêineres, e que o par obrigatório JSON+MD não existe
nem para a auditoria (vii) nem para o fluxo de receita: `dados/outputs/` contém apenas `meta-do-
projeto.json`.

---
