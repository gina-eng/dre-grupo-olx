# Sprint dos diagnósticos · 10 a 18/09

Replanejado em **11/09/2026**: os nove passam a fechar **todos até sexta, 18/09**, a pedido do
cliente. O lote completo de acessos foi recebido em 10/09 e disparou a contagem; o kick-off combinou
**até 15 dias corridos** a partir dali, e a entrega acontece em **9**.

> Este documento substitui o `sprint-diagnosticos-10-a-24-09.md`, que fechava os nove em 24/09.
> Ele **não substitui** o [cronograma do Ciclo 1](cronograma-e-marcos.md), detalha, em dias, a
> janela em que a granularidade semanal não serve.

---

## O tamanho real da janela

| | |
|---|---|
| Recebimento do lote completo | quinta, **10/09/2026** |
| Início dos diagnósticos | quinta, **10/09/2026**, no mesmo dia |
| Fechamento dos nove | sexta, **18/09/2026** |
| Prazo declarado no kick-off | até **15 dias corridos** |
| **Prazo efetivo** | **9 dias corridos** |
| **Dias úteis dentro deles** | **7**: 10, 11, 14, 15, 16, 17 e 18 |
| Consolidação causal | **14 a 18/09**, em paralelo aos diagnósticos |
| CRT, Nuvem de Conflito e Matriz | **16 a 18/09**, sobre as UDEs das entrevistas |
| Matriz aprovada, gate de bloqueio duro | sexta, **18/09/2026** |

> **Vocabulário.** A **Matriz** e a **revisão de qualidade** são a mesma sessão, não duas etapas: o
> gate em que alguém que não participou da análise testa o material antes do comitê
> ([regra 4](../CLAUDE.md), skill `dre-matriz-gp`). "Matriz" é o nome do método e fica nos documentos
> internos. **No portal a etapa aparece como "revisão de qualidade"**, porque "Matriz aprovada" não
> diz nada a quem lê de fora.
| **Evento único: apresentação + Comitê 1** | quarta, **23/09/2026**, confirmado em 11/09 |

**Fechar em 18 devolve ao projeto os seis dias que o atraso de acesso tinha consumido**, e faz a
entrega acontecer seis dias antes do teto contratado. O custo não é de prazo, é de concentração:

| | Plano de 10/09 | Agora |
|---|---|---|
| Dias corridos | 15 | **9** |
| Dias úteis para os nove | 11 | **7** |
| Pico de diagnósticos abertos | 6 | **8** |
| Dias com 5 frentes conjuntas | 1 (17/09) | **3 seguidos** (15, 16 e 17) |
| Consolidação causal | depois dos nove | **em paralelo a eles** |
| Matriz aprovada | 02/10 | **18/09** |

**A análise deixou de ser uma etapa depois do diagnóstico e passou a ser simultânea a ele**, montada
à medida que os achados aparecem. Tudo o que depende da V4 fecha na mesma sexta, 18/09, duas semanas
antes do previsto.

> 🔴 **O que o paralelismo cobra.** Pontuar trava com diagnóstico ainda aberto produz nota
> provisória, e nota provisória que sobe sem evidência nova é exatamente como se nomeia a restrição
> errada. A disciplina que protege isso é a [regra 6](../CLAUDE.md): **nota acima de 3 exige
> evidência formal**, nunca percepção do time. Na prática: uma trava só passa de 3 quando o
> diagnóstico que a sustenta estiver fechado, não antes.

---

## As duas mudanças de 10/09

**1. O lote chegou completo.** Salesforce Marketing Cloud, as duas contas de Meta, Business Suite e
LinkedIn, Search Console, Mouseflow, Unbounce, as contas de GTM que faltavam, o CRM comercial e as
gravações de call com consentimento. Os quatro diagnósticos que estavam totalmente parados abriram,
e os quatro que rodavam em camada parcial ganharam a camada onde mora a causa, não o sintoma.

**2. A apresentação dos diagnósticos deixou de ser evento separado.** Ela passa a acontecer dentro
do Comitê 1, numa sessão só, a pedido do cliente. Duas consequências, e elas puxam em direções
opostas:

- **A favor:** o decisor se desloca uma vez em vez de duas, e desaparece a semana morta entre
  apresentar o diagnóstico e decidir sobre ele. É mais próximo do que um comitê deveria ser.
