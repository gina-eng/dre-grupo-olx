# Série de receita 2025–2026: o primeiro denominador auditável do projeto

> **O que é.** Leitura da V4 sobre a planilha de evolução de receita que o Grupo OLX enviou em
> **28/08/2026** na thread "Onboarding V4 e Grupo OLX". Original e procedência em
> [`assets/originais/A-visao-de-negocio-e-fluxo-de-receita/`](../assets/originais/README.md).
> Estado de máquina em [`dados/outputs/serie-receita-2025-2026.json`](../dados/outputs/serie-receita-2025-2026.json),
> gerado por `.claude/scripts/build_serie_receita.py`. Nenhum número desta página foi digitado à mão.
>
> **O que ela é, como dado.** Receita **bruta faturada**, 19 meses fechados (jan/2025 a jul/2026),
> aberta em 39 linhas sobre 4 unidades de negócio. É declarada pelo cliente, não auditada pela V4.
>
> **O que ela não é.** Não é truput. Não há coluna de custo, imposto ou margem, então ela não
> converte sozinha na métrica-mãe do método. E não é funil: continua sem volume por etapa.
>
> **Marcação de fonte:** `[D]` = declarado pelo cliente · `[E]` = derivação da V4 sobre o declarado.

---

## 1. O que a série fecha, e por que isso importa mais do que parece

Ela cobre o item **A1** do [checklist](checklist-dados-e-acessos.md) quase inteiro: 20 meses de
coluna contra os 24 pedidos, com a abertura por linha de negócio que o item exige.

E ela passa no teste que nenhum material do projeto tinha passado até aqui: **a soma das quatro
unidades bate com a linha TOTAL nos 19 meses**, com divergência máxima de R$ 51 sobre R$ 94,9
milhões, que é arredondamento ao real na exibição. A planilha é internamente consistente.

Isso importa porque o projeto vinha operando sem denominador. A [meta do
projeto](../03-estrategia/meta-do-projeto.md) propõe uma régua em pontos percentuais de run-rate, e
até 28/08 não havia como dizer quanto vale um ponto. Agora há.

| Candidata a vertical governante | Run-rate `[D]` | 1 p.p. vale |
|---|---|---|
| Grupo inteiro | R$ 103,8 mi/mês | R$ 1,04 mi/mês · R$ 12,5 mi/ano |
| Real Estate (vertical cheia) | R$ 50,0 mi/mês | R$ 500 mil/mês · R$ 6,0 mi/ano |
| `Classifieds - B&A` (núcleo de Imóveis) | R$ 42,8 mi/mês | R$ 428 mil/mês · R$ 5,1 mi/ano |
| Autos (vertical cheia) | R$ 34,4 mi/mês | R$ 344 mil/mês · R$ 4,1 mi/ano |
| `Classifieds - Dealers` (núcleo de Autos) | R$ 23,4 mi/mês | R$ 234 mil/mês · R$ 2,8 mi/ano |

> Run-rate = média mensal de jan–jul/2026, os 7 meses comparáveis entre os dois anos. Comparar 12
> meses de 2025 com 7 de 2026 é o erro mais fácil de cometer com esta planilha, e o script recusa
> fazê-lo.

---

## 2. O grupo cresce 9,8%, e Imóveis responde por um quinto disso

| Unidade | jan–jul/25 | jan–jul/26 | YoY | Peso na receita | Peso no **crescimento** |
|---|---|---|---|---|---|
| **TOTAL** | R$ 661,4 mi | R$ 726,5 mi | **+9,8%** | 100% | 100% |
| Real Estate | R$ 337,6 mi | R$ 350,1 mi | +3,7% | **48,2%** | **19,2%** |
| Autos | R$ 215,5 mi | R$ 240,9 mi | +11,8% | 33,2% | 39,0% |
| Goods & Services | R$ 108,3 mi | R$ 135,5 mi | **+25,1%** | 18,6% | **41,8%** |
| Conecta | ~0 | ~0 | - | 0% | 0% |

