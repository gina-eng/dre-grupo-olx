# Modelos de projeto da matriz — mapeamento completo

Levantado em 2026-08-04 via MCP eKyte. Todos os modelos pertencem à empresa matriz
`6953` (" V4 Company"), workspace `26815`, e podem ser clonados para a `18239` com
`create_project_from_template`. Ver [CLAUDE.md](../CLAUDE.md) para as regras de uso.

## Atenção: `list_projects` esconde 62% do catálogo

`list_projects` devolve **no máximo 75 registros, ordenados alfabeticamente por nome, sem
offset**. Não existe parâmetro de paginação. Resultado: a chamada padrão
(`isModel=1`) corta em "Implementação de E-commerce - Advanced" e **tudo depois de "I" no
alfabeto fica invisível** — inclusive modelos que a squad usaria (Setup Inicial de Google
Ads, Traqueamento, Pack de Criativos, Régua de Relacionamento).

Comportamentos confirmados no teste:

- `createdBy` (10/20/30) é **ignorado** pela API — os três valores devolvem o mesmo payload.
- `textKey=10` (busca por Id) é match **exato**, não aceita substring.
- `textSearch` casa **nome, alias e descrição** — é o filtro que mais rende para escapar do corte.
- `responsibleId` funciona e particiona de verdade.
- `active` default é `1`: os pools `0` (inativo) e `2` (arquivado) só aparecem se pedidos.

**Como listar sem perder nada:** particione por `responsibleId` (Vinicius, Rafael, Leonardo)
e, para o Vinicius — que sozinho estoura o teto —, fatie por `textSearch` de família.
A correção definitiva é a eKyte expor `limit`/`offset` nessa tool.

## Números

| pool | `active` | modelos | observação |
|---|---|---|---|
| Ativos | `1` | 127 | catálogo utilizável |
| Inativos | `0` | 20 | legado 2023–2024, não usar |
| Arquivados | `2` | 52 | histórico, não usar |
| **Total** | | **199** | contra 75 visíveis por padrão |

Autores dos ativos: Vinicius (Matriz) 94 · Rafael Corazza 29 · Leonardo Rosa 4.

## Relevantes para a squad Flagship

Os modelos que encostam nas 4 cadeiras. `Tar.` = tarefas de projeto, `Esf.` = esforço previsto.

