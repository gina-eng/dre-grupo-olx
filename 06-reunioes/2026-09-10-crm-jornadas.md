# CRM · parte 2: o mapa das jornadas e o que está no ar

| | |
|---|---|
| **Data** | 10/09/2026, 15h30 · remoto · 01:05:41 |
| **Origem** | Continuação da [sessão de 09/09](2026-09-09-crm-contexto-e-campana.md). Era a agenda presencial do dia, remarcada para online porque a V4 ainda não tinha acesso para apresentar diagnóstico |
| **Fase do método** | 1 · Identificar · **camada experiencial** do diagnóstico (i) CRM Marketing |
| **Serve a** | O diagnóstico (i), que fecha em **17/09**, e o Comitê 1 de **23/09** |
| **Entregável que ela alimenta** | [`02-diagnostico/auditoria-i-crm-marketing.md`](../02-diagnostico/auditoria-i-crm-marketing.md) |
| **Status** | ✅ Realizado · [transcrição completa](2026-09-10-crm-jornadas-transcricao.md) |

### Presentes

**OLX:** Michelle Morais (CRM, conduziu) · Evelyn Milare (CRM, apresentou o Miro) · Juliana Arndt
(CRM Imóveis) · Pietro Barbosa (CRM, em transição)
**V4:** Leonardo Rosa (consultor focal, quase sem voz na sessão) · Rafael Corazza (coordenador) ·
Matheus Gomes de Souza Netto (dados)
**C3C:** Augusto Vasconcelos presente, não apresenta.
**Ausentes** que estavam em 09/09: Eduardo Santos, Matheus Albuquerque, Guilherme Lippert.

> A ausência importa: os três assuntos que ficaram abertos na parte 1 (escopo das jornadas com a
> C3C, permanência da Blip e dono da construção de jornada) dependem justamente de Eduardo Santos e
> Matheus Albuquerque, e **nenhum deles avançou nesta sessão**.

## O estado da migração, declarado

| | |
|---|---|
| Autos | **100% dos clientes migrados** para o Campana |
| Imóveis | Migração **por ondas até o fim do ano**; a última leva foi a de field sales |
| Jornadas de ciclo de vida migradas e ligadas | **uma**: o onboarding de Imóveis |
| Em teste no dia seguinte (11/09) | a primeira das duas jornadas de onboarding de Autos, entregue pela C3C |

Fonte: 00:02:23 e 00:26:49. A data de ativação do onboarding de Imóveis aparece como *"dia 31"* na
transcrição e como *"31 de maio"* no resumo automático do Gemini: as duas não podem estar certas, e
a leitura por contexto aponta **31/08**. Vira [pendência 34](../PENDENCIAS.md).

## Por que parou: a causa que o cliente contou sem ser perguntado

> **Michelle Morais (00:19:24):** "a gente trabalhava com um formato antes aqui que a gente tinha
> uma pessoa especialista em Marketing Cloud interno nosso e era essa pessoa que cuidava das
> jornadas, da segmentação [...] **Essa figura interna não existe mais.**"
>
> "a gente teve um desfalque de área de março também, bem quando aconteceu essa migração [...] as
> duas pessoas que estavam antes, uma especialista e uma analista, saíram [...] Então Pietro, como
> estagiário, ficou segurando quase dois meses apagando incêndio."

Três fatos na mesma janela de março: a migração começou, o time perdeu duas pessoas e a única
pessoa com a habilidade técnica de construir jornada saiu. O que sobrou foi um estagiário
sustentando a **aquisição**, que é o que produz receita no mês. A camada de ciclo de vida, que
protege a receita do mês seguinte, é a que caiu.

Hoje quem constrói jornada é Augusto Vasconcelos, da C3C, uma consultoria externa e temporária.
Michelle reconhece a dependência e nomeia o caminho: *"idealmente o time deve começar a se
capacitar para que consiga fazer isso também de uma maneira mais autônoma"* (00:19:24).

## O mapa das jornadas, do Miro

Apresentado por Evelyn Milare com o quadro em tela (00:40:19 a 00:56:29). O Miro cobre B2B e B2C, com
divisão por real estate e autos. **Nenhuma das jornadas abaixo está no ar no ambiente novo**, exceto
onde marcado.

### Imóveis (real estate)

