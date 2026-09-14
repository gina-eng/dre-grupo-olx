#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o .docx do Mapa dos Numeros do DR-E Grupo OLX.

Fonte unica: dados/outputs/mapa-de-numeros.json, produzido por
.claude/scripts/build_mapa_numeros.py. O .docx e gerado, nunca editado a mao:
quando o dado mudar, rode o build e regenere.

Nota: identificadores e comentarios ficam sem acento de proposito. O texto que
vai para o cliente, dentro das strings, e acentuado.
"""

import json
import os
import pathlib
import re
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.table import WD_TABLE_ALIGNMENT
from importlib.machinery import SourceFileLoader

AQUI = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
RAIZ = AQUI.parent.parent
_g = SourceFileLoader("gera_docx", str(AQUI / "gera-docx.py")).load_module()

setup, cabecalho, h2, h3, para = _g.setup, _g.cabecalho, _g.h2, _g.h3, _g.para
rule, panel, bullets, run, table = _g.rule, _g.panel, _g.bullets, _g.run, _g.table
shade, cell_margins, borders = _g.shade, _g.cell_margins, _g.borders
INK, MUTED, FAINT, OK, WARN, CRIT = _g.INK, _g.MUTED, _g.FAINT, _g.OK, _g.WARN, _g.CRIT
OXDARK, OXBLOOD = _g.OXDARK, _g.OXBLOOD
SUNK, BRANDWASH, OKWASH, MONO, BODY = _g.SUNK, _g.BRANDWASH, _g.OKWASH, _g.MONO, _g.BODY

DADOS = RAIZ / "dados" / "outputs" / "mapa-de-numeros.json"

# A cor da marca de cobertura. Verde para o que esta em maos, ambar para o que
# esta pela metade, vermelho para o que nao existe.
COR_COBERTURA = {"medido": "c", "concedido": "c", "conferir": "b",
                 "parcial": "b", "declarado": "b", "falta": "a"}
ROTULO = {"medido": "Medido", "concedido": "Concedido", "conferir": "A conferir",
          "parcial": "Parcial", "declarado": "Declarado", "falta": "Falta"}

ORDEM_TRAVAS = ["T7 Exposição", "T6 Atenção", "T5 Interesse", "T4 Qualificação",
                "T3 Compromisso", "T2 Decisão", "T1 Retenção"]

SUBTITULO_TRAVA = {
    "T7 Exposição": "quanta gente certa vê a oferta",
    "T6 Atenção": "quantos param para olhar",
    "T5 Interesse": "quantos se aprofundam",
    "T4 Qualificação": "quantos têm perfil e viram oportunidade",
    "T3 Compromisso": "quantos assumem um compromisso real",
    "T2 Decisão": "quantos assinam",
    "T1 Retenção": "quantos ficam, e por quanto tempo",
}


def brl(v):
    return ("R$ " + f"{v:,.0f}".replace(",", ".")) if v else "-"


def corta(s, n):
    s = re.sub(r"\s+", " ", str(s)).strip()
    return (s[: n - 1] + "…") if len(s) > n else s


def doc_mapa(path):
    d = json.loads(DADOS.read_text(encoding="utf-8"))
    pl, ind = d["placar"], d["indicadores"]
    midia, receita = d["numeros_de_apoio"]["midia"], d["numeros_de_apoio"]["receita"]

    doc = Document()
    setup(doc)
    cabecalho(doc, "Mapa dos Números",
              "O que o DR-E precisa medir, o que já está medido, e o que falta para ter o resto",
              f"14/09/2026  ·  {pl['total']} indicadores catalogados  ·  "
              f"{pl['com_numero_hoje']} com número hoje  ·  Ciclo 1, fase Identificar")

    panel(doc, "Como ler este documento",
          ["O catálogo diz o que precisa ser medido para diagnosticar as travas de receita do "
           "negócio B2B. A coluna de cobertura diz onde cada indicador está hoje, e é ela que "
           "separa o que já temos do que ainda depende de alguém.",
           "Marcação de origem: [D] é número declarado pelo Grupo OLX e ainda não apurado pela V4; "
           "[E] é estimativa da V4. Número sem marca foi apurado na ferramenta.",
           "Onde um campo aparece vazio, ele está assim por falta de dado, não por omissão. A regra "
           "do método é que campo sem fonte fica vazio e vira pendência com dono e prazo, nunca um "
           "valor aproximado.",
           "Nenhum número deste documento foi digitado à mão. Todos saem de "
           "dados/outputs/mapa-de-numeros.json, que por sua vez lê o estado do repositório."])

    # ------------------------------------------------------------------ 01
    h2(doc, "01", "O placar")
    para(doc, f"{pl['total']} indicadores catalogados. {pl['com_numero_hoje']} têm número hoje. "
              f"{pl['sem_numero_hoje']} não têm.", size=11, bold=True, space_after=6)
    para(doc, "A leitura que importa não é quantos faltam, é onde eles estão presos: a maior fila "
              "não é de dado que a OLX precisa produzir, é de ferramenta que já foi concedida e "
              "ninguém abriu.", size=10, color=MUTED, space_after=8)

    table(doc, ["Cobertura", "Qtd.", "O que significa"],
          [[(ROTULO[l["chave"]], COR_COBERTURA[l["chave"]]),
            (str(pl["por_cobertura"][l["chave"]]), "strong"),
            corta(l["definicao"], 220)] for l in d["legenda"]],
          [2.6, 1.3, 12.9])

    h3(doc, "Por prioridade")
    table(doc, ["Prioridade", "Qtd.", "O que essa faixa significa"],
          [[("P0", "a"), (str(pl["por_prioridade"].get("P0", 0)), "strong"),
            "Bloqueia o Comitê 1. Sem esses, a restrição é nomeada sem lastro."],
           [("P1", "b"), (str(pl["por_prioridade"].get("P1", 0)), "strong"),
            "Sustenta o material sob escrutínio. A falta não impede decidir, impede defender."],
           [("P2", "c"), (str(pl["por_prioridade"].get("P2", 0)), "strong"),
            "Desejável. Entra no Ciclo 2 sem custo para o Ciclo 1."]],
          [2.6, 1.3, 12.9])

    panel(doc, f"{pl['p0_presos_em_acesso_nao_conferido']} indicadores P0 estão presos num acesso que ninguém abriu",
          ["O lote completo de acessos foi declarado entregue em 10/09: CRM comercial, Salesforce "
           "Marketing Cloud, Search Console, Mouseflow, Unbounce e as duas contas de Meta. A "
           "conferência item a item, abrindo cada ferramenta, ainda não foi feita.",
           "Isso não é formalidade. Duas vezes neste projeto o acesso chegou e não servia: o GA4 "
           "veio em nível Leitor, que não abre a configuração onde mora a causa, e o Meta veio com "
           "nenhum ativo conectado. Por isso esses indicadores não contam como concedidos.",
           "Vinte deles dependem de uma fonte só, o CRM comercial, que é de onde sai quase todo o "
           "funil. Se o acesso for real, três dos quatro números que faltam para o forecast saem "
           "sem pedir nada à OLX."],
          fill=BRANDWASH)

    # ------------------------------------------------------------------ 02
    doc.add_page_break()
    h2(doc, "02", "O que já temos, com número")
    para(doc, f"Os {pl['com_numero_hoje']} indicadores que carregam valor hoje, e de onde cada "
              "valor vem. Dois grupos foram apurados na ferramenta nos últimos três dias; os "
              "declarados continuam valendo como hipótese, não como base de meta.",
         size=10, color=MUTED, space_after=8)

    com_valor = [i for i in ind if i["tem_numero"]]
    grupos = [
        ("Mídia paga, apurado no V4MOS em 14/09", lambda i: "V4MOS" in i["fonte_do_valor"]),
        ("Comportamento e tráfego, apurado no GA4 em 14/09", lambda i: "GA4" in i["fonte_do_valor"] and "V4MOS" not in i["fonte_do_valor"]),
        ("Receita, série A1 recebida em 28/08", lambda i: "Série de receita" in i["fonte_do_valor"] or "Serie de receita" in i["fonte_do_valor"]),
    ]
    usados = set()
    for titulo, teste in grupos:
        linhas = [i for i in com_valor if teste(i) and i["metrica"] not in usados]
        for i in linhas:
            usados.add(i["metrica"])
        if not linhas:
            continue
        h3(doc, titulo)
        table(doc, ["Indicador", "Valor", "Leitura"],
              [[(i["metrica"], "strong"), (i["valor"], "mono"), corta(i["fonte_do_valor"], 200)]
               for i in linhas], [4.6, 3.6, 8.6])

    resto = [i for i in com_valor if i["metrica"] not in usados]
    if resto:
        h3(doc, "Declarado em reunião, sem lastro auditável", tag="[D]", tagcolor=WARN)
        table(doc, ["Indicador", "Valor", "Quem declarou, e a ressalva"],
              [[(i["metrica"], "strong"), (i["valor"], "mono"), corta(i["fonte_do_valor"], 200)]
               for i in resto], [4.6, 3.6, 8.6])

    panel(doc, "A distância entre o declarado e o medido é o primeiro achado do mapa",
          ["O slide de 28/08 declara que o canal Pago responde por 16% da origem do contato. O GA4, "
           "sobre 987.566 sessões nos domínios B2B em 21 meses, mede Pago em 0,8%. Vinte vezes de "
           "diferença.",
           "As duas leituras não medem a mesma coisa, origem de contato contra origem de sessão, e "
           "parte da distância é isso. Mas o próprio slide anota que campanha paga para WhatsApp "
           "entra como Direto, e a auditoria de rastreamento achou o evento de compra preso ao "
           "gatilho errado. A hipótese simples é que o pago existe e não está sendo atribuído.",
           f"No mesmo período, {brl(midia['total'])} de mídia rodaram nas duas contas. Nenhuma "
           "delas separa B2B de B2C, então esse número ainda não é o investimento do recorte "
           "contratado."],
          fill=BRANDWASH)

    # ------------------------------------------------------------------ 03
    doc.add_page_break()
    h2(doc, "03", "Os sete números que decidem o Comitê 1")
    para(doc, "Nenhum deles depende de ferramenta nova. Quatro foram prometidos no kick-off para "
              "09/09, com dono nomeado, e nenhum chegou.", size=10, color=MUTED, space_after=8)

    table(doc, ["#", "O número", "Para que serve", "Dono", "Prazo"],
          [[(str(x["n"]), "mono"), (x["numero"], "strong"), corta(x["para_que"], 240),
            (x["dri"], "who"), (x["prazo"], "a" if "vencido" in x["prazo"] else "b")]
           for x in d["decidem_o_comite_1"]],
          [0.8, 4.3, 6.6, 2.9, 2.2])

    # ------------------------------------------------------------------ 04
    h2(doc, "04", "A conta que não fecha: unit economics")
    para(doc, "É o bloco que responde se o negócio compra cliente barato ou caro, e ele está "
              "inteiramente vazio. Não por falta de ferramenta: falta o denominador.",
         size=10, color=MUTED, space_after=8)

    ue = [i for i in ind if i["trava"] == "Unit Economics"]
    table(doc, ["Indicador", "Cobertura", "Por que ainda não existe"],
          [[(i["metrica"], "strong"), (ROTULO[i["cobertura"]], COR_COBERTURA[i["cobertura"]]),
            corta(i["procedencia"], 230)] for i in ue],
          [4.4, 2.2, 10.2])

    panel(doc, "As três perguntas que este bloco responde, e o estado de cada uma",
          ["Conhecemos a margem de contribuição? Não. O que existe é uma declaração de kick-off, "
           "margem bruta perto de 100%, sem COGS de produto, com mídia e imposto como únicos "
           "ofensores, e sem abertura por linha. Margem bruta não é margem de contribuição, e o "
           "P&L por vertical que converteria uma na outra não chegou.",
           "Conhecemos o CAC e o custo por venda separadamente? Não, e a Trava de Cegueira pontua "
           "essa dimensão em 0 de 5. O investimento é mensurável; a contagem de clientes novos não "
           "existe em camada nenhuma. Falta o denominador, não a ferramenta.",
           "Dá para apurar por canal de aquisição? Hoje não, por três bloqueios independentes: a "
           "atribuição do canal Direto está furada por declaração do próprio cliente, o "
           "investimento de mídia vive fora do dashboard de funil, e nenhuma das contas separa B2B "
           "de B2C. Resolver um sem os outros dois não produz CAC por canal."],
          fill=BRANDWASH)

    # ------------------------------------------------------------------ 05
    doc.add_page_break()
    h2(doc, "05", "O catálogo, trava por trava")
    para(doc, "As sete travas de receita, na ordem em que o método as percorre, de cima do funil "
              "para baixo. A coluna Hoje traz o valor quando ele existe, e o estado quando não "
              "existe.", size=10, color=MUTED, space_after=8)

    for t in ORDEM_TRAVAS:
        linhas = [i for i in ind if i["trava"] == t]
        if not linhas:
            continue
        h3(doc, f"{t}  ·  {SUBTITULO_TRAVA[t]}",
           tag=f"{sum(1 for i in linhas if i['tem_numero'])}/{len(linhas)} com número",
           tagcolor=MUTED)
        table(doc, ["Indicador", "P", "Cobertura", "Hoje", "O que falta para ter"],
              [[(i["metrica"], "strong"), (i["prioridade"], "mono"),
                (ROTULO[i["cobertura"]], COR_COBERTURA[i["cobertura"]]),
                (corta(i["valor"], 60), "mono" if i["tem_numero"] else "n"),
                corta(i["procedencia"], 190)] for i in linhas],
              [4.0, 0.8, 1.9, 3.3, 6.8])

    # ------------------------------------------------------------------ 06
    doc.add_page_break()
    h2(doc, "06", "A fila da V4: o que sai sem pedir nada à OLX")
    para(doc, "Toda linha desta tabela é trabalho de extração sobre fonte que já foi concedida. "
              "É a fila mais barata do projeto e a mais atrasada.", size=10, color=MUTED, space_after=8)

    table(doc, ["Fonte", "Indicadores", "Estado do acesso", "O que sai de lá", "Prazo"],
          [[(x["fonte"], "strong"), (str(x["indicadores"]), "mono"), corta(x["estado"], 90),
            corta(x["o_que_sai"], 230), (x["prazo"], "b")] for x in d["extracoes_v4"]],
          [3.0, 1.5, 3.4, 6.6, 1.7])

    # ------------------------------------------------------------------ 07
    h2(doc, "07", "O pedido à OLX, consolidado")
    para(doc, "Cada linha tem origem rastreável: item do checklist de 11/08 ou número de pendência "
              "do projeto. Pedido sem origem vira lista de desejos, e é tratado como tal.",
         size=10, color=MUTED, space_after=8)

    table(doc, ["Bloco", "Origem", "O que pedir", "Por quê", "Dono", "Prazo"],
          [[corta(x["bloco"], 30), (x["item"], "mono"), (corta(x["pedido"], 150), "strong"),
            corta(x["por_que"], 200), (x["dri"], "who"), (x["prazo"], "b")]
           for x in d["pedidos_olx"]],
          [2.4, 1.7, 4.3, 5.0, 2.2, 1.2])

    # ------------------------------------------------------------------ 08
    doc.add_page_break()
    h2(doc, "08", "O que a V4 pode exportar sozinha das contas de anúncio")
    para(doc, "Onze exports de interface, sem API e sem concessão nova, em ordem de valor. Eles "
              "não substituem o corte B2B, que só a OLX fecha, mas reduzem o pedido ao cliente ao "
              "que realmente só ele tem.", size=10, color=MUTED, space_after=8)

    for plat in ["Google Ads", "Meta Ads", "As duas"]:
        linhas = [x for x in d["exports_contas_de_anuncio"] if x["plataforma"] == plat]
        if not linhas:
            continue
        h3(doc, plat)
        table(doc, ["#", "P", "O export", "Onde", "O que ele destrava"],
              [[(str(x["n"]), "mono"), (x["prioridade"], "a" if x["prioridade"] == "P0" else "b"),
                (corta(x["export"], 130), "strong"), corta(x["onde"], 110),
                corta(x["destrava"], 260)] for x in linhas],
              [0.7, 0.8, 4.3, 3.8, 7.2])

    panel(doc, "O export número 11 vale mais que os dez anteriores",
          ["Nenhum relatório separa captação de anunciante de captação de consumidor, porque a "
           "separação não está nos dados: está na cabeça de quem montou as campanhas.",
           "Uma frase do time de mídia dizendo qual conta e qual campanha é B2B transforma "
           f"{brl(midia['total'])} de investimento medido no numerador de um CAC. Sem ela, os "
           "outros dez exports produzem um retrato melhor da mídia e nenhum unit economics."],
          fill=BRANDWASH)

    # ------------------------------------------------------------------ 09
    h2(doc, "09", "Ressalvas: o que impede um número de entrar em comitê")
    table(doc, ["#", "A ressalva", "O efeito sobre o número", "Onde está registrada"],
          [[(str(x["n"]), "mono"), (x["ressalva"], "strong"), corta(x["efeito"], 240),
            corta(x["fonte"], 90)] for x in d["ressalvas"]],
          [0.8, 4.4, 7.4, 4.2])

    # ------------------------------------------------------------------ 10
    doc.add_page_break()
    h2(doc, "10", "O que mudou nos últimos dias e a base ainda não registrou")
    para(doc, "Auditoria do próprio repositório. Cada linha é um dado que já existe em estado de "
              "máquina e ainda não chegou aos documentos que o comitê lê.",
         size=10, color=MUTED, space_after=8)

    for x in d["base_desatualizada"]:
        h3(doc, corta(x["o_que_mudou"], 160))
        table(doc, ["Já está em", "Ainda não está em", "Consequência"],
              [[corta(x["onde_ja_esta"], 240), corta(x["onde_ainda_nao_esta"], 420),
                corta(x["consequencia"], 300)]],
              [4.2, 6.4, 6.2])

    panel(doc, "A prioridade de atualização, em ordem",
          ["Commitar a auditoria (i) e as duas atas de CRM, que estão fechadas e fora do git.",
           "Levar a coleta de mídia de 14/09 para os documentos de diagnóstico: sete arquivos ainda "
           "afirmam que o Meta devolve zero, e um deles é o que justifica a dimensão de CTR da "
           "Trava de Atenção estar sem nota.",
           "Regerar o estado das travas, que ainda registra a Cegueira em 6 quando o dossiê de "
           "11/09 fechou em 5.",
           "Conferir os acessos de 10/09 abrindo cada ferramenta, e só depois atualizar o checklist "
           "e dados/acessos.json. Registro otimista é pior que registro desatualizado."],
          fill=BRANDWASH)

    _g.rodape(doc, "Estado de máquina em dados/outputs/mapa-de-numeros.json. "
                   "Regerar com .claude/scripts/build_mapa_numeros.py.")
    doc.save(path)
    return path


if __name__ == "__main__":
    destino = AQUI / "V4 x Grupo OLX - Mapa dos Numeros.docx"
    p = doc_mapa(str(destino))
    print("%9d bytes  %s" % (os.path.getsize(p), p))