| id | modelo | Tar. | Esf. | dias |
|---|---|---|---|---|
| `271432` | Auditoria Técnica de Redes Sociais - Até 2 Redes | 13 | 15.0h | 11 |
| `271457` | Auditoria Técnica de Redes Sociais - Até 5 Redes | 13 | 20.5h | 11 |
| `274557` | Auditoria Técnica de Traqueamento Completo | 20 | 15.0h | 11 |
| `271304` | Auditoria de Criativos Ads & Mensagens | 11 | 14.0h | 11 |
| `271233` | Auditoria de Mídia Paga - Google Ads - Até R$10k | 13 | 9.0h | 11 |
| `271239` | Auditoria de Mídia Paga - Google Ads - R$10k a 25k | 13 | 14.5h | 11 |
| `271271` | Auditoria de Mídia Paga - Google Ads -Acima R$50k | 13 | 22.5h | 12 |
| `271242` | Auditoria de Mídia Paga - Google Ads -R$25k a 50k | 13 | 19.0h | 11 |
| `271232` | Auditoria de Mídia Paga - Meta Ads - Acima R$50k | 11 | 20.5h | 11 |
| `271201` | Auditoria de Mídia Paga - Meta Ads - Até R$10k | 11 | 7.5h | 11 |
| `271209` | Auditoria de Mídia Paga - Meta Ads - De R$10 a 25k | 11 | 13.0h | 11 |
| `271231` | Auditoria de Mídia Paga - Meta Ads - De R$25 a 50k | 11 | 16.5h | 11 |
| `247588` | Diagnóstico e Planejamento Meta e Google  10 à 30k | 18 | 36.5h | 18 |
| `287883` | Diagnóstico e Planejamento Meta e Google  30 à 50k | 18 | 43.5h | 18 |
| `287886` | Diagnóstico e Planejamento Meta e Google 50 à 100k | 18 | 58.5h | 18 |
| `248392` | Diagnóstico e Planejamento de Redes Sociais | 28 | 39.0h | 24 |
| `248863` | Elaboração de Identidade Visual - MIV | 17 | 33.5h | 14 |
| `249156` | Elaboração de Identidade Visual - Rebranding | 27 | 85.5h | 31 |
| `249145` | Elaboração de Identidade Visual -Branding Completo | 24 | 76.5h | 35 |
| `249086` | Elaboração de Identidade Visual – Brand Refresh | 24 | 53.5h | 21 |
| `254881` | Implementação Google Local Service Ads | 16 | 16.0h | 11 |
| `272117` | Implementação Google Meu Negócio | 12 | 9.5h | 6 |
| `254868` | Implementação Google My Business Profile | 13 | 10.0h | 7 |
| `272246` | Implementação SEO | 18 | 32.5h | 16 |
| `283757` | Implementação de Cap. e Edição de Fotos - Advanced | 17 | 55.0h | 12 |
| `283789` | Implementação de Cap. e Edição de Fotos - Basic | 16 | 26.0h | 11 |
| `287555` | Implementação de Cap. e Edição de Vídeo - Advanced | 21 | 62.0h | 13 |
| `287204` | Implementação de Cap. e Edição de Vídeo - Basic | 19 | 30.0h | 12 |
| `287302` | Implementação de Cap. e Edição de Vídeo - Pro | 19 | 45.5h | 13 |
| `285869` | Implementação de Captação e Edição de Fotos - Pro | 16 | 38.0h | 12 |
| `222203` | Implementação de Landing Page | 8 | 17.8h | 14 |
| `272296` | Implementação de Pack de Criativos - 12 criativos | 8 | 23.0h | 6 |
| `272279` | Implementação de Pack de Criativos - 24 criativos | 8 | 39.5h | 8 |
| `272290` | Implementação de Pack de Criativos - 8 criativos | 8 | 16.0h | 6 |
| `271946` | Implementação de Setup Inicial de Google Ads | 11 | 15.0h | 11 |
| `272112` | Implementação de Setup Inicial de Social Ads | 11 | 15.5h | 11 |
| `253684` | Implementação de Site - Advanced | 4 | 6.5h | 0 |
| `222237` | Implementação de Site - Basic | 34 | 55.2h | 34 |
| `253643` | Implementação de Site - Pro | 32 | 75.0h | 29 |
| `274629` | Implementação de Traqueamento Completo | 19 | 23.0h | 12 |
| `177248` | Playbook Aquisição - Estratégia B [SEO] | 11 | 20.8h | 14 |
| `185410` | V4 FOOD 2.0 - E. Aquisição [Mkt Dir. Google Ads] | 7 | 12.0h | 14 |
| `135271` | Criativos para Anúncios | Auditoria de Criativos | 6 | 22.0h | 1 |

## Catálogo ativo completo (127)

