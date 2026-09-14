# Checklist de Dados e Acessos · Diagnóstico

Lista enviada por Gustavo Figueiredo ao Grupo OLX em **11/08/2026**, organizada por frente de
trabalho do DR-E.

**Prioridade declarada:** blocos **A, G, H e J**, "destravam as análises de maior impacto;
o restante pode ser complementado nas duas primeiras semanas."

**Legenda de status:** ✅ recebido · 🟡 parcial · 🟠 solicitado, pendente · ⚪ não iniciado · 🔴 inexistente (registrar como evidência diagnóstica)

**Material recebido até agora:** primeiro lote do data room baixado em **24/08/2026**, 9 arquivos nos blocos E e I; a série de receita do bloco A por e-mail em **28/08**; os exports de GTM do bloco H em **01/09**. Índice, procedência e leitura inicial em [`assets/originais/README.md`](../assets/originais/README.md).

**Acessos verificados em 31/08 e 01/09/2026:** GA4 liberado (H1 ✅) e **GTM confirmado** (H2 ✅), o bloco H, prioritário, está com os dois acessos. Search Console, Salesforce, CRM e ferramentas de SEO/comportamento seguem sem concessão.

**Atualização de 14/09, apurada na API e não declarada:** o V4MOS **deixou de estar inalterado**. As duas contas de Meta foram aprovadas no lote de 10/09, a ingestão começou em 12/09 e a recoleta de 14/09 devolve 90 campanhas, 1.079 anúncios e R$ 7,38 mi no Meta, contra 23 campanhas e R$ 2,75 mi no Google, sobre 01/01/2025 a 14/09/2026. Isto entra aqui porque foi **medido na ferramenta**, não porque alguém informou.

### Conferência do lote de 10/09, feita em 14/09

O método é abrir a fonte, nunca ler o e-mail de concessão. **Nenhum item subiu de status sem
evidência de abertura**, e é por isso que a maior parte da tabela continua como estava.

| Ferramenta | Como foi conferida | Resultado |
|---|---|---|
| **GA4** | Admin API e Data API, ao vivo | ✅ 26 propriedades em 3 contas, **as mesmas de 31/08**: o lote de 10/09 não acrescentou nenhuma. Leitura de dado funciona |
| **V4MOS** | 3 endpoints + os 2 controles de sanidade | ✅ Google 500 e Facebook 114 registros em setembro. Secret inválido devolve 401, organização inexistente devolve 403 |
| **Meta Ads**, as duas contas | Indiretamente, pela ingestão | ✅ Saem de `data: []` para 1.079 anúncios. Só ativo compartilhado produz isso |
| **Google Ads**, MCC 526-656-0190 | Indiretamente, pela ingestão | 🟡 O V4MOS puxa a conta. **A interface não foi aberta** |
| **GTM** | API do Tag Manager | 🔴 **403**, a credencial não tem o escopo `tagmanager.readonly` ([pendência 26](../PENDENCIAS.md)). Export segue manual |
| **CRM comercial** · **Marketing Cloud** · **Search Console** · **Business Manager** | - | 🔴 **Não conferidos.** Não há conector destas fontes neste ambiente: exigem abrir a interface ou pedir export |

> 🔴 **As quatro não conferidas são as que importam para o Comitê 1.** São elas que prendem os **23
> indicadores** marcados como acesso declarado e não conferido no catálogo de métricas, **18 deles
> P0**, e **20 dependem só do CRM comercial**. Três dos quatro dados que faltam para o forecast
> saem de lá: ticket médio de entrada, base ativa de anunciantes e contratos novos por mês.
>
> Elas ficam registradas como pendentes **de propósito**. Promover para concedido sem abrir a
> ferramenta seria trocar um registro desatualizado por um registro otimista, e este projeto já
> levou dois calotes assim: o GA4 chegou em nível Leitor e o Meta chegou com "nenhum ativo
> conectado". Estado item a item em [`dados/acessos.json`](../dados/acessos.json).

---

## 🔴 A. Visão de negócio e Fluxo de Receita · PRIORITÁRIO
*Base para o diagnóstico das travas e para o Mapeamento do Fluxo de Receita.*

