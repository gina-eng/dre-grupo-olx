#!/usr/bin/env python3
"""
PreToolUse guard da pasta eKyte.

Bloqueia a criacao de apontamento de horas enquanto o EXECUTOR REAL nao estiver
declarado no campo `comment`. Existe porque `create_time_tracking` nao tem campo
de usuario: o executor do apontamento vem do TOKEN, nao do executorId da tarefa.
Sem isso, hora de uma pessoa entra na produtividade de outra, e nao ha delete no MCP.

Libera silenciosamente qualquer outra chamada.
"""
import json
import os
import re
import sys

MARCADOR = re.compile(r"executor\s+real\s*:\s*\S", re.IGNORECASE)
AQUI = os.path.dirname(os.path.abspath(__file__))
EXECUTORES = os.path.join(AQUI, "..", "referencia", "executores.md")


def libera():
    sys.exit(0)


def nega(motivo):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": motivo,
        }
    }, ensure_ascii=False))
    sys.exit(0)


def pessoas():
    """Nomes da tabela de executores.md, para a pergunta ser objetiva."""
    try:
        with open(EXECUTORES, encoding="utf-8") as fh:
            linhas = fh.read().splitlines()
    except OSError:
        return []
    achados = []
    for linha in linhas:
        m = re.match(r"^\|\s*`([a-z]+)`\s*\|\s*([^|]+?)\s*\|", linha)
        if m:
            achados.append("%s (%s)" % (m.group(2).strip(), m.group(1)))
    return achados


def main():
    try:
        evento = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        libera()

    nome = evento.get("tool_name") or ""
    entrada = evento.get("tool_input") or {}

    if nome.endswith("create_time_tracking"):
        carga = entrada.get("comment") or ""
    elif nome == "Bash":
        cmd = entrada.get("command") or ""
        if "create_time_tracking" not in cmd:
            libera()
        carga = cmd
    else:
        libera()

    if MARCADOR.search(carga):
        libera()

    lista = pessoas()
    quem = ("\n\nExecutores possiveis:\n  - " + "\n  - ".join(lista)) if lista else ""

    nega(
        "APONTAMENTO BLOQUEADO: o executor real nao esta declarado.\n\n"
        "`create_time_tracking` nao tem campo de usuario. O executor do apontamento "
        "vem do TOKEN carregado nesta sessao, NAO do executorId da tarefa. Se o token "
        "nao for da pessoa que fez o trabalho, a hora entra na produtividade errada "
        "-- e nao existe delete no MCP para corrigir.\n\n"
        "Antes de repetir a chamada, faca DUAS coisas:\n"
        "1. Chame get_current_user e diga em voz alta de quem e o token.\n"
        "2. Pergunte de forma objetiva QUEM EXECUTOU a tarefa e espere a resposta. "
        "Nao deduza pelo executorId, nem pelo .operador, nem por quem pediu."
        + quem +
        "\n\nCom a resposta em maos, inclua no campo `comment` a linha:\n"
        "    Executor real: <nome da pessoa>\n\n"
        "Se o token nao for dessa pessoa, diga isso ao usuario antes de criar."
    )


if __name__ == "__main__":
    main()
