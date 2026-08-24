# Auditorias / Diagnósticos Contratados

O contrato do Grupo OLX (cláusula 1.2) inclui **9 diagnósticos técnicos** dentro do escopo do DR-E —
não são produtos TER contratados à parte.

## Mapa: diagnóstico → insumos → trava provável

| # | Diagnóstico contratado | Bloco de dados | Janela | Onda | Travas que informa | Status |
|---|---|---|---|---|---|---|
| **vii** | Rastreamento Completo (GA4 e GTM) | [H](checklist-dados-e-acessos.md#-h-rastreamento-completo-ga4-e-gtm--prioritário) | S2–S3 | 1 | **Cegueira** (pré-condição) | ⚪ |
| **vi** | Mídia Paga (Google e Meta) | [G](checklist-dados-e-acessos.md#-g-mídia-paga-google-e-meta--prioritário) | S2–S4 | 1 | Exposição · Atenção · Qualificação | ⚪ |
| **ix** | Pré-Vendas, Qualificação e Sales Engagement | [J](checklist-dados-e-acessos.md#-j-pré-vendas-qualificação-e-sales-engagement--prioritário) | S3–S5 | 1 | Qualificação · Compromisso · Decisão | ⚪ |
| **viii** | Páginas de Captura (LPs) e Fluxos de Conversão | [I](checklist-dados-e-acessos.md#i-páginas-de-captura-e-fluxos-de-conversão) | S4–S5 | 1 | Interesse · Compromisso | ⚪ |
| **i** | CRM Marketing (Salesforce Marketing Cloud) | [B](checklist-dados-e-acessos.md#b-crm-marketing) | S5–S6 | 2 | Interesse · Retenção | ⚪ |
| **iv** | Criativos Ads & Mensagens | [E](checklist-dados-e-acessos.md#e-criativos-ads--mensagens) | S6–S7 | 2 | Atenção | ⚪ |
| **v** | Redes Sociais e Conteúdo Orgânico | [F](checklist-dados-e-acessos.md#f-redes-sociais-e-conteúdo-orgânico) | S6–S7 | 2 | Exposição · Atenção | ⚪ |
| **ii** | Ambientes CRO/SEO (domínios B2B) | [C](checklist-dados-e-acessos.md#c-ambientes-croseo-domínios-b2b) | S7–S8 | 3 | Exposição · Interesse | ⚪ |
| **iii** | GEO — IA e Buscas Generativas | [D](checklist-dados-e-acessos.md#d-geo-ia-e-buscas-generativas) | S8–S9 | 3 | Exposição · Atenção | ⚪ |

> A tabela está em ordem de execução, não na numeração da cláusula 1.2. As janelas são semanas do
> Ciclo 1 (S1 = 24/08/2026). Fonte da grade: [04-execucao/cronograma-e-marcos.md](../04-execucao/cronograma-e-marcos.md).

> O **bloco A** (Visão de Negócio e Fluxo de Receita) não corresponde a um diagnóstico técnico —
> alimenta diretamente o **Mapeamento do Fluxo de Receita** e o **Forecast**.

## Sequência e janelas

A ordem segue a lógica de investigação **de baixo para cima** do método
([Regra de Goldratt](../00-playbook/01-fundamentos-dr-ote.md#lógica-de-investigação-de-baixo-para-cima)):
primeiro o que está mais perto do dinheiro, por último o topo do funil.

O que define a janela de cada uma não é só essa ordem: é **o que ela trava ou destrava**. As nove não
rodam em paralelo por três motivos concretos:

1. Sete dependem de acesso que ainda não foi concedido, e acesso chega em série, não de uma vez.
2. Cada auditoria consome tempo do time do Grupo OLX: entrevista, liberação, validação de achado.
   Oito auditorias abertas na mesma semana significam oito frentes de cobrança simultâneas.
3. A leitura de uma melhora depois que a anterior fecha. Mídia paga lida antes do rastreamento é
   número sem lastro; GEO medido antes do posicionamento é linha de base do termo errado.

Por isso o Ciclo 1 executa as nove em **três ondas**, com no máximo **três auditorias abertas por
semana**, cada onda amarrada à decisão que precisa sustentar.

### Onda 1 · S2–S5 · sustenta o Comitê 1

| Auditoria | Janela | Papel na decisão |
|---|---|---|
| (vii) Rastreamento | S2–S3 | Pré-condição. Fecha antes de qualquer número entrar em material de comitê: se o GA4/GTM medem errado, as outras oito herdam o erro. |
| (vi) Mídia Paga | S2–S4 | Abre junto por causa do prazo de acesso e da ingestão no V4MOS. Fecha para o Comitê 1. |
| (ix) Pré-Vendas | S3–S5 | Três semanas de janela: gravações de call envolvem consentimento e LGPD. Entra no Comitê 1 com **leitura preliminar**; o dossiê fecha na S5. |
| (viii) LPs e Fluxos | S4–S5 | Fecha para o **plano de 30 dias** saído do Comitê 1, não para a decisão da restrição. |

> O Comitê 1 não exige as nove fechadas. Exige evidência suficiente para nomear **uma** restrição e
> refutar as concorrentes. Essa é a diferença entre prazo de método e prazo de calendário.

### Onda 2 · S5–S7 · sustenta o Comitê 2

| Auditoria | Janela | Papel na decisão |
|---|---|---|
| (i) CRM Marketing | S5–S6 | Interesse e Retenção. Primeira da onda porque é a mais próxima do dinheiro entre as três. |
| (iv) Criativos e Mensagens | S6–S7 | Insumo direto do posicionamento e da proposta de valor, trabalhados na S6. |
| (v) Redes e Conteúdo Orgânico | S6–S7 | Idem: o que o mercado ouve do Grupo OLX hoje. |

Rodam durante a execução assistida do plano de 30 dias, sem disputar acesso e agenda com ela.

### Onda 3 · S7–S9 · sustenta a fase Expandir e o Comitê 3

| Auditoria | Janela | Papel na decisão |
|---|---|---|
| (ii) CRO e SEO | S7–S8 | Alavanca de prazo longo: alimenta o plano de 90 dias e a matriz de expansão. |
| (iii) GEO | S8–S9 | Parte de linha de base zero e depende do posicionamento fechado para saber que termos monitorar. Fecha três semanas antes do Comitê 3, virando linha de base do Ciclo 2. |

> Isso **não** significa que o diagnóstico das travas fica pela metade no Comitê 1. Todas as travas são
> pontuadas na S3–S4 com a evidência disponível; as auditorias das ondas 2 e 3 aprofundam as camadas
> que não decidem a restrição do ciclo e alimentam a decisão seguinte.

### Carga por semana

| Semana | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 |
|---|---|---|---|---|---|---|---|---|
| Auditorias abertas | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 1 |

## Registro por diagnóstico

Ao concluir cada auditoria, criar um arquivo `diagnostico-<n>-<nome>.md` nesta pasta com:

- **Escopo real auditado** (contas, propriedades, domínios, período)
- **Evidência analítica** — números, com fonte e recorte temporal
- **Evidência experiencial** — o que foi observado na prática (cliente oculto, navegação, gravações)
- **Limitações** — o que não foi possível auditar e por quê (acesso negado, ferramenta inexistente)
- **Score das dimensões** da(s) trava(s) que informa (0–5 cada, total 0–25)
- **Consolidação causal** no formato de política implícita
- **Entrada visual obrigatória** da trava correspondente

## Auditorias como produto TER (não contratadas)

Para referência, a V4 comercializa auditorias como produtos avulsos da categoria TER.
**Nenhuma foi contratada separadamente pelo Grupo OLX** — as nove acima estão embutidas no DR-E.
Se surgir necessidade de auditoria fora dessa lista, é **mudança material de escopo** e depende de
validação formal entre as partes (cláusula 1.5).
