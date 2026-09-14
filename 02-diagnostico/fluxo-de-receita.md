# Mapeamento do Fluxo de Receita · Grupo OLX

**POP 5 · Análise Diagnóstica · Ciclo 1**

> Produzido em **04/09/2026**, com a evidência disponível **antes** do desbloqueio de acesso
> previsto para 08/09. É leitura parcial e datada: o que está `null` está `null` por falta de dado,
> não por omissão, [regra 1 do repositório](../CLAUDE.md).
>
> Par de máquina: [`dados/outputs/dre-fluxo-receita.json`](../dados/outputs/dre-fluxo-receita.json)


---

## O que este mapa diz

O fluxo do anunciante profissional está narrado, não mapeado: zero das dez etapas tem volume, zero
tem tempo médio.

O fluxo de receita do anunciante profissional do Grupo OLX está narrado ponta a ponta em dez
etapas com fonte nomeada, mas não está mapeado: nenhuma das dez tem volume absoluto e nenhuma tem
tempo médio, então perda_absoluta é null nas dez e o ranking por perda absoluta que o POP exige é
indeterminável, ordenar por percentual violaria o próprio checklist da skill. Dos seis
percentuais declarados, apenas um (80% de pagamento da 1ª fatura) é taxa de passagem entre etapas;
os outros cinco são grandezas incomensuráveis somadas sob o mesmo rótulo. A regra 7 não pode ser
verificada por nenhum dos dois caminhos: pela via do cliente falta volume, ticket médio e receita
por vertical (bloco A do checklist, três itens em ⚪); pela via instrumentada o funil B2B do GA4
tem numerador zero (lead_b2b = 0 em agosto/2026), purchase contaminado e denominador provavelmente
não segmentável. Nenhuma trava recebe score aqui e nenhuma restrição é nomeada.

### Em números

| | |
|---|---|
| **0 de 10** | etapas com volume absoluto, perda_absoluta é null nas dez |
| **0 de 10** | etapas com tempo médio de passagem apurado |
| **1 de 6** | percentuais que são taxa de passagem: o 80% da 1ª fatura [D] |
| **null** | reconciliação da regra 7 bloqueada pelos dois caminhos |
| **89% · 8–10%** | [D] anúncios de Imóveis sem lead · churn mensal, unidade não declarada |
| **661.144** | generate_lead_pro: candidato a numerador, significado não confirmado |

### Os achados

1. RANKING IMPOSSÍVEL, E ISSO É O ACHADO. O POP manda ordenar por perda absoluta, não por percentual.
Sem volume em nenhuma das dez etapas, perda_absoluta é null nas dez e ranking_perda[] sai sem
ordem. Pior: quatro etapas (Exposição, Qualificação, Pós-pago Autos, Expansão) não têm sequer
taxa, e o pós-pago de Autos carrega 'alta taxa de abono e contestação', vazamento de magnitude
desconhecida que incide sobre receita JÁ RECONHECIDA e por isso não pode ser excluído do topo.
Declarar um máximo sobre esse conjunto seria somar um score com dimensão faltando.

2. AS 'SEIS TAXAS DO FUNIL' NÃO SÃO SEIS TAXAS. Só o 80% de pagamento da 1ª fatura é passagem
etapa→etapa. Os outros cinco são participação de origem (50%, denominador em disputa entre receita
e base), participação de receita por canal (25% Autos / 10% Imóveis), fatia de quem sai (12%),
participação de estado por anúncio (89%, só Imóveis) e hazard mensal sobre a base (8–10%). Somá-
los como placar de completude é mapa errado com aparência de mapa certo, e é o que
03-estrategia/meta-do-projeto.md §3 e 02-diagnostico/jornada-do-cliente-profissional.md fazem
hoje.

3. EMPATE TÉCNICO ENTRE CHURN E PAGAMENTO: a frase que ordenava as alavancas estava errada. Pela
identidade de regime, −1 p.p. de churn vale +14,3% a 8%, +12,5% a 9% e +11,1% a 10%; levar o
pagamento de 80% para 90% vale +12,5%. As duas empatam no ponto médio e o pagamento vence no topo
da faixa declarada. Todos [E]. A afirmação de que 'um ponto de churn vale mais que dez pontos de
conversão de pagamento' precisa ser corrigida em meta-do-projeto.md §4.1 e §9 antes de qualquer
material do Comitê 1.

4. A CADEIA ENTREGA-ZERO → CHURN É RELATO ÚNICO, NÃO CONVERGÊNCIA. O 89% (00:19:40) e a atribuição do
churn a baixa performance (00:22:16) são a MESMA falante na MESMA sessão, a dois minutos de
distância. O voto do kick-off é percepção da liderança, rotulada como tal pelo próprio
repositório, e a regra 5 não a admite como evidência. Não há corroboração instrumentada.
dados/client.json deve continuar com score null nas oito travas e restricao_identificada null.

5. O DESBLOQUEIO É EXTRAÇÃO, NÃO COLETA. As taxas MQL→SQL e SQL→venda já existem no dashboard de
funil B2B por vertical, canal, time e período, com 12 meses de histórico;
sessão→vitrine→checkout→venda existe no dashboard de canal online. A V4 viu os dois em
00:07:00–00:08:59 e não extraiu um dado, faltam os links (lacuna 1 da ata, DRI Leonardo Rosa,
prazo '-'). Junto vai a pergunta mais barata do projeto: o que generate_lead_pro mede.

---

## As dez etapas

Legenda de natureza: **apurado** = a V4 mediu · **declarado** `[D]` = o cliente afirmou e ninguém
conferiu · **inferido** = leitura da V4 sobre outro fato · **ausente** = não há dado.

### 1. Exposição e geração de demanda (mix de canais)

`declarado`  ·  travas: Cegueira, Exposicao

O contato do anunciante profissional nasce em cinco canais: CRM 29% · Direto 36% · Pago 16% ·
Orgânico 5% · Outros 11%, todos [D] · slide de FLUXOS NÃO VERSIONADO (L28), número que existe
apenas em prosa de anotação da V4 e não é conferível contra a fonte. Decomposições do mesmo slide,
com a mesma dupla marca [D]+não-versionado: CRM 29 = 27 (campanha→WhatsApp) + 2 (→LPs); Direto 36
= 26 (sem campanha) + 10 (→LPs); 26 = 15 WhatsApp + 3 Telefone + 8 Outros; canais de entrada
WhatsApp 42 + Telefone 3 + Outros 8 + Formulário 44; LPs MKT 41 = 2+10+16+5+1+7. 'Outros' inclui
Canal Pro (área logada de Imóveis), MyPlan (área logada de Autos) e eventos de trade (Michelle
Morais, 00:35:02). ACHADO: o próprio slide anota 'teste de campanha paga para WhatsApp: entra tudo
como Direto' e 'perde atribuição: entra tudo como Direto', o maior canal do mapa é, em parte,
artefato de mensuração. Logo Pago (16%) [D] está subestimado e CAC por canal não existe hoje.

PERDA (perda_absoluta = null): não dimensionada. A anotação de atribuição diz QUE o Direto está
inflado, não QUANTO (L15 / F12, DRI 'a definir', prazo '-').

| Campo | Valor |
|---|---|
| Volume | ausente |
| Taxa de entrada | `null` |
| Taxa de saída | ausente, os percentuais são mix de origem de MQL, não taxa de passagem |
| Perda absoluta | `null` |
| Tempo médio (dias) | `null` |
| Estimado | não |

**Fonte.** Slide 'FLUXOS: Autos & Imóveis', Michelle Morais, 28/08/2026, três versões de detalhe crescente.
ARQUIVO-FONTE NÃO VERSIONADO (L28): conferido com `find assets -iname '*fluxo*'`, o único
original versionado em assets/originais/A-visao-de-negocio-e-fluxo-de-receita/ é `jornada-do-
cliente-profissional.png`. Os percentuais existem só em prosa em 02-diagnostico/lacunas-do-fluxo-
de-receita.md §1 e na ata 06-reunioes/2026-08-28-jornada-do-cliente.md (tabela 'Números obtidos',
linha 'Canais'). CORREÇÃO DE GRAU PROBATÓRIO: as duas decomposições (mix de canais e canais de
entrada) vêm do MESMO artefato e fecham no mesmo 97%, não em 100% (L29). Isso demonstra
consistência interna do slide, NÃO acurácia, e não é verificação independente nem reexecutável
enquanto o arquivo não for versionado. A frase 'dois caminhos independentes' e 'sobe muito a
confiança no material', em lacunas-do-fluxo-de-receita.md §1, precisa ser corrigida na origem.
Para fechar: original do slide (DRI Carolina Dallolio, prazo '-', não acordado na sessão) e o
controle de investimento por canal, fora do dashboard, com Mirella Mendonça (00:10:08).

### 2. Entrada: captação do contato e geração de MQL

`declarado`  ·  travas: Exposicao, Qualificacao

Três frentes de entrada declaradas por Carolina Dallolio (00:04:20): clientes que o comercial vai
buscar (base inativa ou campo), clientes que chegam por campanhas e réguas de marketing, e contato
espontâneo. MQL definido na sessão como 'dados básicos, nome, e-mail, telefone e em alguns canais
documento' (00:44:38). O caminho do formulário/LP e os canais WhatsApp e telefone convergem num
fluxo de qualificação automatizado por bot, refinado há cerca de quatro meses, que reaproveita
histórico de inativo.

PERDA (perda_absoluta = null): ausente. Não há taxa contato→MQL declarada em fonte nenhuma.

| Campo | Valor |
|---|---|
| Volume | ausente |
| Taxa de entrada | `null` |
| Taxa de saída | 50% [D], denominador em disputa: o slide diz RECEITA, a fala de 00:05:42 diz BASE. Não usar até a OLX confirmar qual é. É participação de origem, não taxa de passagem. |
| Perda absoluta | `null` |
| Tempo médio (dias) | `null` |
| Estimado | não |

**Fonte.** DENOMINADOR EM DISPUTA, NÃO RESOLVIDO. O slide da jornada diz RECEITA, '50% da receita nasce da
prospecção comercial' (02-diagnostico/jornada-do-cliente-profissional.md, tabela das seis etapas).
A transcrição diz BASE, Carolina Dallolio, 00:05:42, linha 337: 'a gente tem 50% da base que
chega por prospecção comercial'. O repositório carrega as duas versões em documentos diferentes:
jornada-do-cliente-profissional.md adota 'receita'; a ata de 28/08 e 03-estrategia/meta-do-
projeto.md §3 adotam 'base'. NENHUMA das duas fontes diz 'entrada', a versão anterior deste mapa
inventou um terceiro denominador. Enquanto a OLX não confirmar qual é, esta etapa NÃO entra em
reconciliação (ambiguidade 5). Falta ainda a fatia de renovação e de Inside/Field Sales que
completaria os 100%.

### 3. Qualificação (MQL → SQL)

`ausente`  ·  travas: Qualificacao, Compromisso

Bot de qualificação automatizado gera MQL e depois SQL, e entrega ao atendimento comercial. SQL
definido como elegibilidade comercial: 'no caso de imóveis, a gente só vende para imobiliárias e
corretores. Então, se ele não tem um CNPJ da área, ele não vai ser elegível' (Carolina Dallolio,
00:44:38). Cliente já ativo na base pula etapas e vai direto ao comercial ou a um farmer; a rota
depende de por onde ele entrou.

PERDA (perda_absoluta = null): ausente.

| Campo | Valor |
|---|---|
| Volume | ausente para o recorte B2B. Existem candidatos apurados sem confirmação de significado: generate_lead_pro 661.144 e generate_lead 830.116 (agosto/2026, GA4 VivaReal 407391347); lead_b2b = 0 (agosto/2026, OLX App + Web 152644854). |
| Taxa de entrada | `null` |
| Taxa de saída | ausente, existe no dashboard de funil B2B, não extraída |
| Perda absoluta | `null` |
| Tempo médio (dias) | `null` |
| Estimado | não |

**Fonte.** AS DEFINIÇÕES ESTÃO DECLARADAS EM REUNIÃO (00:44:38), NÃO DOCUMENTADAS. Corrigido em relação à
versão anterior, que registrava a lacuna L10 como 'fechada': não existe no repositório nem foi
entregue pelo cliente qualquer política de qualificação, critério escrito de MQL/SQL, SLA ou ICP
versionado. Para o score da Trava de Qualificação isso é percepção, as dimensões de ICP
documentado e de processo de qualificação ficam null até o artefato formal chegar (regra 5). A
TAXA existe e foi vista na tela: o dashboard de funil B2B tem taxa de qualificação (MQL→SQL) e
conversão em vendas (SQL→venda), com filtro por vertical, canal, time comercial e período,
processado às 3h, histórico de 12 meses, Lu Machim, 00:07:00–00:08:59, como registra L6 (a versão
anterior citava 00:05:42–00:08:59, e 00:05:42 é fala de Carolina Dallolio sobre os 50%). A V4 viu
a tela e não extraiu nenhum dado; o dashboard estava em processamento durante a demo. Falta: links
dos dashboards, lacuna 1 da ata, DRI Leonardo Rosa, prazo '-'. PELA VIA INSTRUMENTADA HÁ DOIS
ESTADOS, NÃO UM: (a) `lead_b2b` registrou ZERO eventos em agosto/2026 na propriedade OLX App + Web
(152644854), com a tag 429 montada e ativa, auditoria (vii), achado 3; (b) existem DOIS
candidatos a numerador com volume apurado, `generate_lead_pro` 661.144 e `generate_lead` 830.116,
agosto/2026, propriedade GA4 VivaReal (407391347), registrados em PENDENCIAS.md linhas 310–311 e
346 e em dados/client.json. PENDENCIAS.md:346 diz literalmente: 'generate_lead_pro, com 661.144
eventos em agosto, é o primeiro indicador possivelmente B2B que apareceu em todo o projeto. Se ele
for mesmo o lead de anunciante, é o numerador que falta para o fluxo de receita.' Duas
confirmações pendentes antes de usar: o que `generate_lead_pro` mede (ação 1 da pendência 13) e
qual das duas propriedades é a de referência, porque o mesmo gatilho `[208] lead_dbm` dispara as
tags 209 (G-6TV9FSHYVM) e 356 (G-ZBYP2KJ7L9) no contêiner ZapImóveis ANUNCIE, auditoria (vii),
achado 20, que instrui 'confirmar qual das duas é a de referência antes de usar generate_lead como
numerador do fluxo de receita'.