| # | Jornada | Recorte | Estado |
|---|---|---|---|
| 1 | Pós-cadastro | O limbo entre o cadastro na landing page e o contato do time comercial. Imobiliária e incorporadora | Desligada |
| 2 | **Onboarding** | Por tipo de plano contratado | ✅ **Ativa**, a única migrada |
| 3 | Educacional | Quem passou pelo onboarding, a partir do 3º mês | Desligada |
| 4 | Retenção preventiva | Cliente ativo no 3º mês | Desligada |
| 5 | Recuperação imediata | Inativo há até 30 dias, em duas trilhas: **churn** e **inadimplência** | Desligada |
| 6 | Recuperação total | Inatividade acima de 30 dias | Desligada |
| 7 | Máquina de inbound (lead score) | Cadastrado que nunca comprou: nutrição 1 → nutrição 2 → venda, por score. **Duas versões convivem**, a antiga ligada e a nova revisitada | Legado |
| 8 | Venda online (carrinho abandonado) | Três gatilhos: abandono em **web push real time**, vitrine por e-mail em real time, e checkout | Desligada |
| 9 | Recuperação manual | Os disparos de WhatsApp para inativos que o time sustenta à mão hoje | ✅ Manual |

> A jornada **7** é a mais complexa e a mais frágil. O lead score **não** usa o recurso nativo do
> Marketing Cloud, foi customizado no Salesforce, e Michelle é explícita: *"mesmo com a
> documentação, ela não foi suficiente [...] mesmo documentada ela não ficou tão óbvia assim para
> poder ser replicada"* (00:33:02). Ou seja, existe uma jornada desenhada que hoje ninguém sabe
> reconstruir.

### Autos (pós-migração 2025)

| # | Jornada | Recorte | Estado |
|---|---|---|---|
| 1 | Aquisição de planos profissionais | Duas réguas: abandono de carrinho de plano (autos e demais segmentos, exceto imóveis) e navegação na página de autos | Desligada |
| 2 | **Onboarding** | Um macro que abre em **cerca de seis** variações: contratação offline pelo time de vendas, online pelo cliente, upgrade de plano, genérico para os demais segmentos, e o do Autos 360. Só o **primeiro e-mail** muda por plano, o resto da régua é igual | Em migração, primeira em teste em 11/09 |
| 3 | Retenção preventiva e engajamento | Primeiros **quatro meses** do usuário | Desligada |
| 4 | Upsell | Duas: todos os clientes com plano ativo, e a específica de quem **esgotou o limite de anúncios** | Desligada |
| 5 | Recuperação | Quatro réguas por tempo de cancelamento: **até 30 dias** (com cupom, mais agressiva), **30–180 dias**, **180 dias a 1 ano**, e **acima de 1 ano**, esta 100% via push | Desligada |
| 6 | Autos 360 | Onboarding próprio, ativado por volta de **agosto/2025**, mais engajamento com dois touch points | Desligada |

> **Goods existe e não é foco.** Autopeças e outros segmentos compram plano profissional e recebem
> um onboarding **genérico**: *"Eu não tenho onboarding de trator. Eu não tenho um onboarding para
> quem compra moto"* (00:28:01). Coerente com o escopo fechado no kick-off, em que Goods ficou de
> fora.

### Canal por vertical, e por que eles diferem

| Vertical | Ambiente logado do profissional | Canais em uso |
|---|---|---|
| **Imóveis** | **Canal Pro**, web e app apartados dos portais | E-mail, quase exclusivamente. O app do Canal Pro é *"pouquíssimo explorado"* e **não tem canal de push** |
| **Autos** | Aba **My Plan**, dentro do próprio site e app da OLX | E-mail **e push**, porque o profissional vive no mesmo app do consumidor |

> **Michelle Morais (00:52:27):** "a gente gasta o WhatsApp quando tem receita. Então vou ganhar
> dinheiro, vou vender o plano, vou fazer destaque, upgrade, upsell [...] Agora vou engajar, vou
> divulgar produto, a gente não usa o WhatsApp, salvo algumas exceções."

As exceções nomeadas são **CredAluga** (garantia locatícia, parceria com compromisso contratual
anual de produção) e **Autos 360** (o hub do lojista, gratuito nos planos premium, integra o anúncio
a mais de 50 portais). Os dois têm meta de engajamento e baixa adesão só por e-mail.

## Dado: o que a base perde antes de sair

A higienização virou tema porque Rafael Corazza perguntou o tamanho da perda (00:08:14).

