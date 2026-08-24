#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_forecast_v4_completo.py — Forecast V4 COMPLETO (multi-aba, modelo vivo).

Mantém EXATAMENTE os números aprovados do Forecast V4 de 12 meses
(build_forecast_v4.py, CONFIG Liló Decor) e os expande em uma planilha
xlsx completa e editável:

  1. Resumo Executivo   — dashboard visual (print/share), idêntico ao entregável atual
  2. Premissas          — todos os drivers de entrada, editáveis (fonte de verdade)
  3. Forecast Mensal    — receita, acumulado, atingimento, ticket, MER, CAC (FÓRMULAS)
  4. Funil de Vendas    — etapas e taxas mês a mês (FÓRMULAS)
  5. Cenários & Sens.   — AS-IS vs Com Injeção + upside (AOV R$450 / CRO destravado)
  6. Split de Mídia     — 70/30 Meta/Google e campanhas (consistente com R$3.000/mês)
  7. Premissas & Ressalvas — base de calibração, alavanca governante, MER vs ROAS, pré-requisitos

As abas 3 a 6 leem a aba Premissas por fórmula: mexeu numa premissa, recalcula tudo.
Os defaults de Premissas SÃO os números do CONFIG, então a base bate ao centavo.

Uso:
    .venv/bin/python plugins/v4-estruturacao-ia/scripts/build_forecast_v4_completo.py
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import DataBarRule
import os

