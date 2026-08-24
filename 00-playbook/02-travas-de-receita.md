# As Travas de Receita

## 1. O mapa do sistema

Todo negócio é mapeado como um **Sistema de Produção de Receita** com quatro macro-etapas:

```
Aquisição → Engajamento → Monetização → Retenção
```

Dentro dessas etapas existem **8 pontos** onde o sistema pode estar restringido.
O sistema sempre possui **uma trava governante por vez**.

## 2. Numeração das travas (ATENÇÃO)

Os documentos-fonte da V4 usam **três numerações diferentes** para as mesmas 8 travas.
Enquanto a Matriz não normaliza, este repositório adota o **nome da trava** como identificador
canônico e registra os aliases.

| Trava (nome canônico) | Fundamentos DR-OTE | "As Travas de Receita" / POPs | Fluxo de Estratégia |
|---|---|---|---|
| Cegueira | T0 | Trava 0 | — |
| Exposição | T1 | Trava 7 | Trava 2 |
| Atenção | T2 | Trava 6 | Trava 3 |
| Interesse | T3 | Trava 5 | Trava 4 |
| Qualificação | T4 | Trava 4 | Trava 5 |
| Compromisso | T5 | Trava 3 | Trava 6 |
| Decisão | T6 | Trava 2 | Trava 7 |
| Retenção | T7 | Trava 1 | Trava 8 |

> **Regra deste projeto:** em toda ata, material de comitê e documento entregue ao Grupo OLX,
> a trava é referida **pelo nome** ("Trava de Qualificação"), nunca só pelo número.
> Ver [PENDENCIAS.md](../PENDENCIAS.md).
>
> ⚠️ O contrato do Grupo OLX (cláusula 1.2) fala em **"7 travas"**, enquanto o método opera com 8.
> A diferença é a Trava 0 (Cegueira), que é pré-condição e não restrição de receita em si.

## 3. As 8 travas

### Cegueira — falta de visibilidade
A empresa não possui dados, indicadores ou visibilidade suficiente para diagnosticar o sistema.
Não distingue lead de cliente, não enxerga CAC, LTV, payback ou ROIC.
**Não é uma restrição de receita — é uma pré-condição.** Sem dados mínimos, qualquer diagnóstico é achismo.
A resolução (estruturação de métricas básicas) é obrigatória antes de qualquer intervenção.

### Exposição — o mercado não vê a empresa
Capacidade do sistema de estar presente nos canais onde o ICP está, com frequência adequada,
competindo por *share of voice*.

- **Sintomas quantitativos:** baixo volume de tráfego e leads; baixo alcance mensal; frequência de anúncios baixa; share of voice inferior ao concorrente direto.
- **Sintomas comportamentais:** publicações irregulares; dependência de indicação; ausência em canais estratégicos; comunicação reativa.
- **Dimensões de score:** (A) Alcance mensal · (B) Frequência e consistência · (C) Share of voice vs. concorrentes · (D) Diversidade de canais · (E) Regularidade estratégica.
- **Entrada visual obrigatória:** Mapa de Exposição Competitiva (cliente vs. 2+ concorrentes por canal).

### Atenção — quem vê não se importa
Capacidade de interromper o padrão automático do público. Atenção **não é** impressão, alcance
ou visualização automática — é interrupção de padrão, foco voluntário, primeiros segundos sustentados.

- **Sintomas:** CTR abaixo da média do canal; CPM alto com baixo engajamento; baixo tempo médio de visualização; alto CPL sem aumento de volume; criativos genéricos; headline vaga; comunicação igual à concorrência.
- **Dimensões de score:** (A) CTR/resposta inicial · (B) Diferenciação · (C) Clareza da promessa · (D) Força de interrupção · (E) Competitividade.
- **Entrada visual obrigatória:** Painel Comparativo de Atenção (headline, promessa, visual, gatilho principal — cliente vs. concorrentes).

