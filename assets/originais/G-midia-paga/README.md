# Bloco G · Mídia Paga

Exports diretos da interface do **Google Ads**, uma pasta por conta vinculada à MCC do Viva Real.

> ⚠️ **Confidencial.** Cobre o aviso das comunicações da OLX e a cláusula 5.3 do contrato. Não sai
> deste repositório privado.

## Procedência

| Item | Detalhe |
|---|---|
| Origem | Interface do Google Ads, contas vinculadas à **MCC Viva Real** |
| Exportado em | **16/09/2026**, entre 16h00 e 16h39 |
| Conta usada | operador V4, com o acesso concedido no lote de 10/09 |
| Janela | de cada conta, do primeiro dado até 16/09/2026 |
| Volume | 5 contas · 177 campanhas · **R$ 70,91 mi** acumulados |
| Leitura | [`02-diagnostico/diagnostico-vi-midia-paga.md`](../../02-diagnostico/diagnostico-vi-midia-paga.md) |
| Estado de máquina | [`dados/outputs/google-ads-parque.json`](../../dados/outputs/google-ads-parque.json), gerado por [`build_google_ads_parque.py`](../../.claude/scripts/build_google_ads_parque.py) |

> 🔴 **O export não traz `customer ID` nem o nome oficial da conta.** A identidade de cada uma foi
> **inferida**, por domínio de destino dos anúncios e por convenção de nome de campanha, e a
> evidência está declarada na tabela abaixo. Amarrar cada pasta ao seu `customer ID` é
> [pendência 41](../../PENDENCIAS.md).

## As cinco contas

| Pasta | O que é | Recorte | Primeiro dado | Campanhas | Investimento acumulado |
|---|---|---|---|---:|---:|
| `conta-1-zapmais-b2b/` | ZAP+ / CanalPro, o produto do anunciante profissional | **B2B** | 24/09/2021 | 56 | R$ 2.455.122,45 |
| `conta-2-vivareal-marca/` | VivaReal, busca de marca | **B2C** | 04/07/2024 | 3 | R$ 1.282.927,13 |
| `conta-3-vivareal-sp/` | VivaReal, performance regional com recorte SP | **B2C** | 16/05/2025 | 9 | R$ 2.384.921,36 |
| `conta-4-vivareal-brasil/` | VivaReal Brasil, a conta principal | **B2C** | 01/10/2016 | 92 | R$ 63.330.730,81 |
| `conta-5-vivareal-app/` | VivaReal, instalação de app e vídeo | **B2C** | 01/10/2016 | 17 | R$ 1.454.877,67 |
| **Total** | | | | **177** | **R$ 70.908.579,42** |

**Evidência da identidade de cada conta**

| Pasta | Como foi identificada |
|---|---|
| `conta-1-zapmais-b2b` | anúncios apontam para `movimento.zapmais.com`, `www.zapmais.com.br`, `conteudo.zapmais.com`, `anuncie.zapimoveis.com.br` e `www.datazap.com.br`; campanhas com sufixo `_go_pf` |
| `conta-2-vivareal-marca` | domínio único `www.vivareal.com.br`; 3 campanhas, todas Search de marca, sufixo `_vr_pf` |
| `conta-3-vivareal-sp` | domínio único `www.vivareal.com.br`; Search e PMax com recorte `sp` no nome; primeira veiculação em 16/05/2025 |
| `conta-4-vivareal-brasil` | domínio único `www.vivareal.com.br`; 92 campanhas, DSA e PMax nacionais, histórico desde 2016 |
| `conta-5-vivareal-app` | 14 anúncios apontam para `play.google.com`; campanhas App (UAC) e YouTube; nenhuma ativa |

**Uma conta é B2B e quatro são B2C.** A `conta-1` é a única que fala com o anunciante profissional e
responde por **3.5%** do investimento acumulado do parque. É o recorte contratado do
DR-E. As outras quatro compram o consumidor que procura imóvel: não são objeto deste contrato, mas
entram no diagnóstico porque **dividem a mesma medição** e contaminam todo número de mídia do projeto.

## Conferência

A soma das campanhas bate com a linha `Total: Account` do próprio export em três contas e diverge em
duas, por campanha removida cujo gasto fica no total da conta e não aparece na lista:

