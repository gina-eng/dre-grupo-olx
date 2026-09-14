# Estrutura Comercial Inside Sales · leitura

> **Fonte:** `assets/originais/A-visao-de-negocio-e-fluxo-de-receita/estrutura-comercial-inside-sales.pdf`
> SHA-256 `3fef1001...ae515` · apresentação do Grupo OLX, **28/08/2026** · par de máquina em
> [`dados/outputs/estrutura-comercial-inside-sales.json`](../dados/outputs/estrutura-comercial-inside-sales.json)
>
> ⚠️ **Entregue pelo cliente, não auditada pela V4.** Todo número aqui é `[D]`.

O documento chegou no **mesmo dia** que a série de receita A1 e ficou parado fora do repositório até
14/09. Ele fecha, sozinho, os dois itens que bloqueavam a matemática do forecast.

## O que ele destrava

| Item do checklist | Antes | Agora |
|---|---|---|
| **A2** · funil comercial com volumes e taxas | ⚪ | 🟡 quatro meses, só Inside Sales |
| **A3** · ticket médio, ciclo de venda, CAC por canal | ⚪ | 🟡 ticket e ciclo sim, CAC não |
| A4 · estrutura organizacional | ⚪ | 🟡 101 HCs por célula e papel |
| A5 · metas | ⚪ | 🟡 mapa de OKRs com % de atingimento |
| A6 · ICP e segmentação | ⚪ | 🟡 portes PP, P, M, G com faixa declarada |

E versiona o **slide FLUXOS**, que a [pendência 20](../PENDENCIAS.md) registrava como inexistente no
repositório. O mix de canais `CRM 29 · Direto 36 · Pago 16 · Orgânico 5 · Outros 11` agora tem origem
conferível.

## A operação

| | Real Estate | Autos |
|---|---:|---:|
| Clientes | 16.724 | 6.792 |
| Receita mensal | R$ 19,65 mi | R$ 5,80 mi |
| ARPU da carteira | R$ 1.175 | R$ 858 |
| Headcount | 74 | 27 |
| Células | 1 hunter + 5 farmer | 1 hunter + 5 farmer |

**Conferência interna:** em Real Estate a soma das seis células fecha **exata** nos clientes (16.724) e
erra 0,1% na receita, que é arredondamento. Em **Autos sobra 2,1%**: as células somam 6.938 contra
6.792 declarados, e a receita sobra 4,6%. Não invalida nada, mas precisa de explicação.

## Regra 8 · o funil contra a receita declarada

| | Inside Sales | Vertical inteira (run-rate A1) | Cobertura |
|---|---:|---:|---:|
| Real Estate | R$ 19,65 mi/mês | R$ 50,01 mi/mês | **39,3%** |
| Autos | R$ 5,80 mi/mês | R$ 34,42 mi/mês | **16,9%** |

Sobre `Classifieds - B&A`, o núcleo de assinatura, o Inside Sales de RE cobre **45,9%**.

**A leitura:** Inside Sales é menos da metade da receita B2B, e em Autos é um sexto. O resto vive em
key account, enterprise e canais que este documento não cobre. Qualquer meta construída só sobre este
funil estará falando de 39% do problema em Imóveis e de 17% em Autos.

## O funil B2B, abril a julho de 2026

Soma de RE e Autos, hunter mais farmer:

| Mês | Leads B2B | Vendas B2B | Conversão |
|---|---:|---:|---:|
| abr/26 | 4.283 | 968 | 22,6% |
| mai/26 | 5.056 | 1.344 | 26,6% |
| jun/26 | 4.109 | 1.177 | 28,6% |
| **jul/26** | **3.132** | **720** | **23,0%** |

## 🔴 O mergulho de julho

| | Leads | Abordagem | Vendas |
|---|---|---|---|
| RE hunter | 1.723 → 1.018 · **-40,9%** | 97% → 84% | 431 → 266 · **-38,3%** |
| RE farmer | 1.194 → 579 · **-51,5%** | 90% → **59%** | 360 → 140 · **-61,1%** |
| Autos hunter | 630 → 1.098 · **+74,3%** | 100% → **58%** | 232 → 213 · -8,2% |
| Autos farmer | 562 → 437 · -22,2% | 99% → 99% | 154 → 101 · -34,4% |

**Duas hipóteses, e elas levam a decisões opostas.**

**(a) Julho está incompleto** no dashboard, e o que se vê é safra ainda fechando. Nesse caso não há
achado, e o número certo chega depois.

**(b) Julho é uma quebra real.** Dois indícios pesam a favor:

1. A [auditoria (i) de CRM](auditoria-i-crm-marketing.md) achou que a migração para o **Campana**
   desligou as jornadas de ciclo de vida de todo cliente novo, **Imóveis desde julho**. É exatamente
   a vertical e exatamente o mês em que o funil de RE desaba.
2. **Autos hunter recebeu 74% mais lead em julho e a abordagem caiu de 100% para 58%.** Mês incompleto
   derruba volume, não faz o volume subir. Isso é capacidade de atendimento estourando, não safra
   aberta.

**Como resolver:** pedir a visão fechada de julho e agosto. Se julho fechado continuar nesse patamar,
a hipótese (b) está confirmada e a trava governante muda de conversa.

## O ticket de entrada, que estava `null`

| | ARPU hunter (entrada) | ARPU da carteira | Entrada sobre carteira |
|---|---:|---:|---:|
| Real Estate | R$ 707 | R$ 1.175 | 60% |
| Autos | R$ 602 | R$ 858 | 70% |

O cliente entra pagando 60% do que a carteira paga em média, e a diferença é **expansão dentro da
base**. Isso tem consequência direta no forecast: um modelo que projete `N × ticket de entrada`
subestima a receita de regime em 40% em Imóveis, e o modelo de coorte precisa da curva de expansão,
não de um ticket fixo.

## O que continua faltando

1. **Série mensal longa.** Quatro meses não sustentam tendência. O forecast precisa de 12 a 24.
2. **Churn e base mês a mês.** Há foto da carteira, não movimento. Sem entrada e saída por mês, não há
   coorte, e a ambiguidade entre churn de logo e de receita ([pendência 22](../PENDENCIAS.md)) continua.
3. **CAC.** Nenhum custo de aquisição, e a mídia medida não separa B2B de B2C.
4. **O resto da receita B2B.** 61% em Imóveis e 83% em Autos estão fora deste funil.
5. **Margem.** Continua sem P&L por vertical.

## Perguntas para a OLX

1. Julho fechou? Se sim, o patamar se confirma?
2. Por que Autos soma 6.938 clientes nas células e declara 6.792?
3. A célula GOODS, dentro de Autos, é Goods & Services? Se for, ela não pertence à vertical Autos na
   série A1, e a comparação de cobertura muda.
4. As duas planilhas-fonte citadas no PDF podem ser compartilhadas? Elas têm a série longa.
5. Os números da página 24, `MQL 1.200 → SQL 540 → Vendas 180`, são de quando e de qual vertical? Eles
   não batem com as tabelas das páginas 5 e 6, e parecem ilustrativos.
