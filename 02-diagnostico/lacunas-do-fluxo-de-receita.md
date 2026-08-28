# Lacunas do fluxo de receita — caderno vivo

Caderno de campo do mapeamento. **Cresce a cada material que a OLX apresenta** e só fecha quando o
`mapeamento-fluxo-receita.md` tiver volume, taxa e tempo em cada etapa.

Duas listas: **L** = o que falta ou está errado no fluxo · **F** = o que entra ou muda no
[formulário de kick-off](../portal/assets/form-data.js) (96 perguntas, blocos 01 a 10).

| Origem | Material | Registro |
|---|---|---|
| 28/08 manhã | Jornada do cliente profissional, 6 etapas | [jornada-do-cliente-profissional.md](jornada-do-cliente-profissional.md) — traz 7 ambiguidades próprias, não repetidas aqui |
| 28/08 | **FLUXOS: Autos & Imóveis**, diagrama de canais e dois fluxos | esta página · ⚠️ **arquivo-fonte ainda não versionado** |

> ⚠️ O slide de FLUXOS entrou por imagem colada, não por arquivo. Os percentuais abaixo foram
> **lidos da tela** e precisam de conferência contra o original — ver **L7**. Assim que o PNG ou o
> deck chegar, ele vai para `assets/originais/A-visao-de-negocio-e-fluxo-de-receita/`.

---

## O que o slide de FLUXOS mostra

Um diagrama de canais que desagua em **duas máquinas paralelas** terminando na mesma caixa:

```
Canais de Marketing            Usuário gera tráfego            Fluxo Offline · Lead B2B
CRM · Direto · Pago      →     LPs MKT           →     WhatsApp/Telefone/Outros/Formulário
Orgânico · Outros              Portais / POS                   → MQL → SQL ─┐
                                     │                                      ├→ Venda ($)
Incentivos área logada  ─ ─ ─ ─ ─ ─ ─┘              Fluxo Online            │
(Canal Pro · My Plan)                        Login/Cadastro → Vitrine → Check-out
                                                    (apenas ZAP/VR)
```

Rótulos legíveis: CRM 2% · Direto 10% · Pago 16% · Orgânico 5% · Outros 11% · uma seta de 1% ·
incentivos na área logada 10% (tracejado verde) e 3% (tracejado cinza, direto ao Formulário).
Legenda separa **Impulsionado** de **Não impulsionado**. Rodapé:
*"% Representatividade Total dos MQL do Fluxo Offline - Leads B2B de todo o período histórico."*

Valor real deste material: é o **primeiro desenho da arquitetura de canais** e a primeira vez que
o online e o offline aparecem como esteiras distintas. É estrutura, não medição.

---

## L · Fluxo de receita: corrigir ou preencher

| # | O que falta ou está errado | Por que importa | Status |
|---|---|---|---|
| **L1** | **A prospecção comercial não está no desenho.** Os canais de entrada do fluxo offline são todos de chegada (WhatsApp, Telefone, Outros, Formulário). A jornada da manhã diz que **50% da receita nasce da prospecção comercial** | Metade da receita não tem caminho desenhado. Isso é **achado, não lacuna**: o mapa que a casa usa para pensar aquisição omite a maior origem dela. Confirmar se "Telefone" é também saída ativa | 🔴 aberto |
| **L2** | **O fluxo termina em "Venda ($)".** Não há publicação, entrega de lead, renovação ou churn | A jornada da manhã segue até recorrência, e a hipótese de trava é **Retenção**. O mapa não cobre a etapa onde a trava provavelmente está | 🔴 aberto |
| **L3** | **Autos e Imóveis num diagrama só** | Passo 1 do POP: segmentar antes de somar. A própria jornada dá números diferentes por vertical — canal online 25% em Autos contra 10% em Imóveis. Pedir o fluxo separado | 🔴 aberto |
| **L4** | **Os percentuais não são taxa de conversão.** O rodapé diz representatividade de MQL do fluxo offline | Não são taxas de passagem e não somam receita. Além disso o mix **não fecha**: os rótulos legíveis somam ~58% | 🔴 aberto |
| **L5** | **Janela = "todo o período histórico"** | Mistura antes e depois do aumento de preço de 2026 e apaga sazonalidade. O POP pede **12 meses com corte mensal** | 🔴 aberto |
| **L6** | **Nenhuma seta tem taxa nem volume.** Formulário→MQL, MQL→SQL, SQL→Venda, Login→Vitrine→Check-out→Venda | Sem volume e taxa não há **perda absoluta**, e é a perda absoluta que ordena as travas (Passo 4 do POP). É a lacuna mais cara da lista | 🔴 aberto |
| **L7** | **Atribuição dos percentuais aos canais está ambígua na imagem**: cinco barras, seis rótulos | Antes de citar qualquer um desses números é preciso o arquivo-fonte. Nenhum deles entra em material de cliente até lá | 🔴 aberto |
| **L8** | **"Vitrine (apenas ZAP/VR)"** | O fluxo online de Autos não passa por vitrine. Qual é o caminho de check-out em Autos, e por que ele difere? | 🔴 aberto |
| **L9** | **Impulsionado × não impulsionado sem custo ao lado** | O recorte diz quanto do tráfego é comprado, mas sem investimento por canal não vira **CAC por canal** — que é exatamente a UDE #9 (o CAC é uma média) | 🔴 aberto |
| **L10** | **MQL e SQL aparecem como caixas, sem definição** | Matheus votou **Qualificação** como a trava. Diagnosticar qualificação sem critério escrito de MQL e SQL é impossível | 🔴 aberto |
| **L11** | **Os incentivos na área logada alimentam dois destinos** — 10% de volta ao tráfego e 3% direto ao formulário | Se o incentivo age sobre quem já é cliente, parte do que entra como "novo" é **expansão**, não aquisição. Contamina a leitura de CAC e a de churn. Liga direto à pergunta 3B sobre crescimento vir de cliente novo ou de base | 🔴 aberto |
| **L12** | **"Outros" é a segunda maior fatia (11%) e aparece duas vezes** — como canal de marketing e como canal de entrada | Uma caixa-preta grande no meio do mapa. Sem decompor, 11% da representatividade fica sem dono | 🔴 aberto |
| **L13** | **"Portais / POS": o que é POS aqui?** | Nomenclatura interna não confirmada. Mapa com termo ambíguo não conduz comitê | 🔴 aberto |
| **L14** | **Os dois slides não se conciliam num mapa só.** FLUXOS cobre as etapas 1–2 da jornada com granularidade de canal; a jornada cobre 3–6 sem canal | O `mapeamento-fluxo-receita.md` precisa ser a costura dos dois, com o vocabulário deles | 🟡 em andamento |

