#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analisa_gtm.py: levanta as evidencias da auditoria (vii) a partir dos exports.

Le os conteineres em assets/originais/H-rastreamento-gtm/ e extrai o que a
auditoria de rastreamento precisa checar, conteiner a conteiner:

  onde o dado cai     measurement IDs do GA4, IDs de conversao do Google Ads,
                      pixels do Meta, e qualquer Universal Analytics sobrevivente
  consentimento       setDefaultConsentState, o valor de cada categoria, e se a
                      tag que instancia o template esta pausada
  evento contra       para cada tag de evento do GA4, o event_name declarado
  gatilho             contra o evento que o gatilho de fato escuta. Divergencia
                      aqui e o achado 1 da primeira rodada, e e o mais caro
  PII                 e-mail, telefone e CPF indo para plataforma de midia
  higiene             tags pausadas, tags sem gatilho, gatilhos orfaos

Nao decide nada. Levanta fato com origem (conteiner, tagId, nome), para que o
achado escrito no .md seja rastreavel ate a linha do export. A leitura e o
julgamento ficam no documento da auditoria.

Uso:
    python3 .claude/scripts/analisa_gtm.py
    python3 .claude/scripts/analisa_gtm.py --conta 2971905372
    python3 .claude/scripts/analisa_gtm.py --conteiner GTM-MKTZ2ZP --detalhe
