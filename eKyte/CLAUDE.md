# eKyte — Squad Flagship

Esta pasta é compartilhada pelas 4 cadeiras da squad. Cada pessoa abre ela como projeto
no Antigravity. As regras abaixo valem para todas as sessões, em todas as máquinas.

## Regra dura: saber quem está operando antes de escrever

Duas coisas que tornam essa pergunta obrigatória:

1. **O token do MCP identifica a pessoa, não só a empresa.** Tarefa criada com o token do
   Rafael nasce como criada pelo Rafael, mesmo que quem esteja digitando seja outra pessoa. O
   eKyte preenche `createById` a partir do token, e **não há tool MCP que corrija autoria
   depois**.
2. **O login do Antigravity é compartilhado.** A squad inteira usa `gina@v4company.com`, então
   a sessão **não sabe quem está digitando**. Nunca deduza a pessoa do login — ele é o mesmo
   para todo mundo.

Por isso, **antes da primeira escrita de cada sessão** — `create_task`, `update_task`,
`create_project_from_template`, `update_workspace`, qualquer uma:

1. chame `get_current_user` — é a única fonte de fato;
2. leia `.operador` (uma linha, o slug de quem a máquina declarou) e compare;
3. confirme com quem está ali, numa frase: "operando como Rafael Corazza, é você?".

**Pare** se o `get_current_user` responder **Regina Operações** (é a conta genérica: a autoria
se perde), se não bater com o `.operador`, ou se a pessoa disser que não é ela. Nos três casos,
mande rodar `./scripts/operador.sh <slug>` e reiniciar a sessão.

Leitura (`list_*`, `get_*`) não precisa disso — só escrita.

### Transição — 5 dos 6 tokens chegaram; conferido em 2026-09-02

**Esta seção estava desatualizada.** Em 2026-09-02 o `tokens.json` desta máquina já tinha
token para `rafael`, `leonardo`, `anselmo`, `guilherme` e `robson` — só `japa` (Henrique
Nohama) segue com placeholder. Conferido pelo formato (64 hex), não pela identidade de cada
um: só o `get_current_user` da sessão prova de quem é o token.

Para os cinco, **o bloqueio da regra acima volta a valer sem exceção**: quem vai operar troca
para o próprio token e reinicia a sessão *antes* de escrever. Não é mais aceitável deixar a
autoria cair no Rafael por comodidade.

O procedimento de aviso abaixo vale **só para o `japa`**, enquanto o token dele não chegar:

1. diga em voz alta em quem a autoria vai cair: *"isso vai ser registrado como Rafael Corazza,
   porque seu token ainda não chegou"*;
2. pergunte quem está pedindo de verdade e **grave no `Solicitante` do briefing** — no
   interregno, é o único lugar onde a autoria real existe;
3. siga com a tarefa.

**Não silencie o aviso por repetição.** Ele vai aparecer em toda tarefa, e é o que impede a
squad de esquecer que os registros deste período não são confiáveis quanto a autoria.

Apague esta seção inteira quando o token do `japa` entrar no `tokens.json` — a partir daí o
bloqueio vale para todo mundo, sem exceção.

Trocar de operador **não acontece no meio da conversa**: o token vai na URL do servidor MCP e
é lido uma única vez, quando a sessão abre. Sem reiniciar, o token velho continua valendo e a
próxima tarefa nasce no nome errado, sem erro nenhum. A skill `/operador` conduz isso.

Isso resolve a **autoria**. O **executor** (`executorId` de cada fase do `flow[]`) é outra
coisa: é campo da chamada e é perguntado a cada tarefa, pelo `/solicitar`. Nunca assuma que
quem pediu é quem executa.

### Apontamento de horas também vem do token — verificado em 2026-08-17

`create_time_tracking` **não tem campo de usuário.** Os parâmetros são `workspaceId`,
`ctcTaskId`, `phaseId`, `startDate`, `endDate`, `type` e `comment` — nada sobre quem executou.
Mas `list_time_trackings` **filtra por `executorId`**: o registro tem executor, ele só não é
enviado. **Vem do token**, igual à autoria.

