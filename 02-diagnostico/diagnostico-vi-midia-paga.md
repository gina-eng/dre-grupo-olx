# Diagnóstico (vi) · Mídia Paga (Google e Meta)

> **Fontes.** Google Ads: **export direto da interface em 16/09/2026**, 5 contas da MCC do Viva Real,
> inventário e procedência em [`assets/originais/G-midia-paga/README.md`](../assets/originais/G-midia-paga/README.md).
> Meta: **apenas o cache do V4MOS de 14/09/2026**, `dados/cache/v4mos-2026-09-14.json`.
> Par de máquina em [`dados/outputs/diagnostico-vi-midia-paga.json`](../dados/outputs/diagnostico-vi-midia-paga.json)
> e [`dados/outputs/google-ads-parque.json`](../dados/outputs/google-ads-parque.json).
>
> ⚠️ **Dado de plataforma, não auditado.** Nada aqui foi conferido contra faturamento ou contra o CRM.
> É o que o Google Ads e o V4MOS exibem.
>
> **Método.** Oito frentes de levantamento em paralelo, cada achado submetido a dois céticos
> independentes com lentes distintas (aritmética e interpretação), mais um crítico de completude.
> 84 achados levantados, 81 sobreviveram, 3 derrubados. **Depois disso, cada número que sustenta peso
> neste documento foi recalculado do zero** contra o arquivo de origem, e a seção
> [O que não pode ir ao Comitê 1](#-o-que-não-pode-ir-ao-comitê-1) registra o que a verificação
> mandou descartar, inclusive achados do próprio levantamento.

---

## A leitura

**A mídia paga do Grupo OLX não tem um problema de mídia. Tem um problema de medição, e ele é grande
o bastante para invalidar quase toda métrica de eficiência que o projeto vinha usando.**

Três fatos, cada um verificado em mais de uma fonte:

1. **O parque de Google Ads é 4,1 vezes maior do que o projeto media.** São **R$ 70,96 milhões** em
   5 contas, e a V4 vinha lendo R$ 2,75 mi. Na janela em que o V4MOS diz medir, ele cobre **15,7%**.
2. **A coluna `Conversions` do Google Ads não conta negócio.** O parque declara **158,7 milhões de
   conversões** e **R$ 5,51 trilhões** de valor, e uma campanha sozinha declara 1,74 conversão por
   impressão, o que é fisicamente impossível. Nenhum CPA, CAC ou ROAS calculado sobre essa coluna
   significa alguma coisa.
3. **O recorte contratado é 3,5% do parque**, e roda hoje com **10 unidades criativas no ar**.

O que o diagnóstico **destrava** é igualmente concreto: pela primeira vez existe separação B2B contra
B2C com evidência de negócio, e com ela o primeiro numerador de CAC de mídia B2B com fonte.

---

## 1. O parque: cinco contas, e só uma é o recorte contratado

| Conta | Recorte | Campanhas | No ar | Investimento acumulado | % |
|---|---|---:|---:|---:|---:|
| `conta-1-zapmais-b2b` | **B2B** | 56 | 9 | R$ 2.455.122,45 | 3,46% |
| `conta-2-vivareal-marca` | B2C | 3 | 2 | R$ 1.282.927,13 | 1,81% |
| `conta-3-vivareal-sp` | B2C | 9 | 6 | R$ 2.384.921,36 | 3,36% |
| `conta-4-vivareal-brasil` | B2C | 92 | 14 | R$ 63.330.730,81 | **89,3%** |
| `conta-5-vivareal-app` | B2C | 17 | 0 | R$ 1.454.877,67 | 2,05% |
| **Total** | | **177** | **31** | **R$ 70.908.579,42** | |

A soma bate com a linha `Total: Account` do próprio export em três contas e diverge em duas, por
campanha removida cujo gasto fica no total e não aparece na lista: R$ 20.980,39 na `conta-1` e
R$ 33.036,57 na `conta-5`. O total pela linha de conta é R$ 70.962.596,39.

**Cento e quarenta e seis campanhas de 177 estão pausadas**, e o gasto acumulado é de dez anos, não
de um ano. Ler estes R$ 70,96 mi como orçamento corrente seria erro grosseiro.

---

## 2. 🔴 A pendência 12 estava errada, e agora dá para provar

A [pendência 12](../PENDENCIAS.md) está aberta desde 24/08 com a hipótese de que o sufixo `_pf` da
convenção de nomenclatura significa **pessoa física**, e portanto que até 90% da mídia do grupo
estaria fora do recorte B2B. A própria pendência avisava, em nota, que aquilo era leitura de
nomenclatura e não podia ir a comitê. O aviso estava certo.

**O teste.** 73 das 177 campanhas seguem a convenção. Nelas:

| | |
|---|---|
| Campanhas com o token `pf` na última posição | **73 de 73**, 100% |
| Dentro da `conta-1`, a conta B2B | **25 de 25**, 100% |

**Um token que aparece nos dois lados não separa os dois lados.** `_pf` não pode significar pessoa
física.

**O que separa é o penúltimo token**, e a URL de destino do anúncio confirma sem uma única travessia:

| Token | Campanhas | Destino dos anúncios | Observações |
|---|---:|---|---:|
| `go` | 25, todas na `conta-1` | `www.zapmais.com.br`, `anuncie.zapimoveis.com.br`, `conteudo.zapmais.com` | 68 |
| `vr` | 48, nas contas 2, 3 e 4 | `www.vivareal.com.br` | 33 |

Zero anúncios `go` apontando para VivaReal, zero anúncios `vr` apontando para zapmais ou anuncie.
**101 observações, nenhuma travessia.** Isto é dado de negócio, não nomenclatura: `anuncie.` e
`zapmais.` são superfícies de captação de anunciante profissional.

**A conclusão de negócio da pendência sobrevive, com outro número e por outro caminho.** Não é que
90% da mídia seja B2C por causa de `_pf`. É que **o B2B é 3,46% do parque**, e isso se prova por
conta e por URL de destino.

**O que continua aberto:** 104 das 177 campanhas não seguem a convenção, e elas carregam parte
relevante do gasto. E no Meta a pergunta permanece indecidível: não há URL de destino no material.

---

## 3. 🔴 A medição que o projeto usava é uma conta de performance regional de São Paulo

O V4MOS é a única leitura de mídia que a V4 tem em máquina, e é a base de tudo que o projeto escreveu
sobre mídia paga desde junho.

| Janela 01/01/2025 a 14/09/2026 | Google Ads |
|---|---:|
| Gasto real das 5 contas, somado da série trimestral | **R$ 17.445.178,92** |
| O que o V4MOS reporta | **R$ 2.746.029,59** |
| **Cobertura** | **15,7%** |
| Invisível | R$ 14,70 mi |

E a parte que o V4MOS enxerga **não é uma amostra do parque, é uma conta específica**:

| Trimestre | V4MOS (soma dos meses) | `conta-3-vivareal-sp` | Diferença |
|---|---:|---:|---:|
| 2T/2025 | R$ 288.038,25 | R$ 288.038,46 | R$ 0,21 |
| 3T/2025 | R$ 269.423,46 | R$ 269.423,84 | R$ 0,38 |
| 4T/2025 | R$ 62.938,23 | R$ 62.938,35 | R$ 0,12 |
| 1T/2026 | *(sem dado)* | R$ 0,00 | - |
| 2T/2026 | R$ 315.486,89 | R$ 315.487,48 | R$ 0,59 |

**De abril de 2025 a junho de 2026 a série mensal do V4MOS é, centavo por centavo, a `conta-3` e nada
mais.** Só no 3T/2026 ela passa a somar outras contas.

Isso resolve, de passagem, uma anomalia registrada no [mapa dos números](mapa-de-numeros.md): o
buraco de nov/2025 a abr/2026 na série de Google **não é falha de ingestão**. É a `conta-3` parada:
o 1T/2026 dela é R$ 0,00 no próprio export do Google.

**A consequência é dura e precisa ser dita assim:** todo diagnóstico de mídia do Google escrito neste
projeto antes de 16/09 foi feito sobre a conta de performance regional de São Paulo do VivaReal.
Dos R$ 2,75 mi que o V4MOS vê, **R$ 42.245,79, ou 1,5%, são B2B**.

### 3.1 🔴 Sete arquivos afirmam que o Meta pesa 2,7 vezes o Google, e a comparação é inválida

A frase aparece em `02-diagnostico/fluxo-de-receita.md`, `mapa-de-numeros.md`,
`diagnostico-travas.md`, `PENDENCIAS.md`, `01-cliente/acessos-e-ferramentas.md`,
`04-execucao/sprint-diagnosticos-10-a-18-09.md` e na `SKILL.md` da `dre-v4mos`.

Ela compara **todo o Meta que o V4MOS vê** com **15,7% do Google**. Medido contra o parque real de
Google na mesma janela, o sinal inverte: **R$ 17,45 mi de Google contra R$ 7,38 mi de Meta, ou
2,4 vezes a favor do Google**.

> A correção honesta não é trocar 2,7 por 2,4. É dizer que **a razão entre Meta e Google não é
> conhecida**, porque o lado do Meta também é só o que o V4MOS ingere, e não existe export direto de
> Meta no repositório para conferir.

---

## 4. 🔴 A coluna `Conversions` do Google Ads não conta negócio

| Parque inteiro | |
|---|---:|
| Conversões declaradas | **158.663.191** |
| Valor de conversão declarado | **R$ 5.511.285.299.051** |
| Investimento | R$ 70,91 mi |
| Custo por "conversão" | R$ 0,45 |

R$ 5,51 **trilhões** é aproximadamente 4.400 anos do faturamento do grupo. O campo não é receita: nas
campanhas de compra ele tem a ordem de grandeza do **preço do imóvel anunciado**.

**A prova que não depende de julgamento:**

| Campanha | Conta | Custo | Conversões | Impressões | Conv. por impressão |
|---|---|---:|---:|---:|---:|
| `pmaxssbr_gg_pm_bg_tf_tp_wb_re_vr_pf` | conta-4 | R$ 835.386,75 | **94.045.472** | 54.038.831 | **1,74** |

Uma conversão por impressão já é implausível. **Uma vírgula setenta e quatro é impossível**, e essa
campanha sozinha responde por 59,3% das conversões do parque com 1,2% do investimento.

**O que isso invalida, e é muito:**

- Qualquer CPA, CAC ou ROAS da plataforma, em qualquer das 5 contas.
- A nota de otimização e, mais grave, **o próprio leilão**: as campanhas de maior gasto usam Target
  CPA e Maximize Conversions, ou seja, **o lance é dado contra este sinal**.
- Qualquer leitura de tendência que atravesse a quebra: o custo por conversão da `conta-4` sai de
  R$ 0,10 no 1T/2025 para R$ 3,27 no 3T/2026, e isso é mudança do que se conta, não de performance.

Isso conversa diretamente com a [auditoria (vii)](auditoria-vii-rastreamento.md), achados 1
(`purchase` no gatilho de `begin_checkout`) e 7 (dupla contagem de conversão no Google Ads). **Mas a
dupla contagem não explica esta ordem de grandeza:** dobrar não leva de milhares a 94 milhões.

> **Não há relatório de ações de conversão em nenhuma das 5 contas.** Ninguém no projeto consegue
> nomear que evento está sendo contado. Enquanto isso durar, "custo por conversão" não é métrica de
> negócio, e a regra da casa proíbe usá-la.

---

## 5. A mídia B2B roda com dez unidades criativas no ar

A `conta-1` tem 56 campanhas, **9 no ar**. Descendo até o nível do criativo, com anúncio, grupo de
anúncios e campanha todos habilitados:

| Superfície viva | Quantidade |
|---|---:|
| Anúncios responsivos de busca | **7**, em 6 campanhas |
| Grupos de ativos de Performance Max | **3**, em 2 campanhas |
| **Total** | **10** |

**Toda a aquisição paga de anunciante profissional do Grupo OLX está apoiada em dez peças.** Para a
trava de **Atenção**, isso é o próprio diagnóstico: não há o que testar, não há variação, não há
rotação.

### 5.1 🔴 Uma campanha no ar gasta R$ 22.179,98 por conversão, ao lado de outra que gasta R$ 15,78

As 9 campanhas no ar da `conta-1`, com o custo por conversão do próprio Google:

| Campanha | Custo | Conversões | Custo / conv. |
|---|---:|---:|---:|
| `sebroffbr_..._go_pf` | R$ 539.672,33 | 10.740,72 | R$ 50,25 |
| `pmaxoff26br_..._go_pf` | R$ 159.114,36 | 10.081,04 | **R$ 15,78** |
| `senbwppbr_..._go_pf` | R$ 117.493,68 | 3.407,05 | R$ 34,49 |
| `sebroffsp_..._go_pf` | R$ 55.409,28 | 523,76 | R$ 105,79 |
| **`pmaxon26br_..._go_pf`** | **R$ 22.179,98** | **1,00** | **R$ 22.179,98** |
| `senb26sp_..._go_pf` | R$ 10.764,75 | 95,08 | R$ 113,21 |
| `senbonbr_..._go_pf` | R$ 1.944,66 | 37,00 | R$ 52,56 |
| `sebronbr_..._go_pf` | R$ 1.836,80 | 15,00 | R$ 122,45 |
| `senboffbr_..._go_pf Venda On - 2024` | R$ 0,00 | 0,00 | - |

`pmaxon26br` e `pmaxoff26br` são **a mesma conta, o mesmo ano, o mesmo tipo de campanha**, e a
diferença entre elas é o token de jornada: `on` contra `off`. Uma entrega por R$ 15,78, a outra por
R$ 22.179,98. **Fator de 1.405 vezes.**

> **Ressalva obrigatória:** este quadro usa a coluna `Conversions`, que a seção 4 acabou de
> desqualificar como métrica de negócio. Ele **não** prova que `pmaxon26br` é ineficiente em vendas.
> O que ele prova é que **as duas campanhas não estão medindo a mesma coisa**, e isso é achado de
> medição, não de mídia. A leitura correta é: o sinal de conversão da jornada `on` está quebrado ou
> ausente, e a campanha está sendo otimizada no escuro.

### 5.2 🟠 A conta B2B compra a marca do próprio grupo

Em `conta-1/overview/search-keywords.csv`, entre os termos com maior gasto:
`pro` R$ 60.372,75 · `canal` R$ 55.032,42 · `zap` R$ 29.925,92 · `olx` R$ 20.588,20 ·
`grupo` R$ 16.407,38 · `viva real` R$ 7.014,72.

E há gasto acumulado em critério com status **Removed** dentro de campanha ativa: `zap +` em
correspondência de frase, R$ 50.188,95, e `Grupo OLX`, R$ 16.603,04.

---

## 6. A conta B2C principal compra 95,8% sem controle de termo

`conta-4-vivareal-brasil`, R$ 63,33 mi acumulados:

| Tipo | Investimento | % |
|---|---:|---:|
| Search | R$ 43.506.661,69 | 68,7% |
| Performance Max | R$ 19.798.028,40 | 31,3% |
| Demand Gen | R$ 23.934,78 | 0,04% |
| Display | R$ 2.105,94 | 0,003% |

Dentro de Search, as campanhas **DSA** (segmentação dinâmica, sem palavra-chave) somam
R$ 40.895.366,79. **DSA mais Performance Max dão R$ 60.693.395,19, ou 95,8% do gasto da conta.**

Não é erro: é uma escolha de arquitetura legítima. Vira achado por causa da seção 4, porque **os dois
formatos que menos dão controle humano são exatamente os que mais dependem da qualidade do sinal de
conversão**, e o sinal está comprovadamente quebrado.

> **Contaminação B2B dentro da conta-4: 0,033% do gasto.** As contas estão de fato separadas, o que é
> um contraponto favorável e precisa ser dito.

---

## 7. 🔴 O Meta chega ao projeto sem um único desfecho

| Meta, via V4MOS, 01/01/2025 a 14/09/2026 | |
|---|---:|
| Investimento | R$ 7.375.303,34 |
| Campanhas | 90 |
| Impressões | 1.884.960.898 |
| Cliques | 29.407.990 |
| **Campos de conversão, lead ou receita** | **nenhum** |

Os registros de campanha do Meta têm oito campos: `name`, `objective`, `spend`, `impressions`,
`clicks`, `reach`, `cpm`, `ctr`. **Não existe numerador.** R$ 7,38 milhões entram no projeto sem um
lead atribuído, e 42,2% desse investimento está em campanhas cujo objetivo declarado é conversão
(`OUTCOME_LEADS`, `LEAD_GENERATION`).

**Não há export direto de Meta no repositório.** Nenhum achado desta seção tem segunda fonte, e isso
é lacuna de material, não de análise.

### 7.1 R$ 2,19 milhões de Meta em Localiza e Unidas, e nenhum documento do projeto menciona isso

| Campanha | Objetivo | Investimento |
|---|---|---:|
| `folocalizanewpplbr_mt_ct_bo_fm_ao_cr_at_ol_pf` | OUTCOME_LEADS | R$ 667.499,59 |
| `founidaspplbr_mt_ct_bo_fm_ao_cr_at_ol_pf` | LEAD_GENERATION | R$ 602.718,63 |
| `folocalizapplbr_mt_ct_bo_fm_ao_cr_at_ol_pf` | OUTCOME_LEADS | R$ 485.122,23 |
| `founidasnewpplbr_mt_ct_bo_fm_ao_cr_at_ol_pf` | OUTCOME_LEADS | R$ 437.332,12 |
| `founidasnewautospplbr_mt_ct_bo_fm_ao_cr_at_ol_pf` | OUTCOME_LEADS | R$ 105,84 |
| **Total** | | **R$ 2.192.778,41** |

São **29,7% de todo o investimento de Meta**, em campanhas nomeadas por duas locadoras de veículos,
com objetivo de geração de lead e token de marca `ol` (OLX). Se isto for captação de frota para OLX
Autos, é **mídia B2B que ninguém no projeto contabilizou**. Se for parceria comercial, é receita de
mídia, não custo de aquisição. **As duas leituras mudam o diagnóstico, e nenhuma pode ser afirmada
com o material atual.**

### 7.2 🟠 A camada de anúncio do V4MOS não reconcilia, e a causa está num script deste repositório

| Métrica | Camada de campanha | Camada de anúncio | Divergência |
|---|---:|---:|---:|
| Cliques | 29.407.990 | 54.559.083 | **+85,5%** |
| Impressões | 1.884.960.898 | 1.321.526.150 | -29,9% |
| Investimento | R$ 7.375.303,34 | R$ 6.744.117 | -8,6% |

Em [`.claude/scripts/v4mos_fetch.sh`](../.claude/scripts/v4mos_fetch.sh), o laço que agrega campanhas
aplica o recorte de data (`if dt and not in_range(dt): continue`). **O laço que agrega anúncios não
tem essa linha.** A assimetria é real e foi corrigida.

> Ela **não explica sozinha** a divergência: filtrar por data reduziria os cliques, mas as impressões
> e o investimento da camada de anúncio já são **menores** que os da camada de campanha. Há pelo menos
> uma segunda causa, no endpoint ou na população retornada. Até isso ser reconciliado, **os 1.079
> anúncios e 1.079 criativos do V4MOS não sustentam nenhuma afirmação**, inclusive as de diversidade e
> fadiga criativa.

---

## 8. A reconciliação com o funil: o CAC é faixa, não ponto

Os [dashboards de aquisição](dashboards-aquisicao-pro.md) declaram, para mídia paga B2B offline entre
01/09/2025 e 15/09/2026, **R$ 951,5 mil** de investimento e 645 vendas, dando CAC de R$ 1.475.

**O gasto real de uma única conta de Google, na mesma janela, é maior que isso:**

| Método | Gasto da `conta-1` | CAC sobre 645 vendas |
|---|---:|---:|
| Piso · 4T/25 a 3T/26 fechados, exclui set/2025 | R$ 997.016,56 | R$ 1.545,76 |
| Ponto médio · mais set/2025 estimado a 1/3 do 3T/25 `[E]` | R$ 1.038.874,10 | R$ 1.610,66 |
| Teto · mais o 3T/2025 inteiro | R$ 1.122.589,17 | R$ 1.740,45 |
| *Dashboard, toda a mídia B2B (piso declarado)* | *R$ 951.500,00* | *R$ 1.475,19* |

**Mesmo no piso, uma conta de Google gasta 4,8% mais do que o dashboard atribui a toda a mídia paga
B2B**, Meta incluído. E o próprio documento do dashboard já se declarava piso: *"a página online
equivalente devolve investimento em branco"* e *"as campanhas do Meta não aparecem com custo aqui"*.

> **Correção de um erro do próprio levantamento.** Quatro das oito frentes trataram o mix "70,2%
> Google · 24,7% Meta" como partição dos R$ 951,5 mil e produziram R$ 667.953 como "o Google
> declarado", derivando disso um CAC de R$ 1.985,37. **Esse número foi descartado.** O mix soma 94,9%,
> aparece separado no dashboard sob o rótulo "Complementos", e a fonte nega que o custo de Meta esteja
> ali. Não há partição a fazer.

### 8.1 O CAC dobrou, e 85% disso é taxa, não preço

Reconstruindo o período anterior a partir das variações publicadas no dashboard:

| Etapa | Anterior `[E]` | Atual | Variação |
|---|---:|---:|---:|
| Investimento | R$ 451.162 | R$ 951.500 | +110,9% |
| Impressões | 17.822.998 | 32.170.511 | +80,5% |
| Cliques | 397.232 | 738.057 | +85,8% |
| Sessões | 510.017 | 803.276 | +57,5% |
| MQL | 15.450 | 16.532 | +7,0% |
| SQL | 3.607 | 3.427 | -5,0% |
| **Venda** | **733** | **645** | **-12,0%** |

E as taxas de passagem:

| Passo | Antes | Agora | Variação |
|---|---:|---:|---:|
| Impressão → clique | 2,23% | 2,29% | +2,9% |
| Clique → sessão | 128,4% | 108,8% | -15,2% |
| **Sessão → MQL** | **3,03%** | **2,06%** | **-32,1%** |
| MQL → SQL | 23,35% | 20,73% | -11,2% |
| SQL → venda | 20,32% | 18,82% | -7,4% |

| Custo unitário | Antes | Agora | Variação |
|---|---:|---:|---:|
| CPM | R$ 25,31 | R$ 29,58 | +16,8% |
| CPC | R$ 1,14 | R$ 1,29 | +13,5% |
| Custo por MQL | R$ 29,20 | R$ 57,56 | +97,1% |
| Custo por SQL | R$ 125,07 | R$ 277,65 | +122,0% |
| **CAC** | **R$ 615,54** | **R$ 1.475,19** | **+139,7%** |

**A mídia comprou exposição bem e o sistema quebrou depois do clique.** O CPM subiu 16,8%, o que é
inflação normal de leilão, e o CTR ficou estável. A maior perda isolada está em **sessão → MQL, que
caiu 32,1%**. Vendas por milhão de impressão caíram de 41,1 para 20,0.

> Isto **converge** com o achado central dos [dashboards de aquisição](dashboards-aquisicao-pro.md):
> a perda está depois do MQL, não antes dele. Aqui ela aparece um passo acima, entre a sessão e o MQL.
> Duas fontes independentes, mesma direção.

---

## O que isso muda nas travas

| Trava | O que este diagnóstico acrescenta |
|---|---|
| **Cegueira** | É a trava que mais muda. A medição de mídia do projeto cobria 15,7% do Google e era uma conta só; a coluna de conversão da plataforma não conta negócio; o Meta chega sem desfecho; e a camada de anúncio do nosso próprio conector não reconcilia. **Nenhum número de eficiência de mídia no projeto era confiável antes de 16/09.** |
| **Exposição** | Existe, pela primeira vez, investimento B2B isolado: R$ 2,46 mi acumulados, R$ 997 mil a R$ 1,12 mi nos últimos 12,5 meses. Mas **não há parcela de impressões em nenhuma conta**, nem perdida por orçamento nem por classificação, e sem isso não se sabe quanta demanda B2B fica na mesa. |
| **Atenção** | **Dez unidades criativas no ar** em toda a aquisição paga B2B. Não há rotação, variação nem teste possível nessa superfície. |
| **Qualificação** | O passo que mais caiu é **sessão → MQL, -32,1%**, com a compra de exposição funcionando. Isto é candidato forte, e não pode ser confirmado com o material atual porque nada liga venda a campanha. |
| **Conversão / Retenção** | Nada a acrescentar: o material de mídia não alcança essas etapas. |

---

## 🔴 O que NÃO pode ir ao Comitê 1

Lista produzida pelo crítico de completude e mantida na íntegra, porque cada item é um jeito
específico de o material enganar o cliente.

1. **CAC de mídia B2B como número único.** Nem R$ 1.475, nem R$ 1.985. Vai como **faixa de R$ 1.476 a
   R$ 1.740**, com o método de cada extremo impresso.
2. **Qualquer ROAS ou valor de conversão de Google Ads.** R$ 5,51 trilhões no parque, R$ 297 bilhões
   numa conta de R$ 1,28 mi. Nem como ordem de grandeza.
3. **Qualquer contagem de conversão do Google tratada como lead ou venda**, enquanto ninguém nomear o
   evento contado.
4. **A frase "o Meta pesa 2,7 vezes o Google"**, hoje escrita em sete arquivos. Corrigida abaixo.
5. **Qualquer número de desfecho do Meta.** Não existe nenhum.
6. **Os 1,41 bilhão de alcance e a frequência derivada dele.** É soma de alcances por campanha, não
   alcance de pessoas.
7. **As séries mensais de impressão como gráfico de exposição.** A da `conta-3` é comprovadamente só
   Search (soma 24.233.492 contra 24.233.587 da linha `Total: Search`), as outras duas não têm recorte
   identificável, e cinco variantes se perderam ([pendência 41](../PENDENCIAS.md)).
8. **O mix "70,2% Google · 24,7% Meta" como partição do investimento B2B.** Soma 94,9% e a fonte nega.
9. **As cartas de demografia**, enquanto a soma dos percentuais passar de 100%, o que acontece em
   todas as dez.
10. **"A conta-1 é a conta B2B" como fato.** É inferência por domínio de destino e nome de campanha,
    forte mas inferência, e o `customer ID` segue desconhecido ([pendência 41](../PENDENCIAS.md)).
11. **A pendência 12 como "resolvida".** O que se provou é que `_pf` não significa pessoa física. O
    que sobra é pendência nova sobre a convenção inteira.

---

## O que este diagnóstico não viu

1. **O Meta, de verdade.** Sem export direto, sem campo de conversão, sem URL de destino.
2. **Parcela de impressões**, em nenhuma conta. Para uma trava de Exposição, é o dado central.
3. **Geografia.** Nenhum relatório de localização foi exportado em nenhuma das 5 contas.
4. **A ponte entre mídia e venda.** Nada liga as 645 vendas do CRM a campanha, grupo ou palavra. O
   diagnóstico tem custo de um lado e desfecho do outro.
5. **As ações de conversão.** Não há relatório delas no material, e é o que destrancaria a seção 4.
6. **Por que `pmaxoffbr` foi pausada.** É a maior campanha B2B da história da conta, R$ 757.950,36 e
   58.548,52 conversões a R$ 12,95, e está fora do ar enquanto `pmaxon26br` gasta R$ 22.179,98 por
   uma conversão.

---

## Como este diagnóstico fecha

Ele **não fecha** com o material atual. O que está escrito aqui é a camada de plataforma, e ela é
suficiente para a leitura de trava do Comitê 1. Para fechar faltam, em ordem de impacto:

| # | O que | Por quê | Dono |
|---|---|---|---|
| 1 | Relatório de **ações de conversão** das 5 contas | Sem ele nenhum CPA da plataforma é utilizável | Time de mídia |
| 2 | **Export direto do Meta**, com conversões e URL de destino | Hoje R$ 7,38 mi chegam sem desfecho | Time de mídia |
| 3 | **Parcela de impressões** de busca, perdida por orçamento e por classificação | É o dado central da trava de Exposição | Time de mídia |
| 4 | `customer ID` das 5 contas | Fecha a inferência de identidade e a pendência 12 | Time de mídia |
| 5 | O que são as campanhas **Localiza e Unidas** | R$ 2,19 mi que podem ser B2B não contabilizado | Mirella Mendonça |
| 6 | Relatório de **localização** | Produto vendido a imobiliária não tem número por estado | Time de mídia |
