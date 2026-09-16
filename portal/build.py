#!/usr/bin/env python3
"""Monta as páginas estáticas do portal a partir dos fragmentos em _src/.

Cada fragmento começa com uma linha de metadados:
    <!--@ slug | Título da aba | Título da página | Descrição | Meta lateral -->
seguida do markup. Rode `python3 build.py` na pasta portal/.

O slug pode ser um caminho, como `destrava/identificar`. Nesse caso a página vive
em destrava/identificar/index.html, a aba do pai (`destrava`) fica marcada como
atual, e a barra de título ganha um link de volta para o pai. Só o primeiro
segmento precisa existir no NAV: página filha não vira aba.

A aba Diagnósticos tem uma segunda fonte: a BIBLIOTECA, que publica documentos
Markdown do repositório como páginas do portal (ver `md.py`). O fragmento
`_src/diagnosticos.html` recebe a lista gerada no lugar do marcador
`<!--@biblioteca-->`, e cada documento vira `diagnosticos/<slug>/index.html`.
"""
import datetime, functools, hashlib, pathlib, re, subprocess, sys
import md as markdown

ROOT = pathlib.Path(__file__).parent
SRC  = ROOT / "_src"
REPO = ROOT.parent

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
    ("painel",       "Painel",     "/"),
    ("kickoff",      "Kick-off",   "/kickoff"),
    ("receita",      "Receita",    "/receita"),
    ("cronograma",   "Cronograma", "/cronograma"),
    ("destrava",     "Destrava Receita", "/destrava"),
    ("diagnosticos", "Diagnósticos", "/diagnosticos"),
    ("metricas",     "Métricas",   "/metricas"),
]

# ---------------------------------------------------------------------------
# Biblioteca: documentos do repositório publicados no portal.
#
# A lista é curada à mão, e é ela que decide o que a OLX vê. O que não está aqui
# não é publicado: transcrição integral, PENDENCIAS.md, contrato e material de
# método da V4 ficam de fora por confidencialidade ou por serem registro interno.
# Acrescentar linha aqui publica o documento; não há varredura automática de pasta.
# ---------------------------------------------------------------------------
GRUPOS = [
    ("entregues", "Diagnósticos técnicos com documento",
     "Dos nove contratados, estes já têm análise escrita. Os outros sete fecham em 18 de setembro."),
    ("sistema", "A leitura do sistema de receita",
     "O que os diagnósticos alimentam: o fluxo ponta a ponta, o placar das travas e a maturidade."),
    ("dados", "Dados, acessos e o que ainda falta",
     "O estado da coleta, item a item, e o que depende do time do Grupo OLX."),
    ("sessoes", "Registro das sessões com o time",
     "A camada experiencial do diagnóstico: o que foi dito em sessão, por quem, e o que virou achado."),
]

