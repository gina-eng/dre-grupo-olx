# Modelos de projeto — mapa da conta

Levantado via MCP em 2026-08-03. **119 modelos confirmados**, 2.323 tarefas somadas,
248.181 min de esforço previsto (~4.136 h).

## Limites deste levantamento — leia antes de usar

- `list_projects` tem **cap de 75 registros por resposta e não tem paginação** (sem `skip`/`take`).
- O filtro `createdBy` (10=meus, 20=eKyte, 30=matriz) **não funciona** — as três origens devolvem
  a mesma lista. `isModel=1` + `createdBy=10` volta vazio mesmo havendo 21 modelos seus.
- Os 119 aqui vieram de varredura por `textSearch`. A busca por "Onboarding" achou 8 modelos,
  dos quais **1** estava nos 75 iniciais — prova de que a lista base é truncada.
- Portanto: **este mapa é piso, não teto.** Todo modelo listado existe; podem existir outros.
  Para contagem fechada, exportar pela UI.

## Fatos estruturais

- **Todos os 119 pertencem à empresa matriz `6953`**, workspace `26815` ("V4 Company").
  A empresa `18239` (Flagship) **não tem nenhum modelo próprio** e nenhum projeto ativo.
- Autoria: **94 Vinicius (Matriz)**, **21 Rafael Corazza**, **4 Leonardo Rosa**.
- Nenhum modelo tem tarefas planejadas (`plannedProjectTasksCount: 0`) — todas as tarefas
  estão como não planejadas, o que é o esperado num modelo.

## Catálogo por família

### Auditoria — 23 modelos, 320 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `271782` | Auditoria Técnica de Pós-Venda/CS | 22 | 15 | 1620 | Vinicius |
| `274557` | Auditoria Técnica de Traqueamento Completo | 20 | 11 | 900 | Vinicius |
| `271636` | Auditoria de Ambientes E-Commerce | 17 | 12 | 1410 | Vinicius |
| `271466` | Auditoria de Ambientes Inside Sales - Até 1 Página | 15 | 14 | 1080 | Vinicius |
| `271528` | Auditoria de Ambiente Inside Sales - Até 3 Páginas | 15 | 14 | 1380 | Vinicius |
| `271529` | Auditoria de Ambiente Inside Sales - Até 5 Páginas | 15 | 14 | 1710 | Vinicius |
| `271732` | Auditoria técnica de CRM Marketing | 15 | 11 | 1230 | Vinicius |
| `271689` | Auditoria de Pré-Vendas - Até 6 Pré-Vendedores | 14 | 11 | 840 | Vinicius |
| `271700` | Auditoria de Pré-Vendas - Até 12 Pré-Vendedores | 14 | 11 | 1050 | Vinicius |
| `271709` | Auditoria Fechamento de Vendas - Até 6 Vendedores | 14 | 11 | 840 | Vinicius |
| `271720` | Auditoria Fechamento de Vendas - Até 12 Vendedores | 14 | 11 | 1110 | Vinicius |
| `271233` | Auditoria de Mídia Paga - Google Ads - Até R$10k | 13 | 11 | 540 | Vinicius |
| `271239` | Auditoria de Mídia Paga - Google Ads - R$10k a 25k | 13 | 11 | 870 | Vinicius |
| `271242` | Auditoria de Mídia Paga - Google Ads -R$25k a 50k | 13 | 11 | 1140 | Vinicius |
| `271271` | Auditoria de Mídia Paga - Google Ads -Acima R$50k | 13 | 12 | 1350 | Vinicius |
| `271432` | Auditoria Técnica de Redes Sociais - Até 2 Redes | 13 | 11 | 900 | Vinicius |
| `271457` | Auditoria Técnica de Redes Sociais - Até 5 Redes | 13 | 11 | 1230 | Vinicius |
| `274773` | Auditoria Técnica de Ambientes — Marketplace | 12 | 10 | 870 | Vinicius |
| `271201` | Auditoria de Mídia Paga - Meta Ads - Até R$10k | 11 | 11 | 450 | Vinicius |
| `271209` | Auditoria de Mídia Paga - Meta Ads - De R$10 a 25k | 11 | 11 | 780 | Vinicius |
| `271231` | Auditoria de Mídia Paga - Meta Ads - De R$25 a 50k | 11 | 11 | 990 | Vinicius |
| `271232` | Auditoria de Mídia Paga - Meta Ads - Acima R$50k | 11 | 11 | 1230 | Vinicius |
| `271304` | Auditoria de Criativos Ads & Mensagens | 11 | 11 | 840 | Vinicius |

