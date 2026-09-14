# Carga tributária e o teto da margem de contribuição

> **Par de máquina:** [`dados/outputs/carga-tributaria.json`](../dados/outputs/carga-tributaria.json)
> **Natureza:** estimativa da V4 sobre fonte pública e legislação vigente. **Não é a apuração fiscal
> do Grupo OLX.** O número definitivo está no P&L por vertical, item 4 do
> [mapa de números](mapa-de-numeros.md), com DRI Matheus Rodrigues e prazo vencido em 09/09.

No kick-off o cliente declarou **margem bruta perto de 100%**, apontando **mídia e imposto como os
dois únicos ofensores**. A mídia já está medida: R$ 10,12 mi em 21 meses. O imposto nunca foi
quantificado. Esta nota quantifica.

## A entidade

| | |
|---|---|
| CNPJ | 13.673.743/0004-17 · **é filial**, a matriz é `...0001-XX` |
| Razão social | BOM NEGOCIO ATIVIDADES DE INTERNET LTDA |
| Natureza jurídica | 206 · Sociedade Empresária Limitada |
| Município | **São Paulo, SP** · Av. Paulista, 1106, Bela Vista |
| Situação | Ativa desde 16/09/2014 |
| Capital social | R$ 2.222.010.000,00 |
| CNAE principal | 6319-4/00 · Portais e provedores de conteúdo na internet |

**Duas ressalvas de escopo.** Primeira: é **uma filial**, e o Grupo OLX opera vários CNPJs (OLX, ZAP,
VivaReal). A conta abaixo vale para a atividade, não para o grupo consolidado. Segunda: três CNAEs
secundários têm tratamento próprio e não seguem esta régua, `6462-0/00` holding, `6810-2/01` compra e
venda de imóveis próprios, e `6619-3/02` correspondente bancário.

## Regime

Receita do grupo em 2025: **R$ 1,156 bi**. Acima de R$ 78 mi por ano o **Lucro Real é obrigatório**, e
com ele o **PIS/COFINS não cumulativo**.

## O que sai da margem de contribuição

Margem de contribuição desconta **custo variável**. Imposto sobre receita é variável por definição.
Imposto sobre lucro não é, e entra depois.

| Tributo | Alíquota | Observação |
|---|---:|---|
| PIS | 1,65% | não cumulativo |
| COFINS | 7,60% | não cumulativo |
| **PIS/COFINS** | **9,25%** | permite crédito sobre insumo, energia, aluguel PJ e depreciação |
| ISS São Paulo · TI | 2,90% | Lei 13.701/2003 art. 16, alterada pela Lei 16.757/2017, que levou TI de 2% para 2,9% |
| ISS São Paulo · regra geral | **5,00%** | item 17.06, propaganda e publicidade, e demais serviços |

**Por que o crédito de PIS/COFINS não salva.** O regime dá crédito sobre insumo, energia, aluguel e
depreciação. **Folha de pagamento não gera crédito**, e num negócio digital a folha é o maior custo.
Há 101 pessoas só no Inside Sales. O efetivo fica perto do nominal.

**O que decide entre 2,9% e 5%** é como a NFS-e é codificada. Portal e inserção de publicidade cabem
em 2,9%; agenciamento e propaganda caem na regra geral. Como o pedido foi o pior cenário, a conta
abaixo usa **5%**.

## O pior cenário: 14,25% da receita

| Cenário | Alíquota | **Teto da margem de contribuição** |
|---|---:|---:|
| Piso, ISS de TI | 12,15% | 87,85% |
| **Pior caso, ISS cheio** | **14,25%** | **85,75%** |
| 2027, CBS + ISS | 14,43% | 85,57% |
| 2033, IBS + CBS pleno | **27,91%** | **72,09%** |

**Margem de contribuição de 100% é aritmeticamente impossível.** O teto é 85,75% no pior cenário de
hoje, e isso antes de qualquer outro custo variável.

## Quanto custa o erro

Aplicando 14,25% sobre o run-rate real de 2026:

| | Receita/mês | Imposto/mês | **Truput real/mês** | Erro ao ano |
|---|---:|---:|---:|---:|
| Grupo | R$ 103,78 mi | R$ 14,79 mi | **R$ 88,99 mi** | **R$ 177,5 mi** |
| `Classifieds - B&A` | R$ 42,78 mi | R$ 6,10 mi | **R$ 36,69 mi** | R$ 73,2 mi |
| Inside Sales (RE+Autos) | R$ 25,45 mi | R$ 3,63 mi | **R$ 21,82 mi** | R$ 43,5 mi |

**A régua do projeto muda.** O repositório vinha usando "1 p.p. de run-rate em `Classifieds - B&A`
vale R$ 428 mil por mês". Em truput, o mesmo ponto vale **R$ 367 mil**. A diferença, R$ 61 mil por
mês, é imposto.

## A reforma tributária cai dentro do contrato

O contrato vai de ago/2026 a ago/2027, e atravessa a virada.

| Ano | O que acontece |
|---|---|
| 2026 | Ano-teste. CBS 0,9% e IBS 0,1%, compensáveis. **Sem custo adicional** |
| **2027** | **PIS/COFINS extintos.** CBS cheia, estimada em **9,43%**. O Senado fixa até 31/10 |
| 2029–2032 | ISS transita para IBS |
| 2033 | Regime pleno. CGIBS estima **27,91%** para IBS+CBS somados |

Em 2027 a troca é quase neutra: CBS 9,43% contra PIS/COFINS 9,25%. **O risco está no fim da
transição**, onde a estimativa dobra a carga sobre receita. Um forecast de 12 meses não sente isso,
mas a matriz de expansão e qualquer conversa de LTV sentem.

## O que ainda falta

1. **P&L por vertical com imposto aberto.** Item 4 do mapa de números, vencido em 09/09.
2. **A codificação da NFS-e**, que decide entre 2,9% e 5%.
3. **O crédito efetivo de PIS/COFINS**, que só o razão contábil mostra.
4. **Os outros custos variáveis**, que não estão nesta conta: comissionamento do Inside Sales,
   inadimplência, meio de pagamento no checkout e infraestrutura que escala com uso. Cada um derruba
   mais o teto de 85,75%.

## Imposto sobre o lucro, para contexto

Não entra na margem de contribuição, mas fecha o quadro: **IRPJ 15%** mais adicional de 10% sobre o
que exceder R$ 240 mil por ano, o que leva o efetivo a ~25%, e **CSLL 9%**. Somados, **34% sobre o
lucro real**.

## A recomendação

Parar de usar 100%. Enquanto o P&L não chega, adotar **85% como premissa de trabalho**, marcada `[E]`,
e declarar a premissa em todo material que for a comitê. É conservador contra o pior cenário fiscal e
ainda otimista contra os custos variáveis que faltam mapear.
