#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o .docx da lista de acessos pendentes do DR-E Grupo OLX.

Terceiro documento do par de acessos: os dois primeiros argumentam e organizam o
trabalho; este e so a lista, para conferencia item a item.

Fontes (se mudar la, reflita aqui):
  dados/acessos.json                       -- fonte da verdade dos acessos
  02-diagnostico/checklist-dados-e-acessos.md  -- blocos A a J
  02-diagnostico/coleta-pendente.md        -- bloco 0, as 3 contas de GTM que faltam
  PENDENCIAS.md                            -- itens 6, 11, 12, 13, 17 e 18

Nota: identificadores e comentarios ficam sem acento de proposito.
O texto que vai para o cliente, dentro das strings, e acentuado.
"""

import os
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.table import WD_TABLE_ALIGNMENT

from importlib.machinery import SourceFileLoader

_g = SourceFileLoader("gera_docx", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                "gera-docx.py")).load_module()

setup, cabecalho, h2, para, rule, panel, rodape = (
    _g.setup, _g.cabecalho, _g.h2, _g.para, _g.rule, _g.panel, _g.rodape)
shade, cell_margins, borders, run = _g.shade, _g.cell_margins, _g.borders, _g.run
INK, MUTED, FAINT, OK, WARN, CRIT = _g.INK, _g.MUTED, _g.FAINT, _g.OK, _g.WARN, _g.CRIT
SUNK, BRANDWASH, OKWASH, MONO = _g.SUNK, _g.BRANDWASH, _g.OKWASH, _g.MONO


# ---------------------------------------------------------------- os dados
# (ferramenta, detalhe, auditorias, nivel, situacao, motivo)
# situacao: "parcial" | "pendente"
PENDENTES = [
    ("Google Analytics 4",
     "3 contas · 26 propriedades",
     "(vii) Rastreamento\nalimenta (viii) e (vi)",
     "Editor\nAdministrador se houver vínculo com Google Ads",
     "parcial",
     "Concedido em nível Leitor, confirmado na interface em 01/09. Leitor abre os relatórios, "
     "mas não as telas de Administração, fluxos de dados, retenção, eventos-chave e "
     "configuração de consentimento, que são o objeto da auditoria."),

    ("Google Tag Manager",
     "4 contas, todas com selo 360",
     "(vii) Rastreamento",
     "Leitura",
     "parcial",
     "Concedida apenas a conta BR - www.olx.com.br. Faltam três contas inteiras: "
     "Checkout Unificado - PRO (6326134112), VivaReal (4412254379) e o restante da "
     "ZapImóveis (2971905372). A auditoria cobre hoje uma conta e um contêiner de outra."),

    ("Google Ads",
     "conta de captação de anunciante",
     "(vi) Mídia paga",
     "Administrativo para aceitar a integração\ndepois pode voltar a leitura",
     "parcial",
     "Só a MCC VR09 ZAP+ (526-656-0190) foi aceita, e ela não é a conta do escopo: o GA4 mostra "
     "7 contas de Google Ads vinculadas à propriedade ZapImóveis e nenhuma é essa. Falta "
     "identificar e liberar a que carrega a captação de anunciante."),

    ("Contas @olxbr.com",
     "Anselmo Bueno e Guilherme Monteiro",
     "todas, é o acesso ao data room",
     "Usuário padrão\nsem privilégio administrativo",
     "parcial",
     "Só a conta de Rafael Corazza foi criada. Hoje o data room roda em login compartilhado, "
     "o que concentra a busca de material numa pessoa só e não deixa rastro de quem leu o quê."),

    ("Google Search Console",
     "cada propriedade B2B",
     "(ii) CRO e SEO\n(viii) Páginas de captura",
     "Proprietário",
     "pendente",
     "Perfis inferiores leem os relatórios na interface, mas não autorizam a extração via API, "
     "que é como a busca é consolidada com o resto."),

    ("Meta Ads · VR ZAP+",
     "ID 612188193108418",
     "(vi) Mídia paga\n(iv) Criativos",
     "Admin do Business Manager",
     "pendente",
     "Pendente desde 21/08. Sem ela a auditoria de mídia fecha pela metade e o custo de "
     "aquisição fica sem a parcela de Meta."),

    ("Meta Ads · OLX | Autos | B2B",
     "ID 1742214902479721",
     "(vi) Mídia paga\n(iv) Criativos",
     "Admin do Business Manager",
     "pendente",
     "Pendente desde 21/08. É o único acesso mapeado que cobre a unidade de Autos."),

    ("Meta · portfólio New OLX Brasil",
     "acesso de parceiro",
     "(vi) Mídia paga\n(iv) Criativos · (v) Redes",
     "Parceiro, com os ativos atribuídos",
     "pendente",
     "Em 01/09 a aba Ativos conectados devolveu “Nenhum ativo conectado”. Pedimos junto a "
     "confirmação de quantas páginas e contas existem de fato, porque a visão atual pode estar "
     "limitada pela permissão do usuário."),

    ("Meta Business Suite",
     "",
     "(v) Redes sociais",
     "Analista",
     "pendente",
     "Sem concessão."),

    ("LinkedIn",
     "Company Pages",
     "(v) Redes sociais",
     "Analista",
     "pendente",
     "Sem concessão."),

    ("YouTube e TikTok",
     "",
     "(v) Redes sociais",
     "Analista",
     "pendente",
     "Sem concessão. O GTM confirma que os dois estão instrumentados, então não é mais "
     "descobrir quais canais existem: é acessar os que já sabemos que existem."),

    ("Salesforce Marketing Cloud",
     "",
     "(i) CRM Marketing",
     "Leitura com exportação",
     "pendente",
     "Sem concessão. O GTM revelou Insider, Braze e RD Station convivendo com o Marketing "
     "Cloud, confirmar qual é a ferramenta de fato em uso muda o escopo deste diagnóstico."),

    ("CRM comercial",
     "pipeline, estágios e motivos de perda",
     "(ix) Pré-vendas",
     "Leitura com exportação",
     "pendente",
     "Sem concessão. Confirmar também se a ferramenta é o Salesforce ou outra."),

    ("Plataforma de cadência e discagem",
     "sales engagement",
     "(ix) Pré-vendas",
     "Leitura",
     "pendente",
     "Sem concessão. Confirmar qual é a ferramenta."),

    ("Gravações de calls de qualificação",
     "amostra de 10 a 15 recentes",
     "(ix) Pré-vendas",
     "Amostra, com consentimento",
     "pendente",
     "Envolve consentimento e LGPD, então é o item de prazo menos previsível da lista. Se o "
     "trâmite não fechar, a auditoria de pré-vendas sai sem a camada experiencial."),

    ("Mouseflow",
     "projeto b837e449-83ee-457f-9ef5-8f976953f2bc",
     "(viii) Páginas de captura",
     "Leitura",
     "pendente",
     "Identificado no GTM, gravando sessão em todas as páginas web. Deixou de ser hipótese e "
     "virou pedido concreto."),

    ("Unbounce",
     "onde as landing pages vivem",
     "(viii) Páginas de captura",
     "Leitura, ou export das LPs",
     "pendente",
     "Sem concessão. O contêiner de GTM das LPs já foi recebido; falta a plataforma."),

    ("CMS dos domínios B2B",
     "",
     "(ii) CRO e SEO",
     "Leitura",
     "pendente",
     "Sem concessão."),

    ("Ferramenta de SEO",
     "SEMrush, Ahrefs ou similar",
     "(ii) CRO e SEO",
     "Leitura",
     "pendente",
     "Sem concessão. Pode não existir, e “não existe” é uma resposta completa, que "
     "registramos como leitura de maturidade."),

    ("BI ou fonte única de verdade",
     "",
     "Bloco A, fluxo de receita e forecast",
     "Leitura",
     "pendente",
     "Sem concessão. Se não houver fonte única, isso já é sintoma a registrar."),

    ("ERP e financeiro",
     "custo variável e margem",
     "Bloco A, fluxo de receita e forecast",
     "Leitura",
     "pendente",
     "Sem concessão. É o que converte receita em truput."),
]

CONCEDIDOS = [
    ("Google Ads · MCC VR09 ZAP+ (526-656-0190)",
     "aceite em 24/08, ingerindo no V4MOS desde então"),
    ("Google Analytics 4 · 3 contas, 26 propriedades",
     "leitura confirmada em 31/08, falta a elevação de nível, na lista acima"),
    ("Google Tag Manager · conta BR - www.olx.com.br",
     "confirmada em 01/09, 11 exports de contêiner recebidos"),
    ("Google Drive · data room",
     "aberto em 24/08 pela conta rafael.corazza-ext@olxbr.com"),
]


# ---------------------------------------------------------------- render
def tabela_pendentes(doc, linhas):
    cols = ["Ferramenta", "Auditoria(s)", "Nível necessário", "Status"]
    larguras = [4.3, 3.2, 3.1, 6.2]
    t = doc.add_table(rows=1, cols=len(cols))
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    t.autofit = False
    borders(t)
    for i, htxt in enumerate(cols):
        c = t.rows[0].cells[i]
        c.text = ""
        shade(c, SUNK)
        cell_margins(c)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run(p, htxt.upper(), size=8, bold=True, color=FAINT)

    for ferr, detalhe, auds, nivel, situacao, motivo in linhas:
        cells = t.add_row().cells
        for c in cells:
            c.text = ""
            cell_margins(c)

        # 1. Ferramenta
        p = cells[0].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.12
        run(p, ferr, size=9.5, bold=True, color=INK)
        if detalhe:
            d = cells[0].add_paragraph()
            d.paragraph_format.space_before = Pt(1)
            d.paragraph_format.space_after = Pt(0)
            run(d, detalhe, size=8, color=FAINT, font=MONO)

        # 2. Auditorias  3. Nivel  -- quebra de linha vira paragrafo
        for idx, bloco in ((1, auds), (2, nivel)):
            partes = bloco.split("\n")
            p = cells[idx].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.12
            run(p, partes[0], size=9, bold=(idx == 2), color=INK)
            for extra in partes[1:]:
                e = cells[idx].add_paragraph()
                e.paragraph_format.space_before = Pt(1)
                e.paragraph_format.space_after = Pt(0)
                e.paragraph_format.line_spacing = 1.12
                run(e, extra, size=8.5, color=MUTED)

        # 4. Status
        p = cells[3].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        if situacao == "parcial":
            run(p, "PARCIAL", size=8, bold=True, color=WARN, font=MONO)
            run(p, "  " + motivo, size=9, color=INK)
        else:
            run(p, "PENDENTE", size=8, bold=True, color=CRIT, font=MONO)
            run(p, "  " + motivo, size=9, color=INK)

    for row in t.rows:
        for i, w in enumerate(larguras):
            row.cells[i].width = Cm(w)
    para(doc, "", space_after=2)
    return t


def doc_pendentes(path):
    doc = Document()
    setup(doc)
    cabecalho(doc,
              "Acessos pendentes",
              "O que ainda falta liberar para os nove diagnósticos rodarem",
              "Estado em 03/09/2026, 15h  ·  4 parciais  ·  17 pendentes  ·  4 concedidos")

    panel(doc, "Como ler esta lista",
          ["Esta é a fotografia de 03/09 às 15h, antes da entrega do lote combinada para as 17h "
           "de hoje. Ela serve de conferência: na sexta 04/09 a V4 abre cada ferramenta uma a uma "
           "e marca o que de fato funciona.",
           "A distinção importa porque já aconteceu duas vezes de um acesso chegar concedido e "
           "não utilizável, o Analytics veio em nível Leitor, e o portfólio de Meta apareceu sem "
           "nenhum ativo conectado. Por isso a coluna de status separa parcial de pendente, e "
           "diz o motivo."])

    h2(doc, "01", "O que falta")
    tabela_pendentes(doc, PENDENTES)

    h2(doc, "02", "O que já está concedido")
    para(doc, "Registrado para que nada seja pedido duas vezes.",
         size=9.5, color=MUTED, space_after=4)
    for titulo, nota in CONCEDIDOS:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        run(p, "CONCEDIDO", size=8, bold=True, color=OK, font=MONO)
        run(p, "  " + titulo + ", ", size=9.5, bold=True, color=INK)
        run(p, nota, size=9.5, color=MUTED)
    para(doc, "", space_after=4)

    h2(doc, "03", "Duas coisas que não são acesso, e que também faltam")
    panel(doc, "Entrega de dado, não concessão de ferramenta",
          ["O bloco A, receita mensal dos últimos 24 meses, funil comercial com volumes e taxas "
           "por etapa, e ticket médio com ciclo de vendas, segue sem nenhum item recebido. "
           "Nenhuma liberação de plataforma o destrava, e sem ele o forecast não tem matemática.",
           "As gravações de call da linha (ix) dependem do trâmite de consentimento, não de "
           "permissão em sistema. Vale começar esse trâmite antes de o acesso à ferramenta sair."],
          fill=BRANDWASH)

    rodape(doc, "A justificativa técnica de cada nível está no documento Acessos e níveis de dado.")
    doc.save(path)
    return path


if __name__ == "__main__":
    dest = os.path.expanduser("~/Desktop")
    f = doc_pendentes(os.path.join(dest, "V4 x Grupo OLX - Acessos Pendentes.docx"))
    print("%8d bytes  %s" % (os.path.getsize(f), f))
