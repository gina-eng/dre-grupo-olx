---
name: dre-v4mos
description: "Puxa dados reais de midia paga do V4MOS (Meta e Google Ads) para o diagnostico das travas e para o forecast. Use quando o operador disser /dre-v4mos ou 'puxar dados do V4MOS' ou 'dados de midia' ou 'conectar V4MOS'."
dependencies:
  - dre-onboarding
tools: []
fase: "1 — Identificar"
estimated_time: "20 min"
output_file: "dados/client.json (secao conectores)"
---

# DR-E — V4MOS

O V4MOS e o data hub da V4: expoe, por API, os dados de midia paga que o cliente ja tem nas
plataformas, sem depender de exportacao manual. Para o DR-E ele alimenta o diagnostico das travas de
**Exposicao**, **Atencao** e **Qualificacao**, e os parametros de CAC do forecast.

## Modelo de acesso

| | |
|---|---|
| API | `https://api.data.v4.marketing/v1` |
| Autenticacao | headers `x-client-id` e `x-client-secret` |
| Escopo | query `organizationId` — o **workspace** do cliente |
| Credenciais | `.credentials/clients.json`, na raiz do repositorio |

`.credentials/` esta no `.gitignore` e o arquivo roda em `chmod 600`. **Credencial nunca entra no
repositorio, em nenhuma hipotese** — nem em `client.json`, nem em documento, nem em mensagem. O
`workspace_id` (= `organizationId`) nao e segredo e vive em `dados/client.json` → `meta.workspace_id`.

Formato de `.credentials/clients.json` — chaveado pelo workspace:

```json
{
  "<workspace_id>": {
    "nome": "Grupo OLX",
    "client_id": "<uuid>",
    "client_secret": "<hex de 64 chars>"
  }
}
```

## Endpoints disponiveis

Seis, todos paginados (`limit`, `page`, `meta.hasNextPage`) e filtraveis por `createdStart` /
`createdEnd` em `AAAA-MM-DD`:

| Endpoint | Alimenta |
|---|---|
| `facebook/ads/campaigns` | Exposicao · investimento e alcance por campanha |
| `facebook/ads/ad` | Atencao · CTR e CPC por anuncio |
| `facebook/ads/creatives` | Atencao · diversidade e fadiga criativa |
| `google/ads/campaigns` | Exposicao · investimento e impressoes |
| `google/ads/keywords` | Exposicao e Qualificacao · intencao de busca |
| `google/ads/gender` | Qualificacao · aderencia do publico ao ICP |

## Como rodar

```bash
bash .claude/scripts/v4mos_fetch.sh dados
```

O script le `dados/client.json` → `meta.workspace_id`, sobe ate 5 niveis procurando
`.credentials/clients.json`, pagina todos os endpoints e grava o resultado em `dados/client.json` →
`conectores`, com `fetched_at`.

Se `meta.workspace_id` estiver ausente, ele sai com `SKIP` — nao e erro, e cliente sem integracao.

## Como ler o retorno

| Situacao | Leitura |
|---|---|
| **HTTP 401** | Credencial invalida. Conferir `client_id` e `client_secret`. |
| **HTTP 403** | O `organizationId` nao pertence a essa credencial. Workspace errado. |
| **HTTP 400** | Integracao nao disponivel para esse workspace naquele endpoint. |
| **HTTP 200 com `data: []`** | Autenticado e autorizado, mas **sem dado ingerido**. Nao e falha tecnica — e ausencia de integracao entre a plataforma de anuncios e o V4MOS. |

Essa ultima linha e a mais importante e a mais facil de ler errado. `200` com lista vazia significa
que o caminho ate o dado esta aberto e nao ha dado do outro lado. Antes de reportar como problema
tecnico, cheque se as contas de anuncio do cliente foram de fato conectadas ao workspace.

**Teste de sanidade** — dois controles que separam "sem dado" de "sem acesso":

- Secret invalido deve devolver **401**. Se devolver 200, a autenticacao nao esta sendo validada.
- `organizationId` inexistente deve devolver **403**. Se devolver 200 vazio, voce nao esta consultando
  o workspace que pensa estar.

Rode os dois antes de concluir qualquer coisa sobre ausencia de dado.

## Estado no Grupo OLX

Verificado em **24/08/2026**: autenticacao **OK** nos seis endpoints (401 com secret errado, 403 com
org inexistente — os dois controles passam), e **zero registros** em qualquer janela, inclusive sem
filtro de data.

Conclusao: o workspace existe e a credencial e valida, mas **nenhuma conta de midia foi ingerida
ainda**. Isso e coerente com o **bloco G (Midia Paga)** do
[checklist de dados](../../../02-diagnostico/checklist-dados-e-acessos.md), que segue pendente — os
acessos as contas Google e Meta ainda nao foram concedidos a `gina@v4company.com`.

**Enquanto o bloco G nao fechar**, o diagnostico de midia depende de exportacao manual. Registre isso
em `PENDENCIAS.md` em vez de tratar a lista vazia como dado real: um diagnostico de Exposicao que le
"investimento = 0" e conclui "o cliente nao investe em midia" e um erro grave e perfeitamente
evitavel.

## Quem consome

- `/ee-s2-diagnostico-midia` — declara `v4mos_data: true` e usa `conectores` direto
- `/dre-diagnostico-trava` — camada analitica de Exposicao, Atencao e Qualificacao
- `/dre-forecast` — CAC e % de investimento em midia
- `/dre-fluxo-receita` — volumes de topo de funil

## Finalizacao

1. Rode o fetch e confira `conectores.fetched_at`
2. Se vier vazio, **nao** preencha o diagnostico com zero: registre a pendencia com dono e prazo
3. Atualize `dados/client.json` (version++, `history[]`)
4. Sugira `/ee-s2-diagnostico-midia` quando houver dado
