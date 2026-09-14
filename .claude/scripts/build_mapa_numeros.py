#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_mapa_numeros.py: monta o Mapa dos Numeros do DR-E em estado de maquina.

O Mapa responde tres perguntas numa folha so: que numeros o DR-E precisa ter,
quais ja temos, e o que falta para ter o resto. Ele e o insumo do entregavel
`01-cliente/entregaveis/gera-docx-mapa-numeros.py`.

De onde vem cada coisa:

- O CATALOGO das 78 metricas vive hoje em `portal/assets/metrics-data.js`, que e
  o unico lugar do repositorio onde cobertura, valor e procedencia existem linha
  a linha. Este script le de la. A direcao correta seria o inverso (JSON manda no
  portal, como em build_travas_data.py) e fica registrada como divida.
- Os NUMEROS DE APOIO saem de dados/client.json (coleta V4MOS) e de
  dados/outputs/ (serie de receita e meta do projeto). Nenhum e digitado aqui.
- Os BLOCOS CURADOS (o que pedir, o que exportar, as ressalvas, o que a base
  ainda nao registrou) sao redacao da V4 e vivem neste arquivo, com a fonte de
  cada linha ao lado.

Regra de tipografia do repositorio: travessao e proibido. O script falha se um
aparecer na saida.

Uso:
    python3 .claude/scripts/build_mapa_numeros.py