### 4. Contratação (fechamento da venda)

`declarado`  ·  travas: Decisao, Compromisso

Dois canais com escopo desigual. CANAL ONLINE: vende SOMENTE planos de anúncio; sub-fluxo POS =
login e cadastro → vitrine de planos → checkout → venda computada; a vitrine existe para Zap e
VivaReal, e em Autos a jornada roda dentro do login OLX que o usuário já tem, com POS MyPlan
(Michelle Morais, 00:33:44; Leonardo Costa, 00:30:12 e 00:37:08). Quem para no meio cai em
transbordo de carrinho abandonado para abordagem humana. TIME COMERCIAL (Inside/Field Sales, field
focado em cliente de maior valor): vende todos os produtos e é o único caminho para up, down e
cancelamento, 'um up, um down, um cancelamento é via time comercial' (Carolina Dallolio,
00:12:41).

PERDA (perda_absoluta = null): carrinho abandonado, recuperado por transbordo humano. Sem taxa
declarada, e sem acordo sobre em quais verticais o transbordo existe (L16).

| Campo | Valor |
|---|---|
| Volume | ausente, única pista: '414 vendas' [D], referenciada por Leonardo Costa (00:11:03) sobre o dashboard de canal online que Lu Machim apresentava na tela; não foi lida em voz alta, não consta de nenhum documento, e vem sem período, vertical nem denominador |
| Taxa de entrada | `null` |
| Taxa de saída | Canal online = 25% da receita de Autos e 10% da de Imóveis [D]; 'o restante tudo via comercial' (Carolina Dallolio, 00:12:41). É participação de receita por canal, não taxa de passagem. Sessão→vitrine→checkout→venda existe no dashboard de canal online e não foi extraída. |
| Perda absoluta | `null` |
| Tempo médio (dias) | `null` |
| Estimado | não |

**Fonte.** Slide da jornada, etapa 2, e transcrição 00:12:41. É a única das seis taxas quebrada por vertical,
e fecha a ambiguidade 5 quanto ao resto dos 100% do lado da contratação. VOLUME, CORREÇÃO DE
PROCEDÊNCIA E DE ESCOPO DA AFIRMAÇÃO: '414 vendas' é o único VOLUME DE FUNIL citado na sessão, não
'o único número absoluto pronunciado', a mesma transcrição traz 'Foram 10 vídeos gravados'
(Leonardo Costa, bloco 00:26:33, linha 695) e 'um pagamento de mais de R$ 50.000' (Leonardo Costa,
01:03:19, linha 1299), ambos absolutos. Quem enumera o funil do dashboard é Lu Machim, 'É aqui as
sessões, as vitrines, os checkouts e as vendas' (linha 421); Leonardo Costa apenas REFERENCIA o
número que já estava na tela, 'quando a gente tá falando das 414 vendas, a gente tá falando mais
das vendas que aconteceram online mesmo, com checkout, pagamento' (linha 423, bloco 00:11:03).
Conferido com grep em todo o repositório: '414' não consta de nenhum outro documento, só da linha
423 da transcrição. NÃO usar como volume desta etapa até que período, vertical e denominador sejam
confirmados; é, porém, o item de extração de maior valor imediato. CONFLITO ABERTO (L16): Michelle
Morais registra transbordo só em Imóveis, Carolina Dallolio responde 'não é só imóveis', Michelle
conclui o contrário e a conversa termina sem fechar (00:43:40).

### 5. Pagamento da primeira fatura

`declarado`  ·  travas: Decisao

Modelo majoritariamente pré-pago: Imóveis só pré-pago; Autos dividido entre pré e pós-pago;
PayPerLeads para perfis específicos, locadoras e incorporadoras (Carolina Dallolio, 00:12:41).
Meios de pagamento: metade da base em boleto [D], cerca de 40% cartão [D], o restante Pix [D], SEM
diferenciação de preço por meio, 'a gente sabe que deveria, mas hoje não' (Carolina Dallolio,
00:21:16, L20). Existe modo de pagamento periódico de 3, 6 ou 12 meses [D] com desconto
progressivo, o '~20%' veio hedged na própria fala ('se eu não me engano') e não deve ser usado
como número. Há pagamento de Imóveis 'de mais de R$ 50.000' [D] que não cabe no limite do cartão
(Leonardo Costa, 01:03:19), é exemplo de restrição de meio de pagamento em plano periódico, NÃO
ticket médio e não declarado como típico. MUDANÇA ESTRUTURAL RECENTE: o login na plataforma passou
a exigir pagamento prévio, 'antes a pessoa podia fazer login na plataforma antes de pagar o
boleto e agora não' (Leonardo Costa, bloco 00:26:33, L2).

PERDA (perda_absoluta = null): 20% dos contratos que geraram cobrança nunca viram caixa [D], mais
um vazamento adicional de tamanho desconhecido nos contratos sem cobrança gerada. Se há
recuperação ativa depois, ninguém sabe: ambiguidade 6, não perguntada na sessão, sem DRI e sem
prazo. Sem isso não se sabe se o vazamento é bruto ou líquido.

| Campo | Valor |
|---|---|
| Volume | ausente |
| Taxa de entrada | 80% dos contratos QUE GERARAM COBRANÇA pagam a 1ª fatura [D]; 20% não pagam (Carolina Dallolio, 00:15:30). Contratos fechados que nunca geraram cobrança estão FORA deste denominador. É A ÚNICA taxa_entrada não-null do mapa inteiro: a única passagem etapa→etapa (etapa 4 → etapa 5) declarada em fonte alguma. As outras nove são null porque as taxas que existem para elas não são taxas de passagem. |
| Taxa de saída | 80% dos contratos QUE GERARAM COBRANÇA pagam a 1ª fatura [D]; 20% não pagam (Carolina Dallolio, 00:15:30). Contratos fechados que nunca geraram cobrança estão FORA deste denominador. É a ÚNICA taxa de passagem etapa→etapa de todo o mapa. |
| Perda absoluta | `null` |
| Tempo médio (dias) | `null` |
| Estimado | não |

**Fonte.** Slide da jornada, etapa 3 ('80% dos clientes que fecham contrato de fato pagam a primeira fatura')
CORRIGIDO pela própria Carolina Dallolio na transcrição para um denominador mais estreito: 'dos
100% que fizeram a contratação E GERARAM UM BOLETO ou qualquer coisa do tipo, desses 100%, 80
pagam' (00:15:30, linha 473). Registro de procedência que a crítica adversarial errou: a
formulação larga 'escorrega aí 20% dos clientes entre a contratação e o primeiro pagamento' é
literalmente da própria Carolina em 00:14:12 (linha 445), não uma leitura do slide feita pela V4,
o que aconteceu na sessão foi a falante estreitar o próprio denominador um minuto depois. Vale o
denominador estreito. Contratos que nunca geraram cobrança ficam FORA da conta e constituem
vazamento adicional não medido, sem DRI e sem prazo. Não há data-base nem janela de apuração. A
mudança do login (00:26:33) é ponto de quebra na série: qualquer apuração histórica do 80% cruza
esse corte e precisa ser datada.

### 6. Ativação: publicação do primeiro anúncio

`declarado`  ·  travas: Compromisso, Retencao

Pagou, ativa o plano e o CLIENTE publica, a OLX não publica em nome dele ('Existem alguns players
que eles mesmo publicam os anúncios em nome do cliente, não é o nosso caso', Carolina Dallolio,
00:14:12). Duas rotas: carga via integrador de terceiros ou publicação unitária no CanalPro
(Imóveis, cadastro e senha próprios, acessível só após pagar) e no MyPlan (Autos). Dois modelos de
inventário: Autos por INSERÇÃO, 'um plano de 20 anúncios' [D] é consumido, vendeu o carro o
anúncio não volta, e Imóveis por SLOT, reaproveitável se o imóvel sair no meio do período
(00:16:42 e 00:18:09). CAUSA, NO FORMATO DA REGRA 4, COMO HIPÓTESE A TESTAR: a empresa opera sob a
política implícita de transferir integralmente ao anunciante o trabalho de ativação, não publica
em nome dele, exige integrador de terceiros ou publicação unitária, mantém cadastro e senha
separados no CanalPro e só libera login depois do pagamento, o que gera uma janela entre
pagamento e primeiro anúncio sem responsável, limitando a chance de o cliente chegar a receber
qualquer lead. A metáfora de Carolina Dallolio, 'aquele cliente igual o que contrata academia e
nunca vai fazer exercício', entra apenas como registro de como o cliente é descrito internamente:
é 'a pessoa não faz', que a regra 4 proíbe como causa-raiz. A taxa de não publicação POR CAUSA
nunca foi medida.

PERDA (perda_absoluta = null): cliente que pagou, teve acesso e nunca publicou nunca teve chance
de receber lead. É o elo entre Decisão e Retenção. O tamanho sobre a base paga é DESCONHECIDO
enquanto o denominador do 12% não for confirmado. Também não há quebra por vertical: o corte
declarado é por canal (online × assistido), nunca Autos × Imóveis.

| Campo | Valor |
|---|---|
| Volume | ausente |
| Taxa de entrada | `null` |
| Taxa de saída | 12% dos que saem no 1º mês nunca publicaram [D], até 20% no canal online e 8–10% no assistido [D], COM O QUALIFICADOR DA PRÓPRIA FALA: Lu Machim descreve a faixa do assistido como 'do pior cenário que a gente já teve' (00:15:30, linha 475). Se é pior caso histórico ou média corrente é ambíguo na transcrição e precisa ser perguntado junto com o denominador do 12%. Leonardo Costa estima de improviso que '80% desses, 90' dos 12% vêm do online: fala explicitamente hedged ('sei lá'), no bloco 00:14:12 (linha 445), entra [D]+[E], nunca como taxa. Na mesma fala ele diz 'aqueles 10% de receita do online', que é o número de Imóveis, enquanto Autos é 25%: a fala mistura verticais. |
| Perda absoluta | `null` |
| Tempo médio (dias) | `null` |
| Estimado | sim `[E]` |

**Fonte.** Slide da jornada, etapa 4, e transcrição nos blocos 00:14:12, 00:15:30, 00:16:42 e 00:23:16. [E]
DENOMINADOR: a leitura mais provável das falas põe o 12% sobre QUEM SAI, não sobre a coorte que
pagou, Carolina Dallolio, 00:16:42, linha 483: 'Então dos clientes que saem do 12% vai embora sem
nunca ter sequer publicado'; Leonardo Costa, bloco 00:15:30, linha 469: 'você falou dos 12% que
saem sem publicar um anúncio'; Lu Machim, bloco 00:15:30, linha 475: '20% dos caras QUE SAEM no
online no primeiro mês não publicam um primeiro anúncio'. Em 00:23:16 (linha 597) Carolina
descreve o mesmo cliente como alguém que PAGOU, 'ele paga, mas aí ele tá nesse cenário do
primeiro mês que ou bem ele tá nesses 12% aqui que sequer publicou', mas o contexto verificado é
a pergunta de Gustavo Figueiredo sobre 'churn M0, ou seja, uma não ativação' (linha 566), o que
faz dessa fala uma enumeração de PERFIS de quem churna no 1º mês, coerente com a leitura de 'quem
sai', não contrária a ela. A transcrição é automática (Gemini no Google Meet) e a segmentação é
ruim; a redação precisa ser confirmada com a OLX antes de comitê. SE CONFIRMADA, a consequência é
dura: p(publicação)=88% (=100−12%) deixa de ser termo independente da identidade de regime de
03-estrategia/meta-do-projeto.md §4, os mesmos clientes entram no termo de publicação e no de
churn, e a linha 'Publicação 88%→92% = +4,5%' da tabela de elasticidades cai junto. NENHUMA
consequência aritmética deve ser aplicada a meta-do-projeto.md antes dessa confirmação. Observe
que 02-diagnostico/jornada-do-cliente-profissional.md já registra a ambiguidade 3 como
'respondida' com exatamente essa leitura, e a leitura não foi propagada para a aritmética.

### 7. Entrega do produto: recebimento de leads

`declarado`  ·  travas: Retencao, Cegueira

