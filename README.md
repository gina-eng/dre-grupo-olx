# DR-E — Grupo OLX

Repositório central do projeto **DR-E (Destrava Receita Estratégico)** da V4 Company para o **Grupo OLX**.
Contrato de 12 meses, R$ 752.000, 12 comitês, 9 diagnósticos técnicos contratados.

> 🔒 Repositório **privado**. As comunicações da OLX carregam aviso de confidencialidade que proíbe
> compartilhamento com terceiros sem autorização escrita. Nenhuma credencial vive aqui.

## Por onde começar

| Se você quer… | Vá para |
|---|---|
| Entender o método | [00-playbook/](00-playbook/) — comece pelo [README do playbook](00-playbook/README.md) |
| Saber o que foi contratado | [04-execucao/contrato-e-escopo.md](04-execucao/contrato-e-escopo.md) e [02-diagnostico/auditorias-contratadas.md](02-diagnostico/auditorias-contratadas.md) |
| Saber quem é quem | [01-cliente/stakeholders.md](01-cliente/stakeholders.md) |
| Saber o que está travado | [PENDENCIAS.md](PENDENCIAS.md) |
| Executar o método com o Claude | `/dre-continuar` — índice em [.claude/skills/README.md](.claude/skills/README.md) |

## Estrutura

| Pasta | O que guarda |
|---|---|
| [00-playbook/](00-playbook/) | Metodologia DR-OTE/DR-E: fundamentos, 8 travas, ciclo de 90 dias, toolkit LTP, POPs, economics |
| [01-cliente/](01-cliente/) | Perfil do Grupo OLX, stakeholders, acessos e ferramentas, histórico de onboarding |
| [02-diagnostico/](02-diagnostico/) | Checklist de dados e acessos, auditorias contratadas, dossiês de trava |
| [03-estrategia/](03-estrategia/) | CRT, nuvem de conflito, FRT/PRT, plano de 90 dias, forecast, matriz de expansão |
| [04-execucao/](04-execucao/) | Contrato e escopo, cronograma e marcos |
| [05-resultados/](05-resultados/) | Revisões de ciclo, previsto vs. realizado, ROI |
| [06-reunioes/](06-reunioes/) | Pautas e atas de kick-off, comitês e assessoria assíncrona |
| [dados/](dados/) | Estado de máquina consumido pelas skills: `client.json`, `outputs/`, `cache/` |
| [.claude/](.claude/) | Skills, scripts e templates que operam o método |
| [PENDENCIAS.md](PENDENCIAS.md) | Bloqueios abertos, com severidade, responsável e prazo |

## Playbook — índice rápido

| Doc | Assunto |
|---|---|
| [01](00-playbook/01-fundamentos-dr-ote.md) | Fundamentos DR-OTE, TOC, throughput, níveis do produto |
| [02](00-playbook/02-travas-de-receita.md) | As 8 travas, score 0–25, consolidação causal |
| [03](00-playbook/03-ciclo-90-dias-e-comites.md) | 5 fases, 3 comitês, gate da Matriz, cronogramas |
| [04](00-playbook/04-toolkit-ltp.md) | UDEs, CRT, nuvem, injeção, FRT, PRT, árvore de transição |
| [05](00-playbook/05-pops-ciclo-1.md) · [06](00-playbook/06-pops-ciclo-2.md) | POPs dos ciclos 1 e 2 |
| [07](00-playbook/07-playbook-operacional-dr-e.md) | Semana a semana do DR-E |
| [08](00-playbook/08-economics-e-entregaveis-dr-e.md) | Entregáveis, precificação, alocação de horas, P&L |
| [09](00-playbook/09-ucm-spiced-dr-e.md) | UCM e SPICED aplicados ao DR-E |

## Convenções

- Documentos em **Markdown**, `kebab-case`, com data quando fizer sentido: `2026-08-24-kickoff.md`.
- Arquivos originais (PDF, XLSX, PPTX) em `assets/originais/`; o conteúdo relevante é transcrito em Markdown na pasta temática.
- Todo número carrega fonte. Estimativa é marcada com `[E]`.
- Travas são citadas **pelo nome**, nunca pelo número — as fontes da V4 usam três numerações conflitantes.
- Regras completas de trabalho no repo: [CLAUDE.md](CLAUDE.md).

## Status

🟢 Documentação organizada e skills instaladas. Kick-off em **24/08/2026**.
Ciclo 1 — fase de Onboarding. Pendências ativas em [PENDENCIAS.md](PENDENCIAS.md).