| id | modelo | Tar. | Esf. | dias |
|---|---|---|---|---|
| `250016` | Implementação de CRM Marketing - Pro | 20 | 30.0h | 23 |
| `247462` | Análise Consultiva do Time de Vendas | 24 | 48.5h | 24 |
| `167691` | Assessoria Growth | Alavancagem Comercial | 40 | 111.8h | 45 |
| `168912` | Assessoria Growth | Estruturação Estratégica 2.0 | 36 | 101.2h | 30 |
| `271720` | Auditoria Fechamento de Vendas - Até 12 Vendedores | 14 | 18.5h | 11 |
| `271709` | Auditoria Fechamento de Vendas - Até 6 Vendedores | 14 | 14.0h | 11 |
| `274773` | Auditoria Técnica de Ambientes — Marketplace | 12 | 14.5h | 10 |
| `271782` | Auditoria Técnica de Pós-Venda/CS | 22 | 27.0h | 15 |
| `271432` | Auditoria Técnica de Redes Sociais - Até 2 Redes | 13 | 15.0h | 11 |
| `271457` | Auditoria Técnica de Redes Sociais - Até 5 Redes | 13 | 20.5h | 11 |
| `274557` | Auditoria Técnica de Traqueamento Completo | 20 | 15.0h | 11 |
| `271528` | Auditoria de Ambiente Inside Sales - Até 3 Páginas | 15 | 23.0h | 14 |
| `271529` | Auditoria de Ambiente Inside Sales - Até 5 Páginas | 15 | 28.5h | 14 |
| `271636` | Auditoria de Ambientes E-Commerce | 17 | 23.5h | 12 |
| `271466` | Auditoria de Ambientes Inside Sales - Até 1 Página | 15 | 18.0h | 14 |
| `271304` | Auditoria de Criativos Ads & Mensagens | 11 | 14.0h | 11 |
| `271233` | Auditoria de Mídia Paga - Google Ads - Até R$10k | 13 | 9.0h | 11 |
| `271239` | Auditoria de Mídia Paga - Google Ads - R$10k a 25k | 13 | 14.5h | 11 |
| `271271` | Auditoria de Mídia Paga - Google Ads -Acima R$50k | 13 | 22.5h | 12 |
| `271242` | Auditoria de Mídia Paga - Google Ads -R$25k a 50k | 13 | 19.0h | 11 |
| `271232` | Auditoria de Mídia Paga - Meta Ads - Acima R$50k | 11 | 20.5h | 11 |
| `271201` | Auditoria de Mídia Paga - Meta Ads - Até R$10k | 11 | 7.5h | 11 |
| `271209` | Auditoria de Mídia Paga - Meta Ads - De R$10 a 25k | 11 | 13.0h | 11 |
| `271231` | Auditoria de Mídia Paga - Meta Ads - De R$25 a 50k | 11 | 16.5h | 11 |
| `271700` | Auditoria de Pré-Vendas - Até 12 Pré-Vendedores | 14 | 17.5h | 11 |
| `271689` | Auditoria de Pré-Vendas - Até 6 Pré-Vendedores | 14 | 14.0h | 11 |
| `271732` | Auditoria técnica de CRM Marketing | 15 | 20.5h | 11 |
| `225676` | Checklist Antecipação - Black Friday 2025 | 19 | — | 32 |
| `285880` | Construção de Posicionamento Estratégico | 19 | 26.0h | 16 |
| `249644` | Diagnóstico e Performance Comercial 360 - até 12 | 41 | 82.5h | 35 |
| `249672` | Diagnóstico e Performance Comercial 360 - até 25 | 45 | 106.5h | 35 |
| `249476` | Diagnóstico e Performance Comercial 360 - até 6 | 36 | 66.5h | 35 |
| `247588` | Diagnóstico e Planejamento Meta e Google  10 à 30k | 18 | 36.5h | 18 |
| `287883` | Diagnóstico e Planejamento Meta e Google  30 à 50k | 18 | 43.5h | 18 |
| `287886` | Diagnóstico e Planejamento Meta e Google 50 à 100k | 18 | 58.5h | 18 |
| `248463` | Diagnóstico e Planejamento de CRM Marketing - Pro | 30 | 84.0h | 27 |
| `247608` | Diagnóstico e Planejamento de CRM Marketing -Basic | 20 | 33.0h | 21 |
| `221371` | Diagnóstico e Planejamento de Marketing e Vendas | 38 | 74.2h | 29 |
| `248392` | Diagnóstico e Planejamento de Redes Sociais | 28 | 39.0h | 24 |
| `248863` | Elaboração de Identidade Visual - MIV | 17 | 33.5h | 14 |
| `249156` | Elaboração de Identidade Visual - Rebranding | 27 | 85.5h | 31 |
| `249145` | Elaboração de Identidade Visual -Branding Completo | 24 | 76.5h | 35 |
| `249086` | Elaboração de Identidade Visual – Brand Refresh | 24 | 53.5h | 21 |
| `320126` | Estruturação Estratégica 3.0 - E-commerce | 27 | 27.0h | 30 |
| `320045` | Estruturação Estratégica 3.0 - Inside Sales | 30 | 30.0h | 30 |
| `320134` | Estruturação Estratégica 3.0 - PDV | 27 | 27.0h | 30 |
| `272168` | Estruturação Produtos Marketplace - até 100 SKUs | 20 | 43.0h | 18 |
| `272147` | Estruturação de Produtos Marketplace - até 50 SKUs | 20 | 28.5h | 15 |
| `184026` | Implementação - Assessoria Modular [Padrão Rede] | 22 | 22.6h | 45 |
| `254856` | Implementação CRM - GHL Advanced | 18 | 41.0h | 17 |
| `254838` | Implementação CRM - GHL Basic | 13 | 15.5h | 11 |
| `254851` | Implementação CRM - GHL Pro | 17 | 29.5h | 17 |
| `248808` | Implementação CRM - Kommo Basic | 11 | 16.5h | 18 |
| `248818` | Implementação CRM - Kommo Pro | 20 | 40.5h | 26 |
| `254881` | Implementação Google Local Service Ads | 16 | 16.0h | 11 |
| `272117` | Implementação Google Meu Negócio | 12 | 9.5h | 6 |
| `254868` | Implementação Google My Business Profile | 13 | 10.0h | 7 |
| `272246` | Implementação SEO | 18 | 32.5h | 16 |
| `272331` | Implementação da Plataforma Marketplace | 23 | 28.5h | 16 |
| `251165` | Implementação de CRM Marketing - Advanced | 22 | 52.0h | 28 |
| `249950` | Implementação de CRM Marketing - Basic | 17 | 19.0h | 17 |
| `251919` | Implementação de CRM Vendas - Advanced | 17 | 53.0h | 23 |
| `251695` | Implementação de CRM Vendas - Basic | 14 | 17.0h | 17 |
| `251900` | Implementação de CRM Vendas - Pro | 16 | 33.0h | 17 |
| `283757` | Implementação de Cap. e Edição de Fotos - Advanced | 17 | 55.0h | 12 |
| `283789` | Implementação de Cap. e Edição de Fotos - Basic | 16 | 26.0h | 11 |
| `287555` | Implementação de Cap. e Edição de Vídeo - Advanced | 21 | 62.0h | 13 |
| `287204` | Implementação de Cap. e Edição de Vídeo - Basic | 19 | 30.0h | 12 |
| `287302` | Implementação de Cap. e Edição de Vídeo - Pro | 19 | 45.5h | 13 |
| `285869` | Implementação de Captação e Edição de Fotos - Pro | 16 | 38.0h | 12 |
| `251655` | Implementação de Chatbot - Advanced | 16 | 35.5h | 23 |
| `251606` | Implementação de Chatbot - Basic | 13 | 19.5h | 17 |
| `251636` | Implementação de Chatbot - Pro | 14 | 25.5h | 17 |
| `279045` | Implementação de E-commerce - Advanced | 60 | 118.0h | 35 |
| `222501` | Implementação de E-commerce - Basic | 46 | 73.3h | 30 |
| `277521` | Implementação de E-commerce - Pro | 55 | 95.5h | 26 |
| `248858` | Implementação de Hubspot CRM for Marketing | 23 | 42.0h | 28 |
| `248850` | Implementação de Hubspot CRM for Sales | 23 | 39.5h | 28 |
| `222203` | Implementação de Landing Page | 8 | 17.8h | 14 |
| `272296` | Implementação de Pack de Criativos - 12 criativos | 8 | 23.0h | 6 |
| `272279` | Implementação de Pack de Criativos - 24 criativos | 8 | 39.5h | 8 |
| `272290` | Implementação de Pack de Criativos - 8 criativos | 8 | 16.0h | 6 |
| `272475` | Implementação de Pesquisa de Satisfação | 11 | 12.0h | 5 |
| `285258` | Implementação de Produto para E-commerce - Até 100 | 19 | 43.5h | 16 |
| `285204` | Implementação de Produtos para E-commerce - Até 50 | 19 | 26.0h | 15 |
| `271946` | Implementação de Setup Inicial de Google Ads | 11 | 15.0h | 11 |
| `272112` | Implementação de Setup Inicial de Social Ads | 11 | 15.5h | 11 |
| `253684` | Implementação de Site - Advanced | 4 | 6.5h | 0 |
| `222237` | Implementação de Site - Basic | 34 | 55.2h | 34 |
| `253643` | Implementação de Site - Pro | 32 | 75.0h | 29 |
| `274629` | Implementação de Traqueamento Completo | 19 | 23.0h | 12 |
| `248749` | Implementação e Gestão de Dados - CRM | 18 | 30.5h | 19 |
| `248775` | Implementação e Gestão de Dados - E-Commerce | 20 | 31.5h | 21 |
| `248737` | Implementação e Gestão de Dados - Mídia | 11 | 18.0h | 15 |
| `177072` | Onboarding - Assessoria Modular [Padrão Incub] | 23 | 25.3h | 21 |
| `174327` | Onboarding - Assessoria Modular [Padrão Rede] | 21 | 23.8h | 14 |
| `174300` | Onboarding - Pré-setup [Padrão Rede] | 7 | 4.1h | 2 |
| `192359` | Ongoing - Assessoria Modular [Padrão Rede] | 10 | 5.5h | 30 |
| `175724` | Planejamento de Páscoa [Modelo] | 8 | 10.0h | 3 |
| `177103` | Playbook Aquisição - Estratégia A [Social Boost] | 13 | 25.2h | 15 |
| `177248` | Playbook Aquisição - Estratégia B [SEO] | 11 | 20.8h | 14 |
| `177249` | Playbook Aquisição - Estratégia F [Lançamento] | 24 | 93.0h | 31 |
| `177251` | Playbook Aquisição - Estratégia H [Mkt Dir. - IS] | 18 | 56.2h | 15 |
| `185475` | Playbook Aquisição - Estratégia H [Mkt Dir. - PDV] | 14 | 49.9h | 14 |
| `181617` | Playbook Aquisição - Estratégia Q [Inb. Mkt/Isca] | 14 | 51.8h | 15 |
| `272464` | Régua de Relacionamento - Abandono Carrinho | 9 | 15.0h | 9 |
| `272364` | Régua de Relacionamento - Anti-No-Show | 9 | 13.0h | 9 |
| `272462` | Régua de Relacionamento - Cadência e Fechamento | 9 | 16.0h | 9 |
| `272466` | Régua de Relacionamento - Conversão de Pagamentos | 9 | 16.5h | 9 |
| `272471` | Régua de Relacionamento - Engajamento | 9 | 13.5h | 9 |
| `272469` | Régua de Relacionamento -Monetização da Base Ativa | 9 | 16.5h | 9 |
| `170403` | Tratativa - Processo de Offboarding | 7 | 9.8h | 5 |
| `170680` | Tratativa - Transição entre Squad | 21 | 27.8h | 22 |
| `185410` | V4 FOOD 2.0 - E. Aquisição [Mkt Dir. Google Ads] | 7 | 12.0h | 14 |
| `185406` | V4 FOOD 2.0 - E. Aquisição [Mkt Dir. Meta Ads] | 8 | 6.8h | 14 |
| `185435` | V4 FOOD 2.0 - E. Aquisição [Mkt Dir. Repediu] | 8 | 8.8h | 14 |
| `192211` | V4 FOOD 2.0 - Onboarding [Plano Growth e Scale] | 22 | 23.8h | 14 |
| `198277` | V4 FOOD 2.0 - Onboarding [Plano Start] | 12 | 10.8h | 9 |
| `192163` | V4 FOOD 2.0 - Ongoing [Padrão Rede] | 10 | 5.5h | 30 |
| `192392` | V4 FOOD 2.0 | Implem. Plataforma (Plano Growth) | 19 | — | 12 |
| `190608` | V4 FOOD 2.0 | Implem. Plataforma (Plano Scale) | 25 | — | 19 |
| `192393` | V4 FOOD 2.0 | Implem. Plataforma (Plano Start) | 15 | — | 6 |
| `290063` | [DR-E] Destrava Receita [Full Cycle] | 66 | 85.5h | 145 |
| `288901` | [DR-O] Destrava Receita [Full Cycle] | 59 | 73.0h | 145 |
| `290042` | [DR-T] Destrava Receita [Full Cycle] | 66 | 85.5h | 145 |
| `269641` | [DR-X] Destrava Receita Raio-X - ADDON | 27 | 44.5h | 24 |
| `270022` | [DR-X] Destrava Receita Raio-X - BASE | 29 | 46.5h | 34 |

