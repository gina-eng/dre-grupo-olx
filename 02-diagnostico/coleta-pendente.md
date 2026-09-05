# Coleta pendente: o que o operador traz

> ✅ **Atualizado em 02/09.** O **bloco 1 inteiro chegou**: os 11 exports de contêiner estão em
> `assets/originais/H-rastreamento-gtm/`, incluindo o `GTM-PZ733B5` (ZapImóveis ANUNCIE), que era o
> item 🔴 da lista. Seis já foram auditados, ver
> [auditoria (vii)](auditoria-vii-rastreamento.md). **O que segue aberto é o bloco 2**, as telas de
> administração do GA4, que a API não entrega e só saem por print.

Lista de trabalho aberta em **01/09/2026**. Só itens que a V4 consegue buscar **com os acessos que já
tem**, sem depender de concessão nova da OLX. O que depende da OLX está em
[`checklist-dados-e-acessos.md`](checklist-dados-e-acessos.md) e em [`PENDENCIAS.md`](../PENDENCIAS.md).

Marcar `[x]` conforme entregar. Exports em JSON; telas de configuração, print serve.

---

---

## Bloco 0 · 🔴 O GTM tem QUATRO contas, não uma: aberto em 02/09

A tela inicial do GTM (item 1.8 desta lista) foi vista em 02/09 e a resposta muda o tamanho do
escopo da auditoria (vii):

| Conta | ID | Selo | Contêineres já recebidos |
|---|---|---|---:|
| BR - www.olx.com.br | `94905` | 360 | **10** |
| **Checkout Unificado - PRO** | `6326134112` | 360 | **0** |
| **VivaReal** | `4412254379` | 360 | **0** |
| **ZapImóveis** | `2971905372` | 360 | **1** de N |

Tudo que foi auditado até aqui cobre **uma conta e um contêiner de outra**. As quatro têm selo 360,
ou seja, são todas do tier pago.

> O contêiner que temos da conta ZapImóveis chama-se **"5. ZapImóveis - Container ANUNCIE"**. O
> prefixo `5.` indica uma lista numerada, provavelmente há pelo menos cinco contêineres nessa conta,
> e vimos um.

### O que pedir, em ordem de valor

- [ ] **0.1 · Conta `Checkout Unificado - PRO` (`6326134112`): todos os contêineres** 🔴
  **É o pedido de maior valor do projeto.** O nome junta as duas palavras que definem o escopo
  contratado: *checkout* é onde a receita acontece, e *PRO* é o anunciante profissional. Se a
  hipótese estiver certa, é aqui que mora a medição da receita B2B do grupo, e o
  [achado 1](auditoria-vii-rastreamento.md) (`purchase` disparado pelo gatilho de `begin_checkout`,
  em `GTM-KGFGVFC`) precisa ser relido contra o que existir aqui, porque pode estar corrigido, pode
  estar duplicado, ou pode ser que a conta que auditamos seja a legada.
  *A leitura do nome é inferência, não conclusão. Confirmar antes de afirmar em comitê.*

- [ ] **0.2 · Conta `ZapImóveis` (`2971905372`): os contêineres restantes** 🔴
  Temos o `5.`, faltam os outros. É o lado Imóveis do escopo B2B.

- [ ] **0.3 · Conta `VivaReal` (`4412254379`): todos os contêineres** 🟠
  Terceira vertical, nunca vista. O V4MOS ingere a MCC VivaReal (`526-656-0190`), esta é a
  contraparte de medição dela.

- [ ] **0.4 · Print da tela inicial de cada uma das três contas novas**
  Para saber quantos contêineres existem antes de pedir por nome, como foi feito na conta `94905`.

> Mesmo caminho de export: abrir o contêiner → Administração → Exportar contêiner → versão publicada.
> Os JSON vão para `assets/originais/H-rastreamento-gtm/`, mantendo o padrão de nome
> `gtm-<id>_workspace<n>.json`.

## Bloco 1 · Google Tag Manager: conta `BR - www.olx.com.br`
*Caminho do export: abrir o contêiner → Administração → Exportar contêiner → workspace ou versão publicada.*

- [x] **1.1 · `GTM-PZ733B5` · Zapimóveis ANUNCIE** 🔴
  É o gêmeo do Planos Profissionais no lado Imóveis. Sem ele a auditoria cobre metade do escopo.
