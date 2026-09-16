# Originais recebidos do cliente

Material bruto que veio do **data room do Grupo OLX** (Google Drive). Nada aqui é produzido pela V4:
é insumo, e o que a V4 escreve sobre ele vive em `02-diagnostico/`.

> ⚠️ **Confidencial.** Cobre o aviso das comunicações da OLX e a cláusula 5.3 do contrato. Não sai
> deste repositório privado, não vai para serviço externo, não entra em material que circule fora do
> projeto sem autorização escrita.

## Procedência

| Item | Detalhe |
|---|---|
| Origem | Data room do Grupo OLX, Google Drive |
| Baixado em | 24/08/2026 |
| Conta usada | `rafael.corazza-ext@olxbr.com`, a conta de domínio OLX liberada no mesmo dia |
| Lote | `drive-download-20260824T172625Z-1-003` |
| Volume | 9 arquivos, 457 MB no original (14 MB versionados, ver abaixo) |

> Contagem do lote de 24/08. O repositório tem hoje **93 arquivos versionados** nesta pasta: o lote,
> mais o bloco H (63 exports de GTM de 01 e 11/09) e o bloco A (captura de tela de 28/08, a série de
> receita recebida por e-mail na mesma data, e as 16 capturas dos dashboards de aquisição de 16/09).
> A procedência de cada um está na seção do seu bloco.
>
> *A contagem anterior deste parágrafo dizia 22 e estava defasada desde o commit dos exports de GTM.*

> Nem tudo aqui veio desse lote. Do **bloco A**, a jornada foi apresentada em reunião e capturada
> da tela, a série de receita chegou por e-mail e os dashboards de aquisição vieram em captura de
> tela do Looker: nenhum dos três saiu do Drive.

Este é o **primeiro lote** que efetivamente abriu com a conta corporativa nova. Ele confirma que o
data room está acessível: o item ficou aberto em `dados/acessos.json` até aqui e agora está fechado.

## Como está organizado

Uma pasta por bloco do [checklist de dados](../../02-diagnostico/checklist-dados-e-acessos.md), com
a mesma letra que o Grupo OLX usa no Drive. Os nomes foram passados para minúsculas sem acento e sem
espaço, porque acento em nome de arquivo quebra entre macOS e Linux dentro do git. O caminho original
de cada arquivo está registrado nas tabelas abaixo, então nada se perde.

```
assets/originais/
├── A-visao-de-negocio-e-fluxo-de-receita/  bloco A · série de receita (A1) + jornada (A2)
│   └── dashboards-aquisicao-pro/    16 capturas do Looker · offline/ e online/ · A2, A3 e B3
├── E-criativos-ads-e-mensagens/     bloco E · alimenta o diagnóstico (iv)
├── H-rastreamento-gtm/              bloco H · alimenta a auditoria (vii) · uma subpasta por conta
├── I-paginas-de-captura/            bloco I · alimenta o diagnóstico (viii)
└── _masters/                        vídeos originais · FORA do git
```

### Proxy no git, master fora

Os 8 vídeos vieram como **masters de finalização**: clipes de 10 segundos exportados a 30–51 Mbps,
455 MB no total. Isso não cabe num repositório de documentação que pesa menos de 1 MB, e todo mundo
que clonasse pagaria esse peso para sempre.

Então o que está versionado nos caminhos acima é um **proxy H.264 CRF 23**, 14 MB no total, que é
mais que suficiente para avaliar criativo, mensagem, ritmo e legibilidade de CTA. O master fica em
`_masters/`, bloqueado pelo `.gitignore`, na máquina de quem baixou, e continua no data room da OLX,
que é a fonte canônica. O SHA-256 de cada master está na tabela de integridade no fim deste arquivo,
então dá para provar que o original é o mesmo quando alguém for buscá-lo.

**Se precisar do master** (remontagem, análise quadro a quadro, entrega para produção): baixe do data
room ou peça a quem tem `_masters/` local. Não recomprima a partir do proxy.

---

## Bloco A · Visão de negócio e fluxo de receita

Três itens, de procedências diferentes. Os dois primeiros se completam sem fechar o A2: um dá as
**taxas** do fluxo sem volume, o outro dá o **volume** de receita sem taxas. O terceiro, que chegou
em 16/09, é o que traz volume **e** taxa por etapa, em série mensal.

### A1 · Série de receita 2025–2026

**Item:** evolução da receita mensal, aberta por unidade de negócio, segmento e produto.
**Cobre:** o item **A1** do checklist, *quase inteiro*: traz 20 meses (jan/2025 a jul/2026) contra
os 24 pedidos, e a abertura por linha de negócio que o item exige. Não cobre A2 nem A3.

| Arquivo | O que é | Origem |
|---|---|---|
| `A-visao-de-negocio-e-fluxo-de-receita/evolucao-receita-2025-2026.xlsx` | Pasta original, aba única `Evol_Receita 2025_2026`, 39 linhas × 24 meses | Enviada pelo Grupo OLX na thread de e-mail **"Onboarding V4 e Grupo OLX"**, em **28/08/2026** |
| `A-visao-de-negocio-e-fluxo-de-receita/evolucao-receita-2025-2026.csv` | Export CSV da mesma aba, UTF-8, o que efetivamente se lê por script | Export da pasta acima |

O `.xlsx` e o `.csv` carregam o mesmo conteúdo: a aba `sheet1.xml` das duas cópias baixadas
(28/08 e 08/09) é byte a byte idêntica, o hash difere só por metadado de download.

