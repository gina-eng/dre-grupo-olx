#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os dois documentos de acesso do DR-E Grupo OLX em .docx.

Espelha os dois artifacts publicados:
  1. Acessos e niveis de dado  (a argumentacao)
  2. Checklist de liberacao    (a lista de trabalho)

Nota: identificadores e comentarios ficam sem acento de proposito.
O texto que vai para o cliente, dentro das strings, e acentuado.
"""

import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---------------------------------------------------------------- paleta
OXBLOOD = RGBColor(0x97, 0x00, 0x13)
OXDARK = RGBColor(0x7A, 0x00, 0x10)
INK = RGBColor(0x1A, 0x14, 0x16)
MUTED = RGBColor(0x5E, 0x54, 0x58)
FAINT = RGBColor(0x8F, 0x85, 0x8A)
OK = RGBColor(0x2F, 0x6B, 0x4F)
WARN = RGBColor(0x8A, 0x5A, 0x00)
CRIT = RGBColor(0xA3, 0x22, 0x18)

SUNK = "F4F0F1"
BRANDWASH = "FBEFF0"
OKWASH = "EBF3EE"

BODY = "IBM Plex Sans"
MONO = "IBM Plex Mono"


# ---------------------------------------------------------------- helpers
def shade(cell, hexcolor):
    tcpr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexcolor)
    tcpr.append(shd)


def cell_margins(cell, top=80, bottom=80, left=110, right=110):
    tcpr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for tag, val in (("top", top), ("start", left), ("bottom", bottom), ("end", right)):
        el = OxmlElement("w:" + tag)
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tcpr.append(mar)


def borders(tbl_obj, color="D8D0D2", size=4):
    pr = tbl_obj._tbl.tblPr
    el = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        b = OxmlElement("w:" + edge)
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), str(size))
        b.set(qn("w:color"), color)
        el.append(b)
    pr.append(el)


def run(p, text, size=10.5, bold=False, color=INK, font=BODY, italic=False):
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    rpr = r._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rf.set(qn(a), font)
    return r


def para(container, text="", size=10.5, bold=False, color=INK, font=BODY,
         space_before=0, space_after=6, italic=False, indent=0):
    p = container.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.18
    if indent:
        p.paragraph_format.left_indent = Cm(indent)
    if text:
        run(p, text, size, bold, color, font, italic)
    return p


def rule(doc, color="1A1416", size=18):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(10)
    ppr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:bottom")
    b.set(qn("w:val"), "single")
    b.set(qn("w:sz"), str(size))
    b.set(qn("w:space"), "1")
    b.set(qn("w:color"), color)
    pbdr.append(b)
    ppr.append(pbdr)
    return p


def eyebrow(doc, text):
    para(doc, text.upper(), size=8, bold=True, color=OXDARK, space_after=3)


def h1(doc, text):
    para(doc, text, size=26, bold=True, color=INK, space_after=6)


def h2(doc, num, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(20)
    p.paragraph_format.space_after = Pt(4)
    run(p, num + "   ", size=13, bold=True, color=OXBLOOD, font=MONO)
    run(p, text, size=15, bold=True, color=INK)
    rule(doc, "CFC6C8", 8)


def h3(doc, text, tag=None, tagcolor=WARN):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(2)
    run(p, text, size=11.5, bold=True, color=INK)
    if tag:
        run(p, "   " + tag, size=8.5, bold=True, color=tagcolor, font=MONO)


def bullets(doc, items, size=10, indent=0.55):
    for it in items:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(indent + 0.45)
        p.paragraph_format.first_line_indent = Cm(-0.45)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        run(p, "•  ", size=size, font=MONO)
        run(p, it, size=size)


def table(doc, headers, rows, widths=None, show_header=True):
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    t.autofit = False
    borders(t)
    hdr = t.rows[0].cells
    for i, htxt in enumerate(headers):
        hdr[i].text = ""
        shade(hdr[i], SUNK)
        cell_margins(hdr[i])
        p = hdr[i].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        if show_header:
            run(p, htxt.upper(), size=8, bold=True, color=FAINT)
    for r in rows:
        cells = t.add_row().cells
        for i, val in enumerate(r):
            cells[i].text = ""
            cell_margins(cells[i])
            txt, kind = (val if isinstance(val, tuple) else (val, "n"))
            p = cells[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            if kind == "mono":
                run(p, txt, size=8.5, color=OXBLOOD, font=MONO)
            elif kind == "who":
                run(p, txt, size=9.5, bold=True, color=INK)
            elif kind == "strong":
                run(p, txt, size=9.5, bold=True, color=INK)
            elif kind == "a":
                run(p, txt, size=9, bold=True, color=CRIT, font=MONO)
            elif kind == "b":
                run(p, txt, size=9, bold=True, color=WARN, font=MONO)
            elif kind == "c":
                run(p, txt, size=9, bold=True, color=OK, font=MONO)
            else:
                run(p, txt, size=9.5, color=INK)
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    para(doc, "", space_after=2)
    return t


def panel(doc, title, body, fill=BRANDWASH, accent=OXDARK):
    t = doc.add_table(rows=1, cols=1)
    borders(t)
    c = t.rows[0].cells[0]
    c.text = ""
    shade(c, fill)
    cell_margins(c, top=140, bottom=140, left=170, right=170)
    p = c.paragraphs[0]
    p.paragraph_format.space_after = Pt(3)
    run(p, title.upper(), size=8, bold=True, color=accent)
    for i, b in enumerate(body):
        bp = c.add_paragraph()
        bp.paragraph_format.space_after = Pt(3 if i < len(body) - 1 else 0)
        bp.paragraph_format.line_spacing = 1.18
        run(bp, b, size=9.5, color=INK)
    para(doc, "", space_after=2)


def setup(doc):
    st = doc.styles["Normal"]
    st.font.size = Pt(10.5)
    st.font.color.rgb = INK
    rpr = st.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), BODY)
    for s in doc.sections:
        s.left_margin = Cm(2.1)
        s.right_margin = Cm(2.1)
        s.top_margin = Cm(2.0)
        s.bottom_margin = Cm(2.0)



def rodape(doc, ref_final):
    rule(doc, "CFC6C8", 8)
    para(doc, "PRIVACIDADE E USO", size=8, bold=True, color=OXDARK, space_before=6, space_after=4)
    para(doc,
         "Os acessos solicitados são usados exclusivamente para a finalidade contratual e restritos "
         "aos profissionais estritamente necessários, sob compromisso de confidencialidade. Onde o "
         "nível administrativo é necessário, ele serve para estabelecer a integração de dados, e "
         "nenhuma alteração de configuração, campanha, verba ou publicação acontece sem aprovação "
         "prévia e explícita do Grupo OLX. Credenciais ficam em gerenciador de senhas, com troca "
         "obrigatória ao término da prestação ou em suspeita de incidente, e armazenamento residual "
         "máximo de 30 dias após o encerramento. A OLX pode revogar ou reduzir qualquer permissão a "
         "qualquer tempo.",
         size=9, color=MUTED, space_after=5)
    para(doc, "Encarregado de proteção de dados da V4: lgpd@v4company.com.br. " + ref_final,
         size=9, color=MUTED, space_after=0)


def cabecalho(doc, titulo, sub, meta):
    eyebrow(doc, "V4 Company  ·  Grupo OLX  ·  Destrava Receita, Ciclo 1")
    h1(doc, titulo)
    para(doc, sub, size=12, color=MUTED, space_after=8)
    rule(doc, "1A1416", 18)
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    run(p, meta, size=8.5, color=FAINT, font=MONO)


# ================================================================ DOCUMENTO 1

PERMISSOES = [
    ("Google Analytics 4", "Analista", "Editor ou Administrador",
     "Analista lê os relatórios, mas não permite verificar os fluxos de dados e as configurações "
     "de conversão, que são exatamente o objeto da auditoria. Administrador se houver vínculo "
     "ativo com o Google Ads."),
    ("Google Tag Manager", "Leitura", "Publicar ou Admin",
     "Iniciamos com leitura. A permissão de publicação passa a ser necessária apenas quando houver "
     "correção de medição já aprovada por vocês. Admin de conta se existir contêiner server-side."),
    ("Google Search Console", "Usuário completo", "Proprietário",
     "Perfis inferiores leem os relatórios na interface, mas não autorizam a extração de dados via "
     "API, que é como consolidamos a busca junto com o resto."),
    ("Meta Ads, as duas contas", "Ver desempenho", "Admin do Business Manager",
     "Perfil de visualização vê os relatórios, mas não autoriza um parceiro externo nem conecta os "
     "ativos ao V4MOS, que é o passo que falta hoje."),
    ("Google Ads, captação de anunciante", "Somente leitura", "Administrativo",
     "Necessário para aceitar a integração. Depois de estabelecida a conexão, o acesso pode ser "
     "reduzido para leitura."),
    ("CRM comercial", "Leitura", "Leitura com exportação",
     "Não entra na integração. A permissão de exportar relatórios evita uma segunda rodada de "
     "pedidos a cada recorte novo."),
    ("Salesforce Marketing Cloud", "Leitura", "Leitura com exportação",
     "Mesma situação acima."),
    ("CMS e ferramentas de SEO e comportamento", "Leitura", "Leitura",
     "Nada além de leitura é necessário nesta fase."),
    ("Contas do domínio @olxbr.com", "-", "Usuário padrão",
     "Sem privilégio administrativo. São contas de pessoa, não de sistema."),
]

PROFUNDIDADE = [
    dict(titulo="Google Ads, MCC VivaReal",
         tag="LIBERADO, ESCOPO A CONFIRMAR",
         tagcolor=WARN,
         meta="VR09 ZAP+  ·  526-656-0190",
         temos="A conta está liberada e a integração ingere normalmente: 655 registros de campanha, "
               "8 campanhas distintas, de 16/05/2025 a 22/06/2026, R$ 1,91 milhão investidos e 7,1 "
               "milhões de cliques. Lemos investimento, estrutura e performance dessas campanhas.",
         falta="As 8 campanhas visíveis terminam com o sufixo 'pf' e tratam de aluguel, compra e "
               "Minha Casa Minha Vida, que descreve a jornada de quem procura imóvel. O escopo "
               "contratado é a receita de anunciante. Com o que está visível hoje, a auditoria de "
               "mídia leria o funil de consumidor.",
         pedido=["Esta é a conta correta de captação B2B, ou existe outra estrutura focada em anunciantes?",
                 "Se existir outra, conceder nível administrativo nela para estabelecer a integração.",
                 "Confirmar se a série terminar em 22/06/2026 é o limite de ingestão ou uma lacuna real de dado."],
         nota=""),
    dict(titulo="Data room no Google Drive",
         tag="PRIMEIRO LOTE RECEBIDO",
         tagcolor=WARN,
         meta="9 arquivos, blocos de criativos e páginas de captura",
         temos="A pasta abriu, foi testada, e o primeiro lote já foi baixado. O canal funciona.",
         falta="Não sabemos se o que está publicado encerra os materiais de criativos e de páginas "
               "de captura, ou se ainda haverá novo envio. Sem isso não conseguimos planejar o que "
               "resta pedir nem em que ordem.",
         pedido=["Confirmar se o volume atual encerra esses blocos ou se haverá novo envio, e com que data."],
         nota=""),
    dict(titulo="Teste A/B da página Anuncie ZAP",
         tag="RECEBIDO EM NÍVEL 1",
         tagcolor=CRIT,
         meta="Teste de 17 a 23 de março  ·  auditoria (viii)",
         temos="Recebemos os slides de resultado. Sabemos qual variante foi declarada vencedora e "
               "qual foi a diferença percentual reportada entre elas.",
         falta="Vieram os percentuais, não os totais de visitantes e de conversões por variante. Sem "
               "o denominador não é possível recalcular a significância estatística, ou seja, não dá "
               "para afirmar se a diferença entre as variantes foi resultado real ou variação normal "
               "do período.",
         pedido=["Totais de visitantes e de conversões por variante, no período completo do teste."],
         nota="É o menor item deste documento e o melhor exemplo do que ele pede: não é dado novo, é "
              "o mesmo dado um nível abaixo. Se a decisão de página foi tomada sobre um teste sem "
              "significância, a recomendação de otimização muda de direção."),
    dict(titulo="Biblioteca de criativos",
         tag="AMOSTRA PARCIAL",
         tagcolor=WARN,
         meta="8 peças de 1 campanha  ·  auditoria (iv)",
         temos="Recebemos 8 peças da campanha Mês do Corretor 2026, recorte São Paulo, etapa de "
               "consideração, com três variantes da mesma mensagem.",
         falta="Uma campanha não é amostra: diversidade, fadiga e evolução de mensagem só se leem "
               "numa janela de 6 a 12 meses. E sem os briefings não há como saber qual era a hipótese "
               "por trás das variantes V1, V2 e V3, ou seja, não dá para dizer se o teste respondeu à "
               "pergunta que o motivou.",
         pedido=["Amostras dos últimos 6 a 12 meses, incluindo as peças de baixa performance.",
                 "Briefings das variantes V1, V2 e V3, e das campanhas principais do período."],
         nota="As peças que não funcionaram informam tanto quanto as que funcionaram, e costumam ser "
              "as que ficam de fora quando o pedido não é explícito."),
]

DESTRAVA = [
    ("1 · Medição", "Analytics, Tag Manager, Search Console",
     "(vii) Rastreamento Completo. Pré-requisito técnico de todas as outras oito: se a medição "
     "estiver incorreta, cada leitura seguinte herda o mesmo erro sem que ninguém perceba."),
    ("2 · Contas do domínio", "Três contas nominais @olxbr.com",
     "Nenhuma auditoria em si. Habilita a execução das outras e distribui o trabalho, que hoje "
     "depende de um login só."),
    ("3 · Mídia paga", "Meta Ads (2 contas), Google Ads de captação",
     "(vi) Mídia Paga, e alimenta (iv) Criativos e (v) Redes Sociais. Hoje o lado Meta devolve "
     "vazio, então a auditoria fecha pela metade e o custo de aquisição fica sem a parcela de Meta."),
    ("4 · Comercial e CRM", "CRM comercial, Marketing Cloud, gravações de call",
     "(ix) Pré-Vendas e (i) CRM Marketing. A (i) é a única das nove que toca diretamente a camada "
     "de retenção."),
    ("5 · Web e conteúdo", "CMS e domínios, ferramentas de SEO e comportamento",
     "(ii) CRO e SEO e (viii) Páginas de Captura."),
    ("6 · Data room", "Materiais e confirmações",
     "Completa (iv) e (viii), e resolve a dúvida de escopo que hoje pesa sobre (vi)."),
]

CONTAS = [
    ("Rafael Corazza", "Concluído", "c", "rafael.corazza-ext@olxbr.com"),
    ("Anselmo Bueno", "Em andamento", "b", "aguardando criação"),
    ("Guilherme Monteiro", "Em andamento", "b", "aguardando criação"),
    ("Leonardo Rosa", "Pendente", "a", "leonardo.rosa@v4company.com"),
]


def doc_acessos(path):
    doc = Document()
    setup(doc)
    cabecalho(doc, "Acessos e níveis de dado",
              "Por que cada acesso precisa do nível pedido, e o que cada um destrava nas nove "
              "auditorias contratadas. A lista de trabalho está no Checklist de liberação, enviado "
              "junto com este.",
              "Emitido em 25 ago 2026     Liberações idealmente até 26 ago     "
              "Comitê 1 em 17 set 2026")

    h2(doc, "01", "Dois sentidos de “nível”")
    para(doc,
         "Este documento usa a palavra nível em dois sentidos, e eles pedem coisas diferentes de "
         "vocês. Vale separar antes de entrar na lista, porque a maior parte das dúvidas sobre um "
         "pedido de acesso nasce da confusão entre os dois.",
         color=MUTED, space_after=8)
    table(doc, ["Sentido", "O que significa"], [
        (("Nível de permissão", "strong"),
         "O que a plataforma deixa a gente fazer. Cinco itens pedem nível administrativo ou "
         "proprietário, e não porque vamos alterar alguma coisa: é que estabelecer uma integração "
         "é, no Google e na Meta, um ato administrativo. Depois de ligada, a integração apenas lê."),
        (("Profundidade do dado", "strong"),
         "O que o material entregue deixa a gente concluir. Parte do que já recebemos está "
         "liberado, mas num formato que responde perguntas já feitas e não permite fazer as "
         "perguntas novas do diagnóstico."),
    ], widths=[4.6, 12.0], show_header=False)

    panel(doc, "O prazo é único e vale para tudo: idealmente até 26 de agosto",
          ["As nove auditorias funcionam em cadeia, e as primeiras alimentam as seguintes. Cada dia "
           "de espera na liberação sai do tempo de análise, não de folga. Se algum item não puder "
           "sair até lá, a informação mais útil que vocês podem nos dar é qual: com ela "
           "reorganizamos a sequência das auditorias e o cronograma segue de pé."])

    h2(doc, "02", "Nível de permissão, item a item")
    para(doc,
         "A V4 opera sobre uma plataforma de análise de dados própria, o V4MOS, que lê as contas de "
         "mídia por integração direta e não por exportação manual. É o que permite acompanhar o "
         "comportamento das campanhas ao longo do ciclo, em vez de olhar a foto do mês passado, e é "
         "dela que sai a leitura de investimento e de custo de aquisição levada aos comitês. "
         "Conectar uma conta a essa plataforma exige perfil administrativo. Operá-la depois, não.",
         color=MUTED, space_after=8)
    table(doc, ["Acesso", "Basta para analisar", "Nível pedido", "Por que o nível maior"],
          [(a, b, (c, "strong"), d) for a, b, c, d in PERMISSOES],
          widths=[3.6, 2.6, 3.0, 7.4])

    panel(doc, "O que vale para qualquer nível concedido",
          ["Uso exclusivo para a finalidade contratual, restrito aos profissionais estritamente "
           "necessários e sob compromisso de confidencialidade. Nenhuma alteração de configuração, "
           "campanha, verba ou publicação acontece sem aprovação prévia e explícita de vocês. "
           "Credenciais em gerenciador de senhas, com troca obrigatória ao término da prestação. O "
           "Grupo OLX pode revogar ou reduzir qualquer permissão a qualquer momento, inclusive logo "
           "após a configuração da integração."],
          fill=OKWASH, accent=OK)

    h2(doc, "03", "Profundidade do dado")
    para(doc,
         "O segundo sentido de nível. Acesso concedido e dado utilizável não são a mesma coisa: "
         "parte do material que já recebemos está liberado, mas num formato que não permite concluir.",
         color=MUTED, space_after=8)
    table(doc, ["Nível", "O que é", "Para que serve"], [
        (("Nível 1", "strong"), "Material consolidado: apresentação, PDF, slide de resultado",
         "Traz a conclusão de quem produziu. Serve para entender contexto e histórico."),
        (("Nível 2", "strong"), "Relatório agregado: totais por mês, por campanha ou por área",
         "Mostra tendência. Não permite cortar por segmento, safra, praça ou canal."),
        (("Nível 3", "strong"), "Dado na granularidade da linha, ou acesso à ferramenta",
         "Permite recortar, cruzar e testar hipóteses que ninguém formulou ainda. É o único nível "
         "em que o diagnóstico das travas funciona."),
    ], widths=[2.2, 6.2, 8.2])
    para(doc,
         "Quatro itens já liberados ou já entregues estão hoje no nível 1 ou 2. Abaixo, o que cada "
         "um já permite, o que ainda não permite, e o pedido que resolve a diferença.",
         space_after=4)

    for it in PROFUNDIDADE:
        h3(doc, it["titulo"], it["tag"], it["tagcolor"])
        para(doc, it["meta"], size=8.5, color=FAINT, font=MONO, space_after=6)
        t = doc.add_table(rows=1, cols=2)
        borders(t)
        left, right = t.rows[0].cells
        for c in (left, right):
            c.text = ""
            cell_margins(c, top=120, bottom=120)
        lp = left.paragraphs[0]
        lp.paragraph_format.space_after = Pt(3)
        run(lp, "O QUE JÁ PERMITE", size=8, bold=True, color=OK)
        p2 = left.add_paragraph()
        p2.paragraph_format.space_after = Pt(0)
        p2.paragraph_format.line_spacing = 1.16
        run(p2, it["temos"], size=9.5)
        rp = right.paragraphs[0]
        rp.paragraph_format.space_after = Pt(3)
        run(rp, "O QUE AINDA NÃO PERMITE", size=8, bold=True, color=CRIT)
        p3 = right.add_paragraph()
        p3.paragraph_format.space_after = Pt(0)
        p3.paragraph_format.line_spacing = 1.16
        run(p3, it["falta"], size=9.5)
        for row in t.rows:
            row.cells[0].width = Cm(8.3)
            row.cells[1].width = Cm(8.3)
        para(doc, "", space_after=2)
        corpo = ["%d. %s" % (i, x) for i, x in enumerate(it["pedido"], 1)]
        if it["nota"]:
            corpo.append(it["nota"])
        panel(doc, "O pedido", corpo)

    h2(doc, "04", "O que cada bloco destrava")
    para(doc,
         "O mapa entre os acessos e as nove auditorias contratadas. A ordem não é arbitrária: o "
         "bloco 1 é pré-requisito técnico dos outros oito.",
         color=MUTED, space_after=6)
    table(doc, ["Bloco", "Acessos", "Auditorias que destrava"],
          [((a, "mono"), b, c) for a, b, c in DESTRAVA],
          widths=[3.2, 5.0, 8.4])
    para(doc,
         "A auditoria (iii) GEO, IA e buscas generativas não depende de acesso externo: parte de "
         "linha de base zero e usa os insumos dos blocos 1 e 5.",
         size=9, color=MUTED, space_after=4)

    h2(doc, "05", "Contas do domínio: onde estamos")
    table(doc, ["Pessoa", "Status", "Conta"],
          [(a, (b, k), (c, "mono")) for a, b, k, c in CONTAS],
          widths=[4.6, 3.4, 8.6])
    para(doc,
         "Enquanto houver um login só, duas coisas seguem frágeis. A primeira é de prazo: apenas "
         "uma pessoa consegue buscar material novo no data room, o que concentra o projeto inteiro "
         "num ponto. A segunda protege a OLX: login compartilhado não deixa registro de qual pessoa "
         "acessou qual arquivo, e é esse rastro que sustenta a obrigação de proteção de dados "
         "prevista no contrato. Com contas nominais, cada acesso fica atribuído a alguém.",
         space_after=4)

    rodape(doc, "A lista de trabalho item a item está no Checklist de liberação.")
    para(doc, "", space_after=4)
    para(doc,
         "A ausência de um acesso não interrompe o projeto. Quando um dado não existe ou não pode "
         "ser produzido, isso é registrado como leitura de maturidade e entra no diagnóstico com "
         "essa interpretação, em vez de virar pendência aberta. Por isso, um “não temos” "
         "respondido rápido vale mais do que uma pendência que fica em aberto.",
         size=9, color=MUTED, space_after=0)

    doc.save(path)
    return path


# ================================================================ DOCUMENTO 2

BLOCOS_CHK = [
    ("01", "Medição", "prioridade alta · 3 itens",
     "Destrava: (vii) Rastreamento Completo   ·   Conceder para: gina@v4company.com",
     [
         ("1.1", "Google Analytics 4", "Editor", "a",
          "Propriedades dos domínios B2B  ·  Administrador se houver vínculo com Google Ads",
          "Nível Analista lê os relatórios, mas não permite verificar os fluxos de dados e as "
          "configurações de conversão, que são o objeto desta auditoria."),
         ("1.2", "Google Tag Manager", "Publicar", "a",
          "Contêineres publicados  ·  Admin de conta se for server-side",
          "Iniciamos com leitura. A permissão de publicação passa a ser necessária apenas quando "
          "houver correção de medição já aprovada por vocês."),
         ("1.3", "Google Search Console", "Proprietário", "a",
          "Cada propriedade B2B",
          "Perfis inferiores leem os relatórios na interface, mas não autorizam a extração de "
          "dados via API."),
     ]),
    ("03", "Mídia paga", "3 itens",
     "Destrava: (vi) Mídia Paga, (iv) Criativos e (v) Redes Sociais",
     [
         ("3.1", "Meta Ads, conta VR ZAP+", "Admin do BM", "a",
          "ID 612188193108418  ·  pendente desde 21/08",
          "Nível Admin do Business Manager para conceder acesso de parceiro à V4 e conectar os "
          "ativos ao V4MOS. Hoje a integração devolve vazio no lado Meta, então a auditoria de "
          "mídia fecha pela metade e o custo de aquisição fica sem a parcela de Meta."),
         ("3.2", "Meta Ads, conta OLX Autos B2B", "Admin do BM", "a",
          "ID 1742214902479721  ·  pendente desde 21/08",
          "Mesmo nível e mesma justificativa do item anterior. É, além disso, o único acesso "
          "mapeado que cobre a unidade de Autos."),
         ("3.3", "Google Ads, captação de anunciantes", "Administrativo", "a",
          "Conta a identificar  ·  ver item 6.1",
          "Nível administrativo para aceitar a integração. Depois de estabelecida a conexão, o "
          "acesso pode ser reduzido para leitura."),
     ]),
    ("04", "Comercial e CRM", "3 itens",
     "Destrava: (ix) Pré-Vendas e (i) CRM Marketing   ·   acesso com permissão de exportar relatórios",
     [
         ("4.1", "CRM comercial", "Leitura e exportação", "b",
          "Pipeline, estágios e motivos de perda",
          "Confirmar também se a ferramenta utilizada é o Salesforce ou outra. É o acesso que "
          "valida o funil contra o faturamento declarado."),
         ("4.2", "Salesforce Marketing Cloud", "Leitura e exportação", "b",
          "Jornadas, bases e métricas de retenção",
          "É a única das nove auditorias contratadas que toca diretamente a camada de retenção."),
         ("4.3", "Gravações de calls", "10 a 15 amostras", "n",
          "Ligações recentes de qualificação",
          "Para avaliação da camada experiencial de pré-vendas. Envolve checagem de consentimento, "
          "então vale iniciar hoje mesmo que a entrega venha depois: é o item de prazo mais "
          "imprevisível da lista."),
     ]),
    ("05", "Web e conteúdo", "2 itens",
     "Destrava: (ii) CRO e SEO e (viii) Páginas de Captura",
     [
         ("5.1", "CMS e domínios", "Leitura", "n",
          "Leitura do CMS e relação de domínios e subdomínios B2B",
          "Sem o mapeamento dos domínios não conseguimos delimitar o perímetro do diagnóstico de "
          "conversão e de busca."),
         ("5.2", "Ferramentas de SEO e comportamento", "Leitura", "n",
          "SEMrush ou Ahrefs  ·  Hotjar ou Clarity  ·  caso utilizem",
          "Se não existirem, a resposta já é o dado: registramos como linha de base e seguimos, "
          "sem pendência aberta."),
     ]),
    ("06", "Data room e pontos de atenção", "5 itens",
     "Confirmações e materiais. Não são acessos, e alguns podem ter outro dono interno.",
     [
         ("6.1", "Nomenclatura do Google Ads", "Confirmação", "a",
          "MCC VivaReal  ·  526-656-0190",
          "A conta exibe 8 campanhas ativas com o sufixo 'pf', que descreve jornada B2C: aluguel, "
          "compra e Minha Casa Minha Vida. Esta é a conta correta de captação B2B, ou existe outra "
          "estrutura focada em anunciantes? Sem essa confirmação, a auditoria de mídia mediria o "
          "funil errado."),
         ("6.2", "Janela de dados do Google Ads", "Confirmação", "a",
          "Série termina em 22/06/2026",
          "Trata-se do limite de ingestão da integração, ou há uma lacuna real nos dados depois "
          "dessa data?"),
         ("6.3", "Arquivos do data room", "Confirmação", "a",
          "Primeiro lote baixado: 9 arquivos",
          "Este volume encerra os materiais de criativos e de páginas de captura, ou haverá novo "
          "envio? Precisamos saber para planejar o que resta pedir."),
         ("6.4", "Dados absolutos do teste A/B", "Material", "b",
          "Página Anuncie ZAP  ·  teste de 17 a 23 de março  ·  auditoria (viii)",
          "Precisamos dos totais de visitantes e conversões por variante para recalcular a "
          "significância estatística. Recebemos os percentuais; sem o denominador não é possível "
          "afirmar se a diferença foi resultado real ou variação normal do período."),
         ("6.5", "Biblioteca de criativos e briefings", "Material", "b",
          "Últimos 6 a 12 meses  ·  auditoria (iv)",
          "Amostras do período, incluindo peças de baixa performance, e os briefings das variantes "
          "V1, V2 e V3 para análise de hipóteses. Uma campanha só, como a que recebemos, não "
          "permite ler diversidade nem fadiga criativa."),
     ]),
]


def item_chk(doc, sigla, titulo, nivel, cor_k, meta, porque):
    cores = {"a": CRIT, "b": WARN, "c": OK, "n": MUTED}
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(11)
    p.paragraph_format.space_after = Pt(1)
    run(p, "☐  ", size=12)
    run(p, sigla + "   ", size=9, bold=True, color=OXBLOOD, font=MONO)
    run(p, titulo, size=11.5, bold=True)
    run(p, "   " + nivel.upper(), size=8.5, bold=True, color=cores[cor_k], font=MONO)
    para(doc, meta, size=8.5, color=FAINT, font=MONO, space_after=3, indent=0.72)
    gp = doc.add_paragraph()
    gp.paragraph_format.left_indent = Cm(0.72)
    gp.paragraph_format.space_after = Pt(3)
    gp.paragraph_format.line_spacing = 1.16
    run(gp, porque, size=9.5, color=MUTED)


def doc_checklist(path):
    doc = Document()
    setup(doc)
    cabecalho(doc, "Checklist de liberação",
              "Os dezessete itens necessários para destravar as nove auditorias contratadas, com o "
              "nível de permissão de cada um. A justificativa técnica está no documento Acessos e "
              "níveis de dado, enviado junto com este.",
              "Emitido em 25 ago 2026     Idealmente até 26 ago 2026     "
              "Comitê 1 em 17 set 2026     17 itens")

    h2(doc, "00", "Contexto")
    panel(doc, "Prazo único: idealmente até 26 de agosto",
          ["As nove auditorias funcionam em cadeia, e as primeiras alimentam as seguintes. Se algum "
           "item não puder sair até lá, a informação mais útil é qual: com ela reorganizamos a "
           "sequência e o cronograma segue de pé.",
           "Cinco itens pedem nível administrativo ou proprietário. Eles são necessários para "
           "integrar as contas à nossa plataforma de análise de dados, o V4MOS. Conectar é ato "
           "administrativo nas plataformas do Google e da Meta. Depois de conectada, a integração "
           "apenas lê, e o acesso pode voltar a leitura.",
           "O bloco 1 é prioridade máxima: é pré-requisito técnico das outras oito auditorias. Se a "
           "medição estiver incorreta, cada leitura seguinte herda o mesmo erro."])

    for num, titulo, contagem, destrava, itens in BLOCOS_CHK:
        if num == "03":
            # bloco 02 (contas do dominio) entra antes da midia paga
            h2(doc, "02", "Contas do domínio @olxbr.com")
            para(doc, "Habilita a execução das etapas seguintes   ·   1 item, 3 contas pendentes",
                 size=9.5, color=MUTED, space_after=4)
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(1)
            run(p, "☐  ", size=12)
            run(p, "2.1   ", size=9, bold=True, color=OXBLOOD, font=MONO)
            run(p, "Contas nominais para o time da V4", size=11.5, bold=True)
            run(p, "   USUÁRIO PADRÃO", size=8.5, bold=True, color=MUTED, font=MONO)
            para(doc, "Mesmo padrão da conta já criada  ·  sem privilégio administrativo",
                 size=8.5, color=FAINT, font=MONO, space_after=4, indent=0.72)
            table(doc, ["Pessoa", "Status", "Conta"],
                  [(a, (b, k), (c, "mono")) for a, b, k, c in CONTAS],
                  widths=[4.6, 3.4, 8.6])
            para(doc,
                 "Enquanto houver um login só, apenas uma pessoa consegue buscar material novo no "
                 "data room, o que concentra o projeto num ponto. E login compartilhado não deixa "
                 "registro de quem acessou o quê, que é o rastro que sustenta a obrigação de "
                 "proteção de dados do contrato.",
                 size=9.5, color=MUTED, space_after=4, indent=0.72)

        h2(doc, num, titulo)
        para(doc, destrava + "   ·   " + contagem, size=9.5, color=MUTED, space_after=2)
        for sigla, tit, nivel, cor, meta, porque in itens:
            item_chk(doc, sigla, tit, nivel, cor, meta, porque)

    h2(doc, "07", "Duas coisas que facilitam")
    panel(doc, "Respostas rápidas valem mais do que pendências abertas",
          ["“Não existe” é uma resposta completa. Se algum item não existe, não é "
           "extraível ou não pode ser compartilhado, basta dizer. Registramos como leitura de "
           "maturidade e seguimos em frente.",
           "Prazo inviável também é informação útil. Preferimos reorganizar a ordem do diagnóstico "
           "com antecedência a descobrir a indisponibilidade na semana do comitê."],
          fill=OKWASH, accent=OK)

    rodape(doc, "A justificativa técnica de cada item está no documento Acessos e níveis de dado.")
    doc.save(path)
    return path


if __name__ == "__main__":
    dest = os.path.expanduser("~/Desktop")
    a = doc_acessos(os.path.join(dest, "V4 x Grupo OLX - Acessos e Niveis de Dado.docx"))
    b = doc_checklist(os.path.join(dest, "V4 x Grupo OLX - Checklist de Liberacao.docx"))
    for f in (a, b):
        print("%8d bytes  %s" % (os.path.getsize(f), f))
