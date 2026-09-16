#!/usr/bin/env python3
"""Le os exports de Google Ads organizados por conta e gera o estado de maquina.

Entrada : assets/originais/G-midia-paga/google-ads/<conta>/
Saida   : dados/outputs/google-ads-parque.json

Nada aqui interpreta: o script soma, classifica por convencao de nome de campanha
e compara janelas. A leitura vive em 02-diagnostico/diagnostico-vi-midia-paga.md.
"""
import csv, json, os, re, sys, gzip, collections

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = os.path.join(RAIZ, "assets/originais/G-midia-paga/google-ads")
SAIDA = os.path.join(RAIZ, "dados/outputs/google-ads-parque.json")

CONTAS = [
    ("conta-1-zapmais-b2b",     "ZAP+ / CanalPro · anunciante profissional", "B2B",  "2021-09-24"),
    ("conta-2-vivareal-marca",  "VivaReal · busca de marca",                 "B2C",  "2024-07-04"),
    ("conta-3-vivareal-sp",     "VivaReal · performance regional SP",        "B2C",  "2025-05-16"),
    ("conta-4-vivareal-brasil", "VivaReal Brasil · conta principal",         "B2C",  "2016-10-01"),
    ("conta-5-vivareal-app",    "VivaReal · instalacao de app e video",      "B2C",  "2016-10-01"),
]

def num(s):
    """'R$1,234.56' -> 1234.56 · '12,345' -> 12345.0 · '--'/'' -> None"""
    if s is None: return None
    s = s.replace("R$", "").replace("%", "").replace(",", "").strip()
    if s in ("", "--", "-", "N/A"): return None
    try: return float(s)
    except ValueError: return None

def ler(caminho):
    """Devolve (periodo, header, linhas_de_dado, linhas_de_total)."""
    op = gzip.open if caminho.endswith(".gz") else open
    with op(caminho, "rt", encoding="utf-8-sig", newline="") as fh:
        r = list(csv.reader(fh))
    periodo = r[1][0] if len(r) > 1 and r[1] else ""
    hdr = r[2]
    corpo = r[3:]
    dados = [d for d in corpo if d and not d[0].startswith("Total")]
    totais = {d[0]: d for d in corpo if d and d[0].startswith("Total")}
    return periodo, hdr, dados, totais

def col(hdr, nome):
    return hdr.index(nome) if nome in hdr else None

# convencao de nome da OLX: <id>_<plataforma>_<tipo>_<funil>_<objetivo>_<...>_<marca>_<perfil>
MARCA = {"go": "Grupo OLX", "vr": "VivaReal", "zp": "ZAP"}
def decompoe(nome):
    partes = nome.split("_")
    if len(partes) < 8 or partes[1] not in ("gg", "mt", "wa", "em", "pr", "pc", "so", "mp"):
        return dict(padronizada=False, marca=None, funil=None, objetivo=None, plataforma=None)
    return dict(padronizada=True, plataforma=partes[1],
                funil=partes[3] if len(partes) > 3 else None,
                objetivo=partes[4] if len(partes) > 4 else None,
                marca=MARCA.get(partes[-2], partes[-2]), perfil=partes[-1])

