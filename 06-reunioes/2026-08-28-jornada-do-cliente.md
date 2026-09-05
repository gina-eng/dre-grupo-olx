# Jornada do cliente: sessão de mapeamento do fluxo de receita

| | |
|---|---|
| **Data** | 28/08/2026 (sexta-feira) |
| **Origem** | Combinada no próprio kick-off: *"marcar na sexta pra gente passar pela jornada, porque aí você vê alguma coisa"* ([transcrição](2026-08-24-kickoff-transcricao.md), 02:02:10). É o próximo passo **#8** da ata, *touch points com o time de operação para validar a jornada*, com Carolina Dallolio |
| **Fase do método** | 1 · Identificar · **camada experiencial** do POP Fluxo de Receita (`.claude/skills/dre-fluxo-receita/`) |
| **Serve a** | Comitê 1 de identificação da restrição, **10/09**, faltam 12 dias |
| **Entregável que ela alimenta** | `dados/outputs/dre-fluxo-receita.json` + `02-diagnostico/fluxo-de-receita.md` |
| **Status** | ✅ Realizado · 01:05:30 · [transcrição completa](2026-08-28-jornada-do-cliente-transcricao.md) |

## O que esta reunião é: e o que ela não é

**É** a camada experiencial do diagnóstico: o fluxo de receita contado por quem opera, para ser
cruzado depois com o dado do sistema. O POP é explícito em que o diagnóstico final é a soma das
duas leituras, e Dener disse isso na sala: *"o diagnóstico final é basicamente a soma dessa visão
junto com vocês com o diagnóstico isento"*.

**Não é** comitê. Não decide restrição, não decide meta, não decide Success Fee, isso é 10/09, com
Matriz do GP aprovada. E **não é** rodada de opinião: a pergunta *"onde vocês acham que está a
trava?"* já foi feita e respondida no kick-off (Retenção 3 × Qualificação 2, §2.7 da
[conferência](2026-08-24-kickoff-o-que-a-transcricao-fecha.md)). Refazê-la queima a sessão e reabre
item fechado.

O que falta não é percepção. É **denominador**: volume, taxa de passagem e tempo por etapa.

## Levar: uma coisa só

A **árvore de produção de receita** do portal (`/receita`, v2 de 26/08): 39 nós, **21 confirmados,
16 hipótese, 2 abertos**, cada um apontando a pergunta do bloco 3B que o fecha.

Levar a árvore inverte a mecânica da reunião. Sem ela, você sai com a jornada *narrada* e transcreve
depois. Com ela, você chega com o mapa construído a partir das falas **deles** e pede correção, e
corrigir um mapa é mais rápido, mais preciso e menos custoso para o cliente do que descrever um do
zero. Os 16 nós em hipótese e os 2 abertos **são a pauta**: cada um é uma pergunta já formulada.

> ⚠️ Antes de mandar o link: reler as notas dos nós com olhos de cliente. A árvore nasceu como
> leitura interna da V4 e o `/kickoff` é material **interno**, esse não se compartilha.
> Senha e escopo de cada página em [portal/PUBLICACAO.md](../portal/PUBLICACAO.md).

Mandar antes, assíncrono, é o combinado: decisão #7 da ata, *material antes, sem apresentação
formal, reunião só para discutir*. Usar o encontro para apresentar slide contraria o que a própria
V4 pediu.

## Roteiro · 90 min

| Bloco | Tempo | O que acontece |
|---|---|---|
| **Enquadrar** | 5 min | Dizer em uma frase o que sai da sala: *o fluxo com número por etapa, ou o nome de quem deve cada número e quando*. Lembrar que 10/09 depende disto |
| **Eles apresentam** | 25 min | Sem interromper. Só uma intervenção permitida: quando uma etapa passar sem número, marcar, não perguntar ainda |
| **Refletir o mapa** | 15 min | Abrir a árvore e corrigir **ao vivo**, com eles vendo. O status de cada nó circula aberto → hipótese → confirmado no clique |
| **Denominadores** | 30 min | A tabela vazia, etapa por etapa. É aqui que a reunião dá ou não dá resultado |
| **Reconciliar e fechar** | 15 min | Multiplicar o funil e comparar com a receita declarada. Nomear DRI e prazo do que faltou. Confirmar 10/09 |

