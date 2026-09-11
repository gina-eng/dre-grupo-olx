#!/usr/bin/env python3
"""Monta as páginas estáticas do portal a partir dos fragmentos em _src/.

Cada fragmento começa com uma linha de metadados:
    <!--@ slug | Título da aba | Título da página | Descrição | Meta lateral -->
seguida do markup. Rode `python3 build.py` na pasta portal/.

O slug pode ser um caminho, como `destrava/identificar`. Nesse caso a página vive
em destrava/identificar/index.html, a aba do pai (`destrava`) fica marcada como
atual, e a barra de título ganha um link de volta para o pai. Só o primeiro
segmento precisa existir no NAV: página filha não vira aba.
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path(__file__).parent
SRC  = ROOT / "_src"

_HASHES = {}

def v(caminho):
    """Anexa um hash do conteúdo à URL do asset.

    Sem isto, o navegador de quem já visitou o portal continua usando o CSS e o JS
    antigos do cache (a regra de max-age em vercel.json), e um deploy novo parece
    não ter mudado nada, porque só o HTML e revalidado.
    """
    if caminho not in _HASHES:
        f = ROOT / caminho.lstrip("/")
        try:
            _HASHES[caminho] = hashlib.sha256(f.read_bytes()).hexdigest()[:8]
        except OSError:
            _HASHES[caminho] = "0"
    return f"{caminho}?v={_HASHES[caminho]}"

NAV = [
    ("painel",     "Painel",     "/"),
    ("kickoff",    "Kick-off",   "/kickoff"),
    ("receita",    "Receita",    "/receita"),
    ("cronograma", "Cronograma", "/cronograma"),
    ("destrava",   "Destrava Receita", "/destrava"),
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
<link rel="icon" href="{fav}" type="image/svg+xml">
<link rel="apple-touch-icon" href="{apple}" sizes="180x180">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap">
<link rel="stylesheet" href="{basecss}">
<link rel="stylesheet" href="{shellcss}">
<script src="{shelljs}"></script>
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
    """Clara nas páginas de documentação, de vidro sobre o vermelho na home."""
    tabs, gaveta = [], []
    for slug, label, href in NAV:
        cur = ' aria-current="page"' if slug == active else ""
        tabs.append(f'<a class="tab" href="{href}"{cur}>{label}</a>')
        gaveta.append(f'<a class="nav-item" href="{href}"{cur}>{label}</a>')
    variante = " topbar--red" if active == "painel" else ""
    menu = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
            '<path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/></svg>')
    fechar = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
              '<path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>')
    return f"""<header class="topbar{variante}">
  <div class="topbar-in">
    <button class="icobtn menu-btn" id="menu-btn" type="button" aria-label="Abrir navegação" aria-expanded="false" aria-controls="drawer">{menu}</button>
    <a class="brand" href="/" aria-label="Início">
      <img class="logo-escuro" src="{v("/assets/logo-dark.svg")}" alt="Destrava Receita" width="722" height="279">
      <img class="logo-claro" src="{v("/assets/logo.svg")}" alt="Destrava Receita" width="722" height="279">
    </a>
    <nav class="tabs" aria-label="Seções">{''.join(tabs)}</nav>
    <span class="spacer"></span>
    <button class="icobtn" id="theme" type="button" aria-label="Alternar tema claro e escuro">Tema</button>
  </div>
</header>
<div class="drawer-bd" id="drawer-bd" hidden></div>
<nav class="drawer" id="drawer" aria-label="Navegação" aria-hidden="true">
  <div class="drawer-h">
    <img src="{v("/assets/logo-dark.svg")}" alt="Destrava Receita" width="722" height="279">
    <button class="icobtn" id="drawer-close" type="button" aria-label="Fechar navegação">{fechar}</button>
  </div>
  <div class="drawer-b">
    <p class="side-label">Portal</p>
    {''.join(gaveta)}
    <p class="side-label" id="dtoc-label" hidden>Nesta página</p>
    <div id="dtoc"></div>
  </div>
</nav>
"""

def crumb(h, d, m, pai=None):
    if not h:
        return ""
    meta = f'<span class="meta">{m}</span>' if m else ""
    volta = ""
    if pai:
        rotulo, href = pai
        seta = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" '
                'aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>')
        volta = f'<a class="volta" href="{href}">{seta}{rotulo}</a>'
    return f"""<div class="crumb"><div class="crumb-in">
  {volta}<h1>{h}</h1><p class="desc">{d}</p>{meta}
</div></div>"""

def rail():
    """Trilho de índice da página, à direita. Preenchido em runtime por shell.js."""
    seta = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="m9 18 6-6-6-6"/></svg>')
    return f"""<aside class="rail" aria-label="Índice da página">
  <div class="rail-top">
    <p class="side-label" id="toc-label" hidden>Nesta página</p>
    <button class="rail-tog" id="rail-tog" type="button" aria-label="Recolher o índice"
            aria-expanded="true" aria-controls="toc" hidden>{seta}</button>
  </div>
  <div id="toc"></div>
</aside>"""

FOOTER = """<footer><div class="wrap">
  <p><strong>Destrava Receita Estratégico</strong> · V4 Company × Grupo OLX · contrato de 12 meses
     iniciado em 24 de agosto de 2026.</p>
  <p style="margin-top:.4rem">Acesso restrito. Contém informação confidencial do Grupo OLX,
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
        raiz = slug.split("/")[0]
        if raiz not in {s for s, _, _ in NAV}:
            sys.exit(f"{f.name}: slug '{slug}' não está no NAV")
        # Página filha guarda o pai para o link de volta; página de topo não tem.
        pai = next(((rot, href) for s_, rot, href in NAV if s_ == raiz), None) \
            if "/" in slug else None
        body = raw[m.end():]
        # Todo asset referenciado dentro do fragmento ganha versao. Sem isto o
        # form-data.js e o acessos.js ficariam presos ao cache immutable de um ano.
        body = re.sub(
            r'(src|href)="(/assets/[^"?]+)"',
            lambda m: f'{m.group(1)}="{v(m.group(2))}"',
            body,
        )
        out = ROOT / ("index.html" if slug == "painel" else f"{slug}/index.html")
        out.parent.mkdir(parents=True, exist_ok=True)
        if slug == "painel":
            corpo = body
        else:
            corpo = (f'<div class="doc" id="doc"><div class="doc-main">{body}</div>{rail()}</div>'
                     '<button class="rail-abrir" id="rail-abrir" type="button" hidden>Nesta página</button>')
        out.write_text(DOC.format(
            fav=v("/assets/favicon.svg"), apple=v("/assets/apple-icon.png"),
            basecss=v("/assets/base.css"), shellcss=v("/assets/shell.css"),
            shelljs=v("/assets/shell.js"),
            title=title, desc=cd.replace('"', "&quot;"),
            topbar=topbar(raiz), crumb=crumb(ch, cd, cm, pai),
            body=corpo, footer=FOOTER), encoding="utf-8")
        print(f"  {out.relative_to(ROOT)}  ({len(out.read_text(encoding='utf-8')):,} bytes)")

if __name__ == "__main__":
    print("Gerando portal:")
    build()
