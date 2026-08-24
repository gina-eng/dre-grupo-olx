# Materiais publicados

Páginas na identidade **Destrava Receita** (tokens extraídos de
<https://destrava-receita-docs.vercel.app/>). O arquivo `.html` aqui é a fonte; o link é a versão
publicada. Para atualizar, edite o `.html` e republique **no mesmo link** — publicar sem informar a
URL cria um artifact separado.

| Material | Fonte | Publicado | Público |
|---|---|---|---|
| Formulário de Kick-off | [2026-08-24-kickoff-formulario.html](2026-08-24-kickoff-formulario.html) | <https://claude.ai/code/artifact/ba21bc7f-17bf-4d09-a9c4-1b91700fdea0> | **Interno V4** — instrumento de condução |
| Cronograma de 12 meses | [cronograma-12-meses.html](cronograma-12-meses.html) | <https://claude.ai/code/artifact/620fdf4e-9ea2-4491-8512-1b3aac924070> | **Cliente** — apresentar no kick-off |
| Dicionário de Métricas | [dicionario-de-metricas.html](dicionario-de-metricas.html) | <https://claude.ai/code/artifact/3330df62-0d81-40b7-8c0f-ddd5090a61a4> | **Cliente** — entregar ao time de dados |

> Os artifacts nascem **privados**. Compartilhar com a OLX exige ação explícita no menu de
> compartilhamento da página. O material de uso interno (formulário) não deve ser compartilhado.

## Formulário de Kick-off

88 perguntas em 11 blocos, mais o checklist dos 10 blocos de dados (A–J) com responsável e prazo.
As respostas ficam no `localStorage` do navegador de quem preenche — não há estado compartilhado.
O botão **Exportar ata** gera o Markdown pronto para colar em `06-reunioes/` e alimentar
`/dre-onboarding`.

Cada pergunta declara o que ela alimenta (Fluxo de Receita, trava específica, auditoria contratada,
cláusula do contrato). As marcadas como **crítico** não podem sair da sala sem resposta ou sem dono
e prazo.

## Cronograma

Quatro ciclos de 12 semanas cobrindo 24/ago/2026 → 23/jul/2027, com 4 semanas de reserva até o fim
do contrato. Resolve duas questões que estavam abertas em [PENDENCIAS.md](../PENDENCIAS.md):

- **12 comitês** = 3 por ciclo × 4 ciclos.
- **4 presenciais** = o Comitê 2 de cada ciclo, que é o presencial no DR-E.

Datas de comitê propostas: **17/set**, **08/out** e **12/nov/2026**. A confirmar no kick-off.

Riscos de calendário já mapeados: o Ciclo 1 perde três segundas-feiras (07/set, 12/out, 02/nov) e o
Ciclo 3 abre no Carnaval de 2027 (08–09/fev).

## Dicionário de Métricas

78 métricas — 51 P0, 24 P1, 3 P2 — organizadas de baixo para cima no funil (T1 Retenção → T7
Exposição, mais Unit Economics transversal), no mesmo formato do dicionário feito para o Grupo Lupo.

> ⚠️ **Versão 0.** O catálogo pressupõe receita B2B por plano/assinatura de anunciante com motion
> sales-led. Essa leitura **não foi confirmada** pela OLX — `briefing.modelo_receita` ainda está
> `null` em [dados/client.json](../dados/client.json). Se o modelo for outro (take rate, lead avulso,
> mídia), as camadas de Decisão e Retenção mudam. As perguntas que confirmam isso estão no bloco 03
> do formulário; a v1 sai do próprio kick-off.