### Interesse — chega, mas não aprofunda
Nível de envolvimento cognitivo e emocional que mantém o cliente na jornada.

- **Sintomas:** alta rejeição; baixo tempo de permanência; baixa taxa de scroll; baixo consumo de conteúdo; leads que não respondem após o primeiro material; oferta antes da construção de valor.
- **Dimensões de score:** (A) Tempo de permanência · (B) Estrutura narrativa · (C) Educação e diagnóstico · (D) Provas e diferenciação · (E) Sustentação do engajamento.
- **Entrada visual obrigatória:** Mapa de Profundidade de Interesse por etapa da jornada.

### Qualificação — quem age não tem perfil
Processo pelo qual o sistema define o ICP, atrai perfis coerentes e prioriza oportunidades com
maior probabilidade de gerar throughput sustentável. **Não é "perguntar orçamento"** — é coerência
estratégica entre oferta e público.

- **Sintomas:** alta geração de leads com baixa conversão; volume de leads "sem orçamento"; ticket médio abaixo do planejado; ICP não documentado; comercial reclama da qualidade dos leads.
- **Dimensões de score:** (A) ICP documentado e claro · (B) Alinhamento ICP vs. leads · (C) Alinhamento ICP vs. clientes · (D) Processo de qualificação · (E) Capacidade de desqualificar.
- **Entrada visual obrigatória:** Matriz ICP vs. Realidade (ticket, segmento, porte, dor principal, capacidade de pagamento).

### Compromisso — o lead some antes de decidir
Ação do cliente que prova intenção real e reduz incerteza: agendar, comparecer, enviar dados,
dar sinal, fazer check-in. **Compromisso é um passo que custa algo** — tempo, esforço, fricção.

- **Sintomas:** alta taxa de no-show; alta taxa de "não responde"; baixa taxa de agendamento após qualificação; queda entre lead qualificado → reunião realizada; muito follow para pouco avanço.
- **Dimensões de score:** (A) Tempo até 1º contato · (B) Conversão para agendamento · (C) Taxa de comparecimento · (D) Cadência e qualidade de follow-up · (E) Arquitetura do compromisso. *Nota acima de 3 exige evidência formal.*
- **Entrada visual obrigatória:** Linha do Tempo do Compromisso (mín. 1 caso por modelo de venda; ideal 3).

### Decisão — chega ao fim, mas não fecha
Momento em que o cliente assume compromisso financeiro. Decisão não é interesse; decisão é conversão.

- **Sintomas:** baixa taxa de fechamento; alto volume de propostas abertas; ciclo de vendas longo; muitos "vou pensar"; proposta genérica; ausência de deadline; follow-up irregular.
- **Dimensões de score:** (A) Taxa de conversão · (B) Tempo médio de decisão · (C) Estrutura da proposta · (D) Follow-up estruturado · (E) Arquitetura de urgência.
- **Entrada visual obrigatória:** Matriz de Decisão (clareza da proposta, prazo, follow-up, resolução de objeções, CTA).

### Retenção — vende, mas não se repete
Capacidade de manter clientes economicamente ativos e gerar receita recorrente ou repetida.
Venda isolada não caracteriza retenção.

- **Pergunta estruturante:** *"Se a empresa parar de adquirir novos clientes por 90 dias, o faturamento se sustenta?"*
- **Sintomas:** receita recorrente irrelevante; alto percentual de clientes one-shot; churn elevado ou não medido; LTV próximo ou inferior ao CAC; pós-venda informal.
- **Dimensões de score:** (A) Dados estruturados de retenção · (B) Receita recorrente relevante · (C) Jornada formal de pós-venda · (D) Política clara de continuidade · (E) Estratégia ativa de expansão. *Nota acima de 3 exige evidência formal.*
- **Entrada visual obrigatória:** Scorecard de Retenção por produto (receita recorrente %, recompra %, permanência média, LTV) + cohort.

## 4. Método de diagnóstico (comum a todas as travas)

