# Trava de Cegueira · diagnóstico

**Pontuada em 11/09/2026** · Score **5 de 25** · Confiabilidade **parcial**

> **A OLX mede navegação em altíssimo detalhe e resultado de negócio em lugar nenhum.**

A Trava de Cegueira é **pré-condição, não restrição de receita**. Ela não disputa o posto de trava
governante. O que um score de 5 significa é outra coisa, e precisa estar dita no Comitê 1: **enquanto
ela não subir, o score das outras sete travas nasce com confiabilidade reduzida.**

---

## O teste que resume o diagnóstico

Em 11/09 a V4 fez ao sistema a pergunta que um decisor faria:

> *Quantos anunciantes profissionais novos a OLX ganhou em agosto, e quanto custou cada um?*

O sistema não responde. E o caminho até o "não" é o diagnóstico inteiro.

A propriedade `GA4 Grupo OLX` (`503925542`) carrega `ads.grupoolx.com.br`, `imoveis.`, `autos.`, o
institucional e `vender.olx.com.br`: **toda a superfície B2B do escopo contratado**. Em agosto de
2026 ela registrou **10 nomes de evento**, e os dez são automáticos:

| Evento | Agosto/2026 |
|---|---:|
| `page_view` | 1.406.689 |
| `session_start` | 1.203.225 |
| `first_visit` | 862.074 |
| `user_engagement` | 224.592 |
| `scroll` | 137.399 |
| `click` | 127.734 |
| `form_start` | 7.598 |
| **`form_submit`** | **506** |
| `file_download` | 296 |
| `view_search_results` | 54 |

Nenhum evento de lead. Nenhum de cliente. Nenhum de receita.

**O melhor indicador de resultado B2B que a OLX tem em agosto são 506 envios de formulário**,
capturados automaticamente pelo navegador, que não dizem qual formulário foi enviado, o que a pessoa
queria, nem se virou cliente. De 862 mil primeiras visitas, é o único desfecho observável, e ele não
é um desfecho de negócio.

---

## As cinco dimensões

| | Dimensão | Nota | |
|---|---|:---:|---|
| **A** | Existência de dados básicos (lead, cliente, receita separados) | **1** | 🔴 |
| **B** | CAC calculado e confiável | **0** | 🔴 |
| **C** | LTV e payback calculados | **0** | 🔴 |
| **D** | Fonte única de verdade (CRM/BI) vs. planilhas paralelas | **2** | 🔴 |
| **E** | Cadência de leitura dos indicadores | **2** | 🔴 |
| | **Total** | **5 / 25** | **Estruturalmente travada** |

### A · Dados básicos · nota 1

A receita **existe e está separada**, mas em outro lugar: a série A1, 20 meses abertos por unidade,
segmento e produto, que chegou como anexo de e-mail em 28/08. Lead e cliente **não existem** como
dado no sistema digital. É por isso que a nota é 1 e não 0.

### B · CAC · nota 0

O investimento é mensurável: o V4MOS ingere Google Ads. A contagem de clientes não existe em camada
nenhuma. **Falta o denominador, não a ferramenta.**

> **Nota 0 e não `null`, e a diferença importa.** `null` é para dimensão cujo dado a V4 não conseguiu
> obter. Aqui o dado foi obtido e demonstra ausência: está provado que o CAC não é produzível pelo
> sistema atual.

### C · LTV e payback · nota 0

Sem identidade de cliente não há coorte, e sem coorte não há LTV nem payback. Os itens **A2** (funil
comercial com volumes por etapa) e **A3** (ticket médio, ciclo de vendas) seguem não entregues. O
churn de 8 a 10% ao mês que circula no modelo da meta está registrado como não verificado
([PENDENCIAS 22](../PENDENCIAS.md)).

### D · Fonte única de verdade · nota 2

Existe camada de BI e existe um time que responde por ela, e é por isso que a nota não é menor. Não
chega a 3 porque não há fonte única:

- o GTM escreve em **16 measurement IDs**, mapeados para **8 propriedades** identificadas mais **4
  streams que a V4 não enxerga** ([PENDENCIAS 27](../PENDENCIAS.md));
- há **escrita dupla deliberada**: as tags `[GA4 - Verticalizado]` e `[GA4 - Unificado]` mandam o
  mesmo evento para duas propriedades, então qualquer soma entre propriedades conta o mesmo lead duas
  vezes;
- **Salesforce Marketing Cloud e RD Station convivem** no GTM, sem oficialidade declarada;
- e **o número de receita que o projeto usa chegou por e-mail**, não de um sistema.

### E · Cadência de leitura · nota 2

Aqui está o ponto mais importante deste diagnóstico, e ele não é o que parece.

**A cadência existe, é diária e é disciplinada.** No kickoff de 24/08, Iuna Scheffler e Matheus
Rodrigues descrevem a receita como a principal métrica diária de acompanhamento, com EBITDA
monitorado em paralelo e metas abertas por vertical, linha e canal. Há um gerente de planejamento
financeiro dedicado a acompanhar performance.

**O problema não é falta de rotina. É o que a rotina lê.**

> Uma cadência que lê **receita e EBITDA** sem ler **CAC, LTV e origem de cliente** informa, mas não
> permite dirigir. Ela diz que o número caiu. Não diz onde mexer.

