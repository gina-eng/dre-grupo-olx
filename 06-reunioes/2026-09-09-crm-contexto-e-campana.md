# CRM · parte 1: o contexto, o Campana e o que parou em março

| | |
|---|---|
| **Data** | 09/09/2026, 15h01 · remoto · 01:02:42 |
| **Origem** | Agenda "CRM e V4 consultoria · apresentação CRM", convocada por Michelle Morais. É o capítulo de CRM da varredura contratada, e Michelle o apresenta assim ao time interno: *"eles fazem uma varredura por todas as áreas e processos para entender aonde existe um potencial de receita que está travado"* (00:06:10) |
| **Fase do método** | 1 · Identificar · **camada experiencial** do diagnóstico (i) CRM Marketing |
| **Serve a** | O diagnóstico (i), que fecha em **17/09** ([sprint](../04-execucao/sprint-diagnosticos-10-a-18-09.md)), e o Comitê 1 do evento único de **23/09** |
| **Entregável que ela alimenta** | [`02-diagnostico/auditoria-i-crm-marketing.md`](../02-diagnostico/auditoria-i-crm-marketing.md) |
| **Status** | ✅ Realizado · [transcrição completa](2026-09-09-crm-contexto-e-campana-transcricao.md) · **não houve gravação**, só transcrição |

## O que esta reunião é, e o que ela não é

**É** contexto, e a própria condutora avisou disso na abertura:

> **Michelle Morais (00:03:48):** "não vai ser talvez uma agenda de CRM tão trivial, porque é uma
> agenda que vai contextualizar o momento em que a gente está, muito mais do que o que a gente tem
> em termos de jornada somente."

**Não é** a camada analítica do diagnóstico (i): nenhum relatório de performance, nenhuma base, nenhum
acesso à ferramenta. Tudo que está aqui é **declarado em reunião** (regra 1 do repositório).

E não é a agenda que estava no cronograma: era para ser a sessão presencial de 10/09 com
apresentação de diagnóstico da V4, e Leonardo Rosa a reabriu em 00:58:12 porque os acessos ainda não
tinham chegado. Virou uma segunda sessão online, [10/09](2026-09-10-crm-jornadas.md).

### Presentes

**OLX:** Michelle Morais (CRM, conduziu) · Eduardo Santos (Core Solutions, dono de Sales e Service
Cloud) · Mirella Mendonça (marketing) · Matheus Albuquerque (especialista Salesforce, Core
Solutions) · Evelyn Milare (CRM, visão cross entre Autos e Imóveis) · Pietro Barbosa (CRM, em
transição de área) · Juliana Arndt (CRM Imóveis)
**V4:** Leonardo Rosa (consultor focal) · Rafael Corazza (coordenador) · Guilherme Lippert
(cofundador, produtos de tech) · Matheus Gomes de Souza Netto (engenharia de dados)
**C3C:** Augusto Vasconcelos e Gabriel Lopes constam do convite e **não falam** nesta sessão.

> O time de CRM B2B tem **três pessoas** e está em recomposição: Pietro Barbosa sai, Evelyn Milare
> assume Autos com olhar cross e Juliana Arndt fica em Imóveis (00:13:57 e 00:15:05).

## A operação declarada, em quatro frases

1. **CRM é canal de aquisição antes de ser canal de relacionamento.** É um dos maiores fornecedores
   de MQL para o DBM, o time de inside sales que vende os planos menores (00:16:19).
2. **A aquisição roda em WhatsApp**, *"99%, para não falar 100"* (00:16:19). E-mail existe nas
   jornadas de ciclo de vida, não na aquisição.
3. **O esforço foi deliberadamente desequilibrado para a aquisição.** O upsell voltou para o time
   farmer e o CRM foi para onde há gap comercial: *"CRM tá com a missão maior aqui, aonde tem um gap
   maior comercial, que é conseguir leads para aquisição"* (00:16:19).
4. **O processo é manual de ponta a ponta**, mesmo existindo Marketing Cloud: extração de base,
   cruzamento, limpeza, quebra por volume diário e upload na Blip (00:17:50 e 00:47:06).

## A arquitetura do Campana, por Matheus Albuquerque (00:36:40 e 00:38:56)

| Camada | O que faz |
|---|---|
| Sistemas internos | Conta, cobrança, notificação, geração de contrato |
| **Proxy** | Decide se o registro vai para o ambiente legado ou para o Campana |
| Salesforce | **Três orgs unificadas em uma**: OLX, Zap e VivaReal. Padroniza campo, objeto e processo (`contract` e `service contract` faziam a mesma coisa no legado) |
| Marketing Cloud | Uma BU por origem: OLX, Zap e **a BU do Campana**, que recebe o dado já unificado |