Cada trava é diagnosticada em **duas camadas**:

1. **Camada analítica** — dados solicitados ao cliente, comparados com benchmarks setoriais e histórico da própria conta.
2. **Camada experiencial** — validação prática por modelo de venda:
   - **Inside Sales:** cliente oculto (primeiro contato, qualificação, proposta, follow-up, pós-venda).
   - **Vendas Online:** jornada real até checkout, mapeando fricções.
   - **PDV:** visita presencial, observação de abordagem e comunicação visual.

### Score da trava (0–25)

Cada trava tem 5 dimensões pontuadas de 0 a 5, com evidência analítica **e** experiencial registrada.

| Total | Interpretação |
|---|---|
| 0–10 | Estruturalmente travada. Alta probabilidade de ser a restrição. |
| 11–15 | Frágil. Vazamento relevante. |
| 16–20 | Funcional, com pontos de melhoria. |
| 21–25 | Forte e governada. |

### Consolidação causal (formato obrigatório)

Toda trava diagnosticada termina numa hipótese formulada como **política organizacional**:

> "A empresa opera sob a política implícita de **________**, o que gera **________**, limitando **________**."

Exemplos: *"Evitar investimento constante em mídia"*, *"Priorizar volume de leads em vez de
qualidade"*, *"Evitar pressão de fechamento"*. **Evitar causas operacionais superficiais**
(ex.: "as pessoas não fazem") — causas-raiz são falhas de estrutura, processo, definição
estratégica ou priorização.

### Determinação preliminar

Uma trava é **potencial governante** quando:
- Explica a maioria dos sintomas observados;
- Resolvê-la aumenta o throughput mais do que atacar qualquer outra;
- Não há hipótese concorrente com maior poder explicativo.

**Validação final sempre na CRT.**

## 5. Ferramentas de diagnóstico por trava

| Trava | Ferramentas principais |
|---|---|
| Exposição | CRM (volume/origem de novos contatos), GA4 (sessões ao longo do tempo), heatmaps (volume mínimo analisável), bibliotecas de anúncios |
| Atenção | GA4 (taxa de engajamento, tempo na página), heatmaps e gravações de sessão, plataformas de mídia (CTR por criativo), CRM (leads que não avançam) |
| Interesse | GA4 (páginas/sessão, eventos de exploração), ferramentas de SEO (keywords investigativas), heatmaps (scroll profundo), CRM (pedidos de mais informação) |
| Qualificação | CRM (campos de qualificação, taxa de avanço por perfil), gravações de calls, formulários de entrada, dashboards de pipeline |
| Compromisso | CRM (comparecimento, motivos de perda "sumiu"/"no-show"), agenda/calendário, gravações de calls, ferramentas de automação |
| Decisão | CRM (tempo proposta→decisão, motivos de perda "adiou"), agenda, gravações de calls, dashboards de forecast |
| Retenção | CRM (permanência, motivos de cancelamento), ferramentas de uso do produto, NPS/CSAT, registros de contato pós-venda |

## 6. Integração travas ↔ fluxo estratégico

| Macroetapa | Travas correspondentes |
|---|---|
| Aquisição | Exposição, Atenção |
| Engajamento | Interesse, Qualificação |
| Monetização | Compromisso, Decisão |
| Retenção | Retenção |

## 7. Maturidade Digital

Avaliação paralela ao diagnóstico de travas, em três dimensões:
**Canais Digitais** · **Processos e Automação** · **Uso de Dados e Inteligência**.

| Nível | Característica |
|---|---|
| 1 — Inicial | Presença digital básica, processos informais, baixo uso de dados |
| 2 — Em estruturação | Canais ativos porém pouco integrados; processos parcialmente definidos; dados usados reativamente |
| 3 — Estruturado | Canais claros e integrados; processos documentados e repetíveis; uso consistente de indicadores |
| 4 — Avançado | Estratégia orientada por dados; automação significativa; alta previsibilidade e capacidade de escala |
