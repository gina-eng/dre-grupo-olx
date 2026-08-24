---
name: dre-forecast
description: "Monta o forecast de 12 meses no RevenueFlow a partir da matematica do sistema atual, com as tres linhas (Meta, Atual organico, Com Injecao). Use quando o operador disser /dre-forecast ou 'montar o forecast' ou 'projecao de receita'."
dependencies:
  - dre-fluxo-receita
  - dre-consolidacao-causal
tools: []
fase: "3 — Alinhar"
estimated_time: "2h"
output_file: "dre-forecast.json"
---

# DR-E — Forecast de 12 Meses (POP 27)

Sistema: <https://v4-revenueflow.lovable.app/>

> **Principio central:** o forecast **nao nasce da meta do cliente — nasce da matematica do sistema atual.** A unica diferenca entre o cenario atual e o projetado e a alavanca que decidimos mexer.

## Pre-condicoes

- `dados/outputs/dre-fluxo-receita.json` fechado, com `reconciliacao.divergencia_pct` < 5%
- `restricao_identificada` definida em `dados/client.json`
- Sem fluxo de receita reconciliado, **nao monte forecast**. Projecao sobre funil inconsistente e ficcao com casas decimais.

## Etapas na plataforma

| # | Etapa | Conteudo |
|---|---|---|
| 1 | Acessar | Novo Projeto. Buscar **sempre pela Razao Social**. Editar apenas projetos proprios. |
| 2 | Preenchimento inicial | Razao social, segmento, modelo de venda; faturamento 12m, meta 12m, faturamento do mes atual; ticket medio, crescimento organico mensal, CAC, % de investimento em midia, LTV (meses), taxa de recompra, CPM |
| 3 | Identificar a trava | A selecao determina onde a injecao sera aplicada |
| 4 | Diagnostico (validacao do funil) | O sistema calcula Exposicao → Atencao → Interesse → Qualificacao → Compromisso → Decisao |
| 5 | Injecao | Metrica a melhorar · % de melhoria · tempo de efeito maximo |
| 6 | Forecast completo | Linhas: **Meta** · **Atual (organico)** · **Com Injecao** |
| 7 | Fluxo visual | Evolucao mes a mes |
| 8 | Grande Forecast | Tabela tecnica: receita mensal e acumulada, delta, atingimento, incrementos, evolucao do funil |

## Regras duras

1. **O faturamento gerado pelo funil deve bater** com o faturamento mensal declarado e com o faturamento anual dos ultimos 12 meses. Divergencia significa dados inconsistentes — ajuste as metricas ate a matematica fechar. Nao "arredonde para bater": encontre o erro.
2. **Tempo de efeito maximo:** quanto menor o tempo, maior o impacto acumulado. Seja conservador — tempo de efeito otimista e a forma mais comum de inflar forecast sem perceber.
3. **Uma injecao por forecast.** Duas alavancas simultaneas tornam impossivel atribuir o resultado.
4. **A meta do cliente entra como linha de referencia, nao como premissa.** Se a linha "Com Injecao" nao alcanca a meta, isso e o achado — e a conversa mais util do comite.

## Parametros a validar antes de rodar

| Parametro | Como validar |
|---|---|
| Faturamento 12m | Fonte contabil ou sistema transacional, nao estimativa |
| Ticket medio | Receita / numero de pedidos no mesmo periodo |
| CAC | Investimento total de aquisicao / novos clientes. Se o cliente nao tem, e sintoma de Trava de Cegueira |
| LTV (meses) | Do scorecard de retencao. Se nao medido, marque `[E]` e registre a fragilidade |
| Taxa de recompra | Base de clientes com 2+ compras / base total, na janela |
| Crescimento organico mensal | Regressao dos ultimos 12 meses, nao a media simples |
| % melhoria da injecao | Do `dre-plano-90-dias` (meta do indicador da restricao). Precisa ser defensavel com benchmark ou piloto |

## Ferramenta local alternativa

Para o modelo em planilha: `.venv/bin/python .claude/scripts/build_forecast_v4_completo.py`. Exemplos de saida entregue em `ee-s4-forecast-v4/references/exemplos-entregues.md`. Use o RevenueFlow como fonte oficial; a planilha serve para cenarios e para o material do comite.

## Output

Salve `dados/outputs/dre-forecast.json` seguindo `.claude/shared-templates/PADRAO-OUTPUT.md` mais:

- `projeto_revenueflow` — url, razao social usada
- `parametros` — cada um com `valor`, `fonte`, `estimado`
- `validacao_funil` — `receita_derivada`, `receita_declarada_12m`, `receita_mes_atual`, `divergencia_pct`, `fechou` (boolean)
- `injecao` — `trava`, `metrica`, `melhoria_pct`, `tempo_efeito_meses`, `justificativa`
- `linhas` — `meta[]`, `atual_organico[]`, `com_injecao[]` (12 meses cada)
- `grande_forecast[]` — mes, receita, acumulado, delta, atingimento_pct, funil
- `atinge_meta` — boolean + gap

## Como explicar ao cliente

> "O forecast nao e uma previsao otimista. Ele e a matematica do seu sistema atual. A unica diferenca entre o cenario atual e o projetado e a alavanca que decidimos mexer."

## Finalizacao

1. Salve `dados/outputs/dre-forecast.json`
2. Atualize `dados/client.json`, version++, `history[]`
3. Escreva a versao humana em `03-estrategia/forecast-12-meses.md`
4. Sugira `/dre-matriz-gp`