Fluxo de objetos de uma venda (00:40:22): lead → conta e contato → oportunidade → cotação →
produtos → **pedido** → notificação, cobrança e ativação → contrato → jornada de onboarding.

**O ponto que mais importa para o diagnóstico** está em 00:38:56, e é o próprio arquiteto quem diz:

> **Matheus Albuquerque:** "quando a gente fala de dado para campana, processo Salesforce, a gente
> tá falando de um dado **qualificado para que a gente consiga fazer uma venda** e não
> necessariamente um dado que vai estar super ultra limpo para que a gente consiga fazer um disparo
> totalmente formatado."

E o que Eduardo Santos acrescenta em 00:28:50 fecha o desenho:

> **Eduardo Santos:** "nós não temos uma CDP única hoje, então hoje tá tudo pulverizado os dados.
> Então eu tenho dificuldade de saber onde estão cada um dos dados e como que eu construo essas
> jornadas."

## O achado da sessão: cinco meses sem jornada de ciclo de vida

A migração para o Campana desligou o CRM de ciclo de vida para **todo cliente novo**, e ninguém
religou:

| Vertical | Migração começou | Efeito |
|---|---|---|
| **Autos** | fim de **março/2026** | Cliente novo cadastrado no Campana não recebe jornada nenhuma desde abril |
| **Imóveis** | **julho/2026** | Mesmo efeito, a partir de julho |

> **Michelle Morais (00:26:09):** "os clientes começaram a serem cadastrados os novos clientes no
> ambiente novo, no Campana novo. A gente já parou de disparar para ele as novas jornadas, por
> exemplo, de autos. Elas ficaram no ambiente velho e não ligaram ainda. [...] a gente tá desde
> março, desde abril até agora, sem conversar dentro de um ciclo de vida com esse cliente de autos."

O que continua vivo: o **transacional** (confirmação de compra) e o **billing** (cobrança), que
rodam por fora do time de CRM. O que parou é a camada promocional e de relacionamento.
Quem já estava numa jornada no legado segue nela até o fim; o legado não foi desligado, ele é o
ambiente **atual do B2C** (parte 2, 00:16:35).

**Uma jornada voltou:** o onboarding de Imóveis, migrado e ligado pouco antes desta sessão
(00:23:38). A data tem duas versões, ver [pendência 34](../PENDENCIAS.md).

## O desencontro, e ele aconteceu na sala

Este é o registro mais valioso da sessão, porque não é opinião da V4: é o cliente descobrindo, ao
vivo, que duas áreas tinham entendimentos incompatíveis sobre quem constrói jornada.

> **Eduardo Santos (00:28:50):** "eu entendo que o que existia de jornada do legado a gente
> reconstruiu dentro de campana, porque a gente deu o OK, inclusive para autos, né?"
> **Michelle Morais:** "Ainda não, Edu. A gente tá começando agora. A gente migrou a DEX, só a data
> extension, só os dados para conseguir fazer os disparos de aquisição."
>
> **Mirella Mendonça (00:29:57):** "do ponto de vista de dependência de engenharia aqui, isso foi em
> abril, porque montar a comunicação dentro do Marketing Cloud é coisa de marketing, depende da
> gente."
> **Michelle Morais:** "Não, a gente precisa do conhecimento técnico. [...] a gente sempre teve uma
> pessoa técnica que faz isso pra gente."
>
> **Eduardo Santos (00:30:26):** "Esse era o meu entendimento também. Por isso que para mim tava
> tudo certo. [...] talvez a gente esteja fazendo um monte de coisa, mas não é o que vai resolver o
> nosso problema."
> **Mirella Mendonça (00:34:24):** "isso me parece ser algo bem simples, tá gente?"

**O que isso é, em método:** não é falha de pessoa (regra 5 do repositório). É uma **política
implícita**: a construção de jornada no Marketing Cloud nunca teve dono declarado, foi sempre
executada por um especialista técnico, e quando esse especialista saiu em março
([parte 2](2026-09-10-crm-jornadas.md), 00:19:24) a atividade não caiu para ninguém. Cinco meses de
silêncio com o cliente novo e nenhum alarme, porque nenhum indicador da empresa observa esse
silêncio. O material vai para a CRT como causa candidata, não para uma lista de culpados.

## Blip: a decisão que não está tomada

O disparo de WhatsApp sai pela **Blip**, que não tem integração com o Marketing Cloud. A base é
exportada, tratada e subida à mão (00:47:06).

