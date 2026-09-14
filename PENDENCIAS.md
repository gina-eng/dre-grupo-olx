# Pendências e Inconsistências

Registro vivo do que precisa de decisão, confirmação ou correção.
Atualizar sempre que um item for resolvido, com data e quem decidiu.

**Legenda de severidade:** 🔴 crítico (bloqueia ou expõe risco material) · 🟠 relevante · 🟡 a esclarecer

---

## 🔴 1. Divergência no valor do contrato · R$ 740k vs. R$ 752k

| Fonte | Valor |
|---|---|
| E-mail de Mirella Mendonça, 10/08/2026 | **R$ 740.000,00** |
| Contrato de Prestação de Serviços (cláusula 3.1) | **R$ 752.000,00** |

Diferença de **R$ 12.000**. O e-mail registra o valor como premissa acordada após alinhamento
interno da OLX.

**Ação:** confirmar qual valor está no instrumento efetivamente assinado. Se o contrato assinado
traz R$ 752k e a OLX registrou R$ 740k por escrito, há risco de questionamento no faturamento
do bônus (12º mês).
**Responsável:** Gustavo Figueiredo · **Prazo:** antes do kick-off (24/08)

---

## 🔴 2. Gatilho do Bônus de Sucesso: três definições incompatíveis

| Fonte | Gatilho |
|---|---|
| Contrato Grupo OLX (3.3) | "Cumprimento integral do escopo" ao término da primeira vigência |
| SOW padrão DR-E | Expansão **tecnicamente comprovada de 2 das 8 travas** em D+370 |
| E-mail Mirella (10/08) | KPIs e metodologia de mensuração **a construir a partir do diagnóstico**, formalizados por **aditivo contratual** |

São critérios materialmente distintos: "cumprir o escopo" é obrigação de meio (a V4 controla);
"expandir 2 travas" é resultado técnico (parcialmente sob controle da V4); "KPIs a definir" é
indeterminado.

**Risco:** R$ 376.000 de receita dependem de um critério que hoje admite três leituras.