BIBLIOTECA = [
    dict(slug="rastreamento", grupo="entregues",
         origem="02-diagnostico/auditoria-vii-rastreamento.md",
         titulo="(vii) Rastreamento · GA4 e GTM", selo="fechado · 11 set", tom="ok",
         resumo="60 contêineres de GTM em 4 contas e 1.779 tags lidas uma a uma, mais a "
                "configuração do GA4 por API. 43 achados numerados, e o achado 1 confirmado "
                "na versão que está em produção."),
    dict(slug="midia-paga", grupo="entregues",
         origem="02-diagnostico/diagnostico-vi-midia-paga.md",
         titulo="(vi) Mídia Paga · Google e Meta", selo="plataforma fechada · 16 set", tom="ok",
         resumo="Cinco contas de Google Ads exportadas direto da interface, R$ 70,96 milhões e 177 "
                "campanhas, lidas por oito frentes com verificação adversarial. O parque é 4,1 vezes "
                "maior do que o projeto media, e a coluna de conversão da plataforma não conta negócio."),
    dict(slug="crm-marketing", grupo="entregues",
         origem="02-diagnostico/auditoria-i-crm-marketing.md",
         titulo="(i) CRM Marketing · Salesforce", selo="experiencial fechada", tom="andando",
         resumo="As duas sessões de 09 e 10 de setembro com todo o time de CRM B2B, 2h08 de "
                "registro, 16 achados. A camada de ferramenta ainda depende de base, relatório "
                "de performance e console."),

    dict(slug="fluxo-de-receita", grupo="sistema",
         origem="02-diagnostico/fluxo-de-receita.md",
         titulo="Fluxo de receita ponta a ponta", selo="em construção", tom="andando",
         resumo="O mapa do sistema que produz receita, etapa a etapa, com volume e taxa onde "
                "existe dado apurado e vazio declarado onde não existe."),
    dict(slug="dashboards-aquisicao", grupo="sistema",
         origem="02-diagnostico/dashboards-aquisicao-pro.md",
         titulo="Dashboards de aquisição PRO", selo="recebido · 16 set", tom="ok",
         resumo="Os dois relatórios de Looker do Grupo OLX, lidos print a print: 13 meses de "
                "funil por canal, o primeiro CAC de mídia com numerador B2B, e três "
                "reconciliações, uma delas contra a própria apresentação de Inside Sales."),
    dict(slug="travas", grupo="sistema",
         origem="02-diagnostico/diagnostico-travas.md",
         titulo="Placar das 8 travas", selo="2 de 8 fechadas", tom="andando",
         resumo="Cada trava pontuada em cinco dimensões de 0 a 5, com a evidência que sustenta "
                "cada nota e a regra que limita a 3 tudo que não tem evidência formal."),
    dict(slug="trava-cegueira", grupo="sistema",
         origem="02-diagnostico/trava-cegueira.md",
         titulo="Dossiê da Trava de Cegueira", selo="pontuada", tom="ok",
         resumo="A trava que é pré-condição das outras sete: enquanto a medição estiver assim, "
                "nenhuma taxa do funil B2B pode ser derivada de dado."),
    dict(slug="maturidade-digital", grupo="sistema",
         origem="02-diagnostico/maturidade-digital.md",
         titulo="Maturidade digital", selo="em construção", tom="andando",
         resumo="A leitura por prática e não por ferramenta: o que a operação faz de fato em "
                "mídia, conteúdo, CRM, conversão e dados."),
    dict(slug="jornada-do-cliente", grupo="sistema",
         origem="02-diagnostico/jornada-do-cliente-profissional.md",
         titulo="Jornada do cliente profissional", selo="declarada pela OLX", tom="nota",
         resumo="As seis etapas apresentadas pelo Grupo OLX em 28 de agosto e as seis taxas "
                "declaradas na sessão, com o que cada uma abre e o que ela ainda não fecha."),
    dict(slug="mapa-de-numeros", grupo="sistema",
         origem="02-diagnostico/mapa-de-numeros.md",
         titulo="Mapa de números", selo="referência", tom="nota",
         resumo="Todo número que circula no projeto com fonte, data e recorte. É aqui que se "
                "confere se um dado é apurado, declarado ou estimado."),
    dict(slug="serie-de-receita", grupo="sistema",
         origem="02-diagnostico/serie-de-receita-2025-2026.md",
         titulo="Série de receita 2025–2026", selo="bloco A1 recebido", tom="ok",
         resumo="A série mensal entregue em 28 de agosto, o que ela sustenta e o que ainda falta "
                "para fechar a matemática do forecast."),
    dict(slug="lacunas-do-fluxo", grupo="sistema",
         origem="02-diagnostico/lacunas-do-fluxo-de-receita.md",
         titulo="Lacunas do fluxo de receita", selo="caderno vivo", tom="nota",
         resumo="O que falta ou está errado no fluxo, em lista aberta, com o que entra no "
                "formulário e o que depende de dado do Grupo OLX."),

    dict(slug="os-nove-contratados", grupo="dados",
         origem="02-diagnostico/auditorias-contratadas.md",
         titulo="Os nove diagnósticos do contrato", selo="mapa do escopo", tom="nota",
         resumo="Cada diagnóstico contratado com o bloco de dados que o alimenta, a janela, o "
                "quanto ele custa de hora do time da OLX e as travas que informa."),
    dict(slug="checklist-de-dados", grupo="dados",
         origem="02-diagnostico/checklist-dados-e-acessos.md",
         titulo="Checklist de dados e acessos", selo="10 blocos · A a J", tom="nota",
         resumo="Os dez blocos de dados, item a item, com o estado de cada acesso concedido e "
                "de cada entrega de dado ainda pendente."),
    dict(slug="coleta-pendente", grupo="dados",
         origem="02-diagnostico/coleta-pendente.md",
         titulo="Coleta pendente", selo="o que falta chegar", tom="alerta",
         resumo="A lista de controle do que ainda precisa vir do lado do Grupo OLX para os "
                "diagnósticos fecharem sem limitação declarada."),
    dict(slug="guia-export-gtm", grupo="dados",
         origem="02-diagnostico/guia-export-gtm.md",
         titulo="Guia de export do GTM", selo="operacional", tom="nota",
         resumo="Como exportar um contêiner do GTM em JSON, passo a passo, e por que export de "
                "espaço de trabalho não substitui a versão publicada."),

    dict(slug="sessao-jornada-28-08", grupo="sessoes",
         origem="06-reunioes/2026-08-28-jornada-do-cliente.md",
         titulo="Jornada do cliente · 28 de agosto", selo="realizada", tom="ok",
         resumo="A sessão de mapeamento do fluxo de receita com o time de operação, contada por "
                "quem opera, para ser cruzada depois com o dado do sistema."),
    dict(slug="sessao-crm-09-09", grupo="sessoes",
         origem="06-reunioes/2026-09-09-crm-contexto-e-campana.md",
         titulo="CRM · parte 1 · 09 de setembro", selo="realizada", tom="ok",
         resumo="O contexto da migração, o Campana e o que parou em março. É a sessão que abre "
                "o diagnóstico (i)."),
    dict(slug="sessao-crm-10-09", grupo="sessoes",
         origem="06-reunioes/2026-09-10-crm-jornadas.md",
         titulo="CRM · parte 2 · 10 de setembro", selo="realizada", tom="ok",
         resumo="O mapa das 15 jornadas de relacionamento e o que está no ar depois da migração. "
                "É onde aparece o achado do ciclo de vida desligado."),
]

