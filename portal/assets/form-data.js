const BLOCOS = [
{n:"01", t:"Governança e decisão", d:"O DR-E é um método de decisão. Sem decisor identificado e presente, o comitê vira reunião de status.", tempo:"20 min", qs:[
 {q:"Quem é o decisor final do projeto?", h:"Confirmar se é a Mirella ou se existe instância acima. Quem assina a ata de comitê?", t:"t", f:"Comitês", c:1, v:"p"},
 {q:"Quem aprova mudança de escopo, de investimento ou de prioridade?", h:"Pode ser diferente do decisor do projeto.", t:"t", f:"Comitês", c:1, v:"p"},
 {q:"Quem é o ponto focal operacional, e há um por unidade de negócio?", t:"t", f:"Governança", v:"p"},
 {q:"DRI por frente: CRM/Marketing Cloud, CRO/SEO, mídia paga, tracking, pré-vendas, dados/BI", h:"Nome de pessoa, nunca de área. Área não responde por nada.", t:"L", f:"Todos os diagnósticos", c:1, v:"p"},
 {q:"Quem participa dos comitês e quem tem poder de veto?", t:"L", f:"Comitês", v:"p"},
 {q:"Qual C-Level da OLX participa dos comitês presenciais?", h:"O método padrão DR-E prevê 4 presenciais/ano com C-Level, o contrato não faz a distinção. Pendência aberta.", t:"t", f:"Comitês", v:"p"},
 {q:"Como funciona o ciclo de aprovação interna, jurídico, compliance, segurança da informação, privacidade?", h:"Define o prazo real de liberação de dado e acesso.", t:"L", f:"Cronograma", v:"p"},
 {q:"Existe algum ritual de gestão já rodando em que o DR-E deve se encaixar?", h:"Comitê de crescimento, weekly de marketing, QBR. Evita ritual paralelo concorrente.", t:"L", f:"Cronograma", v:"p"},
 {q:"Há outras consultorias ou agências atuando nas mesmas frentes?", h:"Fronteira de escopo e risco de recomendação conflitante.", t:"L", f:"Escopo", v:"p"}
]},
{n:"02", t:"Recorte do negócio e escopo", d:"O contrato não delimita unidades. Sair daqui sem o recorte fechado é o maior risco de retrabalho do Ciclo 1.", tempo:"20 min", qs:[
 {q:"Quais unidades de negócio entram no escopo do DR-E?", h:"Imóveis (ZAP+, VivaReal, OLX Imóveis), Autos, outras. Registrar o que entra e o que fica fora.", t:"L", f:"Escopo", c:1, v:"p"},
 {q:"O foco declarado é B2B. Isso significa o quê exatamente, receita de anunciante, e não de consumidor final?", h:"E-mail da Mirella de 10/08. Confirmar a leitura.", t:"L", f:"Escopo", c:1, v:"p"},
 {q:"ZAP+, VivaReal, OLX Imóveis e OLX Autos têm P&L separado ou consolidado?", h:"Define se o Fluxo de Receita é um ou vários.", t:"L", f:"Fluxo de Receita", c:1, v:"e"},
 {q:"Quem é o cliente pagante no B2B?", h:"Imobiliária, corretor autônomo, incorporadora, revenda, concessionária, montadora, anunciante de mídia. Listar todos.", t:"L", f:"ICP · Qualificação", c:1, v:"e"},
 {q:"Qual o peso de receita de cada segmento de cliente?", h:"% da receita B2B por segmento, últimos 12 meses.", t:"L", f:"Fluxo de Receita", v:"p"},
 {q:"Existe motion self-service e motion sales-led? Qual o split de receita entre eles?", h:"Muda completamente onde a trava pode estar.", t:"L", f:"Fluxo de Receita", c:1, v:"e"},
 {q:"Há diferença relevante por região/praça?", t:"L", f:"Fluxo de Receita", v:"p"},
 {q:"O que está explicitamente FORA do escopo deste projeto?", h:"Registrar em ata. Protege os dois lados.", t:"L", f:"Escopo", c:1, v:"p"}
]},
{n:"03", t:"Modelo de receita e números-âncora", d:"Os insumos matemáticos do Fluxo de Receita e do Forecast. Sem eles o funil não valida contra o faturamento declarado.", tempo:"25 min", qs:[
 {q:"Como a receita é gerada?", h:"Assinatura de plano, destaque/impulsionamento, lead pago, take rate, mídia/publicidade, serviços. Listar todas as linhas.", t:"L", f:"Fluxo de Receita", c:1, v:"e"},
 {q:"Receita dos últimos 24 meses, aberta por unidade, segmento e linha de receita", h:"Bloco A1. Insumo matemático do Forecast.", t:"L", f:"Forecast", c:1, v:"p"},
 {q:"MRR e ARR atuais, se o modelo é de assinatura", t:"t", f:"Retenção", v:"p"},
 {q:"Ticket médio por segmento de cliente", t:"L", f:"Forecast", c:1, v:"p"},
 {q:"Ciclo de venda médio, por segmento", t:"L", f:"Forecast", c:1, v:"p"},
 {q:"Base de anunciantes ativos hoje; entradas e saídas por mês", t:"L", f:"Retenção", c:1, v:"p"},
 {q:"CAC por canal: existe cálculo? Quem o mantém?", h:"Se não existe, é sintoma de Trava de Cegueira e vira achado do Ciclo 1.", t:"L", f:"Unit Economics", c:1, v:"e"},
 {q:"LTV, payback e margem de contribuição por anunciante", t:"L", f:"Unit Economics", v:"p"},
 {q:"Sazonalidade: quais meses puxam e quais derrubam, e por quê?", t:"L", f:"Forecast", v:"p"},
 {q:"Qual a meta de receita dos próximos 12 meses e de onde ela veio?", h:"Meta herdada do board ou construída da matemática do sistema? Muda a conversa do Comitê 1.", t:"L", f:"Forecast", c:1, v:"e"},
 {q:"Qual a maior mudança estrutural dos últimos 24 meses?", h:"Fusão, novo produto, mudança de pricing, entrada de concorrente. Explica quebras na série histórica.", t:"L", f:"Fluxo de Receita", v:"e"}
]},
{n:"3B", t:"Árvore de produção de receita", d:"O contrato trata o Grupo OLX como um sistema de receita B2B, mas o caminho do dinheiro ainda não está desenhado. Sem esta árvore fechada não existe Fluxo de Receita: o funil não tem contra o que ser validado, e o Forecast não tem de onde sair.", tempo:"30 min", qs:[
 {q:"Quem assina o contrato e quem paga a fatura, em cada marca?", h:"Imobiliária, corretor autônomo, incorporadora, concessionária, revenda, vendedor pessoa física. Um pagante pode cobrir vários usuários e vários anúncios: precisamos da unidade de cobrança, não do nome do segmento.", t:"L", f:"Fluxo de Receita", c:1, v:"i"},
 {q:"O que exatamente o cliente compra quando paga?", h:"Vaga de anúncio, plano por volume, lead, clique, destaque, contrato de mídia, comissão por transação. Listar a unidade de valor de cada linha, não o nome comercial do produto.", t:"L", f:"Fluxo de Receita", c:1, v:"i"},
 {q:"ZAP+, VivaReal e OLX Imóveis são vendidos separados, em combo, ou o mesmo cliente compra os três?", h:"Define se o mesmo anunciante aparece uma vez ou três na base. Muda a contagem de clientes ativos, o ticket médio e a leitura de churn.", t:"L", f:"Fluxo de Receita", c:1, v:"i"},
 {q:"Em Autos, o dealer paga plano, paga por anúncio, ou existe comissão sobre a venda do veículo?", h:"E sobrou alguma operação transacional de compra e venda direta? Receita de assinatura e receita de transação têm travas diferentes.", t:"L", f:"Fluxo de Receita", c:1, v:"i"},
 {q:"Dentro de um mesmo cliente, o que faz a fatura crescer?", h:"Mais anúncios, mais destaque, mais praças, upgrade de plano, mídia adicional. É a alavanca de expansão, quase sempre o crescimento mais barato que existe.", t:"L", f:"Retenção", c:1, v:"i"},
 {q:"Qual linha de receita tem a maior margem de contribuição, e ela é a mesma que mais fatura?", h:"Se a linha que mais fatura não é a que mais lucra, a priorização do Ciclo 1 muda de lugar.", t:"L", f:"Unit Economics", c:1, v:"i"},
 {q:"Como o valor da audiência do consumidor final entra no preço cobrado do anunciante?", h:"O marketplace tem dois lados: o que o anunciante compra é acesso a demanda. Se o tráfego B2C oscila, o B2B sente na renovação? Existe métrica ligando os dois lados? O escopo é B2B, mas o caminho do dinheiro passa pelo B2C.", t:"L", f:"Fluxo de Receita", c:1, v:"i"},
 {q:"Existe canal indireto: revenda, franquia, parceiro ou agência vendendo em nome de vocês?", h:"Se existe, parte do caminho do dinheiro não passa pelo funil próprio nem aparece no CRM, e o diagnóstico do funil ficaria cego para essa fatia.", t:"L", f:"Fluxo de Receita", c:1, v:"i"},
 {q:"O crescimento dos últimos 12 meses veio mais de cliente novo ou de expansão na base?", h:"Separar aquisição de expansão. A resposta decide qual ponta do funil o Ciclo 1 ataca.", t:"L", f:"Fluxo de Receita", c:1, v:"i"},
 {q:"Qual o preço de tabela e qual o desconto médio praticado, por segmento?", h:"A distância entre tabela e praticado costuma ser onde a Trava de Decisão aparece com evidência formal.", t:"L", f:"Decisão", c:1, v:"i"},
 {q:"O que define um cliente ativo, e como uma conta morre?", h:"Cancelamento formal, downgrade até o plano mínimo, inadimplência, ou simplesmente parar de anunciar. Cada um é um tipo diferente de perda e pede um remédio diferente.", t:"L", f:"Retenção", c:1, v:"i"},
 {q:"Do primeiro contato ao dinheiro na conta, quem toca o quê?", h:"Quem prospecta, quem precifica, quem aprova desconto, quem fatura, quem cobra. Cada troca de mão no caminho do dinheiro é um ponto de perda possível.", t:"L", f:"Fluxo de Receita", c:1, v:"i"},
 {q:"Existe alguma linha de receita relevante que não passa por nada do que falamos até aqui?", h:"Dados, API, parcerias, licenciamento, programática. Pergunta de fechamento da árvore: o que sobrar aqui é o que a leitura do sistema estaria ignorando.", t:"L", f:"Fluxo de Receita", c:1, v:"i"}
]},
{n:"04", t:"Funil e operação comercial", d:"Da geração de demanda ao pagamento e à renovação. Aqui moram as travas de Qualificação, Compromisso e Decisão.", tempo:"25 min", qs:[
 {q:"Desenhe o funil ponta a ponta, etapa por etapa, com o nome que vocês usam internamente", h:"Um funil que o cliente não reconhece não serve para conduzir comitê.", t:"L", f:"Fluxo de Receita", c:1, v:"e"},
 {q:"Volumes e taxas de conversão por etapa, últimos 12–24 meses", h:"Bloco A2.", t:"L", f:"Fluxo de Receita", c:1, v:"p"},
 {q:"Estrutura do time comercial: quantos SDRs, closers, farmers, CS; a quem reportam", h:"Bloco A4.", t:"L", f:"Pré-vendas", v:"p"},
 {q:"Metas e modelo de comissionamento por papel", h:"O comissionamento explica o comportamento do funil melhor que o processo escrito.", t:"L", f:"Pré-vendas", c:1, v:"e"},
 {q:"Qual CRM? Qual a fonte de verdade do pipeline?", t:"t", f:"Pré-vendas", c:1, v:"p"},
 {q:"Quais são os estágios do pipeline e a definição objetiva de cada um?", h:"Definição objetiva = o que precisa ser verdade para o negócio avançar.", t:"L", f:"Pré-vendas", c:1, v:"e"},
 {q:"Existe SLA de primeiro contato? Qual é e ele é medido?", t:"L", f:"Compromisso", c:1, v:"e"},
 {q:"Motivos de perda são catalogados? Quais são os cinco principais?", h:"Sem catálogo de perda, a Trava de Decisão não tem evidência.", t:"L", f:"Decisão", c:1, v:"e"},
 {q:"Taxa de no-show em reuniões agendadas", t:"t", f:"Compromisso", v:"p"},
 {q:"Qual o critério de qualificação hoje? Está escrito?", h:"E quem pode desqualificar um lead.", t:"L", f:"Qualificação", c:1, v:"e"},
 {q:"Ferramentas de sales engagement, telefonia e gravação de call", h:"Bloco J. Define se a camada experiencial pode usar gravação real.", t:"L", f:"Pré-vendas", v:"p"},
 {q:"Podemos ouvir gravações de call e acompanhar reuniões reais?", h:"Camada experiencial do diagnóstico. Verificar consentimento e LGPD.", t:"L", f:"Diagnóstico", c:1, v:"p"},
 {q:"Como funciona a renovação? Quem cuida? É ativa ou automática?", t:"L", f:"Retenção", c:1, v:"e"},
 {q:"Motivos de cancelamento são registrados?", t:"L", f:"Retenção", c:1, v:"p"}
]},
{n:"05", t:"Marketing, canais e comunicação", d:"Insumo direto de sete dos nove diagnósticos contratados.", tempo:"20 min", qs:[
 {q:"Verba mensal de mídia por unidade e por canal", h:"Bloco G: prioritário.", t:"L", f:"Diagnóstico (vi)", c:1, v:"p"},
 {q:"Quem opera a mídia: time interno, agência, ou os dois? Quem é o DRI?", t:"L", f:"Diagnóstico (vi)", c:1, v:"p"},
 {q:"Quais contas de anúncio existem e qual o status de acesso de cada uma?", h:"Os acessos vão para gina@v4company.com.", t:"L", f:"Acessos", c:1, v:"p"},
 {q:"O que roda hoje no Salesforce Marketing Cloud? Quais jornadas estão ativas?", h:"Bloco B, diagnóstico (i).", t:"L", f:"Diagnóstico (i)", c:1, v:"p"},
 {q:"Quais são os domínios e ambientes B2B? Quem tem acesso ao CMS?", h:"Bloco C, diagnóstico (ii).", t:"L", f:"Diagnóstico (ii)", c:1, v:"p"},
 {q:"Quais landing pages e fluxos de conversão B2B existem hoje?", h:"Bloco I, diagnóstico (viii).", t:"L", f:"Diagnóstico (viii)", v:"p"},
 {q:"Quais perfis sociais e canais de conteúdo são B2B?", h:"Bloco F, diagnóstico (v). Separar do que é comunicação de consumidor.", t:"L", f:"Diagnóstico (v)", v:"p"},
 {q:"Existe biblioteca de criativos e mensagens? Onde vive?", h:"Bloco E, diagnóstico (iv).", t:"L", f:"Diagnóstico (iv)", v:"p"},
 {q:"Já existe leitura de presença em buscas generativas (ChatGPT, Gemini, Perplexity)?", h:"Bloco D, diagnóstico (iii). Provavelmente não: registrar como linha de base zero.", t:"L", f:"Diagnóstico (iii)", v:"p"},
 {q:"Quem são os concorrentes diretos no B2B, na visão de vocês?", h:"Base do Mapa de Exposição Competitiva.", t:"L", f:"Exposição", c:1, v:"e"},
 {q:"Qual a proposta de valor que vocês comunicam hoje ao anunciante?", h:"Comparar depois com o que o mercado percebe.", t:"L", f:"Atenção", v:"e"}
]},
{n:"06", t:"Dados, tracking e liberação", d:"O gargalo mais comum do Ciclo 1 não é análise, é o dado não chegar. Cada bloco precisa sair daqui com dono e prazo.", tempo:"20 min", qs:[
 {q:"Existe BI ou fonte única de verdade? Qual?", h:"Ou o número vive em planilhas paralelas por área?", t:"L", f:"Cegueira", c:1, v:"e"},
 {q:"Quem consegue extrair dado bruto do CRM e do transacional, e em quanto tempo?", t:"L", f:"Cronograma", c:1, v:"p"},
 {q:"GA4 e GTM: quais propriedades, quem administra, existe data layer documentado?", h:"Bloco H, diagnóstico (vii): prioritário. Determina a confiabilidade de todo o resto.", t:"L", f:"Diagnóstico (vii)", c:1, v:"p"},
 {q:"O que pode sair da OLX, em que formato e com qual anonimização?", h:"Define se trabalhamos com dado agregado ou nominal. Cláusula 5.3 do contrato.", t:"L", f:"LGPD", c:1, v:"p"},
 {q:"Como o data room será operado, Drive da OLX exige conta @olxbr.com?", h:"A conta de Rafael Corazza (rafael.corazza-ext@olxbr.com) saiu em 24/08 e por enquanto o time da V4 opera por ela. Faltam as de Anselmo Bueno e Guilherme Monteiro.", t:"L", f:"Acessos", c:1, v:"p"},
 {q:"Qual o prazo realista para a primeira leva de dados (blocos A, G, H, J)?", h:"Estes quatro são prioritários e destravam o diagnóstico.", t:"t", f:"Cronograma", c:1, v:"p"},
 {q:"Existe restrição de horário, ambiente ou VPN para acesso às ferramentas?", t:"L", f:"Acessos", v:"p"},
 {q:"Há alguma métrica que vocês sabem que hoje está errada ou não confiável?", h:"Pergunta que costuma render o melhor achado do kick-off.", t:"L", f:"Cegueira", c:1, v:"e"}
]},
{n:"07", t:"Hipótese do cliente e histórico", d:"Registrar como hipótese, nunca como diagnóstico. A divergência entre o que o cliente acredita e o que o dado mostra é o valor do produto.", tempo:"15 min", qs:[
 {q:"Na percepção de vocês, onde está o gargalo de receita hoje?", h:"Vai para o client.json como hipótese_cliente, separado da restrição diagnosticada.", t:"L", f:"Consolidação causal", c:1, v:"e"},
 {q:"O que já tentaram para resolver isso? O que funcionou e o que não funcionou?", h:"Tentativa que falhou é evidência de conflito estrutural, insumo da Nuvem.", t:"L", f:"CRT · Nuvem", c:1, v:"e"},
 {q:"O que não pode ser mexido?", h:"Restrições políticas, contratuais, de marca, de tecnologia. Define o campo do possível.", t:"L", f:"PRT", c:1, v:"e"},
 {q:"Que decisão vocês vêm adiando porque envolve escolher entre duas coisas importantes?", h:"Pergunta que revela a nuvem de conflito antes do workshop.", t:"L", f:"Nuvem de Conflito", c:1, v:"e"},
 {q:"Qual resultado, em 12 meses, faria vocês considerarem este projeto um sucesso?", h:"Número e prazo. Vira critério da Goal Tree.", t:"L", f:"Goal Tree", c:1, v:"e"},
 {q:"E o que faria vocês considerarem fracasso?", h:"Mais informativo que a pergunta anterior.", t:"L", f:"Goal Tree", c:1, v:"e"},
 {q:"Que resultado precisa aparecer nos primeiros 90 dias para sustentar o projeto internamente?", t:"L", f:"Plano de 90 dias", c:1, v:"e"}
]},
{n:"08", t:"Ritual, agenda e comunicação", d:"Agenda de comitê que não é bloqueada hoje vira remarcação em outubro.", tempo:"10 min", qs:[
 {q:"Datas dos 3 comitês do Ciclo 1, bloquear agenda agora", h:"Referência: Comitê 1 na semana 4–5, Comitê 2 na 6–7, Comitê 3 na 12.", t:"L", f:"Cronograma", c:1, v:"p"},
 {q:"Formato de cada comitê: presencial ou remoto, e onde", h:"O método padrão DR-E prevê 8 online + 4 presenciais; o contrato fala em 12 encontros sem distinguir. Fechar a distribuição hoje.", t:"L", f:"Cronograma", c:1, v:"p"},
 {q:"Canal de comunicação assíncrona, qual ferramenta, quem entra?", t:"t", f:"Assessoria", v:"p"},
 {q:"O SLA de 12 horas úteis atende? Qual a expectativa de vocês?", h:"Alinhar antes que vire atrito.", t:"t", f:"Assessoria", c:1, v:"p"},
 {q:"Cadência e formato de reporte entre comitês", t:"L", f:"Assessoria", v:"p"},
 {q:"Períodos de blackout: férias, fechamento, feriados, freeze de sistema", t:"L", f:"Cronograma", v:"p"}
]},
{n:"09", t:"Pendências contratuais a fechar", d:"Cinco pontos abertos identificados na leitura do contrato. Levar resolvidos daqui, ou com dono e prazo.", tempo:"15 min", qs:[
 {q:"Valor do contrato: e-mail acordou R$ 740.000, contrato registra R$ 752.000 (Δ R$ 12.000). Qual prevalece?", t:"L", f:"Contrato", c:1, v:"p"},
 {q:"Gatilho do Bônus de Sucesso: existem três definições incompatíveis nos documentos. Qual é a válida?", h:"Contrato cl. 3.3 (cumprimento integral do escopo) · SOW padrão DR-E (expansão comprovada de 2 das 8 travas em D+370) · e-mail Mirella 10/08 (KPIs a construir no diagnóstico). Define R$ 376.000.", t:"L", f:"Contrato", c:1, v:"p"},
 {q:"A janela de garantia (cláusula 2.3) fecha no primeiro encontro. A OLX está ciente?", h:"Registrar em ata que foi comunicado hoje.", t:"L", f:"Contrato", c:1, v:"p"},
 {q:"A cláusula 1.2 fala em 7 travas; o método opera com 8 (a 8ª é a Cegueira, pré-condição). Alinhar redação.", t:"L", f:"Contrato", v:"p"},
 {q:"Contas @olxbr.com: a de Rafael Corazza saiu em 24/08. Prazo para as de Anselmo Bueno e Guilherme Monteiro?", h:"Enquanto for uma só, o acesso ao data room é compartilhado e não deixa rastro de quem leu o quê, o que é frágil para LGPD.", t:"t", f:"Acessos", c:1, v:"p"}
]},
{n:"10", t:"Fechamento", d:"Nada aqui pode sair sem nome e data.", tempo:"10 min", qs:[
 {q:"Decisões tomadas nesta sessão", h:"Uma linha por decisão, com o racional.", t:"L", f:"Ata", c:1, v:"p"},
 {q:"Próximos passos: ação, responsável (pessoa), prazo", t:"L", f:"Ata", c:1, v:"p"},
 {q:"O que ficou em aberto e o que falta para fechar", t:"L", f:"Pendências", c:1, v:"p"},
 {q:"Data e formato do próximo encontro", t:"t", f:"Cronograma", c:1, v:"p"}
]}
];

