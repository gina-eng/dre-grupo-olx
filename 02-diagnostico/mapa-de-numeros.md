# Mapa dos Números

**Apurado em 14/09/2026** · 78 indicadores catalogados · **26 têm número hoje**

> **Estado de máquina:** [`dados/outputs/mapa-de-numeros.json`](../dados/outputs/mapa-de-numeros.json),
> gerado por [`.claude/scripts/build_mapa_numeros.py`](../.claude/scripts/build_mapa_numeros.py).
> **Entregável:** `01-cliente/entregaveis/V4 x Grupo OLX - Mapa dos Numeros.docx`.
> **Catálogo:** vive em `portal/assets/metrics-data.js` e aparece na aba Métricas do portal.

Este documento responde três perguntas numa folha só: que números o DR-E precisa ter, quais já
temos, e o que falta para ter o resto.

---

## A leitura

**A maior fila não é de dado que a OLX precisa produzir. É de ferramenta que já foi concedida e
ninguém abriu.**

| Cobertura | Qtd. | O que significa |
|---|---:|---|
| **Medido** | 9 | Dado em mãos, versionado, com fonte rastreável e conferida |
| **Concedido** | 3 | A fonte foi aberta e testada: ela respondeu. Falta extrair, e isso é trabalho da V4 |
| **A conferir** | 23 | Acesso declarado concedido em 10/09 e **nunca aberto na ferramenta** |
| **Parcial** | 14 | Temos parte: série incompleta, ou o recorte errado, como mídia que mistura B2C e B2B |
| **Declarado** | 4 | Existe só como número dito em reunião. Vale como hipótese, não como base de meta |
| **Falta** | 25 | Nem fonte nem dado. Depende de entrega da OLX ou de decisão não tomada |

Por prioridade: **51 P0** (bloqueiam o Comitê 1), 24 P1, 3 P2. E **18 dos P0 estão na faixa "a
conferir"**, ou seja, presos num acesso que talvez já esteja na mão. Vinte deles dependem de uma
fonte só, o CRM comercial.

> O precedente do projeto justifica a desconfiança: duas vezes o acesso chegou e não servia. O GA4
> veio em nível Leitor, que não abre a configuração onde mora a causa, e o Meta veio com "nenhum
> ativo conectado". Enquanto ninguém abrir a ferramenta, "concedido" é declaração, não cobertura.

---

## O que já temos, com número

### Mídia paga, apurado no V4MOS em 14/09

Janela 01/01/2025 a 14/09/2026.

| Indicador | Valor | Ressalva |
|---|---|---|
| Investimento total | **R$ 10,12 mi** | Meta R$ 7,38 mi · Google R$ 2,75 mi |
| Campanhas | 90 no Meta · 23 no Google | 1.079 anúncios com gasto, CTR e CPM por peça |
| Impressões | 1,94 bi | Meta 1,88 bi · Google 56,4 mi |
| Alcance | 1,41 bi | Só o Meta devolve alcance |
| CPC | R$ 0,25 Meta · R$ 0,27 Google | Praticamente iguais, apesar do CPM 12x maior no Google |
| CTR | 1,56% Meta · 18,03% Google | Onze vezes de diferença: as contas contam clique de forma diferente |
| Série mensal | **21 meses contínuos no Meta** · 11 no Google | Faltam nov/2025 a abr/2026 inteiros no Google |

> 🔴 **Nenhuma das duas contas separa B2B de B2C.** Enquanto isso durar, R$ 10,12 mi não são o
> investimento do recorte contratado, e nenhum CAC de mídia tem numerador válido.

### Comportamento, apurado no GA4 em 14/09

Domínios `*.grupoolx.com.br`, mesma janela.

