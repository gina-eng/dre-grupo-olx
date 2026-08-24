---
name: dre-matriz-gp
description: "Monta a Matriz do Growth Planner e roda o quality gate obrigatorio antes de cada comite. Nenhum comite acontece sem Matriz aprovada. Use quando o operador disser /dre-matriz-gp ou 'aprovar material' ou 'matriz do GP' ou 'quality gate'."
dependencies:
  - dre-plano-90-dias
tools: []
fase: "3 — Alinhar"
estimated_time: "5h (DR-E, com C-Level)"
output_file: "dre-matriz-gp.json"
---

# DR-E — Matriz do Growth Planner (quality gate)

> **Regra nao negociavel do metodo: nao ha comite sem Matriz aprovada.** Ver `00-playbook/03-ciclo-90-dias-e-comites.md`. Material reprovado volta para ajuste; a data do comite so se mantem se o ajuste couber no prazo.

Participantes no DR-E: **Growth Planner + Consultor + C-Level**.

## O que a Matriz avalia

A Matriz nao revisa estetica de slide. Ela testa se o material sustenta uma decisao de C-Level.

| Criterio | Pergunta de aprovacao | Reprova quando |
|---|---|---|
| **Rastreabilidade** | Todo numero tem fonte nomeada e data? | Ha numero sem origem, ou fonte generica ("dados do cliente") |
| **Restricao unica** | O material aponta **uma** restricao governante? | Aponta tres "focos" ou uma lista de melhorias |
| **Cadeia logica** | Diagnostico → causa-raiz → injecao → plano fecham sem salto? | Alguma etapa aparece sem derivar da anterior |
| **Politica implicita** | A causa-raiz esta formulada como politica, nao como pessoa? | "O time nao faz follow-up" em vez da politica que permite isso |
| **Evidencia experiencial** | Ha cliente oculto / jornada / visita registrada? | So planilha |
| **Decisao pedida** | Esta explicito o que o C-Level precisa decidir e o custo de nao decidir? | O material informa mas nao pede decisao |
| **Numeros de guarda** | Ha indicador do que nao pode piorar? | So metricas de ganho |
| **Estimativas marcadas** | Todo `[E]` esta visivel ao leitor? | Estimativa apresentada como dado |
| **Reconciliacao** | Receita do funil bate com a declarada? | Divergencia > 5% sem explicacao |
| **Proximo passo** | Cada acao tem DRI nomeado e data? | Responsavel e uma area |

## Roteiro da sessao

1. **Leitura seca (30 min)** — GP le o material sem o consultor explicar. O que nao se entende sozinho nao vai para o comite.
2. **Confronto de evidencia (2h)** — para cada afirmacao central, o GP pede a fonte. Consultor mostra o dado.
3. **Teste de decisao (1h)** — GP assume o papel do decisor e pergunta o que ele perguntaria. Objecao sem resposta vira ajuste.
4. **Ajustes (1h)** — lista com dono e prazo.
5. **Veredito (30 min)** — `aprovado` · `aprovado_com_ajustes` · `reprovado`.

## Regra de reprovacao

`reprovado` bloqueia o comite. Registre no `dados/client.json` (`progress.skills["dre-matriz-gp"] = "pending"`), abra linha em `PENDENCIAS.md` com severidade alta e avise imediatamente quem controla a agenda do comite — remarcar cedo custa menos que conduzir um comite sem sustentacao.

`aprovado_com_ajustes` so libera o comite depois que os ajustes estao feitos e verificados. Nao e um "aprovado" com asterisco.

## Output

Salve `dados/outputs/dre-matriz-gp.json` com:

- `comite_alvo` — numero, data
- `criterios[]` — `criterio`, `status` (`ok | ajustar | reprova`), `evidencia`, `ajuste_requerido`
- `objecoes_simuladas[]` — pergunta do decisor, resposta preparada, robustez
- `veredito` — `aprovado | aprovado_com_ajustes | reprovado`
- `ajustes[]` — item, dono, prazo, `concluido`
- `participantes`, `data`

## Finalizacao

1. Salve `dados/outputs/dre-matriz-gp.json`
2. Atualize `dados/client.json`: `progress.skills["dre-matriz-gp"]` = `approved` **somente** se o veredito for `aprovado` (ou `aprovado_com_ajustes` com todos os ajustes `concluido: true`), version++, `history[]`
3. Registre o veredito em `06-reunioes/` e em `PENDENCIAS.md` se houver reprova
4. Se aprovado, sugira `/dre-comite`
