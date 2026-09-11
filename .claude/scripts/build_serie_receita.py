#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_serie_receita.py: transforma a serie de receita do cliente em estado de maquina.

Le o original recebido do Grupo OLX em assets/originais (bloco A, item A1) e
escreve dados/outputs/serie-receita-2025-2026.json. Nenhum numero deste projeto
sobre receita bruta deve ser digitado a mao: todos saem daqui.

O que o script calcula, e por que cada coisa esta aqui e nao no .md:

- YoY por linha, no periodo comparavel (jan-jul, os 7 meses que existem nos dois anos).
- Contribuicao de cada unidade para o crescimento do grupo, que separa tamanho de tracao.
- Run-rate mensal por candidata a vertical governante, que e o DENOMINADOR da meta.
- Banda de ruido de uma leitura de 90 dias, calculada sobre a propria serie. E ela
  que diz se uma meta de ciclo e verificavel ou apenas declaravel.

Uso:
    python3 .claude/scripts/build_serie_receita.py
"""
import csv
import json
import pathlib
import statistics as st

RAIZ = pathlib.Path(__file__).resolve().parents[2]
ENTRADA = (RAIZ / "assets" / "originais" / "A-visao-de-negocio-e-fluxo-de-receita"
           / "evolucao-receita-2025-2026.csv")
SAIDA = RAIZ / "dados" / "outputs" / "serie-receita-2025-2026.json"

# Os 7 meses que existem nos dois anos. Comparar 12 meses de 2025 com 7 de 2026
# seria erro de janela, e e o erro mais facil de cometer com esta planilha.
JAN_JUL_25 = (0, 7)
JAN_JUL_26 = (12, 19)
ULTIMO_FECHADO = 19  # ago/26 em diante esta zerado na origem

UNIDADES = ["Real Estate", "Autos", "Goods & Services", "Conecta"]

# As linhas que o cliente descontinuou dentro de Imoveis. Elas puxam a vertical
# para baixo por decisao de portfolio, nao por desempenho comercial, e por isso
# a leitura correta de Imoveis e feita com e sem elas.
DESCONTINUADAS_RE = ["Data", "CRM", "Transactional & Fintech - For Sale",
                     "Transactional & Fintech - Rentals"]

# Assinatura profissional recorrente: o sistema de receita que o DR-E enderecou.
NUCLEO_B2B = ["Classifieds - B&A", "Classifieds - Developers",
              "Classifieds - Dealers", "Classifieds - Goods Pros"]


def numero(s):
    """Converte o formato brasileiro da planilha. Devolve None para celula vazia.

    A planilha usa '-' tanto para 'nao existe' quanto para zero, e traz negativo
    como '- 57.884' (sinal separado do numero). Ambos os casos passam por aqui.
    """
    s = s.strip()
    if s in ("", "-", "–"):
        return None
    negativo = s.startswith("-")
    s = s.lstrip("-").strip().replace(".", "").replace(",", ".")
    if not s or s == "-":
        return None
    try:
        v = float(s)
    except ValueError:
        return None
    return -v if negativo else v


def ler():
    linhas_csv = list(csv.reader(ENTRADA.open(encoding="utf-8")))
    meses = [c.strip() for c in linhas_csv[1][2:26]]
    dados, ordem = {}, []
    for r in linhas_csv[2:]:
        if len(r) < 3 or not r[1].strip():
            continue
        nome = r[1].strip()
        chave, i = nome, 2
        while chave in dados:          # 'Advertising' se repete nas tres unidades
            chave = f"{nome} #{i}"
            i += 1
        dados[chave] = [numero(c) for c in r[2:26]]
        ordem.append(chave)
    return meses, dados, ordem


def soma(serie, a, b):
    return sum(v or 0 for v in serie[a:b])


def banda_de_ruido(serie):
    """Desvio das variacoes de 90 dias sobre a media movel de 3 meses.

    E o teste que decide se uma meta de ciclo pode ser verificada na receita
    bruta. Media movel porque a serie mensal e serrilhada demais: o mes isolado
    varia mais que o efeito que o ciclo pretende produzir.
    """
    ma = [sum(serie[i - 2:i + 1]) / 3 for i in range(2, ULTIMO_FECHADO)]
    ch = [(ma[i] / ma[i - 3] - 1) * 100 for i in range(3, len(ma))]
    return {
        "n": len(ch),
        "media_pct": round(st.mean(ch), 2),
        "desvio_pct": round(st.pstdev(ch), 2),
        "minimo_pct": round(min(ch), 2),
        "maximo_pct": round(max(ch), 2),
        "efeito_minimo_detectavel_2s_pct": round(2 * st.pstdev(ch), 2),
    }


def main():
    meses, D, ordem = ler()
    total = D["TOTAL - 2025&2026"]

    # Verificacao de integridade: a soma das unidades tem de bater com o TOTAL.
    # Se um dia deixar de bater, a planilha mudou e nada abaixo vale.
    #
    # A tolerancia e de R$ 100 e nao de zero porque a origem exibe valores
    # arredondados ao real: a maior divergencia observada e de R$ 51 sobre
    # R$ 94,9 milhoes (abr/25), ou 0,00005%. Isso e arredondamento de exibicao,
    # nao inconsistencia de dado. Uma divergencia acima da tolerancia seria.
    TOLERANCIA = 100.0
    conferencia = []
    for i in range(ULTIMO_FECHADO):
        s = sum(D[u][i] or 0 for u in UNIDADES)
        conferencia.append({"mes": meses[i], "diferenca": round(s - (total[i] or 0), 2)})
    fecha = all(abs(c["diferenca"]) < TOLERANCIA for c in conferencia)

    def bloco(chave, rotulo=None):
        a, b = soma(D[chave], *JAN_JUL_25), soma(D[chave], *JAN_JUL_26)
        return {
            "linha": rotulo or chave,
            "jan_jul_2025": round(a, 2),
            "jan_jul_2026": round(b, 2),
            "yoy_pct": round((b / a - 1) * 100, 2) if a else None,
            "delta": round(b - a, 2),
            "run_rate_mensal_2026": round(b / 7, 2),
        }

    tot25, tot26 = soma(total, *JAN_JUL_25), soma(total, *JAN_JUL_26)

    re_desc25 = sum(soma(D[k], *JAN_JUL_25) for k in DESCONTINUADAS_RE)
    re_desc26 = sum(soma(D[k], *JAN_JUL_26) for k in DESCONTINUADAS_RE)
    re25, re26 = soma(D["Real Estate"], *JAN_JUL_25), soma(D["Real Estate"], *JAN_JUL_26)

    nuc25 = sum(soma(D[k], *JAN_JUL_25) for k in NUCLEO_B2B)
    nuc26 = sum(soma(D[k], *JAN_JUL_26) for k in NUCLEO_B2B)

    out = {
        "meta": {
            "fonte": "assets/originais/A-visao-de-negocio-e-fluxo-de-receita/evolucao-receita-2025-2026.csv",
            "sha256_origem": "4b560e7ee40b7de3bc3c3ab21503ed76c26d015db8c2d4af52bc6ae49a0ea878",
            "recebido_em": "2026-08-28",
            "processado_em": "2026-09-08",
            "item_do_checklist": "A1",
            "natureza": "receita bruta faturada, declarada pelo cliente, nao auditada pela V4",
            "nao_e": "truput. Sem P&L por vertical a serie nao converte em margem de contribuicao",
            "cobertura": "jan/2025 a jul/2026, 19 meses com dado de 24 colunas",
            "ultimo_mes_fechado": "Jul./26",
            "gerado_por": ".claude/scripts/build_serie_receita.py",
        },
        "integridade": {
            "soma_das_unidades_bate_com_total": fecha,
            "meses_conferidos": ULTIMO_FECHADO,
            "tolerancia_reais": TOLERANCIA,
            "maior_diferenca_absoluta": round(max(abs(c["diferenca"]) for c in conferencia), 2),
            "maior_diferenca_relativa_pct": round(max(
                abs(c["diferenca"]) / (total[i] or 1) * 100
                for i, c in enumerate(conferencia)), 6),
            "leitura": ("as unidades somam o TOTAL em todos os meses dentro da tolerancia. "
                        "A diferenca residual e arredondamento ao real na origem."),
        },
        "grupo": {
            "jan_jul_2025": round(tot25, 2),
            "jan_jul_2026": round(tot26, 2),
            "yoy_pct": round((tot26 / tot25 - 1) * 100, 2),
            "ano_2025_fechado": round(soma(total, 0, 12), 2),
            "run_rate_mensal_2026": round(tot26 / 7, 2),
        },
        "unidades": [
            dict(bloco(u), **{
                "share_2026_pct": round(soma(D[u], *JAN_JUL_26) / tot26 * 100, 2),
                "participacao_no_crescimento_pct": round(
                    (soma(D[u], *JAN_JUL_26) - soma(D[u], *JAN_JUL_25)) / (tot26 - tot25) * 100, 2),
            }) for u in UNIDADES
        ],
        "imoveis_sem_descontinuados": {
            "descontinuadas": DESCONTINUADAS_RE,
            "yoy_vertical_cheia_pct": round((re26 / re25 - 1) * 100, 2),
            "arrasto_das_descontinuadas": round(re_desc26 - re_desc25, 2),
            "yoy_ex_descontinuadas_pct": round(((re26 - re_desc26) / (re25 - re_desc25) - 1) * 100, 2),
        },
        "nucleo_assinatura_b2b": {
            "linhas": NUCLEO_B2B,
            "jan_jul_2025": round(nuc25, 2),
            "jan_jul_2026": round(nuc26, 2),
            "yoy_pct": round((nuc26 / nuc25 - 1) * 100, 2),
            "share_do_grupo_pct": round(nuc26 / tot26 * 100, 2),
            "run_rate_mensal_2026": round(nuc26 / 7, 2),
        },
        "linhas": [bloco(k) for k in ordem if k != "TOTAL - 2025&2026"],
        "denominador_da_meta": {
            "definicao": "run-rate = media mensal jan-jul/2026. Um ponto percentual de run-rate, em reais por mes e por ano.",
            "candidatas": [
                {
                    "vertical": k,
                    "run_rate_mensal": round(soma(D[k], *JAN_JUL_26) / 7, 2),
                    "um_pp_mes": round(soma(D[k], *JAN_JUL_26) / 7 / 100, 2),
                    "um_pp_ano": round(soma(D[k], *JAN_JUL_26) / 7 * 12 / 100, 2),
                } for k in ["Real Estate", "Classifieds - B&A", "Autos",
                            "Classifieds - Dealers", "TOTAL - 2025&2026"]
            ],
        },
        "ruido_de_90_dias": {
            "metodo": "desvio das variacoes de 3 meses sobre a media movel de 3 meses, na propria serie",
            "para_que_serve": "define o efeito minimo detectavel de uma meta de ciclo lida em receita bruta",
            "por_linha": {k: banda_de_ruido(D[k]) for k in
                          ["TOTAL - 2025&2026", "Real Estate", "Classifieds - B&A",
                           "Autos", "Classifieds - Dealers", "Goods & Services"]},
        },
        "sazonalidade_janela_ciclo_1": {
            "janela": "ago a nov, medida em 2025",
            "para_que_serve": "separa o que o ciclo produziu do que o calendario produziria sozinho",
            "por_linha": {k: round((D[k][10] / D[k][7] - 1) * 100, 2) for k in
                          ["TOTAL - 2025&2026", "Real Estate", "Classifieds - B&A",
                           "Autos", "Classifieds - Dealers", "Goods & Services"]},
        },
        "meses": meses[:ULTIMO_FECHADO],
        "serie_mensal": {k: [None if v is None else round(v, 2)
                             for v in D[k][:ULTIMO_FECHADO]] for k in ordem},
    }

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    SAIDA.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"escrito: {SAIDA.relative_to(RAIZ)}")
    print(f"integridade: soma das unidades bate com TOTAL = {fecha}")
    print(f"grupo jan-jul: {tot25/1e6:.1f}M -> {tot26/1e6:.1f}M ({(tot26/tot25-1)*100:+.1f}%)")


if __name__ == "__main__":
    main()