| Indicador | Valor |
|---|---|
| Sessões | **987.566** |
| Distribuição por origem | Direto 52,4% · Referral 36,4% · Orgânico 9,9% · **Pago 0,8%** |
| Sessões orgânicas | 97.369 |
| `ads.grupoolx.com.br` | 780.662 sessões · 87,8% de rejeição · 1,03 página por sessão |
| Engajamento | 12,2% em `ads.` · 52,4% em `imoveis.` · 41,8% em `autos.` |
| Envios de formulário | **1.089** em 21 meses, 0,11% das sessões |

### Receita, série A1 recebida em 28/08

Run-rate do grupo **R$ 103,8 mi/mês**; núcleo de assinatura B2B **R$ 68,0 mi/mês**, 65,5% do grupo.
Um ponto percentual de run-rate em `Classifieds - B&A` vale **R$ 427,8 mil/mês**.

> Receita bruta faturada, declarada pelo cliente. **Não é truput.** Sem P&L por vertical ela não
> converte em margem de contribuição, que é a métrica-mãe do método.

### O primeiro achado do mapa

**O slide de 28/08 declara Pago em 16% da origem do contato. O GA4 mede Pago em 0,8% das sessões.
Vinte vezes de diferença.**

As duas leituras não medem a mesma coisa, origem de contato contra origem de sessão, e parte da
distância é isso. Mas o próprio slide anota que campanha paga para WhatsApp *"entra tudo como
Direto"*, e a auditoria (vii) achou o `purchase` preso ao gatilho de `begin_checkout`. A hipótese
simples é que o pago existe e não está sendo atribuído.

---

## Os sete números que decidem o Comitê 1

Nenhum depende de ferramenta nova. Quatro foram prometidos no kick-off para 09/09, com dono
nomeado, e nenhum chegou.

| # | O número | Para que serve | Dono | Prazo |
|---|---|---|---|---|
| 1 | **Ticket médio de entrada**, por vertical e segmento | Converte contrato novo em receita. Sem ele, N não vira R$ | Matheus Rodrigues + Iuna Scheffler | 09/09, vencido |
| 2 | **Base ativa de anunciantes**, por vertical, mês a mês | É o denominador de churn, de CAC e de LTV ao mesmo tempo | Leonardo Rosa | 09/09, vencido |
| 3 | **Contratos novos por mês**, por canal e vertical | É o N de onde tudo desce, e o denominador que falta ao CAC | Leonardo Rosa + Carolina Dallolio | 09/09, vencido |
| 4 | **P&L por vertical**, com mídia e imposto abertos | Converte receita em truput. A meta do projeto é margem de contribuição do mês 12 sobre a do mês 0 | Matheus Rodrigues | 09/09, vencido |
| 5 | **Churn desambiguado**: de logo ou de receita | Muda o ranking das alavancas. Para ser de receita sobre B&A, exigiria R$ 4,07 mi de contrato novo por mês | Iuna + Carolina | pendência 22 |
| 6 | **Net de receita de Imóveis**, mês a mês | Dimensiona a meta zero. A série A1 mostra B&A crescendo 6,4%, o que não confirma o net negativo declarado | Iuna Scheffler | 10/09, vencido |
| 7 | **Metas 2026 por etapa do fluxo** | É a âncora contra a qual a meta do projeto é comparada | Matheus + Iuna | 09/09, vencido |

---

## A conta que não fecha: unit economics

Os nove indicadores do bloco, e o estado de cada um.

| Indicador | Cobertura | Por que ainda não existe |
|---|---|---|
| CAC blended | 🔴 Falta | Numerador parcial e denominador ausente |
| CAC pago | 🟡 Parcial | A mídia está medida e misturada com B2C; "novos clientes por canal" não existe |
| CAC por segmento | 🔴 Falta | Exige a segmentação que o item A6 nunca entregou |
| LTV | 🔴 Falta | Depende de ticket, permanência e margem. Os três ausentes |
| LTV / CAC | 🔴 Falta | Os dois lados da razão estão ausentes |
| CAC payback | 🔴 Falta | Depende de CAC e de margem |
| **Margem de contribuição por anunciante** | 🔴 Falta | Não há P&L por vertical. Margem perto de 100% é declaração, não medição |
| ROAS por canal | 🔴 Falta | Exige receita atribuída por canal, o que a atribuição atual não sustenta |
| MER | 🟡 Parcial | ~186x `[E]`, com janelas que não batem. Ordem de grandeza, não indicador |

