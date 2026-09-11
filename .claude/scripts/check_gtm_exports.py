#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_gtm_exports.py: confere o lote de exports de contêiner do GTM.

Le todo .json em assets/originais/H-rastreamento-gtm/, extrai a identidade real
de dentro do arquivo (conta, contêiner, versao) e diz o que ainda falta contra
os lotes de 02-diagnostico/guia-export-gtm.md.

A distincao que o script existe para fazer: `containerVersionId: 0` e export de
espaco de trabalho, ou seja, rascunho em edicao. Qualquer outro numero e versao
publicada, que e o que esta no ar. Achado escrito sobre rascunho nao sustenta
afirmacao de producao em comite, e ate 11/09 os 11 exports do repositorio eram
todos rascunho.

Nao altera arquivo nenhum, a nao ser com --renomear.

Uso:
    python3 .claude/scripts/check_gtm_exports.py
    python3 .claude/scripts/check_gtm_exports.py --importar
    python3 .claude/scripts/check_gtm_exports.py --importar ~/Desktop
    python3 .claude/scripts/check_gtm_exports.py --renomear

--importar varre a pasta de downloads, traz o que ha de novo e deixa de fora o
que so repete o que ja esta aqui. Depois roda a conferencia normal.
"""
import hashlib
import json
import pathlib
import re
import shutil
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
PASTA = RAIZ / "assets" / "originais" / "H-rastreamento-gtm"
TELAS = PASTA / "telas"
ENTRADA = pathlib.Path.home() / "Downloads"

CONTAS = {
    "94905": "BR - www.olx.com.br",
    "6326134112": "Checkout Unificado - PRO",
    "4412254379": "VivaReal",
    "2971905372": "ZapImoveis",
}

# Os exports ficam em uma subpasta por conta. Com 60 conteineres numa pasta so,
# o nome do arquivo nao diz de qual das quatro contas ele e, e a identidade real
# esta dentro do JSON, longe demais para navegar de olho.
SUBPASTA = {
    "94905": "conta-94905-br-olx-com-br",
    "6326134112": "conta-6326134112-checkout-unificado-pro",
    "4412254379": "conta-4412254379-vivareal",
    "2971905372": "conta-2971905372-zapimoveis",
}


def pasta_da_conta(conta):
    """Subpasta de uma conta. Conta desconhecida cai numa pasta propria, visivel."""
    return PASTA / SUBPASTA.get(str(conta), f"conta-{conta}-NAO-MAPEADA")

# Conteineres nomeados de que precisamos da VERSAO PUBLICADA. Lotes 1, 4 e 5 do
# guia. Cada um ja tem achado escrito contra ele a partir do rascunho.
PUBLICADA_ESPERADA = {
    "GTM-KGFGVFC": ("94905", "Planos Profissionais & PAYG", "lote 1"),
    "GTM-546N2JV": ("94905", "Container Master", "lote 4"),
    "GTM-MXQKDG3": ("94905", "Seller Journey", "lote 4"),
    "GTM-M4TL57GX": ("94905", "Checkout", "lote 4"),
    "GTM-MJX9PG4": ("94905", "Conecta Autos", "lote 4"),
    "GTM-PZ733B5": ("2971905372", "ZapImoveis ANUNCIE", "lote 4"),
    "GTM-T2H3VFL": ("94905", "Google Shopping", "lote 5"),
    # Conta Checkout Unificado - PRO, enumerada por print em 11/09: sao quatro.
    "GTM-NGG9336B": ("6326134112", "Checkout Unificado - Master", "lote 2"),
    "GTM-K4WBMGQV": ("6326134112", "Checkout Unificado - OLX", "lote 2"),
    "GTM-NKSGWD6H": ("6326134112", "Checkout Unificado - Zap Imoveis", "lote 2"),
    "GTM-NRVS3M3D": ("6326134112", "Checkout Unificado - Viva Real", "lote 2"),
}

# Contas com muitos conteineres, confirmado pelo operador em 11/09. A coleta e em
# duas etapas: primeiro o print da lista de nomes, depois o export nominal do que
# a V4 selecionar. Exportar tudo nao cabe na janela que fecha em 15/09.
# Vazio desde 11/09: as quatro contas foram varridas e entregaram 60 conteineres.
# O inventario esta fechado, e o que falta nao e mais cobertura, e sim origem:
# nenhum dos exports e da versao publicada.
CONTAS_ABERTAS = {}

# Os pedidos de print de lista cairam em 11/09: o inventario das quatro contas
# veio por export, que e melhor que print. Sobra o que o export nao mostra.
PRINTS_ESPERADOS = [
    "aba Versoes do GTM-KGFGVFC, com data e autor das ultimas versoes (lote 1): "
    "diz desde quando o purchase esta preso ao gatilho errado, se estiver",
    "tela de Contas com as 4 contas, recebida em 11/09 e ainda nao salva na pasta",
]


def ler(caminho):
    """Devolve a identidade de um export, ou None se nao for um export de GTM."""
    try:
        dado = json.loads(caminho.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as erro:
        return {"arquivo": caminho, "erro": f"nao e JSON legivel: {erro}"}

    # Nem todo .json e objeto: uma varredura recursiva topa com lista, numero e
    # string, e nenhum deles responde a .get().
    if not isinstance(dado, dict):
        return {"arquivo": caminho, "erro": f"JSON de tipo {type(dado).__name__}, nao e export"}

    versao = dado.get("containerVersion")
    if not isinstance(versao, dict):
        return {"arquivo": caminho, "erro": "sem containerVersion: nao e export de conteiner"}

    conteiner = versao.get("container", {})
    bruto = versao.get("containerVersionId", "0")
    # A API devolve o id como string; workspace vem "0", versao publicada vem o numero.
    publicada = str(bruto) not in ("0", "None", "")

    return {
        "arquivo": caminho,
        "erro": None,
        "conta": str(conteiner.get("accountId", "?")),
        "public_id": conteiner.get("publicId", "?"),
        "nome": conteiner.get("name", "?"),
        "versao_id": str(bruto),
        "publicada": publicada,
        "exportado_em": dado.get("exportTime", "?"),
        "tags": len(versao.get("tag", [])),
        "gatilhos": len(versao.get("trigger", [])),
        "variaveis": len(versao.get("variable", [])),
    }


def nome_canonico(item):
    """gtm-<id>_v<N>.json para versao publicada; preserva o workspace no rascunho."""
    base = item["public_id"].lower()
    if item["publicada"]:
        return f"{base}_v{item['versao_id']}.json"
    achado = re.search(r"workspace(\d+)", item["arquivo"].name, re.IGNORECASE)
    sufixo = f"workspace{achado.group(1)}" if achado else "rascunho"
    # Um mesmo workspace pode ser exportado duas vezes em datas diferentes. Quando
    # o conteudo mudou entre as duas, os dois retratos ficam, e a data os separa.
    data = re.search(r"_(\d{4}-\d{2}-\d{2})\.json$", item["arquivo"].name)
    if data:
        return f"{base}_{sufixo}_{data.group(1)}.json"
    return f"{base}_{sufixo}.json"


def sem_ruido(caminho):
    """Conteudo do export sem o que muda a cada clique em Exportar.

    `exportTime` e o carimbo do download, e `fingerprint` e reescrito pelo GTM a
    cada gravacao. Nenhum dos dois e configuracao. Sem tirar os dois, dois
    downloads do mesmo rascunho parecem arquivos diferentes, e a pasta enche de
    copia que nao acrescenta nada.
    """
    def limpa(no):
        if isinstance(no, dict):
            return {k: limpa(v) for k, v in no.items() if k != "fingerprint"}
        if isinstance(no, list):
            return [limpa(x) for x in no]
        return no

    dado = json.loads(caminho.read_text(encoding="utf-8"))
    bruto = json.dumps(limpa(dado.get("containerVersion", {})), sort_keys=True)
    return hashlib.sha256(bruto.encode("utf-8")).hexdigest()


def importar(entrada):
    """Traz os exports de `entrada` para a pasta do repositorio, sem duplicar.

    Tres destinos possiveis para cada arquivo:
      novo         conteiner ou workspace que ainda nao existe na pasta
      identico     mesmo conteudo que ja temos, so o carimbo de export mudou: fica de fora
      retrato      mesmo conteiner e workspace, conteudo alterado: entra com a data no nome,
                   para que os dois convivam e mostrem que o rascunho foi editado
    """
    if not entrada.is_dir():
        print(f"pasta de entrada nao encontrada: {entrada}")
        return

    PASTA.mkdir(parents=True, exist_ok=True)
    conhecidos = {}
    for p in PASTA.rglob("*.json"):
        item = ler(p)
        if item["erro"]:
            continue
        conhecidos.setdefault((item["public_id"], item["versao_id"]), []).append(
            (sem_ruido(p), p.name)
        )

    # rglob, e nao glob: o operador pode organizar os exports em subpastas por
    # conta antes de entregar. A identidade real vem de dentro do JSON, entao a
    # arvore de pastas nao precisa ser preservada aqui.
    candidatos = sorted(
        [p for p in entrada.rglob("*.json") if not p.name.startswith(".")],
        key=lambda p: (p.parent.name, p.name),
    )
    if not candidatos:
        print(f"nada em {entrada}")
        return

    novos, identicos, retratos, ignorados = [], [], [], []
    for p in candidatos:
        item = ler(p)
        if item["erro"]:
            ignorados.append((p.name, item["erro"]))
            continue

        chave = (item["public_id"], item["versao_id"])
        impressao = sem_ruido(p)
        iguais = [nome for h, nome in conhecidos.get(chave, []) if h == impressao]
        if iguais:
            identicos.append((item["public_id"], iguais[0]))
            continue

        destino_dir = pasta_da_conta(item["conta"])
        destino_dir.mkdir(parents=True, exist_ok=True)
        destino = destino_dir / nome_canonico(item)
        datado = bool(conhecidos.get(chave))
        if datado:
            # Ja temos este workspace com outro conteudo. A data separa os dois.
            dia = str(item["exportado_em"])[:10] or "sem-data"
            destino = destino.with_name(destino.stem + f"_{dia}.json")
        if destino.exists():
            identicos.append((item["public_id"], destino.name))
            continue

        shutil.copy2(p, destino)
        conhecidos.setdefault(chave, []).append((impressao, destino.name))
        (retratos if datado else novos).append(
            (item["public_id"], item["nome"], destino.name)
        )

    print(f"entrada: {entrada}")
    print(f"arquivos examinados: {len(candidatos)}\n")
    print(f"NOVOS NA PASTA: {len(novos)}")
    for pid, nome, arq in novos:
        print(f"  {pid:14} {nome[:44]:44} -> {arq}")
    if retratos:
        print(f"\nRETRATOS, mesmo rascunho com conteudo alterado: {len(retratos)}")
        for pid, nome, arq in retratos:
            print(f"  {pid:14} {nome[:44]:44} -> {arq}")
    print(f"\nSEM CONTEUDO NOVO, nao copiados: {len(identicos)}")
    for pid, arq in identicos:
        print(f"  {pid:14} ja temos em {arq}")
    if ignorados:
        print(f"\nIGNORADOS: {len(ignorados)}")
        for nome, erro in ignorados:
            print(f"  {nome}: {erro}")
    print()


def main():
    renomear = "--renomear" in sys.argv[1:]
    argumentos = sys.argv[1:]
    if "--importar" in argumentos:
        i = argumentos.index("--importar")
        depois = argumentos[i + 1:]
        origem = pathlib.Path(depois[0]).expanduser() if depois and not depois[0].startswith("-") else ENTRADA
        importar(origem)
        print("=" * 70)

    if not PASTA.is_dir():
        print(f"pasta nao encontrada: {PASTA.relative_to(RAIZ)}")
        return 1

    itens = [ler(p) for p in sorted(PASTA.rglob("*.json"))]
    quebrados = [i for i in itens if i["erro"]]
    itens = [i for i in itens if not i["erro"]]

    print(f"pasta: {PASTA.relative_to(RAIZ)}")
    print(f"exports lidos: {len(itens)}\n")

    if quebrados:
        print("ARQUIVOS QUE NAO SAO EXPORT DE CONTEINER")
        for i in quebrados:
            print(f"  {i['arquivo'].name}: {i['erro']}")
        print()

    print(f"{'conteiner':16} {'conta':12} {'origem':16} {'tags':>5} {'exportado em':20} arquivo")
    for i in sorted(itens, key=lambda x: (x["conta"], x["public_id"])):
        origem = f"publicada v{i['versao_id']}" if i["publicada"] else "RASCUNHO"
        print(
            f"{i['public_id']:16} {i['conta']:12} {origem:16} {i['tags']:>5} "
            f"{i['exportado_em']:20} {i['arquivo'].name}"
        )

    # Duplicata: mesmo conteiner na mesma origem, em dois arquivos.
    vistos = {}
    for i in itens:
        vistos.setdefault((i["public_id"], i["versao_id"]), []).append(i["arquivo"].name)
    duplicados = {k: v for k, v in vistos.items() if len(v) > 1}
    if duplicados:
        # Dois arquivos do mesmo rascunho sao retratos do conteiner em datas
        # diferentes, e ficam de proposito: mostram que o workspace foi editado
        # durante a auditoria. Ja duas copias da mesma versao publicada sao erro.
        retratos = {k: v for k, v in duplicados.items() if k[1] == "0"}
        erros = {k: v for k, v in duplicados.items() if k[1] != "0"}
        if retratos:
            print("\nRETRATOS DO MESMO RASCUNHO, em datas diferentes")
            for (pid, _), arquivos in retratos.items():
                print(f"  {pid}: {', '.join(sorted(arquivos))}")
        if erros:
            print("\nDUPLICATAS, a mesma versao publicada em dois arquivos")
            for (pid, vid), arquivos in erros.items():
                print(f"  {pid} (v{vid}): {', '.join(sorted(arquivos))}")

    publicadas = {i["public_id"] for i in itens if i["publicada"]}
    presentes = {i["public_id"] for i in itens}

    print("\nFALTA · versao publicada dos conteineres ja auditados")
    faltam = 0
    for pid, (conta, nome, lote) in PUBLICADA_ESPERADA.items():
        if pid in publicadas:
            continue
        faltam += 1
        estado = "so o rascunho" if pid in presentes else "nenhum export"
        print(f"  [ ] {pid:14} {nome:28} conta {conta:12} {lote} · temos {estado}")
    if not faltam:
        print("  nada: todos os nomeados tem versao publicada")

    if not CONTAS_ABERTAS:
        print("\nINVENTARIO · fechado. As 4 contas foram varridas, "
              f"{len(presentes)} conteineres distintos na pasta.")
    else:
        print("\nFALTA · contas de que precisamos do conteiner todo")
    for conta, o_que in CONTAS_ABERTAS.items():
        achados = sorted({i["public_id"] for i in itens if i["conta"] == conta})
        rotulo = CONTAS.get(conta, conta)
        lista = ", ".join(achados) if achados else "nenhum"
        print(f"  [ ] {rotulo} ({conta}): {len(achados)} na pasta [{lista}]")
        print(f"        {o_que}")

    print("\nFALTA · prints, que o script nao consegue conferir sozinho")
    existentes = sorted(p.name for p in TELAS.glob("*")) if TELAS.is_dir() else []
    print(f"  arquivos hoje em telas/: {len(existentes)}"
          + (f" [{', '.join(existentes)}]" if existentes else ""))
    for esperado in PRINTS_ESPERADOS:
        print(f"  [ ] {esperado}")

    if renomear:
        print("\nRENOMEANDO")
        for i in itens:
            alvo = i["arquivo"].with_name(nome_canonico(i))
            if alvo == i["arquivo"]:
                continue
            if alvo.exists():
                print(f"  pulado {i['arquivo'].name}: {alvo.name} ja existe")
                continue
            i["arquivo"].rename(alvo)
            print(f"  {i['arquivo'].name} -> {alvo.name}")
    else:
        fora = [i for i in itens if nome_canonico(i) != i["arquivo"].name]
        if fora:
            print(f"\n{len(fora)} arquivo(s) fora do padrao de nome. "
                  "Rode com --renomear para ajustar.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
