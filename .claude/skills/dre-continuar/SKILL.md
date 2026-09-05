---
name: dre-continuar
description: "Le o estado do projeto DR-E e diz qual e o proximo passo do ciclo de 90 dias. Use quando o operador disser /dre-continuar ou 'onde paramos' ou 'qual o proximo passo' ou 'status do projeto'."
dependencies: []
tools: []
fase: "transversal"
estimated_time: "5 min"
output_file: null
---

# DR-E · Continuar (roteador de estado)

Voce e o copiloto do consultor DR-E do Grupo OLX. Esta skill nao produz entregavel: ela le o estado do repositorio e devolve **uma recomendacao de proximo passo**, com o porque.

## Passo 1 · Ler estado

Leia, nesta ordem:

1. `dados/client.json`: `meta.ciclo_atual`, `meta.fase_atual`, `meta.semana_corrente`, `progress.skills`, `travas`, `restricao_identificada`
2. `PENDENCIAS.md`: bloqueios abertos e severidade
3. `02-diagnostico/checklist-dados-e-acessos.md`: o que ainda nao chegou
4. `00-playbook/07-playbook-operacional-dr-e.md`: a semana corrente do ciclo e as tarefas previstas
5. `04-execucao/cronograma-e-marcos.md`: proximo marco com data

Se `dados/client.json` nao existir, pare e rode `/dre-onboarding`.

## Passo 2 · Diagnosticar a posicao no ciclo

Determine a fase pela evidencia no repositorio, nao pelo que o `client.json` afirma (o arquivo pode estar desatualizado):

| Evidencia encontrada | Fase real |
|---|---|
| Sem `dados/outputs/dre-fluxo-receita.json` | Fase 1 · Identificar, ainda no mapeamento |
| Fluxo de receita pronto, menos de 8 travas com score | Fase 1, diagnostico de travas em curso |
| 8 travas com score, sem `restricao_identificada` | Fase 1 · falta consolidacao causal |
| Restricao identificada, sem impulso controlado | Fase 1, falta confirmar a restricao |
| Restricao confirmada, sem CRT/Nuvem | Fase 2 · Otimizar, entrar no LTP |
| Injecao definida, sem plano de 90 dias | Fase 2, falta traduzir injecao em plano |
| Plano pronto, sem Matriz aprovada | Fase 3 · Alinhar, falta o quality gate do GP |
| Matriz aprovada, comite nao realizado | Fase 3 · preparar comite |
| Comite 3 do ciclo realizado | Fase 5 · Recomecar, rodar `/dre-revisao-ciclo` |

## Passo 3 · Aplicar as travas de bloqueio

Antes de recomendar qualquer avanco, verifique os bloqueios duros do metodo:

- **Nao ha comite sem Matriz aprovada.** Se `progress.skills["dre-matriz-gp"]` nao esta `approved`, o proximo passo e a Matriz, nunca o comite. Ver `00-playbook/03-ciclo-90-dias-e-comites.md`.
- **Nao ha diagnostico de trava sem dado.** Se o bloco de dados correspondente no checklist esta pendente, o proximo passo e cobrar o dado, e a cobranca vira linha em `PENDENCIAS.md` com responsavel e prazo.
- **Nao ha forecast sem fluxo de receita fechado.** A receita derivada do funil precisa bater com a receita declarada.
- **Regra de Goldratt.** Se ha travas sem score, priorize as de baixo do funil (Retencao, Decisao, Compromisso) antes das de topo.

## Passo 4 · Responder

Formato da resposta (curta, sem preambulo):

```
Ciclo {n}, Fase {nome}, semana {x} de 12

Feito:      {ultimas 2-3 entregas com data}
Em aberto:  {bloqueios de PENDENCIAS.md com severidade alta}
Proximo:    /{skill}, {uma linha de porque}

Marco mais proximo: {data}, {evento}
```

Se houver pendencia de severidade alta que bloqueia o proximo passo, diga isso primeiro e proponha a acao de desbloqueio (quem cobra o que, ate quando) antes de sugerir a skill.

## Regras

- Nunca invente progresso. Se o arquivo nao existe, a entrega nao foi feita.
- Nunca sugira duas skills ao mesmo tempo. Uma recomendacao, um porque.
- Se a fase real divergir de `meta.fase_atual`, corrija o `client.json` (version++, entrada em `history[]`) e avise o operador da correcao em uma linha.
