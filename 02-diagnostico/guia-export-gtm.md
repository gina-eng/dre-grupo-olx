# Guia de export do GTM · o que trazer e como

Aberto em **11/09/2026**, para a janela do diagnóstico **(vii) Rastreamento**, que fecha em
**15/09**. Substitui, em detalhe operacional, os blocos 0 e 1 de
[`coleta-pendente.md`](coleta-pendente.md), que continuam valendo como lista de controle.

Este guia existe porque não há conector de GTM neste ambiente. O acesso está concedido, mas a
auditoria só roda sobre o **contêiner exportado em JSON**, que é o que permite ler tag, gatilho,
variável e consent mode offline, linha a linha.

---

## Antes de tudo: os 11 exports que temos são rascunho, não o que está no ar

Conferido em 11/09, lendo o campo `containerVersionId` dentro de cada arquivo. A contagem foi
refeita ao fim do dia, depois da segunda leva:

| | |
|---|---|
| Arquivos na pasta | **62** |
| Contêineres distintos | **60** |
| Com `containerVersionId: 0` | **62**, ou seja, **todos** |
| Com versão publicada | **zero** |

O inventário saiu de 11 para 60 contêineres num único dia, e a proporção não se moveu um milímetro:
**continua sem um único export do que está no ar.** Esse é agora o único item aberto da coleta, e
ele vale mais do que os 49 contêineres que chegaram, porque sem ele nenhum dos achados fala de
produção.

`containerVersionId: 0` é a assinatura de um export de **workspace**, o rascunho em edição. A versão
publicada carrega o número da versão. Os 11 foram exportados em 01/09 pelo caminho do workspace.

**Isso não invalida os 22 achados, mas muda o que eles provam.** Hoje eles descrevem o que está
configurado no rascunho. Levar isso a comitê como "o site da OLX mede errado" é afirmar mais do que
o dado sustenta, e numa conta que compra rigor metodológico esse é o erro caro.

O caso mais sensível é o [achado 1](auditoria-vii-rastreamento.md), a tag `426 [TAG] GA4 - Purchase`
apontando para o gatilho `215`, que escuta `begin_checkout`. Se isso estiver só no workspace, é um
rascunho errado que ninguém publicou, e vira nota de rodapé. Se estiver na versão publicada, é
receita B2B medida errada em produção, e é o achado de abertura do comitê.

> **Por isso o lote 1 abaixo tem uma tarefa só, e ela vale mais que todo o resto:** trazer a versão
> **publicada** do `GTM-KGFGVFC`. São dez minutos, e decide o peso do achado mais grave da auditoria.

---

## Segunda leva de 11/09: o inventário de `94905` fechou, e a VivaReal abriu

Um lote de 31 exports foi baixado na tarde de 11/09 e triado no fim do dia. Ele resolve, **por
export em vez de por print**, boa parte do que os lotes 3 e 5 pediam:

| | |
|---|---|
| Exports triados | 31 |
| Contêineres inéditos | **17** |
| Já tínhamos, sem nada novo dentro | 12 |
| Mesmo rascunho, conteúdo alterado desde 01/09 | **2** |

**A conta `94905` subiu de 10 para 26 contêineres**, o que transforma o "22 é piso, não total" do
lote 5 num inventário que se pode tratar como fechado. Entre os inéditos:

| Contêiner | ID | Tags | Por que importa |
|---|---|---|---|
| `[OLD] OLX - Ajuda` | `GTM-WGKTT96` | **209** | O maior da conta inteira, e o nome diz `[OLD]`. Legado vivo ou casca? |
| `OLX - LPs` | `GTM-PZ83VMV` | 20 | Landing pages, superfície de captura do bloco I |
| `OLX - Projetos Especiais de Autos \| LP` | `GTM-NPQMK7P` | 29 | LP de autos, vertical do escopo |
| `OLX - RD Station \| LP` | `GTM-MVQWQJFB` | 15 | Segundo CRM no rastreamento, ao lado do que já apareceu |
| `[New] Android Tracking` | `GTM-52W35LS` | 1 | Contêiner de app com **uma** tag |
| `[New] iOS Tracking` | `GTM-T8ZBL8Z` | **0** | Contêiner de app com **nenhuma** tag |