**As três perguntas que este bloco responde:**

1. **Conhecemos a margem de contribuição?** Não. O que existe é a declaração de kick-off: margem
   bruta perto de 100%, sem COGS de produto, mídia e imposto como únicos ofensores, sem abertura
   por linha. Margem bruta não é margem de contribuição, e o P&L que converteria uma na outra não
   chegou.
2. **Conhecemos CAC e custo por venda separadamente?** Não, e a Trava de Cegueira pontua essa
   dimensão em **0 de 5**. O investimento é mensurável; a contagem de clientes novos não existe em
   camada nenhuma. **Falta o denominador, não a ferramenta.**
3. **Dá para apurar por canal?** Hoje não, por três bloqueios independentes: a atribuição do Direto
   está furada por declaração do próprio cliente, o investimento de mídia vive fora do dashboard de
   funil (L9), e nenhuma conta separa B2B de B2C. Resolver um sem os outros dois não produz CAC por
   canal.

---

## A fila da V4: o que sai sem pedir nada à OLX

| Fonte | Indicadores | Estado do acesso | O que sai de lá | Prazo |
|---|---:|---|---|---|
| **CRM comercial** | 20 | declarado em 10/09, nunca aberto | Funil de Qualificação a Decisão: leads por origem, MQL, SQL, win rate, ciclo, motivos de perda e de cancelamento, contratos novos | 15/09 |
| Salesforce Marketing Cloud | 2 | declarado em 10/09, nunca aberto | Open e click rate, camada analítica da auditoria (i) | 15/09 |
| Search Console | 1 | declarado em 10/09, nunca aberto | Posição média nas keywords B2B, base da auditoria (ii) | 15/09 |
| GA4 | 3 | **aberto e testado em 14/09** | Sessões com 2+ páginas, páginas de plano e preço, retorno em 7 dias | 16/09 |
| V4MOS · Meta e Google | 14 | **ingerindo desde 12/09** | A camada de mídia já está medida. O que falta é o corte B2B, não a extração | depende de G2 |

---

## O pedido à OLX, consolidado

| Bloco | Origem | O que pedir | Dono | Prazo |
|---|---|---|---|---|
| A | A2 | Funil comercial com volumes e taxas por etapa, 12–24 meses, por vertical e canal | Leonardo Rosa | 17/09 |
| A | A3 | Ticket médio, ciclo de vendas e CAC por canal | Matheus + Iuna | 17/09 |
| A | A5 | Metas comerciais e OKRs vigentes, por etapa do fluxo | Matheus Rodrigues | 17/09 |
| A | A6 | Definição de ICP e segmentação de mercado | Florence Scappini | 17/09 |
| A | meta 2 | **P&L por vertical**, com mídia e imposto abertos por linha | Matheus Rodrigues | 17/09 |
| G | G2 | Investimento mensal por canal e campanha, com a marcação de qual campanha é B2B | Mirella Mendonça | 17/09 |
| G | G3 | Plano de mídia e quais conversões estão otimizadas em cada plataforma | Mirella Mendonça | 17/09 |
| G | G4 | Metas de CPA e ROAS, e o **dicionário da nomenclatura de campanha** | Mirella Mendonça | 17/09 |
| G | pend. 12 | Lista de subcontas do MCC `526-656-0190` e a quem pertencem os 7 customer IDs do ZapImóveis | Mirella Mendonça | 17/09 |
| B | pend. 30 | Clientes novos no Campana por vertical e mês, churn da coorte contra a anterior, receita da coorte | Michelle Morais | 17/09 |
| B | pend. 32 | Miro das jornadas, planilha de acessos, dashboards do Looker | Michelle Morais | 17/09 |
| B | pend. 33 | Antes e depois da higienização de base, em registros, por vertical | Evelyn Milare | 17/09 |
| A | pend. 20 | Arquivo original do slide FLUXOS e da jornada do cliente profissional | Carolina Dallolio | 17/09 |

