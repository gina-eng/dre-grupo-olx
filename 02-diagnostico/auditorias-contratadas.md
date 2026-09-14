# Diagnósticos Contratados

O contrato do Grupo OLX (cláusula 1.2) inclui **9 diagnósticos técnicos** dentro do escopo do DR-E,
não são produtos TER contratados à parte.

## Reajuste de 03/09: os nove rodam juntos, em 15 dias

A grade de doze semanas em duas ondas continua sendo o **desenho do ciclo**, e a lógica de
investigação que a ordena não mudou. O que mudou duas vezes em três dias foi a escala de leitura:

1. **01/09 · a grade saiu de semanas e entrou em dias.** GA4 e GTM entraram, e apareceu na agenda
   uma apresentação de diagnósticos em 10/09 que não existia em documento nenhum. Quatro
   diagnósticos andavam, cinco ficavam congelados por acesso não concedido.
2. **03/09 · o critério de habilitação perdeu a função.** A OLX marcou a entrega do **lote completo
   de acessos para as 17h de 03/09**, e a V4 dimensionou os nove em **15 dias corridos**. Com todos
   habilitados ao mesmo tempo, não há mais o que separar por acesso. A apresentação de 10/09 foi
   **adiada para 24/09**, e o Comitê 1 de 17/09 foi para **01/10**.

Grade dia a dia em
[04-execucao/sprint-diagnosticos-10-a-18-09.md](../04-execucao/sprint-diagnosticos-10-a-18-09.md);
marcos e o deslize dos Comitês 2 e 3 em
[04-execucao/cronograma-e-marcos.md](../04-execucao/cronograma-e-marcos.md).

### O critério de corte desta janela

> **Hora do time da OLX.** O gargalo deixou de ser acesso e nunca foi hora da V4. Passou a ser a
> agenda de quem, do lado do cliente, dá entrevista, libera gravação e valida achado.

Isso **não substitui** a lógica de baixo para cima, que continua ordenando o ciclo. É um segundo
filtro, de curto prazo, aplicado sobre ela, como era o de habilitação até 02/09.

## Mapa: diagnóstico → insumos → estado projetado

