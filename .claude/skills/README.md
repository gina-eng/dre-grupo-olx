# Skills do repositório DR-E — Grupo OLX

Duas famílias, um mesmo estado.

| Prefixo | Origem | O que é |
|---|---|---|
| `dre-*` | Escritas para este projeto | O método DR-OTE/DR-E: fluxo de receita, travas, LTP, ciclo de 90 dias, comitês |
| `ee-*` | Copiadas de `v4-estruturacao-estrategica-3.0` (plugin `v4-estruturacao-ia`) | Diagnósticos e artefatos reaproveitáveis, adaptados aos caminhos deste repo |

## Skills específicas do DR-E

| Skill | Fase | O que entrega |
|---|---|---|
| [`dre-continuar`](dre-continuar/SKILL.md) | transversal | Lê o estado e diz qual é o próximo passo. Ponto de entrada padrão. |
| [`dre-onboarding`](dre-onboarding/SKILL.md) | 0 — Onboarding | `dados/client.json` + dossiês de `01-cliente/` + ata de kick-off |
| [`dre-fluxo-receita`](dre-fluxo-receita/SKILL.md) | 1 — Identificar | Funil ponta a ponta com volume, taxa e perda absoluta por etapa |
| [`dre-diagnostico-trava`](dre-diagnostico-trava/SKILL.md) | 1 — Identificar | Score 0–25 de **uma** trava, camadas analítica + experiencial |
| [`dre-consolidacao-causal`](dre-consolidacao-causal/SKILL.md) | 1 — Identificar | Restrição governante + política implícita |
| [`dre-impulso-controlado`](dre-impulso-controlado/SKILL.md) | 1 — Identificar | Confirmação empírica da restrição (+20–30% em um input) |
| [`dre-udes-crt`](dre-udes-crt/SKILL.md) | 2 — Otimizar | UDEs e Árvore da Realidade Atual — **validação final da trava** |
| [`dre-nuvem-conflito`](dre-nuvem-conflito/SKILL.md) | 2 — Otimizar | Evaporating Cloud, quebra de premissa e Injeção |
| [`dre-frt-prt`](dre-frt-prt/SKILL.md) | 2 — Otimizar | FRT, PRT e Árvore de Transição |
| [`dre-plano-90-dias`](dre-plano-90-dias/SKILL.md) | 3 — Alinhar | Plano do ciclo com DRI, indicador e critério de sucesso |
| [`dre-forecast`](dre-forecast/SKILL.md) | 3 — Alinhar | Forecast 12 meses no RevenueFlow (Meta / Atual / Com Injeção) |
| [`dre-matriz-gp`](dre-matriz-gp/SKILL.md) | 3 — Alinhar | **Quality gate obrigatório** antes de cada comitê |
| [`dre-comite`](dre-comite/SKILL.md) | 3/4/5 | Preparação, roteiro e ata dos Comitês 1, 2 e 3 |
| [`dre-matriz-expansao`](dre-matriz-expansao/SKILL.md) | 4 — Expandir | Hipóteses de expansão por impacto × esforço × risco |
| [`dre-tira-duvidas`](dre-tira-duvidas/SKILL.md) | transversal | Assessoria assíncrona dentro do SLA de 12h úteis |
| [`dre-v4mos`](dre-v4mos/SKILL.md) | 1 — Identificar | Puxa dados reais de mídia paga (Meta e Google) do data hub da V4 |
| [`dre-revisao-ciclo`](dre-revisao-ciclo/SKILL.md) | 5 — Recomeçar | Manter/Ajustar/Abandonar, previsto vs. realizado, nova restrição |

### Sequência típica do Ciclo 1

```
dre-onboarding → dre-fluxo-receita → dre-diagnostico-trava (×8)
   → dre-consolidacao-causal → dre-impulso-controlado
   → dre-udes-crt → dre-nuvem-conflito → dre-frt-prt
   → dre-plano-90-dias → dre-forecast
   → dre-matriz-gp → dre-comite
   → dre-matriz-expansao → dre-matriz-gp → dre-comite (2)
   → dre-revisao-ciclo → dre-matriz-gp → dre-comite (3)
```

