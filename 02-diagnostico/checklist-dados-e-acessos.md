# Checklist de Dados e Acessos — Diagnóstico

Lista enviada por Gustavo Figueiredo ao Grupo OLX em **11/08/2026**, organizada por frente de
trabalho do DR-E.

**Prioridade declarada:** blocos **A, G, H e J** — "destravam as análises de maior impacto;
o restante pode ser complementado nas duas primeiras semanas."

**Legenda de status:** ✅ recebido · 🟡 parcial · 🟠 solicitado, pendente · ⚪ não iniciado · 🔴 inexistente (registrar como evidência diagnóstica)

**Material recebido até agora:** primeiro lote do data room baixado em **24/08/2026**, 9 arquivos nos blocos E e I. Índice, procedência e leitura inicial em [`assets/originais/README.md`](../assets/originais/README.md).

---

## 🔴 A. Visão de negócio e Fluxo de Receita — PRIORITÁRIO
*Base para o diagnóstico das travas e para o Mapeamento do Fluxo de Receita.*

| # | Item | Status | Obs. |
|---|---|---|---|
| A1 | Receita mensal dos últimos **24 meses**, aberta por linha de negócio / segmento / produto | ⚪ | |
| A2 | Funil comercial completo (volumes e taxas de conversão por etapa), últimos **12–24 meses** | ⚪ | |
| A3 | Ticket médio, ciclo de vendas e CAC por canal (se disponível) | ⚪ | |
| A4 | Estrutura organizacional de Marketing, Pré-Vendas e Vendas (organograma e responsabilidades) | ⚪ | |
| A5 | Planejamento estratégico / OKRs vigentes e metas comerciais | ⚪ | |
| A6 | Definição atual de ICP e segmentação de mercado | ⚪ | |

> A1–A3 são os insumos **matemáticos** do Forecast. Sem eles, o funil não valida contra o
> faturamento declarado e o forecast não pode ser construído.

## B. CRM Marketing
*Alimenta o diagnóstico (i) — Salesforce Marketing Cloud.*

| # | Item | Status |
|---|---|---|
| B1 | Acesso de visualização | ⚪ |
| B2 | Arquitetura de Data Extensions e lógica de segmentação atual | ⚪ |
| B3 | Relatórios de performance de e-mail dos últimos 12 meses (entregabilidade, open, CTR, conversão) | ⚪ |
| B4 | Tamanho e saúde da base opt-in | ⚪ |

## C. Ambientes CRO/SEO (domínios B2B)
*Alimenta o diagnóstico (ii).*

| # | Item | Status |
|---|---|---|
| C1 | Relação de domínios e subdomínios B2B em escopo | ⚪ |
| C2 | Acesso ao Google Search Console de cada propriedade | ⚪ |
| C3 | Acesso à ferramenta de SEO utilizada internamente (SEMrush, Ahrefs ou similar), se houver | ⚪ |

## D. GEO (IA e Buscas Generativas)
*Alimenta o diagnóstico (iii). Demais insumos cobertos por C e G.*

| # | Item | Status |
|---|---|---|
| D1 | Lista de queries / temas prioritários de marca e categoria | ⚪ |
| D2 | Inventário de conteúdo institucional e educativo publicado | ⚪ |

## E. Criativos Ads & Mensagens
*Alimenta o diagnóstico (iv).*