"""
import argparse
import collections
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
PASTA = RAIZ / "assets" / "originais" / "H-rastreamento-gtm"
SAIDA = RAIZ / "dados" / "outputs" / "gtm-evidencias.json"

# Eventos de ecommerce e de lead: sao os que sustentam receita, e por isso os
# unicos em que a divergencia entre tag e gatilho vira achado critico.
EVENTOS_RECEITA = {
    "purchase", "begin_checkout", "add_to_cart", "view_cart", "add_payment_info",
    "add_shipping_info", "generate_lead", "generate_lead_pro", "sign_up", "login",
    "checkout", "subscribe", "lead", "lead_b2b",
}

TIPOS = {
    "gaawc": "GA4 config", "gaawe": "GA4 evento", "googtag": "Google tag",
    "ua": "Universal Analytics", "awct": "Google Ads conversao",
    "sp": "Google Ads remarketing", "html": "HTML customizado",
    "gclidw": "Google Ads linker", "cvt": "template da comunidade",
}


def valor(param, chave):
    for p in param or []:
        if p.get("key") == chave:
            if "value" in p:
                return p["value"]
            if "list" in p:
                return p["list"]
            if "map" in p:
                return p["map"]
    return None


def texto_inteiro(no):
    """Achata a entidade em texto, para busca por expressao regular."""
    return json.dumps(no, ensure_ascii=False)


def evento_do_gatilho(gatilho):
    """Que nome de evento este gatilho escuta, se escutar algum."""
    nomes = set()
    for f in gatilho.get("customEventFilter", []) or []:
        arg0 = valor(f.get("parameter"), "arg0")
        arg1 = valor(f.get("parameter"), "arg1")
        if arg0 and "_event" in str(arg0) and arg1:
            nomes.add(str(arg1))
    return nomes


def le_conteiner(caminho):
    dado = json.loads(caminho.read_text(encoding="utf-8"))
    cv = dado.get("containerVersion", {})
    c = cv.get("container", {})
    tags = cv.get("tag", []) or []
    gatilhos = cv.get("trigger", []) or []
    variaveis = cv.get("variable", []) or []
    bruto = texto_inteiro(cv)

    por_gatilho = {g.get("triggerId"): g for g in gatilhos}
    escuta = {gid: evento_do_gatilho(g) for gid, g in por_gatilho.items()}

    r = {
        "arquivo": caminho.relative_to(PASTA).as_posix(),
        "conta": str(c.get("accountId")),
        "public_id": c.get("publicId"),
        "nome": c.get("name", ""),
        "versao": str(cv.get("containerVersionId", "0")),
        "contagem": {
            "tags": len(tags),
            "pausadas": sum(1 for t in tags if t.get("paused")),
            "gatilhos": len(gatilhos),
            "variaveis": len(variaveis),
        },
        "tipos": dict(collections.Counter(
            TIPOS.get(t.get("type"), t.get("type")) for t in tags
        )),
        "ga4": sorted({m for m in re.findall(r"G-[A-Z0-9]{8,12}", bruto)}),
        "google_ads": sorted({m for m in re.findall(r"AW-\d{9,12}", bruto)}),
        "ua": sorted({m for m in re.findall(r"UA-\d{4,10}-\d{1,3}", bruto)}),
        "meta_pixel": sorted({m for m in re.findall(r"fbq\(\s*['\"]init['\"]\s*,\s*['\"](\d{10,17})", bruto)}),
        "gtm_aninhado": sorted({m for m in re.findall(r"GTM-[A-Z0-9]{6,9}", bruto)} - {c.get("publicId")}),
        "consentimento": [],
        "divergencias": [],
        "eventos_receita": [],
        "pii": [],
        "sem_gatilho": [],
        "pausadas_criticas": [],
    }

    # consentimento: onde o default e declarado, e com que valor
    for alvo in tags + variaveis + (cv.get("customTemplate", []) or []):
        corpo = texto_inteiro(alvo)
        if "setDefaultConsentState" not in corpo:
            continue
        concedidos = sorted(set(re.findall(r"(\w+_storage|ad_user_data|ad_personalization)\s*:\s*'granted'", corpo)))
        negados = sorted(set(re.findall(r"(\w+_storage|ad_user_data|ad_personalization)\s*:\s*'denied'", corpo)))
        r["consentimento"].append({
            "onde": alvo.get("name", "?"),
            "tipo": "tag" if alvo.get("tagId") else ("variavel" if alvo.get("variableId") else "template"),
            "id": alvo.get("tagId") or alvo.get("variableId") or alvo.get("templateId"),
            "pausada": bool(alvo.get("paused")),
            "granted": concedidos,
            "denied": negados,
        })

    for t in tags:
        tid, nome_tag = t.get("tagId"), t.get("name", "?")
        gatilhos_da_tag = t.get("firingTriggerId", []) or []

        if not gatilhos_da_tag and not t.get("paused"):
            r["sem_gatilho"].append({"id": tid, "nome": nome_tag})

        # GA4: evento declarado contra evento escutado
        if t.get("type") in ("gaawe", "gaawc"):
            ev = valor(t.get("parameter"), "eventName")
            if isinstance(ev, str) and ev:
                escutados = set()
                for gid in gatilhos_da_tag:
                    escutados |= escuta.get(gid, set())
                base = ev.strip().lower()
                if base in EVENTOS_RECEITA:
                    r["eventos_receita"].append({
                        "id": tid, "nome": nome_tag, "evento": ev,
                        "pausada": bool(t.get("paused")),
                        "gatilhos": gatilhos_da_tag,
                        "escutam": sorted(escutados),
                    })
                # divergencia: o gatilho escuta um evento de receita diferente
                conflito = {e for e in escutados if e.lower() in EVENTOS_RECEITA and e.lower() != base}
                if conflito:
                    r["divergencias"].append({
                        "id": tid, "nome": nome_tag, "declara": ev,
                        "gatilho_escuta": sorted(conflito),
                        "gatilhos": gatilhos_da_tag,
                        "pausada": bool(t.get("paused")),
                    })

        # PII indo para tag de midia ou de analytics
        corpo = texto_inteiro(t)
        achados_pii = sorted({
            p for p in re.findall(
                r"\b(email|e_mail|user_email|phone|telefone|phone_number|cpf|cnpj|document)\b",
                corpo, re.IGNORECASE)
        })
        if achados_pii and t.get("type") in ("gaawe", "gaawc", "awct", "sp", "html", "ua"):
            r["pii"].append({"id": tid, "nome": nome_tag, "tipo": TIPOS.get(t.get("type"), t.get("type")),
                             "campos": achados_pii, "pausada": bool(t.get("paused"))})

        # tag pausada que mede receita ou consentimento
        if t.get("paused"):
            alvo = nome_tag.lower()
            if any(k in alvo for k in ("purchase", "checkout", "lead", "consent", "adopt", "conversion", "conversao")):
                r["pausadas_criticas"].append({"id": tid, "nome": nome_tag,
                                               "tipo": TIPOS.get(t.get("type"), t.get("type"))})

    return r


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--conta")
    ap.add_argument("--conteiner")
    ap.add_argument("--detalhe", action="store_true")
    a = ap.parse_args()

    itens = []
    for p in sorted(PASTA.rglob("*.json")):
        try:
            r = le_conteiner(p)
        except Exception as erro:               # noqa: BLE001
            print(f"falhou em {p.name}: {erro}", file=sys.stderr)
            continue
        if a.conta and r["conta"] != a.conta:
            continue
        if a.conteiner and r["public_id"].upper() != a.conteiner.upper():
            continue
        itens.append(r)

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    SAIDA.write_text(json.dumps({"conteineres": itens}, ensure_ascii=False, indent=2) + "\n",
                     encoding="utf-8")

    print(f"conteineres analisados: {len(itens)}")
    print(f"evidencias em {SAIDA.relative_to(RAIZ)}\n")

    for r in sorted(itens, key=lambda x: (x["conta"], -x["contagem"]["tags"])):
        destaque = []
        if r["divergencias"]:
            destaque.append(f"{len(r['divergencias'])} DIVERGENCIA(S)")
        if r["ua"]:
            destaque.append(f"UA {','.join(r['ua'])}")
        if len(r["ga4"]) > 1:
            destaque.append(f"{len(r['ga4'])} GA4")
        if r["pii"]:
            destaque.append(f"{len(r['pii'])} PII")
        if r["sem_gatilho"]:
            destaque.append(f"{len(r['sem_gatilho'])} sem gatilho")
        print(f"{r['public_id']:14} {r['nome'][:42]:42} {r['contagem']['tags']:>4}t "
              f"{r['contagem']['pausadas']:>3}p  {' · '.join(destaque)}")
        if a.detalhe:
            for k in ("ga4", "google_ads", "meta_pixel", "ua", "gtm_aninhado"):
                if r[k]:
                    print(f"      {k}: {', '.join(r[k])}")
            for d in r["divergencias"]:
                print(f"      DIVERGE tag {d['id']} {d['nome']!r} declara {d['declara']!r}, "
                      f"gatilho escuta {d['gatilho_escuta']}")
            for c in r["consentimento"]:
                print(f"      consent {c['tipo']} {c['id']} pausada={c['pausada']} "
                      f"granted={c['granted']} denied={c['denied']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