**O que a série é, e o que ela não é.** É receita **bruta faturada**, não truput: não há coluna de
custo, imposto ou margem, então ela não converte sozinha em métrica-mãe do método. As colunas de
ago/26 em diante estão zeradas, o último mês fechado é **jul/2026**. A leitura da V4, com o que a
série fecha e os três pontos que ela abre para o cliente explicar, está em
[`02-diagnostico/serie-de-receita-2025-2026.md`](../../02-diagnostico/serie-de-receita-2025-2026.md).

> A série **valida contra ela mesma**: a soma das quatro unidades bate com a linha TOTAL nos 19
> meses com dado, com divergência máxima de **R$ 51 sobre R$ 94,9 milhões** (abr/25), que é
> arredondamento ao real na exibição, não inconsistência. Isso torna o arquivo confiável como
> denominador, e é a primeira vez no projeto que existe um denominador auditável.

### A2 · Jornada do cliente profissional

**Item:** jornada do cliente profissional, o mapa em 6 etapas que o Grupo OLX apresentou.
**Cobre:** o item **A2** do checklist, *parcialmente*: dá as etapas e uma taxa por etapa, não dá
volume absoluto nem série de 12–24 meses.

| Arquivo | O que é | Origem |
|---|---|---|
| `A-visao-de-negocio-e-fluxo-de-receita/jornada-do-cliente-profissional.png` | Slide "Jornada do cliente profissional", 1978×1118 | Apresentado pelo Grupo OLX na sessão de jornada de **28/08/2026**, capturado da tela |

![Jornada do cliente profissional](A-visao-de-negocio-e-fluxo-de-receita/jornada-do-cliente-profissional.png)

Este é o primeiro material do cliente que traz **taxa por etapa do fluxo**. A leitura, o que ele
fecha e as sete ambiguidades que ele abre estão em
[`02-diagnostico/jornada-do-cliente-profissional.md`](../../02-diagnostico/jornada-do-cliente-profissional.md).

> Os seis percentuais do slide são **declarados**, não apurados. Não viram dado antes de bater
> contra CRM, faturamento e plataformas.

### A2 + A3 + B3 · Dashboards de aquisição PRO

**Item:** os dois relatórios de Looker Studio que o Grupo OLX usa para acompanhar aquisição, um por
modelo de venda.
**Cobre:** **A2** (funil com volume e taxa, 13 meses, por canal), **A3** (primeiro CAC com numerador
B2B) e **B3** (resultado dos canais de CRM). Não cobre movimento de base, churn nem margem.

| Origem | Detalhe |
|---|---|
| Como chegou | **Capturas de tela**, não link. Enviadas pelo operador ao repositório em **16/09/2026** |
| Prometido em | Sessão de CRM de **10/09**, por Michelle Morais, item 3 da [pendência 32](../../PENDENCIAS.md) |
| Relatório offline | `Aquisição Offline PRO \\ Marketing` · id `38f3663c-700b-4072-905a-8138a0fd94c2` · 11 páginas |
| Relatório online | `Aquisição Online PRO \\ Marketing` · id `f378f073-cbf8-4d92-9e46-27ebd5ea3d1a` · 5 páginas |
| Conta | `datastudio.google.com/u/6`, conta do operador V4 |

| Arquivo | Página | Dimensão | Master | Proxy no git |
|---|---|---|---|---|
| `offline/01-visao-geral-offline-12m.png` | Visão Geral OFFLINE · Autos+Imóveis · 01/09/2025–15/09/2026 | 2968×6294 | 1.7 MB | 0.44 MB |
| `offline/02-visao-geral-offline-set26.png` | Visão Geral OFFLINE · todas as verticais · 01–15/09/2026 | 2968×6294 | 1.6 MB | 0.41 MB |
| `offline/03-mql-detalhamento.png` | MQL Detalhamento · status do lead | 2968×3694 | 1.4 MB | 0.37 MB |
| `offline/04-vendas-detalhamento.png` | Vendas Detalhamento · periodicidade e receita | 2968×3694 | 1.2 MB | 0.30 MB |
| `offline/05-canais-pagos-performance.png` | Canais Pagos Performance · investimento, cliques, MQL, venda | 2968×6694 | 1.6 MB | 0.41 MB |
| `offline/06-direto-seo-outros.png` | Direto / SEO / Outros · não impulsionados | 2968×4694 | 1.4 MB | 0.35 MB |
| `offline/07-whatsapp-crm.png` | WhatsApp CRM | 2968×4694 | 1.4 MB | 0.37 MB |
| `offline/08-email-marketing-crm.png` | E-mail Marketing CRM | 2968×4694 | 1.4 MB | 0.36 MB |
| `offline/09-push-central-crm.png` | Push/Central CRM | 2968×4694 | 1.3 MB | 0.34 MB |
| `offline/10-product-marketing.png` | Product Marketing · banner, post e referral dentro do produto | 2968×4694 | 1.3 MB | 0.34 MB |
| `offline/11-campanha-tematica-desconto.png` | Campanha Temática / Desconto | 2968×8094 | 2.1 MB | 0.55 MB |
| `online/12-visao-geral-online.png` | Visão Geral ONLINE · ZAP/VR · 01–13/09/2026 | 3336×5594 | 1.4 MB | 0.38 MB |
| `online/13-canais-pagos-performance.png` | Canais Pagos Performance · online | 2968×6694 | 1.2 MB | 0.30 MB |
| `online/14-canalpro-product-marketing.png` | CanalPro Product Marketing | 2968×4694 | 0.9 MB | 0.25 MB |
| `online/15-whatsapp-crm.png` | WhatsApp CRM · online | 2968×4694 | 0.7 MB | 0.18 MB |
| `online/16-email-marketing-crm.png` | E-mail Marketing CRM · online | 2968×4694 | 1.0 MB | 0.28 MB |
| **Total** | | | **21,8 MB** | **5,6 MB** |