### Implementação (outros) — 21 modelos, 328 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `222237` | Implementação de Site - Basic | 34 | 34 | 3310 | Vinicius |
| `253643` | Implementação de Site - Pro | 32 | 29 | 4500 | Vinicius |
| `248850` | Implementação de Hubspot CRM for Sales | 23 | 28 | 2370 | Vinicius |
| `248858` | Implementação de Hubspot CRM for Marketing | 23 | 28 | 2520 | Vinicius |
| `248775` | Implementação e Gestão de Dados - E-Commerce | 20 | 21 | 1890 | Vinicius |
| `274629` | Implementação de Traqueamento Completo | 19 | 12 | 1380 | Vinicius |
| `285204` | Implementação de Produtos para E-commerce - Até 50 | 19 | 15 | 1560 | Vinicius |
| `285258` | Implementação de Produto para E-commerce - Até 100 | 19 | 16 | 2610 | Vinicius |
| `248749` | Implementação e Gestão de Dados - CRM | 18 | 19 | 1830 | Vinicius |
| `254881` | Implementação Google Local Service Ads | 16 | 11 | 960 | Vinicius |
| `254868` | Implementação Google My Business Profile | 13 | 7 | 600 | Vinicius |
| `272117` | Implementação Google Meu Negócio | 12 | 6 | 570 | Vinicius |
| `248737` | Implementação e Gestão de Dados - Mídia | 11 | 15 | 1080 | Vinicius |
| `271946` | Implementação de Setup Inicial de Google Ads | 11 | 11 | 900 | Vinicius |
| `272112` | Implementação de Setup Inicial de Social Ads | 11 | 11 | 930 | Vinicius |
| `272475` | Implementação de Pesquisa de Satisfação | 11 | 5 | 720 | Vinicius |
| `222203` | Implementação de Landing Page | 8 | 14 | 1070 | Vinicius |
| `272279` | Implementação de Pack de Criativos - 24 criativos | 8 | 8 | 2370 | Vinicius |
| `272290` | Implementação de Pack de Criativos - 8 criativos | 8 | 6 | 960 | Vinicius |
| `272296` | Implementação de Pack de Criativos - 12 criativos | 8 | 6 | 1380 | Vinicius |
| `253684` | Implementação de Site - Advanced | 4 | 0 | 390 | Vinicius |

### CRM — Implementação — 11 modelos, 185 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `251165` | Implementação de CRM Marketing - Advanced | 22 | 28 | 3120 | Vinicius |
| `248818` | Implementação CRM - Kommo Pro | 20 | 26 | 2430 | Vinicius |
| `250016` | Implementação de CRM Marketing - Pro | 20 | 23 | 1800 | Vinicius |
| `254856` | Implementação CRM - GHL Advanced | 18 | 17 | 2460 | Vinicius |
| `249950` | Implementação de CRM Marketing - Basic | 17 | 17 | 1140 | Vinicius |
| `251919` | Implementação de CRM Vendas - Advanced | 17 | 23 | 3180 | Vinicius |
| `254851` | Implementação CRM - GHL Pro | 17 | 17 | 1770 | Vinicius |
| `251900` | Implementação de CRM Vendas - Pro | 16 | 17 | 1980 | Vinicius |
| `251695` | Implementação de CRM Vendas - Basic | 14 | 17 | 1021 | Vinicius |
| `254838` | Implementação CRM - GHL Basic | 13 | 11 | 930 | Vinicius |
| `248808` | Implementação CRM - Kommo Basic | 11 | 18 | 990 | Vinicius |

