---
name: dre-comite
description: "Prepara, conduz e documenta os Comites 1, 2 e 3 do ciclo DR-E, com roteiro time-boxed e ata com decisoes rastreaveis. Use quando o operador disser /dre-comite ou 'preparar comite' ou 'ata do comite' ou 'conduzir o comite'."
dependencies:
  - dre-matriz-gp
tools: []
fase: "3 — Alinhar / 4 — Expandir / 5 — Recomecar"
estimated_time: "2h de comite + 5h de preparacao"
output_file: "dre-comite-{n}.json"
---

# DR-E — Comites

Pergunte ao operador **qual comite** (1, 2 ou 3) e se e **preparacao**, **conducao** ou **ata**.

> **Bloqueio duro:** verifique `dados/client.json` → `progress.skills["dre-matriz-gp"]`. Se nao esta `approved` para este comite, **pare** e rode `/dre-matriz-gp`. Ver `00-playbook/03-ciclo-90-dias-e-comites.md`.

O comite e um **ponto de decisao**, nao uma apresentacao de resultados. Se ao fim ninguem decidiu nada, o comite falhou — independentemente da qualidade dos slides.

## Comite 1 — Validacao da trava (2h)

| Bloco | Tempo | Conteudo |
|---|---|---|
| Abertura e contextualizacao | 5 min | Enquadrar como ponto de decisao. Recapitular fluxo de receita e o racional da hipotese. |
| Apresentacao do diagnostico | 15 min | Conectar evidencia **analitica** (dados), **experiencial** (relatos, cliente oculto) e **sistemica** (como se ligam no fluxo). Mostrar onde o fluxo desacelera, onde ha perda direta de receita, como isso aparece no dia a dia. |
| Validacao logica da trava | 15 min | Etapa mais critica. Perguntas: *Se essa trava for resolvida, o sistema melhora de forma perceptivel? Essa hipotese explica a maior parte dos problemas? Existem sintomas relevantes nao explicados?* CRT como instrumento. Eliminar hipoteses concorrentes com evidencia. |
| Definicao da estrategia de otimizacao | 20 min | **Regra explicita: nao sao permitidas solucoes que envolvam aumento de capacidade via novos recursos.** So ajuste de processo, reducao de retrabalho, melhoria de priorizacao, eliminacao de desperdicio. |
| Plano de acao (30 dias) | 20 min | Cada acao: o que · DRI · prazo · metrica de sucesso · como impacta diretamente a restricao. |

**Indicador de qualidade nas semanas seguintes:** reducao de perdas na etapa da restricao, melhoria de conversao associada e **execucao do plano acima de 80%**.

## Comite 2 — Decisao de expansao (2h · DR-E presencial)

| Bloco | Tempo | Conteudo |
|---|---|---|
| Revisao da execucao anterior | 15 min | Concluido / parcial / nao iniciado. Causa dos desvios: priorizacao, capacidade, clareza de instrucao ou fator externo. |
| Analise de resultados | 20 min | Antes/depois com foco na etapa da restricao. Distinguir variacao pontual de mudanca estrutural. |
| Validacao da saturacao da trava | 15 min | *O sistema ja extraiu o maximo possivel com os recursos atuais?* Ausencia de melhoria pode indicar **falha de execucao**, nao saturacao. Se ainda ha espaco sem novos recursos → **voltar a Otimizar**. |
| Estrategia de expansao | 20 min | Para cada alavanca: que problema resolve · como impacta a restricao · risco · retorno esperado. |
| Plano de acao (30 dias) | 20 min | Escopo, DRI, prazo, investimento, metrica. **Criterios de validacao intermediaria** ao longo das semanas. |

> **Quando a decisao e no-go, isso nao e falha do ciclo — e o metodo funcionando.** Registre o no-go na ata com o mesmo peso de um go.

## Comite 3 — Virada de ciclo (2h)

| Bloco | Tempo | Conteudo |
|---|---|---|
| Revisao consolidada do ciclo | 20 min | Acoes → resultados → hipoteses testadas. Que intervencoes geraram impacto e quais nao. |
| Analise sistemica do estado atual | 20 min | Fluxo de receita atualizado: ganho de capacidade, novos gargalos, redistribuicao de perdas. *Onde o fluxo desacelera agora?* |
| Validacao da nova trava | 20 min | Mesmo rigor do Comite 1. CRT como apoio. Reduzir o sistema a **uma unica prioridade clara**. |
| Nova prioridade estrategica | 15 min | Explicita, documentada, com justificativa ligando dados, logica e contexto de negocio. |
| Plano de acao (30 dias) | 15 min | Ja orientado a nova restricao, para continuidade imediata. |

**Classificacao obrigatoria da trava anterior:** `resolvida` · `parcialmente_resolvida` · `nao_resolvida`.

## Preparacao (antes de qualquer comite)

1. Confirme Matriz aprovada.
2. Monte o material a partir dos outputs existentes — nao gere numero novo dentro do material.
3. Prepare as **objecoes do decisor** com resposta e evidencia (reaproveite `objecoes_simuladas[]` da Matriz).
4. Confirme presenca do decisor. Comite sem quem decide vira reuniao de status — remarque.
5. Circule a pauta com antecedencia e diga explicitamente **o que sera decidido**.

## Ata (obrigatoria)

Escreva em `06-reunioes/{AAAA-MM-DD}-comite-{n}.md`. Estrutura minima:

- Data, duracao, participantes (nome e papel), formato (presencial/remoto)
- Decisoes tomadas — cada uma com o racional em uma linha
- Decisoes **nao** tomadas e o que falta para tomar
- Plano de 30 dias: acao · DRI (pessoa) · prazo · metrica · impacto na restricao
- Divergencias registradas (quem discordou e de que)
- Riscos aceitos
- Data do proximo comite

> **Toda decisao vai para ata assinada.** Decisao que so existe na memoria da reuniao nao existe — e a fonte numero um de retrabalho no ciclo seguinte.

## Output

Salve `dados/outputs/dre-comite-{n}.json` com:

- `comite` — numero, data, formato, duracao_min
- `matriz_aprovada` — boolean, data
- `participantes[]` — nome, papel, empresa, presente
- `blocos[]` — bloco, tempo_previsto, tempo_real, conteudo_coberto
- `decisoes[]` — decisao, racional, quem_decidiu, tipo (`go | no_go | ajuste`)
- `plano_30_dias[]` — acao, dri, prazo, metrica, impacto_restricao
- `divergencias[]`, `riscos_aceitos[]`
- Comite 2: `saturacao_validada` — boolean + justificativa, `decisao_expansao`
- Comite 3: `classificacao_trava_anterior`, `nova_restricao`, `justificativa`
- `proximo_comite`

## Finalizacao

1. Salve o JSON e a ata em `06-reunioes/`
2. Atualize `dados/client.json`: `progress`, `meta.fase_atual`, e (Comite 3) `restricao_identificada`; version++, `history[]`
3. Espelhe os marcos em `04-execucao/cronograma-e-marcos.md` e as pendencias em `PENDENCIAS.md`
4. Proximo passo: Comite 1 → acompanhar execucao; Comite 2 → executar expansao; Comite 3 → `/dre-revisao-ciclo`
