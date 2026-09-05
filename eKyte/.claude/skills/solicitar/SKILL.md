---
name: solicitar
description: Solicita uma tarefa no eKyte seguindo o fluxo [INTERNO] PADRÃO FLAGSHIP. Conduz a entrevista de briefing, monta o flow das fases e cria a tarefa. Use quando alguém da squad pedir um criativo, campanha, post, planejamento, otimização ou traqueamento.
---

# Solicitar tarefa no eKyte

## Passo 0 — Carregue o contexto

Leia [referencia/briefing.md](../../../referencia/briefing.md) **antes** de qualquer
pergunta. É o formato obrigatório do `description`. Não invente estrutura.

### Confira quem está operando

Chame `get_current_user` e compare com `.operador` e com
[referencia/executores.md](../../../referencia/executores.md). Detalhe em `/operador`.

Três motivos para **parar aqui**, antes da primeira pergunta da entrevista:

- **`get_current_user` responde "Regina Operações" (gina@v4company.com)** — é a conta genérica
  compartilhada. A tarefa nasceria sem autor de verdade e o MCP não corrige autoria depois.
- **Não bate com `.operador`** — alguém trocou o token sem rodar o script.
- **`.operador` não existe** — ninguém configurou esta máquina.

Nos três, mande rodar `./scripts/operador.sh <slug>` e reiniciar a sessão.
**Nunca abra `tokens.json`** — ele não tem nada que esta skill precise.