E a conta **VivaReal** (`4412254379`), que nunca tinha aparecido, entregou o primeiro:
`GTM-TWSJ9VM · 1. VivaReal - Container MASTER`, 7 tags. **O prefixo `1.` é a mesma convenção de
lista numerada do `5. ZapImóveis - Container ANUNCIE`**, então há pelo menos mais quatro ali.

### O que mudou nos rascunhos entre 01/09 e 11/09

Dos 12 contêineres reexportados, **10 estão idênticos** fora do `fingerprint`. Dois mudaram, e a
mudança foi conferida entidade por entidade:

| Contêiner | Mudança | Toca a receita? |
|---|---|---|
| `GTM-546N2JV` · Container Master | tag `171`, `[TAG] Adopt`, script reescrito | não |
| `GTM-TNX8FDS` · Buyer Journey | variável `1658` `subCategoryId` criada, `1404` ajustada | não |

**Nenhuma toca `purchase` ou `begin_checkout`.** Os 22+ achados escritos sobre os exports de 01/09
seguem válidos no que descrevem. Os dois retratos datados ficam lado a lado na pasta, de propósito,
porque provam que os rascunhos são editados durante a auditoria.

---

## Terceira leva de 11/09: as duas verticais B2B fecham, e a coleta acaba

O operador varreu as quatro contas e entregou os exports organizados em pasta por conta. **28
contêineres inéditos**, todos das duas contas que faltavam.

### VivaReal (`4412254379`): 11 contêineres

A numeração vai de `1.` a `8.`, mais três fora da série.

| Contêiner | ID | Tags |
|---|---|---:|
| 3. VivaReal - Container CLICKSTREAM | `GTM-TRGML4R` | 99 |
| 2. VivaReal - Container Portal VR | `GTM-NP4HWRN` | 98 |
| 6. VivaReal - Container Portal VR - Ambiente QA | `GTM-PNNJ4D3V` | 71 |
| Conectaimobi | `GTM-WBBDN4W` | 31 |
| 4. VivaReal - Container BLOG | `GTM-5RPFK7Z` | 16 |
| 5. VivaReal - Container ANUNCIE | `GTM-T43B5LRJ` | 14 |
| 1. VivaReal - Container MASTER | `GTM-TWSJ9VM` | 7 |
| 7. VivaReal - Container ANUNCIE - Ambiente de QA | `GTM-P4VTWPM2` | 4 |
| 8. VivaReal - Container Checkout | `GTM-TXJVLXSJ` | 3 |
| Sympla - Conectalmobi - Iframe Checkout | `GTM-TCG3ML4` | **0** |
| VivaReal - Container BLOG (WIP) | `GTM-5DV89XS` | **0** |

### ZapImóveis (`2971905372`): 19 contêineres

A numeração vai de `1.` a `12.`, mais sete fora da série. O `5. ANUNCIE` que já tínhamos era, de
fato, o quinto de doze.

| Contêiner | ID | Tags |
|---|---|---:|
| 3. ZapImóveis - Container CLICKSTREAM | `GTM-MKTZ2ZP` | 129 |
| 2. ZapImóveis - Container PORTAL ZAP | `GTM-5X2LZWR` | 127 |
| 9. ZapImóveis - Container PORTAL ZAP - Ambiente QA | `GTM-N6JJ79TH` | 84 |
| 4. ZapImóveis - Container LANDING PAGES | `GTM-MVM68B5` | 62 |
| 5. ZapImóveis - Container ANUNCIE | `GTM-PZ733B5` | 48 |
| 10. ZapImóveis - Container ANUNCIE - Ambinete QA | `GTM-M6NDNP4K` | 47 |
| Guia de Bairros | `GTM-5PNSC98` | 25 |
| 7. ZapImóveis - Container BLOG | `GTM-PBZ477K` | 21 |
| Rede Zap | `GTM-N87GJJD` | 13 |
| www.datazap.com.br | `GTM-PQDRHQM` | 12 |
| 1. ZapImóveis - Container MASTER | `GTM-W662TWW` | 10 |
| LP - Zapfin | `GTM-MFKXMNK` | 9 |
| meuzap.zapimoveis.com.br | `GTM-M23NB5R` | 7 |
| 8. Conecta Imobi | `GTM-NBKDVZ6W` | 5 |
| 6. ZapImóveis - Container DATAZAP/GEOIMOVEL | `GTM-MQSQ9JW` | 4 |
| 11. Zapimovéis - Container Anapro | `GTM-WHJZKXFC` | 4 |
| 12. ZapImóveis - Container Checkout | `GTM-TMXMHKBJ` | 3 |
| 2. ZapImóveis - Container PORTAL ZAP [Lead Only] | `GTM-T8PDZ2MS` | 1 |
| ZapImóveis - Container BLOG (WIP) | `GTM-NWPXB4X` | **0** |

