# Auditorias / Diagnósticos Contratados

O contrato do Grupo OLX (cláusula 1.2) inclui **9 diagnósticos técnicos** dentro do escopo do DR-E —
não são produtos TER contratados à parte.

## Mapa: diagnóstico → insumos → trava provável

| # | Diagnóstico contratado | Bloco de dados | Travas que informa | Status |
|---|---|---|---|---|
| **i** | CRM Marketing (Salesforce Marketing Cloud) | [B](checklist-dados-e-acessos.md#b-crm-marketing) | Interesse · Retenção | ⚪ |
| **ii** | Ambientes CRO/SEO (domínios B2B) | [C](checklist-dados-e-acessos.md#c-ambientes-croseo-domínios-b2b) | Exposição · Interesse | ⚪ |
| **iii** | GEO — IA e Buscas Generativas | [D](checklist-dados-e-acessos.md#d-geo-ia-e-buscas-generativas) | Exposição · Atenção | ⚪ |
| **iv** | Criativos Ads & Mensagens | [E](checklist-dados-e-acessos.md#e-criativos-ads--mensagens) | Atenção | ⚪ |
| **v** | Redes Sociais e Conteúdo Orgânico | [F](checklist-dados-e-acessos.md#f-redes-sociais-e-conteúdo-orgânico) | Exposição · Atenção | ⚪ |
| **vi** | Mídia Paga (Google e Meta) | [G](checklist-dados-e-acessos.md#-g-mídia-paga-google-e-meta--prioritário) | Exposição · Atenção · Qualificação | ⚪ |
| **vii** | Rastreamento Completo (GA4 e GTM) | [H](checklist-dados-e-acessos.md#-h-rastreamento-completo-ga4-e-gtm--prioritário) | **Cegueira** (pré-condição) | ⚪ |
| **viii** | Páginas de Captura (LPs) e Fluxos de Conversão | [I](checklist-dados-e-acessos.md#i-páginas-de-captura-e-fluxos-de-conversão) | Interesse · Compromisso | ⚪ |
| **ix** | Pré-Vendas, Qualificação e Sales Engagement | [J](checklist-dados-e-acessos.md#-j-pré-vendas-qualificação-e-sales-engagement--prioritário) | Qualificação · Compromisso · Decisão | ⚪ |

> O **bloco A** (Visão de Negócio e Fluxo de Receita) não corresponde a um diagnóstico técnico —
> alimenta diretamente o **Mapeamento do Fluxo de Receita** e o **Forecast**.

## Sequência recomendada

Seguindo a lógica de investigação **de baixo para cima** do método
([Regra de Goldratt](../00-playbook/01-fundamentos-dr-ote.md#lógica-de-investigação-de-baixo-para-cima)):

1. **(vii) Rastreamento (GA4/GTM)** — primeiro de todos. Se houver Cegueira, todo o resto é achismo.
2. **(ix) Pré-Vendas, Qualificação e Sales Engagement** — mais próximo do dinheiro.
3. **(viii) LPs e Fluxos de Conversão** — Compromisso.
4. **(i) CRM Marketing** — Retenção e nutrição.
5. **(vi) Mídia Paga** — Qualificação e eficiência de aquisição.
6. **(iv) Criativos & Mensagens** e **(v) Redes Sociais** — Atenção.
7. **(ii) CRO/SEO** e **(iii) GEO** — Exposição.

> Isso **não** significa que o diagnóstico começa pelo fundo do funil e para lá. Todas as travas são
> diagnosticadas; a sequência otimiza o tempo até a hipótese governante.

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