const BLOCOS_DADOS = [
 {id:"A", nome:"Visão de negócio e Fluxo de Receita", prio:1, itens:"Receita 24m por linha · funil 12–24m · ticket, ciclo e CAC · organograma de Mkt/Pré-vendas/Vendas · OKRs e metas · ICP atual", alim:"Fluxo de Receita e Forecast"},
 {id:"B", nome:"CRM Marketing (Salesforce Marketing Cloud)", prio:0, itens:"Jornadas ativas · bases e segmentações · métricas de e-mail · integrações", alim:"Diagnóstico (i) · Interesse e Retenção"},
 {id:"C", nome:"Ambientes CRO/SEO (domínios B2B)", prio:0, itens:"Domínios · acesso ao CMS · Search Console · mapa de páginas", alim:"Diagnóstico (ii) · Exposição e Interesse"},
 {id:"D", nome:"GEO: IA e Buscas Generativas", prio:0, itens:"Presença em respostas de IA · termos monitorados (se houver)", alim:"Diagnóstico (iii) · Exposição e Atenção"},
 {id:"E", nome:"Criativos Ads & Mensagens", prio:0, itens:"Biblioteca de criativos · mensagens por segmento · histórico de testes", alim:"Diagnóstico (iv) · Atenção"},
 {id:"F", nome:"Redes Sociais e Conteúdo Orgânico", prio:0, itens:"Perfis B2B · calendário · métricas orgânicas 12m", alim:"Diagnóstico (v) · Exposição e Atenção"},
 {id:"G", nome:"Mídia Paga (Google e Meta)", prio:1, itens:"Acesso às contas · investimento e performance 12m por campanha", alim:"Diagnóstico (vi) · Exposição, Atenção e Qualificação"},
 {id:"H", nome:"Rastreamento Completo (GA4 e GTM)", prio:1, itens:"Acesso GA4 e GTM · data layer · eventos e conversões configuradas", alim:"Diagnóstico (vii) · Cegueira"},
 {id:"I", nome:"Páginas de Captura e Fluxos de Conversão", prio:0, itens:"LPs ativas · formulários · fluxos pós-conversão", alim:"Diagnóstico (viii) · Interesse e Compromisso"},
 {id:"J", nome:"Pré-Vendas, Qualificação e Sales Engagement", prio:1, itens:"CRM · cadências · scripts · gravações · motivos de perda", alim:"Diagnóstico (ix) · Qualificação, Compromisso e Decisão"}
];
