---
name: dre-plano-90-dias
description: "Traduz a Arvore de Transicao em plano de 90 dias com iniciativas, DRI, prazo, indicador e criterio de sucesso, encaixado nas 5 fases do ciclo. Use quando o operador disser /dre-plano-90-dias ou 'montar o plano' ou 'plano de 90 dias'."
dependencies:
  - dre-frt-prt
tools: []
fase: "3 — Alinhar"
estimated_time: "3h"
output_file: "dre-plano-90-dias.json"
---

# DR-E — Plano de 90 Dias

O plano nao e uma lista de tarefas: e a **sequencia que torna a injecao verdadeira dentro de um ciclo**. Tudo que nao serve a injecao fica de fora, mesmo sendo boa ideia.

## Insumos

- `dados/outputs/dre-frt-prt.json` → `transicao.passos[]` e `prt.obstaculos[]`
- `dados/outputs/dre-consolidacao-causal.json` → a restricao e a politica implicita
- `00-playbook/03-ciclo-90-dias-e-comites.md` → as 5 fases e as datas dos comites
- `04-execucao/cronograma-e-marcos.md` → marcos ja compromissados

## Regra de escopo

Cada iniciativa do plano precisa responder: **"qual passo da Arvore de Transicao isso executa?"** Iniciativa que nao aponta para um passo nao entra. Se o cliente insistir num item fora da injecao, registre-o em backlog com a justificativa de exclusao — nao no plano.

Limite pratico: **3 a 6 iniciativas** por ciclo. Plano com 15 frentes e plano sem restricao — o oposto do que o DR-E propoe.

## Estrutura de cada iniciativa

| Campo | Regra |
|---|---|
| `nome` | Verbo no infinitivo + objeto. Nao "CRM", e "Implantar campos de qualificacao no CRM" |
| `passo_transicao` | Qual passo da Transicao executa |
| `dri` | **Uma** pessoa nomeada, do lado do cliente. V4 assessora, cliente executa |
| `apoio_v4` | O que a V4 entrega para viabilizar |
| `inicio` / `fim` | Datas dentro da janela de 90 dias |
| `indicador` | A metrica que se move se der certo |
| `baseline` | Valor de hoje, com fonte |
| `meta` | Valor esperado ao fim do ciclo, com o racional |
| `criterio_sucesso` | Frase binaria, verificavel no comite |
| `pre_requisitos` | Da PRT |
| `risco` | O que pode impedir + mitigacao |

> **DRI e sempre pessoa, nunca area.** "Marketing" nao responde por nada. Se nao ha nome, a iniciativa nao esta pronta para entrar no plano.

## Encaixe nas 5 fases

| Fase | Semanas | O que o plano contempla |
|---|---|---|
| Identificar | 1–3 | Ja executada — entra como contexto |
| Otimizar | 4–7 | Iniciativas que atacam a restricao diretamente |
| Alinhar | 8–9 | Rituais, indicadores e governanca que sustentam a mudanca |
| Expandir | 10–11 | Ampliacao do que funcionou, so apos evidencia |
| Recomecar | 12 | Revisao do ciclo e proxima restricao |

Distribua as iniciativas respeitando essa logica. **Nao ha expansao antes de evidencia de que a otimizacao funcionou** — expandir cedo e o erro classico que transforma ganho em custo.

## Indicadores

Separe:
- **Indicador da restricao** — o unico que prova que a trava governante cedeu. Um so.
- **Indicadores de suporte** — 3 a 5, que mostram se as iniciativas estao acontecendo.
- **Indicador de guarda** — o que nao pode piorar enquanto a restricao melhora (margem, NPS, churn). Vem dos `efeitos_colaterais[]` da FRT.

## Output

Salve `dados/outputs/dre-plano-90-dias.json` seguindo `.claude/shared-templates/PADRAO-OUTPUT.md` mais:

- `ciclo`, `janela` (`inicio`, `fim`), `injecao`, `restricao`
- `iniciativas[]` — todos os campos da tabela acima
- `indicadores` — `restricao`, `suporte[]`, `guarda[]`, cada um com `baseline`, `meta`, `fonte`, `cadencia_leitura`
- `backlog_excluido[]` — item, quem pediu, motivo da exclusao
- `marcos[]` — comites e entregas, com data
- `riscos[]` — risco, probabilidade, impacto, mitigacao, dono

## Checklist antes de fechar

- [ ] 3 a 6 iniciativas, todas ancoradas em um passo da Transicao
- [ ] Todo DRI e pessoa nomeada
- [ ] Todo indicador tem baseline com fonte
- [ ] Existe indicador de guarda vindo dos efeitos colaterais da FRT
- [ ] Nenhuma iniciativa de expansao antes da evidencia de otimizacao
- [ ] Pre-requisitos da PRT viraram iniciativa ou estao garantidos
- [ ] O que ficou de fora esta no `backlog_excluido[]` com justificativa

## Finalizacao

1. Salve `dados/outputs/dre-plano-90-dias.json`
2. Atualize `dados/client.json`, version++, `history[]`
3. Escreva a versao humana em `03-estrategia/plano-90-dias.md`; espelhe os marcos em `04-execucao/cronograma-e-marcos.md`
4. Sugira `/dre-forecast` (se o ciclo exige projecao) e depois `/dre-matriz-gp` — **o plano nao vai a comite sem Matriz aprovada**