**Proxy no git, master fora**, pela mesma regra dos vídeos do bloco E. O que está versionado é um
**PNG de paleta indexada em 256 cores**, na resolução original: para captura de interface, que é
cor chapada e texto, isso é visualmente indistinguível do original e pesa um quarto. O master PNG de
24 bits fica em `_masters/A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/`, bloqueado
pelo `.gitignore`, e o SHA-256 de cada um está na tabela de integridade no fim deste arquivo.

> **Uma página veio duplicada.** O arquivo da Visão Geral ONLINE foi baixado duas vezes, com hash
> idêntico. Está versionado uma vez só. Por isso são 16 arquivos e 17 downloads.

A leitura da V4, com o funil de 13 meses, o CAC de mídia, as três reconciliações e as quatro
pendências que isto abriu, está em
[`02-diagnostico/dashboards-aquisicao-pro.md`](../../02-diagnostico/dashboards-aquisicao-pro.md).

> ⚠️ **Print não é acesso.** Não filtra, não exporta, não atualiza, e dois rótulos de MQL chegaram
> cobertos pelo próprio render do gráfico, resolvidos por reconciliação aritmética e marcados `[E]`.
> O pedido do **link** continua aberto na pendência 32.

## Bloco E · Criativos, anúncios e mensagens

**Campanha:** Mês do Corretor 2026, peças de consideração, praça São Paulo, unidade RE (imóveis).
**Cobre:** item **E1** do checklist, *parcialmente*. São 8 peças de uma campanha, não a biblioteca
de 6 a 12 meses que foi pedida.

| Arquivo | Formato | Duração | Master | Proxy no git | Bitrate do master |
|---|---|---|---|---|---|
| `v1/1200x628-com-cta.mp4` | 1200x628 | 10s | 38 MB | 1.08 MB | 30.5 Mbps |
| `v2/1080x1080-com-cta.mp4` | 1080x1080 | 10s | 60 MB | 1.54 MB | 47.6 Mbps |
| `v2/1080x1920-com-cta.mp4` | 1080x1920 | 10s | 64 MB | 1.79 MB | 51.4 Mbps |
| `v2/1080x1920-sem-cta.mp4` | 1080x1920 | 10s | 64 MB | 1.78 MB | 51.4 Mbps |
| `v3/1080x1080-com-cta.mp4` | 1080x1080 | 10s | 58 MB | 1.48 MB | 46.8 Mbps |
| `v3/1080x1920-com-cta.mp4` | 1080x1920 | 10s | 64 MB | 1.74 MB | 51.0 Mbps |
| `v3/1080x1920-sem-cta.mp4` | 1080x1920 | 10s | 63 MB | 1.72 MB | 50.8 Mbps |
| `v3/1200x628-com-cta.mp4` | 1200x628 | 10s | 43 MB | 1.09 MB | 34.6 Mbps |
| **Total** | | | **455 MB** | **14 MB** | |

![As três variantes, quadro final](E-criativos-ads-e-mensagens/contato-mes-do-corretor-2026.jpg)

*Quadro final de V1 (1200x628), V2 e V3 (1080x1920), extraído dos próprios arquivos.*

### O que a campanha comunica

Comum às três variantes: oferta **"Até 40% OFF nos planos profissionais"**, CTA **"Saiba mais"**,
prova **"+1,8 milhões de leads/mês em SP"** e assinatura conjunta grupo OLX · Zap · VivaReal · OLX.

O que muda é o ângulo da mensagem, e são três ângulos distintos:

| Variante | Pessoa em cena | Promessa |
|---|---|---|
| V1 | corretora, ambiente de escritório | "Quem é especialista está **onde os negócios acontecem**" |
| V2 | corretor, ambiente de escritório | "Quem entende do mercado **faz negócios aqui**" |
| V3 | **Mônica Poplawski**, nomeada em tela | "**Leads qualificados** pra você focar em fechar uma venda ou locação" |

V1 e V2 são a mesma ideia (pertencimento e status) com elenco diferente. V3 muda de eixo: sai de
status e vai para benefício funcional, com prova social de uma pessoa nomeada. Para o diagnóstico
(iv) isso importa, porque é a única das três que promete **qualificação de lead**, que é exatamente
o terreno das travas de Qualificação e Compromisso.

### Quatro achados para o diagnóstico (iv)

1. **A oferta chega no segundo 5, o CTA no segundo 7, em peça de 10 segundos.** Contei quadro a
   quadro: 0s ambiente vazio, 1s marca, 3s título, 4s subtítulo, 5s a oferta de 40% OFF, 7s o botão
   "Saiba mais". Em feed e em Reels, a maior parte da audiência já saiu antes do segundo 5. A peça
   guarda o argumento comercial para o final, e o final quase ninguém vê.
2. **São masters, não peças de veiculação.** 10 segundos a 30–51 Mbps é exportação de finalização.
   O Meta reencoda para algo na casa de 8 a 12 Mbps de qualquer forma. Não é problema de
   performance, mas indica que o que circula entre os times é o arquivo pesado, e não um pacote de
   entrega organizado por formato.
3. **Nenhuma das 8 tem faixa de áudio.** Para consideração em feed é escolha defensável. Para 9x16
   em Reels e Stories, onde o som está ligado na maioria das sessões, é lacuna a checar: a peça
   compete no som com quem tem som.