| # | Item | Status | Obs. |
|---|---|---|---|
| A1 | Receita mensal dos últimos **24 meses**, aberta por linha de negócio / segmento / produto | 🟡 | **Recebido em 28/08.** 20 meses (jan/25 a jul/26) contra 24, 39 linhas sobre 4 unidades. Falta 2024. [Leitura](serie-de-receita-2025-2026.md) |
| A2 | Funil comercial completo (volumes e taxas de conversão por etapa), últimos **12–24 meses** | 🟡 | **Recebido em 28/08, versionado em 14/09.** 4 meses (abr a jul/26) contra 12–24, e só Inside Sales, que cobre 39% da receita de RE e 17% de Autos. [Leitura](estrutura-comercial-inside-sales.md) |
| A3 | Ticket médio, ciclo de vendas e CAC por canal (se disponível) | 🟡 | Ticket de entrada (R$ 707 RE, R$ 602 Autos) e lead time (1,2 a 2,4 dias) recebidos. **CAC por canal continua ausente.** [Leitura](estrutura-comercial-inside-sales.md) |
| A4 | Estrutura organizacional de Marketing, Pré-Vendas e Vendas (organograma e responsabilidades) | 🟡 | 101 HCs de Inside Sales por célula e papel (hunter e farmer). Falta Marketing e Pré-Vendas. [Leitura](estrutura-comercial-inside-sales.md) |
| A5 | Planejamento estratégico / OKRs vigentes e metas comerciais | 🟡 | Mapa Estratégico 2026 e mapa de OKRs com % de atingimento por vertical. **Sem meta comercial em número absoluto.** [Leitura](estrutura-comercial-inside-sales.md) |
| A6 | Definição atual de ICP e segmentação de mercado | 🟡 | Segmentação por porte operada de fato: RE usa PP (<25), P (25–80), M (80–600), G (650+); Autos usa P (<10), M (11–50), G (50+). Não é ICP, é corte de carteira. [Leitura](estrutura-comercial-inside-sales.md) |

> A1–A3 são os insumos **matemáticos** do Forecast. Sem eles, o funil não valida contra o
> faturamento declarado e o forecast não pode ser construído.

> **A1 saiu de ⚪ em 08/09**, com a série de receita 2025–2026 recebida em 28/08. É o primeiro
> denominador auditável do projeto: a soma das unidades bate com o TOTAL nos 19 meses fechados.
> Com ele, um ponto percentual de run-rate deixou de ser abstração e virou R$ 428 mil por mês na
> linha `Classifieds - B&A`.

> 🔴 **O bloco A inteiro saiu de ⚪ em 14/09, e o material estava conosco desde 28/08.** A apresentação
> Estrutura Comercial Inside Sales chegou no mesmo dia que a série A1, ficou na pasta de Downloads do
> operador e nunca foi versionada nem lida. Ela fecha A2 e A3 em nível parcial, mais A4, A5 e A6.
> **A lição operacional é a mesma da pendência 18:** material recebido que ninguém abre vale zero, e o
> projeto passou 17 dias tratando como bloqueio uma coisa que já tinha.

> **O que A2 ainda não resolve:** são 4 meses contra os 12–24 pedidos, e cobrem só a operação de Inside
> Sales, que responde por 39% da receita de Real Estate e 17% de Autos. Para o forecast falta série
> longa, movimento mensal de base (entrada e saída) e CAC.

## B. CRM Marketing
*Alimenta o diagnóstico (i), Salesforce Marketing Cloud.*

| # | Item | Status | Obs. |
|---|---|---|---|
| B1 | Acesso de visualização | 🟠 | Declarado concedido no lote de 10/09, **sem conferência na ferramenta** ([pendência 18](../PENDENCIAS.md)). O Sales Cloud depende do e-mail `@olxbr` habilitado no MyApps |
| B2 | Arquitetura de Data Extensions e lógica de segmentação atual | 🟡 | **Descrita nas sessões de 09 e 10/09**, incluindo o comparativo DEX legado vs. Campana e as regras de segmentação em uso. Os slides foram apresentados em tela e **não recebidos** |
| B3 | Relatórios de performance de e-mail dos últimos 12 meses (entregabilidade, open, CTR, conversão) | ⚪ | O pedido mudou de sentido: **o e-mail está desligado na aquisição desde a migração**, então a série de 12 meses é de ciclo de vida, não de aquisição |
| B4 | Tamanho e saúde da base opt-in | 🟡 | A **saúde** foi descrita e é ruim: CEP ausente em mais de 50%, nomes duplicados e `undefined`, documento em campo de nome. O **tamanho** não foi dito em nenhuma das duas sessões |