Somam-se a estas as **7 ambiguidades da jornada** — a começar por *89% é sobre anúncio ou sobre
cliente?* — em [jornada-do-cliente-profissional.md](jornada-do-cliente-profissional.md).

---

## F · Formulário: acrescentar ou reforçar

Nenhuma delas existe hoje nas 96. As que têm pergunta próxima estão marcadas como reforço.

| # | Bloco | Pergunta a acrescentar | Nasce de |
|---|---|---|---|
| **F1** | 04 · Funil | "Onde entra a prospecção ativa no fluxo desenhado? Ela gera MQL ou entra direto como oportunidade?" | L1 |
| **F2** | 04 · Funil | "Qual a definição objetiva de MQL e de SQL, escrita, e quem a aplica?" — *reforço*: existe a pergunta genérica de estágios do pipeline, falta nomear MQL/SQL | L10 |
| **F3** | 04 · Funil | "O fluxo termina na venda. Qual é o desenho de pós-venda: publicação, entrega de lead, renovação?" | L2 |
| **F4** | 05 · Marketing | "Investimento mensal por canal, últimos 12 meses, para fechar CAC por canal" — *reforço* da pergunta de CAC do bloco 03 | L9 |
| **F5** | 05 · Marketing | "O que compõe 'Outros', nos canais de marketing e nos canais de entrada?" | L12 |
| **F6** | 05 · Marketing | "O que é POS em 'Portais / POS'?" | L13 |
| **F7** | 3B · Árvore | "Os incentivos na área logada (Canal Pro, My Plan) agem sobre base existente ou sobre prospect? O que eles geram é aquisição ou expansão?" | L11 |
| **F8** | 04 · Funil | "Por que a vitrine existe apenas em ZAP/VR? Qual o caminho de check-out em Autos?" | L8 |
| **F9** | 06 · Dados | "Qual sistema produz a 'representatividade de MQL'? GA4, CRM ou BI? Dá para reproduzir o número?" | L4, L7 |
| **F10** | 03 · Números | "A mesma visão de canais em 12 meses, com corte mensal, e o mix fechando 100%" | L4, L5 |
| **F11** | 02 · Escopo | "O fluxo pode ser separado por vertical? Autos e Imóveis têm o mesmo desenho de canais?" | L3 |

---

## Como alimentar este caderno

1. Material novo → linha na tabela de origem, com registro de onde o original está versionado.
2. Toda lacuna nova ganha ID **L**, e a pergunta correspondente ganha ID **F**, com a referência
   cruzada preenchida nas duas direções.
3. Lacuna que vira compromisso do cliente, com DRI e prazo, **sai daqui** e vira linha de
   [PENDENCIAS.md](../PENDENCIAS.md). Este caderno é o que ainda não tem dono.
4. Status: 🔴 aberto · 🟡 em andamento · ✅ respondido, com a fonte da resposta.