4. **A matriz de formatos está incompleta.** V1 só existe em 1200x628. V2 tem 1x1 e 9x16. Só a V3
   tem os três. Se as três foram para o ar juntas, elas não disputaram os mesmos posicionamentos, e
   qualquer leitura de "qual criativo performou melhor" está contaminada por isso, não por
   criatividade.

> 💡 Isto aqui é **B2B de verdade**: corretor, plano profissional, leads. Vale contrapor à
> [PENDENCIA 12](../../PENDENCIAS.md), que registra que as campanhas visíveis no Google Ads parecem
> ser B2C. Ou o B2B vive em outra conta, ou vive só no Meta. É pergunta para o kick-off.

**O que ainda falta no bloco E:** E2 (brandbook, diretrizes de marca, messaging house) e E3
(briefings das campanhas). Sem E3 não dá para saber se V1, V2 e V3 eram um teste de mensagem
deliberado ou três entregas soltas da agência, e essa distinção muda a leitura inteira.

---

## Bloco I · Páginas de captura e fluxos de conversão

**Cobre:** item **I3** do checklist, histórico de testes A/B.

| Arquivo | Tipo | Peso |
|---|---|---|
| `teste-ab-imoveis/2026-03-teste-ab-lp-anuncie-zap.pptx` | PowerPoint, 8 slides | 2.3 MB |

**Teste A/B: LP Anuncie ZAP**, de 17/03 a 23/03. Resultado declarado no material:

| Campo | Valor declarado |
|---|---|
| Vencedora | Variante A |
| Ganho | 54,3% em eficiência de conversão por visitante único |
| Confiança | 99,93%, p-valor 0,0007 |
| Eficiência em MQL | Variante A 1,5x a Variante B |
| Engajamento | 1,58 sessões por visitante na A contra 1,25 na B |
| Objetivo da LP | Gerar MQL para o comercial vender plano profissional a novo anunciante |
| Mudança testada | Formulário reposicionado, texto hero em mais destaque |
| Recomendação do material | Pausar a B e mandar 100% do tráfego para a A |

> ⚠️ **Os números acima são declaração do cliente, não achado da V4.** Vão para o diagnóstico como
> insumo e precisam de verificação antes de sustentar qualquer decisão: o material não traz volume
> absoluto de visitantes nem de MQL, e sem denominador não dá para recalcular a significância. Um
> teste de 7 dias também atravessa uma única semana, o que não isola efeito de dia da semana.
> Cobrar os dados brutos é item para o kick-off.

**O que ainda falta no bloco I:** I1 (URLs das LPs e fluxos ativos), I2 (taxa de conversão por
página e etapa) e I4 (ferramenta de comportamento).

---

## Bloco H · Rastreamento (GTM)

**Cobre:** item **H1** do checklist, contêineres do Google Tag Manager. É o insumo da
[auditoria (vii)](../../02-diagnostico/auditoria-vii-rastreamento.md).

**Este bloco não veio do data room.** São exports da interface do GTM, feitos pelo operador com o
acesso concedido a `gina@v4company.com` (contêiner → Administração → Exportar contêiner), em três
levas: 01/09, e duas em 11/09. O caminho de origem, portanto, é a própria interface, não uma pasta
do Drive. O roteiro de coleta está em
[`guia-export-gtm.md`](../../02-diagnostico/guia-export-gtm.md).

### Uma subpasta por conta

São quatro contas de GTM sob a organização **OLX / BOM NEGOCIO ATIVIDADES DE INTERNET LTDA**, e o
nome do arquivo não diz de qual delas ele veio. Por isso o bloco é dividido:

```
H-rastreamento-gtm/
├── conta-94905-br-olx-com-br/                28 arquivos · 26 contêineres
├── conta-2971905372-zapimoveis/              19 arquivos · 19 contêineres
├── conta-4412254379-vivareal/                11 arquivos · 11 contêineres
├── conta-6326134112-checkout-unificado-pro/   4 arquivos ·  4 contêineres
└── telas/                                     capturas da interface
```

O ID da conta entra no nome da pasta porque é assim que as contas são citadas na auditoria e nas
pendências. **60 contêineres no total**, em 62 arquivos: a diferença são dois
retratos do mesmo rascunho, exportados em datas diferentes, guardados lado a lado de propósito
porque mostram que os rascunhos foram editados durante a auditoria.

> ⚠️ **Todos os 62 são export de _workspace_, nenhum é de versão publicada.** Os nomes trazem
> `workspace392`, `workspace131` e assim por diante, e o campo `containerVersionId` vem `0` em todos.
> Um workspace pode conter rascunho que não está no ar. Serve para diagnosticar, e foi assim que a
> auditoria (vii) foi levantada. Antes de levar um achado a comitê como "isto roda em produção",
> confirmar contra a versão publicada. É a única pendência aberta da coleta deste bloco.

**Conferência:** `python3 .claude/scripts/check_gtm_exports.py` lê a pasta, diz de que conta e de que
contêiner é cada arquivo, se é rascunho ou versão publicada, e o que falta. Com `--importar` ele traz
exports novos de `~/Downloads` ou de outra pasta, sem duplicar o que já está aqui.

### `conta-94905-br-olx-com-br/` · BR - www.olx.com.br (`94905`)

26 contêineres, em 28 arquivos.

