# Meta do projeto: proposta da V4

> **O que este documento é.** A execução do próximo passo **#5** do kick-off, *"sugestão de meta de
> projeto ancorada nas metas da OLX, V4, 10/09"*
> ([conferência do kick-off](../06-reunioes/2026-08-24-kickoff-o-que-a-transcricao-fecha.md), §10).
> Ele entrega a **régua** e a **matemática que produz o número**, não o número.
>
> **O que ele não é.** Não é forecast (esse é o POP 27, e não roda sem fluxo reconciliado). Não é a
> meta acordada, nenhuma meta se acorda antes da trava governante estar validada em ata. E não
> contém um único valor absoluto, porque o material de metas comprometido por Matheus Rodrigues e
> Iuna Scheffler ainda não chegou (próximo passo **#2**, prazo 09/09).
>
> **Marcação de fonte:** `[D]` = declarado pelo cliente em reunião, não apurado · `[E]` = derivação
> da V4 sobre dado declarado. Regras 1 e 2 do [repositório](../CLAUDE.md).

---

## 1. Por que a V4 chega com a meta pronta

A OLX ficou de calcular a meta. Se ela chegar pronta do lado do cliente, ela virá na régua do
FP&A, **receita acumulada no ano fiscal**, e essa régua, aplicada a este sistema, tem um defeito
matemático que a §4 demonstra: ela esconde entre 4 e 6 vezes o valor que o projeto constrói, e
concentra 75% do mérito no primeiro ciclo.

Não é questão de negociar um número mais fácil. É que a régua errada faria a V4 assinar um alvo que
a própria inércia da base de recorrência impede de atingir dentro de doze meses, e apagaria do
placar exatamente os ciclos 3 e 4, que são onde a mudança estrutural acontece.

Quem define a régua conduz a conversa. Essa é a razão de a V4 chegar na apresentação dos
diagnósticos com esta proposta em vez de receber a deles.

> ⚠️ **A data mudou, o compromisso não.** O próximo passo #5 do kick-off marcava esta entrega para
> 10/09. Com o reajuste de 03/09, a apresentação dos diagnósticos passou para **24/09** e é ali que
> esta proposta entra. Ver [cronograma-e-marcos.md](../04-execucao/cronograma-e-marcos.md).

---

## 2. O que o método obriga, antes de qualquer número

| # | Regra | Fonte | Consequência para a meta |
|---|---|---|---|
| 1 | A métrica-mãe é **truput** (vendas − custos totalmente variáveis), nunca faturamento bruto | [Fundamentos](../00-playbook/01-fundamentos-dr-ote.md#throughput-como-métrica-mãe) | A meta é de margem de contribuição. E o cliente **já concordou**: *"sou mais disposto a sacrificar a receita e melhorar a margem do que o contrário"*, Matheus Rodrigues, 01:58:27 |
| 2 | **Uma restrição por ciclo** | Princípio inegociável 2 | Não existe meta com três alavancas simultâneas. Cada ciclo tem um indicador, e ele é o da restrição vigente |
| 3 | A meta **não é premissa do forecast**, o forecast nasce da matemática do sistema atual, e a meta do cliente entra como linha de referência | [POP 27](../.claude/skills/dre-forecast/SKILL.md) | Se a linha "Com Injeção" não alcança a meta declarada, **isso é o achado**, não um erro a corrigir |
| 4 | Explorar antes de expandir; nunca elevar a entrada com o balde furado | [Regra de Goldratt](../00-playbook/01-fundamentos-dr-ote.md#lógica-de-investigação-de-baixo-para-cima) | A meta do Ciclo 1 é obrigatoriamente **sem novos recursos**. Meta que precisa de verba nova no primeiro ciclo é meta fora do método |
| 5 | Nada de número sem fonte | Regra 1 do repositório | O valor absoluto fica `null` até o material de metas chegar |

E um dado de contexto econômico que o próprio cliente deu e que **muda o desenho da meta**: margem
de contribuição perto de 100%, sem COGS de produto, com mídia e imposto como únicos ofensores
relevantes `[D]`. Num negócio assim, **receita ganha por conversão e retenção é quase inteiramente
truput**, enquanto receita ganha por exposição carrega o CAC junto. A meta correta pesa alavancas
que não consomem mídia, e isso é a mesma direção que o método já obriga pela regra 4.

---

## 3. O que já temos na mão para conduzir

Seis taxas com origem nomeada, apresentadas pela própria OLX em 28/08
([jornada do cliente profissional](../02-diagnostico/jornada-do-cliente-profissional.md)):

| Etapa | Taxa `[D]` | O que ela é, em linguagem de sistema |
|---|---|---|
| Entrada | 50% da base nasce de prospecção ativa | Dependência de capacidade humana na aquisição |
| Contratação | canal online = 25% da receita de Autos, 10% de Imóveis | Peso do autosserviço |
| Pagamento | **80%** dos que contratam e geram cobrança pagam a 1ª fatura | **20% de vazamento entre contrato e caixa** |
| Publicação | **12%** saem no 1º mês sem publicar (até 20% no online, 8–10% no assistido) | Vazamento de ativação, concentrado no autosserviço |
| Leads | 89% dos anúncios de Imóveis não recebem lead | A entrega média do produto é zero |
| Recorrência | churn **8–10%/mês**, baixa performance como principal motivo | O denominador da recorrência |

Mais três coisas que valem tanto quanto as taxas:

- **Os dashboards existem** e abrem por vertical, canal, time e período, com processamento diário,
  Lu Machim, 28/08. O trabalho da V4 mudou de *coletar* para *extrair*.
- **A OLX declarou net de receita negativo em Imóveis:** *"as nossas entradas não estão compensando
  o churn mais downgrade"* (Iuna Scheffler) `[D]`. Isso muda a natureza da meta do primeiro ciclo,
  ver §6.
- **O cliente já votou na trava:** Retenção 3, Qualificação 2. Percepção, não diagnóstico, mas
  percepção que converge com as taxas acima.

---

## 4. A matemática do sistema: e o achado que muda a régua

O sistema de receita B2B é uma base recorrente. Sua receita de regime obedece a uma identidade de
três termos, todos declarados:

```
Receita de regime  ∝  contratos × p(pagamento) × p(publicação) × ticket
                      ─────────────────────────────────────────────────
                                    churn mensal
```

Com os valores `[D]` (80% · 88% · 9%), cada real de contrato novo sustenta **7,8 reais** de receita
de base. Daí saem duas leituras que valem a apresentação inteira.

### 4.1 Quanto vale cada alavanca `[E]`

Elasticidade da receita **de regime**, uma alavanca por vez:

| Alavanca | Movimento | Efeito no regime |
|---|---|---|
| Pagamento da 1ª fatura | 80% → 85% | **+6,2%** |
| Pagamento da 1ª fatura | 80% → 90% | **+12,5%** |
| Publicação no 1º mês | 88% → 92% | **+4,5%** |
| Churn mensal | 9,0% → 8,5% | **+5,9%** |
| Churn mensal | 9,0% → 8,0% | **+12,5%** |
| Churn mensal | 9,0% → 7,0% | **+28,6%** |

> **Teto matemático do sistema atual, sem um real a mais de mídia:** +26% de receita de regime no
> cenário conservador (86% · 92% · 8,0%), +44% no agressivo (90% · 94% · 7,5%) `[E]`.

O baseline de churn move o prêmio, não a direção: se o churn real for 8%, −1 p.p. vale +14,3%; se
for 10%, vale +11,1%. **Em qualquer ponto da faixa declarada, um ponto de churn vale mais que dez
pontos de conversão de pagamento.** É a primeira frase que a V4 tem para dizer sobre onde está o
dinheiro, e ela não dependeu de nenhum acesso.

### 4.2 O achado: a base tem inércia de onze meses

Com churn de 9%, a constante de tempo da base é **1/c ≈ 11 meses** e a meia-vida do ajuste é **7,7
meses** `[E]`. Uma melhoria implantada hoje só entrega metade do seu valor em regime daqui a oito
meses. Simulando os três cenários de cascateamento da §6, mês a mês, com rampa de três meses por
injeção:

| Cenário | Run-rate de saída (mês 12) | Truput acumulado no ano | Run-rate no mês 18 | Regime |
|---|---|---|---|---|
| Conservador | **+5,0%** | +1,6% | +9,1% | +11,5% |
| **Base** | **+8,6%** | +3,1% | +15,1% | **+19,0%** |
| Ambicioso | **+11,8%** | +4,2% | +22,8% | +29,6% |

A distância entre as colunas **não é conservadorismo · é aritmética de recorrência**. E ela tem uma
consequência distributiva que decide como o projeto será julgado:

| Ciclo | Truput acumulado no ano contratual | Participação no ganho do ano | Run-rate de saída |
|---|---|---|---|
| Ciclo 1 (efeito a partir do M4) | +2,47% | **74,7%** | +5,9 p.p. |
| Ciclo 2 (M7) | +0,57% | 17,2% | +2,1 p.p. |
| Ciclo 3 (M10) | +0,27% | 8,1% | +1,9 p.p. |
| Ciclo 4 (M13) | 0% | **0%** | 0 no ano |

> **Medida por receita acumulada no ano, a metade final do contrato vale 8% do resultado e o quarto
> ciclo vale zero.** Medida por run-rate de saída, cada ciclo vale o que de fato construiu.

Essa é a razão técnica, não comercial, para a régua da §5.

### 4.3 Premissas do modelo, ditas antes que perguntem

O modelo é honesto sobre o que assume, e cada premissa tem uma pergunta correspondente já aberta:

1. As taxas `[D]` valem para o sistema todo, e não só para a fatia onde foram medidas.
2. O churn de 8–10% é sobre **clientes**; se for sobre **receita**, o efeito muda de tamanho,
   ambiguidade 4 da [leitura da jornada](../02-diagnostico/jornada-do-cliente-profissional.md).
3. A base está em equilíbrio, **e em Imóveis ela não está** (§6.1).
4. Entradas e ticket constantes: o modelo isola o efeito das travas, sem sazonalidade nem preço.
5. Sem interação entre alavancas. Na prática, quem publica tem menos chance de churnar, o que
   torna o modelo **conservador**, não otimista.

---

## 5. A régua proposta: três níveis, um número cada

| Nível | Métrica | Por que essa |
|---|---|---|
| **Meta do projeto** (12 meses) | **Truput de saída**: margem de contribuição do mês 12 sobre a do mês 0, na vertical governante | É a única régua em que os quatro ciclos aparecem. Mede o sistema construído, não o caixa da rampa |
| **Meta de ciclo** (90 dias) | Elevação do **indicador da restrição vigente**, em pontos percentuais, mais a contribuição-alvo em pontos de run-rate | Uma restrição por ciclo. O indicador só se conhece quando a trava é validada em ata |
| **Meta de comitê** (30 dias) | **Execução ≥ 80% do plano** | Já é o indicador de qualidade do Comitê 1 no [playbook](../00-playbook/03-ciclo-90-dias-e-comites.md). Protege o método de ser julgado por execução que não aconteceu |

**Métrica secundária, não meta:** truput incremental acumulado no ano. Ela existe para o FP&A
reconciliar com o P&L, e é declarada desde já como sendo de 3 a 6 vezes menor que o ganho de
regime, pela inércia, não pelo desempenho.

**Faixa proposta para a meta do projeto, com o que se sabe hoje `[E]`:** run-rate de saída de
**+8% a +12%** de truput na vertical governante, contra um teto matemático conservador de +26% em
regime. A faixa fecha em número único quando o material de metas chegar e a trava for validada.

---

## 6. O cascateamento nos quatro ciclos

Datas aproximadas a partir de 24/08/2026, o método avança por estado do sistema, não por
calendário ([cronograma](../04-execucao/cronograma-e-marcos.md)).

| Ciclo | Janela | Fase dominante | Natureza da meta | Alvo `[E]` |
|---|---|---|---|---|
| **1** | ago–nov/2026 | Identificar + Otimizar | **Sem novos recursos.** Recuperar vazamento na restrição validada | +3 a +6 p.p. de run-rate |
| **2** | nov/26–fev/2027 | Alinhar + Expandir | Primeira expansão com investimento, aprovada por causalidade | +2 a +3 p.p. |
| **3** | fev–mai/2027 | Nova restrição | Elevação da segunda trava, **gatilho técnico do bônus** | +2 a +3 p.p. |
| **4** | mai–ago/2027 | Consolidação | Estruturar o que sobrevive ao contrato. Efeito em regime cai no ano seguinte | +2 p.p., materializado em 2027/28 |

**Como ler o cascateamento:** ele é *decrescente em caixa no ano* e *crescente em valor de regime*.
Isso não é um defeito a corrigir, é o formato de qualquer intervenção estrutural em base
recorrente, e precisa estar dito em ata **antes** do primeiro ciclo, não depois do terceiro.

### 6.1 A meta zero, que vem antes de tudo em Imóveis

A OLX declarou net de receita negativo em Imóveis. Uma base que encolhe não persegue crescimento,
ela persegue **inflexão**. E o tamanho dessa meta é calculável no minuto em que o número do net
chegar `[E]`:

| Net de receita hoje | Melhoria combinada necessária só para o net voltar a zero |
|---|---|
| −3%/mês | +3,1% |
| −5%/mês | +5,3% |
| −8%/mês | +8,7% |
| −10%/mês | +11,1% |

Se o net de Imóveis estiver em −5%, **metade da meta do projeto se consome só em parar a
sangria**, e isso precisa aparecer no material, ou o ciclo 1 será lido como fracasso enquanto faz
exatamente a coisa certa. É a pergunta mais barata e mais cara de fazer na apresentação.

### 6.2 O que o cascateamento **não** define

A sequência de travas dos ciclos 2, 3 e 4. O método proíbe: a restrição seguinte se descobre no
Comitê 3 do ciclo anterior, contra o sistema já modificado. Qualquer material que anuncie hoje qual
será a trava do ciclo 3 está errado, por mais convincente que pareça.

---

## 7. Como isso resolve o Success Fee

[Pendência #2 do repositório](../PENDENCIAS.md), R$ 376.000 dependendo de um gatilho com três
leituras incompatíveis. A arquitetura acima entrega o aditivo quase pronto:

| Componente | Proposta | Por quê |
|---|---|---|
| **Gate técnico** | Expansão comprovada de **2 das 8 travas** ao longo dos 4 ciclos | É o padrão da SOW DR-E e é o que a V4 controla |
| **Gate de resultado** | Run-rate de truput de saída dentro da faixa acordada | Alinha com "margem acima de receita", já validado por Matheus Rodrigues em reunião |
| **Gate de execução** | ≥ 80% do plano executado por ciclo, medido em ata | Protege ambos os lados: sem execução, a restrição foi removida e a receita não subiu por decisão do cliente |

O argumento que sustenta isso na mesa é do próprio método, e o cliente já o aceitou em outra forma:
*a V4 não controla a execução, então o bônus premia a entrega técnica, identificar, validar e
elevar o gargalo* ([08-economics](../00-playbook/08-economics-e-entregaveis-dr-e.md#modelo-de-bônus-opção-b)).
Ancorar o bônus em faturamento bruto seria, além de injusto, incoerente com a North Star que a
própria OLX declarou.

---

## 8. O que falta para virar número absoluto

Quatro insumos. Nenhum depende de acesso novo, **todos já têm dono e compromisso**.

| # | Insumo | Fecha | DRI | Prazo |
|---|---|---|---|---|
| 1 | Metas 2026 por etapa do fluxo, receita por vertical, overview do ano | O denominador e a âncora da meta | Matheus Rodrigues + Iuna Scheffler | 09/09 (próximo passo #2) |
| 2 | P&L por vertical | Converte receita em truput | Matheus Rodrigues | 09/09 (#3) |
| 3 | Net de receita de Imóveis, mês a mês | Dimensiona a meta zero (§6.1) | Iuna Scheffler | 10/09 |
| 4 | Base ativa, ticket médio e churn extraídos do dashboard, de logo **e** de receita | Fecha a ambiguidade 4 e calibra o modelo | Leonardo Rosa, via links dos dashboards | 09/09 |

Com os quatro, esta página vira número em uma tarde. Sem eles, ela continua sendo a régua, e a
régua sozinha já é mais do que a OLX espera receber.

> Os prazos de 09 e 10/09 na tabela acima são os **compromissos assumidos no kick-off** e seguem de
> pé: o adiamento da apresentação para 24/09 é da V4 e não relaxa entrega de dado do cliente. O que
> ele muda é a consequência de o insumo faltar, antes o material iria incompleto para a mesa, agora
> há duas semanas para cobrar.

---

## 9. Como conduzir, em 10 minutos, na apresentação de 24/09

1. **Abrir pela régua, não pelo número.** *"Antes de trazer meta, precisamos combinar em que régua
   ela é medida, porque a régua natural do FP&A esconde metade do que este projeto constrói."*
2. **Mostrar 4.2.** A tabela de inércia sozinha justifica o run-rate de saída. É aritmética, não
   argumento comercial, e por isso não se discute, se confere.
3. **Mostrar 4.1.** Um ponto de churn vale mais que dez pontos de conversão de pagamento. É a
   primeira direção técnica que a V4 dá, e ela sai só de números que **eles** apresentaram.
4. **Fazer a pergunta da meta zero.** *"Qual é o net de receita de Imóveis, mês a mês?"* A resposta
   define se o ciclo 1 persegue crescimento ou inflexão.
5. **Fechar o compromisso de régua, não de valor.** O número entra no Comitê 1, com a trava
   validada. Registrar em ata: *a meta do projeto é run-rate de truput de saída na vertical
   governante; o valor se fixa no Comitê 1*.

> ⚠️ **O que não fazer:** apresentar a faixa de +8% a +12% como compromisso. Ela é o resultado do
> modelo sobre taxas declaradas e não apuradas. Apresentada como promessa, vira dívida; apresentada
> como consequência da matemática deles, vira autoridade.

---

## Estado

- Modelo e cenários em [`dados/outputs/meta-do-projeto.json`](../dados/outputs/meta-do-projeto.json)
- Insumo direto de: `03-estrategia/forecast-12-meses.md` (POP 27) e do aditivo do Success Fee
- **Nenhum valor absoluto é acordado até o Comitê 1**, com a trava governante validada em ata