---

## O que a V4 exporta sozinha das contas de anúncio

Onze exports de interface, sem API e sem concessão nova. Eles não substituem o corte B2B, que só a
OLX fecha, mas reduzem o pedido ao cliente ao que realmente só ele tem.

### Google Ads

| # | P | O export | O que destrava |
|---|---|---|---|
| 1 | P0 | Campanhas **segmentadas por Ação de conversão**, jan/25 a set/26 | Diz **qual** conversão o Google conta. São 896.625 conversões a R$ 3,06: se forem eventos de navegação importados do GA4, o CPA da conta é ficção e o Smart Bidding compra sessão |
| 2 | P0 | Campanhas **por mês**, incluindo pausadas, mesma janela | Fecha o buraco de nov/2025 a abr/2026 e diz se foi pausa real ou falha de ingestão |
| 3 | P0 | **Páginas de destino** por campanha | É o corte B2B contra B2C sem depender da nomenclatura: quem manda para `ads.`, `anuncie` e `planos` é captação de anunciante |
| 4 | P0 | Tela de **Ações de conversão**, todas as colunas | Mostra se `session_start`, marcado como evento-chave no GA4 VivaReal, está importado como conversão |
| 5 | P1 | Lista de subcontas do MCC | Fecha a pendência 12 |

### Meta Ads

| # | P | O export | O que destrava |
|---|---|---|---|
| 6 | P0 | Campanhas **por mês**, nas duas contas, com **Resultados, Indicador de resultado e Custo por resultado** | É exatamente o que o V4MOS não traz. Hoje o Meta tem R$ 7,38 mi e 1,88 bi de impressões sem um único desfecho associado |
| 7 | P0 | Detalhamento **por ação**, com conversas de mensagem iniciadas | O WhatsApp é 42% da entrada do funil. Se a campanha paga para WhatsApp existe, ela aparece aqui, com nome e custo |
| 8 | P1 | Mesmo relatório no **nível de anúncio** | Fecha a auditoria (iv) com 1.079 peças, contra as 8 que existiam antes de 12/09 |
| 9 | P0 | Lista de contas de anúncio do portfólio | Diz se a operação é maior que as duas contas concedidas |
| 10 | P1 | Conjuntos de dados e pixels | Cruza com os três pixels do GTM: `592658194155317`, `818079879779548`, `935989184453347` |

### E o que vale mais que os dez

> **11 · Uma frase do time de mídia: qual conta e qual campanha é captação de anunciante, e qual é
> consumidor.** Nenhum relatório separa os dois, porque a separação não está nos dados: está na
> cabeça de quem montou as campanhas. Essa frase transforma R$ 10,12 mi de investimento medido no
> numerador de um CAC. Sem ela, os outros dez produzem um retrato melhor da mídia e nenhum unit
> economics.

---

## Ressalvas: o que impede um número de entrar em comitê

| # | A ressalva | O efeito |
|---|---|---|
| 1 | Nenhuma conta de mídia separa B2B de B2C | R$ 10,12 mi medidos não são o investimento do recorte contratado |
| 2 | `purchase` dispara no gatilho de `begin_checkout` | A conversão de checkout do anunciante privado do ZapImóveis não é derivável |
| 3 | `session_start` é evento-chave no GA4 VivaReal | Infla qualquer taxa relatada e, se importado, treina o Smart Bidding para comprar sessão |
| 4 | O canal Direto está inflado por mídia sem atribuição | Pago declarado em 16%, medido em 0,8% |
| 5 | Escrita dupla no GA4 | Somar as duas propriedades conta o mesmo lead duas vezes |
| 6 | O slide FLUXOS não está versionado | O mix de canais inteiro não é conferível contra a fonte |
| 7 | Seis meses ausentes na série do Google | nov/2025 a abr/2026 sem registro, origem não apurada |
| 8 | A regra 8 não pode ser verificada | Não existe funil derivável para confrontar com a receita declarada |

