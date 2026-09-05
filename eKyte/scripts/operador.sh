#!/usr/bin/env bash
#
# Define quem está operando o eKyte NESTA máquina.
#
# O token do MCP identifica a pessoa, não só a empresa: quem cria tarefa com o token
# do Rafael aparece no eKyte como Rafael. Este script escreve o .mcp.json com o token
# de quem vai operar e grava o slug em .operador, para a sessão saber quem esperar.
#
# Uso:  ./scripts/operador.sh            (pergunta)
#       ./scripts/operador.sh rafael     (direto)
#
set -euo pipefail

raiz="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tokens="$raiz/tokens.json"

if [[ ! -f "$tokens" ]]; then
  echo "erro: $tokens não existe."
  echo
  echo "  cp '$raiz/tokens.exemplo.json' '$tokens'"
  echo
  echo "Depois abra o arquivo e cole o seu token. Ele é gitignored — não vai pro repo."
  exit 1
fi

# Duas checagens separadas de propósito: JSON quebrado e JSON válido mas com estrutura
# errada dão mensagens muito diferentes, e a causa mais comum é vírgula sobrando no último
# item — que o jq reporta como "expected another key-value pair", fácil de ler errado.
if ! erro="$(jq -e . "$tokens" 2>&1 >/dev/null)"; then
  echo "erro: $tokens não é um JSON válido."
  echo "  $erro"
  echo
  echo "Causa mais comum: vírgula sobrando depois do último token. JSON não aceita."
  exit 1
fi

if [[ "$(jq -r '.tokens | type' "$tokens")" != "object" ]]; then
  echo "erro: $tokens não tem o objeto 'tokens'. Compare com tokens.exemplo.json."
  exit 1
fi

slug="${1:-}"

if [[ -z "$slug" ]]; then
  echo "Quem vai operar o eKyte nesta máquina?"
  echo
  jq -r '.tokens | to_entries[] |
    "  \(.key)" + (if (.value | length) == 0 or (.value | startswith("COLE-"))
                   then "   (sem token — preencha em tokens.json)" else "" end)' "$tokens"
  echo
  read -r -p "slug: " slug
fi

token="$(jq -r --arg s "$slug" '.tokens[$s] // empty' "$tokens")"

if [[ -z "$token" ]]; then
  echo "erro: '$slug' não está em tokens.json."
  echo "Slugs disponíveis: $(jq -r '.tokens | keys | join(", ")' "$tokens")"
  exit 1
fi

if [[ "$token" == COLE-* ]]; then
  echo "erro: '$slug' ainda está com o placeholder em tokens.json."
  echo "Cole o token de verdade e rode de novo."
  exit 1
fi

# tokens.json guarda a URL inteira em algumas máquinas e só o token em outras. Sem
# normalizar, a concatenação abaixo gera "...token=https://...token=<hex>" — que o eKyte
# aceita e responde como anônimo, sem erro visível, e a autoria se perde em silêncio.
token="${token##*token=}"

if [[ ! "$token" =~ ^[0-9a-f]{64}$ ]]; then
  echo "erro: o token de '$slug' não tem o formato esperado (64 hex)."
  echo "Cole em tokens.json a URL do eKyte inteira ou só o token — as duas formas servem."
  exit 1
fi

jq -n --arg t "$token" '{
  mcpServers: {
    ekyte: {
      type: "http",
      url: ("https://api.ekyte.com/mcp?token=" + $t)
    }
  }
}' > "$raiz/.mcp.json"

printf '%s\n' "$slug" > "$raiz/.operador"

echo "ok — o eKyte desta máquina passa a operar como '$slug'."
echo
echo "1. REINICIE a sessão do Antigravity. O token do MCP só é lido na abertura."
echo "2. Na primeira ação, o Claude confirma com get_current_user se bate com '$slug'."
echo "   Se não bater, o token está trocado — pare e corrija antes de criar qualquer coisa."
