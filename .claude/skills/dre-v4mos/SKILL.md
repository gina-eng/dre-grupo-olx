---
name: dre-v4mos
description: "Puxa dados reais de midia paga do V4MOS (Meta e Google Ads) para o diagnostico das travas e para o forecast. Use quando o operador disser /dre-v4mos ou 'puxar dados do V4MOS' ou 'dados de midia' ou 'conectar V4MOS'."
dependencies:
  - dre-onboarding
tools: []
fase: "1, Identificar"
estimated_time: "20 min"
output_file: "dados/client.json (secao conectores)"
---

# DR-E · V4MOS

O V4MOS e o data hub da V4: expoe, por API, os dados de midia paga que o cliente ja tem nas
plataformas, sem depender de exportacao manual. Para o DR-E ele alimenta o diagnostico das travas de
**Exposicao**, **Atencao** e **Qualificacao**, e os parametros de CAC do forecast.

## Modelo de acesso

| | |
|---|---|
| API | `https://api.data.v4.marketing/v1` |
| Autenticacao | headers `x-client-id` e `x-client-secret` |
| Escopo | query `organizationId`, o **workspace** do cliente |
| Credenciais | `.credentials/clients.json`, na raiz do repositorio |

`.credentials/` esta no `.gitignore` e o arquivo roda em `chmod 600`. **Credencial nunca entra no
repositorio, em nenhuma hipotese**, nem em `client.json`, nem em documento, nem em mensagem. O
`workspace_id` (= `organizationId`) nao e segredo e vive em `dados/client.json` → `meta.workspace_id`.

Formato de `.credentials/clients.json`, chaveado pelo workspace:

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

Se `meta.workspace_id` estiver ausente, ele sai com `SKIP`, nao e erro, e cliente sem integracao.

## Como ler o retorno

| Situacao | Leitura |
|---|---|
| **HTTP 401** | Credencial invalida. Conferir `client_id` e `client_secret`. |
| **HTTP 403** | O `organizationId` nao pertence a essa credencial. Workspace errado. |
| **HTTP 400** | Integracao nao disponivel para esse workspace naquele endpoint. |
| **HTTP 200 com `data: []`** | Autenticado e autorizado, mas **sem dado ingerido**. Nao e falha tecnica, e ausencia de integracao entre a plataforma de anuncios e o V4MOS. |

Essa ultima linha e a mais importante e a mais facil de ler errado. `200` com lista vazia significa
que o caminho ate o dado esta aberto e nao ha dado do outro lado. Antes de reportar como problema
tecnico, cheque se as contas de anuncio do cliente foram de fato conectadas ao workspace.

**Teste de sanidade**: dois controles que separam "sem dado" de "sem acesso":

- Secret invalido deve devolver **401**. Se devolver 200, a autenticacao nao esta sendo validada.
- `organizationId` inexistente deve devolver **403**. Se devolver 200 vazio, voce nao esta consultando
  o workspace que pensa estar.

Rode os dois antes de concluir qualquer coisa sobre ausencia de dado.

## Estado no Grupo OLX

Atualizado em **14/09/2026**. As tres contas ingerem, e a coleta larga (01/01/2025 a 14/09/2026) e a
referencia atual do projeto:

| Lado | Coleta de 14/09 |
|---|---|
| **Google Ads** (MCC 526-656-0190) | 23 campanhas, R$ 2.746.029,59, 56,4 mi de impressoes, 10,17 mi de cliques, CTR 18,03%, CPA R$ 3,06. **So 11 dos 21 meses tem dado**: faltam nov/2025 a abr/2026 |
| **Meta Ads** (612188193108418 e 1742214902479721) | 90 campanhas, 1.079 anuncios, R$ 7.375.303,34, 1,88 bi de impressoes, 29,4 mi de cliques, 1,41 bi de alcance, CPM R$ 3,91, CTR 1,56%. **21 meses continuos** |

> 🔴 **CORRIGIDO EM 16/09, LEIA ANTES DE USAR.** A frase abaixo esta errada e foi mantida so como historico.
> O V4MOS cobre **15,7%** do investimento de Google do grupo: de abril/2025 a junho/2026 a serie mensal dele e,
> centavo por centavo, **uma conta so**, a de performance regional de SP do VivaReal. O buraco de nov/2025 a
> abr/2026 nao e falha de ingestao, e essa conta parada. **Nao use o Google do V4MOS como investimento do grupo,
> nem a razao Meta/Google.** Ver `02-diagnostico/diagnostico-vi-midia-paga.md`.

~~O Meta investe **2,7 vezes** o Google na mesma janela, e e a unica serie mensal de midia sem buraco,
portanto a unica utilizavel em `/dre-forecast`.~~

**Historico, porque ele explica dois defeitos ja corrigidos.** Ate 08/09 o Meta devolvia zero nos
seis endpoints, com os dois controles de sanidade passando, isto e, acesso nao concedido e nao falha
tecnica. As contas sairam no lote de acessos de 10/09 e a ingestao comecou em 12/09, mas ficou
invisivel por dois dias porque o script gravava so na chave `connectors`, em ingles, que as skills
`dre-*` nao leem. Hoje ele grava nas duas, `connectors` e `conectores.v4mos.ultima_coleta`. O
segundo defeito era o payload cru ir para dentro do `client.json`; agora ele vai para
`dados/cache/v4mos-<data>.json`, fora do git e regeneravel.

**A ressalva que substituiu a antiga, e que vale para todo consumidor desta skill:** o bloco G
fechou no que era acesso, e nao fechou no que e recorte. **Nenhuma das tres contas separa B2B de
B2C**, e 90,4% do investimento de Meta esta em campanhas com sufixo `_pf`, a mesma nomenclatura que
levanta a hipotese de consumidor final no Google (`PENDENCIAS.md`, pendencia 12). Os R$ 10,12 mi
medidos **nao sao** o investimento do recorte B2B contratado.

O erro a evitar mudou de forma, nao de natureza. Antes era ler "investimento = 0" e concluir que o
cliente nao investe em midia. Agora e ler R$ 10,12 mi e usar como numerador de um CAC B2B. Os dois
sao o mesmo erro: tratar o que a ferramenta devolve como se fosse a pergunta que foi feita.

## Quem consome

- `/ee-s2-diagnostico-midia`: declara `v4mos_data: true` e usa `conectores` direto
- `/dre-diagnostico-trava`: camada analitica de Exposicao, Atencao e Qualificacao
- `/dre-forecast`: CAC e % de investimento em midia
- `/dre-fluxo-receita`: volumes de topo de funil

## Finalizacao

1. Rode o fetch e confira `conectores.fetched_at`
2. Se vier vazio, **nao** preencha o diagnostico com zero: registre a pendencia com dono e prazo
3. Atualize `dados/client.json` (version++, `history[]`)
4. Sugira `/ee-s2-diagnostico-midia` quando houver dado
