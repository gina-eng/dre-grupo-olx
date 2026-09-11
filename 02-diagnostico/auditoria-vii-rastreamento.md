# Auditoria (vii) · Rastreamento Completo (GA4 e GTM)

> **Como ler este documento.** Ele cresceu em **quatro rodadas**, na ordem em que o material chegou,
> e cada rodada mantém a fonte que tinha na data. Para o estado atual, vá direto a:
>
> | | |
> |---|---|
> | Cobertura de hoje | [quarta rodada](#quarta-rodada--11092026--o-parque-inteiro-entra): **60 contêineres**, 4 contas, 1.779 tags |
> | Achados | **41**, numerados em sequência contínua entre as rodadas |
> | O que não está confirmado | [Ressalvas de leitura](#ressalvas-de-leitura), atualizadas em 11/09 e válidas para as quatro rodadas |
> | Leitura da trava | [o que a quarta rodada muda](#o-que-a-quarta-rodada-muda-na-leitura-da-trava) |
>
> 🔴 **A ressalva que governa todas:** os 62 exports são de espaço de trabalho, nenhum é de versão
> publicada. Os achados de configuração descrevem o rascunho até que a versão publicada seja
> comparada.

---

## Primeira rodada · 01/09/2026 · os cinco primeiros contêineres

**Fonte:** export em JSON de 5 contêineres do GTM, conta `BR - www.olx.com.br` (accountId `94905`),
exportados em 01/09/2026, mais consultas à API de dados do GA4 na mesma data.

| Contêiner | ID | Superfície |
|---|---|---|
| OLX - Container Master | `GTM-546N2JV` | Carregador dos 5 domínios B2B + zonas |
| OLX - Planos Profissionais & PAYG | `GTM-KGFGVFC` | `planoprofissional` · `adquirir` · `pointsofsales` · `goldpayments` · `planos` |
| OLX - Seller Journey | `GTM-MXQKDG3` | `www2` · `olx-pay` · `conta` |
| OLX - Checkout | `GTM-M4TL57GX` | `pagamento.olx.com.br` |
| OLX - Conecta Autos | `GTM-MJX9PG4` | `conectaautos.olx.com.br` |

> **Onde o dado cai.** Os cinco escrevem no mesmo measurement ID, `G-50C013M2CC`. Cruzando com o
> GA4, essa é a propriedade **OLX App + Web** (`152644854`, tier 360, 219 nomes de evento), **não** a
> `GA4 Grupo OLX` (`503925542`), que segue com zero evento-chave. Ou seja: a medição B2B existe, mas
> mora numa propriedade que ninguém indicou no onboarding.

---

## 🔴 1. O evento `purchase` do GA4 é disparado pelo gatilho de `begin_checkout`

Em `GTM-KGFGVFC`:

| Tag | ID | Gatilho | O gatilho escuta |
|---|---|---|---|
| `[TAG] GA4 - Begin Checkout` | 154 | `215` | `begin_checkout` |
| **`[TAG] GA4 - Purchase`** | **426** | **`215`** | **`begin_checkout`** |

As duas tags disparam no mesmo gatilho. **Todo início de checkout nos domínios de Planos
Profissionais e PAYG gera um `purchase` no GA4.** O gatilho correto existe e está ocioso: `306`
(`[AC] Purchase - Planos Profissionais`) não é usado por tag nenhuma, e `441` só alimenta uma tag do
Braze que está pausada. O único consumidor do evento real `purchase` é a tag `164`, de **Universal
Analytics**, desativada pelo Google.

**Consequência:** na superfície de receita B2B, o GA4 conta tentativa como venda. Em agosto a
propriedade registrou 2.686.897 `begin_checkout` e 565.258 `purchase`, os dois marcados como
evento-chave. Os números globais não são iguais porque app e outras superfícies também enviam
`purchase`; a contaminação é da parcela B2B, que é justamente a do escopo.

**Correção:** apontar a tag 426 para o gatilho 306 ou 441.

---

## 🔴 2. O consentimento concede tudo por padrão, e o botão de recusar está oculto

O template AdOpt aparece em três contêineres. **Em dois deles o padrão é `denied`. No Master, o
único que de fato instancia o template numa tag, o padrão é `granted` em tudo:**

```js
setDefaultConsentState({
  ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted',
  analytics_storage: 'granted', functionality_storage: 'granted',
  personalization_storage: 'granted', security_storage: 'granted', wait_for_update: 500
});
```

O `galleryReference` do Master marca `"isModified": true`, o template da galeria foi editado
localmente. Em `GTM-MJX9PG4` e `GTM-MXQKDG3` a versão íntegra (`denied`) está presente **mas nenhuma
tag a instancia**: ela não roda.

Some-se a isso a tag `[TAG] Adopt - OLX - Tag Initialization` (Master, id 171):

```html
<style> button#adopt-reject-all-button { display: none !important; } </style>
<script async> setTimeout(loadScript, 4000); </script>
```

**O botão "recusar tudo" do banner é escondido por CSS**, e o injetor do banner só carrega **4
segundos** depois, tempo em que as tags já dispararam sob o padrão `granted`.

**Leitura:** os três elementos juntos, padrão concedido, recusa oculta, banner atrasado, descrevem
um consent mode que não coleta consentimento, apenas o encena. Isso é matéria de LGPD e de política
do Google (Consent Mode v2), e não é decisão da V4: **é achado para levar à OLX com o jurídico
deles na sala.**

**A confirmar:** se existe orientação jurídica interna que sustente o padrão `granted` para o Brasil
(há teses sobre legítimo interesse em analytics). Nada sustenta esconder o botão de recusa.

---

## 🔴 3. `lead_b2b` não existe nos dados

A tag `429 [TAG] DataLayer - Lead B2B` está montada e ativa. **A propriedade registrou zero eventos
`lead_b2b` em agosto.**

A causa está na tag `349 [TAG] Lead B2B Validation`, que alimenta o gatilho. Ela roda em **todo
clique da página** e identifica o lead por **posição no DOM**:

```js
els = document.querySelectorAll("#contactUs a.olx-button");
if (i == 0) { lead_type: "telefone" }
else if (i == 2) { lead_type: "whatsapp" }
```

Qualquer mudança de layout, um botão a mais, uma ordem trocada, desliga a medição sem erro
visível. É o que parece ter acontecido. A mesma tag deixou um `console.log(el)` em produção,
disparando a cada clique.

**Consequência:** o lead B2B de Planos Profissionais, que é o topo do funil da receita contratada,
não tem numerador.

---

## 🔴 4. A tag que grava o objeto de usuário está pausada: e 20+ variáveis dependem dela

No Master, `57 [API] Dados do usuário + Insider Object User - Local Storage` está **pausada**. É a
única tag no material exportado que grava a chave `user_olx` no `localStorage`.

Nos outros contêineres, as propriedades de usuário enviadas ao GA4 leem exatamente essa chave:

```js
function() { return JSON.parse(localStorage.getItem('user_olx')).gtm_user_72; }
```

Se `user_olx` não existir, `JSON.parse(null)` devolve `null` e o acesso à propriedade lança
`TypeError`. Ficam sem valor, em `GTM-KGFGVFC`, `GTM-MJX9PG4` e `GTM-MXQKDG3`:
`user_account_type`, `user_account_level`, `user_login_type`, `user_gender`, `user_email`,
`user_phone`, `user_zip_code`, `olx_user_id`.

**A mais cara:** em `GTM-MXQKDG3`, `[VAR] User - Account Type` alimenta o parâmetro
**`seller_category`** dos eventos `ad_insertion`, `ad_edition` e `ad_remove`. `seller_category` é
precisamente o que separa anunciante **profissional** de anunciante **particular**, o corte B2B.
Sem ele, 4,6 milhões de `ad_insertion` por mês não são segmentáveis por tipo de vendedor.

**A confirmar:** se o site grava `user_olx` por código próprio, fora do GTM. Se gravar, o problema
não existe. Se não gravar, é a falha de maior alcance do conjunto.

---

## 🔴 5. Parâmetros de item lidos sem índice de array

Em `GTM-KGFGVFC` e `GTM-M4TL57GX` as variáveis de e-commerce apontam para caminhos como:

```
ecommerce.items.item_id     ecommerce.items.price     ecommerce.items.quantity
items.item_category         ecommerce.items.item_category_2
```

`items` é um **array**. Sem índice (`items.0.item_id`) a variável do dataLayer devolve indefinido. O
próprio contêiner prova que a forma correta é conhecida: `[VAR] E-commerce - Items` usa
`ecommerce.items.0`.

Há ainda erro de nome: `item_category_2` com sublinhado, contra `item_category2` do padrão GA4 e do
contêiner de Checkout.

**Consequência provável:** `purchase` e `begin_checkout` chegam sem item, sem preço e sem quantidade.
**Confirmar no Preview antes de afirmar em comitê**: é leitura de configuração, não de payload.

---

## 🟠 6. Universal Analytics ainda instalado e disparando

`UA-70177409-2` aparece ativo em `GTM-KGFGVFC` (pageview e purchase) e em `GTM-MJX9PG4` (pageview,
interações, section views, YouTube, e-commerce). O Universal Analytics parou de processar dados em
2023–2024. São tags que carregam, custam performance e não medem nada.

Pior: em `GTM-MJX9PG4`, `[TAG] GA4 - Section Views` está **pausada** enquanto a equivalente em UA
está ativa. As visualizações de seção existem só na propriedade morta.

## 🟠 7. Dupla contagem de conversão no Google Ads

Em `GTM-MXQKDG3`, o evento `ad_insertion` dispara **duas** conversões na conta `963385983`:

| Tag | Gatilho | Cobertura |
|---|---|---|
| `[PXL] Google Ads - Ad Insertion - Real Estate` | 461 | Imóveis |
| `[PXL] Google Ads - Ad Insertion - Autos` | 463 | Autos |
| `[PXL] Google Ads - Ad Insertion - Goods` | 465 | O resto |
| **`[PXL] Google Ads - Ad Insertion`** | **343** | **Tudo, sem filtro** |

As três primeiras particionam o universo; a quarta cobre o universo inteiro. Cada inserção conta
duas vezes. **A confirmar:** pode ser intencional, com a genérica marcada como secundária. Se as duas
forem primárias, o Smart Bidding está otimizando sobre o dobro do volume real.

## 🟠 8. O gatilho de `ad_remove` escuta um nome que não existe

`GTM-MXQKDG3`, gatilho `377`: escuta o evento `ads_remove`. A tag e o GA4 usam `ad_remove`. Em
agosto: `ad_remove` = 157.632 eventos, `ads_remove` = zero. Ou seja, os 157 mil vêm de outra origem
(app ou outro contêiner) e **a tag web nunca dispara**.

## 🟠 9. `plano-profissional` contra `planos-profissionais`

O mesmo conceito aparece escrito de duas formas, em gatilhos ativos:

| Gatilho | Filtro |
|---|---|
| `306` | `checkout_type` contém `plano-profissional` |
| `436` | `checkout_type` contém `planos-profissionais` |
| `434` | `content_group` **igual a** `plano-profissional` |
| `441` | `content_group` contém `planos-profissionais` |

Uma das duas grafias não casa com nada. Como `306` é justamente o gatilho de purchase que deveria
estar em uso (achado 1), a grafia precisa ser resolvida antes da correção.

## 🟠 10. Ferramentas de terceiros sem gate de consentimento

| Tag | Contêiner | `consentStatus` |
|---|---|---|
| `[TAG] Mouseflow - All Pages` | Master | **NOT_SET** |
| `[TAG] CRM Web Push - Insider` | `GTM-KGFGVFC` | **NOT_SET** |
| `[TAG] CRM Web Push - Insider` | `GTM-MJX9PG4` | NEEDED (`ad_storage`) |

O **Mouseflow grava sessão de usuário** e roda sem verificação adicional de consentimento. O Insider
é gatilhado em um contêiner e não no outro, a mesma ferramenta, na mesma conta, com dois critérios.

## 🟠 11. SPA com `page_view` limitado a uma vez por carregamento

`GTM-KGFGVFC`, tag `339 [TAG] GA4 - Pageview`: dispara em **All Pages** e no evento de dataLayer
`page_view`, com `tagFiringOption: ONCE_PER_LOAD`. O gatilho de dataLayer só existe porque a
aplicação é SPA (os seletores CSS do contêiner apontam para `#root`, React). Em SPA, `ONCE_PER_LOAD`
mede a primeira tela e ignora toda a navegação seguinte.

## 🟠 12. Dois erros de JavaScript em produção

**`GTM-KGFGVFC`, tag 405 · `Virtual Select Promotion - Intercom`:** declara `curUrl` e `searchParams`
e depois usa `search.searchParams.get(...)`. `search` não existe naquele escopo. Quebra sempre que o
parâmetro `local` contém "intercom", ou seja, exatamente no tráfego que a tag existe para medir.

**`GTM-MJX9PG4`, tag 54 · `Evento GA - View Promotion`:** faz
`links[i].getAttribute("href").indexOf(...)` sem checar nulo. Qualquer `<a>` sem `href` na página
derruba a tag. **A correção já existe no Master** (tag 364 testa `links[i] && links[i].getAttribute("href") &&`)
e não foi propagada para o filho.

## 🟠 13. Eventos de alto volume que não são evento-chave

| Evento | Volume (ago/2026) | Evento-chave |
|---|---:|---|
| `ad_insertion` | 4.602.128 | ✅ |
| **`ad_edition`** | **4.140.566** | ❌ |
| **`ad_remove`** | **157.632** | ❌ |
| `qualified_lead_autos_pro` | 4.680.465 | ✅ |

## 🟠 14. Toda a stack Braze está pausada

Quatorze tags do Braze, distribuídas por Master, `GTM-KGFGVFC` e `GTM-MXQKDG3`, estão com
`paused: true`: inicialização, page view, begin checkout, purchase, ad insertion/edition/remove.
Alguém montou a instrumentação inteira de CRM e não a ligou. **Perguntar se é implantação em espera
ou projeto abandonado**, muda a leitura da camada de retenção, que é a auditoria (i).

## 🟠 15. Existe uma atribuição paralela em cookie, para o Salesforce

Master, tag `162 [TAG] Settings - UTM Cookies`. Escreve `sf_utm_source/medium/campaign/content/term`
em `.olx.com.br`, modelo **last-click não-direto**, janela de **90 dias**. O próprio comentário no
código diz: *"Atribuição client-side. Não substitui dados do GA4."*

**Isto responde a ressalva que estava aberta:** a OLX de fato mede fora do GA4. Há uma segunda fonte
de verdade de atribuição, com modelo e janela diferentes dos do GA4, alimentando o Salesforce. Toda
divergência de números entre marketing e comercial provavelmente nasce aqui.

Esses mesmos cookies alimentam a tag `448 [TAG] Mensagens Dinâmicas WhatsApp`, que personaliza a
mensagem de WhatsApp conforme o canal de origem, e **não emite nenhum evento de GA4 ao fazê-lo**.

## 🟡 16. Dados pessoais

A tag pausada `57` do Master monta, no `localStorage`, um objeto com **md5 e sha256 de e-mail,
telefone, gênero e CEP**, e monta `window.insider_object.user` com **e-mail, telefone e apelido em
texto claro**, além de enviar nome, e-mail e telefone ao Braze. Está pausada, é risco latente, não
ativo. Registrar para a revisão de LGPD do contrato.

Em `GTM-KGFGVFC`, a tag `379` carrega `dataunion.com.br` (PH3A, enriquecimento de dados cadastrais)
na página de planos de autos, gatilhada por `utm_campaign=ph3a`. Está com gate de `ad_storage`.

## 🟡 17. Inventário técnico levantado do export

**Pixels e IDs.** Meta: `592658194155317` (Seller Journey, rotulado "OLX Pay"), `818079879779548` e
`935989184453347` (Conecta Autos), três pixels distintos, nenhum ligado às duas contas pendentes de
aprovação. Google Ads: `AW-10947843670` e conversões em `963385983`. Floodlight: advertiser
`14127847`. TikTok: `CO25OBRC77U47AMPJES0`, **confirma TikTok ativo**, item F2 do checklist.

**Contêineres filhos que ainda não temos:** as zonas do Master apontam para
`GTM-PZ733B5` (**Zapimóveis - Container ANUNCIE**, B2B de imóveis, com fronteira estreitíssima:
só dispara quando a URL contém `adquirir.zapimoveis.com.br/?action=zap-owners&zapOwnersUuid`),
`GTM-5WWRGTQ` (OLX - VAS), `GTM-KP8QMDH` (LPs Unbounce), `GTM-T2H3VFL` (Loja - Google Shopping),
`GTM-PWP7Z4C` (Wallet). Nenhum deles aparecia na lista visível de 22.

**Fallback perigoso.** `GTM-MXQKDG3` resolve o measurement ID por tabela de regex de hostname, com
valor padrão **`G-XXXXXXXXXX`**. Hoje casa; num domínio novo, os hits somem em silêncio.

---

## O que isso significa para o método

A regra 8 deste repositório exige que a receita derivada do funil bata com a declarada, com 5% de
tolerância. Com os achados 1, 3, 4 e 5, o funil B2B derivável do GA4 hoje tem **numerador
inexistente** (`lead_b2b` = 0), **denominador não segmentável** (`seller_category` vazio) e
**conversão contaminada** (`purchase` disparado por `begin_checkout`).

Não é caso de "medir mal". É caso de **não haver funil B2B mensurável** até que 1, 3 e 4 sejam
corrigidos. Isso é evidência dura de **Trava de Cegueira**, e a causa-raiz em formato de política
implícita se escreve assim:

> *A medição é responsabilidade de quem implementa cada superfície, não de quem responde pela
> receita.* Daí decorrem 22+ contêineres com convenções próprias, a mesma correção aplicada num e
> não no outro, dois consentimentos opostos, e ninguém encarregado de conferir se o número que sai
> corresponde ao negócio.

---

## Ressalvas de leitura

> **Atualizadas em 11/09/2026, depois da quarta rodada.** Valem para **toda a auditoria**, as quatro
> rodadas e os 41 achados, e não só para a primeira. Estão aqui, no fim da primeira rodada, porque é
> onde nasceram.

### A ressalva que governa todas as outras: rascunho não é produção

🔴 **Os 41 achados que vêm do GTM descrevem o espaço de trabalho, não o que está no ar.**

Conferido em 11/09 lendo `containerVersionId` dentro de cada arquivo: os **62 exports trazem `0`**,
a assinatura de export de workspace. A versão publicada carrega o número da versão. **Nenhum export
do parque é de versão publicada.**

Nenhum achado de configuração está, hoje, confirmado em produção, e nenhum deve ser afirmado como
tal em comitê antes da comparação. O caso mais sensível continua sendo o
[achado 1](#-1-o-evento-purchase-do-ga4-é-disparado-pelo-gatilho-de-begin_checkout): se o `purchase`
preso ao gatilho de `begin_checkout` existir só no workspace, é rascunho que ninguém publicou; se
estiver na versão publicada, é receita B2B medida errada em produção. Coleta pedida em
[`guia-export-gtm.md`](guia-export-gtm.md), lote 1.

**Um dado de 11/09 tempera essa ressalva, sem anulá-la.** Doze contêineres foram reexportados dez
dias depois da primeira leva. **Dez estavam idênticos** fora do `fingerprint`, e os dois que mudaram
não tocaram `purchase` nem `begin_checkout`. Ou seja: estes rascunhos não são material em edição
ativa, são a configuração assentada. Isso torna provável que espelhem o publicado, e **provável não
é confirmado**.

### As duas origens de evidência não têm o mesmo peso

Isto importa para pontuar a Trava de Cegueira, porque a regra 6 do método exige evidência formal
para nota acima de 3.

| Origem | O que sustenta | Vale como |
|---|---|---|
| **API do GA4**, lida em 31/08, 01/09 e 11/09 | propriedades de alto volume com zero evento-chave, `session_start` como conversão na VivaReal, tier de serviço por propriedade, mapa de measurement ID para propriedade | 🟢 **produção observada** |
| **Export de GTM**, 62 arquivos | tag, gatilho, variável, consentimento, tudo que as quatro rodadas leem | 🟡 **configuração de rascunho** |

**Uma nota de Cegueira apoiada no lado GA4 não herda a ressalva do rascunho.** Uma nota apoiada no
lado GTM herda. Na prática os dois lados dizem a mesma coisa, mas o material de comitê deve deixar
claro qual evidência sustenta qual afirmação.

### Confirmações que só o navegador dá

Leitura de configuração exportada e de contagem de evento não é observação de comportamento. Quatro
achados pedem o Preview do GTM ou a página publicada:

| Achado | O que confirmar |
|---|---|
| [5](#-5-parâmetros-de-item-lidos-sem-índice-de-array) | se os parâmetros de item chegam vazios de fato |
| [11](#-11-spa-com-page_view-limitado-a-uma-vez-por-carregamento) | se a SPA perde `page_view` na navegação interna |
| [18](#-18-no-lado-imóveis-o-consentimento-não-roda-as-duas-tags-do-adopt-estão-pausadas) | se o banner do AdOpt realmente não aparece no domínio ZapImóveis ANUNCIE |
| [31](#-31-o-page_view-do-checkout-olx-escuta-dois-eventos-diferentes) | se a página empurra os dois eventos e o `page_view` conta em dobro |

E o [achado 4](#-4-a-tag-que-grava-o-objeto-de-usuário-está-pausada-e-20-variáveis-dependem-dela)
cai por terra se o site gravar `user_olx` por código próprio, fora do GTM.

### O que o GA4 não deixou ver

As telas de administração do GA4 (fluxos de dados, retenção, exportação para BigQuery, definição de
eventos-chave) seguem fora de alcance: as propriedades continuam em `can_edit: false`, conferido por
API em 11/09. A decisão desta janela foi **seguir sem elas**, e a auditoria cobre a maior parte da
causa pelo GTM, que não depende desse nível. Ver [PENDENCIAS 13](../PENDENCIAS.md).

Some-se a isso que **quatro streams de GA4 que recebem dado do GTM não estão entre as 71 propriedades
visíveis** à V4 ([achado 37](#-37-as-landing-pages-b2b-medem-na-propriedade-cega-e-quatro-streams-estão-fora-do-alcance-da-v4),
[PENDENCIAS 27](../PENDENCIAS.md)). Parte da medição do grupo tem destino que a auditoria não alcança.

### O que esta auditoria não é

Nada aqui descreve performance de negócio. Descreve **como a medição está montada**. Taxa de
conversão, receita e volume aparecem só como consequência do que a medição produz ou deixa de
produzir.

### Ressalvas encerradas

| Ressalva | Estava assim | Encerrada porque |
|---|---|---|
| **Cobertura parcial** | "auditados 6 contêineres de um total ainda desconhecido"; as contas `Checkout Unificado - PRO` e `VivaReal` inteiramente por auditar | 11/09: as quatro contas foram varridas e os **60 contêineres** auditados. O inventário está fechado no nível de conta e de contêiner |
| **Exports não lidos** | "cinco exports no repositório ainda não foram lidos: Buyer Journey, VAS, Unbounce LP, Login, Wallet" | os cinco entraram na quarta rodada, junto com os outros 40 |

---

# Segunda rodada · 02/09/2026 · o lado Imóveis entra

Os 6 contêineres restantes chegaram ao repositório. O inventário passa de 5 para **11 exports**, e o
mais decisivo é o `GTM-PZ733B5`, **ZapImóveis ANUNCIE**, o gêmeo do Planos Profissionais no lado
Imóveis. Era ele que faltava para a auditoria deixar de cobrir metade do escopo contratado.

| Contêiner | ID | Tags | Pausadas | Estado |
|---|---|---:|---:|---|
| 5. ZapImóveis - Container ANUNCIE | `GTM-PZ733B5` | 48 | 9 | 🔴 auditado nesta rodada |
| OLX - Buyer Journey | `GTM-TNX8FDS` | 124 | 37 | ⚪ pendente |
| OLX - VAS | `GTM-5WWRGTQ` | 48 | 18 | ⚪ pendente |
| OLX - Unbounce \| LP | `GTM-KP8QMDH` | 40 | 0 | ⚪ pendente · insumo de (viii) |
| OLX - Login | `GTM-TW9TWPT5` | 5 | 1 | ⚪ pendente |
| OLX - Wallet | `GTM-PWP7Z4C` | 3 | 0 | ⚪ pendente |

## 🔴 18. No lado Imóveis o consentimento não roda: as duas tags do AdOpt estão pausadas

No `GTM-PZ733B5`, as **duas** tags que inicializam o consentimento estão desligadas:

| Tag | ID | Tipo | Estado |
|---|---|---|---|
| `[TAG] Adopt - Tag Initialization` | 338 | `html` | **pausada** |
| `[TAG] AdOpt - Consent Initialization` | 340 | template AdOpt | **pausada** |

Ao mesmo tempo, **17 tags do contêiner declaram `consentSettings: NEEDED`**, elas estão escritas
para esperar um sinal de consentimento. Esse sinal nunca chega, porque quem o emitiria está pausado.
Sem estado default declarado, o GTM não trata o consentimento como ativo e as tags disparam.

O que dispara sem gate nenhum, nesse contêiner: **GA4 em duas propriedades**, **dois pixels do
Meta**, **duas contas de conversão do Google Ads** e o Braze.

> Este achado é **diferente** do achado 2, não uma repetição dele. No Master o consentimento roda e
> concede tudo por padrão, é uma configuração permissiva. Aqui ele **não roda**. São dois defeitos
> distintos, na mesma obrigação de LGPD, em dois lados do mesmo grupo.

**Quem decide:** jurídico / DPO da OLX. Não é correção técnica.

## 🔴 19. A medição B2B de Imóveis mora numa terceira propriedade

Os 5 contêineres da primeira rodada escrevem todos em `G-50C013M2CC` (**OLX App + Web**,
`152644854`). O ZapImóveis ANUNCIE escreve em outras duas:

| Constante no contêiner | Measurement ID | Tags que enviam |
|---|---|---:|
| `[CONST] GA4 - Verticalizado` | `G-6TV9FSHYVM` | 16 |
| `[CONST] GA4 - Unificado` | `G-ZBYP2KJ7L9` | 2 |

Mais quatro Google Tags soltas: `GT-K8GV5GMK`, `G-W39KX3CBHX`, `AW-791128603`, `AW-10779204119`.

**A superfície B2B do grupo está espalhada por pelo menos três propriedades do GA4**, e o onboarding
apontou uma quarta (`GA4 Grupo OLX`, `503925542`) que não recebe de nenhum contêiner auditado. Isso
agrava a [pendência 16](../PENDENCIAS.md): não é só que a medição B2B mora em outro lugar, é que ela
mora em vários, e ninguém entregou o mapa.

## 🟠 20. `generate_lead` é contado duas vezes, em duas propriedades

O mesmo gatilho, `[208] lead_dbm`, evento customizado `lead_dbm`, dispara duas tags:

| Tag | ID | Destino |
|---|---|---|
| `[GA4 Verticalizado] generate_lead` | 209 | `G-6TV9FSHYVM` |
| `[GA4 Unificado] generate_lead` | 356 | `G-ZBYP2KJ7L9` |

Um lead de anunciante Imóveis vira **dois** `generate_lead`, em duas propriedades. Não é dupla
contagem dentro da mesma propriedade, então não infla o relatório de uma só, mas qualquer
consolidação que some as duas conta cada lead duas vezes. Confirmar qual das duas é a de referência
antes de usar `generate_lead` como numerador do fluxo de receita.

## ✅ Contraponto: aqui a consolidação de tags foi feita certo

Nove tags estão pausadas neste contêiner, seis delas do funil comercial, `purchase Privado`,
`add_to_cart` e `begin_checkout` nas variantes Privado e Profissional. **Verifiquei gatilho por
gatilho, e não há perda de cobertura:**

| Tag pausada | Gatilho | Absorvida pela tag ativa |
|---|---|---|
| `purchase Privado` (227) | 222 | `[TAG] GA4 Verticalizado - purchase` (317) |
| `add_to_cart - Privado` (243) | 264 | `[TAG] GA4 - add_to_cart` (258) |
| `begin_checkout - Privado` (248) | 247 | `[TAG] GA4 Verticalizado - begin_checkout` (308) |
| `begin_checkout - Profissional` (256) | 255 | idem (308) |
| `add_to_cart - Profissional` (267) | 246 | idem (258) |
| `add_to_cart - New Page Prof.` (303) | 304, 325 | idem (258) |

Cada gatilho das seis pausadas aparece na lista de disparo de uma tag ativa equivalente. Isso é
**consolidação bem executada**: alguém unificou seis tags em três e desligou as antigas em vez de
deixar as duas gerações rodando.

> E é exatamente esse cuidado que falta no `GTM-KGFGVFC`, do lado OLX, onde o achado 1 mostra a tag
> de `purchase` apontando para o gatilho de `begin_checkout` com o gatilho correto ocioso. **Mesma
> organização, mesmo tipo de trabalho, dois padrões de rigor.** Para uma trava de Cegueira isso é
> mais informativo do que qualquer um dos dois achados isolado: a capacidade existe na casa e não
> está distribuída por igual.

## 🟠 21. Mouseflow está instalado e pausado no ZapImóveis ANUNCIE

A tag `[TAG] Mouseflow` (139), projeto `6228af6b-03b2-4583-b00a-88…`, está **pausada**. É um projeto
diferente do encontrado no Master (`b837e449-83ee-457f-9ef5-8f976953f2bc`).

Insumo direto do diagnóstico **(viii) Páginas de captura**: a ferramenta de comportamento existe, tem
dois projetos, e no domínio de captação de anunciante Imóveis ela não está gravando. Muda o pedido de
acesso, não é "vocês têm Hotjar ou similar?", é "temos dois projetos de Mouseflow, um deles
desligado; qual é o oficial e por que este está pausado?".

## 🟠 22. Mais dois IDs de conversão do Google Ads e mais dois pixels do Meta

| Tipo | ID | Onde |
|---|---|---|
| Google Ads conversão | `791128603` | `[PXL] Google Ads - Remarketing` |
| Google Ads conversão | `10779204119` | `[PXL] GoogleAds_add-to-cart`, `_Checkout`, `_Purchase`, `_lead` |
| Meta pixel | `328237602412769` | PageView, lead, add-to-cart, Checkout, Purchase |
| Meta pixel | `191084528414847` | `[PXL] Facebook_engaged-session` |

**Nenhum dos dois IDs de Google Ads corresponde à MCC `526-656-0190`**, a única a que a V4 tem
acesso. Somados aos 7 customer IDs que o GA4 revelou vinculados ao ZapImóveis, a operação de mídia
do grupo é comprovadamente muito maior do que a conta liberada, ver
[pendência 12](../PENDENCIAS.md).

E os pixels do Meta sobem de três para **cinco** distintos no grupo: `592658194155317`,
`818079879779548`, `935989184453347`, `328237602412769`, `191084528414847`.

> Cinco pixels e duas contas de conversão que não conhecemos, numa operação cuja auditoria de mídia
> paga (vi) está travada por falta de acesso. Este é o argumento concreto para o pedido: não estamos
> pedindo acesso genérico, estamos pedindo estes IDs, que aparecem no código do próprio site.

---

# Terceira rodada · 11/09/2026 · a conta Checkout Unificado entra

**Fonte:** export em JSON dos **4 contêineres** da conta `Checkout Unificado - PRO`
(`6326134112`), exportados em 11/09/2026. São todos de **espaço de trabalho**
(`containerVersionId: 0`), então vale a [ressalva 1](#ressalvas-de-leitura).

| Contêiner | ID | Superfície | Tags |
|---|---|---|---:|
| Checkout Unificado - **Master** | `GTM-NGG9336B` | carrega os três por zona | 4 |
| Checkout Unificado - **OLX** | `GTM-K4WBMGQV` | `pagamento.olx.com.br` | 9 |
| Checkout Unificado - **Zap Imóveis** | `GTM-NKSGWD6H` | `pagamento.zapimoveis.com.br` | 9 |
| Checkout Unificado - **Viva Real** | `GTM-NRVS3M3D` | `pagamento.vivareal.com.br` | 6 |

**A hipótese do nome estava certa: é aqui que a receita é medida.** O Master distribui por
zona, uma por domínio de pagamento, e cada filho mede `page_view`, `begin_checkout` e `purchase`
da sua vertical. É a arquitetura mais limpa que apareceu no projeto até agora. E é justamente por
isso que os achados abaixo pesam: eles não descrevem legado esquecido, descrevem a construção mais
nova e mais cuidada da casa.

---

## 🔴 23. O "Checkout Unificado" escreve em três propriedades diferentes do GA4

| Contêiner | Measurement ID |
|---|---|
| Checkout Unificado - OLX | `G-50C013M2CC` |
| Checkout Unificado - Zap Imóveis | `G-6TV9FSHYVM` |
| Checkout Unificado - Viva Real | `G-59PP1FKKEN` |

O checkout é unificado no código e **fragmentado na medição**. `G-50C013M2CC` é a propriedade
**OLX App + Web** (`152644854`), a mesma dos cinco contêineres da conta `94905`. As outras duas não
foram identificadas: a API de dados não resolve measurement ID para propriedade, e a tela de fluxos
de dados exige Administrador, que o lote de 10/09 não concedeu.

**Consequência para o método.** Não existe uma propriedade onde a receita B2B do grupo apareça
somada. Qualquer total de `purchase` do anunciante profissional é, hoje, a soma manual de três
relatórios, feita por alguém que saiba que as três existem. É a **Trava de Cegueira na sua forma
mais cara**: o número existe, está certo em cada pedaço, e não há lugar onde ele seja um número só.

**A confirmar:** quais propriedades são `G-6TV9FSHYVM` e `G-59PP1FKKEN`, e se alguma consolidação
(BigQuery, roll-up, Looker) já resolve isso fora do GA4.

## 🔴 24. Dois esquemas de dataLayer incompatíveis, dentro da mesma conta

| | Checkout OLX | Checkout Zap e Viva Real |
|---|---|---|
| Valor da transação | `value` | `ecommerce.value` |
| Item | `items.0.item_id` | `ecommerce.items.0.item_id` |
| Transação | `transaction_id` | `ecommerce.transaction_id` |
| Variáveis de dataLayer | 28 | 17 |

O checkout OLX lê o dataLayer **na raiz**; Zap e Viva Real leem **sob `ecommerce`**, que é a
convenção do próprio GA4. São dois contratos de dados diferentes para o mesmo produto, na mesma
conta, mantidos pela mesma equipe.

**Consequência:** qualquer trabalho de consolidação das três verticais precisa de uma camada de
tradução que hoje não existe em lugar nenhum. E o lado que segue a convenção do Google é o de
Imóveis, não o da OLX.

## 🔴 25. O checkout OLX não envia `seller_category`, que é a chave que separa profissional de particular

Nos três contêineres existe a variável `[VAR] dataLayer - seller_category`. A diferença está em
quem a envia:

| | Como as tags GA4 mandam parâmetro | `[VAR] GA4 - Event Settings` é usada por | `seller_category` chega ao GA4 |
|---|---|---|---|
| Zap Imóveis | variável compartilhada | **3 tags** | ✅ |
| Viva Real | variável compartilhada | **3 tags** | ✅ |
| **OLX** | **tabela inline em cada tag** | **0 tags** | 🔴 **não** |

No contêiner do OLX a variável de Event Settings **está montada, inclui `seller_category`, e não é
referenciada por tag nenhuma**. As três tags GA4 montam a própria tabela de parâmetros, e nessa
tabela `seller_category` não entra.

**Consequência, e ela é direta sobre o escopo contratado:** no checkout da OLX não há como separar,
dentro do GA4, a compra do **anunciante profissional** da compra do particular. O contrato é sobre
receita B2B. Do lado Imóveis o recorte existe; do lado OLX, não.

## 🔴 26. E-mail e telefone do usuário vão para o GA4 como propriedades de usuário

Só no contêiner do OLX, na tag `24 [TAG] GA4 - page_view`:

```
userProperties: user_email, user_id, user_logged_in, user_phone, user_zip_code
```

Os valores vêm direto do dataLayer, **sem hash e sem transformação**. `user_email` e `user_phone`
são dado pessoal identificável, e mandá-los ao GA4 como propriedade de usuário viola a política do
próprio Google, além de ser matéria de LGPD.

Isso **não** é o mesmo que o achado 16: lá era rastro de dado pessoal em cookie de terceiro. Aqui é
envio explícito, nomeado, para a propriedade GA4 da OLX, na página de pagamento.

**É achado para levar à OLX com o jurídico deles na sala**, junto com o achado 28. Não é decisão da
V4, e não deve ser corrigido por ninguém antes de a OLX saber que existe.

## 🔴 27. Toda a medição Braze do checkout dispara sobre um SDK que nunca foi inicializado

| Contêiner | Tag de Braze | Estado |
|---|---|---|
| Master | `23 [TAG] Braze - Initalization - Checkout Unificado` | 🔴 **pausada** |
| OLX | `39 Purchase` · `40 Begin Checkout` | ativas |
| Zap Imóveis | `38 Purchase` · `39 Begin Checkout` | ativas |
| Viva Real | `32 Begin Checkout` · `33 Purchase` | ativas |

A tag de inicialização é a **única** da conta que carrega o SDK do Braze, e está pausada. As **seis**
tags de ação continuam ativas nos três filhos. O template do Braze, quando não encontra o SDK,
registra no console e **segue chamando mesmo assim**: o evento não chega a lugar nenhum, e a
interface do GTM não acusa erro.

**Consequência:** as seis tags parecem cobertura de CRM sobre o checkout, e não são. É o mesmo
padrão do [achado 14](#-14-toda-a-stack-braze-está-pausada) na conta `94905`, agora na conta nova.
Duas contas, mesma decisão, e em nenhuma das duas alguém desligou o que dependia do que foi pausado.

> O nome da tag está grafado `Initalization`. É detalhe, mas entra no mesmo inventário do achado 9,
> das duas grafias de `plano-profissional`: a taxonomia não tem revisão.

## 🔴 28. O consent mode encenado foi replicado na conta nova, não herdado dela

A tag `10 [TAG] Adopt - OLX - Tag Initialization` do Master é **o mesmo código** do achado 2, na
conta `94905`:

```html
<style> button#adopt-reject-all-button { display: none !important; } </style>
<script> setTimeout(loadScript, 4000); </script>
```

E a tag `8 [TAG] AdOpt - Consent Initialization` declara, na tabela `GCMDefaults`, **`granted` nos
sete tipos de consentimento**, tanto na linha da região `BR` quanto na linha padrão. O template da
galeria traz como valor de fábrica `analytics_storage: granted` e **todo o resto `denied`**: o
`granted` geral foi digitado, não é o default.

**Por que isso é pior do que o achado 2, e não igual.** Em 02/09 dava para ler o achado 2 como
herança de um contêiner antigo que ninguém revisou. Esta conta é a mais nova do grupo, foi montada
com zonas, um contêiner por vertical e consent trigger próprio. **O padrão foi copiado para dentro
do trabalho mais cuidadoso da casa.** Deixa de ser descuido pontual e vira o que o método chama de
política implícita.

Some-se a isso: **todas as tags GA4 e Braze dos três filhos estão com `consentStatus: NOT_SET`**.
A única tag do conjunto que declara depender de consentimento é a `Meta - Base Code`, em OLX e Zap.

## 🟠 29. O Meta mede só Autos no checkout OLX, e não mede nada no Viva Real

| Contêiner | Pixel | O que o Meta recebe |
|---|---|---|
| OLX | `1492901718177368` | **só Autos**: os gatilhos 34 e 37 filtram `item_id` por `.*(MOTORCYCLES\|VEHICLES).*` |
| Zap Imóveis | `328237602412769` | InitiateCheckout e Purchase, sem filtro de categoria |
| Viva Real | - | 🔴 **nenhuma tag de Meta** |

O pixel do checkout OLX é `1492901718177368`, que **não está entre os cinco** já mapeados. São
**seis** pixels distintos conhecidos no grupo. E a variável que o guarda se chama
`[VAR] Meta - Pixel ID - Autos`, o que sugere que a instrumentação do checkout OLX nasceu de um
projeto de Autos e ficou como está.

**Insumo direto do diagnóstico (vi) Mídia Paga:** a otimização de campanha do Meta no checkout vê
Autos inteiro, Imóveis pela metade e Viva Real nada. Qualquer leitura de ROAS por vertical herda
esse recorte.

## ✅ 30. Contraponto: aqui o `purchase` está no gatilho certo

Nos três filhos, a tag de `purchase` dispara em um gatilho `[AC] purchase` que escuta o evento
`purchase`, e a de `begin_checkout` em um gatilho que escuta `begin_checkout`. Sem cruzamento.

Isso **não absolve** o [achado 1](#-1-o-evento-purchase-do-ga4-é-disparado-pelo-gatilho-de-begin_checkout):
`GTM-KGFGVFC` cobre outra superfície (`planoprofissional`, `adquirir`, `pointsofsales`,
`goldpayments`, `planos`), e lá a tag `426` continua apontando para o gatilho de `begin_checkout`.
O que este achado estabelece é **de que tamanho é o problema**: não é a casa inteira medindo errado,
é uma superfície medindo errado enquanto a vizinha mede certo, sem ninguém entre as duas.

## 🟠 31. O `page_view` do checkout OLX escuta dois eventos diferentes

`24 [TAG] GA4 - page_view` dispara nos gatilhos **5** (`customPageview`) **e 41** (`page_view`).
Zap e Viva Real disparam só em `customPageview`.

Se a página empurrar os dois eventos, o `page_view` do checkout OLX conta em dobro, e o denominador
de conversão do checkout cai pela metade. **A confirmar no Preview do GTM**, que é a mesma ressalva
do achado 11.

---

## O que a terceira rodada muda na leitura da trava

A conta `Checkout Unificado - PRO` era a aposta de maior valor da coleta, e ela entrega as duas
coisas ao mesmo tempo: **a melhor arquitetura de medição do grupo** e **a repetição integral dos
problemas de governança** já encontrados na conta legada.

Isso reforça, e agora com prova em duas contas independentes, a política implícita já escrita:

> *A medição é responsabilidade de quem implementa cada superfície, não de quem responde pela
> receita.*

O que a terceira rodada acrescenta é o **contrafactual**: quando a mesma casa monta do zero, com
tempo e com cuidado, ela produz zonas limpas, um contêiner por vertical e gatilhos corretos, **e
ainda assim** três propriedades de GA4, dois esquemas de dataLayer, consentimento concedido por
padrão e seis tags disparando sobre um SDK desligado. Não falta capacidade técnica. Falta alguém
encarregado de conferir se o número que sai corresponde ao negócio.

---

# Quarta rodada · 11/09/2026 · o parque inteiro entra

**Fonte:** export em JSON dos **60 contêineres** das quatro contas de GTM, o inventário completo do
grupo, conferido contra a API de administração do GA4 na mesma data. As três primeiras rodadas
cobriram 15 contêineres. Esta cobre os **45 restantes**.

| | Rodadas 1 a 3 | **Agora** |
|---|---:|---:|
| Contêineres | 15 | **60** |
| Tags | 367 | **1.779** |
| Tags pausadas | 93 | **275** |
| Gatilhos | 295 | **1.634** |
| Variáveis | 668 | **4.711** |

> **Método.** As evidências foram extraídas por
> [`analisa_gtm.py`](../.claude/scripts/analisa_gtm.py), que lê cada export e levanta measurement ID,
> consentimento, evento declarado contra evento escutado pelo gatilho, e higiene. O script não julga:
> cada achado abaixo foi conferido tag a tag no export antes de ser escrito. **Dois candidatos caíram
> na conferência** e estão registrados no fim, porque saber o que foi verificado e não procede vale
> tanto quanto o que procede.

---

## 🔴 32. Os três contêineres Master do grupo concedem consentimento por padrão

O [achado 2](#-2-o-consentimento-concede-tudo-por-padrão-e-o-botão-de-recusar-está-oculto) descreveu
isso no Master da OLX. Com o parque inteiro na mão, o padrão aparece inteiro, e ele é pior do que
parecia.

`setDefaultConsentState` aparece em **26 contêineres**. Em 22 deles o padrão é o correto: tudo
`denied`, menos `security_storage`. Em **quatro** está tudo `granted`:

| Contêiner | ID | Conta | O que é |
|---|---|---|---|
| OLX - Container Master | `GTM-546N2JV` | `94905` | **Master da OLX** |
| 1. ZapImóveis - Container MASTER | `GTM-W662TWW` | `2971905372` | **Master do ZapImóveis** |
| 1. VivaReal - Container MASTER | `GTM-TWSJ9VM` | `4412254379` | **Master da VivaReal** |
| OLX - Teste Adopt | `GTM-PQTNMNM3` | `94905` | contêiner de teste, ativo |

**Os três são os Masters das três verticais.** Não é um contêiner desviado: é exatamente o contêiner
que carrega os outros, em cada vertical, que concede tudo por padrão. Os 22 que trazem a versão
íntegra são os contêineres carregados, e nenhum deles instancia o template.

A leitura muda de escala. O que na primeira rodada era "o Master da OLX está com o consentimento
encenado" agora é: **as três verticais do grupo concedem consentimento por padrão, cada uma pelo seu
Master, e a versão correta do template está presente em todo lugar onde não roda.**

Isso reforça, e agora em três contas independentes, a política implícita já escrita: a medição é
responsabilidade de quem implementa cada superfície. O template correto circulou. Quem tinha o poder
de fazê-lo rodar, editou para `granted`.

**Correção:** trocar o padrão para `denied` nos quatro, e fazer a atualização de consentimento vir
do CMP. É uma edição em quatro contêineres, e resolve o parque.

---

## 🔴 33. Três dos quatro ambientes de QA escrevem na propriedade de produção do GA4

As contas ZapImóveis e VivaReal mantêm contêineres de homologação ao lado dos de produção, na mesma
conta. Eles não são casca: têm 47, 84, 71 e 4 tags. E três deles apontam para a **mesma propriedade
do GA4 que a produção**:

| Ambiente de QA | Tags | Escreve em | Produção equivalente | Compartilham |
|---|---:|---|---|---|
| `GTM-M6NDNP4K` · 10. ZapImóveis ANUNCIE QA | 47 | `G-6TV9FSHYVM` | `GTM-PZ733B5` | 🔴 **sim** |
| `GTM-N6JJ79TH` · 9. ZapImóveis PORTAL ZAP QA | 84 | `G-W39KX3CBHX` | `GTM-5X2LZWR` | 🔴 **sim** |
| `GTM-PNNJ4D3V` · 6. VivaReal Portal VR QA | 71 | `G-VVV61GFPY5` | `GTM-NP4HWRN` | 🔴 **sim** |
| `GTM-P4VTWPM2` · 7. VivaReal ANUNCIE QA | 4 | `G-VVV61GFPY5` | `GTM-T43B5LRJ` | não |

O contêiner de QA do ANUNCIE do ZapImóveis tem **três tags de `purchase` ativas** (198, 204 e 256),
todas com o measurement ID `G-6TV9FSHYVM` escrito direto no parâmetro, sem passar por variável. Essa
é uma stream da propriedade **GA4 ZapImóveis** (`407374944`), a mesma da produção.

**Consequência:** toda compra de teste feita em homologação entra na propriedade de produção como
receita. Não dá para saber, pelo dado, qual `purchase` do ZapImóveis é real e qual é ensaio. Isso
ataca diretamente a regra 8 do método, que exige que a receita derivada do funil bata com a declarada
dentro de 5%: **o numerador está contaminado por um volume que ninguém mede.**

**Correção:** propriedade separada para homologação, ou no mínimo um parâmetro de ambiente em toda
tag de QA, com filtro na propriedade. A primeira é a correta.

---

## 🔴 34. O `begin_checkout` do anunciante privado do ZapImóveis não dispara

Em `GTM-PZ733B5` (5. ZapImóveis - Container ANUNCIE), o gatilho **255**, chamado
`[CE] customPageView - begin_checkout - privado`, exige **cinco** condições simultâneas. Duas delas
são:

```
{{[VAR] dataLayer - page_name}} CONTAINS /anuncie-profissional/novo/autonomo/plano-contratacao/checkout
{{[VAR] dataLayer - page_name}} CONTAINS /anuncie-profissional/novo/imobiliaria/plano-contratacao/checkout
```

O GTM soma as condições de um gatilho com **E**, não com OU. `autonomo` e `imobiliaria` são caminhos
irmãos: divergem num segmento e não coexistem numa mesma string. **O gatilho não pode ser satisfeito
por nenhuma navegação possível.** Nunca disparou e nunca vai disparar.

O nome do gatilho diz `privado`, e as condições falam de `profissional`. É assinatura de duplicação:
alguém copiou o gatilho do profissional e não trocou as condições.

O mesmo erro está no gatilho **170** do contêiner de QA `GTM-M6NDNP4K`, que alimenta a tag 213,
ativa.

**Por que é crítico, e não higiene.** O `purchase` do anunciante privado **funciona**: a tag 317
dispara pelo gatilho 222, em `/anuncie-privado/plano-contratacao/finalizado`. Então, no ZapImóveis:

| Etapa do funil, anunciante privado | Mede? |
|---|---|
| `begin_checkout` | 🔴 **não** |
| `purchase` | ✅ sim |

**Há venda sem início de checkout.** A taxa de conversão de checkout do anunciante privado não é
baixa nem alta: ela é indefinida, porque o denominador é zero. Qualquer forecast que use essa taxa
está usando um número que o sistema não produz.

**Correção:** separar em dois gatilhos, um por caminho, ou trocar as duas condições `CONTAINS` por
uma `MATCH_REGEX` com alternância.

---

## 🔴 35. 114 tags ativas de Universal Analytics, numa ferramenta desligada há mais de dois anos

O [achado 6](#-6-universal-analytics-ainda-instalado-e-disparando) registrou UA sobrevivendo em um
contêiner. No parque inteiro, a conta é outra:

| | |
|---|---:|
| Tags do tipo Universal Analytics | **153** |
| Delas, **ativas** | **114** |
| Contêineres afetados | **19** de 60 |
| Propriedades UA distintas | **16** |

Os piores:

| Contêiner | Tags UA ativas |
|---|---:|
| `GTM-WGKTT96` · [OLD] OLX - Ajuda | 22 |
| `GTM-KP8QMDH` · OLX - Unbounce \| LP | 20 |
| `GTM-MVM68B5` · 4. ZapImóveis - LANDING PAGES | 13 |
| `GTM-WBBDN4W` · Conectaimobi | 12 |
| `GTM-KN3K8B8` · OLX - Hub Segurança | 8 |
| `GTM-NPQMK7P` · OLX - Projetos Especiais de Autos \| LP | 8 |

As 16 propriedades se agrupam em cinco raízes, uma por ativo: `UA-70177409` (OLX, 4 propriedades),
`UA-230770` (ZapImóveis, 7), `UA-126375` (VivaReal, 3), `UA-147552108` (2) e `UA-87467831` (1).

O Universal Analytics parou de processar dado novo em julho de 2023 nas propriedades padrão e em
julho de 2024 nas 360. **Essas 114 tags disparam, carregam script e não produzem dado em lugar
nenhum.** O custo é triplo: desempenho de página em toda a superfície do grupo, ruído que esconde o
que importa no contêiner, e, o mais caro, a aparência de que aquela superfície está medida.

**Correção:** excluir, não pausar. Pausar preserva o ruído no contêiner e mantém a ilusão de
cobertura.

---

## 🔴 36. Sete contêineres têm `G-XXXXXXXXXX` como measurement ID padrão

Sete contêineres da conta `94905` resolvem a propriedade do GA4 por tabela de consulta sobre o
hostname. Exemplo, `GTM-MXQKDG3`:

| | |
|---|---|
| Entrada | `{{Page Hostname}}` |
| Se casar com `[VAR] RegEx Para Hostname` | `G-50C013M2CC` |
| Se casar com `[VAR] RegEx Para Hostname Temporário` | `G-50C013M2CC` |
| **Se não casar com nada** | **`G-XXXXXXXXXX`** |

`G-XXXXXXXXXX` é o placeholder da documentação do Google. Não é uma propriedade: é a string que se
digita quando ainda não se sabe o ID.

**O problema não é o placeholder, é a direção da falha.** Quando o hostname não casa, a tag **não
deixa de disparar**: ela dispara com um ID inválido. O GA4 descarta o hit, o navegador não acusa
nada, o contêiner não registra erro. **A perda é silenciosa e não tem contador.**

E a regex é estreita de propósito. A de `GTM-MXQKDG3` é:

```
^(www[.])?(?!lp[.])(([a-z][a-z]|comprasegura|conta|planoprofissional)[.])?olx[.]com[.]br$
```

O `(?!lp[.])` exclui explicitamente os subdomínios de landing page. Qualquer hostname fora dessa
lista, incluindo um domínio novo de campanha, cai no padrão e mede no vazio até alguém reparar.

Contêineres com esse padrão: `GTM-MXQKDG3`, `GTM-TNX8FDS`, `GTM-KCCPDZV`, `GTM-MVQWQJFB`,
`GTM-NPQMK7P`, `GTM-PP7ZQJD`, `GTM-PWP7Z4C`.

**Correção:** o valor padrão da tabela deve ser vazio, e a tag deve ter uma exceção que a impeça de
disparar sem ID. Falhar fechado, e não aberto para o vazio.

---

## 🔴 37. As landing pages B2B medem na propriedade cega, e quatro streams estão fora do alcance da V4

Cruzando os 16 measurement IDs do parque com a API de administração do GA4, em 11/09:

| Measurement ID | Propriedade | ID | Contêineres |
|---|---|---|---:|
| `G-50C013M2CC` | OLX App + Web | `152644854` | 23 |
| `G-W39KX3CBHX` | GA4 ZapImóveis | `407374944` | 8 |
| `G-ZBYP2KJ7L9` | **GA4 ZapImóveis + VivaReal** | `494455315` | 4 |
| `G-6TV9FSHYVM` | GA4 ZapImóveis | `407374944` | 4 |
| `G-VVV61GFPY5` | GA4 VivaReal | `407391347` | 3 |
| `G-59PP1FKKEN` | GA4 VivaReal | `407391347` | 3 |
| `G-FFM6R038BL` | **GA4 Grupo OLX** | `503925542` | 2 |
| `G-9M01VVDZJF` | ANAPRO | `469847974` | 1 |
| `G-BXPE27834L` · `G-NBBQMWSXTE` | GA4 ZapImóveis | `407374944` | 1 cada |
| `G-6FL09MRR02` | GA4 VivaReal | `407391347` | 1 |
| `G-SP7M9MSCB3` · `G-28CQ5W5559` · `G-XWEMHMPHXB` · `G-CLVJ1JLDJF` | 🔴 **não estão entre as 71 propriedades visíveis** | - | 6 |

Três leituras saem daí.

**Uma: a propriedade cega recebe justamente a superfície B2B.** `G-FFM6R038BL` é a **GA4 Grupo OLX**
(`503925542`), a única do grupo no tier gratuito e com **zero evento-chave**
([PENDENCIAS 13](../PENDENCIAS.md)). Quem escreve nela: `OLX - Site Institucional` (`GTM-KGMSNP6`) e
`OLX - Unbounce | LP` (`GTM-KP8QMDH`), que é o contêiner das landing pages de campanha, com 40 tags.
**A captação B2B mede na propriedade onde ninguém definiu o que é conversão.**

**Duas: existe uma arquitetura de escrita dupla, e ela é deliberada.** As tags dos portais vêm em
pares nomeados `[GA4 - Verticalizado]` e `[GA4 - Unificado]`, com os mesmos gatilhos, escrevendo em
`G-W39KX3CBHX` (GA4 ZapImóveis) e `G-ZBYP2KJ7L9` (GA4 ZapImóveis + VivaReal). Isso **não** é dupla
contagem dentro de uma propriedade, e corrige a leitura do
[achado 20](#-20-generate_lead-é-contado-duas-vezes-em-duas-propriedades): é escrita paralela
intencional. Mas significa que **qualquer soma entre propriedades do grupo conta o mesmo lead duas
vezes**, e que a propriedade Unificada existe sem ter sido citada em nenhum documento de onboarding.

**Três: seis contêineres escrevem em quatro streams que a V4 não enxerga.** `G-SP7M9MSCB3` (em
3 contêineres, ZAP e VIVA), `G-28CQ5W5559`, `G-XWEMHMPHXB` e `G-CLVJ1JLDJF`. Parte da medição do
grupo sai para propriedades fora do acesso concedido, e a auditoria não alcança o destino.

**Ação:** pedir acesso às quatro, ou a confirmação de que foram descontinuadas. Entra em
`PENDENCIAS`.

---

## 🟠 38. Quatro gatilhos são logicamente impossíveis, e dois estão em produção

Além dos gatilhos 255 e 170 do [achado 34](#-34-o-begin_checkout-do-anunciante-privado-do-zapimóveis-não-dispara):

| Contêiner | Gatilho | Exige, ao mesmo tempo | Tag dependente |
|---|---|---|---|
| `GTM-WGKTT96` · [OLD] OLX - Ajuda | `375` · All pages - Blue Tags | `pageType` EQUALS `listing` **e** EQUALS `ad_detail` | `376` Blue Tags, **ativa** |
| `GTM-MKTZ2ZP` · 3. ZapImóveis CLICKSTREAM | `1225` · nonSinglePageApplicationRoutes | `Page Path` EQUALS `/` **e** EQUALS `/zapwaymais/` **e** CONTAINS mais três caminhos | nenhuma |

Uma variável não tem dois valores ao mesmo tempo. A tag `376` está ativa, marcada como disparando em
todas as páginas pelo nome, e não dispara em nenhuma.

Foram testados os 1.634 gatilhos do parque. Outros 15 candidatos apareceram e **foram descartados na
conferência**, porque as condições eram compatíveis: em `/autos-e-pecas/pecas-e-acessorios/`, por
exemplo, a URL contém as duas strings, e o E está correto.

---

## 🟠 39. O maior contêiner do parque é o que está marcado como legado

`GTM-WGKTT96`, chamado **`[OLD] OLX - Ajuda`**, tem **209 tags**, mais que qualquer outro contêiner
das quatro contas. O segundo é o `OLX - Buyer Journey`, com 124.

| | |
|---|---:|
| Tags | 209 |
| Pausadas | 59 |
| **Ativas** | **150** |
| Tags UA ativas | 22 |
| Propriedades UA | 3 |
| Gatilhos impossíveis | 1 |

Ele convive com `GTM-5VJJT94P` (`OLX - Central de Ajuda`, 2 tags) e `GTM-TW8N3LN` (`OLX - Chat`,
2 tags). O prefixo `[OLD]` sugere que a superfície foi reconstruída e o contêiner antigo ficou.
**Mas 150 tags ativas não são um contêiner desligado.**

Não dá para decidir isso pelo export: depende de o contêiner ainda estar instalado em alguma página.
É o tipo de pergunta que a versão publicada e um teste no Preview respondem em minutos.

---

## 🟠 40. O contêiner `OLX - Testes de SDK` está ativo, com o measurement ID por preencher

`GTM-TQHV6TD` tem 4 tags, nenhuma pausada:

| Tag | Tipo | Aponta para |
|---|---|---|
| `5` · [TAG] GA4 - Settings & Page View | Google tag | `{{[VAR] GA4 - G-XXXXXXXXXX}}` |
| `9` · [TAG] GA4 - Generic Event | GA4 evento | `{{[VAR] GA4 - G-XXXXXXXXXX}}` |
| `7` · [TAG] GAU - Page View | Universal Analytics | - |
| `14` · [TAG] GAU - Generic Event | Universal Analytics | - |

Aqui o placeholder não é valor padrão de tabela: é o valor de uma **constante**, e a variável foi
batizada com o próprio placeholder. Duas tags de GA4 apontam para um ID que não existe, e as outras
duas para uma ferramenta desligada. O contêiner mede exatamente nada, e está no ar.

---

## 🟡 41. Quatro contêineres vazios, dois deles marcados `(WIP)`

| Contêiner | ID | Tags | Gatilhos | Variáveis |
|---|---|---:|---:|---:|
| `[New] iOS Tracking` | `GTM-T8ZBL8Z` | 0 | 1 | 0 |
| `VivaReal - Container BLOG (WIP)` | `GTM-5DV89XS` | 0 | 0 | 0 |
| `ZapImóveis - Container BLOG (WIP)` | `GTM-NWPXB4X` | 0 | 0 | 0 |
| `Sympla - Conectalmobi - Iframe Checkout` | `GTM-TCG3ML4` | 0 | 0 | 0 |

Contêiner vazio não mede errado, não mede. O que merece nota é o par `[New] Android Tracking`
(`GTM-52W35LS`, **1 tag**) e `[New] iOS Tracking` (**0 tags**): os dois contêineres criados para o
rastreamento de aplicativo estão praticamente vazios, e o prefixo `[New]` indica intenção recente.

E `Sympla - Conectalmobi - Iframe Checkout` é o quarto contêiner com a palavra checkout no nome, sem
nenhuma tag dentro.

---

## Dois candidatos que a conferência derrubou

**O `purchase` em `customPageView` do ZapImóveis não é o achado 1 de novo.** As tags 220 e 256 de
`GTM-PZ733B5` e `GTM-M6NDNP4K` disparam `purchase` num gatilho de `customPageView`, o que à primeira
vista repete o erro mais grave da primeira rodada. **Não repete.** O gatilho 226 exige, junto com o
`customPageView`, que `pageInfo.pageName` contenha `/zapimoveis/anuncie/finalizado`. É a página de
confirmação. Disparar a compra no pageview da página de obrigado é padrão correto quando não há
evento dedicado. Fica registrado como verificado e limpo.

**Não há PII nova comprovada nos 45 contêineres.** A varredura por `email`, `phone` e `cpf` acusou
dezenas de ocorrências, mas a conferência mostrou que quase todas são **nomes de variável de
dataLayer**, não valor enviado a plataforma. O [achado 26](#-26-e-mail-e-telefone-do-usuário-vão-para-o-ga4-como-propriedades-de-usuário),
que tem evidência de envio real, continua sendo o único achado de PII da auditoria.

---

## O que a quarta rodada muda na leitura da trava

As três primeiras rodadas descreveram um sistema que mede errado em pontos específicos. A quarta
mostra que **os pontos específicos são o sistema**.

O dado decisivo é o do [achado 32](#-32-os-três-contêineres-master-do-grupo-concedem-consentimento-por-padrão).
O template correto de consentimento está em 22 contêineres. O template editado para `granted` está em
quatro, e **três deles são os Masters das três verticais**, isto é, exatamente os contêineres que
rodam. Isso não é distribuição aleatória de erro: é o mesmo desvio, tomado três vezes, por três times
diferentes, em três contas separadas, sempre no ponto de maior alcance.

A política implícita já escrita nas rodadas anteriores se confirma com prova em quatro contas:

> *A medição é responsabilidade de quem implementa cada superfície, não de quem responde pela
> receita.*

E a quarta rodada acrescenta o **custo acumulado** dessa política, que agora dá para somar:

| O que | Quanto |
|---|---|
| Tags ativas de uma ferramenta desligada há 2 anos | **114** |
| Contêineres cujo ID padrão de medição é um placeholder | **7** |
| Ambientes de homologação escrevendo na propriedade de produção | **3** |
| Etapas de funil B2B que não disparam | **1**, o `begin_checkout` do privado no ZapImóveis |
| Streams de GA4 fora do alcance da auditoria | **4** |
| Propriedades GA4 distintas recebendo dado do parque | **8** identificadas, mais 4 não identificadas |

Nenhum desses itens é difícil de corrigir isoladamente. Quatro edições de consentimento, uma limpeza
de UA, um valor padrão de tabela, um gatilho reescrito. **A dificuldade não é técnica.** Cada um
desses defeitos passou por uma pessoa que sabia fazer certo, e nenhum teve alguém encarregado de
conferir se o número que sai corresponde ao negócio. É a mesma conclusão da terceira rodada, agora
com 60 contêineres e 1.779 tags sustentando.

**Para o Comitê 1:** isto não é uma lista de correções de rastreamento. É a medida de quanto da
Trava de Cegueira é política e quanto é técnica. A resposta que o parque dá é: **quase tudo é
política.**