| O que se corrige | Detalhe |
|---|---|
| **CEP ausente** | **mais de 50%** da base, por falta de preenchimento `[E]` |
| Nome | Caixa alta e baixa, duplicados, `undefined`, nome sobre nome. Percentual não lembrado na sala |
| Campos trocados | Documento gravado em campo de nome |
| Telefone | Duplicados e sem padrão de máscara |
| Data | Formatos distintos, o que quebra segmentação |

> **Michelle Morais (00:10:30):** "a gente fez uma sanitização, mas só foi uma sanitização com a
> cabeça muito de billing, ou seja, eu tenho que limpar a base para não ter nenhum blocker na hora
> de fazer a cobrança [...] na perspectiva de marketing e de mensageria, a gente tinha que fazer a
> nossa."

**O CEP é e não é bloqueio, ao mesmo tempo.** Michelle diz que ele *"virou um campo mandatório no
processo de qualificação"* do bot; Juliana Arndt corrige em 00:09:23: *"dá pra gente disparar sem
essa informação, sem o CEP, só que aí ele vai entrar na qualificação e vai precisar preencher. Só
demora um pouco mais o fluxo"*. A régua de qualificação, aliás, encolheu: *"Ela tinha nove
perguntas, aí virou sete, virou quatro"* (00:10:30).

**O que já melhorou:** Evelyn Milare automatizou a higienização dentro do Marketing Cloud, gerando
uma base tratada sem tocar no arquivo-fonte. Feito para Autos, previsto para Imóveis na semana de
15/09 (00:11:44).

## Gargalos que o próprio time listou (00:21:42)

1. **Blocklist e exclusões** ainda manuais.
2. **Motor de rotatividade sustentável** inexistente: o disparo deveria seguir o capacity de
   atendimento, e hoje é calibrado à mão, no olho, por média diária. Está no escopo da C3C.
3. **Volume e faseamento** definidos manualmente.
4. **Tracking de campanha**: a integração Marketing Cloud ↔ Blip tem limitação técnica, falta o
   campo que carrega a tag de campanha, e há quebras de público que não se consegue fazer. Em
   discovery com o time de CX.

## E-mail: abandonado na aquisição, e a conta muda em outubro

> **Michelle Morais (00:14:04):** "o e-mail hoje tá esquecido, a gente não faz mais nenhum tipo de
> disparo hoje de e-mail para aquisição, mas temos sim esse ti[me] de voltar com e-mail, até porque
> ele é o canal mais barato."
>
> "a gente tem uma regra nova que a meta tá implantando até outubro, que deve encarecer a forma de
> cobrança que os disparos de WhatsApp vão passar a ter."

Um canal de custo marginal quase zero foi desligado e 100% da aquisição ficou no canal que vai
encarecer em outubro. Vira [pendência 35](../PENDENCIAS.md).

## Testes A/B: quase inexistentes, por confissão

> **Michelle Morais (00:59:14):** "a gente hoje, até de novo pelos processos muito manuais aqui, faz
> pouquíssimos testes A/B [...] faz um pouquinho quando a gente fala na parte de aquisição, mas nos
> demais assim não faz, gente, sendo super transparente com vocês."

E a automação tem um custo cultural que o time antecipa: o processo manual tem *"muita liberdade
poética"* para mudar copy e horário no meio do caminho, e automatizar tira isso (00:12:59).

## Documentação: o Miro tem o desenho, o Confluence vai ter a regra

> **Michelle Morais (00:25:29):** "a gente tem um processo de documentação muito pobre, assim, a OLX
> como um todo não é boa em documentar [...] a maior dureza desse processo é porque você não tinha
> segmentação e as regras completamente documentadas para ele replicar."

A migração está sendo feita por **engenharia reversa** da jornada existente. Duas decisões saíram
daí, e são as únicas decisões da sessão:

| # | Decisão |
|---|---|
| 1 | **Documentação padrão em duas peças:** o fluxo visual no **Miro** e a especificação textual (nomes, segmentação, motivo, passos manuais, tags e UTMs) no **Confluence**, escrita pela C3C |
| 2 | **Ordem de migração por impacto de negócio e churn:** onboarding primeiro, carrinho abandonado em seguida, depois inativos e cancelados, upsell, e por fim pós-cadastro e nutrição |