**A leitura:** Imóveis é quase metade da receita e menos de um quinto da tração. Autos e Goods &
Services, juntos 52% da receita, carregam **81% do crescimento**.

E o motor de Goods & Services não é assinatura: são `Intermediação` (+71,2%, R$ +24,8 mi) e `Taxa de
Entrega` (+17,6%), receita transacional de marketplace, take-rate sobre GMV. **É outro modelo de
negócio, com outra restrição.** Isso torna a [pendência 5](../PENDENCIAS.md) (escopo por unidade
não delimitado) cara em dinheiro, e não mais só em método: escolher Imóveis ou Autos como vertical
governante muda o denominador da meta em R$ 15,6 milhões por mês.

---

## 3. Os 3,7% de Imóveis são um artefato de portfólio, não desempenho comercial

Quatro linhas dentro de Real Estate foram desligadas entre 2025 e 2026:

| Linha | jan–jul/25 | jan–jul/26 | YoY |
|---|---|---|---|
| `CRM` | R$ 5,3 mi | R$ 0,7 mi | −87,0% |
| `Data` | R$ 3,4 mi | R$ 0,6 mi | −82,2% |
| `Transactional & Fintech - For Sale` | R$ 0,7 mi | R$ 0,0 mi | −97,1% |
| `Transactional & Fintech - Rentals` | R$ 0,6 mi | R$ 0,0 mi | −100,0% |
| **Arrasto somado** | | | **R$ −8,7 mi** |

Tirando as quatro, Real Estate cresce **+6,5%**, não +3,7%. E o núcleo, `Classifieds - B&A`, que
sozinho é 85% da vertical, cresce **+6,4%**.

> **Consequência de método:** qualquer meta ancorada na vertical cheia carrega decisões de portfólio
> que a V4 não controla e que não têm nada a ver com trava de receita. A meta precisa ser ancorada
> na **linha**, não na unidade. Isso é a mesma regra 3 do repositório aplicada ao denominador.

---

## 4. A série não confirma o net negativo declarado em Imóveis: e essa é a pergunta mais valiosa que ela abre

No kick-off, Iuna Scheffler declarou: *"as nossas entradas não estão compensando o churn mais
downgrade"* em Imóveis `[D]`. A [meta do projeto](../03-estrategia/meta-do-projeto.md) §6.1 construiu
sobre isso o conceito de **meta zero**: uma base que encolhe não persegue crescimento, persegue
inflexão, e metade da meta do ciclo se consumiria só em parar a sangria.

**A receita de `Classifieds - B&A` cresceu 6,4% em doze meses.** Ela não está encolhendo.

As duas afirmações só são compatíveis de três maneiras, e cada uma leva o Ciclo 1 para um lugar
diferente:

| # | Leitura | O que ela implicaria | Como testar |
|---|---|---|---|
| **a** | O net negativo é de **logo**, não de receita. A base perde clientes e o preço segura o faturamento | A pior das três. Um sistema que parece saudável no P&L e está se esvaziando por baixo. O ticket médio estaria subindo por reajuste, não por valor entregue | Contagem de clientes ativos B2B, mês a mês, ao lado da receita |
| **b** | O net negativo é de um **subsegmento** dentro de B&A (uma praça, um porte, um produto) | A meta zero existe, mas é local, e o denominador dela é muito menor que R$ 42,8 mi/mês | Abertura de B&A por porte de cliente e por praça |
| **c** | O net negativo é **recente** e a série ainda não o mostra no acumulado | Sustentável pelos dados: a tração cai de **+9,2%** (jan–mar) para **+4,9%** (mai–jul), −4,2 p.p. em um semestre | Fechamento de ago e set/26, que a planilha ainda não traz |

A leitura **c** tem evidência dentro da própria série. As leituras **a** e **b** não são
verificáveis com o que existe hoje, e a **a** é a que mais muda o projeto.

