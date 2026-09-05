---
name: operador
description: Descobre e confirma quem esta operando o eKyte nesta maquina, e detecta quando o token carregado e o da conta generica (gina@v4company.com), caso em que a autoria se perde. Use ao configurar a pasta, ao trocar de operador, e antes da primeira escrita de cada sessao.
---

# Quem está operando o eKyte

Duas coisas que tornam essa pergunta necessária:

1. **O token do MCP identifica a pessoa.** Tarefa criada com o token do Rafael nasce como
   criada pelo Rafael. O eKyte preenche `createById` a partir do token e **não há tool MCP
   que corrija autoria depois**.
2. **O login do Antigravity é compartilhado.** A squad usa `gina@v4company.com`, então a
   sessão **não sabe quem está digitando**. Nunca deduza a pessoa do login.

## Passo 1 — Quem o token realmente é

Chame `get_current_user`. É a única fonte confiável — `.operador` é declaração, isto é fato.

### Se responder "Regina Operações" (gina@v4company.com), pare

É a **conta genérica**. Tudo criado nessa sessão nasce sem autor real, e não dá para consertar
depois. Não crie, não atualize, não conclua nada. Diga:

> O token carregado é o da conta genérica, não o de uma pessoa. Qualquer tarefa criada agora
> ficaria sem autor de verdade. Rode `./scripts/operador.sh <seu-slug>` e reinicie a sessão.

Só siga se a pessoa reafirmar que quer mesmo gravar na conta genérica — aí é decisão dela,
mas registre no `Solicitante` do briefing quem pediu de verdade.

**Exceção em vigor, agora só para o `japa`:** desde 2026-09-02, `rafael`, `leonardo`,
`anselmo`, `guilherme` e `robson` têm token — ver
[CLAUDE.md](../../../CLAUDE.md#transição--5-dos-6-tokens-chegaram-conferido-em-2026-09-02).
Para esses cinco, divergência de operador **volta a parar a sessão**: quem vai escrever troca
para o próprio token antes. Só o `japa` (Henrique Nohama) segue sem, e aí vale avisar e seguir.

Confira também `companyId == 18239` ("V4 Company | Flagship"). Token de outra empresa não
enxerga os workspaces da squad.

## Passo 2 — Bate com o que a máquina declarou?

Leia `.operador` — arquivo de uma linha com o slug, escrito por `./scripts/operador.sh`.
Compare com a linha correspondente em [referencia/executores.md](../../../referencia/executores.md).

- **Não existe `.operador`** — ninguém configurou esta máquina. Vá para
  [Trocar de operador](#trocar-de-operador).
- **Não bate com o `get_current_user`** — pare. Alguém trocou o token sem rodar o script, ou
  o slug está apontando para o token de outra pessoa. Diga qual usuário o token realmente é e
  qual a máquina declarou.
- **O slug está em `executores.md` sem `executorId`** — a pessoa ainda não existe como usuário
  no eKyte, ou a tabela não foi preenchida. Avise: ela pode operar, mas não pode receber fase.

**Nunca leia `tokens.json`.** Ele só interessa ao script.

## Passo 3 — Confirme com quem está ali

O login é compartilhado, então `.operador` pode ser de quem sentou naquela máquina antes.
Confirme em uma linha, sem transformar em interrogatório:

> Operando como **Rafael Corazza** — token pessoal, confere com `.operador`. É você?

Se a pessoa disser que não, vá para [Trocar de operador](#trocar-de-operador).

## Trocar de operador

Não dá para trocar no meio da conversa: o token vai na URL do servidor MCP e é lido **uma vez**,
quando a sessão abre. Instrua:

```
./scripts/operador.sh <slug>
```

e **reiniciar a sessão do Antigravity**. Sem reiniciar, o token velho continua valendo — e a
próxima tarefa nasce no nome errado, sem erro nenhum.

**Confira se o script mexeu no arquivo certo.** Ele escreve `eKyte/.mcp.json`, mas o servidor
`ekyte` também costuma estar em `~/.claude.json`, global da máquina — e é essa entrada que
vale quando a sessão abre com o repositório pai como raiz, não o `eKyte/`. Se as duas
divergirem, o script troca uma e a sessão lê a outra: a troca não acontece e nada avisa.
Compare os dois antes de reiniciar, sem imprimir o token:

```
python3 - <<'EOF'
import json, os, re
def tok(p, k=('mcpServers','ekyte','url')):
    d = json.load(open(os.path.expanduser(p)))
    for x in k: d = d[x]
    return re.search(r'token=([0-9a-f]+)', d).group(1)
a, b = tok('~/.claude.json'), tok('.mcp.json')
print('global', a[:8]+'…'+a[-4:], '| eKyte', b[:8]+'…'+b[-4:], '|', 'OK' if a == b else 'DIVERGEM')
EOF
```

Divergindo, alinhe a entrada global com a mesma URL do `.mcp.json` recém-gerado.

Se o slug ainda não tiver token, o script recusa e diz para colar em `tokens.json`. O token
pessoal sai do eKyte em **menu do usuário → Integrações → MCP**. Nunca ponha ali o token da
conta genérica.

## Executor ≠ autor

Se a pessoa perguntou "quem é o executor", provavelmente ela quer o `executorId` das fases,
não a autoria. São coisas diferentes:

- **autoria** é o token, resolvida aqui, uma vez por máquina, e a conta genérica **não serve**;
- **executor** é campo de cada entrada do `flow[]`, perguntado a cada tarefa pelo `/solicitar`,
  e aí a conta genérica **serve** como balde de fase sem dono.

A tabela de `executorId` está em [referencia/executores.md](../../../referencia/executores.md).
