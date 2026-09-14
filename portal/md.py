#!/usr/bin/env python3
"""Markdown -> HTML no subconjunto que os documentos deste repositório usam.

Sem dependência externa: o portal é estático e o build roda com o Python do sistema.

Suportado: títulos, parágrafos, listas (inclusive de tarefa e aninhadas), tabelas com
alinhamento, citações, blocos de código, régua e, na linha, negrito, itálico, código,
link, autolink e tachado.

**Tudo é escapado antes de qualquer marcação.** HTML escrito dentro do Markdown sai como
texto, nunca como elemento. É o que permite publicar documento do repositório sem auditar
cada arquivo em busca de `<script>`.

Âncoras de título seguem a regra do GitHub (minúscula, pontuação fora, espaço vira hífen),
porque os documentos linkam entre si com âncoras escritas para o GitHub.
"""
import re

ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
ALINHA = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(?:\|\s*:?-{2,}:?\s*)*\|?\s*$")
CERCA = re.compile(r"^\s*(```|~~~)")
REGUA = re.compile(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$")
TITULO = re.compile(r"^\s*(#{1,6})\s+(.*?)\s*#*\s*$")
# Emoji de estado usado como abertura de citação, vira a cor da barra lateral.
SINAL = {"🔴": "grave", "⚠️": "alerta", "🟠": "alerta", "🟡": "alerta",
         "✅": "ok", "🟢": "ok", "🔜": "espera", "⚪": "espera", "ℹ️": "nota"}


def escapar(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def texto_puro(t):
    """O texto de um título sem marcação, que é o que vira âncora e título de aba."""
    t = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[`*_~]", "", t)
    return t.strip()


def _inicia_bloco(linha):
    """Uma linha que abre bloco novo não é continuação de parágrafo nem de item."""
    return bool(CERCA.match(linha) or REGUA.match(linha) or TITULO.match(linha)
                or ITEM.match(linha) or linha.strip().startswith((">", "|")))


def ancora(texto):
    """Mesma regra do GitHub: sem ela, link interno de documento longo aponta para o vazio."""
    s = texto.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


class Conversor:
    """Um por documento: a numeração de âncoras repetidas é por página."""

    def __init__(self, resolver=None):
        # resolver(href) -> URL final, ou None para o link virar texto sem destino.
        self.resolver = resolver or (lambda href: href)
        self.usadas = {}

    # ---------------------------------------------------------------- linha
    def inline(self, t):
        # O código sai antes e volta no fim: sem isto, um link cujo texto é um trecho de
        # código (`[`arquivo.json`](caminho)`) ficaria partido em dois e não viraria link.
        guardados = []

        def guardar(m):
            guardados.append("<code>" + escapar(m.group(0).strip("`")) + "</code>")
            return "\x00%d\x00" % (len(guardados) - 1)

        t = re.sub(r"`+[^`]+`+", guardar, t)
        t = self._fora_do_codigo(t)
        return re.sub(r"\x00(\d+)\x00", lambda m: guardados[int(m.group(1))], t)

    def _fora_do_codigo(self, t):
        t = escapar(t)
        t = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", t)
        t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", self._link, t)
        t = re.sub(r"&lt;(https?://[^\s&]+)&gt;",
                   lambda m: self._ancora_html(m.group(1), m.group(1)), t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", t)
        t = re.sub(r"~~(.+?)~~", r"<del>\1</del>", t)
        return t

    def _link(self, m):
        texto, href = m.group(1), m.group(2)
        destino = self.resolver(href)
        if destino is None:
            return ('<span class="md-interno" title="documento interno do projeto, '
                    'fora do portal">%s</span>' % texto)
        return self._ancora_html(destino, texto)

    @staticmethod
    def _ancora_html(href, texto):
        fora = href.startswith("http")
        extra = ' target="_blank" rel="noopener"' if fora else ""
        return f'<a href="{href}"{extra}>{texto}</a>'

    # ---------------------------------------------------------------- bloco
    def render(self, texto):
        """Devolve (título do documento, corpo em HTML). O primeiro `# ` vira o título."""
        linhas = texto.replace("\r\n", "\n").split("\n")
        titulo = None
        for i, ln in enumerate(linhas):
            if not ln.strip():
                continue
            m = TITULO.match(ln)
            if m and len(m.group(1)) == 1:
                titulo = texto_puro(m.group(2))
                linhas = linhas[i + 1:]
            break
        return titulo, self.blocos(linhas)

    def blocos(self, linhas):
        saida, i, n = [], 0, len(linhas)
        while i < n:
            ln, bruto = linhas[i], linhas[i].strip()
            if not bruto:
                i += 1
                continue
            if CERCA.match(ln):
                cerca = bruto[:3]
                corpo, i = [], i + 1
                while i < n and not linhas[i].strip().startswith(cerca):
                    corpo.append(linhas[i])
                    i += 1
                i += 1
                saida.append("<pre><code>" + escapar("\n".join(corpo)) + "</code></pre>")
                continue
            if REGUA.match(ln):
                saida.append("<hr>")
                i += 1
                continue
            m = TITULO.match(ln)
            if m:
                saida.append(self._titulo(len(m.group(1)), m.group(2)))
                i += 1
                continue
            if bruto.startswith(">"):
                html, i = self._citacao(linhas, i, n)
                saida.append(html)
                continue
            if bruto.startswith("|") and i + 1 < n and ALINHA.match(linhas[i + 1]):
                html, i = self._tabela(linhas, i, n)
                saida.append(html)
                continue
            if ITEM.match(ln):
                html, i = self._lista(linhas, i, n)
                saida.append(html)
                continue
            corpo = []
            while i < n and linhas[i].strip() and not self._abre_bloco(linhas, i, n):
                corpo.append(linhas[i].strip())
                i += 1
            saida.append("<p>" + self.inline(" ".join(corpo)) + "</p>")
        return "\n".join(saida)

    def _abre_bloco(self, linhas, i, n):
        ln = linhas[i]
        if CERCA.match(ln) or REGUA.match(ln) or TITULO.match(ln) or ITEM.match(ln):
            return True
        if ln.strip().startswith(">"):
            return True
        return ln.strip().startswith("|") and i + 1 < n and ALINHA.match(linhas[i + 1])

    def _titulo(self, nivel, texto):
        cru = texto_puro(texto)
        base = ancora(cru) or "secao"
        self.usadas[base] = self.usadas.get(base, 0) + 1
        ident = base if self.usadas[base] == 1 else f"{base}-{self.usadas[base] - 1}"
        # `#` no meio do documento é divisor de parte: vira h2 com classe própria, para
        # entrar no índice lateral (montado sobre h2) sem perder a âncora do GitHub.
        tag = "h2" if nivel <= 2 else ("h3" if nivel == 3 else "h4")
        classe = ' class="md-parte"' if nivel == 1 else ""
        return f'<{tag} id="{ident}"{classe}>{self.inline(texto)}</{tag}>'

    def _citacao(self, linhas, i, n):
        dentro = []
        while i < n and linhas[i].strip().startswith(">"):
            corte = linhas[i].strip()[1:]
            dentro.append(corte[1:] if corte.startswith(" ") else corte)
            i += 1
        primeiro = next((c.strip() for c in dentro if c.strip()), "")
        marca = ""
        for emoji, nome in SINAL.items():
            if primeiro.startswith(emoji):
                marca = f" md-{nome}"
                break
        return f'<blockquote class="md-nota{marca}">{self.blocos(dentro)}</blockquote>', i

    def _tabela(self, linhas, i, n):
        def celulas(ln):
            cru = ln.strip()
            cru = cru[1:] if cru.startswith("|") else cru
            cru = cru[:-1] if cru.endswith("|") else cru
            return [c.replace("\\|", "|").strip() for c in re.split(r"(?<!\\)\|", cru)]

        cabecalho = celulas(linhas[i])
        alinhamentos = []
        for c in celulas(linhas[i + 1]):
            esq, dir_ = c.startswith(":"), c.endswith(":")
            alinhamentos.append("center" if esq and dir_ else "right" if dir_ else "")
        i += 2
        linhas_corpo = []
        while i < n and linhas[i].strip().startswith("|"):
            linhas_corpo.append(celulas(linhas[i]))
            i += 1

        def estilo(k):
            al = alinhamentos[k] if k < len(alinhamentos) else ""
            return f' style="text-align:{al}"' if al else ""

        partes = ["<div class=\"scrollx\"><table>"]
        if any(c for c in cabecalho):
            partes.append("<thead><tr>" + "".join(
                f"<th{estilo(k)}>{self.inline(c)}</th>" for k, c in enumerate(cabecalho)
            ) + "</tr></thead>")
        partes.append("<tbody>")
        for linha in linhas_corpo:
            partes.append("<tr>" + "".join(
                f"<td{estilo(k)}>{self.inline(c)}</td>" for k, c in enumerate(linha)
            ) + "</tr>")
        partes.append("</tbody></table></div>")
        return "".join(partes), i

    def _lista(self, linhas, i, n):
        base = len(linhas[i]) - len(linhas[i].lstrip())
        ordenada = bool(re.fullmatch(r"\d+[.)]", ITEM.match(linhas[i]).group(2)))
        itens, atual, corte = [], None, 0
        while i < n:
            ln = linhas[i]
            if not ln.strip():
                j = i
                while j < n and not linhas[j].strip():
                    j += 1
                if j >= n:
                    break
                mj = ITEM.match(linhas[j])
                recuo = len(linhas[j]) - len(linhas[j].lstrip())
                if not ((mj and recuo >= base) or recuo > base):
                    break
                if atual is not None:
                    atual.append("")
                i = j
                continue
            m, recuo = ITEM.match(ln), len(ln) - len(ln.lstrip())
            if m and recuo == base:
                atual = [m.group(3)]
                itens.append(atual)
                corte = len(m.group(1)) + len(m.group(2)) + 1
                i += 1
                continue
            if atual is not None and recuo > base:
                atual.append(ln[min(corte, recuo):])
                i += 1
                continue
            # Continuação preguiçosa: linha sem recuo logo abaixo do item ainda é a frase
            # dele, como no CommonMark. Sem isto, negrito que atravessa a quebra fica aberto.
            if atual is not None and not _inicia_bloco(ln):
                atual.append(ln.strip())
                i += 1
                continue
            break

        partes = []
        for item in itens:
            # A continuação simples entra na própria frase do item: negrito ou link que
            # atravessa a quebra de linha do arquivo só fecha se as duas metades forem
            # convertidas juntas.
            cabeca, k = item[0], 1
            while k < len(item) and item[k].strip() and not _inicia_bloco(item[k]):
                cabeca += " " + item[k].strip()
                k += 1
            resto = item[k:]
            tarefa = re.match(r"^\[([ xX])\]\s+(.*)$", cabeca)
            classe, marca = "", ""
            if tarefa:
                feito = tarefa.group(1).lower() == "x"
                cabeca = tarefa.group(2)
                classe = ' class="md-tarefa"'
                marca = ('<span class="md-caixa%s" aria-hidden="true"></span>'
                         % (" feito" if feito else ""))
                marca = f'<span class="sr-so-leitor">{"feito" if feito else "aberto"}: </span>' + marca
            dentro = self.inline(cabeca)
            if any(l.strip() for l in resto):
                dentro += self.blocos(resto)
            partes.append(f"<li{classe}>{marca}{dentro}</li>")
        tag = "ol" if ordenada else "ul"
        return f'<{tag} class="md-lista">' + "".join(partes) + f"</{tag}>", i


def render(texto, resolver=None):
    return Conversor(resolver).render(texto)
