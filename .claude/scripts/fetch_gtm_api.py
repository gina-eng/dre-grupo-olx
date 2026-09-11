#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fetch_gtm_api.py: inventario e versoes PUBLICADAS do GTM pela API.

ATENCAO, ESTE SCRIPT NUNCA RODOU. Escrito em 11/09/2026 e barrado antes do
primeiro uso: o consentimento OAuth do client ID padrao do gcloud foi bloqueado
pelo Google, entao o escopo tagmanager.readonly nao pode ser concedido por esse
caminho. Ver PENDENCIAS 26. A coleta seguiu manual, pelo guia de export. Quando
existir um client ID proprio da V4, este arquivo deve ser testado contra uma
conta so (--conta) antes de ser solto sobre as quatro.

Existe para substituir a coleta manual descrita em
02-diagnostico/guia-export-gtm.md, que pedia export a export pela interface do
Gerenciador de Tags. A API entrega as tres coisas que faltavam de uma vez:

  1. a lista de conteineres de cada conta, que era o gargalo dos lotes 3 e 5
     e dependia de print de tela;
  2. a versao LIVE de cada conteiner, ou seja, o que esta no ar, e nao o
     rascunho de workspace que os 15 exports de 01 e 11/09 trouxeram
     (`containerVersionId: 0`);
  3. o historico de versoes com data e autor, que era o print da aba Versoes
     pedido no lote 1.

O arquivo gravado imita o envelope do export da interface
(`exportFormatVersion`, `exportTime`, `containerVersion`), para que
check_gtm_exports.py continue lendo a pasta sem alteracao.

Credencial: ADC de gina@v4company.com, com escopo tagmanager.readonly. Sem esse
escopo a API devolve 403 ACCESS_TOKEN_SCOPE_INSUFFICIENT. Para conceder:

    gcloud auth application-default login --scopes=openid,\\
https://www.googleapis.com/auth/userinfo.email,\\
https://www.googleapis.com/auth/cloud-platform,\\
https://www.googleapis.com/auth/analytics.readonly,\\
https://www.googleapis.com/auth/tagmanager.readonly

Somente leitura. Nao publica, nao altera e nao cria workspace.

Uso:
    python3 .claude/scripts/fetch_gtm_api.py --listar
    python3 .claude/scripts/fetch_gtm_api.py --baixar
    python3 .claude/scripts/fetch_gtm_api.py --baixar --conta 6326134112
    python3 .claude/scripts/fetch_gtm_api.py --baixar --conteiner GTM-KGFGVFC