> **Isto não desmente o cliente.** Iuna descreve um movimento que ela vê no sistema dela; a série
> mede receita bruta faturada. As duas coisas podem estar certas ao mesmo tempo, e o ponto onde
> elas se encontram é exatamente onde a trava de Retenção mora.

---

## 5. O churn de 8–10% ao mês não pode ser sobre receita: a série impõe o limite

O churn declarado é de **8–10% ao mês** `[D]`, com a
[ambiguidade 4](jornada-do-cliente-profissional.md) em aberto: é sobre cliente ou sobre receita?
A série responde por aritmética `[E]`.

A base de `Classifieds - B&A` cresceu 6,4% em doze meses, o que é uma deriva líquida de **+0,52% ao
mês**. Entradas brutas têm de repor o churn e ainda produzir essa deriva:

| Se o churn de **receita** for | A OLX precisa vender, todo mês | Por ano | Equivalente à base |
|---|---|---|---|
| 2%/mês | R$ 1,08 mi | R$ 13 mi | 30% |
| 5%/mês | R$ 2,36 mi | R$ 28 mi | 66% |
| **9%/mês** | **R$ 4,07 mi** | **R$ 49 mi** | **114%** |

Ou seja: se 9% fosse churn de receita, o Grupo OLX reconstruiria **mais que a totalidade** da
carteira de Imóveis todo ano, numa vertical onde metade da entrada nasce de prospecção ativa e
depende de capacidade humana `[D]`. Isso não é impossível, mas é uma afirmação extraordinária, e
ninguém no projeto a fez.

**A leitura provável `[E]`:** os 8–10% são churn de **logo**, concentrado numa cauda de contas
pequenas, e o churn de receita é uma fração disso. Se for esse o caso, o modelo de elasticidade da
[meta do projeto](../03-estrategia/meta-do-projeto.md) §4.1, que trata 9% como churn de receita,
**superestima o valor de um ponto de churn**, e o ranking das alavancas precisa ser refeito antes
de virar meta.

> Isto não invalida a direção do modelo, que é a de que retenção vale mais que aquisição numa base
> recorrente. Invalida a **calibragem**, e calibragem é o que separa uma faixa proposta de um
> número acordado. É o insumo 4 da §8 da meta do projeto, e ele acabou de ficar mais urgente.

---

## 6. A meta de ciclo, como está proposta hoje, não é verificável na receita bruta

Este é o achado com consequência operacional mais direta.

A série é serrilhada. Medindo a variação de 90 dias sobre a média móvel de 3 meses, que é a forma
mais estável de ler um trimestre, o **ruído próprio** de cada linha é:

| Linha | Desvio de uma leitura de 90 dias (1σ) | Efeito mínimo detectável (2σ) |
|---|---|---|
| Real Estate | ±2,80% | **+5,60%** |
| `Classifieds - B&A` | ±2,83% | **+5,67%** |
| `Classifieds - Dealers` | ±3,99% | +7,98% |
| Autos | ±4,50% | +8,99% |
| Grupo inteiro | ±4,16% | +8,32% |

A [meta do projeto](../03-estrategia/meta-do-projeto.md) §6 propõe para o Ciclo 1 um alvo de **+3 a
+6 p.p. de run-rate**. Contra uma banda de ±2,8%, **a metade de baixo dessa faixa é
indistinguível de ruído**, e mesmo o topo fica na fronteira.

Some-se a isso a inércia já documentada: com constante de tempo de 11 meses, uma injeção implantada
no início do Ciclo 1 tem **cerca de 24% do seu ganho de regime materializado** ao fim de 3 meses
`[E]`. O ciclo é curto para o sistema que ele mexe.

**As três correções que isso obriga:**