# ============================ NÚMEROS (CONFIG Forecast V4 · Liló Decor) ============================
# Espelham build_forecast_v4.py. NÃO alterar: "siga os números".
CONFIG = {
    "cliente": "Liló Decor",
    "escopo": "E-commerce",
    "saida": "clientes/lilo-decor/forecast-v4-lilo-decor.xlsx",
    "mes_atual_label": "Jul/2026",
    "mes_atual_pos": "Mês 1 de 12",
    "meses": ["Jul/26", "Ago/26", "Set/26", "Out/26", "Nov/26", "Dez/26",
              "Jan/27", "Fev/27", "Mar/27", "Abr/27", "Mai/27", "Jun/27"],
    "meta_anual": 480000,
    "meta_mensal": 40000,
    "fat_asis": [19000, 18500, 20000, 20500, 26000, 24000, 17000, 18000, 19000, 20000, 24000, 20000],
    "fat_inj":  [20000, 21500, 24000, 27000, 38000, 36000, 26000, 28000, 31000, 33000, 37000, 40000],
    "midia":    [3000] * 12,
    "base":     [52, 55, 61, 68, 94, 88, 62, 66, 72, 75, 83, 89],
    "expo":     [150000] * 12,
    "txAt":     [5.0] * 12,
    "txIn":     [12.0, 12.1, 12.2, 12.4, 12.6, 12.7, 12.8, 12.9, 13.0, 13.1, 13.2, 13.2],
    "txQu":     [40, 41, 43, 44, 46, 47, 48, 49, 50, 51, 52, 52],
    "txCo":     [60, 61, 62, 63, 64, 65, 66, 66, 67, 67, 68, 68],
    "txDe":     [9.7, 9.7, 9.7, 9.8, 9.8, 9.8, 9.9, 9.9, 9.9, 10.0, 10.0, 10.0],
    "txRe":     [18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    "label_decisao": "Decisão · pedido pago",
    "label_base": "Base · compradores/mês",
    # constantes de referência (calibração real Shopify)
    "aov_real": 382,
    "aov_meta": 450,
    "conv_real": 0.4,        # % conversão online real
    "breakeven_roas": 2.9,   # ROAS de mídia atribuída (break-even)
}

# Split de mídia (S3 · consistente com R$3.000/mês). Meta 2100 + Google 900.
MIDIA_SPLIT = {
    "Meta Ads": {
        "total": 2100, "pct": 70,
        "campanhas": [
            ("Retargeting DPA (BOF)", "Dynamic Product Ad", 850, "Visitantes 30d + carrinho abandonado. Melhor ativo (ROAS 4,5x), estava pausado."),
            ("Catálogo ASC Advantage+ (MOF)", "Advantage+ Shopping", 600, "Catálogo Shopify + lookalike. Segundo melhor (ROAS 3,4x), também pausado."),
            ("Prospecting estruturado (TOF)", "Vídeo / UGC", 500, "Lookalike da base + dopamine decor. Substitui os boosts avulsos por aquisição mensurável."),
            ("Instagram Shopping", "Coleções + tags", 150, "Feed e Explore com produtos marcados. Fecha o loop visual da descoberta."),
        ],
    },
    "Google Ads": {
        "total": 900, "pct": 30,
        "campanhas": [
            ("Search Marca (defensiva)", "Search exata", 120, "lilo decor, loja liló recife. Captura quem viu o Reel e foi buscar."),
            ("Search Produto autoral", "Search", 210, "cerâmica colorida, vaso autoral, objeto de design brasileiro. Território de autoria."),
            ("Search Presentes de design", "Search", 120, "presente criativo de design, presente de decoração exclusivo. Escala em datas."),
            ("Search Dopamine decor", "Search", 150, "decoração colorida aesthetic, maximalista. Pesquisa pós-Instagram do nicho."),
            ("Google Shopping (feed)", "Shopping / PMax", 300, "Catálogo via feed do Shopify, que casa os eventos corretamente."),
        ],
    },
}

# ============================ IDENTIDADE VISUAL (Destrava Receita · sem azul) ============================
C_RED_DEEP = "980000"
C_RED = "C81E1E"
C_ASIS = "E74C3C"
C_INJ = "C81E1E"
C_GREEN = "00A878"
C_TEXT = "2D3748"
C_SEC = "4A5568"
C_LABEL = "6C757D"
C_BAND = "FDECEC"
C_CELL_INJ = "FFF0EC"
C_CELL_DELTA = "E8F8F3"
C_CALLOUT = "E8F8F3"
C_WHITE = "FFFFFF"
C_TRACK = "EBEBEB"
C_HEADREF = "F5F5F5"
FONT = "Arial"

# formatos de número (pt-BR renderiza # ##0 com ponto de milhar)
F_MONEY = 'R$ #,##0'
F_MONEY_NEG = '"R$ "#,##0;"-R$ "#,##0'
F_PCT = '0.0%'
F_NUM = '#,##0'
F_MULT = '0.00"x"'

# ============================ FORMATADORES DE TEXTO ============================
def _dot(n):
    return f"{n:,.0f}".replace(",", ".")

def money_card(v):
    return f"R$ {_dot(round(v))}"

def money_tab(v):
    return f"R${_dot(round(v))}"

def delta_money(v):
    s = "+" if v >= 0 else "-"
    return f"{s}R${_dot(round(abs(v)))}"

def pct1(v):
    if abs(v) < 1e-9:
        return "0%"
    return f"{v:.1f}%"

def rate(v):
    return f"{v:.0f}%" if abs(v - round(v)) < 1e-9 else f"{v:.1f}%"

def vol(v):
    return _dot(round(v))

def cumsum(xs):
    out, s = [], 0
    for x in xs:
        s += x
        out.append(s)
    return out

# ============================ HELPERS DE CÉLULA ============================
def col_letter(i):
    """0-based data col -> letra (dados começam em B=2)."""
    return chr(ord('A') + 1 + i)

def put(ws, cell, val, *, size=10, bold=False, color=C_TEXT, fill=None,
        align="center", wrap=False, numfmt=None, italic=False):
    c = ws[cell]
    c.value = val
    c.font = Font(name=FONT, size=size, bold=bold, color=color, italic=italic)
    c.alignment = Alignment(horizontal=align, vertical="center", wrap_text=wrap)
    if fill:
        c.fill = PatternFill("solid", fgColor=fill)
    if numfmt:
        c.number_format = numfmt
    return c

def band(ws, r, text, fill, color, lastcol, size=10, bold=True, align="left"):
    ws.merge_cells(f"A{r}:{chr(ord('A')+lastcol-1)}{r}")
    put(ws, f"A{r}", text, size=size, bold=bold, color=color, fill=fill, align=align)
    for cc in range(1, lastcol + 1):
        ws.cell(row=r, column=cc).fill = PatternFill("solid", fgColor=fill)


# ============================ ABA 1 · RESUMO EXECUTIVO (visual/print) ============================
def build_resumo(ws, cfg, D):
    ws.sheet_view.showGridLines = False
    m = cfg["meses"]
    n = len(m)
    LASTCOL = 1 + n

    def col(i):
        return chr(ord('A') + 1 + i)

    band(ws, 1, f"  FORECAST 12 MESES · COMITÊ DE ELEVAÇÃO · {cfg['cliente'].upper()}",
         C_RED_DEEP, C_WHITE, LASTCOL, size=14)
    ws.row_dimensions[1].height = 30
    band(ws, 2, f"  Meta Anual: {money_card(cfg['meta_anual'])}  ·  Escopo: {cfg['escopo']}  ·  "
                f"AS-IS (não executar) vs Com Injeção (executar o plano)  ·  "
                f"Alavanca governante: conversão antes do checkout (verba estável)",
         C_WHITE, C_SEC, LASTCOL, size=9, bold=False)
    ws.row_dimensions[2].height = 18

    # 5 cartões
    cards = [
        ("MÊS ATUAL", cfg["mes_atual_label"], cfg["mes_atual_pos"], C_LABEL),
        ("FATURAMENTO AS-IS", money_card(D["fat_a"][-1]), f"Acum. 12m: {money_card(D['acc_a'][-1])}", C_ASIS),
        ("COM INJEÇÃO", money_card(D["fat_i"][-1]), f"Acum. 12m: {money_card(D['acc_i'][-1])}", C_INJ),
        ("DELTA", delta_money(D["delta_m"][-1]), f"Acum. 12m: {delta_money(D['delta_acc'][-1])}", C_GREEN),
        ("META ANUAL", money_card(cfg["meta_anual"]), f"{money_card(cfg['meta_mensal'])}/mês run-rate", C_RED_DEEP),
    ]
    card_cols = [("B", "C"), ("D", "E"), ("F", "G"), ("H", "I"), ("J", "K")]
    for (c1, c2), (title, val, sub, accent) in zip(card_cols, cards):
        ws.merge_cells(f"{c1}4:{c2}4")
        ws.merge_cells(f"{c1}5:{c2}5")
        ws.merge_cells(f"{c1}6:{c2}6")
        put(ws, f"{c1}4", title, size=8, bold=True, color=C_LABEL, fill=C_WHITE)
        put(ws, f"{c1}5", val, size=14, bold=True, color=accent, fill=C_WHITE)
        put(ws, f"{c1}6", sub, size=8, bold=False, color=C_SEC, fill=C_WHITE)
        for r in (4, 5, 6):
            for cc in (c1, c2):
                ws[f"{cc}{r}"].fill = PatternFill("solid", fgColor=C_WHITE)
                ws[f"{cc}{r}"].border = Border(
                    bottom=Side(style="thin", color=C_TRACK),
                    top=Side(style="thin", color=C_TRACK),
                    left=Side(style="thin", color=C_TRACK) if cc == c1 else Side(),
                    right=Side(style="thin", color=C_TRACK) if cc == c2 else Side())
    ws.row_dimensions[4].height = 16
    ws.row_dimensions[5].height = 24
    ws.row_dimensions[6].height = 16

    # Progresso
    put(ws, "A8", "PROGRESSO ATÉ A META ANUAL (acumulado)", size=9, bold=True, color=C_TEXT, align="left")
    def bar(r, label, pct, fill_color):
        put(ws, f"A{r}", f"{label}   {pct1(pct)}", size=9, bold=True, color=fill_color, align="left")
        filled = max(0, min(n, round(pct / 100 * n)))
        for i in range(n):
            cc = f"{col(i)}{r}"
            ws[cc].fill = PatternFill("solid", fgColor=fill_color if i < filled else C_TRACK)
            ws[cc].value = None
    bar(9, "AS-IS", D["prog_a"], C_ASIS)
    bar(10, "Com Injeção", D["prog_i"], C_GREEN)
    ws.row_dimensions[9].height = 15
    ws.row_dimensions[10].height = 15

    # Callout run-rate
    ws.merge_cells(f"A12:{chr(ord('A')+LASTCOL-1)}13")
    callout = (f"  RUN-RATE DA META ({money_card(cfg['meta_mensal'])}/mês) atingido no Mês 12 ({m[-1]}).  "
               f"Acumulado Com Injeção: {money_card(D['acc_i'][-1])} = {pct1(D['prog_i'])} da Meta Anual  "
               f"(AS-IS pára em {money_card(D['acc_a'][-1])} = {pct1(D['prog_a'])}).  "
               f"Delta de executar o plano em 12 meses: {delta_money(D['delta_acc'][-1])}.")
    put(ws, "A12", callout, size=10, bold=True, color=C_GREEN, fill=C_CALLOUT, align="left", wrap=True)
    for r in (12, 13):
        for cc in range(1, LASTCOL + 1):
            ws.cell(row=r, column=cc).fill = PatternFill("solid", fgColor=C_CALLOUT)
    ws.row_dimensions[12].height = 22
    ws.row_dimensions[13].height = 22

    # Cabeçalho tabela
    put(ws, "A14", "MÊS", size=9, bold=True, color=C_WHITE, fill=C_RED_DEEP, align="left")
    for i in range(n):
        put(ws, f"{col(i)}14", m[i], size=9, bold=True, color=C_WHITE, fill=C_RED_DEEP)
    ws.row_dimensions[14].height = 20

    r = [15]
    def row(label, values, *, label_color=C_TEXT, val_color=C_TEXT, cell_fill=None,
            bold_val=False, label_bold=False):
        put(ws, f"A{r[0]}", label, size=9, bold=label_bold, color=label_color, align="left")
        for i in range(n):
            put(ws, f"{col(i)}{r[0]}", values[i], size=9, bold=bold_val, color=val_color, fill=cell_fill)
        r[0] += 1

    def secband(text):
        band(ws, r[0], text, C_BAND, C_RED_DEEP, LASTCOL)
        r[0] += 1

    secband("  RECEITA MENSAL")
    row("Receita AS-IS", [money_tab(v) for v in D["fat_a"]], label_color=C_ASIS, val_color=C_ASIS)
    row("Receita Com Injeção", [money_tab(v) for v in D["fat_i"]], label_color=C_INJ, val_color=C_INJ,
        cell_fill=C_CELL_INJ, bold_val=True)
    row("Delta mensal", [delta_money(v) for v in D["delta_m"]], label_color=C_GREEN, val_color=C_GREEN,
        cell_fill=C_CELL_DELTA)
    secband("  RECEITA ACUMULADA")
    row("Acumulado AS-IS", [money_tab(v) for v in D["acc_a"]], label_color=C_ASIS, val_color=C_ASIS)
    row("Acumulado Com Injeção", [money_tab(v) for v in D["acc_i"]], label_color=C_INJ, val_color=C_INJ,
        cell_fill=C_CELL_INJ, bold_val=True)
    secband("  ATINGIMENTO DE META (receita do mês / run-rate alvo)")
    row("Atingimento AS-IS", [pct1(v) for v in D["atg_a"]], label_color=C_ASIS, val_color=C_ASIS)
    row("Atingimento Com Injeção", [pct1(v) for v in D["atg_i"]], label_color=C_INJ, val_color=C_INJ,
        cell_fill=C_CELL_INJ, bold_val=True)
    secband("  ALAVANCAS DE CRESCIMENTO (cenário Com Injeção)")
    row("Ticket médio (fat / base)", [money_tab(v) for v in D["ticket"]])
    row("MER (receita total / mídia)", [f"{v:.1f}x" for v in D["mer"]])
    row("Investimento em mídia", [money_tab(v) for v in D["midia"]])
    row("CAC (mídia / decisão)", [money_tab(v) for v in D["cac"]])
    row(cfg["label_base"], [vol(v) for v in D["base"]])
    row("Churn", ["n/d"] * n, val_color=C_LABEL)
    secband("  FUNIL DE VENDAS (cenário Com Injeção · volumes/mês)")
    row("Exposição · impressões", [vol(v) for v in D["expo"]])
    row(f"Atenção · cliques ({rate(cfg['txAt'][0])} CTR)", [vol(v) for v in D["aten"]])
    row(f"Interesse · add ao carrinho ({rate(cfg['txIn'][0])}→{rate(cfg['txIn'][-1])})", [vol(v) for v in D["inte"]])
    row(f"Qualificação · checkout ({rate(cfg['txQu'][0])}→{rate(cfg['txQu'][-1])})", [vol(v) for v in D["qual"]],
        label_bold=True)
    row(f"Compromisso · pagamento iniciado ({rate(cfg['txCo'][0])}→{rate(cfg['txCo'][-1])})", [vol(v) for v in D["comp"]])
    row(f"{cfg['label_decisao']} ({rate(D['cd0'])}→{rate(D['cd1'])} do clique)", [vol(v) for v in D["deci"]],
        val_color=C_INJ, bold_val=True)
    row(f"Recompra · pedido repetido ({rate(cfg['txRe'][0])}→{rate(cfg['txRe'][-1])})", [vol(v) for v in D["reco"]],
        val_color=C_GREEN)

    # nota de rodapé
    r[0] += 1
    ws.merge_cells(f"A{r[0]}:{chr(ord('A')+LASTCOL-1)}{r[0]+2}")
    nota = ("Nota: forecast modelado (projeção de execução). Pontos de partida ancorados em dado real da Liló Decor "
            "(AOV R$382, conversão 0,4%, add ao carrinho 3,15%, carrinho→checkout 36%, recompra 18,75%, verba R$3.000/mês). "
            "A alavanca do cenário Com Injeção é a trava governante (conversão antes do checkout): a curva sobe por conversão "
            "e recompra com verba estável e exposição flat, não por mais mídia. Churn = n/d (a régua de recompra é o proxy). "
            "Detalhamento e ressalvas nas abas Premissas, Forecast Mensal, Funil, Cenários e Ressalvas. "
            "Pré-requisito para escalar: corrigir a supercontagem do rastreamento Meta↔Shopify.")
    put(ws, f"A{r[0]}", nota, size=8, bold=False, color=C_LABEL, align="left", wrap=True)
    ws.row_dimensions[r[0]].height = 22
    ws.row_dimensions[r[0] + 1].height = 22

    ws.column_dimensions["A"].width = 34
    for i in range(n):
        ws.column_dimensions[col(i)].width = 11.5
    ws.freeze_panes = "B15"


# ============================ ABA 2 · PREMISSAS (drivers editáveis) ============================
def build_premissas(ws, cfg):
    """Escreve os drivers e devolve dict {chave: linha} para as abas modelo referenciarem."""
    ws.sheet_view.showGridLines = False
    n = len(cfg["meses"])
    LASTCOL = 1 + n

    band(ws, 1, "  PREMISSAS DO FORECAST · DRIVERS EDITÁVEIS", C_RED_DEEP, C_WHITE, LASTCOL, size=13)
    ws.row_dimensions[1].height = 26
    band(ws, 2, "  Esta é a fonte de verdade do modelo. As abas Forecast Mensal, Funil, Cenários e Split leem "
                "estas células por fórmula: altere aqui e tudo recalcula. Os valores atuais SÃO a base aprovada.",
         C_WHITE, C_SEC, LASTCOL, size=9, bold=False)
    ws.row_dimensions[2].height = 26
    ws["A2"].alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    # cabeçalho de meses
    put(ws, "A4", "DRIVER", size=9, bold=True, color=C_WHITE, fill=C_RED_DEEP, align="left")
    for i in range(n):
        put(ws, f"{col_letter(i)}4", cfg["meses"][i], size=9, bold=True, color=C_WHITE, fill=C_RED_DEEP)
    ws.row_dimensions[4].height = 20

    rows = {}
    r = [5]

    def secband(text):
        band(ws, r[0], text, C_BAND, C_RED_DEEP, LASTCOL)
        r[0] += 1

    def driver(key, label, values, numfmt, note=""):
        put(ws, f"A{r[0]}", label, size=9, bold=False, color=C_TEXT, align="left")
        for i in range(n):
            put(ws, f"{col_letter(i)}{r[0]}", values[i], size=9, color=C_TEXT,
                fill=C_HEADREF, numfmt=numfmt)
        rows[key] = r[0]
        r[0] += 1

    secband("  META")
    driver("meta", "Meta run-rate mensal (R$)", [cfg["meta_mensal"]] * n, F_MONEY)

    secband("  RECEITA (cenários)")
    driver("fat_asis", "Faturamento AS-IS (R$)", cfg["fat_asis"], F_MONEY)
    driver("fat_inj", "Faturamento Com Injeção (R$)", cfg["fat_inj"], F_MONEY)

    secband("  ALAVANCAS")
    driver("midia", "Investimento em mídia (R$)", cfg["midia"], F_MONEY)
    driver("base", "Base de compradores (un)", cfg["base"], F_NUM)
    driver("expo", "Exposição / impressões (un)", cfg["expo"], F_NUM)

    secband("  TAXAS DE CONVERSÃO DO FUNIL (Com Injeção)")
    driver("txAt", "Exposição → Atenção (CTR)", [v / 100 for v in cfg["txAt"]], F_PCT)
    driver("txIn", "Atenção → Interesse (add carrinho)", [v / 100 for v in cfg["txIn"]], F_PCT)
    driver("txQu", "Interesse → Qualificação (checkout) [TRAVA]", [v / 100 for v in cfg["txQu"]], F_PCT)
    driver("txCo", "Qualificação → Compromisso (pagto iniciado)", [v / 100 for v in cfg["txCo"]], F_PCT)
    driver("txDe", "Compromisso → Decisão (pedido pago)", [v / 100 for v in cfg["txDe"]], F_PCT)
    driver("txRe", "Decisão → Recompra", [v / 100 for v in cfg["txRe"]], F_PCT)

    # constantes de referência (coluna B única)
    secband("  CONSTANTES DE REFERÊNCIA (calibração real Shopify)")
    const = [
        ("meta_anual", "Meta anual (R$)", cfg["meta_anual"], F_MONEY),
        ("aov_real", "AOV atual real (R$)", cfg["aov_real"], F_MONEY),
        ("aov_meta", "AOV meta / sensibilidade (R$)", cfg["aov_meta"], F_MONEY),
        ("breakeven", "Break-even ROAS de mídia (x)", cfg["breakeven_roas"], F_MULT),
    ]
    for key, label, val, fmt in const:
        put(ws, f"A{r[0]}", label, size=9, color=C_TEXT, align="left")
        put(ws, f"B{r[0]}", val, size=9, color=C_TEXT, fill=C_HEADREF, numfmt=fmt)
        rows[key] = r[0]
        r[0] += 1

    ws.column_dimensions["A"].width = 40
    for i in range(n):
        ws.column_dimensions[col_letter(i)].width = 11.5
    ws.freeze_panes = "B5"
    return rows


# ============================ ABA 3 · FORECAST MENSAL (fórmulas) ============================
def build_forecast_mensal(ws, cfg, P):
    ws.sheet_view.showGridLines = False
    n = len(cfg["meses"])
    LASTCOL = 1 + n
    PR = "'Premissas'"
    FU = "'Funil de Vendas'"

    band(ws, 1, "  FORECAST MENSAL · MODELO VIVO (fórmulas)", C_RED_DEEP, C_WHITE, LASTCOL, size=13)
    ws.row_dimensions[1].height = 26
    band(ws, 2, "  Receita, acumulado, atingimento e unit economics calculados a partir da aba Premissas. "
                "MER = receita total da loja / investimento em mídia (eficiência do negócio, não é o ROAS de mídia atribuída).",
         C_WHITE, C_SEC, LASTCOL, size=9, bold=False)
    ws.row_dimensions[2].height = 26
    ws["A2"].alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    put(ws, "A4", "INDICADOR", size=9, bold=True, color=C_WHITE, fill=C_RED_DEEP, align="left")
    for i in range(n):
        put(ws, f"{col_letter(i)}4", cfg["meses"][i], size=9, bold=True, color=C_WHITE, fill=C_RED_DEEP)
    ws.row_dimensions[4].height = 20

    rows = {}
    r = [5]

    def secband(text):
        band(ws, r[0], text, C_BAND, C_RED_DEEP, LASTCOL)
        r[0] += 1

    def frow(key, label, formula_fn, numfmt, *, val_color=C_TEXT, cell_fill=None,
             bold=False, label_bold=False, label_color=C_TEXT):
        rows[key] = r[0]  # set antes de escrever: permite auto-referência (acumulado)
        put(ws, f"A{r[0]}", label, size=9, bold=label_bold, color=label_color, align="left")
        for i in range(n):
            put(ws, f"{col_letter(i)}{r[0]}", formula_fn(i), size=9, bold=bold, color=val_color,
                fill=cell_fill, numfmt=numfmt)
        r[0] += 1

    def pcell(key, i):
        return f"{PR}!{col_letter(i)}{P[key]}"

    secband("  RECEITA MENSAL")
    frow("rec_a", "Receita AS-IS", lambda i: f"={pcell('fat_asis', i)}", F_MONEY,
         val_color=C_ASIS, label_color=C_ASIS)
    frow("rec_i", "Receita Com Injeção", lambda i: f"={pcell('fat_inj', i)}", F_MONEY,
         val_color=C_INJ, label_color=C_INJ, cell_fill=C_CELL_INJ, bold=True)
    frow("delta", "Delta mensal (Injeção − AS-IS)",
         lambda i: f"={col_letter(i)}{rows['rec_i']}-{col_letter(i)}{rows['rec_a']}", F_MONEY_NEG,
         val_color=C_GREEN, label_color=C_GREEN, cell_fill=C_CELL_DELTA)

    secband("  RECEITA ACUMULADA")
    frow("acc_a", "Acumulado AS-IS",
         lambda i: (f"={col_letter(i)}{rows['rec_a']}" if i == 0
                    else f"={col_letter(i-1)}{rows['acc_a']}+{col_letter(i)}{rows['rec_a']}"),
         F_MONEY, val_color=C_ASIS, label_color=C_ASIS)
    frow("acc_i", "Acumulado Com Injeção",
         lambda i: (f"={col_letter(i)}{rows['rec_i']}" if i == 0
                    else f"={col_letter(i-1)}{rows['acc_i']}+{col_letter(i)}{rows['rec_i']}"),
         F_MONEY, val_color=C_INJ, label_color=C_INJ, cell_fill=C_CELL_INJ, bold=True)
    frow("acc_d", "Delta acumulado",
         lambda i: f"={col_letter(i)}{rows['acc_i']}-{col_letter(i)}{rows['acc_a']}", F_MONEY_NEG,
         val_color=C_GREEN, label_color=C_GREEN, cell_fill=C_CELL_DELTA)

    secband("  ATINGIMENTO DE META (receita do mês / run-rate alvo)")
    frow("atg_a", "Atingimento AS-IS",
         lambda i: f"={col_letter(i)}{rows['rec_a']}/{pcell('meta', i)}", F_PCT,
         val_color=C_ASIS, label_color=C_ASIS)
    frow("atg_i", "Atingimento Com Injeção",
         lambda i: f"={col_letter(i)}{rows['rec_i']}/{pcell('meta', i)}", F_PCT,
         val_color=C_INJ, label_color=C_INJ, cell_fill=C_CELL_INJ, bold=True)

    secband("  UNIT ECONOMICS (cenário Com Injeção)")
    frow("ticket", "Ticket médio (receita / base)",
         lambda i: f"={col_letter(i)}{rows['rec_i']}/{pcell('base', i)}", F_MONEY)
    frow("mer", "MER (receita total / mídia)",
         lambda i: f"={col_letter(i)}{rows['rec_i']}/{pcell('midia', i)}", F_MULT, bold=True)
    frow("cac", "CAC (mídia / decisão)",
         lambda i: f"={pcell('midia', i)}/{FU}!{col_letter(i)}$DECI$", F_MONEY)
    frow("midia", "Investimento em mídia", lambda i: f"={pcell('midia', i)}", F_MONEY)
    frow("base", "Base de compradores", lambda i: f"={pcell('base', i)}", F_NUM)

    # databar na receita com injeção
    ws.conditional_formatting.add(
        f"B{rows['rec_i']}:{col_letter(n-1)}{rows['rec_i']}",
        DataBarRule(start_type="num", start_value=0, end_type="max", color=C_RED, showValue=True))

    ws.column_dimensions["A"].width = 34
    for i in range(n):
        ws.column_dimensions[col_letter(i)].width = 11.5
    ws.freeze_panes = "B5"
    return rows


# ============================ ABA 4 · FUNIL DE VENDAS (fórmulas) ============================
def build_funil(ws, cfg, P):
    ws.sheet_view.showGridLines = False
    n = len(cfg["meses"])
    LASTCOL = 1 + n
    PR = "'Premissas'"

    band(ws, 1, "  FUNIL DE VENDAS · MODELO VIVO (fórmulas)", C_RED_DEEP, C_WHITE, LASTCOL, size=13)
    ws.row_dimensions[1].height = 26
    band(ws, 2, "  Volumes por etapa calculados da Exposição pelas taxas da aba Premissas. "
                "A trava governante é Interesse → Qualificação (checkout): é onde a receita vaza hoje.",
         C_WHITE, C_SEC, LASTCOL, size=9, bold=False)
    ws.row_dimensions[2].height = 26
    ws["A2"].alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    put(ws, "A4", "ETAPA", size=9, bold=True, color=C_WHITE, fill=C_RED_DEEP, align="left")
    for i in range(n):
        put(ws, f"{col_letter(i)}4", cfg["meses"][i], size=9, bold=True, color=C_WHITE, fill=C_RED_DEEP)
    ws.row_dimensions[4].height = 20

    rows = {}
    r = [5]

    def secband(text):
        band(ws, r[0], text, C_BAND, C_RED_DEEP, LASTCOL)
        r[0] += 1

    def frow(key, label, formula_fn, numfmt, *, val_color=C_TEXT, bold=False, label_bold=False):
        rows[key] = r[0]
        put(ws, f"A{r[0]}", label, size=9, bold=label_bold, color=val_color, align="left")
        for i in range(n):
            put(ws, f"{col_letter(i)}{r[0]}", formula_fn(i), size=9, bold=bold, color=val_color, numfmt=numfmt)
        r[0] += 1

    def pcell(key, i):
        return f"{PR}!{col_letter(i)}{P[key]}"

    secband("  VOLUMES POR ETAPA (un/mês)")
    frow("expo", "Exposição · impressões", lambda i: f"={pcell('expo', i)}", F_NUM)
    frow("aten", "Atenção · cliques",
         lambda i: f"={col_letter(i)}{rows['expo']}*{pcell('txAt', i)}", F_NUM)
    frow("inte", "Interesse · add ao carrinho",
         lambda i: f"={col_letter(i)}{rows['aten']}*{pcell('txIn', i)}", F_NUM)
    frow("qual", "Qualificação · checkout [TRAVA]",
         lambda i: f"={col_letter(i)}{rows['inte']}*{pcell('txQu', i)}", F_NUM, label_bold=True, bold=True)
    frow("comp", "Compromisso · pagamento iniciado",
         lambda i: f"={col_letter(i)}{rows['qual']}*{pcell('txCo', i)}", F_NUM)
    frow("deci", "Decisão · pedido pago",
         lambda i: f"={col_letter(i)}{rows['comp']}*{pcell('txDe', i)}", F_NUM, val_color=C_INJ, bold=True)
    frow("reco", "Recompra · pedido repetido",
         lambda i: f"={col_letter(i)}{rows['deci']}*{pcell('txRe', i)}", F_NUM, val_color=C_GREEN)

    secband("  TAXAS DE CONVERSÃO (referência · vindas de Premissas)")
    frow("r_at", "CTR (Exposição → Atenção)", lambda i: f"={pcell('txAt', i)}", F_PCT, val_color=C_SEC)
    frow("r_in", "Add carrinho (Atenção → Interesse)", lambda i: f"={pcell('txIn', i)}", F_PCT, val_color=C_SEC)
    frow("r_qu", "Checkout (Interesse → Qualificação)", lambda i: f"={pcell('txQu', i)}", F_PCT, val_color=C_SEC)
    frow("r_co", "Pagto iniciado (Qualif. → Compromisso)", lambda i: f"={pcell('txCo', i)}", F_PCT, val_color=C_SEC)
    frow("r_de", "Pago (Compromisso → Decisão)", lambda i: f"={pcell('txDe', i)}", F_PCT, val_color=C_SEC)
    frow("r_re", "Recompra (Decisão → Recompra)", lambda i: f"={pcell('txRe', i)}", F_PCT, val_color=C_SEC)

    # taxa clique -> pedido (métrica composta)
    secband("  MÉTRICA COMPOSTA")
    frow("clq_ped", "Clique → pedido pago",
         lambda i: f"={col_letter(i)}{rows['deci']}/{col_letter(i)}{rows['aten']}", F_PCT, val_color=C_INJ, bold=True)

    ws.conditional_formatting.add(
        f"B{rows['deci']}:{col_letter(n-1)}{rows['deci']}",
        DataBarRule(start_type="num", start_value=0, end_type="max", color=C_RED, showValue=True))

    ws.column_dimensions["A"].width = 38
    for i in range(n):
        ws.column_dimensions[col_letter(i)].width = 11.5
    ws.freeze_panes = "B5"
    return rows


# ============================ ABA 5 · CENÁRIOS & SENSIBILIDADE ============================
def build_cenarios(ws, cfg, D):
    ws.sheet_view.showGridLines = False
    LASTCOL = 6

    band(ws, 1, "  CENÁRIOS & SENSIBILIDADE", C_RED_DEEP, C_WHITE, LASTCOL, size=13)
    ws.row_dimensions[1].height = 26
    band(ws, 2, "  Base = os números aprovados do forecast. Os cenários de sensibilidade são upsides que "
                "dependem de destravar CRO e ticket: entram como potencial, não estão embutidos na base.",
         C_WHITE, C_SEC, LASTCOL, size=9, bold=False)
    ws.row_dimensions[2].height = 26
    ws["A2"].alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    # comparativo AS-IS vs Injeção (acumulado 12m)
    r = 4
    band(ws, r, "  COMPARATIVO 12 MESES (acumulado)", C_BAND, C_RED_DEEP, LASTCOL); r += 1
    heads = ["INDICADOR", "AS-IS (não executar)", "Com Injeção (executar)", "Delta", "", ""]
    for j, h in enumerate(heads):
        put(ws, f"{chr(ord('A')+j)}{r}", h, size=9, bold=True, color=C_WHITE, fill=C_RED_DEEP,
            align="left" if j == 0 else "center")
    r += 1

    def cmp_row(label, a, i, fmt="money", tone=C_INJ):
        put(ws, f"A{r}", label, size=9, color=C_TEXT, align="left")
        if fmt == "money":
            put(ws, f"B{r}", a, numfmt=F_MONEY, color=C_ASIS, size=9)
            put(ws, f"C{r}", i, numfmt=F_MONEY, color=tone, size=9, bold=True)
            put(ws, f"D{r}", i - a, numfmt=F_MONEY_NEG, color=C_GREEN, size=9, bold=True)
        elif fmt == "pct":
            put(ws, f"B{r}", a / 100, numfmt=F_PCT, color=C_ASIS, size=9)
            put(ws, f"C{r}", i / 100, numfmt=F_PCT, color=tone, size=9, bold=True)
            put(ws, f"D{r}", (i - a) / 100, numfmt=F_PCT, color=C_GREEN, size=9, bold=True)
        return None

    acc_a, acc_i = D["acc_a"][-1], D["acc_i"][-1]
    cmp_row("Receita acumulada 12m", acc_a, acc_i); r += 1
    cmp_row("Receita do mês 12 (run-rate)", D["fat_a"][-1], D["fat_i"][-1]); r += 1
    cmp_row("Atingimento da meta anual", D["prog_a"], D["prog_i"], fmt="pct"); r += 1
    # decisão/pedidos acumulados (funil injeção)
    ped_i = sum(D["deci"])
    put(ws, f"A{r}", "Pedidos pagos acumulados 12m (funil Injeção)", size=9, color=C_TEXT, align="left")
    put(ws, f"C{r}", round(ped_i), numfmt=F_NUM, color=C_INJ, size=9, bold=True); r += 1
    r += 1

    # sensibilidade
    band(ws, r, "  SENSIBILIDADE (upside sobre a base · não embutido)", C_BAND, C_RED_DEEP, LASTCOL); r += 1
    for j, h in enumerate(["ALAVANCA", "PREMISSA DO UPSIDE", "EFEITO NA BASE", "", "", ""]):
        put(ws, f"{chr(ord('A')+j)}{r}", h, size=9, bold=True, color=C_WHITE, fill=C_RED_DEEP,
            align="left")
    ws.merge_cells(f"C{r}:F{r}")
    r += 1

    sens = [
        ("AOV → R$450 (meta)",
         "Ticket sobe de ~R$382 para R$450 sem gastar R$1 a mais em mídia (embalagem premium, kits, frete grátis acima de R$399).",
         f"Receita e MER sobem ~18% no mês. Ex.: o mês de pico iria de {money_card(D['fat_i'][-1])} para ~{money_card(D['fat_i'][-1]*450/382)}."),
        ("CRO destravado",
         "Add ao carrinho 3,15% → 4,5% e carrinho→checkout 36% → 50% (cenário destravado do diagnóstico de funil).",
         "Pedidos pagos sobem +30% a +40% sobre a base, sem mídia adicional. Cada ponto de CRO vira pedido de graça."),
        ("Recompra → 30%",
         "Régua de CRM leva a recompra de 18,75% para ~30% (a 'recompra' do funil já sobe de 18% para 30% na base).",
         "LTV e receita recorrente crescem; reduz a dependência de aquisição paga mês a mês."),
    ]
    for alav, prem, efe in sens:
        put(ws, f"A{r}", alav, size=9, bold=True, color=C_INJ, align="left", wrap=True)
        put(ws, f"B{r}", prem, size=9, color=C_TEXT, align="left", wrap=True)
        ws.merge_cells(f"C{r}:F{r}")
        put(ws, f"C{r}", efe, size=9, color=C_GREEN, align="left", wrap=True)
        ws.row_dimensions[r].height = 42
        r += 1

    r += 1
    band(ws, r, "  RISCOS QUE LIMITAM A CURVA", C_BAND, C_RED_DEEP, LASTCOL); r += 1
    riscos = [
        "Rastreamento: enquanto a supercontagem do servidor e o CAPI não forem corrigidos, o ROAS aparente está inflado e o número real é desconhecido. Pré-requisito inegociável para escalar.",
        "Sazonalidade: Julho e Agosto são historicamente fracos em decoração (ressalva: no ano passado Julho foi o melhor mês). O pico real é o Q4 (Black Friday e Natal de gifting).",
        "Margem: contribuição de 35% com descontos de R$63 mil e devoluções em alta no trimestre. O MER saudável não garante o lucro se desconto e devolução não forem contidos.",
        "Execução de CRO (time técnico): sem corrigir o 'Esgotado' falso, frete grátis exposto cedo e CTA sticky no mobile, o funil fica na base, sem o upside.",
    ]
    for risco in riscos:
        ws.merge_cells(f"A{r}:F{r}")
        put(ws, f"A{r}", "•  " + risco, size=9, color=C_SEC, align="left", wrap=True)
        ws.row_dimensions[r].height = 32
        r += 1

    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 40
    for c in ("C", "D", "E", "F"):
        ws.column_dimensions[c].width = 16


# ============================ ABA 6 · SPLIT DE MÍDIA ============================
def build_split(ws, cfg):
    ws.sheet_view.showGridLines = False
    LASTCOL = 4

    band(ws, 1, "  SPLIT DE MÍDIA · R$3.000/MÊS (70% Meta / 30% Google)", C_RED_DEEP, C_WHITE, LASTCOL, size=13)
    ws.row_dimensions[1].height = 26
    band(ws, 2, "  Alocação por canal e campanha, consistente com o investimento flat de R$3.000/mês do forecast. "
                "A curva sobe pela eficiência (religar o que converte e destravar o funil), não pela verba.",
         C_WHITE, C_SEC, LASTCOL, size=9, bold=False)
    ws.row_dimensions[2].height = 26
    ws["A2"].alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    r = 4
    for canal, dados in MIDIA_SPLIT.items():
        band(ws, r, f"  {canal.upper()}  ·  {dados['pct']}%  ·  {money_card(dados['total'])}/mês",
             C_BAND, C_RED_DEEP, LASTCOL); r += 1
        for j, h in enumerate(["CAMPANHA", "TIPO", "VERBA/MÊS", "PAPEL"]):
            put(ws, f"{chr(ord('A')+j)}{r}", h, size=9, bold=True, color=C_WHITE, fill=C_RED_DEEP,
                align="left" if j != 2 else "center")
        r += 1
        for nome, tipo, verba, papel in dados["campanhas"]:
            put(ws, f"A{r}", nome, size=9, bold=True, color=C_TEXT, align="left", wrap=True)
            put(ws, f"B{r}", tipo, size=9, color=C_SEC, align="left")
            put(ws, f"C{r}", verba, size=9, color=C_INJ, bold=True, numfmt=F_MONEY, align="center")
            put(ws, f"D{r}", papel, size=9, color=C_SEC, align="left", wrap=True)
            ws.row_dimensions[r].height = 30
            r += 1
        # subtotal
        put(ws, f"A{r}", "Subtotal", size=9, bold=True, color=C_RED_DEEP, align="left")
        put(ws, f"C{r}", dados["total"], size=9, bold=True, color=C_RED_DEEP, numfmt=F_MONEY, align="center")
        r += 2

    band(ws, r, "  TOTAL MENSAL", C_BAND, C_RED_DEEP, LASTCOL); r += 1
    put(ws, f"A{r}", "Investimento total em mídia", size=10, bold=True, color=C_TEXT, align="left")
    put(ws, f"C{r}", 3000, size=10, bold=True, color=C_RED_DEEP, numfmt=F_MONEY, align="center")
    r += 2

    ws.merge_cells(f"A{r}:D{r+2}")
    nota = ("ROAS de mídia atribuída (métrica de campanha, base diferente do MER da loja): projetado de 2,55x em Julho "
            "(conta reaquecendo) a 3,57x no pico de Black Friday, sobre break-even de 2,9x. Pré-requisito: corrigir a "
            "supercontagem do rastreamento servidor antes de escalar, senão o ROAS aparente mede fumaça. Marketplaces "
            "(Amazon, Mercado Livre, Shopee, Westwing) ficam fora por corroerem a margem de 35%.")
    put(ws, f"A{r}", nota, size=8, color=C_LABEL, align="left", wrap=True)
    ws.row_dimensions[r].height = 22

    ws.column_dimensions["A"].width = 34
    ws.column_dimensions["B"].width = 22
    ws.column_dimensions["C"].width = 14
    ws.column_dimensions["D"].width = 52


# ============================ ABA 7 · PREMISSAS & RESSALVAS ============================
def build_ressalvas(ws, cfg):
    ws.sheet_view.showGridLines = False
    LASTCOL = 1

    band(ws, 1, "  PREMISSAS & RESSALVAS", C_RED_DEEP, C_WHITE, LASTCOL, size=13)
    ws.row_dimensions[1].height = 26

    r = 3
    def section(title, itens):
        nonlocal r
        ws.merge_cells(f"A{r}:A{r}")
        put(ws, f"A{r}", title, size=10, bold=True, color=C_RED_DEEP, align="left", fill=C_BAND)
        r += 1
        for it in itens:
            put(ws, f"A{r}", it, size=9, color=C_TEXT, align="left", wrap=True)
            # altura proporcional ao tamanho do texto
            ws.row_dimensions[r].height = max(28, 14 * (1 + len(it) // 105))
            r += 1
        r += 1

    section("Base de calibração (dado real Shopify · Liló Decor)", [
        "AOV atual de R$382 e conversão online de 0,4%. A meta de AOV de R$450 entra como upside de MER, não está na base.",
        "Add ao carrinho de 3,15%, carrinho para checkout de 36% e checkout para pago de 35,5% (este já saudável). Recompra de 18,75%.",
        "Verba de mídia estabilizada em R$3.000/mês por 12 meses, revertendo a queda de Abril (R$3.000) para Junho (R$300).",
        "Break-even de ROAS de mídia atribuída de 2,9x. Margem de contribuição de 35%.",
    ])

    section("Alavanca governante", [
        "O cenário Com Injeção NÃO cresce por mais mídia: a verba é flat e a exposição é flat. Cresce por conversão e recompra.",
        "A trava é Interesse para Qualificação (add ao carrinho para checkout): é onde a receita vaza hoje, não no checkout, que já converte bem.",
        "Cada ponto de CRO vira pedido sem custo de mídia adicional. Por isso o CAC cai ao longo dos 12 meses com verba constante.",
    ])

    section("MER x ROAS (não confundir)", [
        "MER (receita total da loja / investimento em mídia) é a eficiência do negócio inteiro. No forecast varia de ~6,7x a ~13,3x porque a receita total é muito maior que a mídia. É indicador de negócio, não de campanha.",
        "ROAS de mídia atribuída (receita atribuída à campanha / verba da campanha) é a métrica de mídia, projetada de 2,55x a 3,57x sobre break-even 2,9x. Base diferente do MER: não somar nem comparar diretamente.",
    ])

    section("Pré-requisitos inegociáveis", [
        "Corrigir a supercontagem do rastreamento servidor e instalar o CAPI/GTM completo ANTES de escalar. Hoje o servidor conta 4 onde o Shopify conta 3, inflando o ROAS aparente. O Shopify é a fonte de verdade dos pedidos.",
        "Religar o retargeting DPA (ROAS 4,5x) e o catálogo ASC (3,4x) que estavam pausados, e encerrar os boosts avulsos de post.",
        "Executar as ações de CRO em paralelo (time técnico): corrigir o 'Esgotado' falso do estoque, expor frete grátis acima de R$399 cedo, CTA sticky no mobile, autoria nomeada e prova social.",
    ])

    section("Ressalvas de honestidade", [
        "Este forecast é uma projeção condicional, não uma promessa. A maior fonte de incerteza é a medição: enquanto o tracking não for corrigido, o número real é desconhecido.",
        "Os pedidos pagos dependem tanto da mídia quanto das ações de CRO e CRM do time técnico. Sem destravar o site, o forecast fica na base, sem o upside.",
        "Sazonalidade: Julho e Agosto são historicamente fracos em decoração (ressalva: no ano passado Julho foi o melhor mês). O pico real é o Q4.",
        "Revisar este forecast mensalmente com o dado real do Shopify. A primeira revisão, em Agosto, já recalibra as premissas de Julho.",
        "Churn não é medido isoladamente (n/d). A régua de recompra é o proxy usado no modelo.",
    ])

    ws.column_dimensions["A"].width = 120


# ============================ COMPUTO DERIVADO (para abas estáticas) ============================
def derive(cfg):
    n = len(cfg["meses"])
    fat_a, fat_i = cfg["fat_asis"], cfg["fat_inj"]
    midia, base, expo = cfg["midia"], cfg["base"], cfg["expo"]
    meta_a, meta_m = cfg["meta_anual"], cfg["meta_mensal"]
    acc_a, acc_i = cumsum(fat_a), cumsum(fat_i)
    delta_m = [fat_i[i] - fat_a[i] for i in range(n)]
    delta_acc = cumsum(delta_m)
    atg_a = [fat_a[i] / meta_m * 100 for i in range(n)]
    atg_i = [fat_i[i] / meta_m * 100 for i in range(n)]
    ticket = [fat_i[i] / base[i] for i in range(n)]
    mer = [fat_i[i] / midia[i] for i in range(n)]
    aten = [expo[i] * cfg["txAt"][i] / 100 for i in range(n)]
    inte = [aten[i] * cfg["txIn"][i] / 100 for i in range(n)]
    qual = [inte[i] * cfg["txQu"][i] / 100 for i in range(n)]
    comp = [qual[i] * cfg["txCo"][i] / 100 for i in range(n)]
    deci = [comp[i] * cfg["txDe"][i] / 100 for i in range(n)]
    reco = [deci[i] * cfg["txRe"][i] / 100 for i in range(n)]
    cac = [midia[i] / deci[i] for i in range(n)]
    return {
        "fat_a": fat_a, "fat_i": fat_i, "midia": midia, "base": base, "expo": expo,
        "acc_a": acc_a, "acc_i": acc_i, "delta_m": delta_m, "delta_acc": delta_acc,
        "atg_a": atg_a, "atg_i": atg_i, "ticket": ticket, "mer": mer,
        "aten": aten, "inte": inte, "qual": qual, "comp": comp, "deci": deci, "reco": reco, "cac": cac,
        "prog_a": acc_a[-1] / meta_a * 100, "prog_i": acc_i[-1] / meta_a * 100,
        "cd0": deci[0] / aten[0] * 100, "cd1": deci[-1] / aten[-1] * 100,
    }


# ============================ MAIN ============================
def build(cfg):
    D = derive(cfg)
    wb = Workbook()

    ws_resumo = wb.active
    ws_resumo.title = "Resumo Executivo"
    build_resumo(ws_resumo, cfg, D)
    ws_resumo.sheet_properties.tabColor = C_RED_DEEP

    ws_prem = wb.create_sheet("Premissas")
    P = build_premissas(ws_prem, cfg)
    ws_prem.sheet_properties.tabColor = C_RED

    ws_fm = wb.create_sheet("Forecast Mensal")
    FM = build_forecast_mensal(ws_fm, cfg, P)
    ws_fm.sheet_properties.tabColor = C_RED

    ws_fu = wb.create_sheet("Funil de Vendas")
    FU = build_funil(ws_fu, cfg, P)
    ws_fu.sheet_properties.tabColor = C_RED

    # CAC referencia a linha Decisão do Funil: injeta o número da linha no placeholder
    deci_row = FU["deci"]
    for i in range(len(cfg["meses"])):
        cell = ws_fm.cell(row=FM["cac"], column=2 + i)
        cell.value = cell.value.replace(f"{col_letter(i)}$DECI$", f"{col_letter(i)}{deci_row}")

    ws_cen = wb.create_sheet("Cenários & Sensibilidade")
    build_cenarios(ws_cen, cfg, D)
    ws_cen.sheet_properties.tabColor = C_GREEN

    ws_split = wb.create_sheet("Split de Mídia")
    build_split(ws_split, cfg)
    ws_split.sheet_properties.tabColor = C_RED

    ws_res = wb.create_sheet("Premissas & Ressalvas")
    build_ressalvas(ws_res, cfg)
    ws_res.sheet_properties.tabColor = C_LABEL

    # força o recálculo das fórmulas ao abrir (Excel / Google Sheets / LibreOffice)
    wb.calculation.fullCalcOnLoad = True

    os.makedirs(os.path.dirname(cfg["saida"]), exist_ok=True)
    wb.save(cfg["saida"])

    print(f"OK -> {cfg['saida']}")
    print(f"  Abas: {wb.sheetnames}")
    print(f"  AS-IS acc 12m:   {money_card(D['acc_a'][-1])}  ({pct1(D['prog_a'])} da meta)")
    print(f"  Com Injeção 12m: {money_card(D['acc_i'][-1])}  ({pct1(D['prog_i'])} da meta)")
    print(f"  Delta acc 12m:   {delta_money(D['delta_acc'][-1])}")
    print(f"  Run-rate mês 12: {money_card(D['fat_i'][-1])}  (meta {money_card(cfg['meta_mensal'])})")
    print(f"  Ticket {money_tab(D['ticket'][0])}→{money_tab(D['ticket'][-1])} · "
          f"MER {D['mer'][0]:.1f}x→{D['mer'][-1]:.1f}x · CAC {money_tab(D['cac'][0])}→{money_tab(D['cac'][-1])} · "
          f"decisão {vol(D['deci'][0])}→{vol(D['deci'][-1])}/mês · pedidos 12m {vol(sum(D['deci']))}")


if __name__ == "__main__":
    build(CONFIG)
