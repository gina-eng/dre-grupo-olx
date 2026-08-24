#!/usr/bin/env python3
"""Monta as páginas estáticas do portal a partir dos fragmentos em _src/.

Cada fragmento começa com uma linha de metadados:
    <!--@ slug | Título da aba | Título da página | Descrição | Meta lateral -->
seguida do markup. Rode `python3 build.py` na pasta portal/.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).parent
SRC  = ROOT / "_src"

NAV = [
    ("painel",     "Painel",     "/"),
    ("kickoff",    "Kick-off",   "/kickoff"),
    ("cronograma", "Cronograma", "/cronograma"),
    ("metricas",   "Métricas",   "/metricas"),
]

DOC = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@300..700&family=Geist+Mono:wght@400..600&display=swap">
<link rel="stylesheet" href="/assets/base.css">
<link rel="stylesheet" href="/assets/shell.css">
<script src="/assets/shell.js"></script>
</head>
<body>
{topbar}
{crumb}
{body}
{footer}
</body>
</html>
"""

def topbar(active):
    tabs, drawer = [], []
    for slug, label, href in NAV:
        cur = ' aria-current="page"' if slug == active else ""
        tabs.append(f'<a class="tab" href="{href}"{cur}>{label}</a>')
        drawer.append(f'<a href="{href}"{cur}>{label}</a>')
    return f"""<header class="topbar">
  <div class="topbar-in">
    <button class="icobtn menu-btn" id="menu-btn" type="button" aria-label="Abrir navegação" aria-expanded="false" aria-controls="drawer">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/></svg>
    </button>
    <a class="brand" href="/" aria-label="Início"><img src="/assets/logo.svg" alt="Destrava Receita" width="722" height="279"></a>
    <nav class="tabs" aria-label="Seções">{''.join(tabs)}</nav>
    <span class="spacer"></span>
    <button class="icobtn" id="theme" type="button" aria-label="Alternar tema claro e escuro">Tema</button>
  </div>
</header>
<nav class="drawer" id="drawer" aria-label="Navegação">{''.join(drawer)}</nav>"""

def crumb(h, d, m):
    if not h:
        return ""
    meta = f'<span class="meta">{m}</span>' if m else ""
    return f"""<div class="crumb"><div class="crumb-in">
  <h1>{h}</h1><p class="desc">{d}</p>{meta}
</div></div>"""

FOOTER = """<footer><div class="wrap">
  <p><strong>Destrava Receita Estratégico</strong> · V4 Company × Grupo OLX · contrato de 12 meses
     iniciado em 24 de agosto de 2026.</p>
  <p style="margin-top:.4rem">Acesso restrito. Contém informação confidencial do Grupo OLX —
     não repassar sem autorização escrita.</p>
</div></footer>"""

def build():
    frags = sorted(SRC.glob("*.html"))
    if not frags:
        sys.exit("Nenhum fragmento em _src/")
    for f in frags:
        raw = f.read_text(encoding="utf-8")
        m = re.match(r"<!--@(.*?)-->\s*", raw, re.S)
        if not m:
            sys.exit(f"{f.name}: falta a linha de metadados <!--@ ... -->")
        parts = [p.strip() for p in m.group(1).split("|")]
        while len(parts) < 5:
            parts.append("")
        slug, title, ch, cd, cm = parts[:5]
        if slug not in {s for s, _, _ in NAV}:
            sys.exit(f"{f.name}: slug '{slug}' não está no NAV")
        body = raw[m.end():]
        out = ROOT / ("index.html" if slug == "painel" else f"{slug}/index.html")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(DOC.format(
            title=title, desc=cd.replace('"', "&quot;"),
            topbar=topbar(slug), crumb=crumb(ch, cd, cm),
            body=body, footer=FOOTER), encoding="utf-8")
        print(f"  {out.relative_to(ROOT)}  ({len(out.read_text(encoding='utf-8')):,} bytes)")

if __name__ == "__main__":
    print("Gerando portal:")
    build()