def main():
    saida = {"meta": {"gerado_por": ".claude/scripts/build_google_ads_parque.py",
                      "fonte": "assets/originais/G-midia-paga/google-ads/",
                      "natureza": "export direto da interface do Google Ads em 16/09/2026, conta do operador V4",
                      "ressalva": "o export nao traz customer ID nem nome oficial da conta; a identidade de "
                                  "cada conta foi inferida por dominio de destino e convencao de nome de campanha"},
             "contas": [], "consolidado": {}}

    tot_geral = collections.Counter()
    for slug, rotulo, recorte, inicio in CONTAS:
        d = os.path.join(BASE, slug)
        periodo, hdr, dados, totais = ler(os.path.join(d, "campanhas.csv"))
        ic = {n: col(hdr, n) for n in ("Campaign", "Campaign status", "Campaign type", "Campaign subtype",
                                       "Bid strategy type", "Cost", "Conversions", "Impr.", "Clicks",
                                       "Conv. rate", "Cost / conv.", "Optimization score", "Budget", "CTR")}
        camps = []
        for row in dados:
            g = lambda k: row[ic[k]] if ic[k] is not None and ic[k] < len(row) else None
            nome = g("Campaign")
            if not nome: continue
            camps.append(dict(nome=nome, status=g("Campaign status"), tipo=g("Campaign type"),
                              subtipo=g("Campaign subtype"), estrategia=g("Bid strategy type"),
                              custo=num(g("Cost")), conversoes=num(g("Conversions")),
                              impressoes=num(g("Impr.")), cliques=num(g("Clicks")),
                              taxa_conversao=num(g("Conv. rate")), custo_por_conversao=num(g("Cost / conv.")),
                              ctr=num(g("CTR")), orcamento_diario=num(g("Budget")),
                              nota_otimizacao=num(g("Optimization score")),
                              **decompoe(nome)))

        somas = lambda sel: dict(
            campanhas=len(sel),
            custo=round(sum(c["custo"] or 0 for c in sel), 2),
            conversoes=round(sum(c["conversoes"] or 0 for c in sel), 2),
            impressoes=int(sum(c["impressoes"] or 0 for c in sel)),
            cliques=int(sum(c["cliques"] or 0 for c in sel)))

        ativas = [c for c in camps if c["status"] == "Enabled"]
        t = somas(camps)
        # serie trimestral do overview
        serie = []
        ts = os.path.join(d, "overview", "time-series.csv")
        if os.path.exists(ts):
            with open(ts, encoding="utf-8-sig") as fh:
                rr = list(csv.DictReader(fh))
            for linha in rr:
                per = linha.get("Quarter") or linha.get("Month") or linha.get("Week")
                serie.append({"periodo": per,
                              **{k.lower().replace(".", "").replace(" ", "_").replace("/", "_por_"): num(v)
                                 for k, v in linha.items() if k != (list(linha)[0])}})
        conta = dict(slug=slug, rotulo=rotulo, recorte=recorte, primeiro_dado=inicio, periodo_export=periodo,
                     total=t, ativas=somas(ativas),
                     por_tipo={k: somas([c for c in camps if c["tipo"] == k])
                               for k in sorted({c["tipo"] for c in camps if c["tipo"]})},
                     por_status=dict(collections.Counter(c["status"] for c in camps)),
                     padronizadas=sum(1 for c in camps if c["padronizada"]),
                     campanhas=sorted(camps, key=lambda c: -(c["custo"] or 0)),
                     serie_trimestral=serie)
        saida["contas"].append(conta)
        for k, v in t.items(): tot_geral[k] += v

    b2b = [c for c in saida["contas"] if c["recorte"] == "B2B"]
    b2c = [c for c in saida["contas"] if c["recorte"] == "B2C"]
    agr = lambda cs, campo: round(sum(c[campo]["custo"] for c in cs), 2)
    saida["consolidado"] = dict(
        contas=len(saida["contas"]),
        campanhas=int(tot_geral["campanhas"]),
        custo_total=round(tot_geral["custo"], 2),
        conversoes_total=round(tot_geral["conversoes"], 2),
        impressoes_total=int(tot_geral["impressoes"]),
        cliques_total=int(tot_geral["cliques"]),
        custo_b2b=agr(b2b, "total"), custo_b2c=agr(b2c, "total"),
        custo_b2b_ativas=agr(b2b, "ativas"), custo_b2c_ativas=agr(b2c, "ativas"),
        share_b2b=round(agr(b2b, "total") / max(tot_geral["custo"], 1), 4))
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    json.dump(saida, open(SAIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    c = saida["consolidado"]
    print(f"{c['contas']} contas · {c['campanhas']} campanhas · R$ {c['custo_total']:,.2f}")
    print(f"  B2B R$ {c['custo_b2b']:,.2f} ({c['share_b2b']:.1%})  ·  B2C R$ {c['custo_b2c']:,.2f}")
    print(f"  conversoes declaradas: {c['conversoes_total']:,.0f}")
    print(f"-> {os.path.relpath(SAIDA, RAIZ)}")

if __name__ == "__main__":
    main()