POR_ORIGEM = {d["origem"]: d for d in BIBLIOTECA}

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


def escrever(slug, title, ch, cd, cm, corpo, layout_doc=True):
    """Grava uma página do portal. `corpo` já vem em HTML."""
    raiz = slug.split("/")[0]
    if raiz not in {s for s, _, _ in NAV}:
        sys.exit(f"slug '{slug}' não está no NAV")
    # Página filha guarda o pai para o link de volta; página de topo não tem.
    pai = next(((rot, href) for s_, rot, href in NAV if s_ == raiz), None) \
        if "/" in slug else None
    out = ROOT / ("index.html" if slug == "painel" else f"{slug}/index.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    if layout_doc:
        corpo = (f'<div class="doc" id="doc"><div class="doc-main">{corpo}</div>{rail()}</div>'
                 '<button class="rail-abrir" id="rail-abrir" type="button" hidden>Nesta página</button>')
    out.write_text(DOC.format(
        fav=v("/assets/favicon.svg"), apple=v("/assets/apple-icon.png"),
        basecss=v("/assets/base.css"), shellcss=v("/assets/shell.css"),
        shelljs=v("/assets/shell.js"),
        title=title, desc=cd.replace('"', "&quot;"),
        topbar=topbar(raiz), crumb=crumb(ch, cd, cm, pai),
        body=corpo, footer=FOOTER), encoding="utf-8")
    print(f"  {out.relative_to(ROOT)}  ({len(out.read_text(encoding='utf-8')):,} bytes)")


# ------------------------------------------------------------------ biblioteca
@functools.lru_cache(maxsize=None)
def atualizado(origem):
    """Data da última alteração do documento, pelo git, com o mtime como reserva."""
    try:
        saida = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", origem],
            cwd=REPO, capture_output=True, text=True, timeout=10).stdout.strip()
        if saida:
            a, m, d = saida.split("-")
            return f"{d}/{m}/{a}"
    except (OSError, ValueError, subprocess.SubprocessError):
        pass
    ts = (REPO / origem).stat().st_mtime
    return datetime.date.fromtimestamp(ts).strftime("%d/%m/%Y")


