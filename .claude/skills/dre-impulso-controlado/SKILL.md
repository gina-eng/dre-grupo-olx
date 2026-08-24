---
name: dre-impulso-controlado
description: "Desenha e le o teste de impulso controlado (aumento de 20-30% em um input) para confirmar empiricamente se a trava apontada e mesmo a restricao. Use quando o operador disser /dre-impulso-controlado ou 'confirmar a restricao' ou 'teste de impulso'."
dependencies:
  - dre-consolidacao-causal
tools: []
fase: "1 — Identificar"
estimated_time: "2h de desenho + 2 a 4 semanas de leitura"
output_file: "dre-impulso-controlado.json"
---

# DR-E — Impulso Controlado

A consolidacao causal produz uma hipotese. O impulso controlado a submete ao mundo real: **aumenta-se deliberadamente um input em 20–30% e observa-se onde o sistema entope.**

## Logica

Se a restricao esta corretamente identificada, aumentar o volume que chega ate ela **nao** aumenta o throughput na mesma proporcao — a fila cresce na estacao restringida. Se o throughput acompanha o input, a restricao esta em outro lugar (ou nao ha restricao ativa naquele ponto).

Ver `00-playbook/01-fundamentos-dr-ote.md`.

## Passo 1 — Escolher o input

Escolha **um** input, a montante da trava suspeita, que seja:

- **Controlavel** — o cliente consegue mexer sem negociacao longa
- **Mensuravel em ate 4 semanas** — respeita o ciclo de venda do negocio
- **Reversivel** — se der ruim, volta ao patamar anterior sem dano

Exemplos por trava suspeita:

| Restricao suspeita | Input a impulsionar | O que observar |
|---|---|---|
| Qualificacao | Volume de leads (+25% de verba) | O CPL cai/mantem mas o SQL nao acompanha |
| Compromisso | Volume de leads qualificados | Agendamentos nao acompanham; no-show sobe |
| Decisao | Volume de propostas enviadas | Propostas abertas acumulam; win rate cai |
| Retencao | Volume de novos clientes | Base nao cresce liquida; churn absorve a entrada |
| Atencao | Investimento em midia | Impressoes sobem, CTR cai, CPL sobe |

**Nunca impulsione dois inputs ao mesmo tempo.** Duas variaveis, zero conclusao.

## Passo 2 — Definir a leitura antes de rodar

Escreva, antes do teste comecar:

- **Baseline** — valor do input e do throughput nas 4–12 semanas anteriores, com sazonalidade considerada
- **Magnitude** — +20% a +30%. Abaixo disso o sinal se perde no ruido; acima, o custo do teste fica alto e o sistema pode reagir de forma nao linear.
- **Janela** — no minimo 1 ciclo de venda completo
- **Metrica de confirmacao** — a metrica que, se **nao** acompanhar o input, confirma a restricao
- **Criterio de parada antecipada** — o que faz abortar o teste (queda de margem alem de X, reclamacao de cliente, estouro de capacidade operacional)
- **Custo do teste** — quanto o cliente vai gastar a mais, e aprovado por quem

## Passo 3 — Executar e registrar

Acompanhamento semanal. Registre input, throughput e as metricas intermediarias entre o input e a restricao suspeita. Nao ajuste nada durante a janela — ajuste no meio do teste destroi a leitura.

## Passo 4 — Ler o resultado

| Padrao observado | Leitura |
|---|---|
| Input +25%, throughput +0-8% | **Restricao confirmada.** A fila cresceu na estacao suspeita. |
| Input +25%, throughput +20-25% | Restricao **nao** esta ali. O sistema tinha folga. Volte a consolidacao causal. |
| Input +25%, throughput +10-15% | Inconclusivo. Restricao parcial, ou capacidade que se esgota dentro da janela. Estenda a janela ou aumente a magnitude. |
| Throughput cai | O input impulsionado degrada a qualidade a montante (ex.: verba extra comprando publico pior). Achado relevante por si so. |

Registre tambem **onde a fila apareceu fisicamente** — leads sem contato, propostas sem resposta, pedidos sem entrega. A evidencia fisica vale mais em comite do que a estatistica.

## Passo 5 — Concluir

- Restricao **confirmada** → segue para `/dre-udes-crt`. O impulso vira evidencia de abertura do comite.
- Restricao **refutada** → volte a `/dre-consolidacao-causal` com o novo dado. Refutar e resultado valido e barato; descobrir isso depois de 90 dias de plano nao e.

## Output

Salve `dados/outputs/dre-impulso-controlado.json` com:

- `input_impulsionado`, `justificativa`, `magnitude_pct`, `janela_semanas`
- `baseline` — input e throughput, com sazonalidade
- `criterio_confirmacao`, `criterio_parada`, `custo_estimado`, `aprovado_por`
- `leitura_semanal[]` — semana, input, throughput, metricas intermediarias
- `resultado` — `confirmada | refutada | inconclusiva`
- `fila_observada` — onde o acumulo apareceu fisicamente
- `conclusao` e `proximo_passo`

## Finalizacao

1. Salve `dados/outputs/dre-impulso-controlado.json`
2. Atualize `dados/client.json`: `restricao_identificada.confirmada`, version++, `history[]`
3. Escreva a versao humana em `02-diagnostico/impulso-controlado.md`
4. Sugira `/dre-udes-crt` se confirmada; `/dre-consolidacao-causal` se refutada
