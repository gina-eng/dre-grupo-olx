# Auditoria (vii) · Rastreamento Completo (GA4 e GTM)

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

1. Tudo acima é leitura de **configuração exportada** e de **contagem de eventos**, não de
   comportamento observado em navegador. Os achados 5 e 11 pedem confirmação no Preview do GTM.
2. O achado 4 cai por terra se o site gravar `user_olx` por código próprio.
3. 🔴 **A cobertura é menor do que parecia.** Em 02/09 descobriu-se que o GTM do grupo tem **quatro
   contas**, não uma: `BR - www.olx.com.br` (`94905`), `Checkout Unificado - PRO` (`6326134112`),
   `VivaReal` (`4412254379`) e `ZapImóveis` (`2971905372`), todas com selo 360. Dos 11 exports
   recebidos, **10 são da primeira conta e 1 da ZapImóveis**. As contas `Checkout Unificado - PRO` e
   `VivaReal` estão **inteiramente por auditar**, e o "22+ contêineres" registrado no checklist é o
   piso de **uma** das quatro. Foram auditados **6 de um total ainda desconhecido**, os 5 da
   primeira rodada mais o ZapImóveis ANUNCIE.
   Cinco exports já estão no repositório e ainda não foram lidos: Buyer Journey (124 tags), VAS (48),
   Unbounce LP (40), Login (5) e Wallet (3). O que está fora pode conter tanto correções quanto
   problemas equivalentes.
5. O achado 18 descreve a configuração exportada do workspace. Confirmar no site publicado se o
   banner do AdOpt de fato não aparece no domínio ZapImóveis ANUNCIE, workspace não é
   necessariamente o que está no ar.
4. Nada aqui descreve performance de negócio, descreve como a medição está montada.

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