A nota não passa de 3 também pela regra 6 do método: a evidência é transcrição de reunião, não
dashboard verificado. Os dashboards internos existem, sob responsabilidade de Lu Machim, e os links
ficaram como ação pendente em 28/08 e nunca foram compartilhados.

---

## Inventário de Indicadores

Entrada visual obrigatória da Trava de Cegueira: o que existe, onde vive, quem lê, com que
frequência.

| Indicador | Existe | Onde vive | Quem lê | Frequência |
|---|:---:|---|---|---|
| Receita | ✅ | FP&A, planilha e dashboards internos | Matheus Rodrigues, Iuna Scheffler | **diária** |
| EBITDA | ✅ | FP&A | FP&A e diretoria | monitorado |
| Sessões e navegação | ✅ | GA4, 8 propriedades | não identificado | não identificada |
| Envio de formulário | 🟡 | GA4, evento automático | não identificado | não identificada |
| Lead B2B | ❌ | tag `lead_b2b` existe no GTM e não chega à propriedade B2B | - | - |
| Lead qualificado | ❌ | **definido** no GA4 como `qualify_lead` desde 05/09/2025 | - | - |
| Cliente novo | ❌ | **definido** no GA4 como `close_convert_lead` desde 05/09/2025 | - | - |
| CAC | ❌ | - | - | - |
| LTV | ❌ | - | - | - |
| Payback | ❌ | - | - | - |
| Churn | 🟡 declarado | modelo da meta, 8–10% ao mês | - | não verificado |

**A linha que mais diz é a do meio.** `qualify_lead` e `close_convert_lead` são as duas etapas que
faltam para fechar o funil B2B, são eventos **personalizados** (alguém os nomeou), e estão definidos
como evento-chave há mais de um ano. **Zero ocorrência em 2,19 milhões de sessões.**

Alguém do grupo sabia qual era o funil de receita B2B a ponto de nomear as duas etapas. Ninguém
fechou o circuito entre essa definição e o que o site empurra para o dataLayer.

---

## Três sintomas que o diagnóstico descartou

| Sintoma | Por que não procede |
|---|---|
| "Ninguém definiu o que é conversão" | **Falso**, e foi afirmado por engano na varredura de 31/08. Os eventos-chave existem desde 2025. O problema é emissão, não definição. Corrigido em [PENDENCIAS 13](../PENDENCIAS.md) |
| "Falta ferramenta ou acesso" | **Falso.** O GA4 responde tudo em leitura por API, o GTM foi exportado inteiro nas quatro contas, o V4MOS ingere Google Ads |
| "Falta capacidade técnica na casa" | **Falso.** A conta `Checkout Unificado - PRO` mostra arquitetura deliberada e gatilhos corretos. A casa sabe fazer |

Os três descartes empurram a causa para o mesmo lugar: não é falta de instrumento, de acesso nem de
competência.

---

## Hipótese causal

> A empresa opera sob a política implícita de **tratar a medição como responsabilidade de quem
> implementa cada superfície, e não de quem responde pela receita**, o que gera **um sistema que mede
> navegação em altíssimo detalhe e resultado de negócio em lugar nenhum, com o funil B2B nomeado no
> GA4 e nunca emitido pelo site**, limitando **a capacidade de dizer quanto custa e quanto vale um
> anunciante profissional, e portanto de decidir onde investir**.

É **hipótese**. A validação acontece na CRT (`/dre-udes-crt`), sobre as UDEs das entrevistas, nunca
aqui.

A auditoria (vii) sustenta a mesma política pelo lado do GTM, com prova em quatro contas
independentes: o template de consentimento correto está em 22 contêineres e o editado está nos três
Masters, que são os que rodam. **Os dois lados do sistema, medidos por caminhos diferentes, apontam a
mesma causa.**

---

## O que fazer, em ordem

| | Ação | Custo | Quando |
|---|---|---|---|
| 1 | **Subir a retenção** das propriedades `503925542` e `494455315` de 2 para 14 ou 50 meses | um clique | **hoje** |
| 2 | Emitir `qualify_lead` e `close_convert_lead` no dataLayer das superfícies B2B | implementação | Ciclo 1 |
| 3 | Declarar a fonte oficial de verdade entre Salesforce MC e RD Station | decisão | antes do Comitê 1 |

A ação 1 vem primeiro por um motivo que não é de prioridade estratégica: **é o único item deste
diagnóstico que piora enquanto ninguém age.** O dado que passa de 2 meses é descartado e não volta.
Todo dia de espera custa um dia de história que nenhuma correção futura recupera.

A ação 2 é barata porque **metade dela já foi feita**: o nome do evento existe, já é evento-chave,
já está esperando. Falta o site empurrar.

---

## O que este diagnóstico não viu

- **Camada experiencial sobre as ferramentas, não sobre o time.** A V4 testou o sistema, não
  entrevistou quem o usa. As entrevistas de 16 e 17/09 podem mudar a leitura da dimensão E.
- **Dashboards internos nunca verificados.** Existem, e os links são ação pendente desde 28/08.
- **Sem acesso a Salesforce Marketing Cloud nem ao CRM comercial**, o que limita as dimensões D e A.

Por isso a confiabilidade é **parcial**, e não alta.
