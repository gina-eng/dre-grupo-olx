---
name: dre-matriz-expansao
description: "Transforma a discussao de crescimento em processo estruturado: cada hipotese de expansao avaliada por impacto x esforco x risco. Insumo do Comite 2. Use quando o operador disser /dre-matriz-expansao ou 'matriz de expansao' ou 'onde escalar'."
dependencies:
  - dre-plano-90-dias
tools: []
fase: "4 — Expandir"
estimated_time: "2h"
output_file: "dre-matriz-expansao.json"
---

# DR-E — Matriz de Expansao (POP 28)

Objetivo: tirar a decisao de crescimento do campo da intuicao. Cada hipotese de expansao vira uma linha comparavel.

## Pre-condicao inegociavel

**So se expande depois que a restricao atual esta saturada.** Verifique em `dados/outputs/dre-revisao-ciclo.json` → `capacidade_restricao.saturada`, ou na validacao de saturacao do Comite 2.

Se ainda ha espaco de otimizacao sem recursos novos, a resposta e voltar a Otimizar. Expandir sobre restricao nao saturada multiplica custo sem multiplicar throughput — e o erro mais caro do metodo.

## O que cada hipotese precisa explicitar

| Campo | Pergunta |
|---|---|
| `mudanca` | Qual mudanca sera realizada? |
| `problema_resolvido` | Qual problema ela resolve? |
| `impacto_sistema` | Como impacta o sistema de receita — especificamente a etapa da restricao? |
| `resultado_esperado` | Qual resultado, em numero, com que prazo? |

Hipotese que nao consegue responder as quatro nao entra na matriz.

## Avaliacao

Tres eixos, 1 a 5:

- **Impacto** — efeito **direto sobre a restricao**. Nao "impacto no negocio" em geral. Se a alavanca melhora uma etapa que nao e a restricao, o impacto no throughput e zero, por melhor que pareca.
- **Esforco** — tempo, complexidade, recursos novos, dependencia de terceiros.
- **Risco** — probabilidade de nao funcionar × custo se nao funcionar. Inclua risco de degradar um indicador de guarda.

Priorize por **impacto alto / esforco baixo / risco baixo**. Quando duas alavancas empatam, prefira a que produz evidencia mais rapido — aprender cedo vale mais que otimizar a escolha.

## Validacao intermediaria

Toda alavanca aprovada precisa de um **criterio de validacao intermediaria**: o que precisa ser verdade na semana 2 ou 3 para continuar investindo. Sem esse criterio, expansao ruim so aparece no fim do ciclo.

## Output

Salve `dados/outputs/dre-matriz-expansao.json` com:

- `restricao_saturada` — boolean, evidencia
- `hipoteses[]` — `mudanca`, `problema_resolvido`, `impacto_sistema`, `resultado_esperado`, `impacto` (1-5), `esforco` (1-5), `risco` (1-5), `score`, `investimento_estimado`, `criterio_validacao_intermediaria`, `dri`
- `recomendacao[]` — ordem sugerida, com justificativa
- `descartadas[]` — hipotese, motivo

## Finalizacao

1. Salve `dados/outputs/dre-matriz-expansao.json`
2. Atualize `dados/client.json`, version++, `history[]`
3. Escreva a versao humana em `03-estrategia/matriz-de-expansao.md`
4. Sugira `/dre-matriz-gp` e depois `/dre-comite` (Comite 2)