**Consequência:** a hora cai em quem é o dono do token, **não** no executor da tarefa. Ter o
Leonardo como `executorId` da fase não manda a hora para ele.

Confirmado na tarefa `10166907` (Santuá Confecções, KickOff): executor Leonardo Rosa,
apontamento criado com o token do Rafael → `list_time_trackings` devolve
`exec: Rafael Corazza`. O apontamento `12429833` é esse caso, e o comentário `12898714` da
tarefa é o único lugar que registra que quem fez a reunião foi o Leonardo.

Isso é **pior que o problema de autoria**, porque hora apontada é métrica de produtividade de
pessoa, não só um campo "criado por". Enquanto os 5 tokens não chegarem, **todo apontamento
feito via MCP infla o Rafael e zera os outros.** Ao apontar hora de outra pessoa: diga em voz
alta em quem a hora vai cair e registre o executor real num `create_task_comment`.

**Não existe delete no MCP.** Nenhuma das 94 tools apaga nada — não há `delete_time_tracking`.
Apontamento errado só se corrige na UI. Confirme antes de criar.

### A pergunta obrigatória: quem executou?

São **duas perguntas diferentes** e a segunda foi a que faltou nas tarefas de 17/08:

| pergunta | responde | quando |
|---|---|---|
| quem está **operando**? | `get_current_user` (o token) | 1x por sessão, antes da 1ª escrita |
| quem **executou** a tarefa? | **só a pessoa sabe — pergunte** | a cada apontamento |

**Nunca deduza quem executou.** Não pelo `executorId` da tarefa (é atribuição, não execução),
não pelo `.operador` (é o token da máquina), não por quem pediu. Pergunte de forma objetiva,
oferecendo a lista de [referencia/executores.md](referencia/executores.md), e espere a resposta.

Toda chamada de `create_time_tracking` leva no `comment` a linha:

```
Executor real: <nome da pessoa>
```

Isso não é burocracia — é o único lugar onde a execução real fica registrada enquanto o token
não for da pessoa certa. E se o token não for dela, **diga isso antes de criar**, não depois.

**Isso é obrigatório por hook, não por boa vontade.** `.claude/settings.json` roda
[scripts/guard-apontamento.py](scripts/guard-apontamento.py) em `PreToolUse` e **nega** a
chamada enquanto a linha `Executor real:` não estiver no `comment` — inclusive quando o
apontamento vai por `curl` no Bash em vez da tool MCP. O texto do bloqueio traz a lista de
pessoas e o que fazer. Para revisar ou desligar: `/hooks`.

**Onde a garantia NÃO vale:** o hook está em `eKyte/.claude/settings.json`, que só carrega
quando **esta pasta é a raiz do projeto**. Abrir a pasta pai como raiz desliga o hook (e o MCP
também, então a única via seria `curl` — exatamente o furo). Abra `eKyte/` como projeto.

### Não existe upload de arquivo no MCP

Há `list_artifacts` e `get_detailed_artifact`, mas **nenhum `create_artifact`**. Não se sobe
peça nem entrega por aqui. O que dá é **anexar arquivo que já está na biblioteca**, pelo campo
`artifacts` do `create_task_comment`. Subir arquivo novo é só na UI.

## Regra dura: só o fluxo `22597`

**A squad só usa tarefas e projetos do fluxo `[INTERNO] PADRÃO FLAGSHIP` (`22597`).**
Nada é criado, clonado ou puxado fora desse contexto. Decisão da squad em 2026-08-04, sem
exceção pendente.

Antes de qualquer `create_task`, **confirme o fluxo do tipo**: chame `get_task_type_flow` e
verifique `workflowId == 22597`. Se for outro, **não crie** — diga qual fluxo o tipo pertence
e peça o tipo equivalente no `22597`. O mesmo vale para `create_project_from_template`: se as
tarefas do modelo não forem do `22597`, não clone.

Isso não é preciosismo de organização. O tipo de tarefa **carrega o fluxo dele**: um tipo do
`14250` faz a tarefa nascer em fases como `Planejamento [CON]` (58770) ou `Config. Tráfego
[GT]` (30746), que a squad não opera. A tarefa fica válida no banco e invisível na operação.

