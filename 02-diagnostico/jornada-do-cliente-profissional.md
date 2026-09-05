# Jornada do cliente profissional: o mapa que a OLX apresentou

> **Status: conceito declarado pelo cliente, não verificado.** Os seis percentuais desta página
> vieram de uma apresentação do Grupo OLX, não do sistema. Nenhum deles é dado ainda: valem como
> **hipótese com origem nomeada** até baterem contra CRM, faturamento e plataformas. Regra 1 do
> repositório. Enquanto isso, todo número daqui é citado com a marca `[D]`, *declarado*.

| | |
|---|---|
| **Origem** | Apresentado pelo Grupo OLX na sessão de jornada do cliente, [28/08/2026](../06-reunioes/2026-08-28-jornada-do-cliente.md) |
| **Original** | [`assets/originais/A-visao-de-negocio-e-fluxo-de-receita/jornada-do-cliente-profissional.png`](../assets/originais/A-visao-de-negocio-e-fluxo-de-receita/jornada-do-cliente-profissional.png) |
| **Escopo declarado** | *"Etapas que lojistas de automóveis, corretores e imobiliárias enfrentam na aquisição e utilização dos produtos OLX"*, B2B, Autos e Imóveis |
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
nenhum denominador. Agora há seis pontos de vazamento nomeados pelo próprio cliente, o que muda a
sessão de mapeamento de "descrever" para "conferir".

**Ele confirma, com número, a UDE #2.** No kick-off ficou registrado que o anunciante compra posição
e não recebe garantia de lead, podendo receber zero: *"não tem garantias de performance… ele pode
receber zero ou 100 leads"* (Leonardo Costa, 01:35:23). Os **89%** dizem que zero **é o caso
comum**, não o extremo. Isso deixa de ser risco contratual e passa a ser a descrição do produto
entregue na média.

**Ele corrige para pior uma previsão feita na sala.** Dener estimou de improviso a perda entre
compra e pagamento: *"não tem 15% que compra e não paga?"*. O mapa diz **20%**, um em cada cinco
contratos fechados nunca vira caixa. Trava de **Decisão**, com tamanho.