O anúncio publicado passa a receber lead por três vias: lead do próprio anúncio ('um match
perfeito'), lead de anúncios similares e lead de outros canais no modelo PayPerLeads, acionado por
CRM, push, WhatsApp e Facebook (Carolina Dallolio, 00:18:09 e 00:19:40). A OLX declara
explicitamente que a composição existe 'para amenizar esse efeito zero leades ali direto no seu
próprio anúncio', ou seja, já reconhece o zero-lead como problema e opera um paliativo. A entrega
é medida por PROXY: 'a proxy que a gente usa é três leads em 7 dias para OLX. A gente não tem um
número mágico para real estate porque muda muito de aluguel para venda' [D] (Leonardo Costa, bloco
00:55:01, linha 1159). Marcação de vendido raramente volta do integrador, o que impede medir o
desfecho (L26).

PERDA (perda_absoluta = null), CORREÇÃO ESTATÍSTICA: a entrega MEDIANA do produto é zero, o caso
típico é o anúncio sem nenhum lead [D]. A MÉDIA não é zero e não é calculável, porque todos os
leads caem nos 11% e a distribuição nunca foi medida. E o escopo é Imóveis, por anúncio: não
existe número equivalente para Autos. A frase 'a entrega média do produto é zero' está replicada
em 02-diagnostico/jornada-do-cliente-profissional.md e em 03-estrategia/meta-do-projeto.md §3 e
precisa ser corrigida nos dois. O 89% dá MAGNITUDE DECLARADA [D] à UDE #2 do kick-off (o
anunciante compra posição, não garantia de lead): o zero-lead deixa de ser risco contratual e
passa a ser o caso típico segundo o próprio cliente, confirmação depende de apuração no sistema.
O que concentra os leads nos 11% segue aberto (ambiguidade 2): faixa de preço, praça, ranking,
qualidade da foto ou DEDUPLICAÇÃO, a pista da dedup vem do kick-off ('193.000 anúncios sincados
que equivalem a 15 milhão de anúncios não sincados, duplicados', 01:29:11) e tem conflito interno
na própria fonte, que o resumo registra como 1,5 milhão. Se for dedup, é problema de produto, não
de demanda, e a injeção muda completamente. Não usar esse número sem reapuração.

| Campo | Valor |
|---|---|
| Volume | ausente |
| Taxa de entrada | `null` |
| Taxa de saída | 89% dos anúncios de IMÓVEIS recebem ZERO lead [D], logo 11% concentram toda a entrega. É participação de estado por anúncio, não taxa de passagem entre etapas. |
| Perda absoluta | `null` |
| Tempo médio (dias) | `null` |
| Estimado | não |

**Fonte.** Slide da jornada, etapa 5, e transcrição, Carolina Dallolio, bloco 00:19:40 (linha 491): '89% dos
anúncios de imóveis não recebem nenhum lead'. Os documentos do repositório citam 00:18:09, que é o
timestamp do bullet de resumo automático, não o da fala, mesma coisa com o proxy de 3 leads em 7
dias, citado como 00:53:50 quando a fala está em 00:55:01. O 89% é sobre ANÚNCIO, não sobre
cliente, a distribuição por cliente nunca foi medida nem pedida (ambiguidade 1, aberta), e é ela
que se liga ao churn, que é medido por cliente/pagamento. Não há taxa declarada de quanto a
composição de leads recupera, então não se sabe se 89% é a entrega real ou só a do canal próprio.
Não existe equivalente do 89% para Autos: procurado na transcrição inteira, não existe.

### 8. Recorrência ou churn

`declarado`  ·  travas: Retencao

Planos mensais, trimestrais ou anuais com renovação automática. No pré-pago basta não pagar para
interromper, não há evento de cancelamento, então o churn de Imóveis é inferido por não
pagamento, não medido. DEFINIÇÃO QUE MUDA A LEITURA: churn é interrupção de pagamento; quem paga e
não usa NÃO é churn, é inativo gerando receita (Leonardo Rosa pergunta, Carolina Dallolio
confirma, 00:22:16, L18). Logo a insatisfação silenciosa de quem paga sem publicar, exatamente o
perfil que os 89% produzem, não aparece em métrica nenhuma.

PERDA (perda_absoluta = null): é o vazamento RECORRENTE do fluxo: age todo mês sobre a base
inteira. ATENÇÃO À CATEGORIA, na receita de REGIME, recorrente e por coorte têm peso idêntico,
porque toda coorte entra todo mês; a diferença entre eles é de TEMPO DE RESPOSTA (o churn muda a
constante de tempo da base, os vazamentos de coorte não), o que é argumento de sequenciamento, não
de magnitude. O 12% de não publicação NÃO é vazamento independente empilhado sobre este: pela
leitura mais provável das falas, é PERFIL de quem churna no 1º mês, e somá-los conta os mesmos
clientes duas vezes. A V4 deriva [E] que 8–10% ao mês composto em 12 meses implica perder 63% a
72% da base por ano, SE a taxa for sobre número de clientes e SE se mantiver constante, duas
premissas não confirmadas. É magnitude COMPATÍVEL com o net de receita negativo declarado em
Imóveis (UDE #1), mas suficiência não é demonstrável sem o volume de entradas: nem o net nem as
entradas têm número em documento nenhum.

| Campo | Valor |
|---|---|
| Volume | ausente |
| Taxa de entrada | `null` |
| Taxa de saída | 8–10% ao mês [D], concentrado no 1º mês. É hazard mensal sobre a base, não taxa de passagem entre etapas. CUIDADO: o 8–10% de churn coincide numericamente com o 8–10% de NÃO PUBLICAÇÃO no canal assistido (etapa 6), são taxas diferentes com o mesmo intervalo, e a do canal assistido vem com o qualificador 'pior cenário que a gente já teve'. |
| Perda absoluta | `null` |
| Tempo médio (dias) | `null` |
| Estimado | sim `[E]` |

**Fonte.** Slide da jornada, etapa 6, e transcrição, Carolina Dallolio, 00:22:16 (linha 539): 'de 8 a 10% de
turn... o principal motivo de ch mesmo eh atribuído a baixa performance', com 'a maior
concentração de churn no primeiro mês' (00:23:16). CORREÇÃO AO SLIDE, registrada na mesma fala: 'O
esquecimento, como eu falei, ele responde por 20% dos ATRASOS, mas não do ch', o slide põe
'(boleto facilita esquecimento)' dentro da caixa dos 8–10% e sugere o contrário (L19). Isso RETIRA
o meio de pagamento da explicação do churn; não é suporte positivo à hipótese de entrega, a
cadeia por entrega de produto segue apoiada apenas na atribuição declarada do cliente, sem
registro estruturado de motivo de cancelamento (pergunta 6 do roteiro, sem resposta capturada nem
em 24/08 nem em 28/08). UNIDADE NÃO DECLARADA: os 8–10% não dizem se são de logo ou de receita
(ambiguidade 4, aberta). Iuna Scheffler lê o net em RECEITA no kick-off ('net negativo é em
receita, as nossas entradas não estão compensando o churn mais downgrade', 24/08, 01:07:38), o que
sugere que podem não ser a mesma métrica. Toda derivação de 63–72%/ano, de constante de tempo de
11 meses e das elasticidades de meta-do-projeto.md §4 pende dessa resposta.

### 9. Faturamento e recebimento do pós-pago (só Autos)

`ausente`  ·  travas: Decisao, Retencao, Cegueira

[E] Pela estrutura pós-paga, é a única rota em que o serviço é entregue antes do recebimento, mas
o momento em que a receita é RECONHECIDA e em que o contrato passa a existir segue SEM RESPOSTA: é
o nó 3B-11 da árvore do portal, levado como pergunta 3 do roteiro da sessão de 28/08 e não fechado
em ata (a seção 'Nós da árvore alterados' saiu vazia). Enquanto isso durar, a posição desta etapa
no fluxo é hipótese de desenho, não fato contábil, e a afirmação de que em Imóveis ela 'não
existe' (tudo pré-pago, faturamento e recebimento colapsando na etapa 5) é a mesma inferência,
também sem fonte. O slide a descreve como 'Pós-pago: alta taxa de abono e contestação'. O pós-pago
é declarado como concentrado no field sales de Autos (Carolina Dallolio, 00:23:16).

PERDA (perda_absoluta = null): não dimensionada, e atinge a etapa onde a receita já entrou no
resultado. Um vazamento de magnitude desconhecida sobre receita já reconhecida NÃO pode ser
excluído do topo de nenhum ranking de perda.

| Campo | Valor |
|---|---|
| Volume | ausente |
| Taxa de entrada | `null` |
| Taxa de saída | ausente, 'alta taxa' sem percentual |
| Perda absoluta | `null` |
| Tempo médio (dias) | `null` |
| Estimado | sim `[E]` |

**Fonte.** Slide da jornada, etapa 6, bullet 'Pós-pago: alta taxa de abono e contestação', é o ÚNICO bullet
numérico ausente das seis etapas, e segue sem número (ambiguidade 7, aberta, não perguntada na
sessão). Sem ele, o truput de Autos está superestimado por valor desconhecido. Pergunta contábil
aberta: 06-reunioes/2026-08-28-jornada-do-cliente.md, roteiro, pergunta 3, 'Quando a receita é
reconhecida, e o contrato existe?', nó 3B-11 marcado como aberto.

### 10. Expansão e recompra

`ausente`  ·  travas: Retencao, Decisao

Cliente ativo na área logada (Canal Pro em Imóveis, MyPlan em Autos) busca upgrade, destaque
adicional ou cota de festival, 'aqui a gente está falando essencialmente de clientes que já são
nossos... é muito mais um upgrade, uma venda one shot de um destaque, cota para festival. Aqui a
gente não fala muito em aquisição' (Michelle Morais, 00:36:13, L11). CAUSA NO FORMATO DA REGRA 4:
a empresa opera sob a política implícita de que toda mudança de plano, up, down e cancelamento,
passe por atendimento humano, sem self-service: 'do ponto de vista de gestão, upgrade e tal, a
gente não tem upgrade, por exemplo, self service hoje' (Leonardo Costa, 00:39:34, linha 909;
Michelle Morais parafraseia em 00:41:15), coerente com up, down e cancelamento só via time
comercial na etapa 4 (Carolina Dallolio, 00:12:41). O tamanho do efeito é DESCONHECIDO: não há
volume, taxa nem participação de receita de expansão declarados. Destaque está saturado e é a
demanda nº 1 de upgrade (L23). Canal de engajamento assimétrico e sem gestão: em Autos 60–70% usam
o app e em Imóveis 20–30% [D] (Leonardo Costa, 00:38:26, linha 885, fala com autocorreção: 'na
casa dos 70, 60%' e 'é 20% só usa o app, eh, 30%'), e 'a gente não tem nenhuma etapa de touch
point com foco em ativação do app', formulação de Gustavo Figueiredo, que é COO da V4 e não da
OLX, em 00:40:31 (linha 949), CONFIRMADA por Michelle Morais ('Não é incentivado hoje', linhas
967–971) e por Leonardo Costa ('para B2B', 'Não'). O dado declarado é a confirmação da OLX, não a
pergunta do consultor.

PERDA (perda_absoluta = null): ausente. Não é possível afirmar tamanho nem superlativo ('a
alavanca mais barata que existe') sobre uma etapa em que nada foi medido: o único benchmark do
material é externo e citado de memória.

| Campo | Valor |
|---|---|
| Volume | ausente |
| Taxa de entrada | `null` |
| Taxa de saída | ausente |
| Perda absoluta | `null` |
| Tempo médio (dias) | `null` |
| Estimado | não |

**Fonte.** Transcrição de 28/08, blocos 00:36:13, 00:38:26, 00:39:34, 00:40:31 e 00:41:15. NENHUMA taxa,
nenhum volume, nenhum percentual de receita de expansão foi declarado, nem NRR, nem participação
de destaque e SVA não recorrente na receita (pergunta F14, sem resposta). O benchmark citado ('lá
fora, geralmente 50% da receita vem de venda de destaques', Leonardo Costa, 01:00:35, os
documentos do repositório citam 00:59:26, que é o bullet de resumo) é externo, citado de memória,
e NÃO é número da OLX. Todo o material de expansão está parqueado para o Comitê 2 por decisão
registrada em ata (regra 3, uma restrição por vez) e não deve contaminar o Comitê 1.

---

## Ranking de perda: indeterminável, e isso é o achado

O ranking por perda absoluta é indeterminável hoje: nenhuma etapa tem volume, e quatro (Exposição,
Qualificação, Pós-pago Autos, Expansão) não têm sequer taxa. Ordenar por percentual violaria o
Passo 4 e o checklist de fechamento da skill ('Ordene as etapas por perda absoluta de receita
potencial, nao por taxa percentual… uma taxa ruim em cima de volume pequeno perde para uma taxa
mediana em cima de volume grande'). NESTA ETAPA, especificamente: não há taxa nenhuma, os
percentuais de canal são mix de origem de MQL, e a única perda nomeada é a atribuição perdida do
canal Direto, cuja magnitude o próprio slide declara existir sem quantificar (L15/F12).

| Etapa | Perda absoluta |
|---|---|
| 1 · Exposição e geração de demanda (mix de canais) | `null` |
| 2 · Entrada, captação do contato e geração de MQL | `null` |
| 3 · Qualificação (MQL → SQL) | `null` |
| 4 · Contratação (fechamento da venda) | `null` |
| 5 · Pagamento da primeira fatura | `null` |
| 6 · Ativação, publicação do primeiro anúncio | `null` |
| 7 · Entrega do produto, recebimento de leads | `null` |
| 8 · Recorrência ou churn | `null` |
| 9 · Faturamento e recebimento do pós-pago (só Autos) | `null` |
| 10 · Expansão e recompra | `null` |

---

## Reconciliação: regra 7

A REGRA 7 NÃO É VERIFICÁVEL HOJE, POR NENHUM DOS DOIS CAMINHOS. Ela exige que a receita derivada
do funil bata com a declarada dentro de 5%; os quatro campos ficam null, e o null é o registro,
não a omissão, de que a regra está bloqueada. Regra 1 do repositório: campo sem dado fica null,
não é apagado.

PELA VIA DO CLIENTE falta tudo o que a multiplicação pede. Não há volume de entrada em nenhuma das
dez etapas, não há ticket médio (dados/client.json: briefing.ticket_medio = null; bloco A3 do
checklist, ⚪), não há receita declarada por vertical, e os 100% da etapa 2 não fecham, o
denominador do 50% está dividido entre 'receita' (slide) e 'base' (Carolina Dallolio, 00:05:42) em
dois documentos do próprio repositório, e falta a fatia de renovação e de Inside/Field Sales. O
bloco A do checklist (A1–A3) está com os três itens em ⚪, nenhum recebido, e nenhuma concessão de
ferramenta o destrava: é entrega de dado, não acesso.

PELA VIA INSTRUMENTADA o GA4 também não fecha. O funil B2B derivável hoje tem NUMERADOR
INEXISTENTE: `lead_b2b` = 0 em agosto/2026 na propriedade OLX App + Web (152644854), com a tag
429 montada e ativa e a tag 349 identificando o lead por posição no DOM (auditoria vii, achado 3).
Tem CONVERSÃO CONTAMINADA, a tag 426 de purchase dispara no gatilho 215, que escuta
begin_checkout, em Planos Profissionais e PAYG (achado 1); a parcela B2B contaminada dentro dos
565.258 purchase de agosto nunca foi isolada. E tem um DENOMINADOR PROVAVELMENTE NÃO SEGMENTÁVEL,
com a formulação que importa: a única tag do export que grava `user_olx` está pausada e
`seller_category` depende dela, MAS a própria auditoria escreve 'A confirmar: se o site grava
user_olx por código próprio, fora do GTM. Se gravar, o problema não existe'. Isso é inferência
sobre export de GTM condicionada a uma verificação que ninguém fez, não é estado apurado, e não
deve ir ao Board como se fosse.

MESMO QUE OS DOIS CAMINHOS ABRISSEM, A DERIVAÇÃO AINDA NÃO FECHARIA por um terceiro motivo: das
seis taxas declaradas do mapa, apenas UMA (o 80% do pagamento da 1ª fatura) é taxa de passagem
entre etapas. As outras cinco são grandezas incomensuráveis entre si, participação de origem
(50%), participação de receita por canal (25%/10%), fatia de quem sai (12%), participação de
estado por anúncio (89%, só Imóveis) e hazard mensal sobre a base (8–10%). Uma cadeia
multiplicativa não se monta com elas. Some-se que quatro dos seis vêm somados sobre Autos e
Imóveis, que têm modelo de anúncio (inserção × slot) e de cobrança (pré × pré/pós) diferentes: o
Passo 1 do POP manda montar um fluxo por unidade antes de consolidar, e é exatamente por isso que
`unidades[]` não pôde ser emitido.

O QUE DESTRAVA, NA ORDEM DE CUSTO: (1) links dos dashboards de funil B2B e de canal online, onde
as taxas de passagem já existem por vertical, canal, time e período, com histórico de 12 meses
(lacuna 1 da ata, DRI Leonardo Rosa); (2) confirmar o que `generate_lead_pro` mede e qual
propriedade é a de referência (ações 1 e 2 da pendência 13); (3) bloco A do checklist, receita
por linha de negócio, funil com volumes, ticket médio, ciclo e CAC. Até lá, qualquer número de
receita derivada seria invenção, e a divergência é indeterminada, não zero.

| Campo | Valor |
|---|---|
| Receita derivada | `null` |
| Receita declarada | `null` |
| Divergência | `null` |

---

## Ordem de diagnóstico das travas

Regra de Goldratt: de baixo para cima no funil. Resolver Exposição com Retenção quebrada só aumenta
o custo do desperdício.

| # | Trava | Por quê |
|---|---|---|
| 1 | **Cegueira** | PRÉ-CONDIÇÃO, NÃO RESTRIÇÃO, entra em primeiro por ser gate, não por ser candidata a governante. Pelo playbook, 'Cegueira não é uma restrição de receita, é uma pré-condição', e ela é o motivo pelo qual as outras sete não podem ser pontuadas hoje: sem volume por etapa, sem tempo médio, com lead_b2b = 0 em agosto/2026 (tag 429 ativa, lead identificado por posição no DOM), purchase contaminado pelo gatilho 215 e denominador provavelmente não segmentável, qualquer nota nas demais seria percepção. Evidências formais já disponíveis: o próprio slide de FLUXOS documenta que campanha paga para WhatsApp 'entra tudo como Direto' (buraco de atribuição declarado pelo cliente); a propriedade GA4 que carrega toda a superfície B2B do escopo (Grupo OLX 503925542) é a única em tier gratuito e tem ZERO eventos-chave; Autos 360 tem 449 eventos e nenhum marcado como conversão; session_start está marcado como evento-chave na VivaReal. ATENÇÃO À REGRA 5/6: essas evidências alimentam a pré-condição, NÃO produzem nota. A regra gateia notas 4 e 5, que na escala do playbook afirmam que a dimensão está SAUDÁVEL, a frase de 02-diagnostico/lacunas-do-fluxo-de-receita.md:50 usa a regra ao contrário e precisa ser corrigida na origem. |
| 2 | **Retencao** | REGRA DE GOLDRATT, DE BAIXO PARA CIMA: é a trava mais a jusante do fluxo, associada às etapas 7 (entrega de leads), 8 (churn), 9 (pós-pago) e 10 (expansão), e contamina a leitura de tudo o que está acima, resolver Exposição com Retenção quebrada só aumenta o custo do desperdício. É também onde estão os dois percentuais de maior magnitude declarada: 89% dos anúncios de Imóveis sem lead [D] e churn de 8–10% ao mês [D], concentrado no 1º mês. Diagnosticar primeiro NÃO significa concluir que é a restrição: a cadeia entrega-zero → churn é hipótese nomeada, relato único do cliente, sem elo provado. Duas perguntas abrem o diagnóstico: a unidade do churn (logo ou receita, ambiguidade 4) e a distribuição do 89% por cliente (ambiguidade 1). E a vertical onde o churn dói não tem proxy de performance, o de 3 leads em 7 dias existe só em Autos. |
| 3 | **Decisao** | Segunda de baixo para cima: associada às etapas 4, 5, 9 e 10. Carrega a ÚNICA taxa de passagem etapa→etapa do mapa inteiro, 80% dos contratos que geraram cobrança pagam a 1ª fatura [D], o que a torna a única trava com um número tecnicamente utilizável hoje. Pela aritmética de regime ela EMPATA com Retenção no ponto médio da faixa de churn e a VENCE no topo (levar 80%→90% vale +12,5% [E]), de modo que sequenciá-la em segundo é escolha de profundidade de funil, não de magnitude, a magnitude está empatada e é indecidível sem volume. Três perguntas abrem: se há recuperação ativa dos 20% (ambiguidade 6, nunca perguntada), qual o tamanho dos contratos que nunca geraram cobrança (fora do denominador dos 80%, sem DRI e sem prazo) e qual a magnitude do abono e contestação do pós-pago (ambiguidade 7). |
| 4 | **Compromisso** | Associada às etapas 3, 4 e 6, com a etapa 6 (ativação, publicação do primeiro anúncio) como núcleo. A política implícita já está formulada no formato da regra 4 e é testável: a empresa transfere integralmente ao anunciante o trabalho de ativação, não publica em nome dele, exige integrador de terceiros ou publicação unitária, mantém cadastro e senha separados no CanalPro e só libera login depois do pagamento, criando uma janela entre pagamento e primeiro anúncio sem responsável. NÃO diagnosticar antes de Retenção e NÃO tratar o 12% como vazamento independente: pela leitura mais provável das falas ele é fatia de quem SAI, portanto perfil de quem churna no 1º mês, e empilhá-lo sobre o churn conta os mesmos clientes duas vezes. Confirmar o denominador com a OLX é pré-requisito do diagnóstico desta trava. |
| 5 | **Qualificacao** | Associada às etapas 2 e 3. Fica em quinto pela regra de Goldratt, está acima de Compromisso no funil, e porque o material que existe hoje não sustenta score: as definições de MQL ('nome, e-mail, telefone e em alguns canais documento') e de SQL (elegibilidade por CNPJ da área) são declaração verbal em reunião (00:44:38), e não há no repositório nem foi entregue pelo cliente qualquer política de qualificação, critério escrito, SLA ou ICP versionado. Pela regra 5, as dimensões de ICP documentado e de processo de qualificação ficam null até o artefato formal chegar. O paradoxo é que a TAXA existe e foi vista na tela: o dashboard de funil B2B tem MQL→SQL e SQL→venda com 12 meses de histórico. Esta trava é a que mais depende de uma extração e menos de uma coleta nova. |
| 6 | **Exposicao** | ÚLTIMA ENTRE AS RESTRIÇÕES, POR REGRA DE GOLDRATT, Retenção antes de Exposição, sempre. Associada às etapas 1 e 2. Diagnosticá-la agora seria caro e cego por duas razões independentes: (a) o maior canal do mapa é em parte artefato de mensuração, o próprio slide anota que campanha paga para WhatsApp 'entra tudo como Direto', logo Pago (16%) [D] está subestimado e CAC por canal não existe hoje; (b) sobre DEMANDA não há evidência em nenhuma direção, porque ela é imensurável no estado atual. Três argumentos que circulavam como evidência de demanda foram retirados: participação de origem não é medida de capacidade, ausência de self-service não é medida de etapa não medida, e 'ninguém alegou escassez' é argumento do silêncio numa sessão em que ninguém perguntou. Aumentar topo com Retenção e Decisão em aberto só aumenta o custo do desperdício. |
| 7 | **Atencao** | NÃO AGENDADA. Nenhuma das dez etapas do fluxo mapeia para esta trava, o material da sessão de 28/08 não descreve nenhuma estação de captura de atenção com volume, taxa ou tempo. Registrar como não mapeada é diferente de registrar como saudável: não há dado em nenhuma direção, e nenhum score deve ser produzido. Reavaliar quando o slide de FLUXOS for versionado (L28) e o diagrama do caminho de aquisição, que hoje falta (L1), for entregue. |
| 8 | **Interesse** | NÃO AGENDADA, pelo mesmo motivo: nenhuma etapa do fluxo narrado mapeia para ela. Ausência de mapeamento não é evidência de saúde nem de trava, é ausência de dado, e o campo fica sem score. Reavaliar junto com Atenção quando o material de topo de funil (diagrama de canais, LPs de marketing, réguas de CRM) chegar com volume e taxa. |

---

## Números apurados que existem no projeto

Todos com propriedade e período. A coluna final diz se o número entra no mapa, e por quê.

| Métrica | Valor | Propriedade | Período | No mapa? | Por quê |
|---|---|---|---|---|---|
| `begin_checkout` | 2.686.897 | GA4 OLX App + Web (152644854), tier 360 | agosto/2026 | não | Mistura app, web e consumidor. Não é segmentável ao recorte B2B enquanto seller_category estiver vazio (auditoria vii, achado 4, condicional). Marcado como evento-chave. |
| `purchase` | 565.258 | GA4 OLX App + Web (152644854) | agosto/2026 | não | Conversão contaminada: a tag 426 do GTM-KGFGVFC dispara purchase no gatilho 215, que escuta begin_checkout (auditoria vii, achado 1). A parcela B2B contaminada dentro dos 565.258 nunca foi isolada, então nenhum percentual de contaminação pode ser afirmado. |
| `ad_insertion` | 4.602.128 | GA4 OLX App + Web (152644854) | agosto/2026 | não | É, ao pé da letra, anúncio publicado por mês, mas somando profissional e particular. O corte falta, não o número. Evento-chave. |
| `ad_edition` | 4.140.566 | GA4 OLX App + Web (152644854) | agosto/2026 | não | Mesmo motivo do ad_insertion, e não está marcado como evento-chave (auditoria vii, achado 13). |
| `ad_remove` | 157.632 | GA4 OLX App + Web (152644854) | agosto/2026 | não | Não segmentável, não é evento-chave, e a origem (app ou outro contêiner) não foi apurada (auditoria vii, achado 8). |
| `qualified_lead_autos_pro` | 4.680.465 | GA4 OLX App + Web (152644854) | agosto/2026 | não | O nome sugere lead qualificado de Autos profissional, o que o tornaria candidato a numerador da etapa 3, mas o que o evento mede nunca foi confirmado com a OLX, e a magnitude (4,68 mi/mês) é incompatível com um funil B2B de anunciante. Perguntar junto com generate_lead_pro. |
| `lead_b2b` | 0 | GA4 OLX App + Web (152644854) | agosto/2026 | sim | Entra como ACHADO, não como volume: a tag 429 está montada e ativa e a propriedade registrou zero eventos, porque a tag 349 identifica o lead por posição no DOM (auditoria vii, achado 3). É a prova de que o topo do funil B2B instrumentado não tem numerador. |
| `Nomes de evento distintos` | 219 | GA4 OLX App + Web (152644854) | leitura de 01/09/2026 | não | Quais dos 219 são evento-chave é o item 2.4 da coleta-pendente.md, não marcado. Só sete volumes de agosto estão registrados. |
| `session_start (marcado como EVENTO-CHAVE)` | 13,27 mi | GA4 VivaReal (407391347), tier 360 | agosto/2026 | não | Início de sessão marcado como conversão infla qualquer taxa relatada e, se importado no Google Ads, treina o Smart Bidding para comprar sessão. É achado de Cegueira, não volume de etapa. Se está importado no Google Ads segue sem resposta (ação 2 da pendência 13). |
| `generate_lead` | 830.116 | GA4 VivaReal (407391347) | agosto/2026 | sim | Entra como CANDIDATO A NUMERADOR da etapa 3, com duas confirmações pendentes: o achado 20 da auditoria (vii) mostra que o gatilho [208] lead_dbm dispara as tags 209 (G-6TV9FSHYVM) e 356 (G-ZBYP2KJ7L9), logo qualquer consolidação que some as duas propriedades conta cada lead duas vezes. A própria auditoria instrui confirmar qual é a de referência antes de usar como numerador do fluxo de receita. |
| `generate_lead_pro` | 661.144 | GA4 VivaReal (407391347) | agosto/2026 | sim | Entra como o CANDIDATO A NUMERADOR mais forte. PENDENCIAS.md:346 diz: 'é o primeiro indicador possivelmente B2B que apareceu em todo o projeto. Se ele for mesmo o lead de anunciante, é o numerador que falta para o fluxo de receita.' O que ele mede segue sem resposta (ação 1 da pendência 13). É a pergunta mais barata do projeto. |
| `Sessões do canal AI Assistant` | 247.694 | GA4 VivaReal (407391347) | junho–agosto/2026 (leitura de 31/08/2026) | não | Linha de base da auditoria (iii) GEO, não do fluxo de receita B2B. Registrado em dados/client.json. |
| `Sessões` | 2,47 mi | GA4 Grupo OLX (503925542), tier STANDARD (gratuito) | junho–agosto/2026 | não | É a propriedade que carrega ads., imoveis., autos., o institucional e vender.olx.com.br, toda a superfície B2B do escopo, e tem ZERO eventos-chave. Volume de sessão sem definição de resultado não serve de etapa; serve de evidência da pré-condição de Cegueira. |
| `Sessões` | 1,14 mi | GA4 Autos 360 / Ex-Altimus (516288559), tier 360 | junho–agosto/2026 | não | 449 nomes de evento distintos e nenhum marcado como conversão. O dado existe, ninguém definiu o que é resultado. |
| `Nomes de evento distintos` | 449 | GA4 Autos 360 (516288559) | leitura de 31/08/2026 | não | Zero eventos-chave sobre 449 eventos instrumentados, em propriedade de tier pago. Evidência de Cegueira, não etapa de fluxo. |
| `page_view` | 11,19 mi | GA4 ANAPRO (469847974) | junho–agosto/2026 | não | Nenhum evento-chave. Page view não é etapa de fluxo de receita. |
| `Sessões` | 119 | GA4 OLX PRO (382768600) | três meses até 31/08/2026 | não | É o produto do anunciante profissional, exatamente o recorte B2B contratado, e registra 119 sessões em três meses, só tráfego direto. Significa propriedade órfã, não produto sem tráfego. Não é volume utilizável. |
| `Eventos registrados` | 0 | GA4 OLX Pro Landing (382776122) | junho–agosto/2026 | não | Zero evento no período. Achado de instrumentação. |
| `Contas de Google Ads vinculadas` | 7 (9221562141 · 6794249680 · 7581320191 · 6386557247 · 1973081572 · 5004050899 · 4632447364) | GA4 ZapImóveis (407374944) | leitura de 31/08/2026 | não | Nenhuma delas é a 526-656-0190, a única a que a V4 tem acesso. Mede o tamanho do que a V4 NÃO enxerga, não uma etapa do fluxo. |
| `Investimento em Google Ads` | R$ 2.746.029,59 | Não é propriedade GA4, V4MOS, MCC ZAP+ VivaReal 526-656-0190 | 01/01/2025 a 14/09/2026, coleta de 14/09, com quebra mensal e por campanha | não | RECOLETADO EM 14/09 sobre janela larga, substitui os R$ 1,91 mi de 22/06. Agora tem quebra: 23 campanhas e série mensal. Duas ressalvas impedem o uso: **só 11 meses têm dado, faltam nov/2025 a abr/2026 inteiros**, origem não apurada entre pausa real e falha de ingestão; e a conta não separa B2B de B2C (pendência 12). Sem CAC por canal e sem certeza de recorte, não entra no mapa. |
| `Cliques em Google Ads` | 10,17 mi | V4MOS, MCC 526-656-0190 | 01/01/2025 a 14/09/2026 | não | Mesmo motivo do investimento. CTR de 18,03% e CPA de R$ 3,06 sobre 896.625 conversões, e é justamente o CPA que não pode ser lido: a coleta não diz QUAL ação de conversão o Google está contando, item 4 da lista de exports do [mapa de números](mapa-de-numeros.md). |
| `Registros de campanha / campanhas distintas` | 23 campanhas | V4MOS, MCC 526-656-0190 | 01/01/2025 a 14/09/2026 | não | Eram 8 na leitura de 22/06. O retorno bruto agora **está versionado como cache regenerável** em `dados/cache/v4mos-2026-09-14.json`, fora do git por peso (1,8 MB), então dá para recalcular e separar por campanha. |
| `Meta Ads · investimento` | R$ 7.375.303,34 | V4MOS, contas 612188193108418 (VR ZAP+) e 1742214902479721 (OLX Autos B2B) | 01/01/2025 a 14/09/2026 | não | **O Meta saiu de zero.** As contas pedidas em 21/08 foram concedidas no lote de 10/09, o V4MOS passou a ingerir em 12/09 e a recoleta de 14/09 cobre 21 meses. São 90 campanhas e 1.079 anúncios. O Meta pesa **2,7 vezes o Google**, o que inverte a leitura de mídia que o projeto carregava. Não entra no mapa porque a conta não separa B2B de B2C: R$ 7,38 mi é mídia do grupo, majoritariamente consumidor. |
| `Meta Ads · impressões, alcance e cliques` | 1,88 bi · 1,41 bi · 29,41 mi | V4MOS, duas contas de Meta | 01/01/2025 a 14/09/2026 | não | CPM de R$ 3,91 e CTR de 1,56%. **É a única série mensal de mídia contínua que o projeto tem**, 21 meses sem nenhum mês faltando, e por isso é a única utilizável no forecast. Mesmo bloqueio de recorte B2B. |
| `Métricas unitárias de mídia` | CPM R$ 3,91 · CTR 1,56% · CPC R$ 0,25 (Meta) · CTR 18,03% · CPC R$ 0,27 · CPA R$ 3,06 (Google) | V4MOS, dois lados | 01/01/2025 a 14/09/2026 | não | CORREÇÃO DE UMA AFIRMAÇÃO DESTE DOCUMENTO: até 12/09 ele dizia que não havia nenhuma métrica unitária de mídia no repositório. Há, desde 14/09. Não entram no mapa por dois motivos: recorte B2B ausente, e o CTR de 1,56% contra 18,03% denuncia que as duas contas contam clique de formas diferentes, o que precisa ser resolvido antes de somar ou comparar. |
| `Contêineres de GTM auditados / inventariados` | 11 exports recebidos · 6 auditados · 22+ contêineres numa das quatro contas do grupo | GTM, contas 94905 · 6326134112 · 4412254379 · 2971905372 | exports de 01/09 e 02/09/2026 | não | Contagem apurada de configuração, não de negócio. Duas das quatro contas estão inteiramente por auditar, e cinco exports já no repositório ainda não foram lidos, a frase 'a auditoria (vii) cobre o escopo B2B' não se sustenta até isso chegar. |
| `Nível de serviço das propriedades GA4` | 360 (pago): VivaReal 407391347 · ZapImóveis 407374944 · OLX App + Web 152644854 · Autos 360 516288559. STANDARD (gratuito): GA4 Grupo OLX 503925542 | GA4, cinco propriedades | leitura de 01/09/2026 | não | A única propriedade no tier gratuito é a que carrega toda a superfície B2B do escopo contratado. É alocação de orçamento de ferramenta, evidência de política implícita para a pré-condição de Cegueira, não etapa de fluxo. |

---

## O que falta para fechar

- CONFIRMAR O QUE `generate_lead_pro` MEDE, é a pergunta mais barata do projeto e o repositório já
a formulou. 661.144 eventos em agosto/2026 na propriedade GA4 VivaReal (407391347), e
PENDENCIAS.md:346 diz que 'se ele for mesmo o lead de anunciante, é o numerador que falta para o
fluxo de receita'. Junto: qual das duas propriedades é a de referência para `generate_lead`
(830.116), porque o gatilho [208] lead_dbm dispara as tags 209 e 356 em duas propriedades e
qualquer consolidação conta cada lead duas vezes, auditoria (vii), achado 20. Ações 1 e 2 da
pendência 13, sem resposta registrada.
- VOLUME ABSOLUTO SEGMENTÁVEL AO RECORTE B2B. Correção importante em relação à versão anterior deste
mapa: NÃO é verdade que 'não existe um único número de anúncios publicados/mês ou leads/mês em
documento nenhum'. Existem, apurados na API do GA4: ad_insertion 4.602.128 e ad_edition 4.140.566
(agosto/2026, OLX App + Web 152644854), registrados em dados/client.json e na auditoria (vii). O
que falta é o CORTE profissional × particular (`seller_category`), não o número. Continuam de fato
inexistentes em documento nenhum: clientes ativos, contratos/mês, ticket médio e receita por
vertical.
- LINKS DOS DASHBOARDS DE FUNIL B2B E DE CANAL ONLINE. O trabalho já mudou de coletar para EXTRAIR:
as taxas de qualificação (MQL→SQL) e de conversão (SQL→venda) existem lá, por vertical, canal,
time e período, com histórico de 12 meses. Lacuna 1 da ata, DRI Leonardo Rosa, prazo '-' (não
acordado na sessão; a ata manda não inventar). Primeira extração a fazer: recuperar as '414
vendas' com período, vertical e denominador.
- TEMPO MÉDIO DE PASSAGEM POR ETAPA: zero das dez etapas tem, e o campo tempo_medio_dias sai null
nas dez. Sem ele nenhuma das perguntas-gatilho de tempo do POP é respondível, e a tabela do
roteiro segue vazia.
- PERÍODO DE APURAÇÃO DOS SEIS PERCENTUAIS. O slide não traz data-base, janela nem safra. O
dashboard olha 12 meses por padrão; o slide de FLUXOS diz 'todo o período histórico' (L5). Não se
sabe se 89%, 12%, 80% e 8–10% são de 12 meses, do mês corrente ou do histórico inteiro.
- SEPARAÇÃO POR VERTICAL EM QUATRO DOS SEIS PERCENTUAIS. Só as etapas 4 (25%/10%) e 7 (89%, só
Imóveis) vêm quebradas. Entrada, Pagamento, Publicação e Churn vêm somados sobre Autos e Imóveis,
que têm modelo de anúncio diferente (inserção × slot) e modelo de cobrança diferente (pré ×
pré/pós). Somar economias diferentes produz mapa errado com aparência de mapa certo, passo 1 do
POP e critério de aceite da própria sessão, não cumprido. CONSEQUÊNCIA DIRETA SOBRE ESTE JSON: o
schema da skill pede `unidades[]`, uma entrada para Autos e outra para Imóveis, cada uma com seu
`etapas[]`. Este entregável emite UM `etapas[]` consolidado porque quatro dos seis percentuais
chegaram somados sobre as duas verticais, separá-los agora seria inventar o corte. A separação em
duas unidades é entrega pendente e depende deste item.
- RESOLVER 'RECEITA' × 'BASE' NO 50% DA ETAPA 2. O slide diz receita, a fala de 00:05:42 diz base, e
o repositório carrega as duas versões em documentos diferentes. Enquanto isso durar, a etapa 2 não
entra em reconciliação. Falta também a fatia de renovação e de Inside/Field Sales que fecha os
100%.
- CONFIRMAR O DENOMINADOR DO 12% (etapa 6) E, SÓ DEPOIS, PROPAGAR A CONSEQUÊNCIA. Se confirmado que
o 12% é fatia de quem SAI, p(publicação)=88% deixa de ser termo independente da identidade de
regime de 03-estrategia/meta-do-projeto.md §4, e a linha 'Publicação 88%→92% = +4,5%' e os tetos
de +26% e +44% precisam ser refeitos. NENHUMA aritmética deve ser alterada antes da confirmação da
OLX: a base textual é transcrição automática do Gemini, mal segmentada.
- UNIDADE DO CHURN: logo ou receita (ambiguidade 4). Toda a derivação de 63–72%/ano, a constante de
tempo de 11 meses, a tabela de elasticidades e o cascateamento por ciclo pendem dessa única
resposta.
- DISTRIBUIÇÃO DO 89% POR CLIENTE (ambiguidade 1). O 89% é por anúncio; o churn é por
cliente/pagamento. Sem a taxa por cliente as duas pontas da cadeia causal não se ligam.
- O QUE CONCENTRA OS LEADS NOS 11% (ambiguidade 2), com a pista da deduplicação reaberta, o número
do kick-off tem conflito na própria fonte ('15 milhão' na fala, '1,5 milhão' no resumo) e precisa
de reapuração antes de qualquer uso.
- RECUPERAÇÃO DOS 20% QUE NÃO PAGAM (ambiguidade 6) e MAGNITUDE DA 'ALTA TAXA DE ABONO E
CONTESTAÇÃO' NO PÓS-PAGO (ambiguidade 7). Nenhuma das duas foi perguntada na sessão. E, junto com
a segunda, o nó 3B-11: quando a receita é reconhecida e quando o contrato passa a existir,
pergunta 3 do roteiro, levada à sessão e não fechada em ata.
- PROXY DE PERFORMANCE PARA IMÓVEIS. Declarado inexistente (Leonardo Costa, 00:55:01). Enquanto não
houver, a causa declarada do churn não é medida na vertical onde o churn dói.
- REGISTRO ESTRUTURADO DE MOTIVO DE CANCELAMENTO. Pergunta 6 do roteiro; grep na transcrição de
28/08 devolve só a atribuição genérica a baixa performance, e a pergunta também ficou sem resposta
capturada no kick-off.
- POLÍTICA DE QUALIFICAÇÃO ESCRITA: critério de MQL/SQL, estágios do CRM, SLA e ICP documentado. As
definições de 00:44:38 são declaração verbal em reunião; não há artefato formal no repositório nem
entregue pelo cliente. Pela regra 5, as dimensões correspondentes da Trava de Qualificação ficam
null até o documento chegar. Abrir linha em PENDENCIAS.md com DRI e prazo.
- QUANTO DO CANAL DIRETO É MÍDIA PAGA SEM ATRIBUIÇÃO (L15/F12), DRI 'a definir', sem prazo.
Enquanto durar, CAC por canal não existe e a realocação de verba é cega.
- SE O SITE GRAVA `user_olx` POR CÓDIGO PRÓPRIO, FORA DO GTM. É um F12 na página, e decide se o
achado 4 da auditoria (vii), denominador não segmentável, existe ou 'cai por terra', nas
palavras da própria auditoria. Nada no repositório registra que a verificação tenha sido feita ou
a pergunta enviada à OLX.
- ARQUIVOS ORIGINAIS: o slide de FLUXOS não está versionado (L28), conferido com find em assets/, o
único original de negócio versionado é jornada-do-cliente-profissional.png; os percentuais de
canal existem só em prosa. O da jornada é captura de tela, com o original no Drive (L27). Material
de cliente que não pode ser conferido contra a fonte não sustenta comitê.
- O PAR DE ENTREGÁVEIS DESTE POP NÃO EXISTE: não há dados/outputs/dre-fluxo-receita.json nem
02-diagnostico/fluxo-de-receita.md (ou mapeamento-fluxo-receita.md), citados como destino em
QUATRO documentos do repositório (jornada-do-cliente-profissional.md, lacunas-do-fluxo-de-
receita.md, a ata de 28/08 e 02-diagnostico/README.md) e em CINCO skills (dre-fluxo-receita, dre-
forecast, dre-consolidacao-causal, dre-diagnostico-trava, dre-continuar). dados/outputs/ contém
apenas meta-do-projeto.json. Regra do repositório: skill que gera um sem o outro está incompleta.
Esta reemissão entrega o lado de máquina no schema canônico; o .md humano continua faltando.
- CONFORMIDADE DE SCHEMA: RESOLVIDO NESTA REEMISSÃO, COM UMA EXCEÇÃO NOMEADA. Passaram a existir
como campo, com null explícito onde não há dado: `tempo_medio_dias` (null nas dez),
`perda_absoluta` (null nas dez), `taxa_entrada` (não-null só na etapa 5), `estimado` como booleano
(true nas etapas 6, 8 e 9, onde a marcação [E] já existia no texto), `travas_associadas[]` por
etapa (o campo que liga este mapa ao score 0–25 de cada trava), `ranking_perda[]`, `reconciliacao`
com os quatro campos null, `travas_prioritarias[]` e os campos de summary do PADRAO-OUTPUT.md. A
EXCEÇÃO é `unidades[]`: continua não emitido, porque quatro dos seis percentuais chegaram somados
sobre Autos e Imóveis e separá-los seria inventar o corte, ver o item de separação por vertical
acima.
- AS SETE AMBIGUIDADES DO SLIDE E AS QUATRO LACUNAS DA SESSÃO AINDA NÃO SÃO LINHA DE PENDENCIAS.md,
com DRI e prazo. A ata registra prazo '-' nas quatro e DRI 'a definir' em uma, e
02-diagnostico/coleta-pendente.md não menciona a jornada nem os dashboards.
- CORRIGIR OS TIMESTAMPS CITADOS NOS DOCUMENTOS DO REPOSITÓRIO. Conferidos contra os cabeçalhos `###
**hh:mm:ss**` da transcrição: o 89% é 00:19:40 e está citado como 00:18:09; '3 leads em 7 dias' é
00:55:01 citado como 00:53:50; o benchmark de destaque é 01:00:35 citado como 00:59:26; a
demonstração dos dashboards por Lu Machim é 00:07:00–00:08:59, não 00:05:42, que é fala de
Carolina Dallolio; a frase do touch point de app é 00:40:31, não 00:38:26; o self-service é
00:39:34, com 00:41:15 sendo só a paráfrase de Michelle Morais; e o hedge de Leonardo Costa sobre
os 80–90% dos 12% está em 00:14:12. Não muda nenhum valor, mas em material de cliente uma citação
que não bate ao ser conferida derruba a credibilidade das outras seis taxas.

---

## Ressalva metodológica

O QUE ESTE MAPA NÃO É. Não é o fluxo de receita mapeado. É o fluxo NARRADO, com origem nomeada.
Pelo próprio POP, etapa sem volume, taxa e tempo não está mapeada, e das dez etapas acima, ZERO
têm volume absoluto e ZERO têm tempo médio. Seis carregam um percentual declarado cada; e DAS
SEIS, APENAS UMA, o 80% de pagamento da 1ª fatura, é taxa de passagem entre etapas. As outras
cinco são coisas diferentes somadas sob o mesmo rótulo: participação de origem (50%, com
denominador em disputa entre receita e base), participação de receita por canal (25% Autos / 10%
Imóveis), fatia de quem sai (12%), participação de estado por anúncio (89%, só Imóveis) e hazard
mensal sobre a base (8–10%). Chamá-las de 'as seis taxas do funil', como fazem 03-estrategia/meta-
do-projeto.md §3 e 02-diagnostico/jornada-do-cliente-profissional.md, é um placar de completude
somado com itens incomensuráveis, mapa errado com aparência de mapa certo. TODAS SÃO DECLARADAS,
NENHUMA É APURADA. É por isso que `taxa_entrada` sai não-null em uma única etapa das dez: o campo
canônico só admite passagem etapa→etapa, e só existe uma.

Os seis percentuais vieram de uma apresentação que a própria OLX enquadrou como educacional e como
jornada, explicitamente NÃO como funil ('aqui não tô trazendo nenhuma visão de funil ou nada
disso, uma visão de jornada mesmo do nosso cliente profissional', Carolina Dallolio, 00:04:20), é
por isso que vêm sem denominador, sem volume e sem período. O original nem é arquivo: é captura de
tela, sem metadado, sem data-base e sem a fonte do número dentro do slide. Os percentuais de canal
da etapa 1 estão pior: o slide de FLUXOS não foi versionado, e eles existem apenas em prosa em
duas anotações de reunião da V4, as duas decomposições que 'fecham' vêm do mesmo artefato e
fecham no mesmo 97%, o que demonstra consistência interna do slide, não acurácia, e não é
reexecutável. Todo número deste mapa carrega [D] obrigatoriamente, no ponto de uso e não só nesta
ressalva. E a transcrição é automática (Gemini no Google Meet, do lado da V4), com segmentação
ruim: leituras que dependem de onde cai uma vírgula não sustentam aritmética.

DOIS NÚMEROS QUE CIRCULAM COMO SE FOSSEM DO CLIENTE E NÃO SÃO: o 88% de publicação é 100−12%
construído pela V4 sobre uma taxa que é de NÃO publicação e que, pela leitura mais provável, é
medida sobre quem sai; e o 9% de churn é o ponto médio ESCOLHIDO dentro da faixa declarada 8–10%.
Os dois estão rotulados [D] na fonte, em 03-estrategia/meta-do-projeto.md §4, e o rótulo está
errado: só o 80% é declarado ali; 88% e 9% são construções da V4 e devem ser [E]. Além do duplo-
cômputo da publicação, a identidade de regime daquele §4 (contratos × pagamento × publicação ×
ticket ÷ churn) é um produto sobre um SUBCONJUNTO do fluxo: não tem termo para a Qualificação
(etapa 3), nem para a Entrega de leads (etapa 7, a causa declarada do churn), nem para o abono e
contestação do pós-pago (etapa 9, que incide sobre receita já reconhecida). Os tetos de +26% e
+44% são, portanto, tetos de um modelo de TRÊS termos apresentados como 'teto matemático do
sistema atual' de um fluxo de dez etapas. Refazer antes de qualquer material de comitê.

O QUE A REGRA 7 EXIGE E NÃO PODE SER VERIFICADO. A receita derivada do funil tem de bater com a
declarada dentro de 5%. Isso não é executável hoje por NENHUM dos dois caminhos. Pela via do
cliente, falta tudo o que a multiplicação pede: volume de entrada, ticket médio, receita declarada
por vertical e os 100% fechados da etapa 2, cujo denominador está dividido entre 'receita' e
'base' em duas fontes. O bloco A do checklist (A1–A3) está com os três itens em ⚪, nenhum
recebido, e nenhuma concessão de ferramenta o destrava. Pela via instrumentada, o GA4 também não
fecha: o funil B2B derivável hoje tem NUMERADOR INEXISTENTE (`lead_b2b` = 0 em agosto/2026, com a
tag 429 ativa e a tag 349 identificando o lead por posição no DOM, achado 3), CONVERSÃO
CONTAMINADA (a tag 426 de purchase dispara no gatilho 215, que escuta begin_checkout, em Planos
Profissionais e PAYG, achado 1) e um DENOMINADOR PROVAVELMENTE NÃO SEGMENTÁVEL, e aqui a
formulação importa: a única tag do export que grava `user_olx` está pausada, e `seller_category`,
que separa anunciante profissional de particular, depende dela; mas a própria auditoria escreve 'A
confirmar: se o site grava user_olx por código próprio, fora do GTM. Se gravar, o problema não
existe', e a Ressalva de leitura 2 repete que 'o achado 4 cai por terra' nesse caso. Isso é
inferência sobre export de GTM, condicionada a uma verificação que ninguém fez, não é estado
apurado do rastreamento do cliente, e não deve ir ao Board como se fosse. Apurados de verdade
nessa frente são apenas a contagem de API (`lead_b2b` = 0) e a configuração exportada do gatilho
de purchase. A auditoria também ressalva explicitamente que ao menos um achado (o 18) descreve
configuração de WORKSPACE, que não é necessariamente o que está no ar; se os demais exports também
forem de workspace, isso precisa ser confirmado com a OLX antes de qualquer conclusão sobre
produção, a generalização 'todos os exports são de workspace' não está escrita em documento
nenhum e não deve ser afirmada.

CORREÇÃO DE UMA AFIRMAÇÃO FALSA DA VERSÃO ANTERIOR: não é verdade que os seis eventos da
propriedade OLX App + Web sejam 'os únicos números apurados que existem no projeto'. Eles são os
números apurados DAQUELA propriedade (152644854, agosto/2026). O projeto tem muito mais apurado,
tudo com fonte, propriedade e data-base, session_start 13,27 mi, generate_lead 830.116 e
generate_lead_pro 661.144 na GA4 VivaReal (407391347, agosto/2026); 2,47 mi de sessões na GA4
Grupo OLX e 1,14 mi na Autos 360 com 449 nomes de evento, 11,19 mi de page_view na ANAPRO e 119
sessões na OLX PRO (jun–ago/2026); 247.694 sessões do canal AI Assistant; os tiers de serviço das
cinco propriedades; e, fora do GA4, **R$ 10,12 mi de investimento medido em mídia na recoleta de
14/09** (Meta R$ 7,38 mi em 90 campanhas e 1.079 anúncios, Google R$ 2,75 mi em 23 campanhas,
01/01/2025 a 14/09/2026), que substituiu os R$ 1,91 mi agregados do MCC 526-656-0190 que este
parágrafo citava. Está tudo em
PENDENCIAS.md, em dados/client.json e no campo numeros_apurados deste JSON, e o próprio
client.json anota: 'Nenhum numero acima foi usado ainda em diagnostico. Sao leituras de
verificacao de acesso.' Bastaria um board member abrir o PENDENCIAS.md do próprio projeto para
derrubar a frase de exclusividade, e com ela a autoridade do resto da ressalva. O ponto
verdadeiro é outro e continua de pé: nenhum desses números é volume de etapa do funil B2B, porque
nenhum está segmentado ao recorte profissional.

O QUE ESTE MAPA TAMBÉM NÃO É: não é diagnóstico de trava e não nomeia restrição. dados/client.json
registra score null nas oito travas e restricao_identificada null, e assim deve continuar. A
cadeia entrega-zero → churn é RELATO ÚNICO DO CLIENTE (duas falas da mesma pessoa na mesma
sessão), sem corroboração instrumentada; o voto do kick-off é percepção e a regra 5 não o admite
como evidência. O achado de atribuição do canal Direto é evidência formal de um BURACO DE
MENSURAÇÃO, documentado pelo próprio cliente, alimenta as evidências da pré-condição de Cegueira,
não produz nota, e a regra 5/6 não se aplica ali: ela gateia notas 4 e 5, que na escala do
playbook (0–10 travada, 21–25 forte e governada) são afirmações de que a dimensão está SAUDÁVEL. A
frase de 02-diagnostico/lacunas-do-fluxo-de-receita.md:50, 'Trava de Cegueira com evidência
formal... Nota acima de 3 no score de trava exige evidência formal: aqui ela existe', usa a regra
ao contrário e precisa ser corrigida na origem. E Cegueira, pelo playbook, 'não é uma restrição de
receita, é uma pré-condição'.

RESPOSTA À PERGUNTA-GATILHO SOBRE DEMANDA, com o escopo que a evidência sustenta: há evidência
DECLARADA de problema de entrega e de conversão, a entrega mediana do produto é zero em Imóveis
(89% dos anúncios sem lead) e o churn é atribuído pelo cliente a baixa performance. Sobre DEMANDA
não há evidência em nenhuma direção, porque ela é hoje imensurável: o canal Direto está inflado
por mídia sem atribuição e `lead_b2b` = 0. Três argumentos que a versão anterior contava como
evidência foram retirados: 'metade da aquisição depende de prospecção humana' é participação de
origem, não medida de capacidade; 'a expansão não tem self-service' é ausência de funcionalidade
sobre uma etapa em que nada foi medido; e 'ninguém alegou escassez de demanda' é argumento do
silêncio, extraído de uma sessão em que ninguém perguntou sobre demanda. Quanto a se o fluxo
cresce linear ou aos trancos: não há série temporal em documento nenhum, então fica sem resposta;
o que a estrutura sugere [E] é uma base de recorrência que responde com atraso longo.

═══════════════════════════════════════════
MAIOR VAZAMENTO: POR QUE O CAMPO NÃO EXISTE NESTE ENTREGÁVEL
═══════════════════════════════════════════

NÃO É POSSÍVEL ELEGER UM MAIOR VAZAMENTO NESTE ENTREGÁVEL, E DIZER QUE É É QUEBRAR O PRÓPRIO POP.
O passo 4 do POP Fluxo de Receita (.claude/skills/dre-fluxo-receita/SKILL.md) manda ordenar as
etapas por PERDA ABSOLUTA de receita potencial, não por taxa percentual, 'uma taxa ruim em cima
de volume pequeno perde para uma taxa mediana em cima de volume grande', e o checklist de
fechamento repete: 'Ranking é por perda absoluta, não por percentual'. Nenhuma das dez etapas tem
volume absoluto, logo perda_absoluta é null nas dez. Pior: três das dez (Qualificação, Pós-pago de
Autos, Expansão) não têm sequer taxa, e a de pós-pago carrega um vazamento de magnitude
desconhecida sobre receita JÁ RECONHECIDA, 'alta taxa de abono e contestação', o único bullet do
slide sem número, ambiguidade 7, nunca perguntada. Um vazamento não medido que incide depois do
reconhecimento pode ser maior que qualquer um dos medidos, e não pode ser excluído do topo do
ranking. Declarar um máximo sobre um conjunto com membros não medidos é somar um score com
dimensão faltando. É por isso que `ranking_perda[]` sai com perda_absoluta null nas dez e com o
campo `impossivel_ordenar` em cada item, em vez de uma ordem.

O QUE O MATERIAL SUSTENTA, COMO HIPÓTESE NOMEADA E SEM ORDINAL: a cadeia entrega-zero → percepção
de baixa performance → churn → as entradas não compensam churn mais downgrade → net de receita
negativo em Imóveis (UDE #1, Iuna Scheffler, kick-off 24/08, 01:07:38). A cadeia é COERENTE E NÃO
ESTÁ PROVADA EM NENHUM ELO. Três ressalvas duras, que vêm antes do encadeamento e não depois: (i)
o churn de 8–10% ao mês [D] não tem unidade declarada, logo ou receita, ambiguidade 4 aberta, e
sem base absoluta não se converte em dinheiro; (ii) o 89% é POR ANÚNCIO e só de Imóveis, e a
distribuição por cliente, que é o que se liga ao churn, nunca foi medida nem pedida (ambiguidade
1); (iii) em Imóveis, a vertical onde o churn dói, a performance NÃO é medida, o proxy de 3 leads
em 7 dias existe só na OLX/Autos, e Leonardo Costa declarou que para real estate não há número
(00:55:01).

GRAU PROBATÓRIO, CORRIGIDO: isto é RELATO ÚNICO DO CLIENTE, não convergência de três fontes. O 89%
(00:19:40) e o churn com 'o principal motivo é atribuído a baixa performance' (00:22:16) são a
MESMA falante, Carolina Dallolio, na MESMA sessão, separados por cerca de dois minutos de fala
contínua: são duas frases de uma narrativa, não duas fontes convergindo. O voto do kick-off
(Retenção 3 × Qualificação 2) é percepção da liderança, rotulada como tal pelo próprio repositório
(03-estrategia/meta-do-projeto.md:77, 'Percepção, não diagnóstico'), e a regra 5/6 não a admite
como evidência. Não há corroboração instrumentada: o caminho GA4 está quebrado (lead_b2b = 0,
seller_category provavelmente vazio, purchase contaminado). dados/client.json confirma
travas.*.score = null nas oito, e restricao_identificada = null.

ARITMÉTICA: A FRASE QUE ORDENA AS ALAVANCAS ESTAVA ERRADA E FOI CORRIGIDA. Circulava, aqui e em
03-estrategia/meta-do-projeto.md §4.1, que 'em qualquer ponto da faixa declarada, um ponto de
churn vale mais que dez pontos de conversão de pagamento'. É falso em dois dos três pontos da
faixa. Pela identidade de regime que o próprio documento usa (receita ∝ p(pagamento)/churn): a 8%
de churn, −1 p.p. vale +14,3%; a 9%, +12,5%; a 10%, +11,1%. Levar o pagamento da 1ª fatura de 80%
para 90% vale +12,5%. Logo as duas alavancas EMPATAM no ponto médio (a própria frase admite isso
na linha seguinte, autorrefutando-se) e o pagamento VENCE no topo da faixa declarada. A versão
anterior citava só o extremo favorável (8%) e omitia o de 10%, que a fonte original traz
explicitamente. Todos esses números são [E]: derivação da V4 sobre taxas declaradas. E o argumento
de recorrência não é razão adicional, a recorrência já está integralmente precificada dentro da
elasticidade, porque é por ser recorrente que o churn aparece no denominador; contá-la de novo
dobra o peso de um único argumento.

CONCLUSÃO OPERACIONAL: entre churn e pagamento da 1ª fatura há EMPATE TÉCNICO, indecidível até
chegarem a unidade do churn (ambiguidade 4), o baseline real e o volume absoluto. Os 20% que
contratam, geram cobrança e nunca pagam são o SEGUNDO CANDIDATO pela taxa declarada, e não é
possível dizer que sejam 'os mais fáceis de atacar': não se sabe se há recuperação ativa
(ambiguidade 6, nunca perguntada), nem se a causa é fricção de cobrança ou inviabilidade de meio
de pagamento. O 12% de não publicação NÃO entra como vazamento independente: pela leitura mais
provável das falas é fatia de quem sai, portanto perfil de quem churna, e empilhá-lo conta os
mesmos clientes duas vezes. Ordenar por dinheiro exige volume; corrigir a medição não entrega
volume. Este campo fica sem vencedor até o bloco A2 chegar. Corrigir a frase-fonte em
03-estrategia/meta-do-projeto.md §4.1 e §9 item 3 antes de qualquer material do Comitê 1.

═══════════════════════════════════════════
ONDE O DINHEIRO FICA PARADO
═══════════════════════════════════════════

PELA MEDIDA QUE O POP PEDE, A PERGUNTA NÃO TEM RESPOSTA HOJE: nenhuma das dez etapas tem tempo
médio de passagem, `tempo_medio_dias` sai null nas dez. A tabela do roteiro da sessão de 28/08
('Volume/mês · Taxa de entrada · Tempo médio · Fonte · [E]?') saiu VAZIA da sala, e não existe
versão preenchida em 02-diagnostico/ nem em dados/outputs/ (dados/outputs/ contém apenas meta-do-
projeto.json; dados/cache/ está vazia). Qualquer afirmação de 'mais tempo aqui' seria invenção. O
que o material sustenta, estruturalmente e sem número de tempo, é isto.

(1) O dinheiro fica parado, no sentido de capital que entrou e não devolveu valor, DENTRO DA BASE
PRÉ-PAGA DE IMÓVEIS. O cliente paga adiantado, em planos de 3, 6 ou 12 meses com desconto
progressivo [D]; o produto entrega zero lead em 89% dos anúncios de Imóveis [D]; e a perda só
aparece na renovação, um ciclo inteiro depois. O TAMANHO DESSE CAPITAL É DESCONHECIDO: não há
ticket médio em documento nenhum do repositório (dados/client.json: briefing.ticket_medio = null;
bloco A3 do checklist, ⚪). O único valor citado na sessão, 'para imóveis, a gente tá falando de um
pagamento de mais de R$ 50.000' (Leonardo Costa, 01:03:19), é exemplo de restrição de limite de
cartão dentro do plano periódico, não é ticket típico, não tem frequência nem participação na
base, e NÃO deve ser usado como régua. Pior, pela definição fechada em ata: esse cliente NÃO é
churn enquanto estiver pagando, é 'inativo gerando receita'. A insatisfação fica invisível pelo
tempo inteiro do plano e a métrica só a enxerga no fim.

(2) A base tem inércia [E]. Com churn de 9% a constante de tempo é 1/c ≈ 11 meses e a meia-vida do
ajuste é 7,7 meses, uma melhoria feita hoje só entrega metade do seu valor de regime daqui a
cerca de oito meses. ATENÇÃO: o 9% é ponto médio ESCOLHIDO pela V4 dentro da faixa declarada
8–10%, não taxa do cliente; com 8% a constante vira 12,5 meses, com 10% vira 10 meses. E toda essa
leitura pende da ambiguidade 4 (churn de logo ou de receita).

(3) No sentido literal de caixa retido, o dinheiro fica parado entre CONTRATAÇÃO e PAGAMENTO: 20%
do que foi contratado E gerou cobrança nunca chega [D], e não há processo de recuperação conhecido,
a pergunta nunca foi feita.

(4) E há uma quarta parada que ninguém mede: contratos que fecharam e NUNCA GERARAM COBRANÇA. A
correção de denominador de Carolina Dallolio (00:15:30) os coloca fora dos 80%, e eles não
aparecem em métrica alguma, sem DRI e sem prazo.

(5) Uma quinta, em Autos e só lá: o abono e a contestação do pós-pago incidem DEPOIS de a receita
ter entrado no resultado. Sem magnitude (ambiguidade 7), e sem resposta sobre quando exatamente a
receita é reconhecida (nó 3B-11, aberto).

═══════════════════════════════════════════
DEPENDÊNCIAS ESTRUTURAIS DO FLUXO (14)
═══════════════════════════════════════════

1. AQUISIÇÃO ANCORADA EM ESFORÇO HUMANO: 50% [D] nasce de prospecção comercial ativa, denominador
em disputa entre receita (slide) e base (Carolina Dallolio, 00:05:42), e é participação de origem,
não medida de capacidade. SE essa via está saturada é DESCONHECIDO: não há headcount, ocupação de
agenda, produtividade por vendedor nem fila de demanda não atendida em documento nenhum (bloco
A2/04-3 do checklist). A dependência é estrutural; o limite é hipótese. Formulada como política a
testar: a empresa opera sob a política implícita de crescer o topo por esforço humano em vez de
por canal instrumentado, não verificada. A prospecção ativa NÃO aparece no diagrama de canais
(L1, o desenho do caminho continua faltando).

2. MUDANÇA DE PLANO SÓ POR ATENDIMENTO HUMANO: up, down e cancelamento passam obrigatoriamente
pelo time comercial (Carolina Dallolio, 00:12:41) e não existe upgrade self-service (Leonardo
Costa, 00:39:34, L22). É política, não recurso. O tamanho do efeito é desconhecido: a etapa 10 não
tem volume, taxa nem participação de receita declarados.

3. BOT DE QUALIFICAÇÃO (MQL→SQL), automatizado há cerca de quatro meses, reaproveitando histórico
de inativo. Cliente já ativo na base pula etapas, a rota depende de por onde ele entrou, o que
torna o denominador do funil dependente do canal. As definições de MQL e SQL são declaração verbal
(00:44:38), sem política escrita no repositório.

4. TRANSBORDO DE CARRINHO ABANDONADO → time de atendimento humano. O slide de FLUXOS registra três
fluxos entrando no Formulário (24% + 3% + 17%) [D], e continua ABERTO se o transbordo é
subconjunto dos 41% de LPs ou entrada adicional (L30), se for subconjunto, dizer que 'vale 17% da
entrada' é dupla contagem. Nada disso é conferível enquanto o slide não for versionado (L28).
Some-se o conflito não resolvido sobre existir em Autos: Michelle Morais diz que só em Imóveis,
Carolina Dallolio responde 'não é só imóveis', Michelle conclui o contrário e a conversa termina
sem fechar (L16, 00:43:40).

5. SISTEMAS SEPARADOS POR VERTICAL: POS com vitrine em Zap e VivaReal; Canal Pro (Imóveis) com
cadastro e senha próprios, acessível só após pagar; MyPlan dentro do login OLX (Autos). Duas
jornadas de plataforma, um único mapa, e o passo 1 do POP manda montar um fluxo por unidade antes
de consolidar.

6. SEQUÊNCIA PAGAMENTO → LOGIN, invertida recentemente: o cliente agora só faz login depois de
pagar (Leonardo Costa, bloco 00:26:33). Dependência estrutural nova entre as etapas 5 e 6 e ponto
de quebra em qualquer série histórica do 80% e do 12%.

7. INTEGRADOR DE TERCEIROS na publicação e na marcação de vendido: 'quem usa integrador raramente
manda marcação de vendido pra gente'. A OLX não controla nem a entrada do anúncio nem o registro
do desfecho (L26).

8. MEIO DE PAGAMENTO E TIME DE SOLUÇÕES FINANCEIRAS: metade da base em boleto [D], ~40% cartão
[D], resto Pix [D], sem diferenciação de preço (Carolina Dallolio, 00:21:16). O esquecimento
responde por 20% dos ATRASOS e explicitamente NÃO pelo churn [D] (00:22:16), o percentual é do
comportamento, não do canal de cobrança. A associação entre boleto e maior incidência de atraso é
declarada por Iuna Scheffler sem magnitude (01:01:58). Há pagamento de Imóveis acima de R$ 50 mil
que não cabe no cartão [D] (Leonardo Costa, 01:03:19), exemplo de restrição de limite, não
ticket. A venda de maior valor depende de roadmap de outro time, com mudança estrutural declarada
só para 2027.

9. DASHBOARDS (funil B2B e canal online), dono operacional Lu Machim, processados às 3h, histórico
de 12 meses, com filtro por vertical, canal, time e período. TODA a apuração dos seis percentuais
depende deles, e os LINKS AINDA NÃO CHEGARAM (lacuna 1 da ata, DRI Leonardo Rosa, prazo '-').

10. INVESTIMENTO DE MÍDIA FORA DO DASHBOARD, em controle à parte com Mirella Mendonça (00:10:08).
Sem ele não existe CAC por canal, e, com o problema de atribuição do Direto, nem com ele o CAC
fecha. ATUALIZADO EM 14/09: o investimento medido no V4MOS deixou de ser um agregado sem quebra e
passou a ser **R$ 10,12 mi com quebra mensal e por campanha** (Meta R$ 7,38 mi, Google R$ 2,75 mi,
01/01/2025 a 14/09/2026). O que continua faltando é o mesmo de antes, e agora é a única coisa que
falta: **saber qual campanha é captação de anunciante e qual é consumidor**. Nenhuma das duas
contas separa B2B de B2C (pendência 12), e essa separação não está nos dados, está na cabeça de
quem montou as campanhas. É uma frase do time de mídia que transforma R$ 10,12 mi no numerador de
um CAC.

11. DUAS CAMADAS DE ATRIBUIÇÃO CONVIVENDO: o GA4 e, em paralelo, cookies `sf_utm_*` gravados em
.olx.com.br pela tag 162 do Container Master, modelo last-click não-direto, janela de 90 dias,
alimentando o Salesforce, com comentário no próprio código: 'Atribuição client-side. Não
substitui dados do GA4'. Dois modelos e duas janelas diferentes para a mesma pergunta (auditoria
vii, achado 15).

12. MEDIÇÃO DISPERSA POR SUPERFÍCIE: a superfície B2B escreve em pelo menos três propriedades GA4
(G-50C013M2CC → OLX App + Web 152644854; G-6TV9FSHYVM; G-ZBYP2KJ7L9), o GTM do grupo tem QUATRO
contas com duas inteiramente por auditar, cinco exports já no repositório ainda não lidos, e a V4
está em nível LEITOR no GA4, que não abre fluxos de dados, definições personalizadas, retenção
nem a lista de eventos-chave. O mapa propriedade × measurement ID × superfície é ação da pendência
16 e não foi entregue.

13. ENTREGA DE ACESSOS DA OLX: a entrega marcada para 17h de 03/09 não ocorreu e foi
recomprometida para terça, 08/09 [D]. É a única premissa declarada que sustenta o cronograma
remontado, e já falhou uma vez.

14. BLOCO A DO CHECKLIST (A1–A3) SEM NENHUM ITEM RECEBIDO, conferido em 02-diagnostico/checklist-
dados-e-acessos.md linhas 22–24, os três em ⚪: receita por linha de negócio, funil com volumes e
taxas, ticket médio, ciclo e CAC. Não é acesso, é entrega de dado, nenhuma concessão de
ferramenta o destrava, e a auditoria (vii), mesmo corrigida, reabilita a medição, não entrega os
volumes.

═══════════════════════════════════════════
VIOLAÇÕES REJEITADAS NA REVISÃO ADVERSARIAL (3)
═══════════════════════════════════════════

1. CAMPO: etapas[ordem=6], 'há fala contrária em 00:23:16', usada para hedgear o denominador do
12%. POR QUÊ: a fala existe, mas não é contrária. Conferido nas linhas 566 a 597 da transcrição:
em 00:23:16 quem abre o assunto é Gustavo Figueiredo perguntando 'vocês têm a metrificação do que
que é um turn M0, ou seja, uma não ativação'. Carolina Dallolio responde que a maior parte do
churn acontece no primeiro mês, que esse cliente já pagou porque a maioria é pré-pago, e enumera
os perfis: 'ou bem ele tá nesses 12% aqui que sequer publicou... ou ele pode ser publicado e não
recebido leads... ou ele tem outro motivo para ir embora'. É uma enumeração de PERFIS DE QUEM
CHURNA NO PRIMEIRO MÊS, o que é coerente com a leitura de 'quem sai' e não a contradiz, o que a
fala acrescenta é que esse cliente pagou, não que o 12% seja medido sobre a coorte que pagou.
Rejeitada a caracterização de 'fala contrária'. ACEITO e aplicado, porém, tudo o mais da crítica:
a transcrição é automática, a leitura depende de segmentação, a redação precisa ser confirmada com
a OLX, e nenhuma consequência aritmética pode ser aplicada a meta-do-projeto.md §4 antes disso.

2. CAMPO: etapas[ordem=10].fonte, '00:38:26 é precisamente o timestamp do BULLET DE RESUMO
AUTOMÁTICO sobre uso de app (linha 109)'. POR QUÊ: meia verdade que, se aplicada inteira,
introduziria um erro novo. Conferido com awk sobre os cabeçalhos `### **hh:mm:ss**` da
transcrição: a linha 861 é um bloco de fala REAL sob 00:38:26, e é exatamente ali (linha 885) que
Leonardo Costa diz 'na casa dos 70, 60% que usa OLX autos aplicativo... é 20% só usa o app, eh,
30%'. Portanto citar 00:38:26 para o share de app está CERTO, e a ata de 28/08 o cita
corretamente. O que está errado, e foi corrigido, é citar 00:38:26 para a frase do touch point,
que está em 00:40:31 (linha 949). A existência de um bullet de resumo com o mesmo timestamp não
invalida o timestamp da fala.

3. CAMPO: etapas[ordem=5].taxa, 'o campo de taxa reverte ao denominador largo... que é o do
slide, não o da transcrição'. POR QUÊ: a atribuição de procedência está errada, e ela importa
porque o material vai ao cliente. A formulação larga '20% escorregam entre a contratação e o
primeiro pagamento' é literalmente de Carolina Dallolio, na transcrição, linha 445, bloco
00:14:12: 'a gente tem 80% paga. Então, escorrega aí 20% dos clientes entre a contratação e o
primeiro pagamento'. Não é leitura do slide feita pela V4, o que aconteceu na sessão foi a
própria falante estreitar o denominador cerca de um minuto depois, em 00:15:30: 'dos 100% que
fizeram a contratação e geraram um boleto ou qualquer coisa do tipo, desses 100%, 80 pagam'. A
SUBSTÂNCIA da crítica foi aceita e aplicada (vale o denominador estreito, e os contratos sem
cobrança gerada são vazamento adicional não medido); rejeitada apenas a atribuição, que
apresentaria à OLX como erro de leitura da V4 algo que é autocorreção da própria oradora.

═══════════════════════════════════════════
NOTA DE PROVENIÊNCIA DESTA REEMISSÃO
═══════════════════════════════════════════

Esta versão NÃO refaz a análise. É a reemissão, no schema canônico da skill dre-fluxo-receita, do
conteúdo já corrigido contra 55 violações da revisão adversarial. O trabalho aplicado aqui foi de
conformidade de formato mais os dois campos que faltavam, correspondentes às duas violações
bloqueantes remanescentes (índices 27 e 28 de criticas-fluxo.json): (27) a eleição de um maior
vazamento por elasticidade percentual foi substituída por `ranking_perda[]` com perda_absoluta
null nas dez etapas e um campo `impossivel_ordenar` por item; (28) `etapas[]` passou a carregar os
campos canônicos `tempo_medio_dias`, `perda_absoluta`, `taxa_entrada`, `estimado` (booleano) e
`travas_associadas[]`, sem perda dos campos `ordem`, `o_que_acontece`, `natureza` e `taxa_saida`
da versão anterior. O texto do campo `perda` de cada etapa, que o schema não comporta como campo
próprio, foi preservado integralmente dentro de `o_que_acontece` sob o rótulo 'PERDA
(perda_absoluta = null)'. Nenhuma fonte, marcação [D]/[E] ou 'ausente' foi removida. O registro de
correções aplicadas (31 itens) permanece no arquivo de trabalho fluxo-corrigido.json, fora do
schema de entrega.

---

## Ponto de alavanca

O ponto de conversa com a OLX não é qual vazamento atacar, é que o mapa não permite escolher, e
que a escolha custa uma extração, não um projeto.

CONTEXTO. O fluxo do anunciante profissional está narrado ponta a ponta, com origem nomeada em
cada etapa, e mesmo assim nenhuma das dez etapas tem volume absoluto e nenhuma tem tempo médio. O
POP manda ordenar por perda ABSOLUTA ("uma taxa ruim em cima de volume pequeno perde para uma taxa
mediana em cima de volume grande"), e sem volume perda_absoluta é null nas dez. Entre churn
(8–10%/mês [D]) e pagamento da 1ª fatura (80% [D]) há EMPATE TÉCNICO pela elasticidade de regime,
a 8% de churn, −1 p.p. vale +14,3%; a 9%, +12,5%; a 10%, +11,1%; levar o pagamento de 80% para 90%
vale +12,5%, e todos esses números são [E], derivação da V4 sobre taxas declaradas. Eleger um
vencedor hoje é quebrar o próprio POP.

RAZÃO 1 · O desbloqueio já está na tela do cliente, não em coleta nova. O dashboard de funil B2B
tem taxa de qualificação (MQL→SQL) e conversão em vendas (SQL→venda) por vertical, canal, time e
período, com histórico de 12 meses, e o dashboard de canal online tem sessões → vitrines →
checkouts → vendas. A V4 viu os dois em 00:07:00–00:08:59 e não extraiu um dado. Faltam os LINKS:
lacuna 1 da ata, DRI Leonardo Rosa, prazo '-'. Primeira extração: recuperar as "414 vendas" com
período, vertical e denominador.

RAZÃO 2 · A pergunta mais barata do projeto cabe num e-mail. `generate_lead_pro` registrou 661.144
eventos em agosto/2026 na GA4 VivaReal (407391347) e PENDENCIAS.md:346 já escreveu que, se for o
lead de anunciante, "é o numerador que falta para o fluxo de receita". Junto vai a segunda: qual
das duas propriedades é a de referência para `generate_lead` (830.116), porque o gatilho [208]
lead_dbm dispara as tags 209 e 356 e qualquer consolidação conta cada lead duas vezes. Ações 1 e 2
da pendência 13, sem resposta registrada.

RAZÃO 3 · Três respostas de uma frase cada valem mais que qualquer análise adicional: (a) o churn
de 8–10% é de logo ou de receita (ambiguidade 4), dela pendem os 63–72%/ano, a constante de tempo
de 11 meses e toda a tabela de elasticidades; (b) o denominador do 12% de não publicação é a
coorte que pagou ou quem sai (se for quem sai, p(publicação)=88% deixa de ser termo independente e
os tetos de +26% e +44% de meta-do-projeto.md §4 caem); (c) qual a magnitude da "alta taxa de
abono e contestação" do pós-pago de Autos (ambiguidade 7), é o único vazamento que incide DEPOIS
do reconhecimento de receita e, por isso, não pode ser excluído do topo do ranking.

ÂNCORA DA DISCUSSÃO. A conversa a ter no Comitê 1 é sobre a entrega do bloco A do checklist
(A1–A3, três itens em ⚪) e sobre os links dos dashboards, não sobre qual trava atacar. Enquanto
isso não chega, dados/client.json deve continuar com score null nas oito travas e
restricao_identificada null, e a cadeia entrega-zero → churn segue como HIPÓTESE NOMEADA, sem
ordinal e sem veredito.