| Quem | O que disse |
|---|---|
| **Eduardo Santos (00:52:42)** | "teoricamente a BP vai morrer, né?" · "a gente tem um down time muito grande com eles" · "não funciona" · "eles já nem tão participando do bid de disparo" |
| **Mirella Mendonça (00:52:42)** | "pelo que eu entendi hoje na reunião, isso não está pacificado de que Blip vai morrer" |
| **Eduardo Santos (00:53:48)** | Migração prevista para o **Q1**, e a discussão com o comercial "ainda precisa acontecer". O atendimento já vai 100% para o Salesforce |
| **Michelle Morais (00:56:14)** | "até que a gente tenha isso formalizado, a gente segue com o plano": há agenda na semana com Paloma e Etienne para integrar Blip e Marketing Cloud |
| **Eduardo Santos (00:57:16)** | "a gente não deveria ter essa premissa de integração com Blip, eu deveria ter a premissa de ter o disparo" · "a Blip deveria ser utilizada como um broker" |

Duas pessoas da mesma empresa, na mesma sala, com leituras opostas sobre a permanência da
ferramenta de que depende **100% da aquisição de CRM**. Vira [pendência 31](../PENDENCIAS.md).

## Riscos que o próprio cliente levantou

**Mirella Mendonça (00:48:35)**, sobre as etapas de tratamento, exclusão manual e disparo por fora:

> "o item quatro, cinco, o sete e o oito, digamos assim, eles são super críticos porque envolve
> LGPD, envolve inúmeros outros riscos aqui pra gente."

A V4 registra porque afeta o desenho da injeção, não porque o achado seja nosso:
[pendência 33](../PENDENCIAS.md).

## Números declarados nesta sessão

Todos **declarados**, nenhum apurado contra sistema. Marcados `[E]` onde são estimativa de quem
falou.

| Onde | Número | Fonte |
|---|---|---|
| Aquisição, upsell e one shot | **99% a 100%** em WhatsApp `[E]` | 00:16:19 |
| Migração de Autos | começou no **fim de março/2026** | 00:26:09 |
| Migração de Imóveis | começou em **julho/2026** | 00:26:09 |
| Data Extension de Autos | concluída por volta de **maio/2026** `[E]` | 00:31:09, confirmado por Pietro Barbosa |
| Orgs de Salesforce unificadas | **3** (OLX, Zap, VivaReal) em **1** | 00:37:47 |
| Tempo de casa de Evelyn Milare | "três semanas" `[E]` | 00:13:57 · **corrigido na parte 2**: três semanas na área, um ano de OLX |

## Decisões

O Gemini classificou a sessão como **"Precisa de mais conversa"**, e está certo: nenhuma decisão
estrutural foi fechada. A única coisa acordada foi de agenda, ajustar o cronograma e manter uma
segunda sessão online de cerca de uma hora para fechar o capítulo de CRM (00:58:12).

Três assuntos ficaram explicitamente em aberto, e é isso que a ata precisa registrar: **o escopo das
jornadas com a C3C**, **a permanência da Blip** e **quem constrói jornada no Marketing Cloud**.

## Próximos passos registrados na sessão

| # | Ação | DRI declarado |
|---|---|---|
| 1 | Reunião à parte para detalhar o escopo das jornadas e as pendências da C3C | Eduardo Santos + Mirella Mendonça |
| 2 | Fórum técnico sobre a arquitetura do Campana e os fluxos do Sales Cloud, para a V4 | Matheus Albuquerque |
| 3 | Enviar o plano de mídia para validação | Mirella Mendonça |
| 4 | Limpeza da base de Imóveis para consumo de marketing, até a semana seguinte | Evelyn Milare |
| 5 | Reunir Paloma e Etienne sobre automação do disparo de WhatsApp, com Matheus Albuquerque na sala | Eduardo Santos |
| 6 | Enviar a Michelle a relação de acessos pendentes que impacta o cronograma | Leonardo Rosa |
| 7 | Sessão online para fechar o CRM (aconteceu em 10/09) | O grupo |

## Para onde esta sessão manda material

| Destino | O quê |
|---|---|
| [`02-diagnostico/auditoria-i-crm-marketing.md`](../02-diagnostico/auditoria-i-crm-marketing.md) | Todos os achados, com a leitura por trava |
| [`02-diagnostico/checklist-dados-e-acessos.md`](../02-diagnostico/checklist-dados-e-acessos.md) | Bloco B: B2 sai de ⚪, e a nota das quatro ferramentas ganha resposta parcial |
| [`PENDENCIAS.md`](../PENDENCIAS.md) | Itens 30, 31, 32, 33 e 34 |
| CRT (a montar) | O desencontro sobre a dona da jornada, como causa candidata em formato de política |