### Diagnóstico e Planejamento — 10 modelos, 292 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `249672` | Diagnóstico e Performance Comercial 360 - até 25 | 45 | 35 | 6390 | Vinicius |
| `249644` | Diagnóstico e Performance Comercial 360 - até 12 | 41 | 35 | 4950 | Vinicius |
| `221371` | Diagnóstico e Planejamento de Marketing e Vendas | 38 | 29 | 4450 | Vinicius |
| `249476` | Diagnóstico e Performance Comercial 360 - até 6 | 36 | 35 | 3990 | Vinicius |
| `248463` | Diagnóstico e Planejamento de CRM Marketing - Pro | 30 | 27 | 5040 | Vinicius |
| `248392` | Diagnóstico e Planejamento de Redes Sociais | 28 | 24 | 2340 | Vinicius |
| `247608` | Diagnóstico e Planejamento de CRM Marketing -Basic | 20 | 21 | 1980 | Vinicius |
| `247588` | Diagnóstico e Planejamento Meta e Google  10 à 30k | 18 | 18 | 2190 | Vinicius |
| `287883` | Diagnóstico e Planejamento Meta e Google  30 à 50k | 18 | 18 | 2610 | Vinicius |
| `287886` | Diagnóstico e Planejamento Meta e Google 50 à 100k | 18 | 18 | 3510 | Vinicius |

### Playbook de Aquisição — 6 modelos, 94 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `177249` | Playbook Aquisição - Estratégia F [Lançamento] | 24 | 31 | 5580 | **Rafael** |
| `177251` | Playbook Aquisição - Estratégia H [Mkt Dir. - IS] | 18 | 15 | 3375 | **Rafael** |
| `181617` | Playbook Aquisição - Estratégia Q [Inb. Mkt/Isca] | 14 | 15 | 3105 | **Rafael** |
| `185475` | Playbook Aquisição - Estratégia H [Mkt Dir. - PDV] | 14 | 14 | 2995 | **Rafael** |
| `177103` | Playbook Aquisição - Estratégia A [Social Boost] | 13 | 15 | 1510 | **Rafael** |
| `177248` | Playbook Aquisição - Estratégia B [SEO] | 11 | 14 | 1245 | **Rafael** |

### V4 FOOD 2.0 — 6 modelos, 67 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `192211` | V4 FOOD 2.0 - Onboarding [Plano Growth e Scale] | 22 | 14 | 1430 | **Rafael** |
| `198277` | V4 FOOD 2.0 - Onboarding [Plano Start] | 12 | 9 | 645 | **Rafael** |
| `192163` | V4 FOOD 2.0 - Ongoing [Padrão Rede] | 10 | 30 | 330 | **Rafael** |
| `185406` | V4 FOOD 2.0 - E. Aquisição [Mkt Dir. Meta Ads] | 8 | 14 | 405 | **Rafael** |
| `185435` | V4 FOOD 2.0 - E. Aquisição [Mkt Dir. Repediu] | 8 | 14 | 530 | **Rafael** |
| `185410` | V4 FOOD 2.0 - E. Aquisição [Mkt Dir. Google Ads] | 7 | 14 | 720 | **Rafael** |

### Outros — 6 modelos, 54 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `272364` | Régua de Relacionamento - Anti-No-Show | 9 | 9 | 780 | Vinicius |
| `272462` | Régua de Relacionamento - Cadência e Fechamento | 9 | 9 | 960 | Vinicius |
| `272464` | Régua de Relacionamento - Abandono Carrinho | 9 | 9 | 900 | Vinicius |
| `272466` | Régua de Relacionamento - Conversão de Pagamentos | 9 | 9 | 990 | Vinicius |
| `272469` | Régua de Relacionamento -Monetização da Base Ativa | 9 | 9 | 990 | Vinicius |
| `272471` | Régua de Relacionamento - Engajamento | 9 | 9 | 810 | Vinicius |

### Audiovisual — 6 modelos, 108 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `287555` | Implementação de Cap. e Edição de Vídeo - Advanced | 21 | 13 | 3720 | Vinicius |
| `287204` | Implementação de Cap. e Edição de Vídeo - Basic | 19 | 12 | 1800 | Vinicius |
| `287302` | Implementação de Cap. e Edição de Vídeo - Pro | 19 | 13 | 2730 | Vinicius |
| `283757` | Implementação de Cap. e Edição de Fotos - Advanced | 17 | 12 | 3300 | Vinicius |
| `283789` | Implementação de Cap. e Edição de Fotos - Basic | 16 | 11 | 1560 | Vinicius |
| `285869` | Implementação de Captação e Edição de Fotos - Pro | 16 | 12 | 2280 | Vinicius |