def resolvedor(origem):
    """Traduz os links de um documento do repositório para links do portal.

    O que aponta para documento publicado vira URL do portal; o que aponta para
    arquivo interno perde o link e continua como texto, para não oferecer ao
    cliente um caminho que ele não pode abrir.
    """
    base = pathlib.PurePosixPath(origem).parent

    def resolver(href):
        if href.startswith(("http://", "https://", "mailto:", "#", "/")):
            return href
        alvo, _, ancora = href.partition("#")
        if not alvo:
            return href
        doc = POR_ORIGEM.get("/".join(_normalizar(base / alvo)))
        if not doc:
            return None
        return f"/diagnosticos/{doc['slug']}" + (f"#{ancora}" if ancora else "")

    return resolver


def _normalizar(caminho):
    partes = []
    for p in pathlib.PurePosixPath(caminho).parts:
        if p == "..":
            if partes:
                partes.pop()
        elif p != ".":
            partes.append(p)
    return partes


def biblioteca_html():
    """A lista de documentos que entra no fragmento da aba Diagnósticos."""
    blocos = []
    for chave, titulo, sub in GRUPOS:
        # Mesmo corte de build_biblioteca(): documento sem fonte no disco nao ganha cartao,
        # senao a lista ofereceria link para pagina que nao foi gerada.
        docs = [d for d in BIBLIOTECA if d["grupo"] == chave and (REPO / d["origem"]).exists()]
        if not docs:
            continue
        cartoes = []
        for d in docs:
            cartoes.append(
                f'<a class="bib-card" href="/diagnosticos/{d["slug"]}">'
                f'<span class="bib-selo bib-{d["tom"]}">{d["selo"]}</span>'
                f'<h4>{d["titulo"]}</h4><p>{d["resumo"]}</p>'
                f'<span class="bib-pe"><span class="bib-abrir">Abrir documento ›</span>'
                f'<span class="bib-data">atualizado em {atualizado(d["origem"])}</span></span></a>')
        blocos.append(
            f'<div class="bib-grupo"><h3>{titulo}</h3><p class="bib-sub">{sub}</p>'
            f'<div class="bib-cards">{"".join(cartoes)}</div></div>')
    return '<div class="bib">' + "".join(blocos) + "</div>"


def build_biblioteca():
    """Publica cada documento da BIBLIOTECA como página do portal."""
    for d in BIBLIOTECA:
        fonte = REPO / d["origem"]
        if not fonte.exists():
            # Fonte que ainda nao existe nao derruba o build: o repositorio e escrito por
            # mais de uma sessao ao mesmo tempo, e um documento pode estar listado aqui
            # antes de ser commitado. O aviso sai em vez do erro, para o corte ficar visivel.
            print(f"  ! sem fonte, nao publicado: {d['origem']}  ({d['titulo']})")
            continue
        titulo_doc, corpo = markdown.render(fonte.read_text(encoding="utf-8"),
                                            resolvedor(d["origem"]))
        rodape = (f'<p class="md-fonte">Documento-fonte do projeto: <code>{d["origem"]}</code> · '
                  f'atualizado em {atualizado(d["origem"])} · '
                  f'<a href="/diagnosticos">voltar para Diagnósticos</a></p>')
        escrever(f"diagnosticos/{d['slug']}",
                 f"{d['titulo']} · Portal DR-E Grupo OLX",
                 d["titulo"], d["resumo"],
                 f"atualizado em {atualizado(d['origem'])}",
                 f'<article class="md">{corpo}{rodape}</article>')


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
        if slug.split("/")[0] not in {s for s, _, _ in NAV}:
            sys.exit(f"{f.name}: slug '{slug}' não está no NAV")
        body = raw[m.end():]
        # Todo asset referenciado dentro do fragmento ganha versao. Sem isto o
        # form-data.js e o acessos.js ficariam presos ao cache immutable de um ano.
        body = re.sub(
            r'(src|href)="(/assets/[^"?]+)"',
            lambda m: f'{m.group(1)}="{v(m.group(2))}"',
            body,
        )
        if "<!--@biblioteca-->" in body:
            body = body.replace("<!--@biblioteca-->", biblioteca_html())
        escrever(slug, title, ch, cd, cm, body, layout_doc=(slug != "painel"))
    build_biblioteca()


if __name__ == "__main__":
    print("Gerando portal:")
    build()