| # | Diagnóstico contratado | Bloco | Janela | Custo de hora da OLX | Travas que informa |
|---|---|---|---|---|---|
| **vii** | Rastreamento Completo (GA4 e GTM) | [H](checklist-dados-e-acessos.md#-h-rastreamento-completo-ga4-e-gtm--prioritário) | 09–14 set | 🟢 Baixo, só os exports das 3 contas de GTM que faltam | **Cegueira** (pré-condição) |
| **ii** | Ambientes CRO/SEO (domínios B2B) | [C](checklist-dados-e-acessos.md#c-ambientes-croseo-domínios-b2b) | 09–15 set | 🟢 Baixo, camada pública já rodou; falta Search Console | Exposição · Interesse |
| **viii** | Páginas de Captura e Fluxos de Conversão | [I](checklist-dados-e-acessos.md#i-páginas-de-captura-e-fluxos-de-conversão) | 09–18 set | 🟢 Baixo, export do Unbounce e Mouseflow | Interesse · Compromisso |
| **vi** | Mídia Paga (Google e Meta) | [G](checklist-dados-e-acessos.md#-g-mídia-paga-google-e-meta--prioritário) | 10–21 set | 🟠 Médio, mapa de contas e finalidade de cada uma | Exposição · Atenção · Qualificação |
| **ix** | Pré-Vendas, Qualificação e Sales Engagement | [J](checklist-dados-e-acessos.md#-j-pré-vendas-qualificação-e-sales-engagement--prioritário) | 10–23 set | 🔴 **Alto**, entrevistas e gravações com consentimento | Qualificação · Compromisso · Decisão |
| **i** | CRM Marketing (Salesforce Marketing Cloud) | [B](checklist-dados-e-acessos.md#b-crm-marketing) | 14–22 set | 🟠 Médio, entrevista com o time de automação | Interesse · Retenção |
| **iv** | Criativos Ads & Mensagens | [E](checklist-dados-e-acessos.md#e-criativos-ads--mensagens) | 16–22 set | 🟠 Médio, acervo de peças e racional de campanha | Atenção |
| **v** | Redes Sociais e Conteúdo Orgânico | [F](checklist-dados-e-acessos.md#f-redes-sociais-e-conteúdo-orgânico) | 16–22 set | 🟢 Baixo, Business Suite e LinkedIn concedidos | Exposição · Atenção |
| **iii** | GEO: IA e Buscas Generativas | [D](checklist-dados-e-acessos.md#d-geo-ia-e-buscas-generativas) | 21–23 set | 🟢 Nenhum · roda de fora | Exposição · Atenção |

> ✅ **(i) saiu na frente e já tem documento.** As duas sessões de CRM aconteceram em **09 e
> 10/09**, antes do lote de acessos, e fecharam a camada experiencial com 16 achados em
> [`auditoria-i-crm-marketing.md`](auditoria-i-crm-marketing.md). A janela efetiva do diagnóstico
> passou a ser **11–17/09**, ver [sprint](../04-execucao/sprint-diagnosticos-10-a-18-09.md).

**Os nove rodam. Nenhum fica congelado, desde que o lote de 03/09 chegue utilizável, e não só
concedido.** Essa condicional é o que a tabela existe para não deixar esquecer: o GA4 já chegou uma
vez em nível Leitor, e o portfólio Meta já apareceu sem ativo conectado.

### A carga em paralelo quebra a regra de três, conscientemente

| Pico no período | 09–11/09 | 14–15/09 | 16–18/09 |
|---|---|---|---|
| Diagnósticos abertos | 4 | 5 | **6** |
| **Que cobram hora da OLX** | 3 | 4 | **5** |

A regra de no máximo três abertos por vez existe para proteger a agenda do cliente, e nos dias 16, 17
e 18/09 há **cinco frentes simultâneas** sobre o time do Grupo OLX. A mitigação é de **concentração,
não de redução**: as entrevistas de (ix), (i) e (iv) vão para dois blocos fechados, quarta 16 e quinta
17. O pico e os blocos são o mesmo dia de propósito, uma agenda tomada por duas manhãs custa menos
ao cliente do que cinco frentes cutucando todo dia durante uma semana.

### O que a compressão custa, por diagnóstico

**(ix) Pré-vendas é o único com risco de prazo estrutural.** Ele tinha três semanas de janela no
desenho original porque gravação de call envolve consentimento e LGPD, e esse trâmite não acelera
com pressão de cronograma. Comprimido a dez dias úteis, o cenário provável é fechar sem a camada
experiencial, o que o limita a nota ≤ 3 na Trava de Qualificação, pela
[regra 6 do repositório](../CLAUDE.md).

**(iii) GEO continua fechando por último**, agora por 21–23/09 em vez de S8–S9. Não é gargalo: não
depende de nada e não ajuda a nomear a restrição. Fecha em posição de folga, como sempre esteve.

> ⚠️ O **bloco A** (Visão de Negócio e Fluxo de Receita) não corresponde a um diagnóstico técnico,
> alimenta diretamente o **Mapeamento do Fluxo de Receita** e o **Forecast**. Ele **não é acesso a
> ferramenta, é entrega de dado**, e nenhuma concessão de 17h o destrava. Segue sem nenhum item
> recebido, e sem A1–A3 o forecast não tem matemática mesmo com os nove diagnósticos fechados.

## Sequência e janelas: o desenho original do ciclo

> A partir daqui o documento descreve a **grade de doze semanas**, que foi comprimida na janela de
> 04–18/09 pelo critério acima. Ela deixou de ser a grade de execução do Ciclo 1, mas continua sendo
> o **racional de sequência**, e é ela que volta a valer no Ciclo 2, quando os acessos já estarão
> maduros e o prazo não será de 15 dias.

A ordem segue a lógica de investigação **de baixo para cima** do método
([Regra de Goldratt](../00-playbook/01-fundamentos-dr-ote.md#lógica-de-investigação-de-baixo-para-cima)),
aplicada ao fluxo de ganho: primeiro fecha-se o caminho da aquisição até a captura, depois o que
acontece com o lead até virar receita, e por último o topo do funil.

O que define a janela de cada um não é só essa ordem: é **o que ele trava ou destrava**. Os nove não
rodam em paralelo por três motivos concretos:

1. Os acessos chegam em série, não de uma vez.
2. Cada diagnóstico consome tempo do time do Grupo OLX: entrevista, liberação, validação de achado.
   Oito diagnósticos abertos na mesma semana significam oito frentes de cobrança simultâneas.
3. A leitura de um melhora depois que o anterior fecha. Mídia paga lida antes do rastreamento é
   número sem lastro; GEO medido antes do posicionamento é linha de base do termo errado.

Por isso o Ciclo 1 executa os nove em **duas ondas**, com no máximo **três diagnósticos abertos por
semana**.

> ⚠️ **A grade é projetada, não fixa.** A sequência muda conforme o diagnóstico revelar onde o sistema
> trava: um achado da onda 1 pode puxar um diagnóstico da onda 2 para a frente, ou adiar outro que
> deixou de ser decisivo. É o método operando por estado do sistema, não desvio de cronograma. A grade
> é revalidada a cada comitê.

### Onda 1 · S2–S4 · da aquisição à captura, sustenta o Comitê 1

| Diagnóstico | Janela | Papel na decisão |
|---|---|---|
| (vii) Rastreamento Completo | S2–S3 | Pré-condição. Fecha antes de qualquer número entrar em material de comitê: se o GA4/GTM medem errado, os outros oito herdam o erro. |
| (viii) Páginas de Captura | S3–S4 | Onde o lead entra. Fecha a leitura de Interesse e Compromisso no ponto de conversão. |
| (vi) Mídia Paga | S2–S4 | O que se paga pela entrada. Abre junto com o rastreamento por causa do prazo de acesso e da ingestão no V4MOS. |

Os três formam a espinha do fluxo de ganho: **como se mede, onde o lead entra e o que se paga por ele**.

> O Comitê 1 não exige os nove fechados. Exige evidência suficiente para nomear **uma** restrição e
> refutar as concorrentes. Essa é a diferença entre prazo de método e prazo de calendário.

### Onda 2 · S4–S9 · completa o fluxo de ganho e volta ao topo

| Diagnóstico | Janela | Papel na decisão |
|---|---|---|
| (ix) Pré-Vendas | S4–S6 | O que acontece com o lead depois da captura. Três semanas de janela: gravações de call envolvem consentimento e LGPD. |
| (i) CRM Marketing | S5–S6 | Nutrição e retenção, o que sustenta a receita depois da primeira venda. |
| (iv) Criativos e Mensagens | S6–S7 | O que o mercado ouve hoje. Insumo do posicionamento e da proposta de valor, trabalhados na S6. |
| (v) Redes e Conteúdo Orgânico | S7–S8 | Mesma camada, no canal próprio. |
| (ii) CRO e SEO | S7–S8 | Alavanca de prazo longo: alimenta o plano de 90 dias e a matriz de expansão. |
| (iii) GEO | S8–S9 | Parte de linha de base zero e depende do posicionamento fechado para saber que termos monitorar. Fecha três semanas antes do Comitê 3, virando linha de base do Ciclo 2. |

A onda segue o dinheiro primeiro e o topo do funil depois. Ela roda durante a execução assistida do
plano de 30 dias, sem disputar acesso e agenda com ela.

> Isso **não** significa que o diagnóstico das travas fica pela metade no Comitê 1. Todas as travas são
> pontuadas na S3–S4 com a evidência disponível; os diagnósticos da onda 2 aprofundam as camadas que
> não decidem a restrição do ciclo e alimentam a decisão seguinte.

### Carga por semana: desenho original

| Semana | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 |
|---|---|---|---|---|---|---|---|---|
| Diagnósticos abertos | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 1 |

> A carga **executada** na janela de 09–23/09 é outra, e está no Gantt em dias: pico de **seis
> abertos** e **cinco cobrando hora do time da OLX**, contra o teto de três deste desenho. A
> diferença entre as duas tabelas é exatamente o preço do prazo de 15 dias.

## Registro por diagnóstico

Ao concluir cada diagnóstico, criar um arquivo `diagnostico-<n>-<nome>.md` nesta pasta com:

- **Escopo real auditado** (contas, propriedades, domínios, período)
- **Evidência analítica**: números, com fonte e recorte temporal
- **Evidência experiencial**: o que foi observado na prática (cliente oculto, navegação, gravações)
- **Limitações**: o que não foi possível auditar e por quê (acesso negado, ferramenta inexistente)
- **Score das dimensões** da(s) trava(s) que informa (0–5 cada, total 0–25)
- **Consolidação causal** no formato de política implícita
- **Entrada visual obrigatória** da trava correspondente

## Auditorias como produto TER (não contratadas)

Para referência, a V4 comercializa auditorias como produtos avulsos da categoria TER.
**Nenhuma foi contratada separadamente pelo Grupo OLX**: as nove acima estão embutidas no DR-E.
Se surgir necessidade de auditoria fora dessa lista, é **mudança material de escopo** e depende de
validação formal entre as partes (cláusula 1.5).
