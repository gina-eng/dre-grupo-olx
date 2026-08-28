# O que a transcrição do kick-off fecha, move e deixa aberto

> **Insumo:** [transcrição integral de 24/08/2026](2026-08-24-kickoff-transcricao.md) (02:11:54) e as
> anotações do Gemini no mesmo arquivo.
> **Alvos:** as 88 perguntas do formulário de kick-off (`portal/assets/form-data.js`) e a árvore de
> produção de receita (`portal/_src/receita.html`, SEED).
> **Status:** conferência concluída e **aplicada ao portal** em 26/08 (formulário e árvore). O que
> falta aplicar está no §7.

Regra usada em toda a leitura: a sala presencial de São Paulo tem rótulo único
("Olhamos para o futuro 01 - SP"), então fala sem nome identificável fica marcada como
**[sala SP]** e não é atribuída a pessoa. Número dito em transcrição automática não vira dado
(regra 1 do repositório), vira linha do §8.

---

## 1. Placar

| Material | Antes | Depois desta conferência |
|---|---|---|
| Formulário, **96 perguntas** | 0 respondidas | **39 respondidas** · **34 parciais** · 23 em aberto |
| Bloco 3B (árvore), 13 perguntas | 13 abertas | **7 respondidas** · **4 parciais** · 2 abertas |
| Árvore | 22 nós: 18 aberto · 4 hipótese | **39 nós: 21 confirmado · 16 hipótese · 2 aberto** |
| Pendências | 12 abertas | 2 fecham · 4 avançam · **2 novas** |

> O material dizia "88 perguntas em 11 blocos". São **96**: a contagem estava errada no cabeçalho e
> na ata. Corrigido junto.

O bloco 3B era o material mais caro em aberto e é o que mais rendeu. A pergunta mais cara de
todas (3B-1, "o que exatamente o cliente compra quando paga") **fechou com fala literal**.

---

## 2. As oito respostas que mudam o projeto

### 2.1 O escopo fechou: Autos e Imóveis, Goods fora (02-1, pendência #5)

> **[sala SP]:** "É autos, imóveis e goods. A gente tem linhas bem menores, mas acho que autos,
> imóveis. A goods, a gente deixa de lado."
> **Dener, 01:59:34:** "Já ficou bem mais claro para mim. Já tirou a questão ali do goods, já
> facilitou. Isso aí era um complicador grande."

E o recorte de trabalho dentro disso, dito por Florence às 00:23:11:

> "Quando a gente olha para aquisição de novos, a gente tem três pilares: os leads B2B, a
> prospecção comercial e canal online. Nessas três frentes é parque de diversão para vocês."

**Consequência:** duas unidades no escopo, com times estruturados por vertical e metas abertas por
vertical. Em TOC, cada sistema de receita tem sua restrição governante, então o Ciclo 1 ainda
precisa escolher **uma**. A percepção do cliente (§2.7) aponta para Imóveis.

### 2.2 O cliente compra posição, não lead, e não há garantia de performance (3B-1)

> **Dener:** "o cara que compra um pacote de leads aqui, ele não compra um pacote de leads, ele
> compra um inventário, um grau de posição, e ele pode receber zero ou 100 leads."
> **Leonardo Costa:** "Exato. Não tem garantia. O range é gigantesco."
> **Leonardo Costa, 01:17:16:** "mesmo no modelo que a gente trabalha hoje de marketplace, a gente
> trabalha no modelo pay per listing."
> **[sala SP], 02:07:29:** "A gente vende exatamente os mesmos produtos de 15 anos atrás."
> "O formato que a gente cobra impede que ele publique todo o inventário, porque você pode ter 100
> imóveis para anunciar, mas você tem dinheiro para anunciar 50."

**Unidade de valor:** inserção/slot de anúncio ativo, mais produtos de visibilidade (destaque,
super destaque). Leonardo Costa acrescenta o benchmark: lá fora visibilidade é 30% a 50% da receita
em real estate, aqui é muito menos, e os produtos de visibilidade já estão saturados.

**Por que importa:** a promessa vendida (posição) e a expectativa comprada (lead) não são a mesma
coisa. Isso é insumo direto da Trava de Decisão e explica o churn descrito em §2.4.

### 2.3 Triple Bundle: um contrato, três portais, origem opaca (3B-2, 3B-0)

> **[sala SP], 01:28:15:** "no caso de imóveis, a relação desse B2B é com Grupo OLX. Ele compra e
> a gente distribui nos três portais. Tem um conceito aqui que você vai escutar bastante da gente,
> é o do Triple Bundle. Na hora que ele vai receber os leads, ele recebe de todos os portais.
> Não é transparente para ele. Ele não sabe o que está vindo de qual portal."
> Em Autos: "é uma marca, é o OLX, está dentro da marca OLX e está tudo certo."

**Consequências, em cadeia:**
1. O anunciante de imóveis é **um** registro, não três. A contagem de base ativa, ticket e churn
   precisa ser lida no Grupo, não por marca.
2. A opacidade da origem quebra a experiência: a imobiliária responde um lead da OLX mandando
   link do ZAP ou do VivaReal (Leonardo Costa, 01:33:44).
3. O ponto de partida da árvore muda: o nó pagante é do Grupo, e as marcas são canais de entrega.

### 2.4 A retenção já é lida em quatro modos, e o resumo do Gemini tinha subestimado isso (3B-10)