> ⚠️ **O bloco B foi desenhado para uma ferramenta e o GTM mostrou quatro.** Além do Salesforce
> Marketing Cloud, o export de 01/09 revelou **Insider** (`10007563`, web push e personalização,
> ativo), **Braze** (`sdk.iad-07.braze.com`, instrumentação completa mas **14 tags pausadas**) e
> **RD Station** (contêiner `GTM-MVQWQJFB` em `materiais.olx.com.br`). Mais os cookies `sf_utm_*`
> que alimentam atribuição no Salesforce. **Perguntar qual é a ferramenta oficial e o que as outras
> três fazem**, quatro plataformas de relacionamento convivendo já é achado de maturidade.

> ✅ **A camada experiencial do bloco B fechou em 10/09**, com duas sessões e todo o time de CRM B2B
> na sala. Leitura completa, com 16 achados, em
> [`auditoria-i-crm-marketing.md`](auditoria-i-crm-marketing.md). O que ela muda aqui:
>
> - **A stack declarada é Salesforce Marketing Cloud + Blip**, e mais nada. Em duas horas de CRM,
>   **Insider, Braze e RD Station não foram citados uma única vez**. A pergunta da nota acima
>   continua aberta, agora com peso: ou as três são de outra área, ou não têm dono.
> - **A Blip entra no bloco B como quinta ferramenta**, e é por ela que sai 99% a 100% da aquisição.
>   Não tem integração com o Marketing Cloud: a base sai em planilha e sobe à mão.
> - **O que mais importa não é o que falta receber, é o que está desligado.** As jornadas de ciclo
>   de vida do cliente novo estão fora do ar desde abril em Autos e julho em Imóveis. Pedir
>   relatório de performance de uma operação parada mede o período anterior, não o atual.

## C. Ambientes CRO/SEO (domínios B2B)
*Alimenta o diagnóstico (ii).*

| # | Item | Status | Obs. |
|---|---|---|---|
| C1 | Relação de domínios e subdomínios B2B em escopo | 🟡 | **Reconstruída do GA4 em 01/09**, não recebida da OLX, falta a OLX confirmar quais estão em escopo. Ver tabela abaixo |
| C2 | Acesso ao Google Search Console de cada propriedade | 🟠 | Sem concessão. **Declarado no lote de 10/09 e não conferido em 14/09**: não há conector de Search Console neste ambiente, a conferência exige abrir a interface. É uma das quatro ferramentas que a [pendência 18](../PENDENCIAS.md) manda abrir |
| C3 | Acesso à ferramenta de SEO utilizada internamente (SEMrush, Ahrefs ou similar), se houver | ⚪ | Pode não existir, se não existir, é achado de maturidade |

**C1 · Domínios com tráfego na propriedade GA4 Grupo OLX** (`503925542`), jun–ago/2026, por sessões:

| Domínio | Sessões | Leitura |
|---|---:|---|
| `lp.olx.com.br` | 2.146.626 | Farm de landing pages, 87% do tráfego da propriedade |
| `ads.grupoolx.com.br` | 168.238 | **Candidato a domínio de captação de anunciante** |
| `vender.olx.com.br` | 165.796 | Jornada de quem vende |
| `app.olx.com.br` | 75.959 | |
| `grupoolx.com.br` + `www.` | 34.069 | Institucional |
| `imoveis.grupoolx.com.br` | 23.373 | Vertical Imóveis B2B |
| `validador.olx.com.br` | 19.004 | |
| `autos.grupoolx.com.br` | 13.963 | Vertical Autos B2B |
| `olxpay` · `bemvindo` · `eventos` · `bensdeconsumo` · `dicas` · `cms` · `historicoveicular` · `chama-na-olx` | < 3.000 cada | Cauda longa |

> A família `*.grupoolx.com.br` é a que mais se parece com o recorte B2B contratado, e `ads.` é a mais
> promissora. **Confirmar com a OLX** antes de fixar o escopo: a leitura é de tráfego, não de negócio.

## D. GEO (IA e Buscas Generativas)
*Alimenta o diagnóstico (iii). Demais insumos cobertos por C e G.*

| # | Item | Status |
|---|---|---|
| D1 | Lista de queries / temas prioritários de marca e categoria | ⚪ |
| D2 | Inventário de conteúdo institucional e educativo publicado | ⚪ |