### O que a terceira leva muda para a coleta

**Um: o lote 3 está fechado, e com ele a coleta de inventário.** As quatro contas foram varridas. O
que resta é uma coisa só, a mesma de sempre: **a versão publicada**.

**Dois: a pergunta do checkout ficou maior.** Existem agora **quatro contêineres de checkout** em
três contas diferentes, e nenhum deles é o `Checkout Unificado`:

| Contêiner | Conta | Tags |
|---|---|---:|
| `OLX - Checkout` (`GTM-M4TL57GX`) | `94905` | 4 |
| `8. VivaReal - Container Checkout` (`GTM-TXJVLXSJ`) | `4412254379` | 3 |
| `12. ZapImóveis - Container Checkout` (`GTM-TMXMHKBJ`) | `2971905372` | 3 |
| `Sympla - Conectalmobi - Iframe Checkout` (`GTM-TCG3ML4`) | `4412254379` | **0** |

Contra os quatro da conta `Checkout Unificado - PRO`, que têm 4, 9, 9 e 6 tags. **Qual desses mede o
checkout que está no ar?** É a mesma pergunta do lote 2, agora multiplicada por três verticais, e é
a versão publicada que responde.

**Três: ambiente de QA convive com produção na mesma conta**, com 71 e 84 tags. Anotado para a
auditoria, não muda a coleta.

---

## Confirmado por imagem em 11/09: são quatro contas, todas 360

A tela de Contas do Gerenciador de Tags foi capturada em 11/09, sob a organização
**OLX / BOM NEGOCIO ATIVIDADES DE INTERNET LTDA**. Ela confirma visualmente o que o Bloco 0 de
[`coleta-pendente.md`](coleta-pendente.md) tinha registrado em 02/09 a partir de uma captura
cortada:

| Conta | ID | Selo | Em 01/09 | **Hoje** |
|---|---|---|---:|---:|
| BR - www.olx.com.br | `94905` | 360 | 10 | **26** |
| Checkout Unificado - PRO | `6326134112` | 360 | 0 | **4** |
| VivaReal | `4412254379` | 360 | 0 | **11** |
| ZapImóveis | `2971905372` | 360 | 1 de N | **19** |
| | | | **11** | **60** |

**Quatro contas, nenhuma a mais.** O escopo da auditoria (vii) está fechado no nível de conta, e
**desde 11/09 também no nível de contêiner**: as quatro foram varridas e entregaram 60 contêineres.

> **A coluna Contêineres apareceu vazia porque nenhuma conta estava selecionada.** Esclarecido pelo
> operador em 11/09, junto com o fato que reorganiza esta coleta: **cada uma das quatro contas tem
> muitos contêineres**.

### Por isso a coleta é em duas etapas, e não em bloco

Exportar contêiner a contêiner em três contas cheias não cabe na janela que fecha em **15/09**, e
não é necessário: a auditoria não precisa de todos, precisa **dos que tocam a receita B2B**.

| Etapa | Quem faz | Custo |
|---|---|---|
| **1 · a lista** | operador: um print da lista de contêineres de cada conta | 3 cliques |
| **2 · a seleção** | V4: leio os nomes e devolvo a lista nominal do que exportar | - |
| **3 · o export** | operador: só os contêineres nomeados, versão publicada | proporcional à lista |

O nome do contêiner é informativo o bastante para escolher: foi assim que `Planos Profissionais &
PAYG`, `Seller Journey` e `Checkout` saíram dos 22 da primeira conta, e nenhum dos três foi escolha
errada.

> **A etapa 1 é o gargalo de tudo que vem depois.** Enquanto a lista não existe, o único item
> executável desta coleta é o lote 1.

## O caminho, uma vez

Vale para todo contêiner desta lista.

1. Abrir <https://tagmanager.google.com> com a conta que recebeu o acesso.
2. No seletor de conta, no topo, **escolher a conta certa**. São quatro, e a tela abre na última
   usada. O nome e o ID de cada uma estão nos lotes abaixo.