| ID | Contêiner | Tags | Pausadas | Gatilhos | Variáveis |
|---|---|---:|---:|---:|---:|
| `GTM-WGKTT96` | [OLD] OLX - Ajuda | 209 | 59 | 207 | 218 |
| `GTM-TNX8FDS` | OLX - Buyer Journey | 124 | 37 | 71 | 186 |
| `GTM-TNX8FDS` | OLX - Buyer Journey | 124 | 37 | 71 | 187 |
| `GTM-5WWRGTQ` | OLX - VAS | 48 | 18 | 43 | 52 |
| `GTM-KP8QMDH` | OLX - Unbounce \| LP | 40 | 0 | 39 | 50 |
| `GTM-KGFGVFC` | OLX - Planos Profissionais & PAYG | 29 | 8 | 29 | 98 |
| `GTM-NPQMK7P` | OLX - Projetos Especiais de Autos \| LP | 29 | 0 | 14 | 74 |
| `GTM-MXQKDG3` | OLX - Seller Journey | 28 | 14 | 19 | 53 |
| `GTM-MJX9PG4` | OLX - Conecta Autos | 25 | 1 | 17 | 33 |
| `GTM-KCCPDZV` | OLX - Dicas | 22 | 0 | 27 | 34 |
| `GTM-PZ83VMV` | OLX - LPs | 20 | 0 | 15 | 29 |
| `GTM-KN3K8B8` | OLX - Hub Segurança | 15 | 0 | 9 | 25 |
| `GTM-MVQWQJFB` | OLX - RD Station \| LP | 15 | 1 | 16 | 29 |
| `GTM-546N2JV` | OLX - Container Master | 13 | 5 | 21 | 20 |
| `GTM-546N2JV` | OLX - Container Master | 13 | 5 | 21 | 20 |
| `GTM-PP7ZQJD` | OLX - Encontro Certo \| LP | 10 | 0 | 11 | 11 |
| `GTM-KGMSNP6` | OLX - Site Institucional | 6 | 0 | 5 | 19 |
| `GTM-TW9TWPT5` | OLX - Login | 5 | 1 | 2 | 8 |
| `GTM-M4TL57GX` | OLX - Checkout | 4 | 0 | 2 | 27 |
| `GTM-TQHV6TD` | OLX - Testes de SDK | 4 | 0 | 1 | 6 |
| `GTM-PWP7Z4C` | OLX - Wallet | 3 | 0 | 1 | 19 |
| `GTM-TVLDBBK2` | OLX - Chatbot | 3 | 0 | 1 | 6 |
| `GTM-5VJJT94P` | OLX - Central de Ajuda | 2 | 0 | 0 | 1 |
| `GTM-PQTNMNM3` | OLX - Teste Adopt | 2 | 0 | 4 | 1 |
| `GTM-TW8N3LN` | OLX - Chat | 2 | 1 | 2 | 17 |
| `GTM-52W35LS` | [New] Android Tracking | 1 | 0 | 1 | 25 |
| `GTM-P5958DMR` | OLX - Favoritos | 1 | 0 | 0 | 16 |
| `GTM-T8ZBL8Z` | [New] iOS Tracking | 0 | 0 | 1 | 0 |
| | **total** | **797** | **187** | **650** | **1264** |
### `conta-2971905372-zapimoveis/` · ZapImóveis (`2971905372`)

19 contêineres, em 19 arquivos.

| ID | Contêiner | Tags | Pausadas | Gatilhos | Variáveis |
|---|---|---:|---:|---:|---:|
| `GTM-MKTZ2ZP` | 3. ZapImóveis - Container CLICKSTREAM | 129 | 0 | 199 | 821 |
| `GTM-5X2LZWR` | 2. ZapImóveis - Container PORTAL ZAP | 127 | 17 | 107 | 297 |
| `GTM-N6JJ79TH` | 9. ZapImóveis - Container PORTAL ZAP - Ambiente de QA | 84 | 5 | 68 | 219 |
| `GTM-MVM68B5` | 4. ZapImóveis - Container LANDING PAGES | 62 | 4 | 50 | 59 |
| `GTM-PZ733B5` | 5. ZapImóveis - Container ANUNCIE | 48 | 9 | 51 | 122 |
| `GTM-M6NDNP4K` | 10. ZapImóveis - Container ANUNCIE - Ambinete de QA | 47 | 17 | 60 | 171 |
| `GTM-5PNSC98` | Guia de Bairros | 25 | 0 | 24 | 58 |
| `GTM-PBZ477K` | 7. ZapImóveis - Container BLOG | 21 | 1 | 20 | 194 |
| `GTM-N87GJJD` | Rede Zap | 13 | 0 | 17 | 14 |
| `GTM-PQDRHQM` | www.datazap.com.br | 12 | 0 | 8 | 8 |
| `GTM-W662TWW` | 1. ZapImóveis - Container MASTER | 10 | 1 | 17 | 9 |
| `GTM-MFKXMNK` | LP - Zapfin | 9 | 0 | 11 | 6 |
| `GTM-M23NB5R` | meuzap.zapimoveis.com.br | 7 | 0 | 6 | 54 |
| `GTM-NBKDVZ6W` | 8. Conecta Imobi | 5 | 0 | 2 | 3 |
| `GTM-MQSQ9JW` | 6. ZapImóveis - Container DATAZAP/GEOIMOVEL | 4 | 0 | 2 | 171 |
| `GTM-WHJZKXFC` | 11. Zapimovéis - Container Anapro | 4 | 1 | 2 | 0 |
| `GTM-TMXMHKBJ` | 12. ZapImóveis - Container Checkout | 3 | 0 | 3 | 26 |
| `GTM-T8PDZ2MS` | 2. ZapImóveis - Container PORTAL ZAP [Lead Only] | 1 | 0 | 2 | 2 |
| `GTM-NWPXB4X` | ZapImóveis - Container BLOG (WIP) | 0 | 0 | 0 | 0 |
| | **total** | **611** | **55** | **649** | **2234** |
### `conta-4412254379-vivareal/` · VivaReal (`4412254379`)