**Ele dá a primeira leitura de retenção com régua.** 8–10% ao mês, composto sobre doze meses,
implica perder entre **63% e 72% da base por ano** se a taxa for sobre número de clientes e se
mantiver constante, *derivação da V4, não número do cliente*. Confirmadas as duas premissas, isso
explica sozinho o net negativo em Imóveis que Iuna e Florence relataram (UDE #1).

## A cadeia que os números desenham

Lida de trás para frente, na ordem do método (do truput para o topo), a apresentação encadeia
quatro etapas numa única história:

> **89%** dos anúncios de Imóveis não recebem lead → o cliente percebe baixa performance →
> **baixa performance é o principal motivo de churn** → **8–10%** ao mês → as entradas não
> compensam churn mais downgrade → **net de receita negativo em Imóveis**.

E, antes disso, dois vazamentos independentes na entrada do sistema: **20%** que contratam e não
pagam, e **12%** que saem no primeiro mês sem sequer publicar, ou seja, sem nunca terem tido a
chance de receber lead nenhum.

Isso posiciona a hipótese na **Trava de Retenção**, com causa a montante em **Decisão** e no que o
produto entrega. Note que é exatamente onde o cliente já apontava: Retenção 3 votos, Qualificação 2
([conferência do kick-off](../06-reunioes/2026-08-24-kickoff-o-que-a-transcricao-fecha.md), §2.7).

> ⚠️ **Isso não é a restrição.** É uma hipótese com três fontes convergindo, percepção do cliente,
> UDEs e agora taxas declaradas. Vira diagnóstico quando o dado do sistema confirmar e o impulso
> controlado responder. Regra 3 do repositório: uma restrição por vez, e ela se prova.

## As sete perguntas que este mapa abre

Cada uma muda a leitura acima se for respondida de um jeito ou de outro.

| # | Ambiguidade | Por que muda tudo |
|---|---|---|
| 1 | **89% é sobre anúncio ou sobre cliente?** | Um cliente com 50 anúncios e 3 com lead não está sem lead. A distribuição por cliente é outro número, e é o que importa para churn |
| 2 | O que explica a concentração dos leads nos 11%? | Faixa de preço, praça, ranking, qualidade da foto ou **deduplicação**, a OLX declarou 193 mil anúncios sincados contra ~1,5 milhão duplicados. Se for dedup, é problema de produto, não de demanda |
| 3 | **12%** é dos que saem no primeiro mês, ou dos clientes totais? | A frase do slide comporta as duas leituras. A diferença é de uma ordem de grandeza no tamanho do vazamento |
| 4 | **8–10%** é churn de logo ou de receita? | Iuna disse que a OLX lê o net em receita. Se a taxa for de logo, o impacto financeiro ainda não está medido |
| 5 | **50% prospecção + 25%/10% online**: e o resto? | Falta a fatia de Inside/Field Sales e de renovação. Sem os 100% fechados não dá para reconciliar com o faturamento (regra 8) |
| 6 | Os **20%** que não pagam são recuperados depois? | Se há recuperação ativa, o vazamento líquido é menor. Se não há, é dinheiro contratado e abandonado |
| 7 | "Alta taxa de abono e contestação" no pós-pago: **quanto**? | É o único item do slide sem número, e fica na etapa onde a receita já foi reconhecida |

Nenhuma delas é pergunta de opinião, todas se respondem com consulta ao sistema, e cinco delas
com os acessos já pedidos.

## Atualização com a transcrição da sessão

A [transcrição de 28/08](../06-reunioes/2026-08-28-jornada-do-cliente-transcricao.md) responde
três das sete ambiguidades e **corrige duas leituras** do slide.

| # | Situação |
|---|---|
| 1 · 89% anúncio ou cliente | **Continua aberta**, e agora confirmada como sendo sobre **anúncio**: *"89% dos anúncios de imóveis não recebem nenhum lead"* (Carolina, 00:18:09). A distribuição por cliente segue sem medida |
| 2 · o que concentra os leads nos 11% | Aberta |
| 3 · a que se refere o 12% | **Respondida e decomposta**: é dos que saem no primeiro mês sem nunca ter publicado, e a média esconde as pontas, até **20%** no canal online contra **8–10%** em inside e field sales (Lu Machim e Leonardo Costa, 00:15:30). O vazamento é do autosserviço |
| 4 · churn de logo ou de receita | Aberta |
| 5 · o resto dos 50% + 25%/10% | **Respondida**: o restante é todo do time comercial, dividido entre inside sales e field sales, com field focado em cliente de maior valor (Carolina, 00:12:41) |
| 6 · os 20% que não pagam são recuperados | Aberta |
| 7 · quanto é a "alta taxa de abono e contestação" | Aberta |

### Duas correções ao slide

**O denominador dos 80% é mais estreito do que o slide sugere.** Não é "dos clientes que fecham
contrato": é dos que **fecharam contrato e geraram cobrança**. Carolina, 00:15:30: *"dos 100% que
fizeram a contratação e geraram um boleto ou qualquer coisa do tipo, desses 100%, 80 pagam"*.

**Esquecimento não é causa de churn na proporção que o slide sugere.** A caixa de churn traz
"boleto facilita esquecimento" ao lado dos 8–10%, mas a transcrição separa: o esquecimento responde
por **20% dos atrasos**, e o principal motivo de churn continua sendo **baixa performance**
(Carolina, 00:22:16).

### E uma definição que muda a leitura de retenção

Cliente que **paga e não usa não é churn**, é inativo gerando receita (Carolina e Leonardo Rosa,
00:22:16). Os 8–10% medem, portanto, **interrupção de pagamento**, não abandono de uso. A
insatisfação silenciosa de quem paga sem publicar não aparece em lugar nenhum dessa métrica, e é
justamente o perfil que os 89% sem lead produzem.

---

## Como usar este documento

1. **Não citar percentual daqui em material de cliente sem a marca `[D]`.** São números de
   apresentação, não de apuração. O primeiro que cair na verificação derruba a credibilidade dos
   outros cinco.
2. As sete perguntas viram linha de [PENDENCIAS.md](../PENDENCIAS.md) com DRI e prazo assim que a
   transcrição da sessão chegar e disser quem se comprometeu com o quê.
3. As etapas 1 a 6 entram como a camada conceitual do `mapeamento-fluxo-receita.md`. Os volumes
   absolutos continuam faltando, é o bloco **A2** do checklist, e sem ele o Forecast não roda.
4. A árvore de produção de receita do portal (`/receita`) precisa absorver este mapa: as seis etapas
   confirmam nós hoje em hipótese, em especial os de 3B-11 (caminho do dinheiro) e 3B-1 (o que o
   cliente compra).