**Exceção em vigor:** enquanto durar a transição descrita em
[CLAUDE.md](../../../CLAUDE.md#transição--desde-2026-08-12-só-o-rafael-tem-token), não pare —
avise em quem a autoria vai cair, garanta o `Solicitante` correto no briefing e siga.

**Só existe um fluxo: `22597` ([INTERNO] PADRÃO FLAGSHIP).** Nenhuma tarefa é criada com tipo
de outro fluxo. O seletor do eKyte oferece 1.217 tipos, mas 1.167 são de fluxos da matriz —
esta skill é a barreira que impede que um deles entre por engano.

Se o usuário já descreveu o pedido na mensagem, use isso para pré-preencher e confirme
em vez de perguntar de novo o que já foi dito.

## Passo 1 — Entrevista

Pergunte em blocos curtos, não um questionário de 15 itens de uma vez. Ordem:

1. **Quem está pedindo** (nome e cadeira) e **para qual cliente**. O login do Antigravity é
   compartilhado pela squad, então **a sessão não sabe quem está digitando** — o
   `get_current_user` do Passo 0 diz de quem é o *token*, que pode ser de quem usou a máquina
   antes. Confirme numa linha: "pedido em nome de Rafael Corazza, certo?".

   Se a pessoa disser que não é ela, **pare** e mande trocar o operador — não siga registrando
   no nome errado. Se ela disser que está pedindo *por* outra pessoa, o `Solicitante` do
   briefing recebe o nome de quem pediu, mas a autoria no eKyte continua sendo a do token:
   diga isso em voz alta, não esconda.
2. **Que tipo de entrega é** — mostre os 9 tipos de produção do `CLAUDE.md` e deixe escolher.
   Se nenhum servir, o `22597` tem ~50 tipos (onboarding, diagnóstico, estratégia, comercial):
   liste com `list_task_types_create_task` filtrando `workflowId == 22597`. Nunca ofereça tipo
   de outro fluxo, mesmo que o nome pareça perfeito.
3. **Objetivo, Destino e Mensagem central** — os três que travam a criação
4. **Prazo** (`currentDueDate`)
5. Os campos do bloco extra do tipo escolhido

### Trave aqui

Não avance sem `Destino` concreto e `Mensagem central` preenchida.

`Destino` genérico é recusa: "acervo", "para ter", "depois vemos", "redes sociais" sem
dizer qual perfil e quando. Peça o nome da campanha, do conjunto, do perfil com data, ou
da reunião com o cliente.

Se a pessoa não sabe qual é a mensagem, diga que o briefing não está pronto e **pare**.
Não ofereça inventar. Não há copy no meio do fluxo para consertar depois.

Os outros campos podem ir como `— NÃO INFORMADO —`. Nunca preencha por suposição.

## Passo 2 — Resolva os IDs

```
list_short_workspaces          → workspaceId do cliente
get_task_type_flow             → fases ATIVAS do tipo nesse workspace
list_admin_editors_users       → executorId por cadeira
```

### Executor de cada fase — pergunte, não assuma

Quem **pede** não é quem **faz**. O solicitante vem do token; o `executorId` de cada entrada
do `flow[]` é escolha da pessoa, a cada tarefa.

Monte a lista de candidatos com [referencia/executores.md](../../../referencia/executores.md),
conferindo contra `list_admin_editors_users` (o arquivo pode estar defasado; a API manda).
Mostre as fases ativas com o executor proposto e deixe corrigir antes de criar:

```
Validação [CN]            → Rafael Corazza
Execução Criativo [DES]   → Regina Operações (genérica)   ⚠ cadeira sem dono
Finalizado [CN]           → Rafael Corazza
```

Marque com `⚠` toda fase que cair na conta genérica e diga isso com todas as letras. Como
**executor** ela é aceitável — é uma fila de trabalho ainda não distribuída, não um registro
falso. Como **autor** nunca é (isso é o Passo 0).

**Não invente usuário.** As 6 pessoas de `executores.md` têm `executorId` e podem receber fase
— o que falta é saber **a cadeira de cada uma**, que ninguém declarou. Por isso pergunte em vez
de sugerir, e não deduza cadeira pelo nome nem pelo histórico de quem executou parecido antes.

Sempre chame `get_task_type_flow` — não monte o `flow[]` a partir da tabela do
`CLAUDE.md`, que pode estar defasada em relação à UI.

### Trave aqui também — fluxo do tipo

O `get_task_type_flow` devolve `workflowId`. **Se não for `22597`, não crie a tarefa.**
Diga a que fluxo o tipo pertence e peça o equivalente no `22597`. Vale mesmo que a pessoa
insista: tipo de fluxo alheio faz a tarefa nascer em fases que a squad não opera, e ela some
da operação sem dar erro nenhum.

Confira também se o fluxo está vivo. O objeto `workflow` **aninhado** na resposta do
`get_task_type_flow` mente: vem com `active:1` mesmo para fluxo desativado. Na dúvida, use
`get_detailed_workflow`. Foi assim que uma tarefa nasceu órfã no fluxo morto `22584` em
2026-08-04.


## Passo 3 — Monte a chamada

`create_task` exige: `title`, `description`, `phaseDueDate`, `currentDueDate`,
`estimatedTime`, `workspaceId`, `executorId`, `phaseId`, `ctcTaskTypeId`, `situation`,
`flow`.

- `title` — `CLIENTE — entrega em 6 palavras`. Sem o nome do tipo, que já é campo.
- `description` — o HTML montado do template. Bloco comum + bloco do tipo.
- `phaseId` — primeira fase **ativa** do tipo (hoje `88691`, Validação, no fluxo `22597`).
- `situation` — `10` (Ativa)
- `estimatedTime` — da tabela do `CLAUDE.md`
- `flow` — uma entrada por fase ativa, com `phaseId`, `sequential` (ordem do fluxo),
  `executorId` da cadeira da fase, `active: 1`, `effort` em minutos, e `phaseDueDate`
  calculado de trás para frente a partir de `currentDueDate` em **dias úteis**.

## Passo 4 — Confirme antes de criar

Mostre um resumo em texto — **quem vai constar como autor** (o usuário do `get_current_user`,
não o slug), cliente, tipo, prazo, fases com executor e data, e o briefing renderizado em
markdown legível (não HTML cru). Pergunte se pode criar.

A linha do autor não é enfeite: é a última chance de alguém notar que está operando com o
token da pessoa errada antes de a tarefa existir.

Criar tarefa é ação que aparece no backlog de outras pessoas. Sempre confirme.

## Passo 5 — Crie e devolva

Depois de criar, informe o `taskId` e o link. Se der erro de validação, mostre o campo
que o eKyte recusou — não tente adivinhar e recriar em loop.

## Para múltiplos clientes ou datas

- Mesma tarefa em vários clientes → `workspaces` numa única chamada
- Vários posts do mesmo planejamento → `multipleDate: 1` + `multipleDateTasks`
- Tarefa recorrente (ex: Planejamento de Conteúdo mensal) → `recurring: 1` +
  `recurringFrequency: 50`, e `create_recurring_task` quando concluir

## Retorno de tarefa

Se o pedido for devolver uma tarefa e não criar: leia o `description` atual com
`get_detailed_task`, **acrescente** o bloco de retorno do `briefing.md` ao final e grave
com `update_task` (`/description`). Nunca sobrescreva o briefing original.
`Origem: Cliente | Interno` é obrigatório — é a métrica de taxa de defeito.