## E. Criativos Ads & Mensagens
*Alimenta o diagnóstico (iv).*

| # | Item | Status | Obs. |
|---|---|---|---|
| E1 | Biblioteca de criativos veiculados nos últimos 6–12 meses | 🟡 | 8 peças de **uma** campanha (Mês do Corretor 2026, SP, consideração, RE) recebidas em 24/08, ver [originais](../assets/originais/README.md#bloco-e--criativos-anúncios-e-mensagens). Falta o resto da janela de 6–12 meses |
| E2 | Brandbook, diretrizes de marca e documento de proposta de valor (messaging house, se existir) | ⚪ | |
| E3 | Briefings das principais campanhas recentes | ⚪ | Sem os briefings não dá para saber qual era a hipótese por trás das variantes V1, V2 e V3 recebidas em E1 |

## F. Redes Sociais e Conteúdo Orgânico
*Alimenta o diagnóstico (v).*

| # | Item | Status |
|---|---|---|
| F1 | Acesso de analista ao Meta Business Suite e à(s) Company Page(s) do LinkedIn | ⚪ |
| F2 | Acessos equivalentes a demais canais ativos (YouTube, TikTok, etc.) | 🟡 |
| F3 | Calendário editorial e relatórios de performance orgânica dos últimos 6 meses | ⚪ |

> **F2 · canais confirmados pelo GTM (01/09):** TikTok pixel `CO25OBRC77U47AMPJES0` **ativo** em
> Conecta Autos. Meta com **três pixels distintos**: `592658194155317`, `818079879779548`,
> `935989184453347`. YouTube com rastreamento de vídeo instrumentado. Não é mais "a confirmar quais
> canais existem", é pedir acesso a esses.

## 🔴 G. Mídia Paga (Google e Meta) · PRIORITÁRIO
*Alimenta o diagnóstico (vi).*

| # | Item | Status | Obs. |
|---|---|---|---|
| G1 | Acesso de leitura às contas de Google Ads e Meta Ads (IDs das contas) | ✅ | **As três contas ingerem, conferido em 14/09.** As duas de Meta (612188193108418 e 1742214902479721) saíram no lote de 10/09 e a MCC do Google já estava. Conferência **indireta, pela ingestão no V4MOS**, que é prova de acesso de leitura: nenhuma das duas interfaces foi aberta. Segue faltando o escopo, não o acesso: em 31/08 o GA4 revelou **7 contas de Google Ads** vinculadas à propriedade ZapImóveis, e a conta a que a V4 tem acesso não está entre elas, e a lista de contas do portfólio Meta nunca veio, ver PENDÊNCIAS 11 e 12 |
| G2 | Investimento mensal por canal/campanha dos últimos 12 meses | 🟡 | **Existe desde 14/09, e não serve como está.** A coleta do V4MOS entrega R$ 10,12 mi com quebra mensal e por campanha sobre 21 meses (Meta R$ 7,38 mi em 90 campanhas, Google R$ 2,75 mi em 23). Duas ressalvas: **nenhuma conta separa B2B de B2C**, então isto não é o investimento do recorte contratado, e o Google tem só 11 meses com dado, faltam nov/2025 a abr/2026. O item fecha quando o time de mídia disser qual campanha é captação de anunciante |
| G3 | Plano de mídia vigente e definição das conversões otimizadas em cada plataforma | ⚪ | |
| G4 | Metas de CPA/ROAS praticadas e contato da agência, caso a operação seja terceirizada | ⚪ | |

## 🔴 H. Rastreamento Completo (GA4 e GTM) · PRIORITÁRIO
*Alimenta o diagnóstico (vii).*

| # | Item | Status | Obs. |
|---|---|---|---|
| H1 | Acesso de analista à(s) propriedade(s) GA4 | ✅ | **Liberado · confirmado em 31/08.** 3 contas e 26 propriedades: Grupo OLX (285763706), OLX (70177409), Viva Real (126375). **Nível: Leitor**, confirmado na interface pelo operador em 01/09, bate com o `can_edit=false` que a API devolve nas 26 propriedades. **Reconferido por API em 14/09**, e o quadro não mudou: as mesmas 26 propriedades, `can_edit=false` em todas, e `custom_dimensions` e `custom_metrics` vazias na propriedade B2B 503925542, o que é coerente com Leitor. **O lote de 10/09 não acrescentou nenhuma propriedade.** O documento de 25/08 pede Editor ou Administrador: **pedido em aberto** |
| H2 | Acesso de leitura ao(s) contêiner(es) GTM publicados | ✅ | **Confirmado em 01/09** na interface. Conta `BR - www.olx.com.br`, selo 360, com **22+ contêineres**. Inventário abaixo. ⚠️ **A API segue fechada, testada em 14/09**: devolve `403`, a credencial não tem o escopo `tagmanager.readonly`, então todo export continua manual ([pendência 26](../PENDENCIAS.md)) |
| H3 | Plano de mensuração e taxonomia de eventos e conversões, se documentado | 🟡 | Não recebido, mas **reconstruído** a partir do export de 5 contêineres em 01/09, ver [auditoria (vii)](auditoria-vii-rastreamento.md). A taxonomia praticada tem duas grafias para o mesmo conceito e um gatilho que escuta evento inexistente |
| H4 | Configuração de consentimento (LGPD / consent mode) e eventual tagueamento server-side | 🟡 | **Auditado em 01/09 pelo export.** Consent mode via AdOpt, client-side, sem contêiner server-side. Três problemas: padrão `granted` em tudo, botão de recusar oculto por CSS, injetor com 4s de atraso, ver [auditoria (vii)](auditoria-vii-rastreamento.md) achado 2 |

### H2 · Inventário de contêineres: conta `BR - www.olx.com.br`

> 🔴 **Corrigido em 02/09: são quatro contas de GTM, não uma.** `BR - www.olx.com.br` (`94905`),
> `Checkout Unificado - PRO` (`6326134112`), `VivaReal` (`4412254379`) e `ZapImóveis`
> (`2971905372`), todas com selo 360. O inventário abaixo cobre **só a primeira**. Dos 11 exports
> recebidos, 10 são dela e 1 da ZapImóveis; as outras duas contas estão inteiramente por auditar.
> Ver [PENDÊNCIAS 17](../PENDENCIAS.md) e o Bloco 0 de [`coleta-pendente.md`](coleta-pendente.md).

Confirmado por acesso à interface em 01/09/2026. A lista é alfabética e estava cortada na captura,
então **22 é piso desta conta**, não total do grupo.

| Contêiner | ID | Tipo | Relevância para o escopo B2B |
|---|---|---|---|
| **OLX - Planos Profissionais & PAYG** | `GTM-KGFGVFC` | Web | 🔴 **Máxima.** É a monetização do anunciante profissional, a receita contratada |
| **OLX - Seller Journey** | `GTM-MXQKDG3` | Web | 🔴 **Máxima.** Jornada de quem anuncia |
| **OLX - Container Master** | `GTM-546N2JV` | Web | 🔴 É o que carrega em `ads.`, `imoveis.`, `autos.`, institucional e `vender.olx.com.br` |
| **OLX - Checkout** | `GTM-M4TL57GX` | Web | 🔴 Onde o pagamento acontece, fecha o fluxo de receita |
| OLX - Conecta Autos | `GTM-MJX9PG4` | Web | 🟠 Vertical Autos B2B |
| OLX - Buyer Journey | `GTM-TNX8FDS` | Web | 🟡 Contraponto B2C, útil para comparar padrão de medição |
| OLX - RD Station \| LP | `GTM-MVQWQJFB` | Web | 🟡 **Indica RD Station na stack**, ver nota |
| OLX - LPs · Site Institucional · Login · Favoritos · Chat · Chatbot · Central de Ajuda · [OLD] Ajuda · Dicas · Hub Segurança · Encontro Certo · Projetos Especiais de Autos · Teste Adopt | - | Web | ⚪ Fora do recorte imediato |
| [New] Android Tracking · [New] iOS Tracking | `GTM-52W35LS` · `GTM-T8ZBL8Z` | App | ⚪ Camada de app |

> **Achado lateral: RD Station.** Existe um contêiner dedicado a RD Station. O contrato e o checklist
> tratam Salesforce Marketing Cloud como o CRM de marketing (bloco B). Se RD Station também opera,
> há **duas ferramentas de automação convivendo**, o que muda o desenho de B1–B4 e é sintoma clássico
> de medição fragmentada. Confirmar no próximo contato.

> ✅ **Export recebido em 01/09** dos 5 contêineres do recorte B2B. Auditoria em
> [`auditoria-vii-rastreamento.md`](auditoria-vii-rastreamento.md): 5 achados críticos, 12 relevantes.
> Faltam os exports de `GTM-PZ733B5` (Zapimóveis ANUNCIE), `GTM-5WWRGTQ`, `GTM-KP8QMDH`, `GTM-T2H3VFL`
> e `GTM-PWP7Z4C`, descobertos nas zonas do Master e ausentes da lista visível.

> **Ter acesso não é o mesmo que conseguir auditar:** não há conector de GTM neste ambiente. O caminho
> é **exportar o contêiner em JSON** (Administração → Exportar contêiner) e versioná-lo no repositório,
> o que permite auditar tags, gatilhos, variáveis e consent mode offline. **Não são os 22**, bastam os
> quatro marcados 🔴 mais o Conecta Autos para cobrir o escopo contratado.

> **O que o nível Leitor entrega e o que não entrega.** Entrega tudo que já foi levantado: eventos,
> eventos-chave, canais, atribuição, vínculos de Google Ads, tier de serviço, domínios. Isso sustenta
> a auditoria (vii) na camada de **sintoma**.
>
> Não entrega as telas de Administração: **configuração dos fluxos de dados**, regras de criação e
> modificação de evento, definições personalizadas, detalhe da configuração de conversão, retenção de
> dados, domínios cruzados, filtros de tráfego interno e referências indesejadas, e a **configuração
> de consentimento (H4)**. É a camada de **causa**, exatamente o que o documento de 25/08 argumentou
> ao pedir Editor.
>
> **Mitigação parcial:** boa parte da causa vive no GTM, não no GA4. Com o export dos contêineres em
> JSON dá para reconstruir tags, gatilhos, variáveis e consent mode sem elevar o nível do GA4. O que
> continua fora de alcance é a configuração server-side do próprio GA4.

## I. Páginas de Captura e Fluxos de Conversão
*Alimenta o diagnóstico (viii).*

| # | Item | Status | Obs. |
|---|---|---|---|
| I1 | URLs das principais LPs e fluxos de conversão ativos | 🟡 | Reconstruível do GA4. O GTM revelou que as LPs rodam em **Unbounce** (contêiner `GTM-KP8QMDH`), sobre ~20 hostnames listados na zona correspondente |
| I2 | Taxas de conversão por página / etapa | ⚪ | |
| I3 | Histórico de testes A/B realizados, se houver | 🟡 | 1 teste recebido em 24/08 (LP Anuncie ZAP, 17–23/03), ver [originais](../assets/originais/README.md#bloco-i--páginas-de-captura-e-fluxos-de-conversão). Vieram só os slides de resultado: **sem volume absoluto de visitantes e de MQL**, não dá para recalcular a significância |
| I4 | Acesso a ferramenta de comportamento (Hotjar, Clarity ou similar), se disponível | 🟡 | **Existe: Mouseflow**, projeto `b837e449-83ee-457f-9ef5-8f976953f2bc`, gravando sessão em todas as páginas web (Master, tag 27). Deixa de ser "pode não existir" e vira pedido de acesso concreto |

## 🔴 J. Pré-Vendas, Qualificação e Sales Engagement · PRIORITÁRIO
*Alimenta o diagnóstico (ix). Bloco mais informativo para as travas de fundo de funil.*

| # | Item | Status |
|---|---|---|
| J1 | Acesso de leitura ao CRM comercial | ⚪ |
| J2 | Critérios atuais de qualificação (scoring, SLAs entre Marketing e Vendas) | ⚪ |
| J3 | Playbooks e cadências de prospecção/atendimento (ferramenta de engagement, se houver) | ⚪ |
| J4 | Amostra de gravações de calls de qualificação (**10 a 15 ligações recentes**) | ⚪ |
| J5 | Taxas de conversão e tempos médios por etapa de pré-vendas | ⚪ |

---

## Como usar este checklist

1. **Atualize o status a cada recebimento.** Este arquivo é a fonte de verdade da fase Identificar.
2. **Item inexistente não é falha do cliente, é dado.** Marque 🔴 e registre no diagnóstico da trava correspondente como evidência de maturidade.
3. **Bloco A é pré-requisito do Forecast.** Sem A1–A3, a matemática do sistema não valida.
4. **Cobrar apenas o que ainda falta**, por bloco, no canal oficial do projeto.
