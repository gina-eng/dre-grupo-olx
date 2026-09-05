---
name: dre-tira-duvidas
description: "Responde a assessoria assincrona do cliente dentro do SLA de 12h uteis do DR-E, sem alterar a estrategia central definida em comite. Use quando o operador disser /dre-tira-duvidas ou 'responder o cliente' ou 'duvida do cliente' ou 'acompanhar metricas'."
dependencies:
  - dre-comite
tools: []
fase: "transversal (semanas 4-11)"
estimated_time: "1h por bloco"
output_file: null
---

# DR-E · Tira Duvidas e Acompanhamento (POPs 31-32)

Assessoria assincrona continua. **SLA do DR-E: 12 horas uteis.** Ver `00-playbook/03-ciclo-90-dias-e-comites.md` e a clausula de SLA em `04-execucao/contrato-e-escopo.md`.

## Regra central

**Ajustes taticos sao permitidos desde que nao alterem a estrategia central definida no comite.**

Antes de responder, classifique a demanda:

| Tipo | Como tratar |
|---|---|
| **Duvida de execucao** | Responder direto. Aponte o documento do repositorio que sustenta a resposta. |
| **Ajuste tatico** | Autorizar, registrar no acompanhamento, informar o impacto esperado. Nao precisa de comite. |
| **Mudanca de estrategia** | **Nao autorizar por canal assincrono.** Registrar como ponto de pauta do proximo comite, com o custo de esperar. Se for urgente, propor comite extraordinario. |
| **Pedido fora de escopo** | Comparar com `04-execucao/contrato-e-escopo.md`. Responder o que esta dentro, registrar o que esta fora e encaminhar comercialmente. |

Quando a duvida vier disfarcada de ajuste tatico mas mudar a alavanca do ciclo, diga isso explicitamente. Deixar passar e como o plano se dissolve sem ninguem decidir dissolve-lo.

## Acompanhamento de metricas (POP 32)

Foco **na etapa da restricao**. Nao reporte o painel inteiro toda semana, reporte a restricao e os indicadores de guarda.

1. **Diferencie variacao normal de mudanca estrutural.** Compare com a variabilidade historica da propria metrica, nao com a semana anterior.
2. **Classifique todo desvio relevante:** `falha de execucao` · `hipotese incorreta` · `fatores externos`.
3. Se o indicador de guarda piorou, isso sobe na comunicacao antes de qualquer boa noticia.

## Formato da resposta ao cliente

- Responda a pergunta feita, primeiro, em uma ou duas linhas.
- Depois o racional, com o dado e a fonte.
- Se a resposta muda algo no plano, diga o que muda, quem faz e ate quando.
- Se depende de dado que nao chegou, diga qual, de quem e desde quando esta pendente.

## Registro

Toda interacao relevante vira linha em `06-reunioes/assessoria-assincrona.md`: data, quem perguntou, o que foi perguntado, classificacao, o que foi respondido, se gerou acao.

Demanda que revele bloqueio → linha em `PENDENCIAS.md` com dono e prazo.
Demanda classificada como mudanca de estrategia → entra na pauta do proximo comite no `06-reunioes/`.

## Controle de SLA

Registre `recebido_em` e `respondido_em` em horas uteis. Estouro de SLA e um fato contratual: registre, nao suavize. Ver `PENDENCIAS.md`.
