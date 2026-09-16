# Dashboards de Aquisição PRO · leitura

> **Fonte:** 16 capturas de tela do Looker Studio do Grupo OLX, feitas em **16/09/2026**, versionadas em
> [`assets/originais/A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/`](../assets/originais/A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/)
> · par de máquina em [`dados/outputs/dashboards-aquisicao-pro.json`](../dados/outputs/dashboards-aquisicao-pro.json)
>
> ⚠️ **Dado do cliente, não auditado pela V4.** Todo número aqui é `[D]`: é o que o dashboard da OLX
> exibe, não o que a V4 mediu. Nenhum deles foi conferido contra o BigQuery de origem.

São **dois relatórios**, um por modelo de venda, com a mesma arquitetura de páginas:

| Relatório | ID | Mede | Páginas versionadas |
|---|---|---|---|
| **Aquisição Offline PRO \\ Marketing** | `38f3663c…0fd94c2` | Venda assistida: lead → MQL → SQL → venda, com receita | 11 |
| **Aquisição Online PRO \\ Marketing** | `f378f073…5ea3d1a` | Autosserviço no checkout: sessão → identificada → vitrine → checkout → venda | 5 |

Eles são a entrega prometida por **Michelle Morais** em 10/09 ("a gente faz muito mais aqui pelo
Looker") e registrada como item 3 da [pendência 32](../PENDENCIAS.md). Chegaram como **print, não como
link**: dá para ler, não dá para filtrar nem extrair.

## O que isto destrava

| Item do checklist | Antes | Agora |
|---|---|---|
| **A2** · funil comercial com volumes e taxas, 12–24 meses | 🟡 4 meses, só Inside Sales | 🟡 **13 meses, aquisição inteira**, por canal. Falta série exportável e movimento de base |
| **A3** · ticket médio, ciclo de venda e **CAC por canal** | 🟡 sem CAC | 🟡 **primeiro CAC de mídia com numerador B2B**, ver abaixo. Falta CAC dos demais canais |
| **B3** · performance de canais de CRM | ⚪ | 🟡 volume e venda por canal de CRM, 13 meses |

E resolve, de lado, a maior lacuna declarada do [mapa dos números](mapa-de-numeros.md): *"nenhum CAC
de mídia tem numerador válido"*, porque os R$ 10,12 mi apurados no V4MOS misturam B2B e B2C. Este
dashboard traz um recorte **só B2B**, de R$ 951,5 mil.

---

## 1. O funil offline, ponta a ponta

Janela **01/09/2025 a 15/09/2026** (12,5 meses), verticais **Autos e Imóveis**.

| Etapa | Volume | Conversão da etapa | Acumulado sobre o topo |
|---|---:|---:|---:|
| Leads totais | **131.782** | - | 100% |
| MQL | **87.368** | 66,3% | 66,3% |
| SQL | **50.450** | 57,7% | 38,3% |
| Venda | **12.068** | 23,9% | **9,2%** |

Receita associada: **R$ 14,0 mi**, ticket médio **R$ 1,01 mil**, `life_time` **4,0**, `receita_ltv`
**R$ 46,0 mi**. Recorrente R$ 11,4 mi (+8%), oneshot R$ 798,6 mil (-39%).

**Conferência interna:** as três séries mensais somam **exatamente** os totais do topo (SQL 50.450,
venda 12.068, MQL 87.368) e as seis linhas da tabela de canais também. O dashboard é internamente
consistente.

### Série mensal

| Mês | MQL | SQL | Venda | Qualificação | Conversão |
|---|---:|---:|---:|---:|---:|
| ago/25 | 7.976 | 4.274 | 1.165 | 54% | 27% |
| set/25 | 7.968 | 3.981 | 1.077 | 50% | 27% |
| out/25 | 7.31x `[E]` | 4.208 | 1.102 | 58% | 26% |
| nov/25 | 6.428 | 3.866 | 1.037 | 60% | 27% |
| dez/25 | 4.065 | 2.257 | 647 | 56% | 29% |
| jan/26 | 7.406 | 3.706 | 891 | 50% | 24% |
| fev/26 | 6.330 | 3.932 | 632 | 62% | 16% |
| mar/26 | 8.219 | 5.063 | 1.045 | 62% | 21% |
| abr/26 | 8.140 | 5.127 | 1.232 | 63% | 24% |
| mai/26 | 6.771 | 4.438 | 1.132 | 66% | 26% |
| jun/26 | 7.265 | 3.968 | 1.064 | 55% | 27% |
| jul/26 | 6.780 | 4.073 | 982 | 60% | 24% |
| ago/26 | 7.16x `[E]` | 3.957 | 886 | 55% | 22% |
| set/26 (15 d) | 3.521 | 1.874 | 341 | 53% | 18% |

> **Os dois `[E]` são de renderização, não de estimativa livre.** Em out/25 e ago/26 o rótulo de MQL
> fica coberto pelo rótulo de percentual no gráfico. O que se lê são os primeiros dígitos, e a soma
> dos dois está **fixada em 14.475** pela reconciliação com o total de 87.368. Ou seja: out/25 está
> entre 7.306 e 7.315, e ago/26 entre 7.160 e 7.169. Resolve-se com um print da tabela, não com
> estimativa.

**A leitura da série.** O topo oscila sem tendência (6,3 a 8,2 mil MQL/mês, fora dez/25). A
**qualificação melhorou**: de 50–54% no fim de 2025 para 55–66% em 2026. E a **conversão final piorou**:
de 27% para 22%. O sistema qualifica mais e fecha menos, e o resultado líquido é venda caindo de
~1.100/mês para ~900/mês. A queda de venda é de **-25,1%** contra os 380 dias anteriores, com MQL
caindo só 9,0%: **a perda está depois do MQL, não antes dele.**

---

## 2. Por canal · onde entra e onde fecha

Mesma janela, mesmas verticais. Receita arredondada pelo próprio dashboard.

| Canal | MQL | % do topo | SQL | Venda | % da venda | MQL → venda | Receita |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Direto** | 27.251 | 31,2% | 20.346 | **6,4 mil** | **53,0%** | **23,5%** | R$ 8 mi |
| **CRM** | 30.575 | **35,0%** | 20.577 | 3,7 mil | 30,7% | 12,1% | R$ 4 mi |
| Outros canais | 10.936 | 12,5% | 4.925 | 1,1 mil | 9,1% | 10,1% | R$ 1 mi |
| **Mídia Paga** | 16.532 | 18,9% | 3.427 | **645** | **5,3%** | **3,9%** | R$ 844 mil |
| SEO | 2.070 | 2,4% | 1.171 | 262 | 2,2% | 12,7% | R$ 390 mil |
| Não se aplica | 4 | - | 4 | 2 | - | - | R$ 871 |

**O contraste que organiza a página:** CRM é o maior gerador de MQL do sistema e o Direto é o maior
gerador de venda. Um MQL de Direto vale **6 vezes** um MQL de Mídia Paga na conversão final (23,5%
contra 3,9%). Mídia Paga entrega 18,9% do topo e 5,3% da venda.

**Ressalva de atribuição, e ela é grande.** O slide de 28/08 já anotava que campanha paga para
WhatsApp *"entra tudo como Direto"*, e a [auditoria (vii)](auditoria-vii-rastreamento.md) achou o
`purchase` preso ao gatilho de `begin_checkout`. Então "Direto = 53% da venda" pode ser, em parte,
pago mal atribuído. **A hierarquia entre canais neste quadro não é confiável enquanto o
rastreamento não for corrigido**, e é por isso que o número de mídia paga da seção 3 vale mais: lá o
denominador é o investimento, que não depende de atribuição.

---

## 3. 🔴 Mídia paga: o investimento dobrou e a venda caiu

Página **Canais Pagos Performance**, offline, mesma janela.

| Métrica | Valor | vs. 380 dias anteriores | vs. ano anterior |
|---|---:|---:|---:|
| Impressões | 32.170.511 | **+80,5%** | +70% |
| Cliques | 738.057 | **+85,8%** | +69% |
| **Investimento** | **R$ 951,5 mil** | **+110,9%** | - |
| Sessões pós-clique | 803.276 | +57,5% | +52% |
| MQL | 16.532 | +7% | +3% |
| SQL | 3.427 | **-5%** | -5% |
| **Venda** | **645** | **-12%** | **-8%** |

O funil inteiro cresce até a sessão e inverte o sinal depois dela. Em número:

| | Período anterior `[E]` | Período atual | Variação |
|---|---:|---:|---:|
| Investimento | R$ 451,2 mil | R$ 951,5 mil | +110,9% |
| Venda | 733 | 645 | -12% |
| **CAC de mídia** | **R$ 616** | **R$ 1.475** | **+140%** |

> Os valores do período anterior são derivados das variações exibidas, não lidos. Marcados `[E]`.

**E o CAC não é coberto pela primeira venda.** O ticket médio de mídia paga é **R$ 1,31 mil** e a
receita atribuída são R$ 844,2 mil, ou **R$ 1.309 por venda**: menos que os R$ 1.475 de mídia gastos
para trazê-la. O canal só fecha no LTV, que o dashboard calcula em R$ 3,4 mi, **R$ 5.271 por venda**,
com `life_time` 4,0. O payback é da ordem de **13 meses de mensalidade**, e depende inteiramente de
uma retenção de 4 meses que o próprio dashboard declara e ninguém auditou.

**O que este número é e o que não é.** É o **primeiro custo de aquisição do projeto com numerador
B2B**. Não é o investimento B2B total: a página online equivalente devolve investimento em branco, e
as campanhas do Meta não aparecem com custo aqui. Então **R$ 951,5 mil é piso, não total**.

Complementos: 70,2% do investimento é Google e 24,7% Meta; **96,4% do objetivo é Novo Cliente**; e
86,6% das desqualificações são *"contato sem sucesso"*, não recusa comercial.

---

## 4. CRM é WhatsApp, e o resto é ruído

As três páginas de CRM do relatório offline somam **exatamente** o canal CRM da visão geral:

| Página | MQL | % do CRM | SQL | Venda | Receita |
|---|---:|---:|---:|---:|---:|
| **WhatsApp CRM** | **29.815** | **97,5%** | 20.227 | 3.582 | R$ 3,5 mi |
| E-mail Marketing CRM | 732 | 2,4% | 332 | 70 | R$ 58,3 mil |
| Push/Central CRM | 28 | 0,09% | 18 | 4 | R$ 12,1 mil |
| **Soma** | **30.575** | 100% | 20.577 | 3.656 | - |

Isso **quantifica a [pendência 31](../PENDENCIAS.md)**, que afirmava que "100% da aquisição de CRM
depende da Blip" a partir de declaração em reunião. O número é **97,5%**, medido no dashboard da
própria OLX. A decisão sobre a saída da Blip passa a ter tamanho: são 29.815 MQL e 3.582 vendas por
ano de um canal com um único broker e sem integração ao Marketing Cloud.

Os outros dois estão em colapso, e isso é coerente com a [auditoria (i)](auditoria-i-crm-marketing.md):

- **E-mail**: -54,8% de MQL e **-63,4% de venda**. A atividade se concentra até dez/25 e some depois.
- **Push/Central**: **-97,0% de MQL**. Vinte e oito MQL em 12,5 meses é um canal desligado, não um
  canal fraco.

O WhatsApp cai pouco em volume (-3,4% de MQL) e muito em venda (**-34,6%**): mesma assinatura do
sistema inteiro, a perda está depois do MQL.

---

## 5. 🟠 Dezoito mil leads em "Trabalhando", e o estoque cresceu 17 vezes

Página **MQL Detalhamento**, mesma janela.

| `status_lead` | Leads | % | MQL | Δ leads vs. período anterior |
|---|---:|---:|---:|---:|
| Desqualificado | 62.478 | 47,4% | 34.486 | -45,7% |
| Qualificado | 50.464 | 38,3% | 50.455 | -3,8% |
| **Trabalhando** | **18.840** | **14,3%** | 2.427 | **+1.603,4%** |
| Total | 131.782 | 100% | 87.368 | -21,8% |

O estoque de lead em atendimento saiu de cerca de **1.106** para **18.840** `[E]`. É a única linha
do dashboard que cresce em três dígitos, e cresce em quatro.

**Duas leituras, e elas levam a decisões opostas.**

**(a) É mudança de taxonomia.** Um status novo, ou uma regra de expiração que deixou de rodar, e o
que se vê é classificação, não fila.

**(b) É fila real.** Dezoito mil leads em processamento significam capacidade de atendimento
estourada, e explicariam por que a qualificação sobe (55→66%) enquanto a conversão final cai (27→22%):
entra mais lead qualificado do que o time consegue trabalhar, e ele envelhece na fila.

A hipótese (b) tem um indício externo a favor: a [leitura do Inside Sales](estrutura-comercial-inside-sales.md)
achou, em jul/26, **Autos hunter recebendo 74% mais lead com a abordagem caindo de 100% para 58%**.
Essa é a mesma assinatura.

**Como resolver:** pedir a definição de `status_lead` e a **distribuição de idade** dos 18.840. Uma
tela, não um projeto. Enquanto isso não vier, o número não entra em comitê como achado.

---

## 6. O funil online perdeu metade do tráfego

Relatório **Aquisição Online PRO**, portal ZAP/VR, objetivo Novo Cliente, `fraude: Não`.

Funil de 01 a 13/09/2026: 19.618 sessões pós → 7.413 identificadas (37,8%) → 3.665 vitrine (49,4%) →
850 checkout (23,2%) → **317 vendas** (37,3%). Taxa ponta a ponta **1,62%**.

| Mês | Sessões pós | Venda | Taxa |
|---|---:|---:|---:|
| ago/25 | 106,9 mil | 1.017 | 0,95% |
| set/25 | 103,5 mil | ~859 `[E]` | 0,83% |
| out/25 | 101,2 mil | 797 | 0,79% |
| nov/25 | 93,9 mil | 594 | 0,63% |
| dez/25 | 91,2 mil | 457 | 0,50% |
| jan/26 | 100,2 mil | ~862 `[E]` | 0,86% |
| fev/26 | 62,7 mil | 641 | 1,02% |
| mar/26 | 69,2 mil | 881 | 1,27% |
| abr/26 | 62,3 mil | 650 | 1,04% |
| mai/26 | 53,0 mil | 700 | 1,32% |
| jun/26 | 51,6 mil | 781 | 1,51% |
| jul/26 | 54,9 mil | 702 | 1,28% |
| ago/26 | 51,8 mil | 714 | 1,38% |
| set/26 (13 d) | 19,6 mil | 317 | 1,62% |

> Os dois `[E]` têm o rótulo de venda coberto no gráfico e foram derivados de sessões × taxa exibida.
> O método confere nos meses legíveis (out/25: 101,2 mil × 0,79% = 800 contra 797 exibidos).

**Entre fev e mar/26 o tráfego cai de ~100 mil para ~65 mil e nunca volta.** De ago/25 a ago/26 são
**-51,5% de sessões**, com a conversão subindo de 0,95% para 1,38% e a venda caindo **-29,8%**. A
melhora de conversão absorveu parte do golpe, não o golpe todo.

**A pergunta que isso abre não é de marketing, é de produto ou de rastreamento:** uma queda de
metade do tráfego num degrau, com conversão subindo junto, tem três explicações típicas, e nenhuma é
"a campanha piorou". Ou o tráfego não qualificado foi cortado de propósito, ou a página de origem
mudou, ou o rastreamento parou de contar parte das sessões. **O `Canal de Marketing` online mostra
Direto com sessões identificadas +51,2% e vitrine +222,4% no mês**, o que é sinal de reclassificação
de tráfego, não de comportamento.

E o CRM online praticamente não existe: 185 sessões e 3 checkouts no mês; a página de WhatsApp
online devolve **1 sessão** e nenhuma venda; a de e-mail, 150 sessões e 1 venda.

---

## 7. Reconciliações

### 7.1 🔴 Contra o Inside Sales: duas fontes da OLX para o mesmo funil, e elas não batem

| Mês | Vendas · Inside Sales (28/08) | Vendas · Looker (16/09) | Divergência |
|---|---:|---:|---:|
| abr/26 | 968 | 1.232 | -21,4% |
| mai/26 | 1.344 | 1.132 | **+18,7%** |
| jun/26 | 1.177 | 1.064 | **+10,6%** |
| jul/26 | 720 | 982 | **-26,7%** |

Em maio e junho a apresentação de Inside Sales declara **mais vendas B2B do que o Looker registra na
aquisição inteira**, o que é impossível se o Inside Sales for um subconjunto. Em abril e julho, o
oposto. Pela **regra 8** do método, divergência acima de 5% é dado inconsistente, e aqui ela chega a
27% trocando de sinal.

Não é erro de ninguém: são **duas definições de "venda"** convivendo na mesma empresa, provavelmente
por data de referência (fechamento contra faturamento) e por escopo de time. Mas é exatamente o tipo
de coisa que não pode aparecer em comitê sem resposta.

### 7.2 O mergulho de julho não se confirma no total

A [leitura do Inside Sales](estrutura-comercial-inside-sales.md) deixou duas hipóteses abertas para a
queda de 39% em jul/26: **(a)** julho estava incompleto no dashboard de 28/08, **(b)** era quebra real.

No Looker, capturado em 16/09 com julho fechado, **jul/26 tem 982 vendas contra 1.064 em junho: -7,7%**.
Não há cliff. Se o Inside Sales tivesse mesmo perdido 457 vendas num mês, o total não cairia 82.

**Isso pesa a favor da hipótese (a)**, mas não a fecha, porque a seção 7.1 mostra que as duas fontes
divergem até 27% em meses normais. O que se pode afirmar hoje: **a quebra de julho não aparece na
aquisição total**, e o achado do mergulho não deve ir a comitê como fato até a visão fechada chegar.

### 7.3 Contra a receita declarada: a aquisição inteira vale 1,6% do faturamento B2B

| | Valor |
|---|---:|
| Receita de aquisição offline, 12,5 meses | R$ 14,0 mi |
| Média mensal | **R$ 1,12 mi/mês** |
| Núcleo de assinatura B2B, run-rate da série A1 | **R$ 68,0 mi/mês** |
| Razão | **1,6%** |

Mesmo somando o LTV projetado (R$ 46,0 mi, ou R$ 3,7 mi/mês), a aquisição fica em **5,4%** do núcleo
B2B mensal.

**Antes de virar tese, isto precisa de uma resposta.** Não se sabe o que `receita_total` mede neste
dashboard: primeira fatura, contrato assinado, ou MRR incremental. Nem se o dashboard cobre key
account e enterprise, que pela [leitura do Inside Sales](estrutura-comercial-inside-sales.md) são 61%
da receita de Imóveis e 83% de Autos. Se cobrir só o que passa por marketing, a razão está certa e
**diz que o sistema de receita do Grupo OLX é de base instalada, não de aquisição**, o que reordena a
conversa de trava. Se não cobrir, a comparação é inválida. **É uma pergunta, não um achado.**

---

## 8. O que perguntar à OLX

| # | Pergunta | Por quê | Dono |
|---|---|---|---|
| 1 | **O link** dos dois relatórios, com acesso de leitura | Print não filtra, não exporta e envelhece. Sem link, nada disso se atualiza no Comitê | Michelle Morais |
| 2 | O que `receita_total`, `receita_ltv` e `life_time` medem, na definição do BigQuery | Decide se a seção 7.3 é achado ou artefato | Marketing Data |
| 3 | O dashboard cobre key account e enterprise, ou só o que passa por marketing? | Define o denominador de tudo | Marketing Data |
| 4 | Definição de `status_lead` e distribuição de idade dos 18.840 em "Trabalhando" | Separa fila real de mudança de taxonomia | Comercial |
| 5 | Por que o tráfego online cai pela metade entre fev e mar/26 | Meia base de tráfego não some por acaso | Produto + Marketing Data |
| 6 | Por que Inside Sales e Looker divergem até 27% no mesmo mês | Regra 8. Sem isso não há número de venda citável | Comercial + Marketing Data |
| 7 | O investimento de mídia B2B online, que a página devolve em branco | R$ 951,5 mil é piso do CAC, não total | Mídia |

---

## 9. Ressalvas de leitura

1. **Print, não extração.** Tudo aqui foi lido de imagem. Onde o rótulo estava coberto pelo próprio
   render, está marcado `[E]` com o método de derivação explícito. Nada foi arredondado "para ficar
   redondo".
2. **A receita por canal vem arredondada pelo dashboard** (R$ 4 mi, R$ 8 mi, R$ 1 mi). Só Mídia Paga
   e SEO aparecem com precisão suficiente para conta.
3. **Os recortes não são somáveis entre si.** "Campanha Temática / Desconto" (11.548 MQL) e "Product
   Marketing" (10.252 MQL) são cortes transversais que atravessam os canais da seção 2, não linhas
   novas.
4. **A janela é de 12,5 meses**, não 12: 01/09/2025 a 15/09/2026. Setembro está pela metade em tudo,
   e nenhuma variação mensal de setembro deve ser lida como tendência.
5. **`fraude: Não` está ligado no relatório online e não existe no offline.** Os dois não medem a
   mesma população.