**Por que a trava é necessária:** o seletor de tipo de tarefa avulsa oferece **1.217 tipos**,
e só **50** são do `22597`. Os outros 1.167 vêm de quatro fluxos da matriz — `14250` ([REDE]
Padrão V4, 1.025 tipos), `10940` (Onboarding, 90), `14560` ([REDE] Stack Digital, 28) e `7397`
(Padrão V4, 24). Todos pertencem à empresa `6953`, e **a Flagship não pode escondê-los**: não
existe `update_task_type` nem `update_workflow` no MCP, e a UI que os controla é da matriz.
Enquanto a rede não separar os catálogos, esta regra é a única barreira.

**Consequência aceita:** a squad **não tem nenhum modelo de projeto próprio** hoje
(`list_projects` com `isModel=1, createdBy=10` devolve vazio). Os 199 modelos de
[referencia/modelos-matriz.md](referencia/modelos-matriz.md) rodam no `14250` e portanto estão
**fora de uso**. Não há projeto utilizável até a squad montar os seus no `22597`.

## Regra dura: nunca criar tarefa fora do formato

**Toda** chamada de `create_task` usa o formato de [referencia/briefing.md](referencia/briefing.md)
no campo `description`. Não improvise estrutura, não resuma o template, não pule campos.

Antes de criar, leia esse arquivo. Ele é a fonte da verdade do briefing porque nenhum
tipo de tarefa tem formulário e a fase de Briefing está desligada — o `description` é o
único lugar onde o briefing existe.

**Não crie a tarefa se `Destino` estiver vazio ou genérico.** Vale para todos os tipos.

**`Mensagem central` trava a criação só nos tipos que produzem peça** — `86882`, `86891`,
`86890`, `86886`, `86885`. Em `86889`, `86888` e `86883` (otimização e traqueamento) não
existe peça nem mensagem: preencha `— NÃO SE APLICA —` e siga.

Nos tipos com peça, se a pessoa não souber responder, diga que o briefing não está pronto e
pare. Um briefing incompleto custa mais caro que uma tarefa não criada: não há copywriter
no meio do fluxo para corrigir direção de mensagem.

Campo sem resposta vai como `<p>— NÃO INFORMADO —</p>`. Nunca preencha por suposição.

## Como solicitar

Digite `/solicitar`. A skill conduz a entrevista, monta o `flow[]` e cria a tarefa.
Criar tarefa "na mão" conversando com o Claude é permitido, mas as regras acima continuam
valendo — a skill só garante que ninguém esqueça.

`/operador` diz com que token esta máquina está operando e confere se bate com a pessoa
declarada. Use ao configurar a pasta pela primeira vez, ou se desconfiar de que as tarefas
estão nascendo no nome errado.

## IDs fixos

- `companyId` = **18239** ("V4 Company | Flagship")
- `workflowId` = **22597** ("[INTERNO] PADRÃO FLAGSHIP"), publicado, `active=1`, `default=1`,
  `shared=1` — e mora na **empresa matriz da rede `6953`**, não na 18239. É fluxo
  compartilhado, herdado pela Flagship.
- Empresa matriz da rede = `6953`, dona dos fluxos compartilhados

**O fluxo `22584` ("[H2] PADRÃO FLAGSHIP") foi aposentado em 2026-08-03 15:50:** renomeado
para "INATIVO" e posto `active=0`. Todos os IDs de fase e de tipo daquele fluxo estão mortos.
Tarefa criada com eles é gravada no banco mas **não aparece na UI** — foi exatamente o que
aconteceu com a tarefa `10088755` em 2026-08-04, criada e depois cancelada.

Cuidado com uma armadilha de leitura: no retorno de `get_task_type_flow`, o objeto `workflow`
**aninhado** vem com `active:1` mesmo para fluxo desativado. Só o `get_detailed_workflow` diz
a verdade. Se for verificar se um fluxo está vivo, use `get_detailed_workflow`.

### Fases (`phaseId`)

16 fases — entrou `Execução Consultor [CN]` na posição 3, que não existia no fluxo antigo.

