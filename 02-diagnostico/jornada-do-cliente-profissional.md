# Jornada do cliente profissional — o mapa que a OLX apresentou

> **Status: conceito declarado pelo cliente, não verificado.** Os seis percentuais desta página
> vieram de uma apresentação do Grupo OLX, não do sistema. Nenhum deles é dado ainda: valem como
> **hipótese com origem nomeada** até baterem contra CRM, faturamento e plataformas. Regra 1 do
> repositório. Enquanto isso, todo número daqui é citado com a marca `[D]` — *declarado*.

| | |
|---|---|
| **Origem** | Apresentado pelo Grupo OLX na sessão de jornada do cliente, [28/08/2026](../06-reunioes/2026-08-28-jornada-do-cliente.md) |
| **Original** | [`assets/originais/A-visao-de-negocio-e-fluxo-de-receita/jornada-do-cliente-profissional.png`](../assets/originais/A-visao-de-negocio-e-fluxo-de-receita/jornada-do-cliente-profissional.png) |
| **Escopo declarado** | *"Etapas que lojistas de automóveis, corretores e imobiliárias enfrentam na aquisição e utilização dos produtos OLX"* — B2B, Autos e Imóveis |
| **Cobre** | Bloco **A2** do [checklist](checklist-dados-e-acessos.md) *parcialmente*: dá as etapas e seis taxas, não dá volumes nem série temporal |
| **Alimenta** | `mapeamento-fluxo-receita.md` (camada conceitual) e o POP Fluxo de Receita |
| **Transcrição da sessão** | 🔜 a receber |

---

## As seis etapas, como eles as nomeiam

| # | Etapa | O que acontece | Número declarado `[D]` |
|---|---|---|---|
| 1 | **Entrada** | Prospecção comercial · campanhas e réguas de marketing · contato espontâneo | **50%** da receita nasce da prospecção comercial |
| 2 | **Contratação** | Canal online (só planos de anúncios) · Time Comercial Inside/Field Sales (todos os produtos, mais up, down e cancelamento) | **25%** da receita vem do canal online em Autos, **10%** em Imóveis |
| 3 | **Pagamento** | Imóveis: só pré-pago · Autos: pré e pós-pago · PayPerLeads para locadoras e incorporadoras | **80%** dos que fecham contrato pagam a primeira fatura |
| 4 | **Publicação dos anúncios** | Em lote via integrador ou unitário pelo CanalPro/MyPlan · Autos: modelo de inserção · Imóveis: modelo de slot | **12%** dos clientes que saem no primeiro mês vão embora **sem publicar** |
| 5 | **Recebimento de leads** | Leads do próprio anúncio · de anúncios similares · de outros canais (PayPerLeads) | **89%** dos anúncios de Imóveis **não recebem nenhum lead** |
| 6 | **Recorrência ou churn** | Planos mensais, trimestrais ou anuais · pré-pago: basta não pagar para interromper ("boleto facilita esquecimento") · pós-pago: alta taxa de abono e contestação | **8–10%** de churn mensal, **baixa performance é o principal motivo** |

## O que este mapa entrega ao diagnóstico

**Ele é o primeiro fluxo com taxa em cada estação.** Até 28/08 a V4 tinha as etapas por narrativa e
nenhum denominador. Agora há seis pontos de vazamento nomeados pelo próprio cliente — o que muda a
sessão de mapeamento de "descrever" para "conferir".

**Ele confirma, com número, a UDE #2.** No kick-off ficou registrado que o anunciante compra posição
e não recebe garantia de lead, podendo receber zero: *"não tem garantias de performance… ele pode
receber zero ou 100 leads"* (Leonardo Costa, 01:35:23). Os **89%** dizem que zero **é o caso
comum**, não o extremo. Isso deixa de ser risco contratual e passa a ser a descrição do produto
entregue na média.

**Ele corrige para pior uma previsão feita na sala.** Dener estimou de improviso a perda entre
compra e pagamento: *"não tem 15% que compra e não paga?"*. O mapa diz **20%** — um em cada cinco
contratos fechados nunca vira caixa. Trava de **Decisão**, com tamanho.

