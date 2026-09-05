# Executores da squad — de/para para `executorId`

Este arquivo é **versionado e não tem token nenhum**. Ele existe para três coisas:

1. resolver `executorId` na hora de montar o `flow[]` de uma tarefa;
2. dizer quais `slug` valem em `tokens.json` e em `./scripts/operador.sh`;
3. distinguir **pessoa** de **conta genérica** — que é o problema que este arquivo resolve.

Os tokens ficam em `tokens.json`, que é gitignored. Ver [Segurança](../CLAUDE.md#segurança).

## A conta genérica é o problema, não a solução

`gina@v4company.com` ("Regina Operações") **não é uma pessoa.** É a conta compartilhada com que
a squad loga, e várias pessoas a usam. Por isso a sessão do Antigravity **não sabe quem está
digitando** — o login é o mesmo para todo mundo. É daí que vem a necessidade de perguntar.

Isso divide o mundo em duas categorias, e a diferença importa:

| | vale como **autor**? | vale como **executor**? |
|---|---|---|
| token pessoal (`rafael`, `leonardo`, …) | **sim** — é o objetivo | sim |
| conta genérica (`Regina Operações`) | **não** — a autoria se perde | **sim** — serve de balde para fase sem dono |

Autor genérico é um registro errado que ninguém consegue corrigir depois. Executor genérico é
só uma fila de trabalho ainda não distribuída — chato, mas honesto.

### O sinal de alarme

Se `get_current_user` responder **Regina Operações**, o token carregado é o genérico:
tudo que for criado naquela sessão nasce sem autor real. **Pare antes de escrever** e mande
rodar `./scripts/operador.sh <slug>` com um slug pessoal, e reiniciar a sessão.

## Duas coisas diferentes que o pedido costuma juntar

| | vem de onde | dá para perguntar? |
|---|---|---|
| **Autoria** (`createById`) — quem *pediu* | do token do MCP, preenchido pelo eKyte sozinho | **não.** É decidido quando a sessão abre. Trocar exige `operador.sh` + reiniciar. |
| **Executor** (`executorId`) — quem *faz* | campo enviado em cada entrada do `flow[]` | **sim, sempre.** É a tabela abaixo. |

## Pessoas

`executorId` é o que vai no `flow[]`. `slug` é o que se digita em `operador.sh`.
Levantado em 2026-08-12 via `list_all_users_with_profile` + `list_admin_editors_users`.
**Os 7 aparecem em `list_admin_editors_users`, então todos podem receber fase.**

| slug | nome | e-mail | cadeira | perfil | `executorId` |
|---|---|---|---|---|---|
| `rafael` | Rafael Corazza | rafael.loureiro@v4company.com | *a confirmar* | 100 | `ddf738f9-8a2a-4687-8b8b-8d248504cffc` |
| `leonardo` | Leonardo Rosa | leonardo.rosa@v4company.com | *a confirmar* | 200 | `066621ed-b1ea-44cc-a3d5-e01ab3ef83fb` |
| `anselmo` | Anselmo Marangoni | anselmo.bueno@v4company.com | *a confirmar* | 200 | `93ec78dd-c4a6-4383-868f-f2e544884dcc` |
| `guilherme` | Guilherme Monteiro | guilhermemonteiro@v4company.com | *a confirmar* | 200 | `034524e2-5c7b-4c51-81bd-13a81fe1fa43` |
| `robson` | Robson Lopes | robson.lopes@v4company.com | *a confirmar* | 200 | `484d6efb-befb-4369-b4ca-e8797f17094f` |
| `japa` | Henrique Nohama | henrique.nohama@v4company.com | *a confirmar* | 200 | `df2ebed2-939d-4c52-ba96-bf79c7ef0853` |

`japa` é o único slug que não é o primeiro nome da pessoa — confirmado pela squad em
2026-08-12. Não deduza os outros por esse padrão: se aparecer um slug novo sem correspondente
óbvio, pergunte.

Atenção ao e-mail do Rafael: é `rafael.loureiro@`, não `rafael.corazza@`.

## Conta genérica — não usar como autor

| slug | nome | e-mail | uso |
|---|---|---|---|
| — | Regina Operações | gina@v4company.com | **só** `executorId` de fase sem dono: `0a2c2fbd-f1ef-4f6c-882d-789180bd2eb2` |

Ela **não tem slug em `tokens.json` de propósito.** Se tivesse, alguém acabaria operando com
ela e a autoria voltaria a se perder — que é exatamente o que este arquivo existe para impedir.

## O que ainda falta

**Executor está resolvido** — os 6 já podem receber fase. Faltam duas coisas, e elas são
independentes:

1. **Tokens** (bloqueia a **autoria**). Só o `rafael` tem token em `tokens.json`; os outros 5
   estão com placeholder. Cada pessoa pega o dela em **eKyte → menu do usuário → Integrações →
   MCP**, cola no `tokens.json` da máquina dela, roda `./scripts/operador.sh <slug>` e reinicia
   a sessão. Enquanto não chegarem, vale a
   [transição](../CLAUDE.md#transição--desde-2026-08-12-só-o-rafael-tem-token): avisa e segue.
2. **Cadeiras** (bloqueia a **sugestão automática** de executor). Ninguém declara cadeira no
   eKyte e não há squad cadastrada, então a coluna está como *a confirmar* e o `/solicitar`
   pergunta o executor de cada fase. Preenchida, ele passa a sugerir.

## As 4 cadeiras

O fluxo `22597` distribui as fases entre Criativo/Design `[DES]`, Conteúdo `[CONT]`, Tráfego
`[GT]` e Atendimento/CN `[CN]`. Nenhuma pessoa acima declara cadeira ainda, então o
`/solicitar` **pergunta o executor de cada fase** e marca com `⚠` toda fase que cair na conta
genérica. Não inventa usuário.

Com 6 pessoas para 4 cadeiras, o problema deixou de ser falta de gente e passou a ser falta de
**declaração**: o eKyte não sabe quem faz o quê, então a distribuição é manual a cada tarefa.

## Como distribuir um token novo

`tokens.json` é gitignored **de propósito**: token commitado não sai do histórico do git, nem
com o repo privado, nem depois de deletado o arquivo. Se um dia o repo vazar ou um notebook for
clonado, o histórico entrega todos eles.

Então o token viaja por fora: 1Password, mensagem direta, o que a squad usar. O que viaja pelo
git é a **estrutura** — este arquivo e `tokens.exemplo.json`. Quem chega copia o exemplo, cola
o próprio token e roda o script. Ninguém precisa saber o token de ninguém para a pasta funcionar.
