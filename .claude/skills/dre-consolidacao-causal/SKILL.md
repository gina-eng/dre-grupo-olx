---
name: dre-consolidacao-causal
description: "Consolida os scores das 8 travas, aplica a regra de Goldratt e determina a trava governante (restricao) com a hipotese causal em formato de politica implicita. Use quando o operador disser /dre-consolidacao-causal ou 'qual e a restricao' ou 'consolidar as travas'."
dependencies:
  - dre-diagnostico-trava
tools: []
fase: "1, Identificar"
estimated_time: "3h"
output_file: "dre-consolidacao-causal.json"
---

# DR-E · Consolidacao Causal

Voce vai transformar 8 diagnosticos isolados em **uma leitura de sistema**: qual trava governa o throughput hoje, e sob que politica implicita ela se sustenta.

## Pre-condicoes

- As 8 travas com score em `dados/client.json` → `travas`. Trava sem score bloqueia a consolidacao.
- `dados/outputs/dre-fluxo-receita.json` fechado, com receita derivada batendo com a declarada.
- Se alguma trava esta com `confiabilidade: "baixa"`, a consolidacao sai com ressalva explicita, nunca silenciosamente.

## Passo 1 · Tabela consolidada

Monte a tabela dos 8 scores, ordenada de baixo para cima no funil (Retencao primeiro):

| Trava | Score | Interpretacao | Perda absoluta associada | Confiabilidade |
|---|---|---|---|---|

A coluna de **perda absoluta** vem do `ranking_perda[]` do fluxo de receita. Score baixo em etapa de volume pequeno vale menos que score medio em etapa de volume grande, o sistema perde onde ha massa.

## Passo 2 · Regra de Goldratt

Investigue **de baixo para cima**: Retencao → Decisao → Compromisso → Qualificacao → Interesse → Atencao → Exposicao.

Motivo: uma trava a jusante contamina a leitura de tudo que esta a montante. Se a Decisao esta quebrada, gerar mais Exposicao so aumenta o custo do desperdicio, e faz a Exposicao **parecer** o problema, porque o volume nao vira receita.

Regra pratica: **a trava governante e a mais baixa no funil que ainda esta estruturalmente travada (0–15)**. Se as travas de baixo estao fortes (21–25) com evidencia formal, suba.

## Passo 3 · Teste de poder explicativo

Uma trava so e **potencial governante** se passar nos tres testes:

1. **Explica a maioria dos sintomas observados**: liste os sintomas confirmados de todas as travas e marque quais essa causa explica. Se explica menos da metade, nao e ela.
2. **Resolve-la aumenta o throughput mais do que atacar qualquer outra**: quantifique: qual receita adicional em 12 meses se essa etapa fosse para o benchmark. Compare com as demais.
3. **Nao ha hipotese concorrente com maior poder explicativo**: nomeie a segunda colocada e diga por que perde.

Registre os tres testes por escrito. Comite vai perguntar.

## Passo 4 · Politica implicita

Consolide as hipoteses causais das travas individuais em **uma** frase de sistema:

> "A empresa opera sob a politica implicita de **____**, o que gera **____**, limitando **____**."

Criterios:
- A politica e uma escolha estrutural, muitas vezes nao declarada e as vezes racional na epoca em que surgiu.
- Nunca "as pessoas nao fazem", nunca "falta processo" generico. Falta de processo e efeito; a politica e o que faz a organizacao aceitar essa falta.
- A frase precisa ser reconhecivel pelo cliente. Se o decisor le e nao se reconhece, ou esta errada ou esta mal escrita.

## Passo 5 · Ressalvas e proxima etapa

Declare explicitamente:
- O que ficou sem dado e como isso afeta a confianca no veredito
- Se a hipotese do cliente (`briefing.hipotese_cliente`) coincide ou diverge do achado, e, se diverge, qual evidencia sustenta a divergencia
- Que a determinacao e **preliminar**: a validacao final acontece na CRT (`/dre-udes-crt`)

> Divergencia entre a hipotese do cliente e o achado nao e problema, e o valor do produto. Mas precisa ser apresentada com evidencia, nao com opiniao.

## Output

Salve `dados/outputs/dre-consolidacao-causal.json` seguindo `.claude/shared-templates/PADRAO-OUTPUT.md` mais:

- `tabela_consolidada[]`: trava, score, interpretacao, perda_absoluta, confiabilidade
- `ordem_investigacao[]`: sequencia Goldratt aplicada, com o que foi descartado e por que
- `restricao`: `trava`, `score`, `justificativa`
- `testes_poder_explicativo`: `sintomas_explicados`, `throughput_potencial`, `hipotese_concorrente`
- `politica_implicita`: `politica`, `efeito`, `limitacao`, `frase_completa`
- `divergencia_hipotese_cliente`: boolean, `hipotese_cliente`, `evidencia`
- `ressalvas[]`
- `preliminar`: sempre `true`

## Finalizacao

1. Salve `dados/outputs/dre-consolidacao-causal.json`
2. Atualize `dados/client.json`: `restricao_identificada`, `consolidacao_causal`, version++, `history[]`
3. Escreva a versao humana em `02-diagnostico/consolidacao-causal.md`
4. Sugira `/dre-impulso-controlado` para confirmar a restricao no mundo real antes de partir para o LTP