3. Abrir o contêiner.
4. Menu **Administrador**, na barra superior.
5. Na coluna do **contêiner**, à direita, clicar em **Exportar contêiner**.
6. Vai aparecer uma lista com os **espaços de trabalho** em cima e as **versões** embaixo.
   **Marcar a versão publicada**, que é a que aparece com o selo de publicada ou ativa, e **não** o
   espaço de trabalho.
7. Clicar em **Exportar**. O navegador baixa um `.json`.

> **Se o contêiner nunca foi publicado**, não vai existir versão. Nesse caso exporte o espaço de
> trabalho mesmo e avise: "este não tem versão publicada". Isso não é falha de coleta, é achado.

**Onde salvar:**

| O que | Pasta |
|---|---|
| Os `.json` | `assets/originais/H-rastreamento-gtm/` |
| Os prints de tela | `assets/originais/H-rastreamento-gtm/telas/` |

**Não se preocupe com o nome do arquivo.** Pode largar como o navegador baixou. A identidade real
(conta, contêiner, número da versão) está dentro do JSON, e o script de conferência lê de lá e
avisa se algum arquivo estiver duplicado ou fora do lugar.

---

## Lote 1 · dez minutos, e decide o achado mais grave

Conta **`BR - www.olx.com.br`** · ID `94905`

- [ ] **`GTM-KGFGVFC` · OLX - Planos Profissionais & PAYG · versão PUBLICADA**
- [ ] **Print da aba Versões deste contêiner**, mostrando data e autor das últimas versões
  Caminho: dentro do contêiner, aba **Versões**, na barra superior. Serve para saber **desde quando**
  o `purchase` está preso ao gatilho errado, se estiver. Sem essa data não dá para dizer qual janela
  do histórico de conversão está contaminada, e o forecast depende disso.

## Lote 2 · a conta que nunca vimos, e é a de maior valor

Conta **`Checkout Unificado - PRO`** · ID `6326134112`

O nome junta as duas palavras que definem o escopo contratado: *checkout* é onde a receita
acontece, *PRO* é o anunciante profissional. Se a hipótese estiver certa, é aqui que mora a medição
da receita B2B do grupo, e o achado 1 precisa ser relido contra o que existir aqui.

- [x] **Print da lista de contêineres** ✅ **recebido em 11/09**

### São quatro, e a estrutura deles é o achado

| Ordem | Contêiner | ID |
|---|---|---|
| 1 | Checkout Unificado - **Master** | `GTM-NGG9336B` |
| 2 | Checkout Unificado - **OLX** | `GTM-K4WBMGQV` |
| 3 | Checkout Unificado - **Zap Imóveis** | `GTM-NKSGWD6H` |
| 4 | Checkout Unificado - **Viva Real** | `GTM-NRVS3M3D` |

**Um Master e uma instância por vertical.** É uma arquitetura deliberada e centralizada, exatamente
o contrário da conta `94905`, onde 22+ contêineres convivem com convenções próprias e a mesma
correção aplicada num e não no outro ([achado 1](auditoria-vii-rastreamento.md) contra o contraponto
do ZapImóveis ANUNCIE). **A capacidade de fazer certo existe na casa, e está concentrada aqui.**

Os quatro IDs têm o formato longo de 8 caracteres (`GTM-NGG9336B`), que o Google passou a emitir
depois dos de 7 (`GTM-KGFGVFC`). São contêineres **mais novos** que os auditados.

> 🔴 **O que isso levanta:** a conta `94905` tem um contêiner chamado **`OLX - Checkout`**
> (`GTM-M4TL57GX`, formato longo também, **4 tags**), auditado em 01/09. Se o checkout de verdade
> migrou para esta conta, aquele pode ser legado ou casca, e parte dos achados da primeira rodada
> descreve um contêiner que não é mais o do fluxo de receita. Só o export resolve.

- [ ] **`GTM-NGG9336B` · Master · versão publicada**
- [ ] **`GTM-K4WBMGQV` · OLX · versão publicada**
- [ ] **`GTM-NKSGWD6H` · Zap Imóveis · versão publicada**
- [ ] **`GTM-NRVS3M3D` · Viva Real · versão publicada**

São quatro exports, mesma conta, mesmo caminho. Nesta ordem: o Master carrega os outros e é onde o
consent mode costuma morar, e OLX e Zap Imóveis são as duas verticais B2B do escopo contratado.

## Lote 3 · fecha as duas verticais B2B

Conta **`ZapImóveis`** · ID `2971905372`

