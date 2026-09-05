---
name: dre-onboarding
description: "Onboarding do DR-E: consolida briefing, stakeholders, acessos e dados iniciais em dados/client.json e nos dossies de 01-cliente. Use quando o operador disser /dre-onboarding ou 'iniciar projeto' ou 'kick-off' ou 'montar o client.json'."
dependencies: []
tools: []
fase: "0, Onboarding"
estimated_time: "2h (kick-off) + consolidacao"
output_file: "dados/client.json"
---

# DR-E · Onboarding

Voce vai transformar o material bruto do inicio de projeto (contrato, e-mails, kick-off, planilhas) no **estado inicial versionado** do projeto: `dados/client.json`, mais os dossies humanos em `01-cliente/`.

## Fontes

| Fonte | Onde | O que extrair |
|---|---|---|
| Contrato | `04-execucao/contrato-e-escopo.md` | Escopo, diagnosticos contratados, valores, SLA, marcos, clausulas de dados |
| E-mails de onboarding | `01-cliente/historico-onboarding.md` | Decisoes, focos declarados, prazos combinados |
| Perfil do cliente | `01-cliente/perfil-grupo-olx.md` | Unidades de negocio, modelo de receita, maturidade |
| Stakeholders | `01-cliente/stakeholders.md` | Decisor, ponto focal, DRIs de cada frente |
| Acessos | `01-cliente/acessos-e-ferramentas.md` | O que ja esta liberado, o que falta |
| Checklist de dados | `02-diagnostico/checklist-dados-e-acessos.md` | Blocos A-J e status |

## Roteiro do kick-off

Siga o roteiro time-boxed de `06-reunioes/2026-08-24-kickoff.md`. Os blocos que **precisam sair fechados**:

1. **Contexto e escopo**: reafirmar o que o DR-E e e o que nao e (`00-playbook/01-fundamentos-dr-ote.md`). Alinhar que e obrigacao de meio.
2. **Governanca**: nomear: decisor, sponsor, DRI por frente, quem aprova a Matriz, quem assina a ata.
3. **Ritual**: datas dos 3 comites do ciclo, cadencia de assessoria assincrona, SLA de resposta.
4. **Dados e acessos**: percorrer os blocos A-J, atribuir dono e prazo a cada um que falta.
5. **Foco declarado**: o que o cliente acredita que e a restricao. Registrar como **hipotese**, nunca como diagnostico.

> A hipotese do cliente entra no `client.json` em `hipotese_cliente`, separada de `restricao_identificada`. Confundir as duas e o erro mais caro do metodo, o DR-E existe justamente porque a percepcao interna costuma apontar para o lugar errado.

## Estrutura de `dados/client.json`

```json
{
  "slug": "grupo-olx",
  "meta": {
    "cliente": "Grupo OLX",
    "produto": "DR-E",
    "inicio": "YYYY-MM-DD",
    "duracao_meses": 12,
    "ciclo_atual": 1,
    "fase_atual": "Identificar",
    "semana_corrente": 1,
    "version": 1,
    "atualizado_em": "YYYY-MM-DD"
  },
  "briefing": {
    "unidades_negocio": [],
    "modelo_receita": "",
    "ticket_medio": null,
    "ciclo_venda_dias": null,
    "receita_declarada_12m": null,
    "foco_declarado": "",
    "hipotese_cliente": ""
  },
  "contrato": {
    "valor_total": null,
    "diagnosticos_contratados": [],
    "sla_horas_uteis": 12,
    "comites_ano": 12,
    "bonus": {"gatilho": "", "divergencia_registrada": true}
  },
  "stakeholders": {
    "decisor": {"nome": "", "cargo": "", "empresa": "OLX"},
    "ponto_focal": {"nome": "", "cargo": "", "empresa": "OLX"},
    "consultor_dre": {"nome": "", "empresa": "V4"},
    "dris_por_frente": {}
  },
  "acessos": {},
  "conectores": {"fetched_at": null},
  "travas": {
    "cegueira": {"score": null, "dimensoes": {}, "evidencias": [], "diagnosticado_em": null},
    "exposicao": {"score": null, "dimensoes": {}, "evidencias": [], "diagnosticado_em": null},
    "atencao": {"score": null, "dimensoes": {}, "evidencias": [], "diagnosticado_em": null},
    "interesse": {"score": null, "dimensoes": {}, "evidencias": [], "diagnosticado_em": null},
    "qualificacao": {"score": null, "dimensoes": {}, "evidencias": [], "diagnosticado_em": null},
    "compromisso": {"score": null, "dimensoes": {}, "evidencias": [], "diagnosticado_em": null},
    "decisao": {"score": null, "dimensoes": {}, "evidencias": [], "diagnosticado_em": null},
    "retencao": {"score": null, "dimensoes": {}, "evidencias": [], "diagnosticado_em": null}
  },
  "restricao_identificada": null,
  "consolidacao_causal": null,
  "progress": {"skills": {}},
  "history": []
}
```

## Regras de preenchimento

- **Nunca invente numero.** Campo sem fonte fica `null` e vira linha no `PENDENCIAS.md`, com dono e prazo.
- **Toda afirmacao carrega fonte.** Se veio de e-mail, cite data e remetente. Se veio do contrato, cite a clausula.
- **Numero estimado leva marca `[E]`** no texto dos dossies e `"estimado": true` no JSON.
- `progress.skills` usa os estados `pending | in_progress | completed | approved`. Só a Matriz do GP usa `approved`.

## Finalizacao

1. Salve `dados/client.json`
2. Atualize os dossies de `01-cliente/` com o que foi fechado no kick-off (governanca, datas, DRIs)
3. Escreva a ata em `06-reunioes/` no formato do template, com decisoes e proximos passos com dono e prazo
4. Atualize `PENDENCIAS.md`: feche o que foi resolvido, abra o que surgiu
5. Sugira `/dre-fluxo-receita` como proximo passo