| seq | id | fase |
|---|---|---|
| 1 | 88690 | Briefing  [CN] |
| 2 | 88691 | Validação [CN] |
| 3 | 88705 | Execução Consultor [CN] |
| 4 | 88692 | Execução Criativo [DES] |
| 5 | 88693 | Execução Tráfego [GT] |
| 6 | 88694 | Execução Copy/Social [CONT] |
| 7 | 88695 | Aprovação Interna [CN] |
| 8 | 88696 | Aprovação Externa [CN] |
| 9 | 88697 | Alteração Criativo [DES] |
| 10 | 88698 | Alteração Tráfego [GT] |
| 11 | 88699 | Alteração Copy/Social [CONT] |
| 12 | 88700 | Aprovação Externa 2 [CN] |
| 13 | 88701 | Veiculação [GT] |
| 14 | 88702 | Publicação [CONT] |
| 15 | 88703 | Entrega [CN] |
| 16 | 88704 | Finalizado [CN] |

O `sequential` do `flowPhase` **não bate** com o `sequential` da `phase` (o flowPhase de
`88692` vem como 3, a phase como 4). O ordinal global é o da `phase` — é ele que está acima.

### Tipos de tarefa (`ctcTaskTypeId`)

O fluxo `22597` tem **~50 tipos**, não 9. Além dos de produção abaixo, entraram trilhas de
onboarding (kickoff, acessos, grupo com o cliente, reuniões de 1ª a 4ª semana), diagnóstico
(mídia paga, orgânico, CRO, maturidade digital, GMN, marketplace, PDV, e-commerce),
estratégia (Persona/ICP, SWOT, TAM/SAM/SOM, posicionamento, brandbook) e comercial (pipeline,
SDR AI-first, CRM, réguas de WhatsApp). Liste com `list_task_types_create_task` filtrando por
`workflowId == 22597` — a resposta é grande demais para o contexto, use `jq` sobre o arquivo.

Todos `allocationType=10` (Ágil). `estimatedTime` em minutos.

| id | tipo | estimatedTime | id no fluxo velho |
|---|---|---|---|
| 86882 | Campanha de Tráfego - Meta Ads | 210 | 86853 |
| 86881 | Campanha de Tráfego - Google Ads | 210 | 86854 |
| 86889 | Otimização de Campanha - Meta Ads | 60 | 86855 |
| 86888 | Otimização de Campanha - Google Ads | 60 | 86856 |
| 86891 | Troca de Criativo - Campanha | 80 | 86857 |
| 86890 | Planejamento de Conteúdo | 200 ou 260 | 86858 |
| 86886 | Elaboração Criativo Avulso | 110 | 86859 |
| 86883 | Configuração de Traqueamento | 75 | 86860 |
| 86885 | Criativos Social Media - Publicação | 135 | 86861 |

`86879` ("[INTERNO] PADRÃO FLAGSHIP (padrão)") é o stub padrão do fluxo — **não usar**.
(Equivale ao antigo `86828`.)

Os `estimatedTime` acima vêm das estimativas da squad, não do eKyte: os tipos do `22597` não
trazem `estimatedTime` na listagem. Só o `60` de Otimização é tempo real medido na rede.

### Cadeiras

Criativo/Design `[DES]` · Conteúdo `[CONT]` · Tráfego `[GT]` · Atendimento/CN `[CN]`

## Sempre ler o fluxo antes de criar

Nunca monte `flow[]` de cabeça. Chame `get_task_type_flow` com o `ctcTaskTypeId` e o
`workspaceId` para pegar as fases **ativas** do tipo naquele workspace. A UI pode ter
mudado desde a última vez que esta tabela foi atualizada.

`phaseId` da tarefa = primeira fase **ativa** do tipo. Hoje isso é `Validação` (88691),
porque `Briefing` (88690) continua `active=0`.

**Mande no `flow[]` só as fases ativas.** Testado em 2026-08-04: não é preciso enviar as 16
entradas com flags `active`. Três entradas ativas, com `sequential` 1..3 contíguo, gravam
certo.