11 contêineres, em 11 arquivos.

| ID | Contêiner | Tags | Pausadas | Gatilhos | Variáveis |
|---|---|---:|---:|---:|---:|
| `GTM-TRGML4R` | 3. VivaReal - Container CLICKSTREAM | 99 | 0 | 105 | 444 |
| `GTM-NP4HWRN` | 2. VivaReal - Container Portal VR | 98 | 20 | 56 | 211 |
| `GTM-PNNJ4D3V` | 6. VivaReal - Container Portal VR - Ambiente QA | 71 | 9 | 75 | 188 |
| `GTM-WBBDN4W` | Conectaimobi | 31 | 0 | 25 | 12 |
| `GTM-5RPFK7Z` | 4. VivaReal - Container BLOG | 16 | 1 | 19 | 160 |
| `GTM-T43B5LRJ` | 5. VivaReal - Container ANUNCIE | 14 | 1 | 14 | 60 |
| `GTM-TWSJ9VM` | 1. VivaReal - Container MASTER | 7 | 1 | 12 | 9 |
| `GTM-P4VTWPM2` | 7. VivaReal - Container ANUNCIE - Ambiente de QA | 4 | 0 | 5 | 26 |
| `GTM-TXJVLXSJ` | 8. VivaReal - Container Checkout | 3 | 0 | 3 | 27 |
| `GTM-5DV89XS` | VivaReal - Container BLOG (WIP) | 0 | 0 | 0 | 0 |
| `GTM-TCG3ML4` | Sympla - Conectalmobi - Iframe Checkout | 0 | 0 | 0 | 0 |
| | **total** | **343** | **32** | **314** | **1137** |
### `conta-6326134112-checkout-unificado-pro/` · Checkout Unificado - PRO (`6326134112`)

4 contêineres, em 4 arquivos.

| ID | Contêiner | Tags | Pausadas | Gatilhos | Variáveis |
|---|---|---:|---:|---:|---:|
| `GTM-K4WBMGQV` | Checkout Unificado - OLX | 9 | 0 | 7 | 32 |
| `GTM-NKSGWD6H` | Checkout Unificado - Zap Imóveis | 9 | 0 | 4 | 20 |
| `GTM-NRVS3M3D` | Checkout Unificado - Viva Real | 6 | 0 | 3 | 19 |
| `GTM-NGG9336B` | Checkout Unificado - Master | 4 | 1 | 7 | 5 |
| | **total** | **28** | **1** | **21** | **76** |

**Totais do bloco:** 60 contêineres, **1779 tags** (275
pausadas), 1634 gatilhos e 4711 variáveis.
---

## Integridade

SHA-256 de cada arquivo no momento em que entrou no repositório, e o caminho exato de onde veio no
Drive. Serve para provar que o arquivo não mudou e para reencontrar a origem.