- [x] **1.2 · `GTM-TNX8FDS` · Buyer Journey**
  Contraponto B2C. Serve para demonstrar em comitê se o consumidor é medido melhor que o anunciante.
- [x] **1.3 · `GTM-TW9TWPT5` · Login**
  Confirma ou descarta o `page_view` duplicado em `conta.olx.com.br/acesso` e `/cadastro`.
- [x] **1.4 · `GTM-KP8QMDH` · LPs Unbounce**
  É onde as landing pages vivem de fato. Insumo direto da auditoria (viii).
- [x] **1.5 · `GTM-5WWRGTQ` (VAS) · `GTM-T2H3VFL` (Google Shopping) · `GTM-PWP7Z4C` (Wallet)**
  Prioridade menor. Fecham o inventário.

- [ ] **1.6 · Print da lista completa de contêineres**, rolando até o fim.
  Sabemos que 22 é piso, não total.
- [ ] **1.7 · Print da aba *Versões* do `GTM-KGFGVFC`** 🔴
  **Data desde quando o `purchase` está preso ao gatilho de `begin_checkout`.** Sem essa data não sei
  que janela do histórico de conversão está contaminada, e o forecast depende de saber.
- [x] **1.8 · Print da tela inicial do GTM, com todas as contas visíveis** ✅ **respondido em 02/09**
  **Sim, existe**: e não uma, três: `Checkout Unificado - PRO`, `VivaReal` e `ZapImóveis`, além da
  `BR - www.olx.com.br`. Ver **Bloco 0** acima, que é a consequência disso.

## Bloco 2 · GA4: propriedade **OLX App + Web** (`152644854`)
*Tudo em Administrador. Só prints; são telas que a API não me entrega.*

- [ ] **2.1 · Vínculos de produto → BigQuery** 🔴
  **A maior alavanca da lista.** Se houver export ativo, temos dado na granularidade da linha e o
  funil (A2) deixa de depender de pedido à OLX.
- [ ] **2.2 · Coleta e modificação de dados → Retenção de dados** 🔴
  Se estiver em 2 meses, **o forecast de 24 meses não tem lastro no GA4**, e isso muda a estratégia
  agora, não em outubro.
- [ ] **2.3 · Coleta e modificação de dados → Fluxos de dados**
  Fecha o mapa propriedade × measurement ID × superfície, e revela Measurement Protocol ou server-side.
- [ ] **2.4 · Eventos-chave (lista completa)**
  Explica por que `ad_edition` (4,14 mi/mês) não é conversão e `session_start` é.
- [ ] **2.5 · Gerenciamento de acesso à propriedade**
  Fecha de vez a dúvida do papel (Leitor vs. Editor) e mostra **com qual conta** o acesso foi dado.

## Bloco 3 · Meta: portfólio `New OLX Brasil`
*Configurações do portfólio. Dois prints.*

- [ ] **3.1 · Contas → Contas de anúncios**
  Quero saber se a operação é maior que as duas contas pendentes.
- [ ] **3.2 · Fontes de dados → Conjuntos de dados / Pixels**
  Cruzar com os três pixels achados no GTM: `592658194155317`, `818079879779548`, `935989184453347`.

## Bloco 4 · Google Ads

- [ ] **4.1 · Lista de subcontas do MCC `526-656-0190`**
  O GA4 mostrou 7 customer IDs vinculados ao ZapImóveis e nenhum é o nosso. Se algum aparecer aqui,
  a [pendência 12](../PENDENCIAS.md) fecha sozinha:
  `9221562141` · `6794249680` · `7581320191` · `6386557247` · `1973081572` · `5004050899` · `4632447364`

## Bloco 5 · Teste rápido

- [ ] **5.1 · Abrir `search.google.com/search-console` e ver se aparece alguma propriedade.**
  Trinta segundos. O GA4 também estava liberado e ninguém sabia.

---

## Onde guardar

Os JSONs de contêiner vão para `assets/originais/H-rastreamento-gtm/` (pasta já criada). Prints de
tela de configuração vão para `assets/originais/H-rastreamento-gtm/telas/`.

> ⚠️ Os exports contêm IDs de pixel, chaves públicas de SDK e IDs de conversão. Nada disso é segredo,
> tudo aparece no código-fonte das páginas, mas o material é confidencial pelo aviso da OLX e não
> sai deste repositório privado.
