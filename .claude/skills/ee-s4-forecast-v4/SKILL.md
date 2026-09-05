---
name: ee-s4-forecast-v4
description: "Gera o Forecast de 12 meses do Comitê de Elevação (DR-X para DR-OTE) no padrão V4 'Fluxo Visual de Otimização': cartões de resumo, progresso da meta, callout de run-rate e funil mês a mês com incrementos, na identidade Destrava Receita (vermelho V4, sem azul). Use quando o operador pedir 'forecast', 'projeção de 12 meses', 'forecasting do comitê', 'modelo AS-IS contra Com Injeção', ou o entregável financeiro do Comitê de Elevação de qualquer cliente DR-X."
---

# Forecast V4 (Fluxo Visual de Otimização)

Entregável financeiro do Comitê de Elevação. Compara dois cenários ao longo de 12 meses: **AS-IS** (não executar) contra **Com Injeção** (executar o plano na trava governante). O formato é fixo e replica o modelo aprovado. Não reinventar o layout.

**Referências vivas (clonar uma destas, nunca Bantur/Infinit):** Liló Decor (e-commerce), Amado & Galantini (inside-sales jurídico), Santuá Confecções (inside-sales B2B) e Vera Cruz Coworking (recorrente/MRR). O catálogo completo, com trava governante, gerador e arquivo de saída de cada cliente, está em `references/exemplos-entregues.md`. Comece sempre pelo par mais próximo do modelo de venda do cliente novo.

## Formato atual: modelo vivo de 7 abas
O que a gente entrega hoje NÃO é o dashboard de aba única do `build_forecast_v4.py` original. É o modelo vivo `build_forecast_v4_*_completo.py`, um `.xlsx` de 7 abas onde a aba 1 é o dashboard idêntico ao entregável e as abas 3 a 6 leem a aba **Premissas** por fórmula (mexeu numa premissa, recalcula tudo):

1. Resumo Executivo: dashboard visual (print/share), idêntico ao entregável.
2. Premissas: todos os drivers de entrada, editáveis (fonte de verdade).
3. Forecast Mensal: receita, acumulado, atingimento, ticket, MER, CAC, CPL (FÓRMULAS).
4. Funil de Vendas: etapas e taxas mês a mês (FÓRMULAS).
5. Cenários & Sensibilidade: AS-IS vs Com Injeção mais os upsides do cliente.
6. Split de Mídia: distribuição por canal e campanhas, coerente com a verba.
7. Premissas & Ressalvas: base de calibração, alavanca governante, MER x CAC, pré-requisitos.

A aba 1 sozinha, o dashboard, é o que segue na estrutura obrigatória abaixo.

## Quando usar
Pedidos como "forecast", "projeção 12 meses", "forecasting", "modelo AS-IS vs Com Injeção", ou o entregável de projeções do Comitê de Elevação. Sempre depois da trava governante estar validada, porque a alavanca do cenário Com Injeção é a trava.

## Estrutura obrigatória do dashboard (não alterar a ordem)
1. Título (faixa vermelho profundo 980000) e subtítulo com a Meta Anual.
2. Cinco cartões de resumo: Mês Atual, Faturamento AS-IS, Com Injeção, Delta, Meta Anual, cada um com o acumulado embaixo.
3. Progresso até a meta: percentual acumulado AS-IS (vermelho) e Com Injeção (verde).
4. Callout de run-rate (faixa verde clara): em que mês o run-rate da meta é atingido e a que percentual da meta anual o acumulado chega.
5. Tabela mês a mês (Mês 1 a Mês 12), nas seções: Receita Mensal, Receita Acumulada, Atingimento de Meta, Alavancas de Crescimento (ticket, mídia, CAC, base, churn), Funil de Vendas (7 etapas com taxa e incremento entre elas).

## Identidade visual (sem azul)
Fonte IBM Plex Sans (padrao tipografico da V4). Vermelho profundo 980000 (faixas de cabeçalho), AS-IS E74C3C, Com Injeção C81E1E, verde 00A878 (deltas e meta batida), texto 2D3748, secundário 4A5568, rótulo 6C757D. Faixa de seção FDECEC, célula da injeção FFF0EC, célula do delta E8F8F3. Sem gridlines. Congelar em B15.

## Convenções de formatação (idênticas à referência)
- Dinheiro na tabela: R$41.000 (sem espaço, ponto de milhar). Nos cartões: R$ 41.000 (com espaço).
- Deltas: +R$3.000. Percentuais de meta e incremento: uma casa (53.6%, +6.5%), zero como 0%.
- Taxas de conversão do funil: com o valor real (7.3%, 25.8%), whole quando inteiro.
- Volumes do funil: ponto de milhar (2.336). Churn: marcador de não medido, seguindo a referência.

## Como gerar
Os geradores ficam em `.claude/scripts/`. Fluxo recomendado:

1. Escolha o par mais próximo em `references/exemplos-entregues.md` (e-commerce, inside-sales ou recorrente/MRR).
2. Copie o gerador desse par (ex.: `build_forecast_v4_vera_cruz_completo.py`) para um novo `build_forecast_v4_<cliente>_completo.py`.
3. Edite o dict CONFIG no topo com os números do cliente (cliente, escopo, saida, meta_anual, séries de 12 meses de faturamento AS-IS e Com Injeção, mídia, base, exposição e as taxas do funil). O script calcula sozinho: funil (atenção→recompra a partir de exposição e taxas), ticket (faturamento/base), CAC (mídia/decisão), acumulados, deltas e percentuais de meta.
4. Rode: `.venv/bin/python .claude/scripts/build_forecast_v4_completo.py` (gerador genérico copiado para este repo; os geradores por cliente citados em `references/exemplos-entregues.md` vivem no repo de origem). A saída vai para `dados/forecast-v4-<slug>.xlsx`.

`build_forecast_v4.py` é a origem de aba única (Liló Decor), mantida por referência. Para um cliente novo, prefira sempre clonar um `_completo`, que já é o formato entregue.

## Disciplina de fonte (obrigatória)
O forecast inteiro é modelado. Ancorar os pontos de partida em dado real (faturamento atual, margem, base ativa, conversão da trava, verba atual) e sinalizar como estimado [E] na apresentação. Nunca apresentar a curva como número auditado.

## Coerência com o diagnóstico
A alavanca do cenário Com Injeção tem que ser a trava governante do cliente, não "mais mídia" por padrão. Se a trava é Decisão ou Qualificação, a curva sobe por conversão com verba estável, e a exposição fica flat. Aumentar exposição na curva quando o diagnóstico refutou isso é erro grave.

## Escopo
O forecast é projeção de execução (DR-OTE), apresentado no Comitê de Elevação como retorno esperado do plano. Deixar isso explícito, não misturar com o diagnóstico do DR-X.