`dre-tira-duvidas` roda em paralelo, semanas 4–11.

## Skills reaproveitadas da Estruturação Estratégica 3.0

Servem como **instrumento** dos diagnósticos contratados e das camadas de evidência das travas.

| Skill | Alimenta | Diagnóstico contratado |
|---|---|---|
| `ee-s1-persona-icp` | Trava de Qualificação | — |
| `ee-s1-swot` | Contexto estratégico, Comitê 2 | — |
| `ee-s1-diagnostico-maturidade` | Maturidade Digital (obrigatória no ciclo) | — |
| `ee-s2-pesquisa-mercado` | Sizing e concorrentes (semanas 2–3) | — |
| `ee-s2-posicionamento` | PUV/CVB (semanas 6–7) | — |
| `ee-s2-diagnostico-midia` | Travas de Exposição, Atenção, Qualificação | **(vi)** Mídia Paga |
| `ee-s2-diagnostico-criativos` | Trava de Atenção | **(iv)** Criativos Ads & Mensagens |
| `ee-s2-diagnostico-cro` | Travas de Interesse e Compromisso | **(ii)** CRO/SEO · **(viii)** LPs |
| `ee-s2-diagnostico-organico-ig` | Travas de Exposição e Atenção | **(v)** Redes Sociais |
| `ee-s4-diagnostico-comercial` | Travas de Qualificação, Compromisso, Decisão | **(ix)** Pré-Vendas |
| `ee-s4-cliente-oculto` | Camada **experiencial** de qualquer trava | — |
| `ee-s4-forecast-v4` | Modelo em planilha, complementar ao RevenueFlow | — |

Sem cobertura por skill (execução manual, ver `02-diagnostico/auditorias-contratadas.md`): **(i)** CRM Marketing / Salesforce Marketing Cloud, **(iii)** GEO — IA e Buscas Generativas, **(vii)** Rastreamento GA4/GTM.

### O que mudou em relação ao repo de origem

As skills `ee-*` foram copiadas e tiveram apenas os **caminhos** reescritos:

| Origem | Aqui |
|---|---|
| `clientes/{slug}/client.json` | `dados/client.json` |
| `clientes/{slug}/outputs/` | `dados/outputs/` |
| `clientes/{slug}/cache/` | `dados/cache/` |
| `plugins/v4-estruturacao-ia/scripts/` | `.claude/scripts/` |
| `plugins/v4-estruturacao-ia/shared-templates/` | `.claude/shared-templates/` |
| `render_portal.sh` (portal de entregas) | registro no dossiê de `02-diagnostico/` |
| `delivery-map.json` (ciclo de 4 semanas) | `00-playbook/07-playbook-operacional-dr-e.md` (ciclo de 90 dias) |

O conteúdo metodológico das `ee-*` **não** foi alterado. Se o repo de origem evoluir, a atualização é uma nova cópia + o mesmo remapeamento.

## Scripts auxiliares

Em [`.claude/scripts/`](../scripts/): `v4mos_fetch.sh`, `meta_ads_fetch.{sh,py}`, `page_audit.{sh,py}`, `page_audit_deep.{sh,py}`, `ig_organic_audit.{sh,py}`, `build_forecast_v4_completo.py`, `validate_output.py`.

Dependências Python em `requirements.txt`, `requirements-deep.txt`, `requirements-meta.txt`.

As credenciais do V4MOS ficam em `.credentials/clients.json`, na raiz do repositório, chaveadas pelo
`workspace_id`. Ver [`dre-v4mos`](dre-v4mos/SKILL.md).

> Os scripts que tocam plataformas do cliente precisam de credenciais. **Nenhuma credencial vai para o repositório** — o `.gitignore` bloqueia `.env*`, `.credentials/`, `*credentials*.json`, `service-account*.json`, `*.pem` e `*.key`.