"""
import json
import pathlib
import re
from collections import Counter, OrderedDict

RAIZ = pathlib.Path(__file__).resolve().parents[2]
CATALOGO = RAIZ / "portal" / "assets" / "metrics-data.js"
CLIENTE = RAIZ / "dados" / "client.json"
SERIE = RAIZ / "dados" / "outputs" / "serie-receita-2025-2026.json"
META = RAIZ / "dados" / "outputs" / "meta-do-projeto.json"
SAIDA = RAIZ / "dados" / "outputs" / "mapa-de-numeros.json"

APURADO_EM = "2026-09-14"

COLUNAS = ["trava", "macrofase", "metrica", "unidade", "fonte", "granularidade",
           "prioridade", "o_que_mede", "cobertura", "procedencia", "valor", "fonte_do_valor"]

ORDEM_TRAVAS = ["T7 Exposição", "T6 Atenção", "T5 Interesse", "T4 Qualificação",
                "T3 Compromisso", "T2 Decisão", "T1 Retenção", "Unit Economics"]

LEGENDA = [
    ("medido", "Medido", "Dado em mãos, versionado no repositório, com fonte rastreável e conferida."),
    ("concedido", "Concedido", "A fonte foi aberta e testada: ela respondeu. Falta só extrair, e isso é trabalho da V4."),
    ("conferir", "A conferir", "O acesso foi declarado concedido em 10/09 e nunca aberto na ferramenta. Pode estar no nível errado, como já aconteceu duas vezes neste projeto."),
    ("parcial", "Parcial", "Temos parte: série incompleta, ou o recorte errado, como mídia que mistura B2C e B2B."),
    ("declarado", "Declarado", "Existe só como número dito em reunião, sem lastro auditável. Vale como hipótese, não como base de meta."),
    ("falta", "Falta", "Nem fonte nem dado. Depende de entrega da OLX ou de uma decisão que ainda não foi tomada."),
]

# Quem destrava cada estado de cobertura. A coluna existe para separar o que a V4
# resolve sozinha do que so a OLX entrega: sao filas diferentes, com prazos
# diferentes, e misturar as duas e o que faz cobranca virar ruido.
DONO_POR_COBERTURA = {
    "medido": "V4 · já em mãos",
    "concedido": "V4 · extração na fonte já testada",
    "conferir": "V4 · abrir a ferramenta concedida em 10/09 e conferir o nível",
    "parcial": "V4 + OLX · o recorte que falta é entrega de dado",
    "declarado": "OLX · confirmar o número com lastro",
    "falta": "OLX · entrega de dado, ou decisão que ainda não foi tomada",
}

# --------------------------------------------------------------- blocos curados

# Os quatro insumos vem de dados/outputs/meta-do-projeto.json (insumos_faltantes).
# Aqui eles ganham o que o JSON nao carrega: o efeito de cada um sobre o Comite 1.
DECIDEM_O_COMITE = [
    {"n": 1, "numero": "Ticket médio de entrada, por vertical e segmento",
     "para_que": "Converte contrato novo em receita. Sem ele, N não vira R$ e o forecast não sai do lugar.",
     "onde_vive": "CRM comercial · item A3 do checklist, pedido em 11/08",
     "estado": "null no modelo da meta", "dri": "Matheus Rodrigues + Iuna Scheffler", "prazo": "09/09, vencido"},
    {"n": 2, "numero": "Base ativa de anunciantes, por vertical, mês a mês",
     "para_que": "É o denominador de churn, de CAC e de LTV ao mesmo tempo. Três indicadores presos num número só.",
     "onde_vive": "Dashboard de funil B2B, Looker sobre BigQuery",
     "estado": "null no modelo da meta", "dri": "Leonardo Rosa", "prazo": "09/09, vencido"},
    {"n": 3, "numero": "Contratos novos por mês, por canal e por vertical",
     "para_que": "É o N de onde tudo desce, e é o denominador que falta para o CAC existir.",
     "onde_vive": "CRM comercial · item A2 do checklist",
     "estado": "não recebido", "dri": "Leonardo Rosa + Carolina Dallolio", "prazo": "09/09, vencido"},
    {"n": 4, "numero": "P&L por vertical, com mídia e imposto abertos",
     "para_que": "Converte receita em truput. A meta do projeto é margem de contribuição do mês 12 sobre a do mês 0: sem P&L ela não tem denominador.",
     "onde_vive": "FP&A",
     "estado": "não recebido", "dri": "Matheus Rodrigues", "prazo": "09/09, vencido"},
    {"n": 5, "numero": "Churn desambiguado: de logo ou de receita",
     "para_que": "Muda o ranking das alavancas. Para ser de receita sobre Classifieds B&A, exigiria R$ 4,07 mi de contrato novo por mês, 114% da carteira ao ano.",
     "onde_vive": "Dashboard de funil B2B + financeiro",
     "estado": "declarado 8 a 10% ao mês, unidade em aberto", "dri": "Iuna Scheffler + Carolina Dallolio", "prazo": "pendência 22, em aberto"},
    {"n": 6, "numero": "Net de receita de Imóveis, mês a mês",
     "para_que": "Dimensiona a meta zero. A série A1 mostra Classifieds B&A crescendo 6,4%, o que não confirma o net negativo declarado no kick-off.",
     "onde_vive": "FP&A + dashboard",
     "estado": "contradição aberta, pendência 21", "dri": "Iuna Scheffler", "prazo": "10/09, vencido"},
    {"n": 7, "numero": "Metas 2026 por etapa do fluxo, receita por vertical, overview do ano",
     "para_que": "É a âncora contra a qual a meta do projeto é comparada. Sem ela, a régua existe e o número não.",
     "onde_vive": "Planejamento financeiro",
     "estado": "prometido no kick-off, não entregue", "dri": "Matheus Rodrigues + Iuna Scheffler", "prazo": "09/09, vencido"},
]

# Cada linha do pedido tem origem rastreavel: item do checklist ou numero de
# pendencia. Pedido sem origem vira lista de desejos e o cliente trata como tal.
PEDIDOS_OLX = [
    {"bloco": "A · Visão de negócio", "item": "A2", "pedido": "Funil comercial completo, volumes e taxas por etapa, 12 a 24 meses, por vertical e por canal",
     "por_que": "É o denominador de metade do catálogo. Existe no Looker sobre BigQuery: é extração, não construção.",
     "dri": "Leonardo Rosa", "prazo": "17/09", "severidade": "P0"},
    {"bloco": "A · Visão de negócio", "item": "A3", "pedido": "Ticket médio, ciclo de vendas e CAC por canal",
     "por_que": "Insumo matemático do forecast. Pedido em 11/08 e nunca entregue.",
     "dri": "Matheus Rodrigues + Iuna Scheffler", "prazo": "17/09", "severidade": "P0"},
    {"bloco": "A · Visão de negócio", "item": "A5", "pedido": "Metas comerciais vigentes e OKRs, abertos por etapa do fluxo",
     "por_que": "Sem a meta do cliente não há contra o que comparar o forecast.",
     "dri": "Matheus Rodrigues", "prazo": "17/09", "severidade": "P0"},
    {"bloco": "A · Visão de negócio", "item": "A6", "pedido": "Definição de ICP e segmentação de mercado",
     "por_que": "Sem critério de segmento não existe denominador para CAC por segmento nem para % de leads dentro do ICP.",
     "dri": "Florence Scappini", "prazo": "17/09", "severidade": "P0"},
    {"bloco": "A · Visão de negócio", "item": "meta 2", "pedido": "P&L por vertical, com mídia e imposto abertos por linha",
     "por_que": "Converte receita em truput. É o único caminho para margem de contribuição, LTV e payback.",
     "dri": "Matheus Rodrigues", "prazo": "17/09", "severidade": "P0"},
    {"bloco": "G · Mídia paga", "item": "G2", "pedido": "Investimento mensal por canal e campanha, 12 meses, com a marcação de qual campanha é B2B",
     "por_que": "As contas medem R$ 10,12 mi sem separar B2B de B2C. Sem a marcação, nenhum CAC de mídia é do recorte contratado.",
     "dri": "Mirella Mendonça", "prazo": "17/09", "severidade": "P0"},
    {"bloco": "G · Mídia paga", "item": "G3", "pedido": "Plano de mídia vigente e quais conversões estão otimizadas em cada plataforma",
     "por_que": "O Google conta 896 mil conversões a R$ 3,06. Saber qual ação é contada decide se esse número significa alguma coisa.",
     "dri": "Mirella Mendonça", "prazo": "17/09", "severidade": "P0"},
    {"bloco": "G · Mídia paga", "item": "G4", "pedido": "Metas de CPA e ROAS praticadas, e o dicionário da nomenclatura de campanha",
     "por_que": "Sem o dicionário, separar B2B de B2C nos nomes é adivinhação: `dartpro25br` parece B2B e carrega o mesmo sufixo de tudo o mais.",
     "dri": "Mirella Mendonça", "prazo": "17/09", "severidade": "P0"},
    {"bloco": "B · CRM", "item": "pendência 30", "pedido": "Clientes novos no Campana por vertical e mês desde abril, churn da coorte contra a anterior, e receita da coorte",
     "por_que": "Mede o que os cinco meses sem jornada de ciclo de vida custaram. Sem tamanho, o achado não entra em forecast.",
     "dri": "Michelle Morais", "prazo": "17/09", "severidade": "P0"},
    {"bloco": "B · CRM", "item": "pendência 32", "pedido": "Miro das jornadas, planilha de links e acessos, dashboard do Looker de canais e o de CRM offline",
     "por_que": "Quatro entregas prometidas em 09 e 10/09, nenhuma chegou. O mapa de 15 jornadas foi reconstruído de uma tela compartilhada e não é citável em comitê.",
     "dri": "Michelle Morais", "prazo": "17/09", "severidade": "P1"},
    {"bloco": "B · CRM", "item": "pendência 33", "pedido": "Antes e depois da higienização de base, em registros, por vertical",
     "por_que": "Separa problema de volume de problema de cadastro. Hoje só existe 'CEP ausente em mais de 50%'.",
     "dri": "Evelyn Milare", "prazo": "17/09", "severidade": "P1"},
    {"bloco": "A · Visão de negócio", "item": "pendência 20", "pedido": "Arquivo original do slide FLUXOS e da jornada do cliente profissional",
     "por_que": "O mix de canais inteiro depende de uma anotação de reunião. Número que não volta à fonte não entra em material de comitê.",
     "dri": "Carolina Dallolio", "prazo": "17/09", "severidade": "P1"},
    {"bloco": "G · Mídia paga", "item": "pendência 12", "pedido": "Lista de subcontas do MCC 526-656-0190 e a quem pertencem os 7 customer IDs vinculados ao ZapImóveis",
     "por_que": "A conta a que a V4 tem acesso não está entre as 7 que o GA4 mostra. Ou o recorte está errado, ou falta conta.",
     "dri": "Mirella Mendonça", "prazo": "17/09", "severidade": "P0"},
]

# O que a V4 faz sem pedir nada. Esta e a fila que nao tem desculpa: o acesso
# chegou em 10/09 e 23 indicadores esperam alguem abrir a ferramenta.
EXTRACOES_V4 = [
    {"fonte": "CRM comercial", "indicadores": 20, "estado": "declarado concedido em 10/09, nunca aberto",
     "o_que_sai": "Funil inteiro de Qualificação a Decisão: leads por origem, MQL, SQL, win rate, ciclo de venda, motivos de perda, motivos de cancelamento, contratos novos.",
     "prazo": "15/09"},
    {"fonte": "Salesforce Marketing Cloud", "indicadores": 2, "estado": "declarado concedido em 10/09, nunca aberto",
     "o_que_sai": "Open rate e click rate, camada analítica da auditoria (i), hoje fechada só na camada experiencial.",
     "prazo": "15/09"},
    {"fonte": "Google Search Console", "indicadores": 1, "estado": "declarado concedido em 10/09, nunca aberto",
     "o_que_sai": "Posição média nas keywords B2B estratégicas, linha de base da auditoria (ii).",
     "prazo": "15/09"},
    {"fonte": "GA4", "indicadores": 3, "estado": "aberto e testado em 14/09, respondeu",
     "o_que_sai": "Sessões com 2 ou mais páginas, visualizações das páginas de plano e preço, taxa de retorno em 7 dias. Presos ao inventário de URLs do item C1.",
     "prazo": "16/09"},
    {"fonte": "V4MOS · Meta e Google Ads", "indicadores": 14, "estado": "ingerindo desde 12/09, recoletado em 14/09",
     "o_que_sai": "Toda a camada de mídia já está medida. O que falta não é extração, é o corte B2B contra B2C.",
     "prazo": "depende de G2"},
]

# O usuario tem acesso as contas e pode exportar. Esta e a lista, em ordem de
# valor, com o que cada export destrava. Tudo aqui e relatorio de interface, nao
# pede API nem concessao nova.
EXPORTS_CONTAS_DE_ANUNCIO = [
    {"plataforma": "Google Ads", "n": 1, "prioridade": "P0",
     "export": "Relatório de campanhas segmentado por Ação de conversão, jan/2025 a set/2026",
     "onde": "Relatórios → Campanhas → Segmentar → Conversões → Nome da ação de conversão",
     "colunas": "Campanha, mês, ação de conversão, conversões, custo, custo por conversão",
     "destrava": "Diz QUAL conversão o Google conta. São 896.625 conversões a R$ 3,06: se forem eventos de navegação importados do GA4, o CPA da conta é ficção e o Smart Bidding está treinado para comprar sessão."},
    {"plataforma": "Google Ads", "n": 2, "prioridade": "P0",
     "export": "Relatório de campanhas por mês, jan/2025 a set/2026, todas as campanhas incluindo pausadas",
     "onde": "Relatórios → Predefinido → Campanha, segmentar por Mês, período personalizado",
     "colunas": "Campanha, tipo, status, mês, custo, impressões, cliques, CTR, CPC, conversões, valor de conversão",
     "destrava": "Fecha o buraco de nov/2025 a abr/2026, seis meses sem nenhum registro no V4MOS, e diz se foi pausa real da conta ou falha de ingestão. Sem isso o Google tem 11 meses de série e o Meta tem 21."},
    {"plataforma": "Google Ads", "n": 3, "prioridade": "P0",
     "export": "Relatório de páginas de destino, por campanha, mesma janela",
     "onde": "Relatórios → Predefinido → Página de destino (URL final expandida)",
     "colunas": "URL final, campanha, custo, cliques, conversões",
     "destrava": "É o corte B2B contra B2C sem depender do dicionário de nomenclatura: quem manda para ads.grupoolx.com.br, anuncie e planos é captação de anunciante; quem manda para busca de imóvel é consumidor."},
    {"plataforma": "Google Ads", "n": 4, "prioridade": "P0",
     "export": "Tela de Ações de conversão, com todas as colunas",
     "onde": "Objetivos → Conversões → Resumo",
     "colunas": "Nome, origem, categoria, contagem, janela de conversão, incluir em Conversões, modelo de atribuição",
     "destrava": "Print ou CSV serve. É onde se vê se session_start do GA4 VivaReal, marcado como evento-chave, está importado como conversão."},
    {"plataforma": "Google Ads", "n": 5, "prioridade": "P1",
     "export": "Lista de subcontas do MCC 526-656-0190",
     "onde": "Administração → Subcontas",
     "colunas": "ID, nome, status, gasto no período",
     "destrava": "Fecha a pendência 12: o GA4 mostra 7 contas vinculadas ao ZapImóveis e nenhuma é a que a V4 enxerga."},
    {"plataforma": "Meta Ads", "n": 6, "prioridade": "P0",
     "export": "Relatório por campanha, detalhado por mês, jan/2025 a set/2026, nas duas contas",
     "onde": "Gerenciador de Anúncios → Relatórios → Exportar",
     "colunas": "Conta, campanha, objetivo, mês, valor gasto, impressões, alcance, frequência, cliques no link, CTR, CPM, Resultados, Indicador de resultado, Custo por resultado",
     "destrava": "Resultados e Indicador de resultado são exatamente o que o V4MOS não traz. Hoje o Meta tem R$ 7,38 mi e 1,88 bi de impressões sem um único desfecho associado."},
    {"plataforma": "Meta Ads", "n": 7, "prioridade": "P0",
     "export": "Detalhamento por Ação, com conversas de mensagem",
     "onde": "Mesmo relatório → Detalhamento → Por ação → Tipo de ação",
     "colunas": "Conversas por mensagem iniciadas, leads, cadastros concluídos, cliques em link de saída",
     "destrava": "O WhatsApp é 42% da entrada do funil e o slide anota que campanha paga para WhatsApp entra como Direto. Se essa campanha existe, ela aparece aqui, com nome e custo."},
    {"plataforma": "Meta Ads", "n": 8, "prioridade": "P1",
     "export": "Mesmo relatório no nível de anúncio, com prévia da peça",
     "onde": "Gerenciador de Anúncios → nível Anúncio → Exportar",
     "colunas": "Anúncio, campanha, mês, gasto, impressões, alcance, frequência, CTR, CPM, resultados",
     "destrava": "Fecha a auditoria (iv) Criativos com 1.079 peças e fadiga por peça, contra as 8 peças de uma campanha que existiam antes de 12/09."},
    {"plataforma": "Meta Ads", "n": 9, "prioridade": "P0",
     "export": "Lista de contas de anúncio do portfólio New OLX Brasil",
     "onde": "Configurações do portfólio → Contas → Contas de anúncios",
     "colunas": "ID, nome, status, quem tem acesso",
     "destrava": "Diz se a operação é maior que as duas contas concedidas, e fecha a pendência 11."},
    {"plataforma": "Meta Ads", "n": 10, "prioridade": "P1",
     "export": "Conjuntos de dados e pixels do portfólio",
     "onde": "Configurações do portfólio → Fontes de dados → Conjuntos de dados",
     "colunas": "ID do pixel, conta vinculada, eventos recebidos, CAPI ativa",
     "destrava": "Cruza com os três pixels achados no GTM: 592658194155317, 818079879779548, 935989184453347. Pixel que recebe evento e não está vinculado à conta é mídia otimizando às cegas."},
    {"plataforma": "As duas", "n": 11, "prioridade": "P0",
     "export": "Uma frase do time de mídia: qual conta e qual campanha é captação de anunciante, e qual é consumidor",
     "onde": "Não é export. É a resposta que vale mais que todos os anteriores.",
     "colunas": "-",
     "destrava": "Enquanto ela não existir, R$ 10,12 mi de mídia medida não é o investimento do recorte contratado, e nenhum CAC de mídia é calculável."},
]

RESSALVAS = [
    {"n": 1, "ressalva": "Nenhuma das contas de mídia separa B2B de B2C",
     "efeito": "R$ 10,12 mi medidos em 113 campanhas não são o investimento do recorte contratado. Todo CAC de mídia fica sem numerador válido.",
     "fonte": "V4MOS, coleta de 14/09"},
    {"n": 2, "ressalva": "O evento purchase dispara no gatilho de begin_checkout",
     "efeito": "A conversão de checkout do anunciante privado do ZapImóveis não é derivável, e o histórico anterior à correção fica sem o dado, não com dado ruim.",
     "fonte": "Auditoria (vii), achado 1, confirmado na versão publicada"},
    {"n": 3, "ressalva": "session_start está marcado como evento-chave no GA4 VivaReal",
     "efeito": "Infla qualquer taxa de conversão relatada e, se importado no Google Ads, treina o Smart Bidding para comprar sessão em vez de cliente.",
     "fonte": "13,27 mi em agosto, GA4 407391347"},
    {"n": 4, "ressalva": "O canal Direto está inflado por mídia paga sem atribuição",
     "efeito": "O slide declara Pago 16% da origem do contato; o GA4 mede Pago 0,8% das sessões. Vinte vezes de diferença, e as duas leituras não medem a mesma coisa.",
     "fonte": "Slide FLUXOS, 28/08, e GA4 503925542, 21 meses"},
    {"n": 5, "ressalva": "Escrita dupla no GA4",
     "efeito": "O gatilho lead_dbm dispara para duas propriedades. Qualquer soma entre elas conta o mesmo lead duas vezes.",
     "fonte": "Auditoria (vii), achado 20"},
    {"n": 6, "ressalva": "O slide FLUXOS não está versionado",
     "efeito": "O mix de canais inteiro existe só em prosa de anotação. Não é conferível contra a fonte e não pode entrar em material de comitê nessa condição.",
     "fonte": "Pendência 20"},
    {"n": 7, "ressalva": "A série do Google tem seis meses ausentes",
     "efeito": "nov/2025 a abr/2026 sem nenhum registro. Origem não apurada entre pausa da conta e falha de ingestão.",
     "fonte": "V4MOS, coletas de 08/09 e 14/09"},
    {"n": 8, "ressalva": "A regra 8 não pode ser verificada",
     "efeito": "Não existe funil derivável para confrontar com a receita declarada. A tolerância de 5% do repositório fica sem os dois lados da conta.",
     "fonte": "CLAUDE.md, regra 8"},
]

BASE_DESATUALIZADA = [
    {"o_que_mudou": "O Meta passou a ingerir no V4MOS em 12/09 e foi recoletado em 14/09: 90 campanhas, 1.079 anúncios, R$ 7,38 mi, 2,7 vezes o Google na mesma janela",
     "onde_ja_esta": "RESOLVIDO EM 14/09. dados/client.json, portal, e os sete documentos que afirmavam o contrário: fluxo-de-receita.md, diagnostico-travas.md, checklist-dados-e-acessos.md, acessos-e-ferramentas.md, PENDENCIAS.md, o sprint de 10 a 18/09 e a SKILL.md da dre-v4mos",
     "onde_ainda_nao_esta": "-",
     "consequencia": "Nenhuma nota de trava subiu, e é deliberado. As duas dimensões que se descreviam como sem nenhum dado, (A) Alcance em Exposição e (A) CTR em Atenção, seguem null com a justificativa reescrita: o que as segura passou a ser falta de recorte B2B e de base de comparação. O método exige benchmark setorial E histórico próprio; o histórico existe com 21 meses e o benchmark não existe com fonte nomeada neste repositório."},
    {"o_que_mudou": "O GA4 respondeu pela API em 14/09 e nove indicadores viraram MEDIDO: 987.566 sessões nos domínios B2B em 21 meses, mix por origem, engajamento, rejeição e scroll",
     "onde_ja_esta": "portal/assets/metrics-data.js",
     "onde_ainda_nao_esta": "Nenhum .md de diagnóstico registra os nove",
     "consequencia": "ÚNICO PONTO AINDA ABERTO DESTA LISTA. O achado do Pago 0,8% contra 16% declarado é material de Comitê 1 e continua fora de documento nenhum da pasta 02-diagnostico."},
    {"o_que_mudou": "A camada experiencial da auditoria (i) CRM fechou em 10/09, com 16 achados",
     "onde_ja_esta": "RESOLVIDO EM 14/09. Commitado com as duas atas, as duas transcrições e o JSON",
     "onde_ainda_nao_esta": "-",
     "consequencia": "O bloco B do checklist saiu de quatro itens em branco para B1 laranja, B2 e B4 parciais, e B3 com o sentido do pedido mudado."},
    {"o_que_mudou": "A Trava de Cegueira foi pontuada em 5 de 25 em 11/09",
     "onde_ja_esta": "RESOLVIDO EM 14/09. dre-diagnostico-travas.json regerado com (A) 2 para 1, (B) 1 para 0 e (D) 1 para 2, e o asset do portal regerado da fonte",
     "onde_ainda_nao_esta": "-",
     "consequencia": "A faixa não muda, segue estruturalmente travada, e o normalizado vai de 10,0 para 8,3 de 25. Fica a ressalva de citação: o dossiê publica 5 de 25, que é a soma bruta contra o denominador não rebaixado pela regra 6, e em comitê o número precisa ser o normalizado."},
    {"o_que_mudou": "O lote de acessos de 10/09 incluiu CRM comercial, Marketing Cloud, Search Console, Mouseflow e Unbounce",
     "onde_ja_esta": "CONFERIDO EM 14/09 até onde o ambiente alcança. GA4, V4MOS e GTM por API; as duas contas de Meta e a MCC do Google indiretamente, pela ingestão. Registrado em dados/acessos.json e no checklist",
     "onde_ainda_nao_esta": "CRM comercial, Salesforce Marketing Cloud, Search Console e Meta Business Manager: sem conector neste ambiente, exigem abrir a interface",
     "consequencia": "As quatro não conferidas são as que prendem os 23 indicadores, 18 deles P0, e 20 dependem só do CRM comercial. Nenhum item subiu de status sem prova de abertura: registro otimista é pior que registro desatualizado. Checagem barata antes de abrir: o Sales Cloud exige o e-mail @olxbr habilitado no MyApps."},
]


def le_catalogo():
    """Le o array do asset do portal. Ele e JSON valido depois de tirar o
    comentario de cabecalho, a atribuicao e o ponto e virgula final."""
    bruto = CATALOGO.read_text(encoding="utf-8")
    corpo = bruto.split("const M =", 1)[1].rsplit(";", 1)[0].strip()
    corpo = re.sub(r"^\s*//.*$", "", corpo, flags=re.M)
    linhas = json.loads(corpo)
    saida = []
    for linha in linhas:
        d = OrderedDict(zip(COLUNAS, linha))
        d["tem_numero"] = d["valor"] not in ("-", "")
        d["destrava_quem"] = DONO_POR_COBERTURA[d["cobertura"]]
        saida.append(d)
    return saida


def numeros_de_apoio():
    cli = json.loads(CLIENTE.read_text(encoding="utf-8"))
    serie = json.loads(SERIE.read_text(encoding="utf-8"))
    v4 = cli["conectores"]["v4mos"]["ultima_coleta"]
    g, f = v4["google_ads"], v4["facebook_ads"]
    return OrderedDict([
        ("midia", OrderedDict([
            ("janela", "01/01/2025 a 14/09/2026"),
            ("coletado_em", v4["fetched_at"]),
            ("google_custo", g["total_cost"]),
            ("google_campanhas", g["total_campaigns"]),
            ("google_meses_com_dado", len(g["monthly_evolution"])),
            ("meta_custo", f["total_spend"]),
            ("meta_campanhas", f["total_campaigns"]),
            ("meta_anuncios", f["total_ads"]),
            ("meta_meses_com_dado", len(f["monthly_evolution"])),
            ("total", round(g["total_cost"] + f["total_spend"], 2)),
            ("ressalva", "Nenhuma das duas contas separa B2B de B2C."),
        ])),
        ("receita", OrderedDict([
            ("fonte", "Série A1, recebida em 28/08, 19 meses fechados"),
            ("run_rate_mensal_grupo", serie["grupo"]["run_rate_mensal_2026"]),
            ("run_rate_mensal_nucleo_b2b", serie["nucleo_assinatura_b2b"]["run_rate_mensal_2026"]),
            ("share_nucleo_b2b_pct", serie["nucleo_assinatura_b2b"]["share_do_grupo_pct"]),
            ("yoy_grupo_pct", serie["grupo"]["yoy_pct"]),
            ("um_pp_de_run_rate_classifieds_ba_mes", 427840.12),
            ("ressalva", "Receita bruta faturada, declarada pelo cliente. Não é truput: sem P&L por vertical não vira margem de contribuição."),
        ])),
    ])


def main():
    indicadores = le_catalogo()
    cob = Counter(i["cobertura"] for i in indicadores)
    pri = Counter(i["prioridade"] for i in indicadores)
    p0_conferir = sum(1 for i in indicadores if i["prioridade"] == "P0" and i["cobertura"] == "conferir")

    doc = OrderedDict([
        ("meta", OrderedDict([
            ("client_name", "Grupo OLX"),
            ("documento", "Mapa dos Números"),
            ("apurado_em", APURADO_EM),
            ("gerado_por", ".claude/scripts/build_mapa_numeros.py"),
            ("catalogo_de", str(CATALOGO.relative_to(RAIZ))),
            ("entregavel", "01-cliente/entregaveis/V4 x Grupo OLX - Mapa dos Numeros.docx"),
            ("pergunta_que_responde", "Que números o DR-E precisa ter, quais já temos e o que falta para ter o resto."),
        ])),
        ("placar", OrderedDict([
            ("total", len(indicadores)),
            ("com_numero_hoje", sum(1 for i in indicadores if i["tem_numero"])),
            ("sem_numero_hoje", sum(1 for i in indicadores if not i["tem_numero"])),
            ("por_cobertura", OrderedDict((k, cob.get(k, 0)) for k, _, _ in LEGENDA)),
            ("por_prioridade", OrderedDict(sorted(pri.items()))),
            ("p0_presos_em_acesso_nao_conferido", p0_conferir),
        ])),
        ("legenda", [OrderedDict([("chave", k), ("rotulo", r), ("definicao", d)]) for k, r, d in LEGENDA]),
        ("numeros_de_apoio", numeros_de_apoio()),
        ("decidem_o_comite_1", DECIDEM_O_COMITE),
        ("indicadores", indicadores),
        ("pedidos_olx", PEDIDOS_OLX),
        ("extracoes_v4", EXTRACOES_V4),
        ("exports_contas_de_anuncio", EXPORTS_CONTAS_DE_ANUNCIO),
        ("ressalvas", RESSALVAS),
        ("base_desatualizada", BASE_DESATUALIZADA),
    ])

    texto = json.dumps(doc, ensure_ascii=False, indent=2) + "\n"
    if "—" in texto:
        raise SystemExit("travessao na saida: proibido pelo CLAUDE.md")
    SAIDA.write_text(texto, encoding="utf-8")
    print(f"gerado: {SAIDA.relative_to(RAIZ)}  ({SAIDA.stat().st_size:,} bytes)")
    print(f"  {len(indicadores)} indicadores · {doc['placar']['com_numero_hoje']} com numero hoje")
    print(f"  cobertura: " + " · ".join(f"{k}={v}" for k, v in doc["placar"]["por_cobertura"].items()))
    print(f"  P0 presos em acesso nao conferido: {p0_conferir}")


if __name__ == "__main__":
    main()
