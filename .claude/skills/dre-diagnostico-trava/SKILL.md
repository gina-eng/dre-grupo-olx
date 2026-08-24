---
name: dre-diagnostico-trava
description: "Diagnostica UMA trava de receita nas duas camadas (analitica e experiencial), pontua as 5 dimensoes de 0 a 5, produz a entrada visual obrigatoria e a hipotese causal em formato de politica. Use quando o operador disser /dre-diagnostico-trava ou 'diagnosticar trava de X' ou 'pontuar a trava'."
dependencies:
  - dre-fluxo-receita
tools: []
fase: "1 — Identificar"
estimated_time: "3-4h por trava"
output_file: "dre-trava-{nome}.json"
---

# DR-E — Diagnostico de Trava

Voce vai diagnosticar **uma** trava de receita. Uma por execucao — misturar travas na mesma analise e o caminho mais rapido para um diagnostico raso.

Pergunte ao operador **qual trava** se ele nao disser. Se ele nao souber, leia `dados/outputs/dre-fluxo-receita.json` → `travas_prioritarias[]` e proponha a primeira.

## Travas validas

`cegueira` · `exposicao` · `atencao` · `interesse` · `qualificacao` · `compromisso` · `decisao` · `retencao`

Referencia canonica de sintomas, dimensoes e entrada visual: `references/dimensoes-por-trava.md` e `00-playbook/02-travas-de-receita.md`.

> **Regra de nomenclatura do projeto:** em qualquer material que chegue ao Grupo OLX, a trava e citada **pelo nome** ("Trava de Qualificacao"), nunca pelo numero — os documentos-fonte da V4 usam tres numeracoes conflitantes. Ver `PENDENCIAS.md`.

## Pre-condicao — Cegueira primeiro

Se a Trava de Cegueira ainda nao foi avaliada, avalie-a antes de qualquer outra. Cegueira nao e restricao de receita: e pre-condicao. Sem CAC, LTV, payback e distincao entre lead e cliente, todo score subsequente e achismo, e o output precisa declarar isso em `confiabilidade`.

## Camada 1 — Analitica

1. Identifique a fonte de dado de cada dimensao. Ferramentas por trava estao na secao 5 de `00-playbook/02-travas-de-receita.md`.
2. Puxe o dado real. Conforme a trava:
   - Midia: `bash .claude/scripts/v4mos_fetch.sh dados` ou `/ee-s2-diagnostico-midia`
   - Site/LP: `bash .claude/scripts/page_audit.sh dados {URL}`
   - Instagram organico: `/ee-s2-diagnostico-organico-ig`
   - Criativos: `/ee-s2-diagnostico-criativos`
   - Comercial/pre-vendas: `/ee-s4-diagnostico-comercial`
3. Compare com **duas** bases: benchmark do setor e historico da propria conta (12 meses). Uma metrica sem par de comparacao nao vira nota.
4. Registre o dado que **nao** conseguiu obter. Dimensao sem evidencia recebe nota `null`, nao nota baixa — e vira linha em `PENDENCIAS.md`.

## Camada 2 — Experiencial

Obrigatoria. Um score construido so com planilha nao sustenta comite.

| Modelo de venda | Validacao |
|---|---|
| Inside Sales / B2B | Cliente oculto: primeiro contato, qualificacao, proposta, follow-up, pos-venda (`/ee-s4-cliente-oculto`) |
| Vendas online | Jornada real ate o checkout, mapeando fricoes tela a tela |
| PDV | Visita presencial: abordagem, comunicacao visual, tempo de espera |

Registre data, canal, quem executou e o que aconteceu. Print, gravacao ou transcricao quando houver autorizacao.

## Passo 3 — Pontuar (0–25)

Cinco dimensoes, 0 a 5 cada. Regras de nota:

- **0** — nao existe. **1-2** — existe informalmente, sem processo. **3** — processo definido mas nao governado. **4** — governado com indicador. **5** — governado, medido e otimizado ciclicamente.
- **Nota acima de 3 exige evidencia formal** (documento, dashboard, processo escrito). Percepcao do time nao sustenta 4 ou 5. Isso vale sempre, e e explicitamente obrigatorio nas travas de **Compromisso** e **Retencao**.
- Toda nota precisa de **evidencia analitica E experiencial**. Se so tem uma das duas, a nota vem com `confiabilidade: "parcial"`.

| Total | Leitura |
|---|---|
| 0–10 | Estruturalmente travada. Alta probabilidade de ser a restricao. |
| 11–15 | Fragil. Vazamento relevante. |
| 16–20 | Funcional, com pontos de melhoria. |
| 21–25 | Forte e governada. |

## Passo 4 — Entrada visual obrigatoria

Cada trava tem um artefato visual que **precisa** existir para o comite. Ver a tabela em `references/dimensoes-por-trava.md`. Produza a tabela/estrutura de dados; o desenho final vai para o material do comite.

## Passo 5 — Hipotese causal

Feche com a frase no formato obrigatorio:

> "A empresa opera sob a politica implicita de **____**, o que gera **____**, limitando **____**."

Regras:
- A causa e uma **falha de estrutura, processo, definicao estrategica ou priorizacao** — nunca "as pessoas nao fazem".
- Exemplos validos: *"evitar investimento constante em midia"*, *"priorizar volume de leads em vez de qualidade"*, *"evitar pressao de fechamento"*.
- E **hipotese**. A validacao acontece na CRT (`/dre-udes-crt`), nunca aqui.

## Output

Salve `dados/outputs/dre-trava-{nome}.json` seguindo `.claude/shared-templates/PADRAO-OUTPUT.md` mais:

- `trava` — nome canonico
- `score_total` (0-25) e `interpretacao`
- `dimensoes[]` — `letra`, `nome`, `nota`, `evidencia_analitica`, `evidencia_experiencial`, `fonte`, `confiabilidade`
- `sintomas_confirmados[]` / `sintomas_descartados[]`
- `entrada_visual` — estrutura de dados do artefato obrigatorio
- `hipotese_causal` — `politica_implicita`, `efeito_gerado`, `limitacao`, `frase_completa`
- `potencial_governante` — boolean + justificativa
- `confiabilidade` — `alta | parcial | baixa`, com o que faltou

## Checklist antes de fechar

- [ ] Cegueira ja avaliada (ou esta e a Cegueira)
- [ ] Camada experiencial executada, com data e responsavel
- [ ] Toda nota > 3 tem evidencia formal citada
- [ ] Dimensao sem dado esta `null`, nao zero
- [ ] Entrada visual obrigatoria produzida
- [ ] Frase causal aponta politica, nao pessoa
- [ ] Dados faltantes viraram linha em `PENDENCIAS.md`

## Finalizacao

1. Salve `dados/outputs/dre-trava-{nome}.json`
2. Atualize `dados/client.json` → `travas.{nome}` (score, dimensoes, evidencias, `diagnosticado_em`), version++, `history[]`
3. Escreva a versao humana em `02-diagnostico/trava-{nome}.md`
4. Se ainda ha travas sem score, sugira a proxima pela ordem de Goldratt (baixo para cima). Se as 8 estao pontuadas, sugira `/dre-consolidacao-causal`