| Conta | Soma das campanhas | `Total: Account` | Delta |
|---|---:|---:|---:|
| `conta-1-zapmais-b2b` | R$ 2.455.122,45 | R$ 2.476.102,84 | R$ -20.980,39 |
| `conta-2-vivareal-marca` | R$ 1.282.927,13 | R$ 1.282.927,13 | - |
| `conta-3-vivareal-sp` | R$ 2.384.921,36 | R$ 2.384.921,36 | - |
| `conta-4-vivareal-brasil` | R$ 63.330.730,81 | R$ 63.330.730,82 | - |
| `conta-5-vivareal-app` | R$ 1.454.877,67 | R$ 1.487.914,24 | R$ -33.036,57 |

## O que cada pasta tem

```
<conta>/
├── campanhas.csv            campanhas da conta, com custo, conversão, tipo e estratégia de lance
├── grupos-de-anuncios.csv
├── anuncios.csv[.gz]        criativo a criativo, com título, descrição e URL final
├── grupos-de-ativos.csv     só nas contas com Performance Max
├── palavras-chave.csv       só nas contas com Search de palavra-chave
├── serie-mensal-*.csv       uma por métrica exportada no gráfico da visão geral
└── overview/                cartões da visão geral: série trimestral, dispositivo, demografia,
                            termo de busca, leilão, rede, nota de otimização, maiores mudanças
```

| Conta | Relatórios | `overview/` | Séries mensais |
|---|---:|---:|---|
| `conta-1-zapmais-b2b` | 5 | 17 | impressoes |
| `conta-2-vivareal-marca` | 4 | 16 | conversoes, cliques |
| `conta-3-vivareal-sp` | 5 | 17 | conversoes, impressoes |
| `conta-4-vivareal-brasil` | 5 | 15 | custo, impressoes |
| `conta-5-vivareal-app` | 3 | 14 | custo, impressoes |

### Proxy no git, master fora

Um arquivo passa de 2 MB: `conta-4-vivareal-brasil/anuncios.csv`, **59.364 linhas e 30,3 MB**, o
inventário de criativos de dez anos de VivaReal. No git ele entra comprimido (`anuncios.csv.gz`,
**2,1 MB**, 14x menor, lido com `zcat` ou `gzip.open`); o original fica em
`_masters/G-midia-paga/google-ads/conta-4-vivareal-brasil/`, bloqueado pelo `.gitignore`. Mesma regra
dos vídeos do bloco E.

**Os 31 relatórios foram conferidos byte a byte** contra a origem, por SHA-256, antes de a pasta de
origem ser removida. Os 79 arquivos de `overview/` vieram dos cinco zips originais.

## 🔴 Cinco séries mensais foram perdidas na organização

Erro do operador, registrado aqui porque a origem não existe mais. Quatro contas tinham **mais de uma**
série mensal de impressões exportada, a `conta-1` tinha três, e os nomes de destino colidiram: a cópia
posterior sobrescreveu a anterior. A pasta de origem foi apagada na mesma execução, antes de a
conferência de hash acusar.

| Conta | Arquivo perdido | Tamanho | SHA-256 |
|---|---|---:|---|
| `conta-1-zapmais-b2b` | `Time_series_chart(2015.10.01-2026.09.01).csv` | 2387 B | `e4dc0fddd584…` |
| `conta-1-zapmais-b2b` | `Time_series_chart(2015.10.01-2026.09.01) (1).csv` | 2333 B | `5515d4db2539…` |
| `conta-3-vivareal-sp` | `Time_series_chart(2016.10.01-2026.09.01) (1).csv` | 1808 B | `7766461fab05…` |
| `conta-4-vivareal-brasil` | `Time_series_chart(2016.10.01-2026.09.01) (4).csv` | 2953 B | `92905c9d7c47…` |
| `conta-5-vivareal-app` | `Time_series_chart(2016.10.01-2026.09.01) (7).csv` | 2375 B | `4cb0698a1690…` |

**O que isso custa:** nada de estrutural. São gráficos de **impressões mensais**. A série trimestral
de custo, cliques e conversões de cada conta sobreviveu inteira em `overview/time-series.csv`, que é a
que o diagnóstico usa, e nenhum relatório de campanha, grupo, anúncio ou palavra-chave foi afetado.
Cada conta afetada ainda tem uma série de impressões: o que se perdeu foram as variantes.

**Como repor:** reexportar o gráfico da visão geral com a métrica *Impressões* nas contas 1, 3, 4 e 5.
Quatro cliques por conta. Está em [pendência 41](../../PENDENCIAS.md).
