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

## 🟠 11. V4MOS com o Google ingerido, Meta ainda vazio

Revalidado em **24/08/2026**, depois de a V4 aceitar o convite do MCC VivaReal.

| Lado | Estado |
|---|---|
| **Google Ads** | ✅ Ingerindo. 655 registros de campanha, 8 campanhas distintas, de 16/05/2025 a 22/06/2026, R$ 1,91 mi de investimento e 7,1 mi de cliques |
| **Meta Ads** | 🟠 Vazio. Os seis endpoints do Facebook devolvem `data: []`, coerente com as duas contas de anúncio ainda pendentes de aprovação na OLX |

**Atualização de 01/09 · agora com evidência de interface, não só de API.** A V4 já enxerga o
portfólio empresarial **`New OLX Brasil`**. Dentro dele, em Contas → Páginas, existe **uma única
página**, `Grupo OLX` (ID `1239097169583910`), e a aba **Ativos conectados** devolve
**"Nenhum ativo conectado"**.

Duas leituras, e convém não confundi-las:

1. **A confirmação esperada:** nenhuma conta de anúncio foi compartilhada com a V4. Isso explica os
   seis endpoints de Facebook do V4MOS devolverem vazio, não é falha técnica, é ativo não concedido.
2. **A leitura que precisa de confirmação:** se a página `Grupo OLX` de fato não tem **nenhum** ativo
   conectado no portfólio, isso quebra vínculo de página com conta de anúncio, pixel e catálogo, e
   afeta lead ads, Advantage+ e atribuição em nível de página. **Mas pode ser artefato de permissão:**
   a interface mostra o que o usuário logado enxerga, não necessariamente o que existe. Confirmar com
   alguém que tenha visão administrativa antes de tratar como achado.

**Ação:** cobrar a aprovação das contas `612188193108418` (VR ZAP+) e `1742214902479721`
(OLX Autos B2B). Sem elas, a auditoria (vi) fecha só pela metade e o CAC do forecast
fica sem o custo de Meta. Pedir junto: acesso de parceiro no portfólio `New OLX Brasil` com os
ativos atribuídos, e confirmação de quantas páginas e contas existem de fato.

---

## 🔴 12. As campanhas visíveis no Google Ads parecem ser B2C, não B2B

Achado ao ler o primeiro dado real que chegou pelo V4MOS. As 8 campanhas do MCC recém-liberado:

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
   R$ 1,91 mi de investimento; o conjunto vinculado ao ZapImóveis é outra ordem de grandeza.
2. A conta liberada pode ser uma conta lateral, não a conta principal de nenhuma das duas frentes.

**Ação revista:** pedir a relação completa das contas de Google Ads do grupo, com o dono e a
finalidade de cada uma, e identificar **qual carrega a captação de anunciante**. Este é o pedido que
mais muda o resultado da auditoria (vi).
**Responsável:** Michelle Morais · **Prazo:** antes da apresentação de 29/09

---

## 🔴 13. O GA4 do grupo não mede conversão: e onde mede, mede errado

Achado da varredura de 31/08, primeira leitura possível depois de o GA4 ser liberado. Sustenta a
auditoria **(vii) Rastreamento Completo**, a prioritária, e é evidência direta de **Trava de Cegueira**.

### Propriedades de alto volume sem nenhum evento-chave

| Propriedade | ID | Volume | Eventos-chave |
|---|---|---|---|
| GA4 Grupo OLX | `503925542` | 2,47 mi de sessões (jun–ago) | **Nenhum.** Só eventos automáticos de enhanced measurement |
| Autos 360 (Ex-Altimus) | `516288559` | 1,14 mi de sessões (jun–ago); 449 nomes de evento distintos | **Nenhum** |
| ANAPRO | `469847974` | 11,19 mi de `page_view` (jun–ago) | **Nenhum** |
| OLX PRO | `382768600` | 119 sessões em 3 meses, só tráfego direto | **Nenhum** |
| OLX Pro Landing | `382776122` | Zero evento no período | - |

O caso do **Autos 360** é o mais eloquente: alguém instrumentou 449 eventos distintos e não marcou
um único como conversão. O dado existe, ninguém definiu o que é resultado. E **OLX PRO**, o produto
do anunciante profissional, exatamente o recorte B2B contratado, registra 119 sessões em três meses,
o que significa que a propriedade está órfã, não que o produto não tem tráfego.

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
| Meta, 01/09 | Portfólio `New OLX Brasil` visível | **"Nenhum ativo conectado"**: nenhuma conta de anúncio compartilhada (pendência 11) |

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

## Itens resolvidos

*(mover para cá com data e responsável quando fechados)*