| # | Item | Status | Obs. |
|---|---|---|---|
| E1 | Biblioteca de criativos veiculados nos últimos 6–12 meses | 🟡 | 8 peças de **uma** campanha (Mês do Corretor 2026, SP, consideração, RE) recebidas em 24/08 — ver [originais](../assets/originais/README.md#bloco-e--criativos-anúncios-e-mensagens). Falta o resto da janela de 6–12 meses |
| E2 | Brandbook, diretrizes de marca e documento de proposta de valor (messaging house, se existir) | ⚪ | |
| E3 | Briefings das principais campanhas recentes | ⚪ | Sem os briefings não dá para saber qual era a hipótese por trás das variantes V1, V2 e V3 recebidas em E1 |

## F. Redes Sociais e Conteúdo Orgânico
*Alimenta o diagnóstico (v).*

| # | Item | Status |
|---|---|---|
| F1 | Acesso de analista ao Meta Business Suite e à(s) Company Page(s) do LinkedIn | ⚪ |
| F2 | Acessos equivalentes a demais canais ativos (YouTube, TikTok, etc.) | ⚪ |
| F3 | Calendário editorial e relatórios de performance orgânica dos últimos 6 meses | ⚪ |

## 🔴 G. Mídia Paga (Google e Meta) — PRIORITÁRIO
*Alimenta o diagnóstico (vi).*

| # | Item | Status | Obs. |
|---|---|---|---|
| G1 | Acesso de leitura às contas de Google Ads e Meta Ads (IDs das contas) | 🟡 | 3 contas mapeadas — ver [acessos](../01-cliente/acessos-e-ferramentas.md) |
| G2 | Investimento mensal por canal/campanha dos últimos 12 meses | ⚪ | |
| G3 | Plano de mídia vigente e definição das conversões otimizadas em cada plataforma | ⚪ | |
| G4 | Metas de CPA/ROAS praticadas e contato da agência, caso a operação seja terceirizada | ⚪ | |

## 🔴 H. Rastreamento Completo (GA4 e GTM) — PRIORITÁRIO
*Alimenta o diagnóstico (vii).*

| # | Item | Status |
|---|---|---|
| H1 | Acesso de analista à(s) propriedade(s) GA4 | ⚪ |
| H2 | Acesso de leitura ao(s) contêiner(es) GTM publicados | ⚪ |
| H3 | Plano de mensuração e taxonomia de eventos e conversões, se documentado | ⚪ |
| H4 | Configuração de consentimento (LGPD / consent mode) e eventual tagueamento server-side | ⚪ |

## I. Páginas de Captura e Fluxos de Conversão
*Alimenta o diagnóstico (viii).*

| # | Item | Status | Obs. |
|---|---|---|---|
| I1 | URLs das principais LPs e fluxos de conversão ativos | ⚪ | O teste de I3 cita a "LP Anuncie ZAP"; falta a relação completa e as URLs |
| I2 | Taxas de conversão por página / etapa | ⚪ | |
| I3 | Histórico de testes A/B realizados, se houver | 🟡 | 1 teste recebido em 24/08 (LP Anuncie ZAP, 17–23/03) — ver [originais](../assets/originais/README.md#bloco-i--páginas-de-captura-e-fluxos-de-conversão). Vieram só os slides de resultado: **sem volume absoluto de visitantes e de MQL**, não dá para recalcular a significância |
| I4 | Acesso a ferramenta de comportamento (Hotjar, Clarity ou similar), se disponível | ⚪ | |

## 🔴 J. Pré-Vendas, Qualificação e Sales Engagement — PRIORITÁRIO
*Alimenta o diagnóstico (ix). Bloco mais informativo para as travas de fundo de funil.*

| # | Item | Status |
|---|---|---|
| J1 | Acesso de leitura ao CRM comercial | ⚪ |
| J2 | Critérios atuais de qualificação (scoring, SLAs entre Marketing e Vendas) | ⚪ |
| J3 | Playbooks e cadências de prospecção/atendimento (ferramenta de engagement, se houver) | ⚪ |
| J4 | Amostra de gravações de calls de qualificação (**10 a 15 ligações recentes**) | ⚪ |
| J5 | Taxas de conversão e tempos médios por etapa de pré-vendas | ⚪ |

---

## Como usar este checklist

1. **Atualize o status a cada recebimento.** Este arquivo é a fonte de verdade da fase Identificar.
2. **Item inexistente não é falha do cliente — é dado.** Marque 🔴 e registre no diagnóstico da trava correspondente como evidência de maturidade.
3. **Bloco A é pré-requisito do Forecast.** Sem A1–A3, a matemática do sistema não valida.
4. **Cobrar apenas o que ainda falta**, por bloco, no canal oficial do projeto.