Correção importante ao [registro provisório feito sobre o resumo](#6-correções-ao-registro-provisório):
a hipótese de que a OLX só enxerga cancelamento formal **está errada**. A transcrição mostra os
quatro modos de morte de conta no vocabulário deles:

| Modo | Fala |
|---|---|
| Não renovação silenciosa (pré-pago) | "a grande maioria contrata planos de maneira pré-paga. Nesse caso o churn não é um churn, ele só para de pagar, não renova" |
| Downgrade | "as nossas entradas não estão compensando o churn mais downgrade" (Iuna) |
| Inadimplência (pós-pago) | "do lado pós-pago fica concentrado nesses times de campo, e eles são apoiados por um time de cobrança, que vai atrás de uma receita devida" |
| Saída tática para voltar melhor | "muitos saíam para voltar numa condição melhor. E a gente foi endurecendo essas políticas" |

**O achado real está no que não existe.** Perguntados se o time de cobrança olha a performance do
cliente, a resposta foi:

> **[sala SP], 01:23:23:** "ele é um time de cobrança mais focado em contas a receber. Esse caso que
> eu acabei de explicar, ele não existe hoje do ponto de vista de CS, de retenção."

Quem faz papel consultivo (reportar performance, visitar, treinar, sugerir visibilidade) é o
executivo comercial, e só nas contas maiores. **Não existe CS de retenção que olhe se o cliente
está tendo resultado.** Num negócio cuja restrição percebida é retenção, isso é candidato a
causa-raiz estrutural.

### 2.5 A remuneração do comercial não remunera retenção (04-4, 3B-11)

> **Iuna, 01:26:30:** "dentro do que é remuneração variável, a gente opera com modelo de 75% sendo
> a carteira deles e 25% um scorecard, onde a gente coloca algum indicador que a gente entende ser
> estratégico. A gente discutiu colocar alguns indicadores de qualidade da base, ou qualidade de
> atendimento do próprio executivo, ou CSAT, mas não estamos lá ainda."

**Formulável como política implícita para a CRT:** *"o comercial é remunerado por faturar a
carteira, não por manter o cliente performando."* Combina com §2.4 (não há CS de retenção) e com
§2.6 (o preço subiu enquanto a performance caía). Os três apontam para o mesmo lugar.

### 2.6 O aumento de preço de 2026 é a mudança estrutural que explica a série (03-11, 3B-9, 07-2)

> **[sala SP], 01:20:27 a 01:21:24:** "esse ano foi um ano onde a gente aumentou muito o preço. A
> gente trabalhou com uma consultoria [de pricing], a gente fez benchmark, olhou para fora, olhou
> para dentro. Aí a gente viu que tinha um bom caminho para recuperar a rentabilidade. Nessa
> recuperação de rentabilidade, o que aconteceu? E talvez aí tenha sido o nosso movimento não muito
> inteligente. A gente foi mexendo no preço dele e ele foi tendo a perda de performance pelo cenário
> mais competitivo. Então ele foi vendo que vocês estão aumentando o meu preço e a performance minha
> está caindo."

E a escada de planos facilita a fuga para baixo: "a gente tem múltiplos pacotes, de 10, de 12, 14,
ele tem opção."

**Isto é tentativa que falhou, declarada pelo próprio cliente**, ou seja, insumo direto da Nuvem de
Conflito, não apenas contexto. Na transcrição a consultoria aparece como "consultoria de privacy",
quase certamente corrupção de *pricing* pelo contexto. Confirmar o nome antes de citar em comitê.

### 2.7 A hipótese do cliente sobre a restrição, com nome e voto (07-1)

Pergunta feita explicitamente pela V4 às 01:52:05. Respostas:

| Quem | Aponta |
|---|---|
| Matheus Rodrigues (FP&A) | "de fora, eu diria que qualificação é a nossa maior dor" |
| Carolina Dallolio (ops comerciais) | retenção (referida por Iuna: "eu compartilho da opinião da Carol") |
| Iuna Scheffler (planejamento) | "eu acho que o nosso grande desafio é retenção" |
| [sala SP] | "tem essa visão de qualificação, sem dúvida. E, dado a nossa relevância, a retenção" |

**Placar: Retenção 3, Qualificação 2.** Vai para `client.json` como `hipotese_cliente`, sempre
rotulada como percepção, nunca como diagnóstico. É exatamente a divergência que o produto existe
para testar contra o dado.

### 2.8 A meta do projeto não é receita (03-10, 07-5, pendência #2)

> **[sala SP]:** "se fosse falar uma única meta, a meta é receita, é margem, é NRR? Qual é a North
> Star?"
> **Iuna:** "hoje é receita. Margem EBITDA é uma das nossas North Star Metrics, compõe PLR, mas o
> que está no nosso dia a dia, o que os times perseguem, é receita."
> **[sala SP]:** "Mas se a gente tivesse que sacrificar EBITDA em prol da receita, a gente poderia?"
> **Matheus:** "Não."
> **Matheus, 01:58:27:** "eu sou mais disposto a sacrificar a receita e melhorar a margem do que o
> contrário. O contrário é impossível."

E a razão econômica, dita por eles: "como a gente não tem um produto que a gente fabrica, a gente
praticamente tem uma margem de 100% em cima do que a gente vende", com mídia e imposto como
ofensores.

**Consequência para o Success Fee (pendência #2):** o KPI do bônus deve ser ancorado em margem, NRR
ou ROIC, não em faturamento bruto, e o próprio cliente já validou esse racional em reunião. Isso é
munição direta para o aditivo, e alinha com o que o método já defende em
[08-economics](../00-playbook/08-economics-e-entregaveis-dr-e.md).

---

## 3. Formulário: o que responder, bloco a bloco

Só entram aqui as perguntas que **mudaram de estado**. As demais seguem abertas e estão no §5.

### Bloco 01 · Governança e decisão

| # | Pergunta | Novo estado | O que gravar |
|---|---|---|---|
| 01-1 | Decisor final | **parcial, mas resolve a dúvida** | Existe instância acima de Mirella: **Florence Scappini** lidera a frente de receita, abriu e fechou a sessão e é referida por Matheus como sua líder. Cargo formal a confirmar |
| 01-3 | Ponto focal operacional | **respondida** | **Carolina Dallolio (Carol)**, operações comerciais, sob Iuna. "a pessoa mais próxima dele que vai estar com a gente no projeto, por exemplo, Carol" |
| 01-4 | DRI por frente | **parcial** | Produto e canais online e WhatsApp/IA: Leonardo Costa · Planejamento, ops comerciais, pricing e performance comercial: Iuna Scheffler (diretora) · Ops comerciais: Carolina Dallolio · FP&A: Matheus Rodrigues · Serviços financeiros (faturamento, contas a receber, compras, tesouraria): Flavia Cardoso (diretora) · CRM: Michelle Morais · Frente de receita: Florence Scappini. **Faltam:** mídia paga, tracking, CRO/SEO, pré-vendas, dados/BI |
| 01-5 | Quem participa dos comitês | **parcial** | Florence, 00:07:31: "esse vai ser o grupo que vai sempre estar acompanhando esse projeto". Ou seja, os nove da lista de convidados. Poder de veto não declarado |
| 01-6 | C-Level nos presenciais | **parcial** | Aparece **"Gui", CFO do Grupo OLX**, com quem Dener já discutiu o modelo de cobrança por lead. Nome completo a confirmar. Não estava na sala |
| 01-7 | Ciclo de aprovação interna | **parcial** | Acesso de terceiro à OLX passa por chamado, **um por pessoa**. O primeiro (Rafael) saiu; os demais foram abertos em 24/08; expectativa de conclusão até quarta 26/08 |
| 01-9 | Outras consultorias/agências | **parcial e relevante** | **Consultoria de pricing** atuou em 2026 e embasou o aumento de preço. **Meta** é parceira: incentivo comercial e IA de recomendação em construção conjunta |

### Bloco 02 · Recorte do negócio e escopo

| # | Novo estado | O que gravar |
|---|---|---|
| 02-1 | **respondida** | Autos e Imóveis dentro. **Goods fora.** Três pilares de trabalho: leads B2B, prospecção comercial, canal online |
| 02-2 | **respondida** | B2B = anunciante profissional. O consumidor final vê as marcas dos portais; o anunciante contrata o Grupo. Leonardo Costa: "toda a esteira B2B online passa por mim" |
| 02-3 | **parcial forte** | Não há P&L por marca em Imóveis: a relação é com o Grupo. A leitura de gestão é **por vertical**, com metas abertas por vertical, linha, canal e região. P&L por vertical foi pedido como documento (Dener, 02:02:10) |
| 02-4 | **respondida** | Imobiliária, corretor autônomo, incorporadora, dealer/revenda, concessionária, **locadora** (já em pay per lead), grandes contas. Banco/financeira entra como **parceiro na jornada**, não como anunciante padrão |
| 02-6 | **respondida qualitativamente** | Três motions: canal online (self-service, porta de entrada de clientes menores), inside sales (telefone e WhatsApp), field sales (clientes maiores). Split de receita não informado, **mas existe no planejamento**: as metas já são abertas por canal de venda |
| 02-7 | **respondida qualitativamente** | Sim. Curitiba citada por Iuna como praça sem prática de exclusividade, onde a razão anúncio/propriedade é muito diferente. Metas abertas regionalmente |
| 02-8 | **respondida** | Fora: Goods. E fora do produto: execução. Dener: "esse é o produto 100% sendo de saber. A gente não tem nada de executar, não tem literalmente nada aqui" |

### Bloco 03 · Modelo de receita e números-âncora

| # | Novo estado | O que gravar |
|---|---|---|
| 03-1 | **respondida** | Pay per listing (slot/inserção) + produtos de visibilidade + pay per lead em nichos (autos: grandes contas e locadoras; imóveis: teste com incorporadoras). Pré-pago majoritário em imóveis, pós-pago em contas de campo |
| 03-2 | **comprometida, não entregue** | Matheus: "vou triangular com a Iuna e a gente prepara um material para vocês". Escopo pedido: metas por etapa do fluxo, receita por vertical, visão global, overview 2026 |
| 03-6 | **parcial, direcional** | Em Imóveis o **net está negativo**, e é net **de receita**: "as nossas entradas não estão compensando o churn mais downgrade" (Iuna). Florence: "eu estou perdendo mais clientes do que estou ganhando". Números faltam |
| 03-7 | **respondida** | Não existe CAC aberto por iniciativa ou frente. Florence: "os custos de aquisição por iniciativa e por frentes, eu vou ter que começar a abrir. Não pode ser um custo, uma média". Evidência formal de Cegueira |
| 03-8 | **respondida** | LTV e payback por anunciante **não existem**. Iuna: "com olhar sobre a perspectiva de qual é o LTV desse cliente, qual foi o CAC, a gente ainda não chegou lá". Margem bruta ~100% (sem COGS de produto), ofensores: mídia e imposto |
| 03-10 | **parcial** | Metas 2026 abertas por vertical, linha (novos, churn, downgrade, upgrade), canal e região. 2027 em long-term plan, menos detalhado. North Star declarada: receita. North Star real: margem (ver §2.8). Número e prazo do projeto ainda ausentes |
| 03-11 | **respondida** | Aumento expressivo de preço em 2026 (ver §2.6) + endurecimento da política de recontratação |

### Bloco 3B · Árvore de produção de receita

| # | Pergunta | Novo estado |
|---|---|---|
| 3B-0 | Quem assina e quem paga | **respondida na contraparte** (Grupo OLX em imóveis, marca OLX em autos), aberta na unidade de cobrança |
| 3B-1 | O que o cliente compra | **respondida** (ver §2.2) |
| 3B-2 | Separado, combo ou os três | **respondida**: combo, Triple Bundle, origem opaca (ver §2.3) |
| 3B-3 | Autos: plano, anúncio ou comissão | **respondida**: mesmo modelo de classificados, PPL em grandes contas e locadoras. Nenhuma menção a comissão sobre venda de veículo |
| 3B-4 | O que faz a fatura crescer | **respondida**: upgrade na escada de pacotes (10, 12, 14, 15), produtos de visibilidade, rentabilização de carteira pelo executivo via "Spark". Ressalva declarada: os produtos de visibilidade já estão saturados |
| 3B-5 | Onde está a margem | **parcial**: margem ~100% em tudo, sem abertura por linha. A pergunta certa vira composição de receita por produto |
| 3B-6 | Audiência B2C no preço do anunciante | **respondida, e é achado** (ver §4) |
| 3B-7 | Canal indireto | **parcial negativa**: nenhuma revenda, franquia ou agência vendendo em nome do grupo. Existe parceiro financeiro na jornada |
| 3B-8 | Novo x expansão | **parcial**: em Imóveis o net é negativo. Autos não declarado |
| 3B-9 | Tabela e desconto | **parcial forte** (ver §2.6). Falta a tabela vigente e o desconto médio por segmento |
| 3B-10 | Cliente ativo e como a conta morre | **respondida** (ver §2.4) |
| 3B-11 | Quem toca o quê até o dinheiro | **parcial forte** (ver §2.5). Faltam: quem precifica, quem aprova exceção de desconto, quem fatura |
| 3B-12 | Linha de receita fora da árvore | **respondida**: seis candidatos (ver §4) |

### Blocos 04 a 09, o que moveu

| # | Novo estado | O que gravar |
|---|---|---|
| 04-3 | parcial | Canal online, inside sales, field sales, gestão de pagamento, cobrança, executivo comercial. Divisão hunter/farmer explícita: "quem faz essa primeira entrada não é necessariamente quem rentabiliza". Headcount não informado |
| 04-4 | **respondida** | 75% carteira + 25% scorecard (ver §2.5) |
| 04-7 | respondida do outro lado do marketplace | Taxa de resposta da imobiliária ao lead: **50% a 58%**, medida por cliente oculto e benchmark. Não é SLA da OLX ao lead B2B, que segue aberto |
| 04-8 | parcial | Causas de churn declaradas: preço, queda de performance percebida, ausência de garantia de resultado na primeira entrega, downgrade facilitado, saída tática. A pergunta "vocês aferem o motivo de saída?" foi feita e **a resposta não aparece na transcrição** |
| 04-12 | aceite genérico | "a gente vai com certeza acionar vocês e, se tiver a possibilidade de fazer, conforme sua visão, perfeito". Falta o aceite específico de gravação de call e o parecer de LGPD |
| 04-13 | **respondida** | Pré-pago renova por novo pagamento; se não paga, não renova. IA + régua de touch. Gestão de pagamento cobra a carteira de maior receita. Pós-pago: field sales + cobrança |
| 05-10 | **respondida** | Concorrentes: Webmotors (autos), Chaves na Mão (imóveis), e **Meta e Google diretamente**. Mercado descrito como "rouba-monte". Clientes pequenos migram verba para Meta/Google e isso é ponto cego de rastreamento |
| 05-11 | parcial | O que se comunica é visibilidade e inserção, sem garantia de performance. [sala SP]: "a gente deveria blindar essa aquisição e a gente não garante" |
| 06-1 | **respondida, e reenquadra a Cegueira** | O dado existe; a leitura não. Florence: "os dados não estavam e eu acho que ainda não estão em perfeita harmonia. A Carolina via na perspectiva dela, a Mirella na perspectiva dela, o time comercial via a venda final". E: "a gente acha que não tem o dado tratado. Não deve ter análise mesmo" |
| 06-5 | **respondida** | Chamado por pessoa, Rafael concluído, demais abertos em 24/08, expectativa até 26/08 |
| 06-6 | **respondida por acordo** | Acessos até quarta 26/08, contagem de 15 dias a partir de 25/08, diagnóstico em ~09/09, comitê em **10/09** |
| 06-8 | **respondida** | Três métricas sob suspeita declarada: (a) investimento de mídia dos clientes pequenos direto em Meta/Google, não rastreável; (b) deduplicação de anúncios, "briga de gato e rato" com as imobiliárias fugindo do algoritmo; (c) a atribuição de receita ao lead B2C foi feita por rateio de planos vendidos, não por atribuição real |
| 07-1 | **respondida** | Retenção 3, Qualificação 2 (ver §2.7) |
| 07-2 | **parcial forte** | Aumento de preço, endurecimento de política de recontratação, testes de PPL, campanhas de reativação, deduplicação algorítmica. Os "band-aids" seguem sem inventário nome a nome |
| 07-3 | **respondida** | Não se mexe: migração da base de imóveis para PPL ("não tem apetite... não é o momento de causar esse tipo de fricção com o mercado", Iuna) e o EBITDA ("o contrário é impossível", Matheus) |
| 07-4 | **respondida, e melhor do que se esperava** | Ver §4.2 |
| 07-5 | **critério respondido, número não** | Margem, NRR e defesa da base, não receita bruta. Dener sugeriu ROIC como ponto médio e prometeu voltar em 15 dias com sugestão de meta de projeto |
| 07-7 | **parcial** | Florence: curto prazo primeiro, "porque a gente mexendo os ponteiros rapidamente isso cria um fator motivacional grande e a gente consegue maior adesão das áreas de tecnologia". O critério de 90 dias é político tanto quanto numérico |
| 08-1 | **parcial** | Comitê de identificação da restrição **pré-setado para 10/09** (dia 9 não funciona para Iuna). Local em aberto: escritório V4 ou escritório do Rio (oferecido por Leonardo Costa) |
| 08-2 | **parcial** | Desenho apresentado: mini comitê semanal com menos gente, comitê mensal, comitê de receita trimestral presencial ocupando um turno inteiro. Ainda não conciliado com os 12 encontros do contrato |
| 08-3 | **princípio acordado** | Tudo enviado antes, por escrito, sem apresentação formal; reunião só para discutir. Ferramenta não definida |
| 09-2 | **avançou** | Dener declarou em reunião que o KPI do bônus será definido até o comitê, e §2.8 dá o eixo (margem/NRR/ROIC). Flavia (financeiro) pediu explicitamente para "calibrar isso no modelo de success fee para garantir o ganha-ganha" |
| 09-4 | **resolvido na prática** | Dener apresentou "as sete travas" mais uma "etapa zero" de visibilidade, o que concilia com a redação do contrato. E Matheus reagiu à etapa zero com "cuidado a dizer que não é um problema nosso", ou seja, o próprio cliente sinaliza Cegueira |

---

## 4. Árvore da receita: diffs por nó

Legenda: `A` aberto · `H` hipótese · `C` confirmado.

### 4.1 Nós existentes

| Nó | De | Para | Nota a gravar |
|---|---|---|---|
| **Receita B2B do Grupo OLX** (raiz) | A | **H** | Modelo de classificados: pay per listing mais produtos de visibilidade, inalterado há 15 anos por declaração própria. Duas verticais no escopo (Autos e Imóveis), Goods fora |
| Origem do valor: audiência B2C | H | **C** | Não é gerida. Perguntados sobre rentabilizar o lead B2C: "a gente não faz nada intencional em cima disso. A gente gera leads." O que existe é uma atribuição de receita ao lead feita no ano passado com o FP&A, por rateio dos planos vendidos. Escala declarada: ~50 mi de usuários/mês, ~4,5 mi de leads/mês, 2,6 leads por usuário em real estate, taxa de resposta da imobiliária de 50% a 58%. Confirmação inversa: quando o anunciante sai, o inventário cai e a conversão do lado do consumidor cai junto |
| Frente Imóveis | H | **C** | Triple Bundle: contrato com o Grupo, distribuição em ZAP+, VivaReal e OLX Imóveis, sem transparência de origem do lead para o anunciante |
| → Imobiliária | A | **C** | Contraparte principal. Mercado sem exclusividade: 193 mil anúncios deduplicados contra ~1,5 mi duplicados, e a deduplicação é disputada ativamente pelas imobiliárias |
| → → Plano por volume de anúncios | A | **C** | Pacotes de 10, 12, 14, 15 anúncios. Unidade: slot de anúncio ativo. Sem garantia de leads: pode receber zero ou mil. Pré-pago na grande maioria |
| → → Destaque e impulsionamento | A | **C** | Produtos de visibilidade. Benchmark internacional 30% a 50% da receita em real estate, muito acima do share atual da OLX. Saturação declarada como problema conhecido |
| → Corretor autônomo | A | **H** | Perfil confirmado como B2B ("se você é um corretor ou uma imobiliária, você é imóveis"). Peso na receita desconhecido |
| → Incorporadora | A | **H** | Mercado primário existe, PPL já testado com incorporadoras, e a calculadora Minha Casa Minha Vida gera lead genérico distribuído para esse mercado |
| → → Contrato de mídia | A | A | Sem sinal |
| Frente Autos | H | **C** | Marca única OLX. Mesmo modelo de classificados. Mercado "já acostumado com pay per use", fricção menor para mudar modelo de cobrança |
| → Concessionária | A | **H** | Existe. Contrato por rede ou por loja segue aberto |
| → Revenda / dealer | A | **H** | Existe, mas o termo segue sem definição do cliente |
| → Vendedor pessoa física | A | **H** | Leonardo Costa cuida "de privados e profissionais", o que sugere segmentação formal privado x profissional. Confirmar se "privado" gera receita |
| → Sobrou operação transacional? | A | **H negativa** | Nenhuma menção a compra e venda direta de veículo em 2h de conversa sobre receita de autos |
| Canal indireto | A | **H negativa** | Nenhuma revenda, franquia ou agência vendendo em nome do grupo |
| Formação do preço | A | **H** | Nó ativo: é aqui que a movimentação de 2026 aconteceu |
| → Tabela por porte e praça | A | **H** | Existe escada de pacotes e leitura regional de metas. Tabela vigente não entregue |
| → Desconto praticado | A | **C** | Aumento expressivo de preço em 2026 baseado em consultoria e benchmark, para recuperar rentabilidade, seguido de churn e downgrade. Política de condição na recontratação existia e foi endurecida |
| → Alavanca de expansão | A | **C** | Upgrade na escada de pacotes, produtos de visibilidade e rentabilização de carteira pelo executivo comercial via "Spark". Teto declarado: saturação da visibilidade |
| → Onde está a margem | A | **H** | Margem bruta ~100%, sem COGS de produto. Ofensores: mídia e imposto. Não existe abertura por linha |
| Caminho do dinheiro até a conta | A | **H** | Multi-handoff confirmado por declaração: "tem produto, tem marketing, tem operações, tem time comercial, e você tem interfaces diversas". E a própria OLX precisou de um workshop para desenhar a jornada |
| → Contrato assinado | A | **H** | Entrada por canal online, inside sales ou field sales conforme porte. Hunter e farmer separados, podendo coincidir em contas grandes. Quem precifica e quem aprova exceção de desconto: aberto |
| → Faturamento | A | **C** | Pré-pago (maioria em imóveis) e pós-pago (contas de campo) |
| → Cobrança e inadimplência | A | **C** | Gestão de pagamento cobra a carteira de maior receita no pré-pago; time de cobrança persegue receita devida no pós-pago. **Nenhum dos dois olha performance do cliente** |
| → Renovação | A | **C** | Pré-pago: renova quem paga de novo, com IA e régua de touch. Não existe CS de retenção olhando resultado do cliente; o papel consultivo mora no executivo comercial das contas maiores |
| Linhas fora da árvore | A | **C** | Ver §4.3 |

### 4.2 Nós novos a criar

| Onde | Nó novo | Estado | Por quê |
|---|---|---|---|
| Frente Autos | **Locadora** | C | Já opera em pay per lead hoje, segmento nomeado por Iuna |
| Frente Imóveis → Imobiliária | **Tier de plano** | H | Existem ao menos três tiers, e o básico não recebe lead similar. O tier é variável de precificação e de entrega |
| Canal indireto | **Parceiro financeiro na jornada** | H | Banco/financeira recebe lead do lojista via OLX e paga para entrar na jornada. Não é anunciante, mas gera receita |
| Caminho do dinheiro | **Remuneração do comercial** | C | 75% carteira + 25% scorecard estratégico, sem indicador de retenção ou qualidade |
| Raiz | **Frente Goods** | fora de escopo | Registrar explicitamente como excluída, com a data e quem decidiu, para não voltar como dúvida |
| Formação do preço | **Ausência de garantia de performance** | C | "ele pode receber zero ou 100 leads. Não tem garantia." É o atrito central entre atenção e ação, e foi nomeado como causa de churn |

### 4.3 Conteúdo do nó "Linhas fora da árvore"

Seis candidatos apareceram, todos ligados ao lado B2C que hoje não é monetizado de forma intencional:

1. **Lead similar**: contato distribuído a no máximo três imobiliárias, por opt-out, disponível só nos
   tiers superiores. **5% do volume total de leads.**
2. **Calculadora Minha Casa Minha Vida**: gera lead genérico para o mercado primário e distribui.
3. **Lead de financiamento em Autos**: já enriquecido com valor de entrada e status de aprovação de
   crédito.
4. **Parceria financeira**: o banco paga para entrar na jornada e recebe o lead do lojista via OLX.
5. **Ferramenta de enriquecimento de lead**: lançamento previsto em evento de outubro de 2026.
6. **Canal WhatsApp B2C com IA de recomendação**, em construção com a Meta.

### 4.4 Nuvem de Conflito: a versão do cliente é melhor que a nossa

O registro provisório propunha "mídia como custo fixo x CAC financiado pelo LTV". Essa nuvem existe
(Florence a formulou: "hoje eu estou limitada na mídia paga, meu dinheiro acaba, eu não faço mais
aquisição"), mas a transcrição entrega **uma nuvem melhor, específica de marketplace de dois lados**,
e formulada pelos próprios executivos:

```
Objetivo comum:  sustentar a receita do marketplace
  Necessidade A: proteger a rentabilidade
    Pré-requisito D:  deixar sair o cliente pequeno que não paga o custo
  Necessidade B: proteger a liquidez da plataforma
    Pré-requisito D': reter o cliente pequeno, porque o inventário dele é único e gera a demanda
D e D' conflitam na mesma decisão de retenção.
```

Fala que a sustenta, [sala SP] 01:06:17: "esse inventário que ele tira da nossa plataforma, na
receita direta ele pode não mexer muito os meus ponteiros, mas no balance do meu marketplace ele
afeta para caramba." E Iuna, 01:08:58: "às vezes o pequeno é quem tem um inventário único, e é esse
inventário único que vai gerar a atratividade da plataforma."

Uma segunda nuvem, também deles: **modelo de cobrança**, classificados/listing (previsível, aceito
pelo mercado) contra pay per lead (alinha incentivos, mas gera fricção e risco de evasão, com o
precedente do concorrente que perdeu base e depois recuperou).

---

## 5. O que continua totalmente aberto

23 perguntas sem nenhum sinal, mais 34 parciais que têm sinal e não fecham. As que mais custam ao
Ciclo 1:

| Bloco | Pergunta | Por que dói |
|---|---|---|
| 03 | Receita 24m aberta por unidade, segmento e linha | Sem ela o Forecast não roda. **Comprometida** por Matheus e Iuna |
| 03 | Ticket médio, ciclo de venda, MRR/ARR, base ativa com entradas e saídas | Insumos matemáticos do fluxo |
| 03 | Sazonalidade | Explica quebras na série |
| 04 | Funil desenhado com nomes internos, volumes e conversões por etapa | O funil não tem contra o que ser validado |
| 04 | CRM e fonte de verdade do pipeline, estágios, critério de qualificação escrito | Qualificação foi votada como trava por Matheus e ninguém descreveu o critério |
| 04 | Motivos de cancelamento são registrados? | Pergunta feita, **resposta não capturada** |
| 05 | Verba de mídia por unidade e canal, e quem é o DRI da aquisição | Dener perguntou "quem é a pessoa de aquisição mesmo?" e não houve resposta clara. Isso é achado, não só lacuna |
| 05 | Salesforce Marketing Cloud, domínios B2B, LPs, criativos, sociais, GEO | Cinco dos nove diagnósticos contratados sem insumo |
| 06 | GA4/GTM, e o que pode sair da OLX com qual anonimização | Bloco H é prioritário e LGPD não foi tratada |
| 3B | Tabela de preços vigente e desconto médio por segmento | Fecha a ponte entre Trava de Decisão e Trava de Retenção |
| 3B | Unidade de cobrança formal (quem é o CNPJ pagante, por rede ou por loja) | Fecha 3B-0 |
| 07 | O que faria isto ser fracasso | Não foi perguntada |
| 08 | SLA, blackouts, canal assíncrono, e a conciliação dos 12 encontros | Ritual não travado vira remarcação em outubro |
| 09 | R$ 740k x R$ 752k | Não foi tratado na reunião |

---

## 6. Correções ao registro provisório

O [registro feito sobre o resumo](../PENDENCIAS.md) precisa de três correções depois da transcrição:

1. **3B-10 estava errado.** A hipótese de que a OLX só enxerga cancelamento formal cai: os quatro
   modos de morte de conta estão no vocabulário deles (§2.4). O achado verdadeiro é outro e é mais
   forte: não existe CS de retenção que olhe a performance do cliente.
2. **3B-4 estava errado por ausência.** A hipótese "a expansão na base não é gerida" cai: existe
   escada de upgrade, existem produtos de visibilidade e existe uma ferramenta de rentabilização de
   carteira ("Spark"). O limite declarado é saturação, não ausência de gestão.
3. **Autos não estava ausente.** O silêncio era do resumo, não da reunião. Autos aparece o tempo
   todo: locadoras em PPL, lead de financiamento com aprovação de crédito, marca única, mercado
   habituado a pay per use. A pendência #5 fecha por outro caminho: **as duas verticais estão no
   escopo e Goods está fora.**

E uma correção na própria ata: a lista de participantes da V4 no arquivo
[`2026-08-24-kickoff.md`](2026-08-24-kickoff.md) está errada. Estiveram **Dener Lippert, Gustavo
Figueiredo, Leonardo Rosa e Gabrielle Rosa**. Rafael Corazza, Anselmo Bueno e Guilherme Monteiro
não aparecem na transcrição nem na lista de convidados.

---

## 7. O que já foi aplicado, e o que falta

### ✅ Aplicado no portal em 26/08

**`portal/assets/form-data.js`** ganhou o objeto `RESPOSTAS`, com as 96 respostas apuradas, chaveadas
por bloco e índice da pergunta. É o registro de máquina do que a transcrição responde.

**`portal/_src/kickoff.html`**: o formulário deixou de nascer vazio. A chave de `localStorage` subiu
para `dre-olx-kickoff-v2`, para que quem já abriu a página antes receba o conteúdo novo em vez de
continuar vendo o rascunho vazio do próprio navegador. Botão **Restaurar apuradas** volta ao texto da
transcrição. O contador passou a distinguir três estados, e não dois: um campo com "Não tratado" tem
texto mas não é resposta, e contá-lo como respondido marcaria 100% com um terço do material em
aberto. Hoje a barra mostra **41%, 39 respondidas, 34 parciais, 23 em aberto**. A ata exportada
carrega a mesma distinção. O textarea passou a crescer com o conteúdo, porque as respostas ficaram
longas e três linhas com rolagem escondiam justamente a evidência citada.

**`portal/_src/receita.html`**: SEED substituído pelo §4 inteiro, de 22 para 39 nós, e chave em
`dre-arvore-receita-v2` pelo mesmo motivo. Página reconstruída com `portal/build.py` e verificada em
navegador: 39 nós, 2 abertos, 16 hipóteses, 21 confirmados, sem erro de console.

### Falta aplicar

### `dados/client.json` (version 4 → 5)
- `briefing.hipotese_cliente`: Retenção e Qualificação, com o placar nominal do §2.7, rotulado como
  percepção da liderança em 24/08/2026.
- `briefing.unidades_negocio`: `no_escopo: true` nas duas, e acrescentar Goods com `no_escopo: false`.
- `briefing.modelo_receita`: pay per listing mais visibilidade, com PPL em nichos.
- `stakeholders`: acrescentar Florence Scappini, Iuna Scheffler, Leonardo Costa, Flavia Cardoso,
  Matheus Rodrigues, Carolina Dallolio, Lu Machim e "Gui" (CFO, nome a confirmar). Rever o campo
  `decisor`, hoje fixado em Mirella.
- `travas.retencao.evidencias` e `travas.cegueira.evidencias`: os itens dos §2.4, §2.5 e §06-1 já
  são fato observável com fala literal, então podem entrar. **Score continua `null`**: nota acima de
  3 exige evidência formal, e evidência formal ainda é o material do §5.

### `PENDENCIAS.md`
- **#5 (escopo por unidade): fecha.** Autos e Imóveis dentro, Goods fora, declarado em 24/08.
- **#12 (campanhas parecem B2C): fecha como achado, não como erro.** A OLX confirmou que a
  monetização do lead B2C não é intencional e que a mídia é lida como verba com teto. As campanhas
  `vr_pf` são coerentes com um marketplace que compra audiência de consumidor para vender inventário
  ao anunciante. Vira insumo do nó "Origem do valor: audiência B2C", não inconsistência.
- **#6 (acessos): atualizar** com o chamado individual por pessoa e o prazo de 26/08.
- **#7 (comitês): avança**, com o desenho semanal/mensal/trimestral, mas segue aberta a conciliação
  com os 12 encontros do contrato.
- **#2 (Success Fee): avança**, com o eixo margem/NRR/ROIC validado pelo cliente e a data do comitê.
- 🔴 **NOVA:** Dener declarou verbalmente, às 02:00:23, uma janela de saída "até o comitê" em que a
  OLX poderia encerrar sem ônus. A cláusula 2.3 do contrato encerra a garantia **no primeiro
  encontro**, que já ocorreu em 24/08. Há divergência entre o dito e o assinado, e o dito está
  gravado. Precisa ir para a ata e, se for para valer, para o aditivo.
- 🟡 **NOVA:** oferta de ingressos de Rock in Rio feita em reunião a executivos do cliente
  (02:03:51). Conta corporativa desse porte costuma ter política de brindes e hospitalidade.
  Verificar antes de qualquer encaminhamento.

### `06-reunioes/2026-08-24-kickoff.md`
A ata pode ser preenchida por inteiro a partir daqui: presentes corrigidos, decisões (§2.1, §2.8,
§07-3, PPL), UDEs (§9) e próximos passos (§10).

---

## 8. Números que apareceram e ainda não são dado

Transcrição automática corrompe cifra. Nenhum destes entra em material de comitê sem confirmação
formal. Todos foram pedidos, direta ou indiretamente, no material que Matheus e Iuna vão preparar.

| Número dito | Quem | Confiança | Uso pretendido |
|---|---|---|---|
| ~4,5 mi de leads/mês (grupo) | Matheus | média (resumo e transcrição concordam) | Denominador do lado B2C |
| ~50 mi de usuários/mês | citado pela sala e confirmado | média | Tamanho da audiência |
| Faturamento do grupo ~R$ 100 a 120 mi/mês | [sala SP] | baixa (pergunta e resposta imprecisas) | Âncora do Forecast |
| 2,6 leads por usuário em real estate | Leonardo Costa | alta | Métrica de fluxo |
| Taxa de resposta ao lead 50% a 58% | Leonardo Costa | alta (medida por cliente oculto) | Trava de Compromisso do outro lado |
| Lead similar = 5% do volume | Leonardo Costa | alta | Dimensiona a linha nova |
| 193 mil anúncios deduplicados x ~1,5 mi duplicados | Leonardo Costa | média (transcrição diz "15 milhão", resumo diz 1,5 mi) | Inventário real |
| Variável do executivo 75/25 | Iuna | alta | Política implícita da CRT |
| Pacotes de 10, 12, 14, 15 anúncios | [sala SP] | alta | Escada de downgrade |
| Queda de ~20% da oferta em uma faixa de preço | [sala SP] | baixa (exemplo hipotético) | não usar |

---

## 9. UDEs candidatos, agora com fala literal

Meta do método: 8 a 15. Estes doze já são fato observável, com fonte na transcrição. Falta atribuir
frequência e dono a cada um antes de entrarem na CRT.

| # | UDE | Ancorado em |
|---|---|---|
| 1 | Em Imóveis, as entradas não compensam churn mais downgrade (net de receita negativo) | Iuna, 01:07:38 · [sala SP], 01:04:39 |
| 2 | O anunciante compra posição e não recebe garantia de lead, podendo receber zero | Dener e Leonardo Costa, 01:35:23 |
| 3 | O aumento de preço de 2026 coincidiu com queda de performance percebida, e o cliente saiu | [sala SP], 01:21:24 |
| 4 | A escada de pacotes facilita o downgrade em vez de conter a saída | [sala SP], 01:20:27 |
| 5 | Não existe CS de retenção que olhe a performance do cliente; a cobrança só olha contas a receber | [sala SP], 01:23:23 |
| 6 | A variável do executivo comercial não tem indicador de retenção nem de qualidade | Iuna, 01:26:30 |
| 7 | Não existe leitura por safra, nem LTV, nem CAC por cliente, para orientar a aquisição | Florence, 01:01:09 · Iuna, 01:02:48 |
| 8 | A aquisição é guiada por preço e oferta, não por segmento, região ou valor do cliente | Iuna, 01:02:48 |
| 9 | O CAC é uma média, sem abertura por iniciativa ou frente | [sala SP], 01:41:53 |
| 10 | Quando a verba de mídia acaba, a aquisição para | Florence, 00:39:13 |
| 11 | O dado existe mas não está em harmonia entre as áreas, e não vira análise | Florence, 01:00:04 e 01:01:55 |
| 12 | O lead entregue não é respondido em ~46% a 50% dos casos | Leonardo Costa, 01:46:14 |
| 13 | A monetização do lead B2C não é intencional; o principal ativo não tem gestão de receita | [sala SP], 02:05:12 |
| 14 | A jornada de aquisição só ficou desenhada depois de um workshop interno | Florence, 00:38:08 |

Os itens 5, 6, 7, 8, 9 e 10 apontam para o mesmo lugar e são formuláveis como uma política implícita
única, forte candidata a causa-raiz:

> **"Aquisição e retenção são medidas por faturamento e por verba, não por valor do cliente ao longo
> do tempo. Como ninguém sabe quanto um cliente vale, ninguém sabe quanto se pode pagar por ele nem
> quanto custa perdê-lo."**

Note que essa política sobrevive à correção do §6: mesmo tendo alavanca de expansão e vocabulário de
churn, a OLX não tem a régua que ligaria uma coisa à outra.

---

## 10. Decisões e próximos passos capturados, para a ata

**Decisões**

| # | Decisão | Fonte |
|---|---|---|
| 1 | Escopo: Autos e Imóveis. Goods fora | [sala SP], 01:27:31 |
| 2 | Prioridade para iniciativas de curto prazo, sem abandonar médio e longo | Florence, 00:20:36 |
| 3 | Margem acima de receita: não se sacrifica EBITDA por receita | Matheus, 01:57:36 e 01:58:27 |
| 4 | Método: Teoria das Restrições, ciclos de até 90 dias, uma restrição por ciclo | Dener, 01:48:08 |
| 5 | Migração total da base de Imóveis para pay per lead está descartada | Iuna, 01:13:14 |
| 6 | Testes de PPL e de garantia em grupos específicos estão aprovados | Dener e Iuna, 01:14:18 |
| 7 | Material assíncrono antes das reuniões, sem apresentação formal | Dener, 01:51:32 |
| 8 | Comitê de identificação da restrição pré-setado para 10/09 | Iuna e Dener, 02:03:51 |

**Próximos passos**

| # | Ação | DRI | Prazo |
|---|---|---|---|
| 1 | Concluir a liberação de acessos (chamados individuais) | Michelle Morais / Florence | 26/08 |
| 2 | Material de metas: metas por etapa do fluxo, receita por vertical, visão global, overview 2026 | Matheus Rodrigues + Iuna Scheffler | antes de 09/09 |
| 3 | Documentação de P&L por vertical | Matheus Rodrigues | antes de 09/09 |
| 4 | Diagnóstico das travas, contagem de 15 dias a partir de 25/08 | V4 | 09/09 |
| 5 | Sugestão de meta de projeto ancorada nas metas da OLX | V4 (Dener) | 10/09 |
| 6 | Agendas dos comitês trimestrais presenciais | Gabrielle Rosa | 25/08 |
| 7 | Definir o local do comitê de 10/09 (escritório V4 ou Rio) | Leonardo Costa + V4 | 25/08 |
| 8 | Touch points com o time de operação para validar a jornada | V4 + Carolina Dallolio | até 09/09 |