Datas: calcule de trás para frente a partir de `currentDueDate`, em dias úteis.

## Projetos — modelos da matriz estão FORA DE USO

**Não clone modelo de projeto da matriz.** A regra do `22597` no topo deste arquivo vale
também para `create_project_from_template`. Os 199 modelos de
[referencia/modelos-matriz.md](referencia/modelos-matriz.md) montam as tarefas com tipos do
fluxo `14250`, não do `22597` — verificado no projeto de teste `QA_TesteProjeto` (320301), cujas
20 tarefas usam tipos como `43918`, `68989` e `69008`, todos do `14250`.

O arquivo de referência fica como **mapa de escopo** — serve para ler o que a rede entrega em
cada produto e inspirar o desenho dos nossos projetos. Não serve como fonte de clone.

Enquanto a squad não montar modelos próprios no `22597`, **não há projeto utilizável**.
`list_projects` com `isModel=1, createdBy=10` devolve vazio: nenhum modelo é nosso.

### Exceção autorizada: DR-E do Grupo OLX — 2026-09-02

A squad abriu **uma** exceção explícita à regra do `22597`, para clonar o modelo `290063`
(`[DR-E] Destrava Receita [Full Cycle]`, 66 tarefas, 145 dias, 5.130 min, criado por Leonardo
Rosa) no workspace do Grupo OLX. Autorizada pelo operador em 2026-09-02, ciente do que segue.

O modelo **é do `14250`**, verificado ao vivo e não por inferência:

| tipo | nome | `workflowId` |
|---|---|---|
| `67866` | Mapeamento do Fluxo de Receita | `14250` |
| `75422` | Realização do Comitê 1 - Validação e Otimização | `14250` |

As fases ativas desses tipos são `Execução [CON]` (58772), `Revisão [GP - Matriz]` (74166) e
`Revisão [C-LEVEL]` (74187) — fases da matriz, que a Flagship não opera. **É o custo aceito.**

Duas coisas que a exceção **não** resolve, e que ninguém deve descobrir de novo do zero:

- as 66 tarefas nascem **não planejadas**, como as 30 do Casa Flutuante. Não aparecem em
  `list_tasks`, `get_detailed_task` devolve `{}` e não há tool de planejamento — planejar
  segue sendo passo obrigatório de UI;
- **não há delete no MCP.** Projeto clonado errado só se corrige na UI.

O `[DR-E] CICLO 1` (`288916`, 40 tarefas, 73 dias) casaria melhor com o ciclo de 90 dias, mas
está **arquivado** (`active=2`). O `290063` é o único DR-E ativo — e vem com a descrição
trocada ("Destrava Receita OPERACIONAL") e o alias `dr-backup`. Corrija os dois no clone.

**Esta exceção não abre precedente.** Vale para o DR-E do Grupo OLX e mais nada; qualquer
outro clone fora do `22597` precisa de decisão nova da squad.

**Ainda não executada em 2026-09-02.** A sessão que autorizou operava com o token do Rafael e
parou antes de escrever, para que a criação nasça no nome do Leonardo — que é o responsável
pelo projeto e o autor do próprio modelo. Os parâmetros já apurados, para não refazer o
levantamento:

| passo | chamada | parâmetros |
|---|---|---|
| 1 | `create_workspace` | `name` "Grupo OLX" · `companyId` 18239 · `externalId` `grupo-olx` (casa com o slug do repo) · `access` 0 |
| 2 | `create_project_from_template` | `noFilterProjectId` 290063 · `workspaceId` <o do passo 1> · `name` "[DR-E] Grupo OLX" · `alias` `DRE-olx` · `startDate` `2026-08-24` · `description` reescrita (o modelo traz o texto do OPERACIONAL) |

`startDate` vem de `meta.inicio` do `dados/client.json` do repo DR-E. Não existe campo de
responsável em `create_project_from_template`: o `createdById` sai do token, então **operar
como `leonardo` já resolve** — não precisa de `update_project` depois. Se por qualquer motivo
a criação sair no nome errado, o `/createdById` do `update_project` é o campo a corrigir.

Achados dos testes de clone, que continuam valendo quando a squad montar os próprios modelos:

1. **`list_projects` devolve no máximo 75 registros, em ordem alfabética e sem offset.** A
   listagem padrão corta em "Implementação de E-commerce" e esconde 62% do catálogo. Nunca
   trate essa lista como completa — use o arquivo de referência ou particione por
   `responsibleId` + `textSearch`.
2. **Tarefa de projeto não é tarefa.** Ela nasce **não planejada**: tem `daysToStart` e
   `daysToComplete` relativos, não `currentDueDate`, e não aparece em `list_tasks` nem no
   Controle de Tarefas. Só entra na operação quando é planejada na UI — e **não há tool MCP
   para planejar**. O `description` vem vazio (sem briefing) e o `effort` é reescrito no clone.

## Pendências que afetam o uso

1. **7 usuários no eKyte: 6 pessoas + 1 conta genérica** — levantado em 2026-08-12, todos em
   `list_admin_editors_users`, todos podem receber fase. Regina Operações
   (`0a2c2fbd-f1ef-4f6c-882d-789180bd2eb2`, gina@v4company.com) **não é uma pessoa**: é a conta
   compartilhada da squad. Serve de `executorId` para fase sem dono, **nunca** de autor.
   Continuam **zero squads** e ninguém declara cadeira, então
   [referencia/executores.md](referencia/executores.md) tem a coluna como *a confirmar* e o
   `/solicitar` pergunta o executor de cada fase em vez de sugerir. Com 6 pessoas para 4
   cadeiras, o gargalo deixou de ser falta de gente e virou falta de declaração.