**Ele dá a primeira leitura de retenção com régua.** 8–10% ao mês, composto sobre doze meses,
implica perder entre **63% e 72% da base por ano** se a taxa for sobre número de clientes e se
mantiver constante — *derivação da V4, não número do cliente*. Confirmadas as duas premissas, isso
explica sozinho o net negativo em Imóveis que Iuna e Florence relataram (UDE #1).

## A cadeia que os números desenham

Lida de trás para frente, na ordem do método (do truput para o topo), a apresentação encadeia
quatro etapas numa única história:

> **89%** dos anúncios de Imóveis não recebem lead → o cliente percebe baixa performance →
> **baixa performance é o principal motivo de churn** → **8–10%** ao mês → as entradas não
> compensam churn mais downgrade → **net de receita negativo em Imóveis**.

E, antes disso, dois vazamentos independentes na entrada do sistema: **20%** que contratam e não
pagam, e **12%** que saem no primeiro mês sem sequer publicar — ou seja, sem nunca terem tido a
chance de receber lead nenhum.

Isso posiciona a hipótese na **Trava de Retenção**, com causa a montante em **Decisão** e no que o
produto entrega. Note que é exatamente onde o cliente já apontava: Retenção 3 votos, Qualificação 2
([conferência do kick-off](../06-reunioes/2026-08-24-kickoff-o-que-a-transcricao-fecha.md), §2.7).

> ⚠️ **Isso não é a restrição.** É uma hipótese com três fontes convergindo — percepção do cliente,
> UDEs e agora taxas declaradas. Vira diagnóstico quando o dado do sistema confirmar e o impulso
> controlado responder. Regra 3 do repositório: uma restrição por vez, e ela se prova.

## As sete perguntas que este mapa abre

Cada uma muda a leitura acima se for respondida de um jeito ou de outro.

| # | Ambiguidade | Por que muda tudo |
|---|---|---|
| 1 | **89% é sobre anúncio ou sobre cliente?** | Um cliente com 50 anúncios e 3 com lead não está sem lead. A distribuição por cliente é outro número, e é o que importa para churn |
| 2 | O que explica a concentração dos leads nos 11%? | Faixa de preço, praça, ranking, qualidade da foto ou **deduplicação** — a OLX declarou 193 mil anúncios sincados contra ~1,5 milhão duplicados. Se for dedup, é problema de produto, não de demanda |
| 3 | **12%** é dos que saem no primeiro mês, ou dos clientes totais? | A frase do slide comporta as duas leituras. A diferença é de uma ordem de grandeza no tamanho do vazamento |
| 4 | **8–10%** é churn de logo ou de receita? | Iuna disse que a OLX lê o net em receita. Se a taxa for de logo, o impacto financeiro ainda não está medido |
| 5 | **50% prospecção + 25%/10% online**: e o resto? | Falta a fatia de Inside/Field Sales e de renovação. Sem os 100% fechados não dá para reconciliar com o faturamento (regra 8) |
| 6 | Os **20%** que não pagam são recuperados depois? | Se há recuperação ativa, o vazamento líquido é menor. Se não há, é dinheiro contratado e abandonado |
| 7 | "Alta taxa de abono e contestação" no pós-pago: **quanto**? | É o único item do slide sem número, e fica na etapa onde a receita já foi reconhecida |

Nenhuma delas é pergunta de opinião — todas se respondem com consulta ao sistema, e cinco delas
com os acessos já pedidos.

## Como usar este documento

1. **Não citar percentual daqui em material de cliente sem a marca `[D]`.** São números de
   apresentação, não de apuração. O primeiro que cair na verificação derruba a credibilidade dos
   outros cinco.
2. As sete perguntas viram linha de [PENDENCIAS.md](../PENDENCIAS.md) com DRI e prazo assim que a
   transcrição da sessão chegar e disser quem se comprometeu com o quê.
3. As etapas 1 a 6 entram como a camada conceitual do `mapeamento-fluxo-receita.md`. Os volumes
   absolutos continuam faltando — é o bloco **A2** do checklist, e sem ele o Forecast não roda.
4. A árvore de produção de receita do portal (`/receita`) precisa absorver este mapa: as seis etapas
   confirmam nós hoje em hipótese, em especial os de 3B-11 (caminho do dinheiro) e 3B-1 (o que o
   cliente compra).
