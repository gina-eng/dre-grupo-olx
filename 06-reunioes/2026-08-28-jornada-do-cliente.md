# Jornada do cliente — sessão de mapeamento do fluxo de receita

| | |
|---|---|
| **Data** | 28/08/2026 (sexta-feira) |
| **Origem** | Combinada no próprio kick-off: *"marcar na sexta pra gente passar pela jornada, porque aí você vê alguma coisa"* ([transcrição](2026-08-24-kickoff-transcricao.md), 02:02:10). É o próximo passo **#8** da ata — *touch points com o time de operação para validar a jornada*, com Carolina Dallolio |
| **Fase do método** | 1 — Identificar · **camada experiencial** do POP Fluxo de Receita (`.claude/skills/dre-fluxo-receita/`) |
| **Serve a** | Comitê 1 de identificação da restrição, **10/09** — faltam 12 dias |
| **Entregável que ela alimenta** | `dados/outputs/dre-fluxo-receita.json` + `02-diagnostico/fluxo-de-receita.md` |
| **Status** | 🔜 Hoje |

## O que esta reunião é — e o que ela não é

**É** a camada experiencial do diagnóstico: o fluxo de receita contado por quem opera, para ser
cruzado depois com o dado do sistema. O POP é explícito em que o diagnóstico final é a soma das
duas leituras, e Dener disse isso na sala: *"o diagnóstico final é basicamente a soma dessa visão
junto com vocês com o diagnóstico isento"*.

**Não é** comitê. Não decide restrição, não decide meta, não decide Success Fee — isso é 10/09, com
Matriz do GP aprovada. E **não é** rodada de opinião: a pergunta *"onde vocês acham que está a
trava?"* já foi feita e respondida no kick-off (Retenção 3 × Qualificação 2, §2.7 da
[conferência](2026-08-24-kickoff-o-que-a-transcricao-fecha.md)). Refazê-la queima a sessão e reabre
item fechado.

O que falta não é percepção. É **denominador**: volume, taxa de passagem e tempo por etapa.

## Levar — uma coisa só

A **árvore de produção de receita** do portal (`/receita`, v2 de 26/08): 39 nós, **21 confirmados,
16 hipótese, 2 abertos**, cada um apontando a pergunta do bloco 3B que o fecha.

Levar a árvore inverte a mecânica da reunião. Sem ela, você sai com a jornada *narrada* e transcreve
depois. Com ela, você chega com o mapa construído a partir das falas **deles** e pede correção — e
corrigir um mapa é mais rápido, mais preciso e menos custoso para o cliente do que descrever um do
zero. Os 16 nós em hipótese e os 2 abertos **são a pauta**: cada um é uma pergunta já formulada.

> ⚠️ Antes de mandar o link: reler as notas dos nós com olhos de cliente. A árvore nasceu como
> leitura interna da V4 e o `/kickoff` é material **interno** — esse não se compartilha.
> Senha e escopo de cada página em [portal/PUBLICACAO.md](../portal/PUBLICACAO.md).

Mandar antes, assíncrono, é o combinado: decisão #7 da ata — *material antes, sem apresentação
formal, reunião só para discutir*. Usar o encontro para apresentar slide contraria o que a própria
V4 pediu.

## Roteiro — 90 min

| Bloco | Tempo | O que acontece |
|---|---|---|
| **Enquadrar** | 5 min | Dizer em uma frase o que sai da sala: *o fluxo com número por etapa, ou o nome de quem deve cada número e quando*. Lembrar que 10/09 depende disto |
| **Eles apresentam** | 25 min | Sem interromper. Só uma intervenção permitida: quando uma etapa passar sem número, marcar — não perguntar ainda |
| **Refletir o mapa** | 15 min | Abrir a árvore e corrigir **ao vivo**, com eles vendo. O status de cada nó circula aberto → hipótese → confirmado no clique |
| **Denominadores** | 30 min | A tabela vazia, etapa por etapa. É aqui que a reunião dá ou não dá resultado |
| **Reconciliar e fechar** | 15 min | Multiplicar o funil e comparar com a receita declarada. Nomear DRI e prazo do que faltou. Confirmar 10/09 |

Se a agenda for de 60 min, corte o bloco de reflexão do mapa para 5 min e proteja os
**denominadores** — é o único bloco que não tem substituto assíncrono.

## A tabela que precisa sair preenchida

Por **unidade** (Autos e Imóveis separados — ver armadilha 2), e por frente de aquisição:

| Etapa (nome interno deles) | Volume/mês | Taxa de entrada | Tempo médio | Fonte | `[E]`? |
|---|---|---|---|---|---|
| | | | | | |

Regra dura do POP: **etapa sem volume, taxa e tempo não está mapeada** — está narrada. E o que for
declarado de cabeça entra marcado `[E]` / `"estimado": true`, nunca como dado.

## Perguntas — as que compram mais mapa por minuto

Ordem deliberada: começa pelo denominador da base, termina na margem.

