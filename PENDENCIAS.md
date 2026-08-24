# Pendências e Inconsistências

Registro vivo do que precisa de decisão, confirmação ou correção.
Atualizar sempre que um item for resolvido — com data e quem decidiu.

**Legenda de severidade:** 🔴 crítico (bloqueia ou expõe risco material) · 🟠 relevante · 🟡 a esclarecer

---

## 🔴 1. Divergência no valor do contrato — R$ 740k vs. R$ 752k

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

## 🔴 2. Gatilho do Bônus de Sucesso — três definições incompatíveis

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
[08-economics](00-playbook/08-economics-e-entregaveis-dr-e.md#modelo-de-bônus-opção-b)) — usar
esse argumento na construção dos KPIs.
**Responsável:** Gustavo Figueiredo + Mirella Mendonça · **Prazo:** após o diagnóstico inicial, antes do Comitê 1

---

## 🔴 3. Janela de garantia fecha no kick-off

A cláusula 2.3 do contrato OLX define a garantia como válida **até o primeiro encontro (Comitê de
Receitas)** — que é o próprio kick-off de 24/08. Diverge da SOW padrão DR-E (60 dias).

**Implicação:** a partir do kick-off, a resilição imotivada obriga a OLX ao pagamento integral das
parcelas vincendas. A OLX precisa entender isso — e a V4 precisa que o kick-off seja irrepreensível,
porque é literalmente o único ponto de saída do cliente.

**Ação:** garantir que o material do kick-off passe pelo gate de qualidade da Matriz.
**Responsável:** Consultor + GP · **Prazo:** 23/08

---

## 🟠 4. Numeração das travas — três padrões conflitantes

| Trava | Fundamentos DR-OTE | POPs / "Travas de Receita" | Fluxo de Estratégia |
|---|---|---|---|
| Exposição | T1 | Trava 7 | Trava 2 |
| Retenção | T7 | Trava 1 | Trava 8 |

Além disso, o **contrato do Grupo OLX fala em "7 travas"** enquanto o método opera com **8**
(a diferença é a Trava 0 — Cegueira, que é pré-condição, não restrição de receita).

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
e **Autos** (B2B). O contrato menciona "domínios B2B" apenas no diagnóstico (ii) — CRO/SEO.

**Perguntas em aberto:**
- O DR-E cobre as duas unidades ou apenas uma?
- Se cobre as duas, o diagnóstico das travas é feito por unidade (dois sistemas de receita) ou consolidado?
- O Success Fee será medido por unidade ou no consolidado?

> Isso não é detalhe. Em TOC, **cada sistema de receita tem sua própria restrição governante**.
> Duas unidades de negócio distintas podem ter travas diferentes — e o método exige
> **uma restrição por ciclo**.

**Ação:** delimitar no kick-off e registrar em ata.
**Responsável:** Consultor + Mirella · **Prazo:** 24/08

---

## 🟠 6. Acessos bloqueados

| Item | Status |
|---|---|
| Google Drive (data room) | 🟠 Restrito a `@olxbr.com`. Chamado aberto para criar contas para 3 pessoas da V4. **Aguardando.** |
| VR09 — ZAP+ MCC VivaReal (526-656-0190) | 🟡 Convite enviado — **falta a V4 dar o aceite** |
| VR — ZAP+ (612188193108418) | 🟠 Pendente de aprovação (OLX) |
| OLX \| Autos \| B2B (1742214902479721) | 🟠 Pendente de aprovação (OLX) |

**Ação:** verificar a caixa de `gina@v4company.com`, dar o aceite pendente e cobrar o restante.
**Responsável:** equipe de operações V4 · **Prazo:** 23/08

---

## 🟡 7. Estrutura de comitês — 12 encontros

O contrato descreve "12 encontros síncronos". O produto padrão DR-E prevê 8 boards online + 4
presenciais = 12. Coincide numericamente, mas o contrato **não distingue** online de presencial.

**Ação:** confirmar no kick-off quantos são presenciais e travar as datas na agenda dos C-Levels
(a dedicação de C-Level em comitê presencial é de ~10h no método — não se resolve com 1 semana de antecedência).

---

## 🟡 8. Papéis V4 não nominados

O método exige **Growth Planner da Matriz** (gate de qualidade obrigatório antes de cada comitê) e
**C-Level V4** (comitês presenciais). Nenhum dos dois está nominado.

**Ação:** definir antes do Comitê 1. Sem GP nominado, o gate de qualidade não acontece — e o gate
é a única proteção contra material fraco chegar ao Board da OLX.

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

**Ação:** cobrar a aprovação das contas `612188193108418` (VR ZAP+) e `1742214902479721`
(OLX Autos B2B). Sem elas, a auditoria (vi) fecha só pela metade e o CAC do forecast
fica sem o custo de Meta.

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

## Itens resolvidos

*(mover para cá com data e responsável quando fechados)*