1. **A meta de ciclo se mede no indicador da restrição, não na receita.** Uma taxa de conversão de
   primeira fatura tem denominador de milhares de contratos por mês e detecta 2 p.p. com folga; a
   receita bruta da vertical não detecta 5. O efeito em receita entra como **consequência derivada**
   e declarada, nunca como o número que prova o ciclo. Isso já é o que a régua de três níveis
   propõe, e a série agora dá a razão técnica para defendê-la.
2. **Se a receita for lida, é em média móvel de 3 meses com a banda declarada junto.** Ler o mês
   isolado é pior: o desvio mensal de B&A é de 5,96 p.p., maior que a meta inteira do ciclo.
3. **A sazonalidade da janela precisa ser descontada, e a notícia aqui é boa.** De agosto a
   novembro de 2025, Real Estate variou **−0,1%** e `Classifieds - B&A` **+0,6%**. A janela do
   Ciclo 1 é sazonalmente quase neutra em Imóveis, então o que aparecer ali é do ciclo. Em Autos
   não: `Classifieds - Dealers` sobe +3,1% sozinho no mesmo período, e uma meta de +3 p.p. medida
   em Autos seria integralmente entregue pelo calendário.

> Testei antes a normalização por **dia útil**, que é o reflexo comum para receita serrilhada, e ela
> **piora** a variância em todas as linhas. O que reduz é dia corrido (de 5,48 para 3,49 em Real
> Estate), o que faz sentido para uma base de assinatura que acumula por dia de calendário, e não
> por expediente. Em Autos nem isso funciona, o que é mais uma evidência de que Autos é um sistema
> de receita diferente.

---

## 7. Três coisas na planilha que precisam de explicação do cliente

1. **Valores negativos.** `Transactional & Fintech - For Sale` tem meses negativos em jul, ago e
   set/25 e em mar e abr/26. Estorno, reclassificação contábil ou provisão revertida mudam a
   leitura, e nenhuma delas é receita.
2. **Linhas que zeram no meio da série.** `CRM` some em set/25, volta com R$ 561 mil em fev/26 e
   some de novo. `Data` cai a zero em abr/26. `Rentals` termina em dez/25 com R$ 566. Descontinuação
   de produto e migração de rubrica produzem o mesmo desenho e têm significados opostos.
3. **`Conecta`.** A unidade registra R$ 318, R$ 40 e R$ 20 nos três primeiros meses de 2025, nada
   depois, e um único lançamento de **R$ 6.865.055 em set/25**. Um valor isolado dessa ordem numa
   unidade zerada é reclassificação ou evento não recorrente, e ele está dentro do TOTAL do mês.

---

## 8. O que a série ainda não resolve

| Falta | Consequência | Item |
|---|---|---|
| P&L por vertical | A receita não vira truput, e a métrica-mãe do método continua sem denominador | Insumo 2 da meta, DRI Matheus Rodrigues |
| Metas 2026 da OLX | A âncora da meta continua sendo só a matemática da V4 | Insumo 1, próximo passo #2 |
| Contagem de clientes ativos, mês a mês | Sem ela não se separa preço de volume, e a §4 fica sem resposta | Novo, ver PENDENCIAS |
| 2024 | Com 20 meses não se separa tendência de ciclo. O A1 pede 24 por isso | A1, parcial |
| Volumes por etapa do funil | O fluxo de receita continua sem reconciliar contra o faturamento (regra 8) | A2 e A3, abertos |

---

## Estado

- Original: `assets/originais/A-visao-de-negocio-e-fluxo-de-receita/evolucao-receita-2025-2026.{csv,xlsx}`
- Estado de máquina: [`dados/outputs/serie-receita-2025-2026.json`](../dados/outputs/serie-receita-2025-2026.json)
- Regenerar: `python3 .claude/scripts/build_serie_receita.py`
- Alimenta: [`03-estrategia/meta-do-projeto.md`](../03-estrategia/meta-do-projeto.md) §5, §6 e §8, o
  forecast (POP 27) e o diagnóstico da trava de Retenção