1. **Quem é o CNPJ pagante?** (3B-0 — seis nós em hipótese) Rede ou loja? Corretor autônomo,
   incorporadora, concessionária, revenda, vendedor PF: quais são cliente e quais são usuário?
   Sem isso, "cliente" é ambíguo e **toda** taxa de churn, base e NRR está medida sobre um
   denominador incerto.
2. **Existe linha de contrato de mídia separada da de listing?** (3B-1, nó **aberto**) Leonardo
   Costa disse que lá fora visibilidade é 30–50% da receita em real estate e aqui a receita está
   lastreada em inserção por anúncio ativo. Onde essa linha entra no P&L?
3. **Quando a receita é reconhecida, e o contrato existe?** (3B-11, nó **aberto** + caminho do
   dinheiro) Pré-pago não renovado não gera evento de cancelamento — então o churn de Imóveis é
   *medido* ou *inferido*?
4. **Qual a tabela vigente por porte e praça, e o desconto médio?** (3B-9) É a ponte entre a trava
   de **Decisão** e a de **Retenção**: o aumento de preço de 2026 é a mudança estrutural que
   explica a série.
5. **Onde está a margem, por linha?** (3B-5) A meta do projeto é margem, não receita — Matheus foi
   literal: *"sou mais disposto a sacrificar a receita e melhorar a margem do que o contrário"*.
   Sem margem por linha não há truput, e sem truput o Comitê 1 não tem o que maximizar.
6. **Os motivos de cancelamento são registrados?** Perguntado no kick-off, **resposta não
   capturada**. Custa 30 segundos e destrava o diagnóstico da trava de Retenção.
7. **Quem é o DRI da aquisição?** Dener perguntou *"quem é a pessoa de aquisição mesmo?"* e não
   houve resposta clara. Se hoje também não houver, isso deixa de ser lacuna e vira **achado** —
   vai para a CRT como causa candidata, não para PENDENCIAS.

## Armadilhas específicas desta reunião

1. **O ótimo local.** Vão chegar 20 oportunidades boas — lead similar como produto, campanha
   genérica contra a Meta, calculadora de financiamento, PPL por grupo. Nenhuma é a pergunta de
   hoje. Não brigue com elas e não as persiga: anote em lista à parte, com o destino já dito em voz
   alta — **Matriz de Expansão, Comitê 2**. Sua função hoje é achar a estação mais lenta, não
   colecionar melhorias.
2. **O funil único.** Autos e Imóveis têm economias diferentes, a aquisição tem três frentes
   (leads B2B, prospecção comercial, canal online) e o Triple Bundle põe um contrato sobre três
   portais com origem opaca para o anunciante. Se apresentarem "a jornada", no singular, peça a
   separação **antes** de somar. Passo 1 do POP: não existe funil único, e somar economias
   diferentes produz mapa errado com aparência de mapa certo.
3. **A jornada desenhada ≠ a jornada real.** A própria Florence disse que a jornada só ficou
   desenhada depois de um workshop interno (UDE #14). O que vier hoje é, em boa parte, o fluxo
   **como projetado**. A divergência entre ele e os números por etapa é justamente onde mora o
   diagnóstico — trate cada lacuna numérica como sinal, não como falha de preparo deles.
4. **"Falta dado" não encerra assunto.** É pecado capital do TOC e Dener já o nomeou na sala. Sempre
   vai faltar. Lacuna vira linha em [PENDENCIAS.md](../PENDENCIAS.md) com dono e prazo — nunca
   motivo para adiar o mapa.

## Critérios de aceite

- [ ] Fluxo separado por unidade (Autos, Imóveis), com o vocabulário interno deles
- [ ] Cada etapa com volume, taxa de passagem e tempo médio — ou com DRI e prazo nomeados
- [ ] Reconciliação feita: receita derivada do funil vs. declarada, divergência < 5% ou explicada
- [ ] Todo número de cabeça marcado `[E]`
- [ ] Nós da árvore promovidos de hipótese a confirmado, e os que caíram, corrigidos
- [ ] Lista de oportunidades parqueada com destino declarado (Comitê 2)
- [ ] Data de 10/09 reconfirmada com quem estava na sala

---

## Ata

*(preencher após o encontro)*

### Presentes

### Fluxo mapeado

A OLX apresentou a jornada **como conceito**, em 6 etapas, com uma taxa declarada por etapa.
Descrição e leitura em
[02-diagnostico/jornada-do-cliente-profissional.md](../02-diagnostico/jornada-do-cliente-profissional.md);
original em [assets/originais/A-visao-de-negocio-e-fluxo-de-receita/](../assets/originais/A-visao-de-negocio-e-fluxo-de-receita/).
Falta a transcrição da sessão para atribuir fala, compromisso e DRI.

### Números obtidos

| Etapa | Volume | Taxa | Tempo | Fonte | `[E]` |
|---|---|---|---|---|---|

### Nós da árvore alterados

| Nó | De | Para | O que mudou |
|---|---|---|---|

### Lacunas → PENDENCIAS

| # | O que falta | DRI | Prazo |
|---|---|---|---|

### Oportunidades parqueadas (Comitê 2)

### Próximos passos