O Miro atual não registra **tempo**: Rafael Corazza perguntou se dá para ler os intervalos no
desenho e Evelyn respondeu que só na documentação textual (00:41:27). O ritmo declarado da migração
é de **cerca de duas semanas por tema** (00:37:50), e Michelle diz que gostaria que fosse mais
rápido.

## Onde ler resultado: Looker, não Salesforce

> **Michelle Morais (01:02:16):** "essa parte de acesso aos nossos dashboards, a gente faz o nosso
> acompanhamento, a gente faz pouco pela Salesforce [...] a gente faz muito mais aqui pelo Looker,
> que é onde a gente consome do nosso BigQuery."

O painel indicado tem MQL, SQL, canal, vertical e receita, e não é só de CRM, é de marketing. Existe
também um dashboard de **CRM offline** que estava com bug e foi corrigido na véspera. Os dois links
foram prometidos e ainda não chegaram ([pendência 32](../PENDENCIAS.md)).

Do lado da integração com o V4MOS, Matheus Gomes de Souza Netto nomeou o que falta: a conexão com o
Salesforce para trazer os números de venda. As contas de anúncio estão resolvidas, com um ajuste
interno pendente no Google, do lado da V4 (01:01:33).

## Números declarados nesta sessão

| Onde | Número | Fonte |
|---|---|---|
| Migração de clientes, Autos | **100%** concluída | 00:02:23 |
| Migração de clientes, Imóveis | por ondas, **até o fim do ano** | 00:02:23 |
| Perda de base por CEP ausente | **mais de 50%** `[E]` | 00:08:14 |
| Régua de qualificação do bot | **9 → 7 → 4** perguntas | 00:10:30 |
| Validação da base de Autos | prevista em 15 dias, levou **mais de dois meses** `[E]` | 00:16:35 |
| Desfalque do time | **2 saídas** em março (uma especialista, uma analista) | 00:19:24 |
| Tempo de Pietro Barbosa sozinho | **quase dois meses** `[E]` | 00:19:24 |
| Ritmo de migração de jornada | **cerca de duas semanas por tema** `[E]` | 00:37:50 |
| Onboarding do Autos 360 no ar desde | **agosto/2025** `[E]` | 00:56:29 |
| Variações da jornada de onboarding de Autos | **cerca de seis** `[E]` | 00:48:05 |
| Réguas de recuperação de Autos | **4** faixas de tempo | 00:53:45 |
| Integração do Autos 360 | anúncio replicado em **mais de 50 portais** | 00:35:22 |

## Próximos passos registrados na sessão

| # | Ação | DRI declarado |
|---|---|---|
| 1 | Enviar as transcrições das duas sessões | Michelle Morais |
| 2 | Compartilhar o acesso ao Miro com o mapeamento das jornadas | Michelle Morais |
| 3 | Montar a lista de links, logins e acessos a dashboards e plataformas internas | Michelle Morais |
| 4 | Compartilhar o link do dashboard de resultados no Looker e o de CRM offline | Michelle Morais |
| 5 | Finalizar a primeira jornada de onboarding de Autos para teste | Augusto Vasconcelos (C3C) |
| 6 | Enviar opções de data e hora da próxima agenda no grupo | Leonardo Rosa |
| 7 | Verificar se a V4 tem acesso ao **MyApps**, pré-requisito para o Sales Cloud | Leonardo Rosa |

> Item 7: Juliana Arndt esclareceu que a liberação do Sales Cloud depende de o e-mail `@olxbr` já
> estar habilitado no MyApps (01:03:21). Os e-mails existem, Michelle fez a liberação. O que falta é
> a conferência, que é parte da [pendência 18](../PENDENCIAS.md).

## Para onde esta sessão manda material

| Destino | O quê |
|---|---|
| [`02-diagnostico/auditoria-i-crm-marketing.md`](../02-diagnostico/auditoria-i-crm-marketing.md) | O mapa das jornadas, os gargalos e a leitura por trava |
| [`02-diagnostico/checklist-dados-e-acessos.md`](../02-diagnostico/checklist-dados-e-acessos.md) | Bloco B, itens B2, B3 e B4 |
| [`PENDENCIAS.md`](../PENDENCIAS.md) | Itens 30, 32, 33, 34 e 35 |
| Matriz de Expansão (Comitê 2) | Retomada do e-mail como primeiro toque de aquisição; push no app do Canal Pro, hoje inexistente |