Se a agenda for de 60 min, corte o bloco de reflexão do mapa para 5 min e proteja os
**denominadores**: é o único bloco que não tem substituto assíncrono.

## A tabela que precisa sair preenchida

Por **unidade** (Autos e Imóveis separados, ver armadilha 2), e por frente de aquisição:

| Etapa (nome interno deles) | Volume/mês | Taxa de entrada | Tempo médio | Fonte | `[E]`? |
|---|---|---|---|---|---|
| | | | | | |

Regra dura do POP: **etapa sem volume, taxa e tempo não está mapeada**, está narrada. E o que for
declarado de cabeça entra marcado `[E]` / `"estimado": true`, nunca como dado.

## Perguntas: as que compram mais mapa por minuto

Ordem deliberada: começa pelo denominador da base, termina na margem.

1. **Quem é o CNPJ pagante?** (3B-0, seis nós em hipótese) Rede ou loja? Corretor autônomo,
   incorporadora, concessionária, revenda, vendedor PF: quais são cliente e quais são usuário?
   Sem isso, "cliente" é ambíguo e **toda** taxa de churn, base e NRR está medida sobre um
   denominador incerto.
2. **Existe linha de contrato de mídia separada da de listing?** (3B-1, nó **aberto**) Leonardo
   Costa disse que lá fora visibilidade é 30–50% da receita em real estate e aqui a receita está
   lastreada em inserção por anúncio ativo. Onde essa linha entra no P&L?
3. **Quando a receita é reconhecida, e o contrato existe?** (3B-11, nó **aberto** + caminho do
   dinheiro) Pré-pago não renovado não gera evento de cancelamento, então o churn de Imóveis é
   *medido* ou *inferido*?
4. **Qual a tabela vigente por porte e praça, e o desconto médio?** (3B-9) É a ponte entre a trava
   de **Decisão** e a de **Retenção**: o aumento de preço de 2026 é a mudança estrutural que
   explica a série.
5. **Onde está a margem, por linha?** (3B-5) A meta do projeto é margem, não receita, Matheus foi
   literal: *"sou mais disposto a sacrificar a receita e melhorar a margem do que o contrário"*.
   Sem margem por linha não há truput, e sem truput o Comitê 1 não tem o que maximizar.
6. **Os motivos de cancelamento são registrados?** Perguntado no kick-off, **resposta não
   capturada**. Custa 30 segundos e destrava o diagnóstico da trava de Retenção.
7. **Quem é o DRI da aquisição?** Dener perguntou *"quem é a pessoa de aquisição mesmo?"* e não
   houve resposta clara. Se hoje também não houver, isso deixa de ser lacuna e vira **achado**,
   vai para a CRT como causa candidata, não para PENDENCIAS.

## Armadilhas específicas desta reunião

1. **O ótimo local.** Vão chegar 20 oportunidades boas, lead similar como produto, campanha
   genérica contra a Meta, calculadora de financiamento, PPL por grupo. Nenhuma é a pergunta de
   hoje. Não brigue com elas e não as persiga: anote em lista à parte, com o destino já dito em voz
   alta, **Matriz de Expansão, Comitê 2**. Sua função hoje é achar a estação mais lenta, não
   colecionar melhorias.
2. **O funil único.** Autos e Imóveis têm economias diferentes, a aquisição tem três frentes
   (leads B2B, prospecção comercial, canal online) e o Triple Bundle põe um contrato sobre três
   portais com origem opaca para o anunciante. Se apresentarem "a jornada", no singular, peça a
   separação **antes** de somar. Passo 1 do POP: não existe funil único, e somar economias
   diferentes produz mapa errado com aparência de mapa certo.
