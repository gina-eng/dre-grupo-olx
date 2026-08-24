---
name: dre-fluxo-receita
description: "Mapeia o fluxo de receita ponta a ponta com volumes e taxas de conversao por etapa, do primeiro contato ate a recompra. Base de todo o diagnostico de travas e do forecast. Use quando o operador disser /dre-fluxo-receita ou 'mapear o funil' ou 'fluxo de receita'."
dependencies:
  - dre-onboarding
tools: []
fase: "1 — Identificar"
estimated_time: "4h"
output_file: "dre-fluxo-receita.json"
---

# DR-E — Fluxo de Receita (POP Fluxo de Receita)

Voce vai desenhar o caminho completo que o dinheiro percorre dentro do negocio: **cada etapa, com volume absoluto, taxa de passagem e tempo medio**. Sem esse mapa, o diagnostico de travas nao tem denominador e o forecast nao tem base.

## Principio

O fluxo de receita e a leitura fisica do throughput (Goldratt): Vendas menos Custos Totalmente Variaveis. Cada etapa e uma estacao; a estacao mais lenta define a vazao do sistema inteiro. Ver `00-playbook/01-fundamentos-dr-ote.md`.

## Passo 1 — Segmentar antes de somar

O Grupo OLX opera unidades com economias diferentes (ver `01-cliente/perfil-grupo-olx.md`). **Nao existe um funil unico.** Monte um fluxo por unidade de negocio / modelo de receita e so depois consolide.

Para cada unidade, registre: modelo de receita (transacional, recorrente, marketplace, take rate), ticket medio, ciclo de venda e sazonalidade.

## Passo 2 — Etapas do fluxo

Mapeie as etapas reais do negocio, nao um funil generico. O esqueleto minimo:

| # | Etapa | Metrica de volume | Taxa que sai dela |
|---|---|---|---|
| 1 | Mercado enderecavel | TAM/SAM/SOM | — |
| 2 | Exposicao | impressoes / alcance | CTR |
| 3 | Visita | sessoes | taxa de engajamento |
| 4 | Lead / cadastro | leads | taxa de conversao de visita |
| 5 | Lead qualificado | MQL/SQL | taxa de qualificacao |
| 6 | Oportunidade | reunioes / propostas | taxa de agendamento e comparecimento |
| 7 | Fechamento | contratos / pedidos | win rate |
| 8 | Receita | faturamento | ticket medio |
| 9 | Retencao | churn, recompra | LTV, frequencia |

Ajuste os nomes ao vocabulario do cliente. Um funil que o cliente nao reconhece nao serve para conduzir comite.

## Passo 3 — Preencher com dado real

Fontes, em ordem de confiabilidade:

1. CRM e sistema transacional do cliente (blocos do `02-diagnostico/checklist-dados-e-acessos.md`)
2. Plataformas de midia (`.claude/scripts/v4mos_fetch.sh dados` ou `.claude/scripts/meta_ads_fetch.sh`)
3. Analytics / tracking
4. Estimativa declarada pelo cliente — **sempre marcada `[E]`**

Regra dura: **a receita derivada do funil precisa bater com a receita declarada.** Se multiplicar volume por taxa por ticket nao chega no faturamento real, o mapa esta errado — nao o faturamento. Investigue: etapa faltando, dupla contagem, canal nao mapeado, receita recorrente somada como nova.

Janela padrao: **ultimos 12 meses**, com corte mensal. Se houver sazonalidade forte, registre o indice sazonal por mes.

## Passo 4 — Ler o mapa

Para cada etapa calcule:

- **Volume absoluto** e **taxa de passagem** (etapa n / etapa n-1)
- **Perda absoluta** — quantas unidades morrem ali. Esta e a coluna que importa: uma taxa ruim em cima de volume pequeno perde para uma taxa mediana em cima de volume grande.
- **Tempo medio** na etapa e tempo acumulado ate a receita
- **Comparacao com benchmark** do setor, quando existir (`ee-s2-diagnostico-midia/references/benchmarks-por-setor.md`)

Ordene as etapas por **perda absoluta de receita potencial**, nao por taxa percentual. Esse ranking e a primeira hipotese de restricao — hipotese, nao veredito.

## Passo 5 — Marcar as travas candidatas

Cada etapa do fluxo mapeia para uma ou mais das 8 travas (`00-playbook/02-travas-de-receita.md`). Registre a associacao: isso define quais diagnosticos de trava rodam primeiro.

Aplique a **regra de Goldratt**: investigue de baixo para cima. Uma trava de Retencao ou Decisao contamina toda a leitura das etapas de topo — resolver Exposicao com Decisao quebrada so aumenta o custo do desperdicio.

## Output

Salve `dados/outputs/dre-fluxo-receita.json` seguindo `.claude/shared-templates/PADRAO-OUTPUT.md` (campos `summary`, `summary_headline`, `summary_highlights`, `summary_key_findings`, `key_leverage_point`) mais:

- `unidades[]` — uma entrada por unidade de negocio, cada uma com `etapas[]`
- `etapas[]` — `nome`, `volume`, `taxa_entrada`, `perda_absoluta`, `tempo_medio_dias`, `fonte`, `estimado`, `travas_associadas[]`
- `reconciliacao` — `receita_derivada`, `receita_declarada`, `divergencia_pct`, `explicacao`
- `ranking_perda[]` — etapas ordenadas por perda absoluta
- `travas_prioritarias[]` — ordem sugerida de diagnostico, com justificativa

## Checklist antes de fechar

- [ ] Receita derivada bate com a declarada (divergencia < 5%) ou a divergencia esta explicada
- [ ] Toda etapa tem fonte nomeada
- [ ] Todo numero estimado esta marcado `[E]` / `"estimado": true`
- [ ] Ranking e por perda absoluta, nao por percentual
- [ ] Ordem de diagnostico respeita a regra de Goldratt (bottom-up)
- [ ] Dados que faltaram viraram linha em `PENDENCIAS.md`

## Finalizacao

1. Salve `dados/outputs/dre-fluxo-receita.json`
2. Atualize `dados/client.json`: `progress.skills`, `briefing.receita_declarada_12m`, version++, `history[]`
3. Escreva a versao humana em `02-diagnostico/fluxo-de-receita.md`
4. Sugira `/dre-diagnostico-trava` para a primeira trava do ranking