| Arquivo | SHA-256 | Caminho no data room |
|---|---|---|
| `E-criativos-ads-e-mensagens/mes-do-corretor-2026-sp-consideracao/v1/1200x628-com-cta.mp4` | `af934723a2c22b69…` | `E. Criativos Ads & Mensagens/Peças/RE/Mês do Corretor 2026/Mês do Corretor _ Peças consideração SP/Motion/V1/1200x628 com CTA.mp4` |
| `E-criativos-ads-e-mensagens/mes-do-corretor-2026-sp-consideracao/v2/1080x1080-com-cta.mp4` | `4450a3335d1cbccb…` | `E. Criativos Ads & Mensagens/Peças/RE/Mês do Corretor 2026/Mês do Corretor _ Peças consideração SP/Motion/V2/1080x1080 com CTA.mp4` |
| `E-criativos-ads-e-mensagens/mes-do-corretor-2026-sp-consideracao/v2/1080x1920-com-cta.mp4` | `3dbded8945745610…` | `E. Criativos Ads & Mensagens/Peças/RE/Mês do Corretor 2026/Mês do Corretor _ Peças consideração SP/Motion/V2/1080x1920 com CTA.mp4` |
| `E-criativos-ads-e-mensagens/mes-do-corretor-2026-sp-consideracao/v2/1080x1920-sem-cta.mp4` | `92c60df7c21afa76…` | `E. Criativos Ads & Mensagens/Peças/RE/Mês do Corretor 2026/Mês do Corretor _ Peças consideração SP/Motion/V2/1080x1920.mp4` |
| `E-criativos-ads-e-mensagens/mes-do-corretor-2026-sp-consideracao/v3/1080x1080-com-cta.mp4` | `c77ac9761976a67b…` | `E. Criativos Ads & Mensagens/Peças/RE/Mês do Corretor 2026/Mês do Corretor _ Peças consideração SP/Motion/V3/1080x1080 com CTA.mp4` |
| `E-criativos-ads-e-mensagens/mes-do-corretor-2026-sp-consideracao/v3/1080x1920-com-cta.mp4` | `f21279362e6e4860…` | `E. Criativos Ads & Mensagens/Peças/RE/Mês do Corretor 2026/Mês do Corretor _ Peças consideração SP/Motion/V3/1080x1920 com CTA.mp4` |
| `E-criativos-ads-e-mensagens/mes-do-corretor-2026-sp-consideracao/v3/1080x1920-sem-cta.mp4` | `02bbcfef42672a26…` | `E. Criativos Ads & Mensagens/Peças/RE/Mês do Corretor 2026/Mês do Corretor _ Peças consideração SP/Motion/V3/1080x1920.mp4` |
| `E-criativos-ads-e-mensagens/mes-do-corretor-2026-sp-consideracao/v3/1200x628-com-cta.mp4` | `2284356e512da371…` | `E. Criativos Ads & Mensagens/Peças/RE/Mês do Corretor 2026/Mês do Corretor _ Peças consideração SP/Motion/V3/1200x628 com CTA.mp4` |
| `A-visao-de-negocio-e-fluxo-de-receita/jornada-do-cliente-profissional.png` | `fb8d738564bb2b10…` | não veio do data room, captura de tela da apresentação de 28/08 |
| `A-visao-de-negocio-e-fluxo-de-receita/evolucao-receita-2025-2026.xlsx` | `b568d3ee65ea0786…` | não veio do data room, anexo da thread de e-mail "Onboarding V4 e Grupo OLX", 28/08 |
| `A-visao-de-negocio-e-fluxo-de-receita/evolucao-receita-2025-2026.csv` | `4b560e7ee40b7de3…` | export CSV da pasta acima, mesma aba |
| `I-paginas-de-captura/teste-ab-imoveis/2026-03-teste-ab-lp-anuncie-zap.pptx` | `4f7c85fe6821206d…` | `I. Páginas de Captura e Fluxos de Conversão/Testes a-b imóveis/Copy of A_B Test Results - Landing Page_.pptx` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-5pnsc98_workspace24.json` | `97c6b099579a88b9…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-5x2lzwr_workspace306.json` | `7c6c5399d18a7a0e…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-m23nb5r_workspace59.json` | `3977457db55f5c7e…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-m6ndnp4k_workspace4.json` | `eca3c9b561adb547…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-mfkxmnk_workspace3.json` | `28bc972d99583a0e…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-mktz2zp_workspace215.json` | `0620ffa10a48d76f…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-mqsq9jw_workspace8.json` | `1b99d7682d34714f…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-mvm68b5_workspace53.json` | `a63abcfee0c524e5…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-n6jj79th_workspace11.json` | `5d78ba710e48abeb…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-n87gjjd_workspace3.json` | `47b4e02fb4df4515…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-nbkdvz6w_workspace10.json` | `c80bb344bdfa6970…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-nwpxb4x_workspace2.json` | `31e9cf6bf42881a5…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-pbz477k_workspace18.json` | `8c8ebb37b113a35b…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-pqdrhqm_workspace3.json` | `413a36cbbcea6b1b…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-pz733b5_workspace92.json` | `b7773df8ae3b250c…` | não veio do data room, export da interface do GTM em 01/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-t8pdz2ms_workspace3.json` | `d1fea315a9162ac6…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-tmxmhkbj_workspace3.json` | `f69a71f69f88d40c…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-w662tww_workspace91.json` | `c219862ebdace0a3…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-2971905372-zapimoveis/gtm-whjzkxfc_workspace24.json` | `c74172ecfbbf25d6…` | não veio do data room, export da interface do GTM em 11/09, conta `2971905372` |
| `H-rastreamento-gtm/conta-4412254379-vivareal/gtm-5dv89xs_workspace2.json` | `510553955fecff0e…` | não veio do data room, export da interface do GTM em 11/09, conta `4412254379` |
| `H-rastreamento-gtm/conta-4412254379-vivareal/gtm-5rpfk7z_workspace13.json` | `8429de62ee230af3…` | não veio do data room, export da interface do GTM em 11/09, conta `4412254379` |
| `H-rastreamento-gtm/conta-4412254379-vivareal/gtm-np4hwrn_workspace192.json` | `fb3a7f12cb965673…` | não veio do data room, export da interface do GTM em 11/09, conta `4412254379` |
| `H-rastreamento-gtm/conta-4412254379-vivareal/gtm-p4vtwpm2_workspace4.json` | `cb01e0b333055be9…` | não veio do data room, export da interface do GTM em 11/09, conta `4412254379` |
| `H-rastreamento-gtm/conta-4412254379-vivareal/gtm-pnnj4d3v_workspace4.json` | `a33da2f30f091ceb…` | não veio do data room, export da interface do GTM em 11/09, conta `4412254379` |
| `H-rastreamento-gtm/conta-4412254379-vivareal/gtm-t43b5lrj_workspace19.json` | `b1f357e212532b4e…` | não veio do data room, export da interface do GTM em 11/09, conta `4412254379` |
| `H-rastreamento-gtm/conta-4412254379-vivareal/gtm-tcg3ml4_workspace2.json` | `99450a2a28d291db…` | não veio do data room, export da interface do GTM em 11/09, conta `4412254379` |
| `H-rastreamento-gtm/conta-4412254379-vivareal/gtm-trgml4r_workspace79.json` | `2475caa50a347bd4…` | não veio do data room, export da interface do GTM em 11/09, conta `4412254379` |
| `H-rastreamento-gtm/conta-4412254379-vivareal/gtm-twsj9vm_workspace55.json` | `87d4a9f5441a40b7…` | não veio do data room, export da interface do GTM em 11/09, conta `4412254379` |
| `H-rastreamento-gtm/conta-4412254379-vivareal/gtm-txjvlxsj_workspace3.json` | `fc9b9f1e285cc975…` | não veio do data room, export da interface do GTM em 11/09, conta `4412254379` |
| `H-rastreamento-gtm/conta-4412254379-vivareal/gtm-wbbdn4w_workspace39.json` | `6116e4c27902f9a7…` | não veio do data room, export da interface do GTM em 11/09, conta `4412254379` |
| `H-rastreamento-gtm/conta-6326134112-checkout-unificado-pro/gtm-k4wbmgqv_workspace13.json` | `3a44360a38fdda59…` | não veio do data room, export da interface do GTM em 11/09, conta `6326134112` |
| `H-rastreamento-gtm/conta-6326134112-checkout-unificado-pro/gtm-ngg9336b_workspace6.json` | `0aabce78a3b837e1…` | não veio do data room, export da interface do GTM em 11/09, conta `6326134112` |
| `H-rastreamento-gtm/conta-6326134112-checkout-unificado-pro/gtm-nksgwd6h_workspace5.json` | `15392671936595cb…` | não veio do data room, export da interface do GTM em 11/09, conta `6326134112` |
| `H-rastreamento-gtm/conta-6326134112-checkout-unificado-pro/gtm-nrvs3m3d_workspace4.json` | `81aefb66ccda4aeb…` | não veio do data room, export da interface do GTM em 11/09, conta `6326134112` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-52w35ls_workspace9.json` | `94af8e1a3a8e5ce2…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-546n2jv_workspace206.json` | `68f2a5f8034b5205…` | não veio do data room, export da interface do GTM em 01/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-546n2jv_workspace206_2026-09-11.json` | `037c4038f2f8cf4c…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-5vjjt94p_workspace3.json` | `7de4dd7049552ac2…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-5wwrgtq_workspace61.json` | `c2bcb2cf61805a1d…` | não veio do data room, export da interface do GTM em 01/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-kccpdzv_workspace22.json` | `7a9647b95bcc5cea…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-kgfgvfc_workspace131.json` | `38b61356d05fa73a…` | não veio do data room, export da interface do GTM em 01/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-kgmsnp6_workspace46.json` | `bc0980d8fc6f4127…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-kn3k8b8_workspace14.json` | `ce305dbb1c47b405…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-kp8qmdh_workspace69.json` | `07eb8af73a1fb478…` | não veio do data room, export da interface do GTM em 01/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-m4tl57gx_workspace3.json` | `a0ff93b7f234449a…` | não veio do data room, export da interface do GTM em 01/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-mjx9pg4_workspace27.json` | `239ed1742bab93c3…` | não veio do data room, export da interface do GTM em 01/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-mvqwqjfb_workspace17.json` | `b39837013df7f1f5…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-mxqkdg3_workspace56.json` | `2bb56df5e77c1051…` | não veio do data room, export da interface do GTM em 01/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-npqmk7p_workspace23.json` | `dbd91c7a860caca9…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-p5958dmr_workspace4.json` | `40129a35be6b96cd…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-pp7zqjd_workspace15.json` | `a79439c215974865…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-pqtnmnm3_workspace4.json` | `da92c96d014dbba3…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-pwp7z4c_workspace11.json` | `5faf33d9342cfb2f…` | não veio do data room, export da interface do GTM em 01/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-pz83vmv_workspace31.json` | `5ba32706cfdba474…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-t8zbl8z_workspace2.json` | `06b7b192065c6d89…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-tnx8fds_workspace392.json` | `b478d7b464815eb5…` | não veio do data room, export da interface do GTM em 01/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-tnx8fds_workspace395.json` | `34051b83a38ada8d…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-tqhv6td_workspace3.json` | `54b039915e83589e…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-tvldbbk2_workspace3.json` | `0040521c63a72bff…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-tw8n3ln_workspace8.json` | `8e92cf159d7acaf2…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-tw9twpt5_workspace3.json` | `dbc3f86e2ed3acd6…` | não veio do data room, export da interface do GTM em 01/09, conta `94905` |
| `H-rastreamento-gtm/conta-94905-br-olx-com-br/gtm-wgktt96_workspace249.json` | `a0e88645f3724bb5…` | não veio do data room, export da interface do GTM em 11/09, conta `94905` |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/offline/01-visao-geral-offline-12m.png` | `f7e10b715cd84d8f…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/offline/02-visao-geral-offline-set26.png` | `366544c904690e60…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/offline/03-mql-detalhamento.png` | `d765703d149ca88a…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/offline/04-vendas-detalhamento.png` | `b4c46bebcc0ba7c3…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/offline/05-canais-pagos-performance.png` | `1b18f1873847f9e3…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/offline/06-direto-seo-outros.png` | `e00b93b6b2808c87…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/offline/07-whatsapp-crm.png` | `96f4fda166f205d7…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/offline/08-email-marketing-crm.png` | `25e47483b82b77f2…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/offline/09-push-central-crm.png` | `7bb6c84bed2636cb…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/offline/10-product-marketing.png` | `3d0cbcf9f5a81fce…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/offline/11-campanha-tematica-desconto.png` | `a1903772dbebda46…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/online/12-visao-geral-online.png` | `52d01aff7bacf3ea…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/online/13-canais-pagos-performance.png` | `c69a2eebc48551ec…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/online/14-canalpro-product-marketing.png` | `97200a950bcffe0e…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/online/15-whatsapp-crm.png` | `87142d9834164bc5…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
| `A-visao-de-negocio-e-fluxo-de-receita/dashboards-aquisicao-pro/online/16-email-marketing-crm.png` | `61e8b3e5c4249db9…` | não veio do data room, captura do Looker do Grupo OLX em 16/09 |