- **Contra:** todo o material precisa estar pronto **antes** do evento, Matriz inclusive. No desenho
  anterior, a Árvore da Realidade Atual e a Nuvem de Conflito podiam ser construídas *depois* de
  apresentar, aproveitando as reações da sala. Agora não podem: por isso o marco duro desta janela é
  a **Matriz de 18/09**, e não a data do comitê.

---

## O que ordena a janela

Com os nove habilitados ao mesmo tempo, o critério de habilitação perdeu a função. O que ordena
volta a ser a lógica original do método, a investigação **de baixo para cima** no fluxo de ganho
([Regra de Goldratt](../00-playbook/01-fundamentos-dr-ote.md#lógica-de-investigação-de-baixo-para-cima)),
com um segundo filtro que agora é o binding:

> **Agenda dos dois lados.** O gargalo desta janela deixou de ser acesso. Passou a ser calendário:
> boa parte do diagnóstico é feita **em conjunto** com o time da OLX, em entrevista, leitura a
> quatro mãos e validação de achado, e isso precisa caber na agenda de quem faz e de quem participa.

Por isso a grade abaixo separa os nove em **dois grupos pelo tanto de trabalho conjunto que exigem**,
e não pela ordem de contrato.

---

## Os nove na janela

### Grupo 1 · a V4 roda sobre material já entregue: abre em 10/09

| # | Diagnóstico | Janela | Onde o time da OLX entra |
|---|---|---|---|
| **vii** | Rastreamento (GA4/GTM) | 10–15 set | Em nada mais. Os exports das 3 contas que faltavam chegaram; a análise já está 80% escrita |
| **ii** | CRO/SEO · domínios B2B | 10–16 set | Em nada mais. Search Console concedido, camada pública já rodada |
| **viii** | Páginas de captura | 10–18 set | **O volume absoluto do teste A/B**, que é entrega de dado e não acesso |

### Grupo 2 · feito em conjunto com o time da OLX: entra escalonado

| # | Diagnóstico | Janela | Onde o time da OLX entra |
|---|---|---|---|
| **vi** | Mídia paga (Google e Meta) | 11–18 set | Finalidade de cada conta. **Depende de ingestão no V4MOS**, ver risco 3 |
| **i** | CRM Marketing (Salesforce MC) | 11–17 set | **Reuniões já realizadas, 09 e 10/09.** É essa dianteira que permite fechar em 17 |
| **ix** | Pré-vendas e qualificação | **14–17 set** | **Entrevistas nos blocos de 16 e 17 + as 10 a 15 gravações de call**, concentradas em 4 dias |
| **iv** | Criativos e mensagens | 15–18 set | Racional de campanha por trás do acervo, que entra em 15 |
| **v** | Redes e conteúdo orgânico | 15–18 set | Pouca entrevista; Business Suite e LinkedIn já concedidos |
| **iii** | GEO · buscas generativas | 16–18 set | Em nada. Roda de fora, sobre linha de base zero |

> **(i) CRM saiu na frente.** As reuniões sobre o assunto aconteceram em **09 e 10/09**, antes do
> lote de acessos, e o diagnóstico abre em 11/09 já sobre o que elas levantaram. O time de CRM não
> precisa entrar nos blocos de entrevista de 16 e 17.

> **(ix) Pré-vendas foi comprimido para quatro dias**, de 14 a 17/09, e deixou de ser o último a
> fechar. Ver o risco 2.

### Carga em paralelo: a regra que este plano quebra

O método limita a **três diagnósticos abertos por vez**, e a regra existe justamente para proteger a
agenda do cliente. Nesta janela ela não é cumprida:

| Pico no período | 10/09 | 11/09 | 14/09 | **15–16/09** | 17/09 | 18/09 |
|---|---|---|---|---|---|---|
| Abertos ao mesmo tempo | 3 | 5 | 6 | **8** | 7 | 5 |
| **Feitos em conjunto** | 1 | 3 | 4 | **5** | **5** | 3 |

O pico chega a **oito diagnósticos abertos** em 15 e 16/09, contra o teto de três do método, e há
**cinco frentes conjuntas em três dias seguidos**: 15, 16 e 17. Isso é consequência direta de fechar
em 9 dias e está registrado aqui como decisão consciente, não como descuido de planejamento.

**A mitigação é de concentração, não de redução:** as entrevistas de (ix) e (iv) são agendadas em
**dois blocos fechados**, quarta 16 e quinta 17, em vez de espalhadas pela semana. As de (i) já
aconteceram em 09 e 10/09, por fora dos blocos. Duas manhãs reservadas rendem mais, para quem
conduz e para quem participa, do que cinco frentes cutucando todo dia durante uma semana.

---

## O plano, dia a dia

| Dia | V4 executa | O que precisa vir do Grupo OLX |
|---|---|---|
| **qua 09 · qui 10/09** | **Reuniões sobre CRM**, antes do lote de acessos. Insumo de (i) | Time de CRM, já realizado |
| **qui 10/09** | **Conferência do lote, abrindo cada ferramenta**, não lendo o e-mail de concessão. Abrem (vii), (ii) e (viii) | 🔴 **Dono da revisão de qualidade definido**, sem o qual não há revisão em 18/09 |
| **sex 11/09** | Abrem (vi) pelas contas certas e **(i) sobre o que as reuniões levantaram**. Ingestão das contas de mídia no V4MOS. **Reporte escrito semanal** | Escalar no mesmo dia o que tiver vindo em nível insuficiente |
| **seg 14/09** | **Abre (ix)**, que roda inteiro em 4 dias. **Abre a consolidação causal**, pontuando o que já fechou. (vii) em fechamento | - |
| **ter 15/09** | **Fecha (vii). Abrem (iv) e (v).** Pico de 8 abertos. Trava de Cegueira pontuada | **Acervo de criativos entregue**, senão (iv) não fecha em 18 |
| **qua 16/09** | **Bloco de entrevistas 1.** Fecha (ii). Abre (iii). **Abre a CRT** sobre as primeiras UDEs | Time de pré-vendas disponível |
| **qui 17/09** | **Bloco de entrevistas 2. Fecham (ix) e (i).** CRT em construção; Nuvem de Conflito esboçada | Time de conteúdo e de mídia disponível |
| **sex 18/09** | **Fecham (viii), (vi), (iv), (v) e (iii).** As 8 travas pontuadas, trava governante nomeada, injeção fechada e **material aprovado na revisão de qualidade**. Acaba o que depende da V4 | 🔴 **Revisor independente**, ainda sem dono. Validação dos achados no mesmo dia em que aparecem |
| **seg 21/09** | **Prévia do material com Florence Scappini**, a pedido dela. É o melhor teste disponível da leitura: ela lidera a frente de receita e é a fonte de boa parte das UDEs que o diagnóstico usa | Florence presente |
| **ter 22/09** | Único dia para absorver o que a prévia levantar, e ensaio. Ver a ressalva do gate abaixo | Confirmar presença dos decisores no comitê |
| **qua 23/09** | **Apresentação dos diagnósticos + Comitê 1**, na mesma sessão. Sai com a restrição nomeada em ata e o plano de 30 dias | **Decisor presente.** DRI assumido para cada ação do plano |

---

## Os cinco riscos desta janela

**1. O acesso pode ter chegado concedido e não utilizável.** É o risco mais provável, porque já
aconteceu duas vezes: o GA4 veio em nível Leitor, que sustenta diagnóstico de sintoma mas não abre
as telas de Administração onde mora a causa; e o portfólio Meta apareceu sem ativo conectado. A
conferência de 10/09 é feita **abrindo cada ferramenta**, e o que estiver em nível insuficiente é
escalado **no mesmo dia**, não na semana seguinte, porque não há semana seguinte sobrando.

**2. 🔴 (ix) Pré-vendas tinha três semanas de janela por um motivo, e agora tem quatro dias.** A
janela original era longa porque gravação de call envolve consentimento e LGPD, e porque é o
diagnóstico que sozinho pontua **três travas**: Qualificação, Compromisso e Decisão. O trâmite de
consentimento se resolveu junto com o lote, o que tira o obstáculo jurídico, mas não encurta o
trabalho: são de 10 a 15 gravações para ouvir e duas rodadas de entrevista, tudo entre 14 e 17/09.

É a compressão mais agressiva do plano, e ela tem um efeito previsível: se a camada experiencial não
fechar, entra como limitação declarada e as três travas ficam pontuadas só pela camada analítica, o
que sustenta uma nota, mas [não sustenta nota acima de 3](../CLAUDE.md). Três das oito travas
limitadas a 3 estreita bastante o que a consolidação causal consegue afirmar.

**Mitigação:** priorizar a escuta das gravações sobre a transcrição integral, e levar para os blocos
de 16 e 17 as perguntas que as gravações não responderem, em vez de usar os blocos para cobrir
terreno já coberto.

**3. 🔴 (vi) Mídia paga é o único cujo prazo não depende só de esforço.** Fechar em 18/09 exige que
as duas contas de Meta estejam **ingeridas no V4MOS**, e ingestão é processo técnico com latência
própria: não acelera com prioridade. Em 08/09 o Meta ainda devolvia zero nos seis endpoints, contra
23 campanhas e R$ 2,59 mi já ingeridos do Google.

Se a ingestão não fechar dentro da semana, **(vi) fecha só com Google** e a camada de Meta entra como
limitação declarada. Isso afeta as travas de Exposição, Atenção e Qualificação, e é material: as
duas contas de Meta são justamente as do B2B em escopo, `VR ZAP+` e `OLX Autos B2B`.

**Ação:** verificar a ingestão na segunda 14/09, não na quinta. Se não estiver rodando, escalar no
mesmo dia e decidir conscientemente se (vi) fecha parcial ou se é o único a estourar 18/09.

**4. A revisão de qualidade não tem dono.** O método exige que o material de comitê seja validado
por **alguém que não participou da análise**, é a única proteção contra material fraco chegar ao
Board, numa conta que compra exatamente rigor metodológico. Com a apresentação absorvida pelo
comitê, **as duas revisões viraram uma só**, e com o paralelismo ela foi de 01/10 para **18/09**: é
o único gate antes de um evento que apresenta e decide na mesma sessão, e agora acontece no mesmo
dia em que o material termina de ser escrito. Definir o revisor até **15/09**, para que ele
acompanhe a consolidação em vez de receber tudo pronto na sexta
([pendência 8](../PENDENCIAS.md)).

**5. 🔴 A prévia de 21/09 acontece depois do gate, e o gate cobre a versão de 18.** A Florence
Scappini pediu ver o material antes do comitê, e isso é bom: ela lidera a frente de receita e é a
fonte de boa parte dos efeitos indesejados que o diagnóstico usa, então é quem percebe primeiro se
a leitura estiver errada. O problema é de sequência. O material é aprovado na revisão de qualidade
em **18/09**; a prévia é em **21**; o comitê em **23**. Sobra **terça 22** para absorver o que ela
levantar.

**A regra a operar:** ajuste de clareza, ênfase ou ordem na terça não mexe no que foi aprovado.
**Mudança estrutural mexe**, e aí o que vai ao comitê não é a versão que passou pelo gate, o que a
[regra 4](../CLAUDE.md) não cobre. Não há dia para reaprovar entre 22 e 23. Na prática, a prévia
serve para confirmar e afiar; se ela derrubar uma leitura central, o caminho honesto é levar isso
ao comitê como achado, não reescrever o material na véspera.

Vale registrar que isso devolve peso à revisão de qualidade de 18/09, que segue sem revisor.

O que essa data **resolve** é maior do que o que ela aperta: entre o Comitê 1 e o Comitê 2 de 03/11
há **26 dias úteis**, então o plano de 30 dias tem tempo de ser executado antes de ser avaliado.
A [pendência 25](../PENDENCIAS.md) fechou por causa disso.

> ⚠️ **O que este plano não resolve.** O **bloco A**, Visão de Negócio e Fluxo de Receita, não é
> acesso a ferramenta, é entrega de dado. **A1, a série de receita, chegou em 28/08**; A2, o funil
> com volumes e taxas por etapa, e A3, ticket, ciclo e CAC, seguem sem data. Sem eles não há
> mapeamento do fluxo de receita e não há matemática de forecast, e isso vale igual com os nove
> diagnósticos fechados. É a pendência mais silenciosa do projeto, porque só aparece como bloqueio
> na hora de montar o forecast.