**Ação:** definir o critério e formalizar por aditivo. O método é explícito sobre por que o bônus
**não** deve ser atrelado a faturamento bruto (ver
[08-economics](00-playbook/08-economics-e-entregaveis-dr-e.md#modelo-de-bônus-opção-b)), usar
esse argumento na construção dos KPIs. A arquitetura de gates (técnico, resultado e execução) e a
régua de medição estão propostas em [03-estrategia/meta-do-projeto.md](03-estrategia/meta-do-projeto.md) §7.
**Responsável:** Gustavo Figueiredo + Mirella Mendonça · **Prazo:** após o diagnóstico inicial, antes do Comitê 1

---

## 🔴 3. Janela de garantia fecha no kick-off

A cláusula 2.3 do contrato OLX define a garantia como válida **até o primeiro encontro (Comitê de
Receitas)**, que é o próprio kick-off de 24/08. Diverge da SOW padrão DR-E (60 dias).

**Implicação:** a partir do kick-off, a resilição imotivada obriga a OLX ao pagamento integral das
parcelas vincendas. A OLX precisa entender isso, e a V4 precisa que o kick-off seja irrepreensível,
porque é literalmente o único ponto de saída do cliente.

**Ação:** garantir que o material do kick-off passe pelo gate de qualidade da Matriz.
**Responsável:** Consultor + revisor independente · **Prazo:** 23/08

---

## 🟠 4. Numeração das travas: três padrões conflitantes

| Trava | Fundamentos DR-OTE | POPs / "Travas de Receita" | Fluxo de Estratégia |
|---|---|---|---|
| Exposição | T1 | Trava 7 | Trava 2 |
| Retenção | T7 | Trava 1 | Trava 8 |

Além disso, o **contrato do Grupo OLX fala em "7 travas"** enquanto o método opera com **8**
(a diferença é a Trava 0 · Cegueira, que é pré-condição, não restrição de receita).

**Risco:** material de comitê com numeração inconsistente destrói credibilidade técnica em uma
conta que compra exatamente rigor metodológico.

**Mitigação adotada neste repositório:** a trava é sempre referida **pelo nome**
("Trava de Qualificação"), nunca só pelo número. Ver
[02-travas-de-receita.md § Numeração](00-playbook/02-travas-de-receita.md#2-numeração-das-travas-atenção).

**Ação:** escalar para a Matriz para normalização do material oficial.
**Responsável:** Consultor → Coordenação PE&G

---

## 🟠 5. Escopo por unidade de negócio não delimitado

O Grupo OLX tem ao menos duas frentes com operações de mídia distintas: **Imóveis** (ZAP+, VivaReal)
e **Autos** (B2B). O contrato menciona "domínios B2B" apenas no diagnóstico (ii), CRO/SEO.

**Perguntas em aberto:**
- O DR-E cobre as duas unidades ou apenas uma?
- Se cobre as duas, o diagnóstico das travas é feito por unidade (dois sistemas de receita) ou consolidado?
- O Success Fee será medido por unidade ou no consolidado?

> Isso não é detalhe. Em TOC, **cada sistema de receita tem sua própria restrição governante**.
> Duas unidades de negócio distintas podem ter travas diferentes, e o método exige
> **uma restrição por ciclo**.

**Ação:** delimitar no kick-off e registrar em ata.
**Responsável:** Consultor + Mirella · **Prazo:** 24/08

---

## 🟠 6. Acessos bloqueados

| Item | Status |
|---|---|
| Google Drive (data room) | 🟢 **Destravado em 24/08.** Abriu com `rafael.corazza-ext@olxbr.com` e o primeiro lote já foi baixado (9 arquivos, blocos E e I). Faltam as contas de Anselmo Bueno e Guilherme Monteiro: hoje só o Rafael consegue buscar material novo lá. |
| VR09, ZAP+ MCC VivaReal (526-656-0190) | 🟢 **Aceite feito.** Ingerindo no V4MOS desde 24/08 |
| VR · ZAP+ (612188193108418) | 🟠 Pendente de aprovação (OLX), revalidado em 31/08, segue vazio |
| OLX \| Autos \| B2B (1742214902479721) | 🟠 Pendente de aprovação (OLX), revalidado em 31/08, segue vazio |
| GA4, 3 contas, 26 propriedades | 🟢 **Liberado em leitura, confirmado em 31/08.** Grupo OLX (285763706), OLX (70177409), Viva Real (126375). Nível de permissão a confirmar |
| GTM · contêineres publicados | 🟠 Sem concessão |
| Google Search Console | 🟠 Sem concessão |
| Salesforce (Marketing Cloud e CRM) | 🟠 Sem concessão |

**Atualização de 04/09.** A entrega de 03/09 não ocorreu. A nova data comprometida é **08/09**.
Se confirmada, fecha de uma vez as quatro linhas 🟠 acima, e é a premissa que sustenta o
cronograma reajustado. A conferência item a item e o risco de "concedido mas não utilizável" estão
na [pendência 18](#-18-a-entrega-de-acessos-de-0309-não-ocorreu-nova-data-é-0809).

**Ação:** conferir o lote em 08/09, abrindo cada ferramenta. Até a conferência, o que trava segue
sendo as duas contas de Meta, o GTM, o Search Console e o Salesforce.
Nos acessos que ainda dependem da OLX, pedir a concessão para `rafael.corazza-ext@olxbr.com`,
que é conta do domínio deles e não passa por aprovação de parceiro externo.
**Responsável:** equipe de operações V4 · **Prazo:** 23/08

> ⚠️ A senha da conta `@olxbr.com` chegou por e-mail e foi repassada por chat. Ela **não está neste
> repositório** e não deve entrar. Trocar no primeiro acesso, ligar 2FA e guardar no gerenciador de
> senhas da V4. Enquanto as outras 2 contas não saírem, o acesso ao data room é um login compartilhado:
> não deixa rastro de quem leu o quê, o que é frágil para a obrigação de LGPD do contrato.

---

## 🟡 7. Estrutura de comitês · 12 encontros

O contrato descreve "12 encontros síncronos". O produto padrão DR-E prevê 8 boards online + 4
presenciais = 12. Coincide numericamente, mas o contrato **não distingue** online de presencial.

**Ação:** confirmar no kick-off quantos são presenciais e travar as datas na agenda dos C-Levels
(a dedicação de C-Level em comitê presencial é de ~10h no método, não se resolve com 1 semana de antecedência).

---

## 🟠 8. A revisão de qualidade do material não tem dono

**Atualização de 04/09: não há Growth Planner neste projeto.** A nomenclatura foi removida dos
documentos e do portal, nomear um papel que não existe é pior do que não nomear nada. O que **não**
sai junto com o nome é a exigência do método.

A [regra 4 do repositório](CLAUDE.md) e o
[playbook](00-playbook/03-ciclo-90-dias-e-comites.md#3-gate-de-qualidade-da-matriz-obrigatório) são
explícitos: **não há comitê sem Matriz aprovada**, e a validação é feita por **quem não participou
da análise**. A Matriz e a revisão de qualidade são a mesma sessão, não duas; no portal ela aparece
como **revisão de qualidade**, porque "Matriz" é vocabulário interno do método. A independência é o ponto, quem escreveu o material não consegue testar a própria
cadeia causal.

**Atualização de 10/09: as duas revisões viraram uma, e ela ficou mais crítica, não menos.** Com a
apresentação dos diagnósticos absorvida pelo Comitê 1, existe **um único material** e **um único
gate** antes de um evento que agora apresenta e decide na mesma sessão. Não há mais um primeiro
encontro em que o material é testado contra a sala antes de virar decisão.

**Atualização de 11/09: a revisão foi de 01/10 para 18/09.** Com a consolidação causal e a CRT
correndo em paralelo aos diagnósticos, o material termina de ser escrito na mesma sexta em que
precisa ser revisado e aprovado.

| Data | O quê | Bloqueia? |
|---|---|---|
| **18/09** | Material do evento único: diagnósticos, CRT, nuvem de conflito e injeção, **e a Matriz no mesmo dia** | **Sim. Bloqueio duro**: sem ela o comitê não acontece |

> 🔴 **Isso torna a nomeação do revisor urgente, não importante.** Revisar num dia material que levou
> uma semana para ser escrito só funciona se o revisor tiver acompanhado a construção. Nomear até
> **15/09**, não até 18.

**A decisão em aberto não é mais "quem é o GP". É esta:**

1. **Quem revisa?** Qualquer pessoa da V4 que não tenha participado da análise serve ao propósito do
   método. Não precisa ser da Matriz nem carregar o título.
2. **Se não houver ninguém**, isso precisa ser uma decisão consciente e registrada em ata, não uma
   etapa que sumiu do cronograma sem ninguém notar. E agora sem rede: era o segundo gate que
   protegia o primeiro, e o primeiro deixou de existir.

> ⚠️ O **C-Level da V4** para o Comitê 2 presencial também segue sem nominação. A dedicação de
> C-Level em comitê é de ~10h no método e não se resolve com uma semana de antecedência
> (ver [pendência 7](#-7-estrutura-de-comitês--12-encontros)).

**Responsável:** Gustavo Figueiredo · **Prazo:** 15/09, para dar tempo de o revisor acompanhar a
consolidação causal em vez de receber o material pronto em 01/10

---

## 🟡 9. Cláusulas contratuais que grandes contas costumam negociar

Verificar se o instrumento assinado manteve a redação padrão:

| Cláusula | Redação padrão | Risco |
|---|---|---|
| 4.1 (uso de marca para case) | OLX permite uso do nome/marca para divulgação de case, sem custo, inclusive após o encerramento | Governança de marca corporativa costuma vetar |
| 7.2 (cessão) | V4 pode ceder para **outra franquia da rede** sem anuência da OLX | Cliente corporativo costuma exigir anuência |
| 7.11 (foro) | Comarca da sede da **CONTRATADA** (Campinas/SP) | Contraparte de porte costuma puxar para sua sede |

---

## 🟡 10. Inconsistência de redação no contrato

A cláusula **3.2** (cashback) refere-se ao *"valor previsto na alínea 'b' desta cláusula"*, mas a
cláusula 3.1 usa numeração romana (**I** e **II**). A referência cruzada está quebrada.

**Ação:** apontar ao jurídico para correção em eventual aditivo.

---

## ✅ 11. V4MOS com o Google ingerido, Meta ainda vazio · RESOLVIDA

**Resolvida em 14/09/2026.** O lote de acessos de 10/09 liberou as duas contas de anúncio, o V4MOS
começou a ingerir Meta em **12/09** e a recoleta de **14/09**, sobre 01/01/2025 a 14/09/2026,
fechou a pendência com dado em volume.

| Lado | Estado |
|---|---|
| **Google Ads** | ✅ Ingerindo. 23 campanhas, R$ 2.746.029,59, 56,4 mi de impressões, 10,17 mi de cliques, CTR 18,03% e CPA R$ 3,06, de 01/01/2025 a 14/09/2026. **Só 11 dos 21 meses têm dado**, faltam nov/2025 a abr/2026 inteiros |
| **Meta Ads** | ✅ Ingerindo. 90 campanhas, 1.079 anúncios, R$ 7.375.303,34, 1,88 bi de impressões, 29,4 mi de cliques, 1,41 bi de alcance, CPM R$ 3,91 e CTR 1,56%, em **21 meses contínuos** |

**O achado que a resolução produziu, e que vale mais que a resolução:** o investimento do Meta é
**2,7 vezes o do Google** na mesma janela. Todo o material do projeto anterior a 12/09 foi escrito
quando o Meta devolvia `data: []`, isto é, sobre uma leitura de mídia invertida. O Meta é também a
única série mensal de mídia contínua que o projeto tem, e portanto a única utilizável no forecast.

**Nota de método sobre por que isso demorou dois dias a aparecer.** A ingestão começou em 12/09 e
ficou invisível até 14/09 porque o script gravava o resultado na chave `connectors`, em inglês, que
só as skills `ee-*` reaproveitadas leem, enquanto as skills `dre-*` deste projeto leem `conectores`.
O script passou a gravar nas duas. Ver o histórico v28 em [`dados/client.json`](dados/client.json).

### O que sobrou de aberto, e virou item próprio

1. **A lista de contas de anúncio do portfólio `New OLX Brasil`.** A leitura de 01/09 pela interface
   mostrava uma única página, `Grupo OLX` (ID `1239097169583910`), com **"Nenhum ativo conectado"**,
   e havia dúvida sobre se era artefato de permissão do usuário logado. As duas contas concedidas
   provam que era: existiam ativos e a visão estava limitada. O que segue sem resposta é **quantas
   contas de anúncio existem de fato no portfólio**, porque a operação pode ser maior que as duas.
   Enquanto isso não vier, R$ 7,38 mi é o piso do investimento em Meta, não o total.
   **Responsável:** Mirella Mendonça · **Prazo:** antes do Comitê 1 de 23/09
2. **Os seis meses ausentes da série do Google**, nov/2025 a abr/2026, origem não apurada entre
   pausa real da conta e falha de ingestão. **Responsável:** Michelle Morais · **Prazo:** 22/09
3. **A separação de B2B e B2C**, que é o que impede esses R$ 10,12 mi de virarem numerador de CAC.
   Segue na [pendência 12](#-12-as-campanhas-visíveis-no-google-ads-parecem-ser-b2c-não-b2b), que
   continua aberta e agora vale para as duas contas de Meta também.


---

## 🔴 12. As campanhas visíveis no Google Ads parecem ser B2C, não B2B

Achado ao ler o primeiro dado real que chegou pelo V4MOS. As 8 campanhas do MCC recém-liberado,
na leitura de 22/06 (a recoleta de 14/09 mostra 23 campanhas nesta mesma conta):

```
dsageralbr_gg_se_bg_ld_ao_wb_re_vr_pf
pmaxaluguelsp_gg_pm_bg_la_ao_wb_re_vr_pf
pmaxcomprasp_gg_pm_bg_lc_ao_wb_re_vr_pf
pmaxgeralbr_gg_pc_bg_ld_ao_wb_re_vr_pf
pmaxsp_gg_pc_bg_ld_ao_wb_re_vr_pf
senbaluguelsp_gg_pc_bg_ld_ao_wb_re_vr_pf
senbcompramcmvsp_gg_pc_bg_lc_ao_wb_re_vr_pf
senbcomprasp_gg_pc_bg_lc_ao_wb_re_vr_pf
```

Duas leituras na nomenclatura, ambas apontando para consumidor final:

- Todas terminam em **`vr_pf`**. Se `pf` for pessoa física, é o oposto do recorte contratado.
- Os temas são **aluguel**, **compra** e **MCMV**, que é jornada de quem procura imóvel,
  não de imobiliária que anuncia.

| | |
|---|---|
| **Por que importa** | O foco declarado pela Mirella em 10/08 é **B2B**. Se a conta liberada é a de captação de consumidor, o diagnóstico de mídia estaria medindo o funil errado |
| **Hipótese alternativa** | O B2B da OLX pode ser servido por outra conta, ou a mídia B2B pode ser residual e a aquisição de anunciante vir de outro canal, o que já seria um achado |
| **Ação** | Confirmar no kick-off: o que significa o sufixo `pf` na convenção interna, e qual conta carrega a mídia de captação de anunciante |
| **Responsável** | Michelle Morais · **Prazo:** kick-off de 24/08/2026 |

> Não conclua nada a partir disso antes da confirmação. É leitura de nomenclatura, não de
> dado de negócio, e nomenclatura de campanha erra com frequência.

**Atualização de 31/08 · a hipótese ganhou evidência independente.** O GA4, liberado nesta data,
lista os vínculos de Google Ads de cada propriedade. A propriedade **GA4 ZapImóveis** (`407374944`)
tem **7 contas de Google Ads vinculadas**:

```
9221562141 · 6794249680 · 7581320191 · 6386557247 · 1973081572 · 5004050899 · 4632447364 (MCC)
```

**Nenhuma delas é a `526-656-0190`**, a única a que a V4 tem acesso. E a propriedade **GA4 Grupo OLX**
(`503925542`) não tem **nenhum** vínculo de Google Ads.

Duas leituras, e as duas mudam o plano de mídia:

1. A operação de Google Ads do grupo é **muito maior** do que a conta liberada. A V4 enxerga hoje
   R$ 2,75 mi de investimento nesta conta; o conjunto vinculado ao ZapImóveis é outra ordem de
   grandeza.
2. A conta liberada pode ser uma conta lateral, não a conta principal de nenhuma das duas frentes.

**Ação revista:** pedir a relação completa das contas de Google Ads do grupo, com o dono e a
finalidade de cada uma, e identificar **qual carrega a captação de anunciante**. Este é o pedido que
mais muda o resultado da auditoria (vi).
**Responsável:** Michelle Morais · **Prazo:** antes da apresentação de 29/09

**Atualização de 14/09 · a hipótese atravessou para o Meta, e com peso.** As duas contas de Meta
entraram em ingestão e trouxeram 90 campanhas. A convenção de nomenclatura é a mesma, e o resultado
é mais forte do que no Google:

| | |
|---|---|
| Campanhas de Meta terminadas em **`_pf`** | 30 de 90 |
| **Investimento nelas** | **R$ 6.664.682,43 de R$ 7.375.303,34, ou 90,4%** |
| O que carrega o resto | 26 campanhas em `_sc`, quase todas de alcance e engajamento no Instagram, mais 34 com nomenclatura livre (`Q1_2025_Março_Engajamento`, `Q3_2025_setembro_alcance`) |

Os maiores itens de gasto são explícitos no objetivo: `folocalizanewpplbr_mt_ct_bo_fm_ao_cr_at_ol_pf`
(R$ 667 mil, `OUTCOME_LEADS`), `founidaspplbr_mt_ct_bo_fm_ao_cr_at_ol_pf` (R$ 603 mil,
`LEAD_GENERATION`), `cmat26f1-alcance_mt_pm_os_aw_tp_cr_at_ol_pf` (R$ 654 mil,
`OUTCOME_AWARENESS`). O infixo **`ppl`** e o objetivo de geração de lead convivendo com o sufixo
`pf` é exatamente a ambiguidade que a pergunta do kick-off deveria ter resolvido e não resolveu.

**O que isso muda na pendência.** Se `pf` significa pessoa física, então **90% do maior investimento
de mídia do grupo está fora do recorte contratado**, e o diagnóstico (vi) mediria o funil errado
numa escala muito maior do que a suspeitada em agosto. Se `pf` significa outra coisa na convenção
interna, a leitura inteira cai. A diferença entre os dois cenários é uma frase, e ela continua sem
dono desde 24/08.

> Vale aqui a mesma ressalva do topo, e ela fica mais importante, não menos, agora que o número é
> grande: **isto é leitura de nomenclatura, não de dado de negócio.** Nenhum material de comitê pode
> afirmar que 90% da mídia é B2C. O que o material pode afirmar é que **R$ 10,12 mi de mídia medida
> não têm recorte declarado**, e que ninguém no projeto sabe qual parte é captação de anunciante.

**Ação atualizada:** obter do time de mídia, por escrito, o significado de `pf`, `sc` e `ppl` na
convenção, e a lista de qual conta e qual campanha é captação de anunciante.
**Responsável:** Mirella Mendonça + Michelle Morais · **Prazo:** antes do Comitê 1 de 23/09


---

## 🔴 13. O GA4 do grupo não mede conversão: e onde mede, mede errado

Achado da varredura de 31/08, primeira leitura possível depois de o GA4 ser liberado, **revisado e
corrigido em 11/09/2026**. Sustenta a auditoria **(vii) Rastreamento Completo**, a prioritária, e é
evidência direta de **Trava de Cegueira**.

> ✅ **O acesso de leitura ao GA4 deixou de ser limitação.** Conferido em 11/09: a API de
> administração responde **tudo** para `gina@v4company.com`, incluindo eventos-chave, fluxos de
> dados, retenção, links do Google Ads e dimensões personalizadas. A ressalva antiga, de que as
> telas de Administração seguiam fora de alcance por causa do `can_edit: false`, confundia
> **permissão de escrita** com **permissão de leitura**. Falta poder editar, e isso não impede
> diagnosticar. O que a V4 não alcança são quatro streams específicas, registradas na pendência 27.

### Propriedades de alto volume cujo evento-chave nunca dispara

> ⚠️ **Corrigido em 11/09/2026.** A redação anterior dizia que estas propriedades não tinham
> **nenhum** evento-chave. **É falso**, e foi erro de leitura: a varredura de 31/08 leu o *volume*
> de eventos-chave no período, não a *configuração*. Lendo a configuração pela API de administração
> em 11/09, as quatro têm evento-chave definido. O que elas não têm é ocorrência. O achado não
> enfraquece com a correção, fica mais preciso e mais grave.

| Propriedade | ID | Sessões (60 dias) | Eventos-chave definidos | Desde | Ocorrências |
|---|---|---:|---|---|---|
| GA4 Grupo OLX | `503925542` | 2.194.847 | `qualify_lead`, `close_convert_lead`, `purchase` | 05/09/2025 | 🔴 **zero** |
| Autos 360 (Ex-Altimus) | `516288559` | 770.548 | os mesmos três | 12/12/2025 | 🔴 **zero** |
| ANAPRO | `469847974` | 680.229 | `purchase` | 09/12/2024 | 🔴 **zero** |
| OLX PRO | `382768600` | 35 | `purchase` | 07/06/2023 | zero |
| OLX Pro Landing | `382776122` | - | propriedade ativa, sem volume no período | - | - |

**A correção muda a natureza do achado.** "Ninguém definiu o que é conversão" é desleixo de
configuração. O que o dado mostra é outra coisa:

> **Alguém definiu o funil B2B no GA4, com `qualify_lead` e `close_convert_lead`, e o site nunca
> emitiu esses eventos.** Em `GA4 Grupo OLX` a definição está de pé há **mais de um ano** e acumulou
> **zero ocorrência** em 2,19 milhões de sessões e 7,39 milhões de eventos.

Isso não é ausência de intenção, é intenção que não virou instrumentação. Alguém sabia qual era o
funil de receita B2B a ponto de nomear as duas etapas. Ninguém fechou o circuito entre essa definição
e o que o site empurra para o dataLayer. É o mesmo desenho que o GTM mostra do outro lado: capacidade
técnica presente, ninguém encarregado de conferir se o número sai.

O **Autos 360** continua eloquente pelo mesmo motivo, agora melhor descrito: 449 nomes de evento
distintos, três eventos-chave definidos há nove meses, e nenhuma ocorrência deles. E **OLX PRO**, o
produto do anunciante profissional, exatamente o recorte B2B contratado, registra **35 sessões em 60
dias**, o que significa que a propriedade está órfã, não que o produto não tem tráfego.

### A retenção de dado repete a divisão entre consumidor e B2B

Lido por API em 11/09, junto com a correção acima. Nunca tinha sido verificado.

| Propriedade | Retenção de dado de evento |
|---|---|
| OLX App + Web · GA4 ZapImóveis · GA4 VivaReal | **50 meses** |
| **GA4 Grupo OLX** (`503925542`) | 🔴 **2 meses** |
| **GA4 ZapImóveis + VivaReal** (`494455315`) | 🔴 **2 meses** |
| ANAPRO · Autos 360 · OLX PRO | 🔴 **2 meses** |

Dois meses é o padrão de fábrica do GA4: é o que fica quando ninguém mexe. As propriedades de
consumidor foram para 50 meses, o máximo. **A propriedade que carrega toda a superfície B2B ficou no
padrão.**

**Consequência direta para o DR-E:** não há série histórica no recorte contratado. Nenhuma comparação
ano a ano, nenhuma linha de base anterior a meados de julho de 2026, nenhum funil histórico para
calibrar o forecast de 12 meses. E, diferente de quase tudo nesta lista, **a correção é um clique** e
não recupera o passado: o dado de antes de 2 meses já foi descartado e não volta.

**Ação acrescentada:** subir a retenção de `GA4 Grupo OLX` e de `GA4 ZapImóveis + VivaReal` para 14
meses (limite do tier gratuito) ou 50 (tier 360), hoje, para parar a sangria. Quanto antes, menos
história se perde.

### Onde há evento-chave, o problema é o inverso

**GA4 VivaReal** (`407391347`) marca **`session_start` como evento-chave**: 13,27 mi em agosto, ao
lado de `generate_lead` (830.116) e `generate_lead_pro` (661.144).

Marcar início de sessão como conversão faz três estragos ao mesmo tempo: infla qualquer taxa de
conversão relatada, torna o CPA calculado pela plataforma um número sem significado, e, se essa
conversão estiver importada no Google Ads, treina o Smart Bidding para comprar sessão, não cliente.

### Por que isso é bloqueio de método, não só de auditoria

A regra 8 deste repositório exige que a receita derivada do funil bata com a declarada, com tolerância
de 5%. Com esta base de medição, **não há funil derivável** para três dos ativos do grupo, e o único
que tem eventos de lead conta sessão junto com lead. Sem correção, o forecast do Comitê 1 herda o erro.

### O tier pago está nas propriedades erradas

O GA4 informa o nível de serviço de cada propriedade. O resultado, lido em 01/09:

| Propriedade | Tier |
|---|---|
| GA4 VivaReal · GA4 ZapImóveis · OLX App + Web · Autos 360 | **`GOOGLE_ANALYTICS_360`** (pago) |
| **GA4 Grupo OLX** (`503925542`) | `GOOGLE_ANALYTICS_STANDARD` (gratuito) |

A propriedade que carrega **`ads.grupoolx.com.br`, `imoveis.`, `autos.`, o institucional e
`vender.olx.com.br`**, ou seja, toda a superfície B2B do escopo contratado, é a única no tier
gratuito. As propriedades de consumidor rodam no tier pago.

E o **Autos 360** agrava: está no tier pago, tem 449 nomes de evento distintos e **nenhum marcado
como conversão**. A OLX paga por capacidade de medição enterprise num ativo onde ninguém definiu o
que é resultado.

Isso não é opinião sobre prioridade, é a alocação de orçamento de ferramenta, e ela diz onde a
atenção da organização está. Para uma trava de **Cegueira**, é evidência de política implícita:
*a medição séria é do consumidor; o B2B se vira com o que dá.*

### O que sobra de bom

`generate_lead_pro`, com 661.144 eventos em agosto, é o **primeiro indicador possivelmente B2B**
que apareceu em todo o projeto. Se ele for mesmo o lead de anunciante, é o numerador que falta para
o fluxo de receita.

**Ação:**
1. Confirmar com a OLX o que `generate_lead_pro` mede e se corresponde ao funil de anunciante.
2. Perguntar se as conversões do GA4 estão importadas no Google Ads e quais campanhas otimizam por elas.
3. Pedir GTM e Search Console, sem eles dá para constatar a falha, não para apontar a causa técnica.
4. **Pedir elevação do GA4 de Leitor para Editor** nas propriedades em escopo. O nível foi
   confirmado na interface em 01/09: somos **Leitor**, o que bate com o `can_edit=false` da API.
   Leitor sustenta o diagnóstico de sintoma, tudo que está neste item foi levantado assim, mas não
   abre as telas de Administração onde mora a causa: fluxos de dados, regras de evento, definições
   personalizadas e a configuração de consentimento (H4). O argumento já está escrito no documento de
   25/08 e não precisa ser reconstruído.

**Responsável:** Consultor + Michelle Morais · **Prazo:** antes da apresentação de 29/09

> Ressalva de leitura: tudo acima vem da API de dados do GA4 em 31/08/2026 e descreve **como a medição
> está configurada**, não como o negócio performa. A OLX pode ter uma camada de mensuração fora do GA4,
> BI próprio, Salesforce, servidor. Se tiver, isso muda o diagnóstico de "não mede" para "mede em
> outro lugar", e a pergunta passa a ser por que as duas camadas não conversam. Perguntar antes de afirmar.

---

## 🟠 14. Apresentação adiada de 10/09 para 29/09, e o mês de silêncio que isso abre

Havia na agenda o evento **"Diagnóstico V4"**, em **10/09/2026, das 15h às 17h**, presencial na OLX
(sala SP-15), organizado por **Mirella Mendonça**, com Dener Lippert e Gustavo Figueiredo na lista.
Ele apareceu sem constar de nenhum documento do projeto, e foi confirmado em 01/09 como apresentação
dos diagnósticos, não antecipação do Comitê 1.

**Decisão de 03/09: adiar.** O gatilho foram dois fatos do mesmo dia, a OLX marcou a entrega do
lote de acessos para as 17h de 03/09, e a V4 dimensionou os nove diagnósticos em 15 dias corridos.
Com os diagnósticos abrindo no dia seguinte à entrega, o dia 10 cairia no terceiro dia útil da
janela: a reunião leria três frentes pela metade em vez do diagnóstico.

**Data vigente, revista em 04/09: terça, 29/09.** A entrega de 03/09 não ocorreu e passou para
08/09 ([pendência 18](#-18-a-entrega-de-acessos-de-0309-não-ocorreu-nova-data-é-0809)), levando a
apresentação de 24 para **29/09** e o Comitê 1 de 01 para **06/10**. As datas de 24/09 e 01/10
aparecem abaixo apenas onde registram a decisão de 03/09, não são mais alvo de agenda.

| | |
|---|---|
| **O que a decisão compra** | Uma apresentação que lê os **nove** diagnósticos, quatro dias úteis depois de eles fecharem (23/09), com a consolidação causal já feita e revisada |
| **O que ela custa** | **Mais de um mês sem contato síncrono com os decisores**, entre o kick-off de 24/08 e 29/09. Numa conta que acabou de fechar a janela de garantia (pendência 3), silêncio longo é lido como parada |
| **A mitigação assumida** | **Reporte escrito nas sextas 11/09 e 18/09**: o que os diagnósticos estão devolvendo, e o que ainda falta da OLX. Não é entregável contratual; é o que impede a leitura errada |

**O argumento a usar na comunicação, e ele não é da V4.** A transcrição do kick-off registra a
regra dita pela sala de São Paulo em 02:01:16: *"a gente poderia passar a contar os 15 dias ali, se
por exemplo a gente conseguir concluir os acessos até quarta, 15D daí em diante é fair pra gente"*,
e em 01:49:48, *"é até 15 dias, **uma vez que a gente receber tudo**"*. Os 15 dias nunca foram data
de calendário: são contagem que começa na entrega dos acessos. O gatilho escorregou de 26/08 para
08/09, e tudo que dependia dele escorregou junto. A tabela comparativa está em
[cronograma-e-marcos.md](04-execucao/cronograma-e-marcos.md#o-relógio-dos-15-dias-é-do-kick-off-e-ele-sempre-foi-condicional).

> ⚠️ **A parte que não sai da regra e precisa ser dita.** No desenho do kick-off o presencial caía um
> dia depois de o diagnóstico fechar (09 → 10/09). Aqui há **quatro dias úteis** entre 23 e 29/09, e
> eles são a consolidação causal e a revisão de qualidade do material, que aquele desenho não
> reservava. Essa diferença precisa ser explicada, não escondida.

**Ações abertas:**

1. **Comunicar o adiamento à Mirella com a data nova junto**, não depois. Adiamento sem data
   substituta é o que gera a leitura de parada. **Prazo: 04/09.**
2. **Confirmar a apresentação em 29/09 e o Comitê 1 em 06/10** na agenda dos decisores. A dedicação
   de C-Level em comitê não se resolve com uma semana de antecedência (pendência 7).
3. **Definir quem revisa o material até 08/09.** São **duas revisões**, 28/09 para a apresentação
   e 05/10 para a Matriz do Comitê 1, esta com bloqueio duro pela regra 4 do repositório.

**Responsável:** Consultor + Gustavo Figueiredo · **Prazo:** comunicação em 04/09; revisor em 08/09

> Cronograma reajustado em [04-execucao/cronograma-e-marcos.md](04-execucao/cronograma-e-marcos.md);
> grade dia a dia em
> [04-execucao/sprint-diagnosticos-09-a-23-09.md](04-execucao/sprint-diagnosticos-09-a-23-09.md).

---

## 🔴 15. Achados críticos da auditoria de rastreamento

Auditoria completa em [`02-diagnostico/auditoria-vii-rastreamento.md`](02-diagnostico/auditoria-vii-rastreamento.md).
Os cinco que exigem decisão da OLX:

| # | Achado | Quem decide |
|---|---|---|
| 1 | `[TAG] GA4 - Purchase` disparada pelo gatilho de `begin_checkout` em `GTM-KGFGVFC`. O gatilho correto existe e está ocioso | Time de dados OLX |
| 2 | Consent mode concede tudo por padrão, botão "recusar tudo" oculto por CSS, banner com 4s de atraso | **Jurídico / DPO da OLX** |
| 3 | `lead_b2b` com zero eventos em agosto, o lead B2B não tem numerador | Time de dados OLX |
| 4 | Tag que grava `user_olx` pausada; `seller_category` (corte profissional vs. particular) fica vazio | Time de dados OLX |
| 5 | Parâmetros de item lidos sem índice de array, `purchase` provavelmente sem item nem valor | Confirmar no Preview |

**Ação:** levar 1, 3, 4 e 5 ao time técnico da OLX como correção. **O item 2 não é correção técnica:**
é decisão de compliance e precisa entrar na pauta com o jurídico deles, não numa lista de bugs.
A V4 não altera configuração sem aprovação prévia e explícita, cláusula do documento de acessos.
**Responsável:** Consultor + Michelle Morais · **Prazo:** antes da apresentação de 29/09

---

## 🟠 16. A medição B2B mora numa propriedade que ninguém indicou

Os 5 contêineres escrevem em `G-50C013M2CC`, que é a propriedade **OLX App + Web** (`152644854`),
não a `GA4 Grupo OLX` (`503925542`). É lá que estão `ad_insertion` (4,6 mi/mês), `ad_edition`
(4,14 mi), `qualified_lead_autos_pro` (4,68 mi), `begin_checkout` (2,69 mi) e `purchase` (565 mil).

Isso reabre a pendência 13 por outro lado: a propriedade "GA4 Grupo OLX" não mede porque **não é ela
que recebe**. O diagnóstico muda de "não medem" para "medem em outro lugar, e o mapa que nos deram
apontava para o lugar errado".

**Ação:** pedir à OLX o mapa de propriedade × measurement ID × superfície, e confirmar qual é a
propriedade de referência do B2B. **Prazo:** antes de 29/09

---

## 🔴 17. O GTM tem quatro contas, e auditamos uma e meia

Visto na tela inicial do GTM em **02/09/2026**, respondendo a uma pergunta que estava aberta desde
01/09: existe conta de GTM separada para ZAP e VivaReal?

| Conta | ID | Selo | Contêineres recebidos |
|---|---|---|---:|
| BR - www.olx.com.br | `94905` | 360 | 10 |
| **Checkout Unificado - PRO** | `6326134112` | 360 | **0** |
| **VivaReal** | `4412254379` | 360 | **0** |
| **ZapImóveis** | `2971905372` | 360 | 1 de N |

**O que isso faz com o que já foi concluído.** O inventário de "22+ contêineres" registrado no
checklist é o piso de **uma** das quatro contas. A auditoria (vii) leu 6 contêineres de um universo
cujo tamanho ainda não sabemos. Nenhum achado publicado deixa de valer, todos vêm de export real,
mas a frase "a auditoria cobre o escopo B2B" não se sustenta enquanto duas contas inteiras não forem
lidas.

**Por que a conta `Checkout Unificado - PRO` é o pedido mais valioso do projeto.** O nome junta as
duas palavras que definem o escopo contratado: *checkout*, onde a receita acontece, e *PRO*, o
anunciante profissional. Se a leitura estiver certa, é ali que mora a medição da receita B2B, e o
[achado 1 da auditoria](02-diagnostico/auditoria-vii-rastreamento.md) precisa ser relido contra ela:
o `purchase` quebrado em `GTM-KGFGVFC` pode estar corrigido nesse contêiner, pode estar duplicado, ou
pode ser que o contêiner auditado seja o legado.

> ⚠️ Isso é **leitura de nomenclatura**, não de dado. É a mesma armadilha da
> [pendência 12](#-12-as-campanhas-visíveis-no-google-ads-parecem-ser-b2c-não-b2b), onde o sufixo
> `pf` sugeriu pessoa física. Confirmar com a OLX antes de tratar como achado.

**Ação:** pedir os exports das três contas, na ordem `Checkout Unificado - PRO` → resto da
`ZapImóveis` → `VivaReal`, mais o print da tela inicial de cada uma. Detalhe operacional no
**Bloco 0** de [`coleta-pendente.md`](02-diagnostico/coleta-pendente.md).
**Responsável:** Consultor + operador · **Prazo:** entra na conferência do lote de 08/09 (pendência 18)

---

## 🟠 18. Acessos recebidos em 10/09: falta a conferência item a item

**Resolvido em 10/09/2026.** O lote completo chegou dois dias depois do compromisso de 08/09.
A contagem disparou no mesmo dia. Com os ajustes de 11/09, os nove diagnósticos rodam de
**10 a 18/09**, a Matriz é aprovada em **18/09**, e o evento único acontece em **23/09**
(ver [pendência 25](#-25-data-do-evento-único-2309--resolvida)).

Os quatro diagnósticos que estavam totalmente parados abriram, e os quatro que rodavam em camada
parcial ganharam a camada onde mora a causa, não o sintoma.

**O que continua aberto é a verificação**, e ela vale como pendência própria porque o precedente
deste projeto é ruim: acesso concedido não é acesso utilizável.

### O risco não é mais a data escorregar. É ter chegado concedido e não utilizável

Já aconteceu duas vezes neste projeto:

| Precedente | O que veio | O que faltava |
|---|---|---|
| GA4, 31/08 | Acesso às 26 propriedades | Nível **Leitor**, que não abre fluxos de dados, regras de evento nem consentimento (pendência 13) |
| Meta, 01/09 | Portfólio `New OLX Brasil` visível | **"Nenhum ativo conectado"**: nenhuma conta de anúncio compartilhada (pendência 11). ✅ **Resolvido em 12/09**, e a explicação foi a suspeitada: era limitação de permissão do usuário logado, não ausência de ativo |

**Ação:** conferência item a item em **10/09**, contra o
[checklist de dados e acessos](02-diagnostico/checklist-dados-e-acessos.md), **abrindo cada
ferramenta**, não lendo o e-mail de concessão. O que estiver em nível insuficiente é escalado **no
mesmo dia**, a janela de 15 dias não tem semana seguinte sobrando, e a folga do contrato acabou.

> ⚠️ **O checklist de dados e acessos ainda reflete o estado anterior a 10/09.** Ele só deve ser
> atualizado item a item **depois** da conferência na ferramenta, para não trocar um registro
> desatualizado por um registro otimista.

**Pedir junto, e não é acesso:** o **bloco A** (Visão de Negócio e Fluxo de Receita, A1–A3) é
entrega de dado e segue sem nenhum item recebido. Nenhuma concessão de ferramenta o destrava, e sem
ele não há mapeamento do fluxo de receita nem matemática de forecast, com ou sem os nove
diagnósticos fechados.

### Atualização de 14/09: a conferência foi feita até onde este ambiente alcança

**Feito, abrindo a fonte e não o e-mail:**

| Ferramenta | Método | Resultado |
|---|---|---|
| **GA4** | Admin API + Data API | ✅ 26 propriedades em 3 contas, **as mesmas de 31/08**, `can_edit=false` em todas e `custom_dimensions` vazias na 503925542. Leitura de dado funciona: 01 a 13/09 devolve os mesmos 10 eventos automáticos de agosto |
| **V4MOS** | 3 endpoints + os 2 controles de sanidade | ✅ Google 500 e Facebook 114 registros em setembro. Secret inválido devolve **401**, organização inexistente devolve **403**: os dois controles passam |
| **Meta Ads**, as duas contas | Indireto, pela ingestão | ✅ De `data: []` para 1.079 anúncios. Só ativo compartilhado produz isso, o que confirma que o "Nenhum ativo conectado" de 01/09 era limitação de permissão do usuário logado |
| **Google Ads**, MCC 526-656-0190 | Indireto, pela ingestão | 🟡 O V4MOS puxa a conta, mas **a interface não foi aberta**. A API do Google Ads também não serviu: o conector deste ambiente está sem `GOOGLE_ADS_DEVELOPER_TOKEN` e o conector alternativo falha com 502 |
| **GTM** | API do Tag Manager | 🔴 **403**, sem o escopo `tagmanager.readonly`. Confirma a [pendência 26](#-26-a-coleta-do-gtm-não-pode-ser-automatizada-com-a-credencial-atual): export segue manual |

**Não feito, e é o que importa.** As quatro ferramentas que decidem o Comitê 1 continuam sem
conferência: **CRM comercial**, **Salesforce Marketing Cloud**, **Google Search Console** e o
**Meta Business Manager**. Não há conector de nenhuma delas neste ambiente, e a do Meta exige uma
autorização OAuth que só uma sessão interativa consegue fazer. **Só abrindo a interface, ou
pedindo export.**

`dados/acessos.json` foi atualizado com exatamente isso: o que abriu está como concedido ou
parcial, com a evidência; o que não abriu **continua pendente**, e nenhum item subiu de status sem
prova de abertura.

O custo do resíduo deixou de ser hipotético quando a aba de Métricas do portal passou a marcar
cobertura indicador a indicador, e ele não diminuiu com esta conferência, porque nada do que foi
conferido é o que prende os indicadores:

| | |
|---|---|
| Indicadores presos em acesso declarado e não conferido | **23** |
| Destes, **P0** (bloqueiam o Comitê 1) | **18** |
| Quantos dependem só do **CRM comercial** | **20** |

Os outros três se dividem entre Salesforce Marketing Cloud (2) e Search Console (1).

**Os 23 seguem presos.** Nenhuma das ferramentas conferidas em 14/09 os destrava: 20 dependem do
CRM comercial, 2 do Marketing Cloud e 1 do Search Console, e são justamente as três que não têm
conector aqui.

**Agravante prático:** não há conector de Salesforce, de Search Console nem do CRM comercial neste
ambiente. Não dá para testar por API como se fez com GA4, V4MOS e GTM. A conferência exige **abrir
a ferramenta na interface**, ou pedir export.

**Dependência técnica que saiu das sessões de CRM de 09 e 10/09, e que pode explicar tudo:** o
Sales Cloud exige o e-mail **`@olxbr` habilitado no MyApps**. Se a habilitação não foi feita, o
acesso nominal existe e a ferramenta não abre, que é exatamente o padrão de calote que esta
pendência existe para pegar. **Perguntar isso antes de abrir**, é a checagem mais barata da lista.

**Por que isso trava a planilha de metas:** dos quatro dados que faltam para o forecast, três saem do
CRM (ticket médio de entrada, base ativa de anunciantes, contratos novos por mês). Se o acesso de
10/09 for real, os três saem sem pedir nada à OLX. Se não for, eles viram pedido, e o pedido tem
prazo de resposta que a janela até 18/09 não comporta.

**Ação:** abrir **CRM comercial**, **Salesforce Marketing Cloud** e **Search Console**, nesta
ordem, na interface, e registrar o nível de permissão de cada um em
[`dados/acessos.json`](dados/acessos.json), que deixou de estar parado em 01/09 e agora traz a
conferência de 14/09 com a lista do que não foi aberto. Confirmar antes se o `@olxbr` está
habilitado no MyApps. O que estiver em nível insuficiente escala no mesmo dia.
**Responsável:** operador + Michelle Morais · **Prazo:** 15/09, antes do meio do sprint

**Responsável:** operador + Michelle Morais · **Prazo:** conferência em 10/09, escalada no mesmo dia

---

## 🔴 19. O denominador de 12% atravessou o modelo de meta sem exame

Achado da Análise Diagnóstica de 04/09 ([diagnostico-travas.md](02-diagnostico/diagnostico-travas.md)).

O slide da jornada, etapa 4, diz: *"**12%** dos clientes **que saem** no primeiro mês vão embora sem
publicar"* `[D]`. O próprio
[jornada-do-cliente-profissional.md](02-diagnostico/jornada-do-cliente-profissional.md) registra na
ambiguidade 3 que a frase comporta duas leituras e que **"a diferença é de uma ordem de grandeza no
tamanho do vazamento"**.

| Leitura | O que significa | Efeito |
|---|---|---|
| 12% **dos que saem** | Vazamento pequeno, concentrado em quem já ia embora | p(publicação) muito acima de 88% |
| 12% **do total** | 12 de cada 100 contratos nunca ativam | p(publicação) = 88% |

**O problema.** [meta-do-projeto.md:93](03-estrategia/meta-do-projeto.md) usa **p(publicação) = 88%**
na fórmula `contratos × p(pagamento) × p(publicação) × ticket`, que só vale sob a segunda leitura. A
ambiguidade foi resolvida silenciosamente, e para o lado que faz o vazamento parecer dez vezes maior.
Isso contamina o "cada real de contrato novo sustenta 7,8 reais" e a alavanca de "+4,5%".

**Por que a ambiguidade voltou a ser aberta.** A tabela de atualização do mesmo documento marca a
ambiguidade 3 como *"Respondida e decomposta"*. Ela não foi: a transcrição de 28/08 entregou uma
decomposição **por canal** (até 20% no online, 8–10% no assistido), e decompor por canal não declara
denominador, os 20% e os 8–10% herdam exatamente a mesma ambiguidade dos 12%.

**Ações:**

1. **Reabrir a ambiguidade 3** em `jornada-do-cliente-profissional.md`, hoje marcada como respondida.
2. **Perguntar à OLX qual é o denominador**: pergunta de uma linha, resposta de trinta segundos.
3. **Marcar o `88%` de `meta-do-projeto.md` como escolha não confirmada** até a resposta chegar.

**Responsável:** Consultor + Carolina Dallolio · **Prazo:** antes da apresentação de 29/09

---

## 🟠 20. O slide FLUXOS não está versionado, e todo o mix de canais depende dele

O mix de canais do anunciante profissional, CRM 29% · Direto 36% · Pago 16% · Orgânico 5% ·
Outros 11% `[D]`, existe **apenas em prosa** de anotação de reunião
([lacunas-do-fluxo-de-receita.md](02-diagnostico/lacunas-do-fluxo-de-receita.md) §1 e a ata de
28/08). O arquivo original nunca foi recebido: em `assets/originais/A-visao-de-negocio-e-fluxo-de-receita/`
só existe o PNG da jornada.

**Duas consequências:**

1. **Nenhum desses números é conferível contra a fonte**, e nenhum é reexecutável. Não podem entrar
   em material de comitê nessa condição.
2. **A leitura de confiança registrada no repositório está errada.** O documento afirma que as duas
   decomposições do slide fecham em 97% "por dois caminhos independentes" e que isso "sobe muito a
   confiança no material". Elas vêm do **mesmo artefato**, é consistência interna, não verificação
   independente. Corrigir na origem.

> ⚠️ O próprio slide traz a anotação *"teste de campanha paga para WhatsApp: entra tudo como Direto"*
> e *"perde atribuição: entra tudo como Direto"*. O maior canal do mapa é, em parte, artefato de
> mensuração: **Direto está inflado, Pago subestimado, e não existe CAC por canal hoje.**

**Responsável:** operador + Carolina Dallolio · **Prazo:** entra na coleta de 08/09

---

## 🔴 21. A série de receita não confirma o net negativo declarado em Imóveis

Achado da entrada da [série de receita 2025–2026](02-diagnostico/serie-de-receita-2025-2026.md),
processada em 08/09. É a inconsistência mais consequente aberta até aqui, porque ela decide se o
Ciclo 1 persegue **crescimento** ou **inflexão**.

| Fonte | O que diz |
|---|---|
| Iuna Scheffler, kick-off de 24/08 | *"as nossas entradas não estão compensando o churn mais downgrade"* em Imóveis |
| [meta-do-projeto.md](03-estrategia/meta-do-projeto.md) §6.1 | Construiu sobre isso a **meta zero**: se o net estiver em −5%/mês, metade da meta do projeto se consome só em parar a sangria |
| Série de receita, jan–jul/25 vs jan–jul/26 | `Classifieds - B&A`, o núcleo de Imóveis, **cresceu 6,4%** |

As três leituras compatíveis e como distinguir uma da outra estão na
[§4 da leitura da série](02-diagnostico/serie-de-receita-2025-2026.md). A mais perigosa é a de que
o net negativo seja de **logo** e não de receita: base perdendo clientes com o preço segurando o
faturamento é um sistema que parece saudável no P&L enquanto se esvazia.

**Ação:** pedir a **contagem de clientes ativos B2B de Imóveis, mês a mês**, na mesma janela da
série de receita. Uma coluna ao lado da outra responde a pergunta em cinco minutos e não depende de
acesso novo. Levar a pergunta para a apresentação de 24/09 na forma da §4, não como contestação.
**Responsável:** operador · **DRI no cliente:** Iuna Scheffler · **Prazo:** 24/09, antes do Comitê 1

---

## 🔴 22. O churn de 8–10% ao mês está no modelo da meta como se fosse de receita

A [ambiguidade 4](02-diagnostico/jornada-do-cliente-profissional.md) pergunta se o churn declarado é
sobre cliente ou sobre receita. A série de receita agora **impõe um limite aritmético** à resposta.

Para que 9%/mês fosse churn de receita sobre `Classifieds - B&A`, o Grupo OLX teria de vender
**R$ 4,07 milhões de contrato novo por mês, R$ 49 milhões por ano, 114% da carteira**, todo ano, numa
vertical onde metade da entrada nasce de prospecção ativa `[D]`. A conta está na
[§5 da leitura da série](02-diagnostico/serie-de-receita-2025-2026.md).

**Por que isso é pendência e não curiosidade:** a §4.1 da
[meta do projeto](03-estrategia/meta-do-projeto.md) trata os 9% como churn de receita para concluir
que *"um ponto de churn vale mais que dez pontos de conversão de pagamento"*. Se o número for de
logo, essa frase, que é a **primeira direção técnica que a V4 dá ao cliente**, está calibrada sobre
a premissa errada, e o ranking das alavancas muda. A direção provavelmente se mantém; o tamanho, não.

**Ação:** extrair do dashboard, para Imóveis, **churn de logo e churn de receita separados**, mesma
janela. Recalibrar §4.1 antes que a faixa de +8% a +12% seja apresentada como proposta.
**Responsável:** operador, via links dos dashboards · **Prazo:** antes de 24/09

---

## 🔴 23. A meta de Ciclo 1, como está proposta, não é verificável na receita bruta

A [meta do projeto](03-estrategia/meta-do-projeto.md) §6 propõe para o Ciclo 1 um alvo de **+3 a +6
p.p. de run-rate**. Medida sobre a própria série do cliente, a variação de 90 dias em
`Classifieds - B&A` tem desvio de **±2,83%**, o que põe o **efeito mínimo detectável em +5,67%**.

**A metade de baixo da faixa proposta é indistinguível de ruído estatístico.** Não é questão de
ambição: é que a régua não tem resolução para o alvo. Some-se a inércia de 11 meses, que entrega só
~24% do ganho de regime em 3 meses, e o Ciclo 1 corre o risco de ser lido como fracasso enquanto faz
a coisa certa, que é exatamente o que a §6.1 já alertava por outro motivo.

**Ação:** fixar em ata, no Comitê 1, que a **meta de ciclo se mede no indicador da restrição**, com
o efeito em receita declarado como consequência derivada, nunca como o número que prova o ciclo. Se
a receita for lida, é em média móvel de 3 meses e com a banda de confiança declarada junto. As três
correções e a sazonalidade da janela ago–nov estão na
[§6 da leitura da série](02-diagnostico/serie-de-receita-2025-2026.md).
**Responsável:** operador · **Prazo:** redação pronta para 24/09, decisão em ata no Comitê 1

---

## 🟠 24. Três anomalias contábeis na série de receita, sem explicação

Nenhuma delas invalida a série, que fecha contra o próprio TOTAL nos 19 meses. Todas mudam a leitura
de alguma linha, e uma delas está dentro do TOTAL de um mês.

| # | Anomalia | Por que importa |
|---|---|---|
| a | `Transactional & Fintech - For Sale` com meses **negativos** (jul, ago e set/25; mar e abr/26) | Estorno, reclassificação e provisão revertida têm significados diferentes, e nenhum é receita |
| b | Linhas que **zeram no meio da série**: `CRM` some em set/25 e reaparece com R$ 561 mil em fev/26; `Data` cai a zero em abr/26; `Rentals` termina em dez/25 com R$ 566 | Descontinuação de produto e migração de rubrica produzem o mesmo desenho e têm consequências opostas para a leitura de Imóveis |
| c | `Conecta` registra R$ 318, R$ 40 e R$ 20 e depois um único lançamento de **R$ 6.865.055 em set/25** | O valor está dentro do TOTAL do mês. Se for não recorrente, set/25 é uma base de comparação inflada |

**Ação:** perguntar junto com a contagem de clientes ativos da pendência 21, no mesmo e-mail.
São perguntas baratas de responder e caras de descobrir depois.
**Responsável:** operador · **Prazo:** 24/09

---

## ✅ 25. Data do evento único: 23/09 · RESOLVIDA

**Resolvida em 11/09/2026.** A OLX confirmou o evento único, apresentação dos diagnósticos e
Comitê 1 na mesma sessão, para **quarta, 23 de setembro**.

A pendência existia porque a data estava em aberto com teto em 29/10, e o teto encostava no
Comitê 2 de 03/11: sobrava **um único dia útil** entre os dois, e um plano de 30 dias lido depois de
um dia de execução faria o Comitê 2 confundir falta de execução com saturação da trava.

**Com 23/09 o problema desaparece, não é mitigado:**

| | |
|---|---|
| Material pronto e aprovado na revisão | 18/09 |
| Apresentação + Comitê 1 | **23/09** |
| Dias úteis entre um e outro | 2, de agenda e ensaio |
| Comitê 2 | 03/11 |
| **Dias úteis de execução do plano de 30 dias** | **26** |

A antecipação só foi possível porque a consolidação causal, a CRT e a Nuvem passaram a correr em
paralelo aos diagnósticos, o que pôs o material pronto em 18/09 em vez de 02/10.

**Fica em aberto um item menor, movido para a [pendência 7](#-7-estrutura-de-comitês--12-encontros):**
a duração do evento. Com a apresentação dentro dele, o Comitê 1 não cabe nas 2h do formato padrão, e
isso precisa ser confirmado com a OLX junto com a convocação.

---

## 🟠 26. A coleta do GTM não pode ser automatizada com a credencial atual

Testado em 11/09, com a janela de **(vii) Rastreamento** ainda aberta. A API do Tag Manager
**responde** para `gina@v4company.com`, e o erro que devolve é `403 ACCESS_TOKEN_SCOPE_INSUFFICIENT`,
não `PERMISSION_DENIED`. A distinção importa: **o acesso do lado da OLX existe**, o que falta é o
escopo OAuth `tagmanager.readonly` na credencial local (ADC), que hoje carrega apenas
`analytics.readonly` e `cloud-platform`.

Duas tentativas de ampliar o escopo via `gcloud auth application-default login` foram **barradas na
tela de consentimento do Google**. O próprio `gcloud` avisa a causa antes de abrir o navegador: os
escopos sensíveis estão sendo bloqueados para o **client ID padrão** da ferramenta.

**O que isso custa:** os lotes 1 a 5 do [guia de export](02-diagnostico/guia-export-gtm.md) seguem
manuais, contêiner a contêiner pela interface. Os caros são o 3 e o 5, que pedem o inventário de três
contas cheias, e é exatamente o que uma chamada de API resolveria.

**O que resolve:** um OAuth client ID próprio da V4 no projeto `charged-thought-504117-b5`, com o
escopo `tagmanager.readonly`, no lugar do client ID padrão do `gcloud`. É configuração de console da
V4, não pedido à OLX.

O script que roda assim que o escopo existir está em
[`.claude/scripts/fetch_gtm_api.py`](.claude/scripts/fetch_gtm_api.py), **escrito e nunca executado**.
Ele inventaria as contas, baixa a versão publicada de cada contêiner e grava no envelope do export da
interface, para que `check_gtm_exports.py` leia a pasta sem alteração.

**Responsável:** Operador V4 · **Prazo:** não bloqueia (vii), que fecha em 15/09 pela via manual

---

## 🟠 27. Quatro streams de GA4 recebem dado do GTM e estão fora do acesso da V4

Levantado na quarta rodada da auditoria (vii), em 11/09, cruzando os 16 measurement IDs do parque de
GTM com a API de administração do GA4.

| Measurement ID | Onde aparece |
|---|---|
| `G-SP7M9MSCB3` | `4. VivaReal - Container BLOG`, `4. ZapImóveis - LANDING PAGES`, `6. ZapImóveis - DATAZAP/GEOIMOVEL` |
| `G-28CQ5W5559` | `3. ZapImóveis - Container CLICKSTREAM` |
| `G-XWEMHMPHXB` | `4. ZapImóveis - Container LANDING PAGES` |
| `G-CLVJ1JLDJF` | `www.datazap.com.br` |

Nenhum dos quatro está entre as **71 propriedades** visíveis a `gina@v4company.com`. Seis contêineres
mandam dado para destinos que a auditoria não alcança, e dois deles são de landing page, superfície
de captação.

**Três explicações possíveis, e elas levam a ações diferentes:** a propriedade existe e o acesso não
foi concedido; a stream foi excluída e a tag ficou apontando para o nada; ou o ID está errado. Só a
primeira é benigna.

**Ação:** pedir à OLX o acesso às quatro, ou a confirmação de que foram descontinuadas.
**Responsável:** Operador V4 junto a Mirella Mendonça · **Prazo:** antes do Comitê 1

---

## 🔴 28. O `begin_checkout` do anunciante privado do ZapImóveis nunca dispara

Achado 34 da auditoria (vii). O gatilho `255` de `GTM-PZ733B5` exige que `page_name` contenha, ao
mesmo tempo, `/anuncie-profissional/novo/autonomo/plano-contratacao/checkout` **e**
`/anuncie-profissional/novo/imobiliaria/plano-contratacao/checkout`. São caminhos irmãos, e o GTM soma
condições com E. O gatilho é impossível.

O `purchase` do mesmo fluxo funciona. **Então existe venda sem início de checkout**, e a taxa de
conversão de checkout do anunciante privado do ZapImóveis não é derivável.

**Por que é bloqueio de método:** a regra 8 deste repositório exige que a receita derivada do funil
bata com a declarada. Para esse recorte não há funil derivável. Qualquer forecast que use a taxa de
checkout do privado no ZapImóveis está usando número que o sistema não produz.

**Ação:** corrigir o gatilho (dois gatilhos separados, ou uma `MATCH_REGEX` com alternância) e, até
lá, **não usar taxa de checkout do anunciante privado do ZapImóveis em forecast**. O período anterior
à correção fica sem esse dado, não com dado ruim.
**Responsável:** time de dados da OLX, apontado pela V4 · **Prazo:** correção antes do Comitê 2; a
ressalva no forecast vale desde já

---

## 🟡 29. Duas chaves de API do Cloud Retail viajam no navegador, e ninguém confirmou a restrição

Encontrado em 11/09 na varredura de segredos anterior ao commit dos exports de GTM, não na auditoria.

O template nativo **Cloud Retail** do GTM está em duas tags ativas, cada uma com sua chave de API em
texto claro no parâmetro `cloudRetailApiKey`, as duas apontando para o projeto Google Cloud
`257705851106`:

| Contêiner | Tag | Conta |
|---|---|---|
| `GTM-NP4HWRN` · 2. VivaReal - Container Portal VR | `937` · Cloud Retail Tag | `4412254379` |
| `GTM-MKTZ2ZP` · 3. ZapImóveis - Container CLICKSTREAM | `2296` · Retail Tag | `2971905372` |

**Isso não é vazamento da V4.** A tag roda no navegador, então a chave já é servida a todo visitante
de `vivareal.com.br` e `zapimoveis.com.br`, e está no código-fonte das páginas. É a categoria que o
[guia de export](02-diagnostico/guia-export-gtm.md) previu: chave pública de SDK. Os valores ficam
onde já estavam, dentro do export bruto, e **não foram copiados para nenhum documento**.

**O que precisa de confirmação é a restrição.** Chave de Cloud Retail não é identificador passivo
como um ID de pixel: ela **grava evento de usuário** no projeto. Sem restrição de referenciador HTTP
no console do Google Cloud, qualquer um que leia o código-fonte pode escrever eventos no catálogo e
contaminar o modelo de recomendação dos dois portais.

**Ação:** pedir à OLX a confirmação de que as duas chaves têm restrição de referenciador e de API.
É uma tela do console e não depende da V4.
**Responsável:** Operador V4 junto ao time de dados da OLX · **Prazo:** sem urgência de comitê,
mas antes do fim do Ciclo 1

---

## 🔴 30. Cinco meses sem jornada de ciclo de vida, e o tamanho disso não está medido

Achado 1 da [auditoria (i)](02-diagnostico/auditoria-i-crm-marketing.md), levantado nas sessões de
CRM de 09 e 10/09.

A migração para o Campana desligou as jornadas de ciclo de vida para **todo cliente novo**: Autos
desde abril, Imóveis desde julho. Quem entrou no ambiente novo não recebeu onboarding, educacional,
retenção preventiva, upsell nem recuperação. Só transacional e billing, que são de outros times.

> **Michelle Morais**, 09/09 (00:26:09): *"a gente tá desde março, desde abril até agora, sem
> conversar dentro de um ciclo de vida com esse cliente de autos."*

**Por que é pendência e não só achado.** O achado é estrutural e já está registrado. O que falta é
**tamanho**, e sem ele não dá para ordenar a trava nem alimentar o forecast:

| O que pedir | Por quê |
|---|---|
| Nº de clientes novos no Campana, por vertical e por mês, desde abril | É o denominador da coorte afetada |
| Churn dessa coorte contra o da coorte imediatamente anterior, mesma janela de vida | É a medida do que a parada custou |
| Receita da coorte, para converter a diferença em reais | Sem isso o achado não entra em forecast |

A OLX tem o dado: o funil B2B com MQL, SQL e vendas, por vertical e por período, existe no Looker
sobre BigQuery (28/08 e 10/09, 01:02:16). É extração, não construção.

**Cuidado de leitura:** a comparação de coortes vai carregar o efeito da própria migração, não só o
da ausência de CRM. Pedir junto qualquer outra mudança de preço, produto ou política comercial na
janela, senão a diferença vira causa única por descuido.

**Ação:** pedir as três linhas acima no grupo do projeto, junto com o link do dashboard.
**Responsável:** Operador V4 + Michelle Morais · **Prazo:** antes do fechamento de (i), **17/09**

---

## 🔴 31. A saída da Blip não está decidida, e 100% da aquisição de CRM depende dela

Achado 4 da [auditoria (i)](02-diagnostico/auditoria-i-crm-marketing.md).

Duas pessoas da OLX, na mesma sala, em 09/09:

| Quem | Posição |
|---|---|
| Eduardo Santos, dono técnico de Sales e Service Cloud | *"teoricamente a BP vai morrer"* · *"a gente tem um down time muito grande com eles"* · **"não funciona"** · a Blip nem foi convidada para o bid de disparo de WhatsApp |
| Mirella Mendonça, marketing | *"pelo que eu entendi hoje na reunião, isso não está pacificado de que Blip vai morrer"* |

Enquanto a decisão não sai, o time de CRM investe horas em **integrar ao Marketing Cloud a
ferramenta que o time técnico quer desligar**, e há agenda marcada para isso. Substituição prevista
para o **Q1**, com a discussão comercial ainda por acontecer.

**Por que isso é da V4 e não só da OLX:** a Blip é o gargalo declarado de três coisas ao mesmo
tempo, automação de disparo, tag de campanha e atribuição de CRM. Qualquer injeção que passe por
CRM esbarra nela, e a Árvore de Pré-Requisitos precisa saber se a ferramenta fica ou sai antes de
desenhar o obstáculo.

**Ação:** pedir a posição formal, uma frase, no grupo do projeto: a Blip fica como broker de
disparo ou é substituída, e com que data. Não é a V4 que decide, mas é a V4 que precisa registrar.
**Responsável:** Eduardo Santos, via operador · **Prazo:** antes do Comitê 1, **23/09**

---

## 🟠 32. O material de CRM foi apresentado em tela e não chegou

Quatro entregas foram prometidas em 09 e 10/09 e, até **14/09**, nenhuma chegou:

| # | O que | DRI declarado |
|---|---|---|
| 1 | Acesso ao **Miro** com o mapeamento de todas as jornadas, B2B e B2C | Michelle Morais |
| 2 | Planilha de **links, logins e acessos** a dashboards e plataformas internas | Michelle Morais |
| 3 | Link do dashboard do **Looker** com resultados de canais de marketing e CRM | Michelle Morais |
| 4 | Link do dashboard de **CRM offline**, que teve um bug corrigido em 09/09 | Michelle Morais |

Somam-se os **slides** apresentados nas duas sessões (fluxo de disparo, comparativo DEX legado vs.
Campana, plano de migração de jornadas), que não foram enviados.

**Consequência prática:** o mapa de 15 jornadas da [auditoria (i)](02-diagnostico/auditoria-i-crm-marketing.md)
foi reconstruído a partir de uma tela compartilhada. Ele serve para o diagnóstico e **não serve
como fonte citável** em comitê enquanto o Miro não chegar. É o mesmo problema do slide FLUXOS
([pendência 20](#-20-o-slide-fluxos-não-está-versionado-e-todo-o-mix-de-canais-depende-dele)), e já
é a segunda vez.

**Ação:** cobrar as quatro no grupo, em uma mensagem só, com o pedido do bloco A junto.
**Responsável:** Operador V4 + Michelle Morais · **Prazo:** **17/09**, para entrar em (i)

---

## 🟠 33. A base pessoal trafega em planilha até a Blip, e a perda na higienização não tem número

Achados 5 e 6 da [auditoria (i)](02-diagnostico/auditoria-i-crm-marketing.md). São dois problemas
com a mesma origem: não há integração entre o Marketing Cloud e a Blip.

**Parte 1, a exposição.** O ciclo de cada disparo é extrair a base, tratar, quebrar por volume
diário, exportar e subir à mão. Quem levantou o risco foi a própria OLX:

> **Mirella Mendonça**, 09/09 (00:48:35): *"o item quatro, cinco, o sete e o oito [...] são super
> críticos porque envolve LGPD, envolve inúmeros outros riscos aqui pra gente."*

A V4 registra porque o desenho da injeção depende disso, **não porque o achado seja nosso**, e não
opina sobre conformidade. É o segundo registro de dado pessoal fora de ambiente controlado neste
projeto, depois do [achado 26 da auditoria (vii)](02-diagnostico/auditoria-vii-rastreamento.md),
que manda e-mail, telefone, CEP e gênero ao GA4 como propriedade de usuário.

**Parte 2, o número que não existe.** Rafael Corazza perguntou o tamanho da perda na higienização e
a resposta veio pela metade: **CEP ausente em mais de 50%** `[E]`, e o percentual de correção de
nome ninguém lembrou. Sem esse número, não dá para dizer quanto da base elegível é perdida por
qualidade de dado, que é justamente o que separa um problema de **volume** de um problema de
**cadastro**.

E há uma contradição a resolver junto: Michelle trata o CEP como campo mandatório da qualificação
do bot, Juliana Arndt diz que dá para disparar sem ele, o fluxo só demora mais (10/09, 00:09:23).
As duas leituras produzem bases elegíveis de tamanhos diferentes.

**Ação:** pedir a Evelyn Milare o antes e depois da automação de higienização, em número de
registros, por vertical. E fechar, numa frase, se o CEP é bloqueio ou atrito.
**Responsável:** Operador V4 + Evelyn Milare · **Prazo:** **17/09**

---

## 🟡 34. Duas datas para a ativação do onboarding de Imóveis

A primeira, e até agora única, jornada de ciclo de vida religada no ambiente novo tem duas datas na
mesma fonte:

| Onde | Data |
|---|---|
| Resumo automático do Gemini, 10/09 | *"o onboarding ativado em **31 de maio**"* |
| Transcrição, 10/09 (00:26:49) | *"foi essa aqui que aconteceu agora no **dia 31**"* |
| Transcrição, 10/09 (00:41:27) | Evelyn Milare: *"a gente ativou semana passada, se não me engano. Retrasada. É bem novinha"* |

As três não fecham. "Semana retrasada" a partir de 10/09 cai na semana de 24 a 30/08, o que aponta
para **31/08**, e 31/05 seria incompatível com "bem novinha" e com a migração de Imóveis ter
começado em julho. **A leitura provável é 31/08**, e leitura provável não entra em documento de
cliente.

**Por que importa:** é a data que marca o fim da janela sem onboarding em Imóveis. Três meses de
diferença mudam o tamanho da coorte da [pendência 30](#-30-cinco-meses-sem-jornada-de-ciclo-de-vida-e-o-tamanho-disso-não-está-medido).

**Ação:** confirmar a data com Michelle Morais. Pergunta de uma linha.
**Responsável:** Operador V4 · **Prazo:** **17/09**

---

## 🟡 35. A Meta encarece o WhatsApp em outubro, e é o único canal de aquisição de CRM que restou

Achado 9 da [auditoria (i)](02-diagnostico/auditoria-i-crm-marketing.md).

> **Michelle Morais**, 10/09 (00:14:04): *"o e-mail hoje tá esquecido, a gente não faz mais nenhum
> tipo de disparo de e-mail para aquisição"* · *"a gente tem uma regra nova que a meta tá
> implantando até outubro, que deve encarecer a forma de cobrança que os disparos de WhatsApp vão
> passar a ter."*

O canal de custo marginal quase zero saiu na migração, e ficou só o canal pago, prestes a ficar mais
caro, carregando 99% a 100% da aquisição de CRM.

**O que não se sabe:** quanto a OLX gasta hoje em disparo de WhatsApp, e qual o impacto da nova
regra sobre esse gasto. Sem os dois, não dá para dizer se isto é ajuste de rodapé ou alavanca de
margem, e a meta do projeto é **margem**.

**Ação:** pedir o custo mensal de disparo de WhatsApp dos últimos 12 meses e a estimativa de
impacto que a OLX já tenha feito. Se não houver estimativa, isso é achado, não lacuna.
**Responsável:** Operador V4 + Michelle Morais · **Prazo:** antes do Comitê 1, **23/09**

---

## Itens resolvidos

*(mover para cá com data e responsável quando fechados)*
