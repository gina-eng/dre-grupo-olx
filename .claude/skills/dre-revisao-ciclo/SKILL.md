---
name: dre-revisao-ciclo
description: "Fecha o ciclo de 90 dias: revisao de aprendizados (Manter/Ajustar/Abandonar), revisao do forecast previsto vs. realizado com classificacao de desvios, e definicao da nova restricao. Use quando o operador disser /dre-revisao-ciclo ou 'fechar o ciclo' ou 'revisao de aprendizados' ou 'previsto vs realizado'."
dependencies:
  - dre-comite
tools: []
fase: "5, Recomecar"
estimated_time: "4h"
output_file: "dre-revisao-ciclo.json"
---

# DR-E · Revisao de Ciclo

POP exclusivo do Ciclo 2+. Transforma o forecast de projecao teorica em **ferramenta de decisao baseada em evidencia**. Ver `00-playbook/06-pops-ciclo-2.md`.

## Parte 1 · Revisao de Aprendizados

Classifique **cada** iniciativa do plano anterior:

| Classificacao | Criterio |
|---|---|
| **Manter** | Gerou o efeito previsto na etapa da restricao, com evidencia |
| **Ajustar** | Direcao certa, execucao ou calibragem errada |
| **Abandonar** | Hipotese refutada, ou custo maior que o retorno |

Regra: **nada fica sem classificacao.** Iniciativa "em andamento" no fim do ciclo e `Ajustar` com prazo novo, ou `Abandonar`, nao um terceiro estado indefinido.

Para cada uma registre: o que se aprendeu que nao se sabia no inicio do ciclo. Se a resposta for "nada", a iniciativa provavelmente nao era um teste de hipotese.

## Parte 2 · Revisao do Forecast (previsto vs. realizado)

| Metrica | Leitura esperada |
|---|---|
| **Volume** (leads, oportunidades, volume na etapa da restricao) | Volume menor que o previsto pode indicar falha de geracao ou capacidade limitada **anterior** a restricao |
| **Taxas de conversao** (por etapa; foco na restricao) | Conversoes abaixo do previsto indicam falha de execucao ou hipotese incorreta no diagnostico |
| **Tempo de ciclo** (por etapa e total) | Aumento de tempo indica acumulo ou ineficiencia, sinal classico de restricao ativa |
| **Capacidade da restricao** (maximo processado / utilizacao) | **Metrica mais critica.** Abaixo do limite → ha espaco de otimizacao. No limite → sinal de necessidade de expansao |
| **Receita gerada** (prevista vs. realizada, ticket medio) | Desvio aqui e **consequencia** das outras, nunca causa isolada |
| **Perdas no fluxo** (drop-off por etapa) | Perdas acima do previsto indicam novas oportunidades de otimizacao |

### Classificacao obrigatoria de cada desvio relevante

| Categoria | Significado |
|---|---|
| **Erro de execucao** | Plano correto, execucao falha |
| **Erro de hipotese** | Premissa do forecast incorreta |
| **Limite estrutural** | Sistema atingiu capacidade maxima |

Essa classificacao **direciona a decisao do Comite**. Nao pule: sem ela, a discussao vira opiniao sobre quem errou.

### Conclusao obrigatoria: uma das tres, explicita

1. **Continuar otimizando**: ha espaco interno na restricao atual
2. **Expandir**: restricao saturada, precisa de recurso novo
3. **Ajustar estrategia**: erro de hipotese relevante, volta ao diagnostico

## Parte 3 · Nova restricao

Com o fluxo de receita atualizado (rode `/dre-fluxo-receita` com os dados do ciclo encerrado):

- Onde o fluxo desacelera **agora**?
- A trava anterior foi `resolvida`, `parcialmente_resolvida` ou `nao_resolvida`?
- A nova restricao tem o mesmo rigor de validacao do Comite 1? (CRT, poder explicativo, evidencia)

> **Nao troque de restricao sem base solida.** O gate do Comite 3 reprova troca de restricao apoiada em percepcao, exige-se evidencia longitudinal, a evolucao real do sistema ao longo do ciclo.

## Parte 4 · Novo plano de 90 dias

Rode `/dre-plano-90-dias` para o proximo ciclo, ja orientado a nova restricao, para que a continuidade seja imediata e nao dependa de reinterpretacao depois.

## Output

Salve `dados/outputs/dre-revisao-ciclo.json` seguindo `.claude/shared-templates/PADRAO-OUTPUT.md` mais:

- `ciclo_encerrado`, `janela`
- `aprendizados[]`: iniciativa, classificacao (`manter|ajustar|abandonar`), evidencia, aprendizado, decisao
- `execucao_pct`: quanto do plano foi executado (referencia: acima de 80% e o indicador de qualidade do metodo)
- `previsto_vs_realizado[]`: metrica, previsto, realizado, desvio_pct, classificacao (`erro_execucao|erro_hipotese|limite_estrutural`), leitura
- `capacidade_restricao`: `utilizacao_pct`, `saturada` (boolean)
- `conclusao`: `continuar_otimizando | expandir | ajustar_estrategia` + justificativa
- `trava_anterior`: `resolvida | parcialmente_resolvida | nao_resolvida`
- `nova_restricao`: trava, evidencia_longitudinal, validada_por
- `roi_ciclo`: investimento, throughput adicional, leitura

## Finalizacao

1. Salve `dados/outputs/dre-revisao-ciclo.json`
2. Atualize `dados/client.json`: `meta.ciclo_atual`++, `meta.fase_atual` = "Identificar", `restricao_identificada`, `progress.skills` reiniciado para o novo ciclo, version++, `history[]`
3. Escreva a versao humana em `05-resultados/ciclo-{n}-revisao.md`
4. Sugira `/dre-plano-90-dias` para o novo ciclo, e `/dre-matriz-gp` antes do proximo comite
