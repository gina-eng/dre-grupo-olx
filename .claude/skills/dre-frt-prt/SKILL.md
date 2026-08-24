---
name: dre-frt-prt
description: "Valida a injecao pela Arvore da Realidade Futura, mapeia obstaculos na Arvore de Pre-Requisitos e produz a Arvore de Transicao (acoes na ordem logica). Use quando o operador disser /dre-frt-prt ou 'FRT' ou 'arvore da realidade futura' ou 'arvore de transicao'."
dependencies:
  - dre-udes-crt
tools: []
fase: "2 — Otimizar"
estimated_time: "4h"
output_file: "dre-frt-prt.json"
---

# DR-E — FRT, PRT e Arvore de Transicao

Tres etapas encadeadas: a injecao e testada (FRT), protegida contra o que pode impedi-la (PRT) e traduzida em sequencia executavel (Transicao).

> **Nenhuma solucao e considerada valida sem passar pela FRT.** Pular esta etapa e o modo mais comum de entregar um plano bonito que nao muda o sistema.

## Parte 1 — FRT (Arvore da Realidade Futura)

Estrutura: **injecao → efeitos intermediarios → efeitos desejados**.

1. Posicione a injecao na base.
2. Projete os primeiros efeitos no formato *SE (injecao) → ENTAO (efeito positivo)*. Cada seta e uma afirmacao logica, sujeita aos mesmos testes de suficiencia da CRT.
3. **Conecte aos UDEs.** Para **cada** UDE da CRT pergunte: *"Esse problema ainda existiria se a injecao fosse verdadeira?"*
   - Se nao existiria → conecte o UDE ao efeito desejado que o substitui.
   - Se ainda existiria → registre. UDE nao coberto e sinal de que a injecao e parcial, ou de que ha uma segunda causa-raiz.
   - Registre `cobertura_udes_pct`. Abaixo de ~70%, reabra a nuvem antes de seguir.
4. Expanda a cadeia ate alcancar os estados finais: previsibilidade, eficiencia, crescimento, escala.
5. **Identifique efeitos colaterais negativos.** *"Essa mudanca pode gerar novos problemas?"* Para cada um, defina a protecao (uma injecao complementar, um limite, um indicador de alerta). Efeito colateral previsto e gerenciavel; nao previsto vira crise no comite 2.
6. Validacao final: *"Se isso for verdade, o sistema passa a produzir os resultados desejados?"*

> "Aqui estamos vendo o sistema funcionando sob novas condicoes. Nao e previsao, e consequencia logica."

## Parte 2 — PRT (Arvore de Pre-Requisitos)

**Use somente quando ha obstaculos relevantes:** injecao estrutural ou complexa · resistencia do cliente · faltam recursos, pessoas ou sistema · a mudanca envolve varias areas · o cliente diz "nao da para fazer agora".

**Nao use** quando a injecao e simples, nao ha resistencia e a implementacao e direta — nesse caso va direto para a Transicao.

Estrutura: **injecao → obstaculos → condicoes necessarias para supera-los**.

| Obstaculo | Condicao necessaria |
|---|---|
| Time nao sabe fazer | Treinamento estruturado |
| Falta CRM | Sistema implementado |
| Faltam dados | Metricas definidas |

Levante os obstaculos com o time que vai executar, nao so com o decisor — quem executa conhece o atrito real. Valide: *"Se essas condicoes existirem, a implementacao fica viavel?"*

> "A solucao esta clara. Agora estamos garantindo que nada impeca ela de acontecer."

## Parte 3 — Arvore de Transicao

Onde o diagnostico vira plano executavel. Estrutura: **acao → efeito intermediario → novo estado do sistema**.

1. Posicione a injecao validada.
2. *"Qual e o primeiro movimento que precisa acontecer para isso se tornar possivel?"*
3. *"Se essa acao acontecer, o que passa a ser possivel que antes nao era?"*
4. Repita: Acao → Efeito → Nova condicao → Proxima acao.
5. **Teste a ordem.** Para cada passo: *"Se isso nao acontecer, o proximo passo ainda e possivel?"* Se a resposta for nao, a ordem esta correta. Se for sim, os dois passos sao paralelos — ou um deles e desnecessario.
6. Valide completude: *"Essa sequencia garante que a injecao se torne realidade?"*

Modelo de saida:

| # | Acao | Efeito intermediario | Novo estado | Pre-requisito (PRT) |
|---|---|---|---|---|

> "Aqui nao estamos listando tarefas. Estamos organizando a sequencia logica que faz o sistema mudar de estado."

## Output

Salve `dados/outputs/dre-frt-prt.json` com:

- `frt` — `injecao`, `nos[]`, `setas[]`, `udes_cobertos[]`, `udes_nao_cobertos[]`, `cobertura_udes_pct`, `efeitos_colaterais[]` (com `protecao`)
- `prt` — `aplicavel` (boolean + motivo), `obstaculos[]` com `condicao_necessaria`, `levantado_com`
- `transicao` — `passos[]` com `ordem`, `acao`, `efeito_intermediario`, `novo_estado`, `pre_requisitos[]`, `teste_ordem_ok`
- `validacao_cliente` — data, participantes, frase de confirmacao

## Checklist antes de fechar

- [ ] Todo UDE da CRT foi confrontado com a injecao
- [ ] Efeitos colaterais mapeados **com protecao definida**
- [ ] PRT aplicado (ou a nao-aplicacao justificada)
- [ ] Cada passo da Transicao passou no teste de ordem
- [ ] A Transicao, executada por completo, torna a injecao verdadeira

## Finalizacao

1. Salve `dados/outputs/dre-frt-prt.json`
2. Atualize `dados/client.json`, version++, `history[]`
3. Escreva a versao humana em `03-estrategia/frt-prt-transicao.md`
4. Sugira `/dre-plano-90-dias` — a Arvore de Transicao e o insumo direto do plano