---

## A base de conhecimento estava atrasada em cinco pontos. Quatro fecharam em 14/09

Auditoria do próprio repositório, feita ao montar este mapa, com o estado depois da rodada de
sincronização.

| O que mudou | Estado | Onde ficou |
|---|---|---|
| **O Meta passou a ingerir em 12/09**, recoletado em 14/09: 90 campanhas, 1.079 anúncios, R$ 7,38 mi, **2,7x o Google** | ✅ fechado | Os sete documentos foram corrigidos: `fluxo-de-receita.md`, `diagnostico-travas.md`, `checklist-dados-e-acessos.md`, `acessos-e-ferramentas.md`, `PENDENCIAS.md`, `sprint-diagnosticos` e a `SKILL.md` da `dre-v4mos` |
| **O GA4 respondeu pela API em 14/09**: nove indicadores viraram medido | 🔴 **aberto** | Segue só em `portal/assets/metrics-data.js`. Nenhum `.md` de diagnóstico registra os nove |
| A camada experiencial da **auditoria (i) CRM** fechou em 10/09, 16 achados | ✅ fechado | Commitada com as duas atas, as duas transcrições e o JSON |
| A **Trava de Cegueira** foi pontuada em 5 de 25 em 11/09 | ✅ fechado | `dre-diagnostico-travas.json` regerado, e o asset do portal com ele |
| O **lote de acessos de 10/09** | 🟡 parcial | Conferido o que este ambiente alcança, registrado em `dados/acessos.json` e no checklist. Quatro ferramentas seguem sem conferência |

### O que a correção do primeiro ponto ensinou, e vale registrar

A previsão era que a dimensão de CTR da Trava de Atenção passasse a ter evidência **e o score da
trava mudasse**. A primeira metade aconteceu, a segunda não, e o motivo é método:

> O CTR existe agora, 1,56% no Meta sobre 1.079 anúncios e 21 meses. Mas o método exige **duas**
> bases de comparação, benchmark setorial **e** histórico da própria conta. O histórico passou a
> existir. O benchmark setorial não existe com fonte documental nomeada neste repositório, e
> inventar um violaria a regra 1. É meia base, não duas.

Somam-se o recorte, nenhuma conta separa B2B de B2C, e a distância de onze vezes entre o CTR do
Meta e o do Google, que não descreve qualidade e sim duas contas contando clique de formas
diferentes. **Medir não é o mesmo que poder pontuar**, e a dimensão segue `null` por uma razão
melhor que a anterior.

### O que sobrou

1. **Os nove indicadores de GA4 em documento.** O achado do Pago 0,8% contra 16% declarado é
   material de Comitê 1 e não está em nenhum `.md` de diagnóstico.
2. **Abrir CRM comercial, Marketing Cloud e Search Console.** São elas que prendem os 23
   indicadores, 18 P0, e 20 dependem só do CRM comercial. Antes de abrir, confirmar se o e-mail
   `@olxbr` está habilitado no MyApps, que é a dependência que saiu das sessões de CRM.
3. **Um benchmark de CTR com fonte nomeada**, que é o insumo mais barato para destravar a dimensão
   (A) de Atenção.
4. **Uma frase do time de mídia** dizendo qual campanha é captação de anunciante. É o que
   transforma R$ 10,12 mi no numerador de um CAC, e é o que falta para o diagnóstico (vi) fechar
   cheio em 18/09.

---

## Como regerar

```bash
python3 .claude/scripts/build_mapa_numeros.py
01-cliente/entregaveis/.venv/bin/python 01-cliente/entregaveis/gera-docx-mapa-numeros.py
```

O `.docx` é gerado, nunca editado à mão. O catálogo das 78 métricas vive em
`portal/assets/metrics-data.js`: mudou lá, rode os dois comandos.