Temos um contêiner só, o `5. ZapImóveis - Container ANUNCIE`. O prefixo `5.` indica lista numerada,
então provavelmente existem ao menos cinco.

- [x] ~~Print da lista de contêineres desta conta~~ ✅ **resolvido por export em 11/09**
- [x] ~~Exportar o que a V4 nomear~~ ✅ **os 19 vieram**, o `5. ANUNCIE` era o quinto de doze

Conta **`VivaReal`** · ID `4412254379`

Terceira vertical. O V4MOS ingere a MCC VivaReal (`526-656-0190`), esta é a contraparte de medição
dela. **Deixou de ser inédita em 11/09**, com a chegada de
`GTM-TWSJ9VM · 1. VivaReal - Container MASTER` (7 tags, rascunho).

O prefixo `1.` repete a convenção de lista numerada do ZapImóveis, então o Master é o primeiro de
uma série, e **faltam os outros**.

- [x] ~~Primeiro contêiner da conta~~ ✅ `GTM-TWSJ9VM`, recebido em 11/09
- [x] ~~Print da lista de contêineres desta conta~~ ✅ **resolvido por export em 11/09**
- [x] ~~Exportar o que a V4 nomear~~ ✅ **os 11 vieram**, numerados de `1.` a `8.`

## Lote 4 · a versão publicada dos cinco já auditados

Conta **`BR - www.olx.com.br`** · ID `94905`, e conta `ZapImóveis` no último.

Mesmo motivo do lote 1, aplicado ao resto da auditoria: separa o que está no ar do que está no
rascunho. Cada um desses já tem achado escrito contra ele.

- [ ] `GTM-546N2JV` · OLX - Container Master · **publicada**
- [ ] `GTM-MXQKDG3` · OLX - Seller Journey · **publicada**
- [ ] `GTM-M4TL57GX` · OLX - Checkout · **publicada**
- [ ] `GTM-MJX9PG4` · OLX - Conecta Autos · **publicada**
- [ ] `GTM-PZ733B5` · 5. ZapImóveis - Container ANUNCIE · **publicada** (conta `2971905372`)

## Lote 5 · fecha o inventário da primeira conta

Conta **`BR - www.olx.com.br`** · ID `94905`

- [x] ~~Print da lista completa de contêineres da conta~~ ✅ **resolvido de outro jeito em 11/09**
  A segunda leva trouxe **26 contêineres distintos** desta conta, por export e não por print. O
  inventário pode ser tratado como fechado, e o pedido de print cai.
- [ ] 🔴 **`GTM-T2H3VFL` · Google Shopping · esclarecer se ainda existe**
  Está marcado como entregue no item 1.5 de [`coleta-pendente.md`](coleta-pendente.md) e **nunca
  apareceu na pasta**. Agora que os 26 da conta estão inventariados e **ele não é nenhum deles**, a
  leitura mudou: provavelmente foi renomeado, movido de conta ou excluído. Vale um olhar na lista
  antes de exportar qualquer coisa.

---

## Quando terminar, confira antes de me chamar

Com os arquivos na pasta, rode:

```bash
python3 .claude/scripts/check_gtm_exports.py
```

Ele lê cada JSON, diz de que conta e de que contêiner é, se é **versão publicada ou rascunho**, e
lista o que ainda falta contra os cinco lotes acima. Não altera arquivo nenhum.

Para renomear os arquivos no padrão do repositório de uma vez:

```bash
python3 .claude/scripts/check_gtm_exports.py --renomear
```

---

## O que não está neste guia, e por quê

**O GA4 não entra.** Conferido por API em 11/09: as 26 propriedades continuam em `can_edit: false`,
o lote de 10/09 não elevou o nível. As telas de Administração do GA4 (fluxos de dados, retenção,
BigQuery, eventos-chave) seguem fora de alcance, e a decisão desta janela é **seguir sem elas**, com
a limitação declarada no fechamento de (vii). Ver [PENDENCIAS 13](../PENDENCIAS.md).

A mitigação é exatamente este guia: boa parte da causa mora no GTM, não no GA4, e o export em JSON
alcança tag, gatilho, variável e consent mode sem depender do nível do GA4.

> ⚠️ Os exports contêm IDs de pixel, chaves públicas de SDK e IDs de conversão. Nada disso é
> segredo, tudo aparece no código-fonte das páginas, mas o material é confidencial pelo aviso da OLX
> e não sai deste repositório privado.