## Inativos (20) — `active=0`, não usar

| id | modelo | Tar. | Esf. | dias |
|---|---|---|---|---|
| `96180` | Alphabeto - Cases - 01/24 | 4 | — | 0 |
| `201875` | CSM - Client Journey USA | 0 | — | 0 |
| `95020` | Casa Lucci - Cases - 01/24 | 9 | 66.0h | 14 |
| `135271` | Criativos para Anúncios | Auditoria de Criativos | 6 | 22.0h | 1 |
| `89610` | Estruturação Comercial | 48 | 48.0h | 79 |
| `90546` | Fluxo Onboarding | 17 | 80.0h | 15 |
| `133005` | Gestão de Mídia | Auditoria de Mídia Paga | 9 | 27.0h | 0 |
| `125201` | Gestão de Mídia | Implementação Google Ads | 23 | 126.0h | 0 |
| `97469` | ISAAS | 36 | 36.0h | 14 |
| `96239` | Natus Representações - Cases - 12/23 | 8 | 47.7h | -7 |
| `105141` | Onboarding de Novo Cliente | 17 | 81.0h | -51 |
| `105155` | Onboarding de Novo Cliente | 17 | 80.0h | 16 |
| `48279` | Onboarding novo cliente | 1 | 12.0h | 7 |
| `89609` | Pele Estética - Cases - 12/23 | 7 | 48.3h | 14 |
| `99454` | Playbook advanced match - cases - 29/02 | 3 | — | 0 |
| `89437` | VIP Print - Cases - 12/23 | 2 | 4.2h | 7 |
| `145697` | [INCUBADORA] Elaboração do Planejamento | 16 | 28.5h | 15 |
| `147052` | [INCUBADORA] Offboarding projeto | Churn | 7 | 12.0h | 3 |
| `145680` | [INCUBADORA] Onboarding |Novo Cliente | 8 | 13.0h | 7 |
| `96181` | [Modelo] - Playbook ecommerce iniciante | 17 | 61.3h | -340 |