"""
import argparse
import datetime
import json
import pathlib
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RAIZ = pathlib.Path(__file__).resolve().parents[2]
PASTA = RAIZ / "assets" / "originais" / "H-rastreamento-gtm"
SAIDA = RAIZ / "dados" / "outputs"
INVENTARIO = SAIDA / "gtm-inventario.json"

# Mesma organizacao de check_gtm_exports.py: uma subpasta por conta.
SUBPASTA = {
    "94905": "conta-94905-br-olx-com-br",
    "6326134112": "conta-6326134112-checkout-unificado-pro",
    "4412254379": "conta-4412254379-vivareal",
    "2971905372": "conta-2971905372-zapimoveis",
}

BASE = "https://tagmanager.googleapis.com/tagmanager/v2"
PAUSA = 0.4          # a cota do GTM e apertada; melhor andar devagar que levar 429
TENTATIVAS = 5


def token():
    """Access token da ADC, pelo gcloud. Nunca e impresso."""
    try:
        bruto = subprocess.run(
            ["gcloud", "auth", "application-default", "print-access-token"],
            capture_output=True, text=True, check=True,
        )
    except FileNotFoundError:
        sys.exit("gcloud nao encontrado no PATH.")
    except subprocess.CalledProcessError as erro:
        sys.exit(f"gcloud nao devolveu token: {erro.stderr.strip()}")
    return bruto.stdout.strip()


class Api:
    def __init__(self):
        self.token = token()

    def get(self, caminho, **params):
        url = f"{BASE}/{caminho.lstrip('/')}"
        if params:
            url += "?" + urllib.parse.urlencode(params)
        espera = 1.0
        for tentativa in range(1, TENTATIVAS + 1):
            pedido = urllib.request.Request(
                url, headers={"Authorization": f"Bearer {self.token}"}
            )
            try:
                with urllib.request.urlopen(pedido, timeout=120) as resposta:
                    time.sleep(PAUSA)
                    return json.loads(resposta.read().decode("utf-8"))
            except urllib.error.HTTPError as erro:
                corpo = erro.read().decode("utf-8", "replace")
                if erro.code == 403 and "SCOPE_INSUFFICIENT" in corpo:
                    sys.exit(
                        "403: a credencial nao tem o escopo tagmanager.readonly.\n"
                        "Rode o gcloud auth application-default login do cabecalho "
                        "deste arquivo e tente de novo."
                    )
                if erro.code in (429, 500, 503) and tentativa < TENTATIVAS:
                    print(f"    {erro.code}, nova tentativa em {espera:.0f}s")
                    time.sleep(espera)
                    espera *= 2
                    continue
                raise RuntimeError(f"HTTP {erro.code} em {caminho}: {corpo[:400]}") from erro
        raise RuntimeError(f"desisti de {caminho} depois de {TENTATIVAS} tentativas")

    def paginado(self, caminho, campo, **params):
        """Junta as paginas de um list. O GTM pagina por nextPageToken."""
        itens, pagina = [], None
        while True:
            if pagina:
                params["pageToken"] = pagina
            dado = self.get(caminho, **params)
            itens.extend(dado.get(campo, []))
            pagina = dado.get("nextPageToken")
            if not pagina:
                return itens


def inventariar(api):
    """Contas, conteineres e historico de versoes de cada um."""
    contas = api.paginado("accounts", "account")
    print(f"contas visiveis: {len(contas)}\n")

    inventario = []
    for conta in contas:
        conta_id = conta.get("accountId")
        nome = conta.get("name", "?")
        conteineres = api.paginado(f"accounts/{conta_id}/containers", "container")
        print(f"{nome} ({conta_id}): {len(conteineres)} conteineres")

        registro = {
            "accountId": conta_id,
            "nome": nome,
            "conteineres": [],
        }
        for c in sorted(conteineres, key=lambda x: x.get("name", "")):
            caminho = c.get("path")
            versoes = []
            try:
                cabecalhos = api.paginado(
                    f"{caminho}/version_headers", "containerVersionHeader"
                )
                versoes = [
                    {
                        "containerVersionId": v.get("containerVersionId"),
                        "nome": v.get("name"),
                        "publicada": bool(v.get("deleted")) is False,
                    }
                    for v in cabecalhos[:10]
                ]
            except RuntimeError as erro:
                print(f"    versoes de {c.get('publicId')} indisponiveis: {erro}")

            ao_vivo = None
            try:
                vivo = api.get(f"{caminho}/versions:live")
                ao_vivo = {
                    "containerVersionId": vivo.get("containerVersionId"),
                    "nome": vivo.get("name"),
                    "tags": len(vivo.get("tag", [])),
                    "gatilhos": len(vivo.get("trigger", [])),
                    "variaveis": len(vivo.get("variable", [])),
                }
            except RuntimeError as erro:
                ao_vivo = {"erro": "sem versao publicada" if "404" in str(erro) else str(erro)[:200]}

            selo = (
                f"v{ao_vivo['containerVersionId']}, {ao_vivo['tags']} tags"
                if "erro" not in ao_vivo else f"SEM VERSAO PUBLICADA"
            )
            print(f"    {c.get('publicId'):14} {c.get('name', '?')[:44]:44} {selo}")

            registro["conteineres"].append({
                "publicId": c.get("publicId"),
                "containerId": c.get("containerId"),
                "nome": c.get("name"),
                "path": caminho,
                "usageContext": c.get("usageContext", []),
                "ao_vivo": ao_vivo,
                "ultimas_versoes": versoes,
            })
        inventario.append(registro)
        print()

    SAIDA.mkdir(parents=True, exist_ok=True)
    INVENTARIO.write_text(
        json.dumps(
            {
                "gerado_em": datetime.datetime.now().isoformat(timespec="seconds"),
                "fonte": "Tag Manager API v2, leitura por gina@v4company.com",
                "contas": inventario,
            },
            ensure_ascii=False, indent=2,
        ) + "\n",
        encoding="utf-8",
    )
    print(f"inventario em {INVENTARIO.relative_to(RAIZ)}")
    return inventario


def baixar(api, inventario, conta_alvo=None, conteiner_alvo=None):
    """Grava a versao publicada de cada conteiner no formato do export da interface."""
    PASTA.mkdir(parents=True, exist_ok=True)
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    baixados, pulados, sem_versao = 0, 0, []

    for conta in inventario:
        if conta_alvo and str(conta["accountId"]) != str(conta_alvo):
            continue
        for c in conta["conteineres"]:
            pid = c["publicId"]
            if conteiner_alvo and pid.upper() != conteiner_alvo.upper():
                continue
            if "erro" in c["ao_vivo"]:
                sem_versao.append(f"{pid} ({c['nome']})")
                continue

            destino_dir = PASTA / SUBPASTA.get(
                str(conta["accountId"]), f"conta-{conta['accountId']}-NAO-MAPEADA"
            )
            destino_dir.mkdir(parents=True, exist_ok=True)
            destino = destino_dir / f"{pid.lower()}_v{c['ao_vivo']['containerVersionId']}.json"
            if destino.exists():
                print(f"  ja existe: {destino.name}")
                pulados += 1
                continue

            versao = api.get(f"{c['path']}/versions:live")
            destino.write_text(
                json.dumps(
                    {
                        "exportFormatVersion": 2,
                        "exportTime": agora,
                        "containerVersion": versao,
                    },
                    ensure_ascii=False, indent=2,
                ) + "\n",
                encoding="utf-8",
            )
            print(f"  {destino.name}  ({len(versao.get('tag', []))} tags)")
            baixados += 1

    print(f"\nbaixados: {baixados} · ja existentes: {pulados}")
    if sem_versao:
        print(f"\nSEM VERSAO PUBLICADA ({len(sem_versao)}), o que e achado, nao falha de coleta:")
        for item in sem_versao:
            print(f"  {item}")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--listar", action="store_true", help="so inventaria, nao baixa")
    p.add_argument("--baixar", action="store_true", help="baixa as versoes publicadas")
    p.add_argument("--conta", help="restringe a um accountId")
    p.add_argument("--conteiner", help="restringe a um publicId, ex. GTM-KGFGVFC")
    args = p.parse_args()

    if not (args.listar or args.baixar):
        p.error("escolha --listar ou --baixar")

    api = Api()
    inventario = inventariar(api)

    if args.baixar:
        print("\nBAIXANDO VERSOES PUBLICADAS")
        baixar(api, inventario, args.conta, args.conteiner)
        print("\nConfira com: python3 .claude/scripts/check_gtm_exports.py")

    return 0


if __name__ == "__main__":
    sys.exit(main())