2. **Multi-token — mecanismo pronto em 2026-08-12, faltam 5 tokens.** `tokens.json` +
   `./scripts/operador.sh` + `.operador` já permitem cada pessoa operar com o próprio token
   (ver [Segurança](#segurança)), e os 6 já existem como usuário no eKyte. **Mas só o slug
   `rafael` tem token:** `leonardo`, `anselmo`, `guilherme`, `robson` e `japa` estão com
   placeholder. Até chegarem, quem operar grava como Rafael, e o campo `Solicitante` do
   briefing é a única forma de saber quem pediu de verdade — ver
   [Transição](#transição--desde-2026-08-12-só-o-rafael-tem-token).
3. **Briefing (88690) desligado** — decisão pendente: ligar a fase ou aceitar o `description`
   como briefing. Os tipos seguem sem formulário (`ctcTaskFormIds: []`), confirmado na tarefa
   `10089217`.
4. **Alteração (88697-88699), Aprovação Externa 2 (88700) e Entrega (88703) inativas** — não
   há caminho de retrabalho ativo. **Isso vale para os 9 tipos de produção, não para o fluxo
   todo:** o tipo de onboarding `86894` (KickOff) tem `Entrega [CN]` (88703) como **única**
   fase, e ativa — verificado em 2026-08-17 na tarefa `10166907`. Os tipos de onboarding,
   diagnóstico, estratégia e comercial têm fluxos curtos e próprios. Sempre
   `list_task_flow_phases` (parâmetro `taskId`, não `ctcTaskId`) em vez de assumir esta lista.
5. **`Elaboração Criativo Avulso` (86886) segue com Aprovação Externa (88696) ativa**, contra
   a decisão de que é peça interna sem aprovação do cliente. Verificado no fluxo novo em
   2026-08-04 — a migração herdou o problema.
6. **`Campanha de Tráfego - Google Ads` (86881) segue sem nenhuma fase de execução ativa**
   (Validação → Veiculação → Finalizado), assimétrico com Meta Ads. Também herdado.

As pendências 3 a 6 são do fluxo antigo e **foram copiadas tal e qual** para o `22597`. A
migração trocou os IDs e ampliou o catálogo de tipos, mas não corrigiu nenhuma delas.

## Segurança

O token do eKyte **não é versionado**. Três arquivos existem só na máquina de quem opera e
precisam estar no `.gitignore` **do repositório que hospeda esta pasta** — confira, não
presuma (ver [O incidente se repetiu](#o-incidente-se-repetiu--corrigido-em-2026-09-02)):

| arquivo | o que é |
|---|---|
| `tokens.json` | o registro `slug → token` da squad. **Nunca leia isso numa sessão** — só o script precisa dele. |
| `.mcp.json` | **gerado** por `./scripts/operador.sh` a partir do `tokens.json`. Não edite à mão. |
| `.operador` | uma linha com o slug de quem a máquina declarou. É por aqui que a sessão sabe quem esperar. |

Versionado, e sem token nenhum: `tokens.exemplo.json` (a estrutura),
[referencia/executores.md](referencia/executores.md) (nomes, cadeiras e `executorId`) e o
próprio `scripts/operador.sh`.

**Por que o `tokens.json` não vai pro git mesmo com o repo privado:** token commitado não sai
do histórico. Deletar o arquivo depois não adianta — qualquer clone antigo, ou o repo virando
público um dia, entrega todos eles de uma vez. O token viaja por fora (1Password, mensagem
direta); o que viaja pelo git é a estrutura.

### O incidente se repetiu — corrigido em 2026-09-02

A afirmação acima **era falsa neste repositório**, exatamente como no episódio de 2026-08-12
descrito no Histórico abaixo. Esta pasta não tem `.git` próprio: ela mora dentro de
`dre-grupo-olx`, e o `.gitignore` de lá não cobria nenhum dos três arquivos. Os cinco tokens
da squad estavam a um `git add .` de entrar no histórico para sempre.

Corrigido em 2026-09-02 com três linhas no `.gitignore` **do repositório pai** — não neste
diretório. Nada do `eKyte/` chegou a ser commitado (`git ls-files eKyte/` estava vazio).

**A lição, porque já falhou duas vezes:** esta pasta viaja para dentro de outros repositórios,
e o `.gitignore` que protege os tokens é o do repositório que a hospeda. Quem levar o `eKyte/`
para um repo novo confere com `git check-ignore -v eKyte/tokens.json` **antes** do primeiro
commit. Este arquivo dizer que está protegido não é evidência de nada.

### `tokens.json` guarda a URL inteira, não o token puro — 2026-09-02

Os cinco slugs preenchidos guardam `https://api.ekyte.com/mcp?token=<64 hex>` (96 chars), e não
os 64 hex sozinhos. O `scripts/operador.sh` concatenava `"…?token=" + $t` sem normalizar, o que
gerava `…token=https://…token=<hex>`. **O eKyte aceita essa URL e responde como anônimo, sem
erro nenhum** — a autoria se perderia em silêncio, que é o oposto do que o script existe para
garantir. Corrigido em 2026-09-02: o script agora aceita as duas formas e valida o formato
final (64 hex) antes de escrever.

### O `.mcp.json` desta pasta pode não ser o que a sessão lê

`operador.sh` escreve `eKyte/.mcp.json`. Mas o servidor `ekyte` também está declarado em
`~/.claude.json`, **global da máquina** — e é essa entrada que vale quando a sessão é aberta
com o repositório pai como raiz, e não o `eKyte/`. As duas guardavam o mesmo token do Rafael,
então a divergência ficou invisível até 2026-09-02.

**Consequência:** rodar `operador.sh <slug>` e abrir a sessão fora do `eKyte/` troca o arquivo
e não troca o token — a próxima tarefa nasce no nome errado, sem erro. Enquanto o script não
souber da entrada global, ao trocar de operador **atualize as duas** e confira com
`get_current_user` logo na abertura. É a única prova de quem é o token.

### Quem chega novo na squad

```
cp tokens.exemplo.json tokens.json     # cola o próprio token
./scripts/operador.sh <slug>           # gera o .mcp.json
```

e reinicia a sessão do Antigravity. Ninguém precisa do token de ninguém para a pasta funcionar.

**Histórico:** até 2026-08-12 o `.mcp.json` tinha o token do Rafael em texto puro e a pasta
não estava no `.gitignore` — este arquivo dizia o contrário, prometendo um `${EKYTE_TOKEN}`
que nunca existiu. O token nunca chegou a ser commitado (a pasta estava como `??`), mas
entraria no primeiro `git add`.