3. **A jornada desenhada ≠ a jornada real.** A própria Florence disse que a jornada só ficou
   desenhada depois de um workshop interno (UDE #14). O que vier hoje é, em boa parte, o fluxo
   **como projetado**. A divergência entre ele e os números por etapa é justamente onde mora o
   diagnóstico, trate cada lacuna numérica como sinal, não como falha de preparo deles.
4. **"Falta dado" não encerra assunto.** É pecado capital do TOC e Dener já o nomeou na sala. Sempre
   vai faltar. Lacuna vira linha em [PENDENCIAS.md](../PENDENCIAS.md) com dono e prazo, nunca
   motivo para adiar o mapa.

## Critérios de aceite

- [ ] Fluxo separado por unidade (Autos, Imóveis), com o vocabulário interno deles
- [ ] Cada etapa com volume, taxa de passagem e tempo médio, ou com DRI e prazo nomeados
- [ ] Reconciliação feita: receita derivada do funil vs. declarada, divergência < 5% ou explicada
- [ ] Todo número de cabeça marcado `[E]`
- [ ] Nós da árvore promovidos de hipótese a confirmado, e os que caíram, corrigidos
- [ ] Lista de oportunidades parqueada com destino declarado (Comitê 2)
- [ ] Data de 10/09 reconfirmada com quem estava na sala

---

## Ata

Fonte: [transcrição integral](2026-08-28-jornada-do-cliente-transcricao.md), 01:05:30, sessão
remota com nome em cada fala.

### Presentes

**Grupo OLX:** Carolina Dallolio (operações comerciais, conduziu a sessão) · Michelle Morais (CRM,
apresentou a jornada granular de canais) · Lu Machim (dashboards) · Leonardo Costa (produtos,
monetização RE) · Iuna Scheffler (planejamento) · Matheus Rodrigues (FP&A) · Mirella Mendonça
**V4:** Leonardo Rosa (consultor focal) · Gustavo Figueiredo (COO) · Rafael Corazza (coordenador)

A sessão foi enquadrada pela própria Carolina como **educacional**, não como entrega de
diagnóstico: *"vamos fazer uma sessão rápida, educacional, só para poupar a dor de cabeça de
vocês"* (00:00:06). E como **conceito**, não funil: *"não estou trazendo nenhuma visão de funil,
uma visão de jornada mesmo do nosso cliente profissional"* (00:04:20).

### Fluxo mapeado

Dois materiais, que se encaixam:

1. **Jornada do cliente profissional**, 6 etapas com uma taxa cada, leitura em
   [02-diagnostico/jornada-do-cliente-profissional.md](../02-diagnostico/jornada-do-cliente-profissional.md),
   original em [assets/originais/A-visao-de-negocio-e-fluxo-de-receita/](../assets/originais/A-visao-de-negocio-e-fluxo-de-receita/).
2. **FLUXOS: Autos & Imóveis**, o diagrama granular de canais que Michelle apresentou, em três
   versões de detalhe crescente. **A aritmética fecha nó a nó, em 97%**, ver
   [lacunas-do-fluxo-de-receita.md](../02-diagnostico/lacunas-do-fluxo-de-receita.md) §1.

E a fonte do dado apareceu: **os dashboards existem**. Lu Machim apresentou o funil B2B com MQL,
SQL e vendas, taxa de qualificação e de conversão, por vertical, por canal, por time comercial e
por período, com processamento diário às 3h, mais o dashboard do canal online com sessões,
vitrines, checkouts e vendas. Isso muda o trabalho da V4 de **coletar** para **extrair**.

### Números obtidos

Todos **declarados** em reunião, ainda não apurados contra o sistema.

| Onde | Número | Fonte na transcrição |
|---|---|---|
| Entrada | 50% da base chega por prospecção comercial ativa | 00:05:42 |
| Contratação | canal online = 25% da receita de Autos, 10% de Imóveis; o resto é do time comercial | 00:12:41 |
| Pagamento | 80% dos que contratam **e geram cobrança** pagam a primeira fatura | 00:15:30 |
| Publicação | 12% saem no 1º mês sem publicar, até **20%** no online, **8–10%** no assistido | 00:15:30 |
| Leads | 89% dos anúncios de Imóveis não recebem nenhum lead | 00:18:09 |
| Recorrência | churn de 8–10%, concentrado no 1º mês; baixa performance é o principal motivo | 00:22:16 |
| Meios de pagamento | metade da base em boleto, ~40% cartão, resto Pix; sem diferenciação de preço | 00:21:16 |
| Atrasos | esquecimento responde por 20% dos **atrasos** (não do churn) | 00:22:16 |
| Canais | CRM 29% · Direto 36% · Pago 16% · Orgânico 5% · Outros 11% | slide FLUXOS |
| App | Autos 60–70% usam app; Imóveis 20–30% | 00:38:26 |
| Entrega | proxy de performance na OLX: 3 leads em 7 dias; Imóveis não tem número | 00:53:50 |

### Definições fechadas

- **MQL**: nome, e-mail, telefone, em alguns canais documento.
- **SQL**: elegibilidade comercial, em Imóveis, ser imobiliária ou corretor com CNPJ do setor.
- **Churn**: interrupção de pagamento. Quem paga e não usa **não** é churn, é inativo gerando receita.
- **POS**: point of sale online, login, vitrine, checkout.
- **Modelo de anúncio**: Autos por **inserção** (o anúncio é consumido); Imóveis por **slot** (reaproveitável).

### Achado da sessão

**O canal Direto, maior fatia do mapa com 36%, é em parte artefato de mensuração.** O próprio slide
anota: *"teste de campanha paga para WhatsApp: entra tudo como Direto"* e *"perde atribuição: entra
tudo como Direto"*. Logo, **Pago (16%) está subestimado** e CAC por canal não existe hoje. É Trava
de Cegueira com evidência formal produzida pelo cliente.

### Nós da árvore alterados

*(a aplicar em `portal/_src/receita.html`, ver a lista de atualizações pendentes)*

### Lacunas → PENDENCIAS

| # | O que falta | DRI | Prazo |
|---|---|---|---|
| 1 | Links dos dashboards de funil B2B e de canal online | Leonardo Rosa | - |
| 2 | Investimento de mídia por canal (fora do dashboard, controle à parte) | Mirella Mendonça | - |
| 3 | Dimensionar quanto do "Direto" é campanha paga sem atribuição | a definir | - |
| 4 | Arquivo original da jornada (está no Drive) e do slide de FLUXOS | Carolina Dallolio | - |

Prazos não foram acordados na sessão; **não inventar**. Fechar no grupo antes de virar linha de
[PENDENCIAS.md](../PENDENCIAS.md).

### Oportunidades parqueadas (Comitê 2)

- **Reempacotamento de produtos em RE**: destaque saturado sendo a demanda nº 1 de upgrade; estudo
  de torná-lo produto escasso, fora do plano padrão. Lá fora, 50% da receita de marketplace vem de
  destaque (00:59:26).
- **Meio de pagamento como alavanca**: cupom para Pix, cliente pequeno só cartão ou Pix, migração
  compulsória de crônico em atraso, financiadora para ticket acima de R$ 50 mil (01:00:35).
- **Canibalização privado × profissional**: teste de reduzir gratuidade de Autos de 4 para 2
  anúncios/ano (00:52:15).
- **Upgrade self-service**, hoje inexistente (00:41:15).
- **Volta ao Paper Lead no mercado primário**, com foco no Sudeste, decisão tomada na OLX no mesmo
  dia (00:03:02). Conversa direto com as decisões 5 e 6 do kick-off.

### Próximos passos

| # | Ação | DRI |
|---|---|---|
| 1 | Compartilhar o Miro com e-mails de boas-vindas e materiais educacionais | Leonardo Costa |
| 2 | Compartilhar os materiais do GT de onboarding | Michelle Morais |
| 3 | Conectar o responsável de produto de Autos (Bruno) ao grupo | Iuna Scheffler |
| 4 | Verificar as réguas de comunicação de Autos | Leonardo Costa |
| 5 | Formalizar por e-mail os acessos por plataforma | Michelle Morais |
| 6 | Compartilhar no grupo os links dos dashboards de domínio | Leonardo Rosa |
| 7 | Revisar o material de reempacotamento e receitas não recorrentes | Leonardo Rosa + Rafael Corazza |

### Modo de operação acordado

Leonardo Rosa assumiu o papel de **consultor focal**: a OLX aciona direto no grupo, e a V4 traduz
para a metodologia. Dúvida substancial vira agenda pontual com o especialista da área, em vez de
travar o diagnóstico (00:56:15 e 00:58:27).