## Arquivados (52) — `active=2`, não usar

| id | modelo | Tar. | Esf. | dias |
|---|---|---|---|---|
| `137135` | Assessoria Growth | Estruturação Estratégica 2.0 | 32 | 146.7h | 30 |
| `79024` | BF - Antecipação + Black Friday - Inside Sales | 31 | 91.7h | 38 |
| `79023` | BF - Antecipação + Black Friday - PDV | 30 | 88.7h | 38 |
| `78645` | BF - Antecipação + Black Friday - e-commerce | 41 | 120.7h | 38 |
| `79033` | BF - Black Friday + Cyber Monday - Inside Sales | 20 | 49.0h | 38 |
| `79032` | BF - Black Friday + Cyber Monday - PDV | 19 | 47.0h | 38 |
| `79035` | BF - Black Friday + Cyber Monday - e-commerce | 30 | 76.0h | 40 |
| `79028` | BF - Black Friday - Inside Sales | 18 | 55.7h | 38 |
| `79027` | BF - Black Friday - PDV | 16 | 41.0h | 38 |
| `79031` | BF - Black Friday - e-commerce | 27 | 73.0h | 38 |
| `79227` | BF - Black November - Inside Sales | 20 | 61.7h | 38 |
| `79226` | BF - Black November - PDV | 18 | 47.0h | 38 |
| `79347` | BF - Black November - e-commerce | 29 | 79.0h | 38 |
| `79350` | BF - Black Week - Inside Sales | 19 | 58.7h | 38 |
| `79348` | BF - Black Week - PDV | 17 | 44.0h | 38 |
| `79351` | BF - Black Week - e-commerce | 28 | 76.0h | 38 |
| `36663` | E-commerce (Scale Up) | 26 | 110.0h | 33 |
| `36662` | E-commerce (Setup) | 24 | 105.0h | 32 |
| `36664` | E-commerce (Solidity) | 31 | 132.0h | 33 |
| `88866` | Estruturação Comercial | 48 | 48.0h | 79 |
| `36646` | Food Service (Scale Up) | 23 | 53.0h | 27 |
| `36645` | Food Service (Setup) | 18 | 53.0h | 18 |
| `36647` | Food Service (Solidity) | 28 | 80.0h | 18 |
| `50004` | INSIDE SALES - PADRÃO | 18 | 51.0h | 18 |
| `36657` | Infoproduto/Educação (Scale Up) | 26 | 80.0h | 16 |
| `36656` | Infoproduto/Educação (Setup) | 20 | 79.0h | 12 |
| `36658` | Infoproduto/Educação (Solidity) | 33 | 105.0h | 18 |
| `36126` | Inside Sales (Scale Up) | 24 | 97.0h | 32 |
| `35744` | Inside Sales (Setup) | 17 | 55.0h | 18 |
| `36213` | Inside Sales (Solidity) | 29 | 133.0h | 18 |
| `47528` | Lançamento Perpétuo | 24 | 117.0h | 17 |
| `89429` | Natus Representações - Cases - 12/23 | 8 | 43.7h | 20 |
| `36640` | PDV (Scale Up) | 25 | 100.0h | 16 |
| `36636` | PDV (Setup) | 18 | 61.0h | 16 |
| `36641` | PDV (Solidity) | 30 | 136.0h | 16 |
| `89566` | Pele Estética - Cases - 12/23 | 7 | 48.3h | 14 |
| `44296` | Playbook 3 meses [Resende Hauffe & Co.] | 41 | 151.1h | 111 |
| `84037` | Playbook E-commerce [Avançado] | 28 | 42.5h | 154 |
| `59896` | Playbook PDV - [Iniciante] | 42 | 129.7h | 175 |
| `60039` | Playbook PDV - [Intermediário] | 50 | 163.7h | 198 |
| `71103` | Playbook Social Media | 4 | 31.5h | 41 |
| `130169` | Playbook de Implementação Social Ads | 15 | 41.0h | 15 |
| `62097` | Playbook inside sales - B2B | 29 | 64.8h | 133 |
| `59611` | Playbook inside sales - B2C | 28 | 38.8h | 168 |
| `60713` | TESTE | 0 | — | 0 |
| `150771` | V4 FOOD | Playbook de Entregáveis | 45 | 128.0h | 46 |
| `288916` | [DR-E] Destrava Receita Estratégico - CICLO 1 | 40 | 48.5h | 73 |
| `288918` | [DR-E] Destrava Receita Estratégico - CICLO 2 | 19 | 24.5h | 133 |
| `287450` | [DR-O] Destrava Receita Operacional - CICLO 1 | 40 | 48.5h | 73 |
| `288886` | [DR-O] Destrava Receita Operacional - CICLO 2 | 19 | 24.5h | 133 |
| `288905` | [DR-T] Destrava Receita Tático - CICLO 1 | 40 | 48.5h | 73 |
| `288907` | [DR-T] Destrava Receita Tático - CICLO 2 | 19 | 24.5h | 133 |