### Onboarding / Ongoing — 5 modelos, 83 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `177072` | Onboarding - Assessoria Modular [Padrão Incub] | 23 | 21 | 1520 | **Rafael** |
| `184026` | Implementação - Assessoria Modular [Padrão Rede] | 22 | 45 | 1355 | **Rafael** |
| `174327` | Onboarding - Assessoria Modular [Padrão Rede] | 21 | 14 | 1430 | **Rafael** |
| `192359` | Ongoing - Assessoria Modular [Padrão Rede] | 10 | 30 | 330 | **Rafael** |
| `174300` | Onboarding - Pré-setup [Padrão Rede] | 7 | 2 | 245 | **Rafael** |

### Destrava Receita — 5 modelos, 247 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `290042` | [DR-T] Destrava Receita [Full Cycle] | 66 | 145 | 5130 | Leonardo Rosa |
| `290063` | [DR-E] Destrava Receita [Full Cycle] | 66 | 145 | 5130 | Leonardo Rosa |
| `288901` | [DR-O] Destrava Receita [Full Cycle] | 59 | 145 | 4380 | Leonardo Rosa |
| `270022` | [DR-X] Destrava Receita Raio-X - BASE | 29 | 34 | 2790 | Vinicius |
| `269641` | [DR-X] Destrava Receita Raio-X - ADDON | 27 | 24 | 2670 | Leonardo Rosa |

### Identidade Visual — 4 modelos, 92 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `249156` | Elaboração de Identidade Visual - Rebranding | 27 | 31 | 5130 | Vinicius |
| `249086` | Elaboração de Identidade Visual – Brand Refresh | 24 | 21 | 3210 | Vinicius |
| `249145` | Elaboração de Identidade Visual -Branding Completo | 24 | 35 | 4590 | Vinicius |
| `248863` | Elaboração de Identidade Visual - MIV | 17 | 14 | 2010 | Vinicius |

### Assessoria Growth — 3 modelos, 106 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `167691` | Assessoria Growth | Alavancagem Comercial | 40 | 45 | 6705 | **Rafael** |
| `168912` | Assessoria Growth | Estruturação Estratégica 2.0 | 36 | 30 | 6075 | **Rafael** |
| `320045` | Estruturação Estratégica 3.0 - Inside Sales | 30 | 30 | 1800 | **Rafael** |

### E-commerce — 3 modelos, 161 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `279045` | Implementação de E-commerce - Advanced | 60 | 35 | 7080 | Vinicius |
| `277521` | Implementação de E-commerce - Pro | 55 | 26 | 5730 | Vinicius |
| `222501` | Implementação de E-commerce - Basic | 46 | 30 | 4400 | Vinicius |

### Chatbot — 3 modelos, 43 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `251655` | Implementação de Chatbot - Advanced | 16 | 23 | 2130 | Vinicius |
| `251636` | Implementação de Chatbot - Pro | 14 | 17 | 1530 | Vinicius |
| `251606` | Implementação de Chatbot - Basic | 13 | 17 | 1170 | Vinicius |

### Marketplace — 3 modelos, 63 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `272331` | Implementação da Plataforma Marketplace | 23 | 16 | 1710 | Vinicius |
| `272147` | Estruturação de Produtos Marketplace - até 50 SKUs | 20 | 15 | 1710 | Vinicius |
| `272168` | Estruturação Produtos Marketplace - até 100 SKUs | 20 | 18 | 2580 | Vinicius |

### Sazonal / Campanha — 1 modelos, 19 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `225676` | Checklist Antecipação - Black Friday 2025 | 19 | 32 | 0 | **Rafael** |

### Comercial — 1 modelos, 24 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `247462` | Análise Consultiva do Time de Vendas | 24 | 24 | 2910 | Vinicius |

### SEO — 1 modelos, 18 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `272246` | Implementação SEO | 18 | 16 | 1950 | Vinicius |

### Posicionamento — 1 modelos, 19 tarefas

| ID | Modelo | Tarefas | Dias | Esforço (min) | Criado por |
|---|---|---|---|---|---|
| `285880` | Construção de Posicionamento Estratégico | 19 | 16 | 1560 | Vinicius |
