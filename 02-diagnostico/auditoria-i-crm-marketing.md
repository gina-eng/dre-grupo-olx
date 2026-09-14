# Auditoria (i) · CRM Marketing (Salesforce Marketing Cloud)

> **Como ler este documento.** Ele abre com a **camada experiencial**, que fechou antes da
> analítica porque as duas sessões de CRM aconteceram em 09 e 10/09, antes do lote de acessos.
>
> | | |
> |---|---|
> | Camada experiencial | ✅ **Fechada** · duas sessões, 02:08:23 de registro, todo o time de CRM B2B na sala |
> | Camada analítica | 🟠 **Aberta** · sem base, sem relatório de performance, sem console. Ver [o que falta](#o-que-falta-para-fechar-i) |
> | Achados | **16**, numerados em sequência |
> | Leitura por trava | [§ Para onde os achados vão](#para-onde-os-achados-vão) · **nenhuma trava é pontuada aqui** |
> | Fechamento previsto | **17/09/2026** ([sprint](../04-execucao/sprint-diagnosticos-10-a-18-09.md)) |
>
> ⚠️ **Tudo aqui é declarado, nada é apurado.** Nenhum número deste documento foi verificado contra
> sistema. Regra 1 do repositório: o que veio de fala é evidência de *como a operação se descreve*,
> e vira dado quando a camada analítica confirmar.

## Fonte

| Sessão | Data | Duração | Registro |
|---|---|---|---|
| Parte 1 · contexto, Campana e o que parou em março | 09/09/2026 | 01:02:42 | [ata](../06-reunioes/2026-09-09-crm-contexto-e-campana.md) · [transcrição](../06-reunioes/2026-09-09-crm-contexto-e-campana-transcricao.md) |
| Parte 2 · o mapa das jornadas e o que está no ar | 10/09/2026 | 01:05:41 | [ata](../06-reunioes/2026-09-10-crm-jornadas.md) · [transcrição](../06-reunioes/2026-09-10-crm-jornadas-transcricao.md) |

Presentes, nas duas somadas: todo o time de CRM B2B (Michelle Morais, Evelyn Milare, Juliana Arndt,
Pietro Barbosa), o dono técnico do Sales e Service Cloud (Eduardo Santos), o arquiteto do Campana
(Matheus Albuquerque), marketing (Mirella Mendonça) e a consultoria que executa a migração (C3C).

**Cruzamentos usados:** a [auditoria (vii) de rastreamento](auditoria-vii-rastreamento.md), que
mapeou a stack de CRM pelo GTM antes de qualquer conversa, e a
[jornada do cliente de 28/08](jornada-do-cliente-profissional.md), que deu os denominadores de churn
e de mix de canal.

---

## 🔴 1. O CRM de ciclo de vida está desligado para todo cliente novo desde abril

É o achado central, e ele não é inferência: é a descrição que a própria gestora da área fez, duas
vezes, em duas sessões.

| Vertical | Migração começou | Jornada de ciclo de vida para cliente novo |
|---|---|---|
| **Autos** | fim de março/2026 | **Desligada desde abril** |
| **Imóveis** | julho/2026 | **Desligada desde julho**, exceto onboarding, religado no fim de agosto |

> **Michelle Morais** (09/09, 00:26:09): "a gente tá desde março, desde abril até agora, sem
> conversar dentro de um ciclo de vida com esse cliente de autos."

**O que continua rodando:** o transacional (confirmação de compra) e o billing, que são de outros
times. E a aquisição, que é manual e nunca parou. **O que parou** é tudo que acontece depois da
venda: onboarding, educacional, retenção preventiva, upsell e recuperação.

**Por que isso é grave aqui e não seria em outra conta:** a jornada declarada em 28/08 põe o churn
em **8% a 10%** `[D]` e o descreve **concentrado no primeiro mês**, e registra que parte de quem sai
nesse primeiro mês vai embora **sem sequer publicar**. Os dois números estão com o denominador em
disputa, churn de logo ou de receita ([pendência 22](../PENDENCIAS.md)) e os 12% sobre que base
([pendência 19](../PENDENCIAS.md)): o que **não** depende do denominador é onde o vazamento fica,
no primeiro mês. O onboarding é exatamente a peça que age nessa janela, e ela ficou fora do ar por
cinco meses em Autos, na coorte inteira de clientes novos.

**O que falta:** o tamanho da coorte e o churn dela contra o da coorte anterior. Sem isso, o achado
é estrutural e não é dimensionado. [Pendência 30](../PENDENCIAS.md).

## 🔴 2. A construção de jornada nunca teve dono, e o dono de fato saiu em março

Três fatos na mesma janela:

1. A migração para o Campana começou no fim de março.
2. Duas das três pessoas da área saíram em março, *"uma especialista e uma analista"* (10/09, 00:19:24).
3. A construção técnica de jornada no Marketing Cloud era feita por essa especialista, e
   *"essa figura interna não existe mais"*.

O que sobrou foi um estagiário sustentando a aquisição por quase dois meses. E a atividade órfã não
caiu para ninguém, porque **nunca foi atribuída a uma área**. A prova é o desencontro que aconteceu
ao vivo em 09/09, entre 00:28:50 e 00:34:24:

| Quem | Entendimento |
|---|---|
| Eduardo Santos (Core Solutions) | As jornadas do legado já tinham sido reconstruídas no Campana: *"a gente deu o OK, inclusive para autos"* |
| Mirella Mendonça (marketing) | Montar jornada é trabalho de marketing: *"montar a comunicação dentro do Marketing Cloud é coisa de marketing, depende da gente"* · *"isso me parece ser algo bem simples"* |
| Michelle Morais (CRM) | Só a Data Extension foi migrada, e montar jornada exige perfil técnico: *"a gente sempre teve uma pessoa técnica que faz isso pra gente"* |

**Formulação como política implícita**, que é o formato que a CRT exige (regra 5: causa-raiz é
política, não pessoa):

> *"A execução técnica de CRM é tratada como serviço de terceiro, não como capacidade da área.
> Quando o terceiro sai, a atividade não tem para onde cair, e como nenhum indicador observa a
> atividade, a parada não gera alarme."*

Hoje quem constrói é Augusto Vasconcelos, da **C3C**, consultoria externa com escopo e prazo
próprios. A dependência foi reconhecida na sala, com o caminho já nomeado por Michelle: capacitar o
time para autonomia.

## 🔴 3. Cinco meses de silêncio e nenhum indicador acusou

Este é o achado que liga a auditoria (i) à **Trava de Cegueira**, já pontuada em 5 de 25.

A parada não foi descoberta por métrica, alerta, relatório ou reunião de resultado. Ela apareceu
**numa conversa com uma consultoria externa**, quando duas áreas compararam o que cada uma
acreditava estar acontecendo. Uma operação que perdeu, por um trimestre e meio, todo o contato
programado com o cliente recém-comprado, e o sistema de gestão não registrou o evento.

Isso confirma, por outro caminho, a dimensão E do
[score da Trava de Cegueira](trava-cegueira.md): a cadência de leitura existe, é diária e
disciplinada, e lê receita e EBITDA sem ler o que produz receita no mês seguinte.

## 🔴 4. Toda a aquisição de CRM depende de uma ferramenta cuja permanência não está decidida

99% a 100% da aquisição de CRM sai por WhatsApp, e o WhatsApp sai pela **Blip**, que não tem
integração com o Marketing Cloud.

| Quem | Posição, em 09/09 |
|---|---|
| Eduardo Santos, dono técnico | *"teoricamente a BP vai morrer"* · *"a gente tem um down time muito grande com eles"* · **"não funciona"** · a Blip nem participa do bid de disparo de WhatsApp |
| Mirella Mendonça | *"isso não está pacificado de que Blip vai morrer"* |
| Michelle Morais | *"até que a gente tenha isso formalizado, a gente segue com o plano"*, e o plano é integrar a Blip ao Marketing Cloud |

Substituição prevista para o **Q1**, com a discussão comercial ainda por acontecer. Enquanto isso,
o time de CRM investe em integrar uma ferramenta que o time técnico quer desligar. É desperdício de
capacidade da estação mais lenta, e é decisão que só o cliente pode tomar.
[Pendência 31](../PENDENCIAS.md).

## 🟠 5. A base de clientes sai em planilha e sobe à mão, e isso custa três coisas

Sem integração Marketing Cloud ↔ Blip, o ciclo de cada disparo é: extrair a base, tratar, quebrar
por volume diário, exportar e subir manualmente na Blip.

**Custo 1 · exposição.** Quem levantou foi a própria OLX, em 09/09 (00:48:35):

> **Mirella Mendonça:** "o item quatro, cinco, o sete e o oito [...] são super críticos porque
> envolve LGPD, envolve inúmeros outros riscos aqui pra gente."

**Custo 2 · medição.** A integração não carrega tag de campanha. Sem tag, não há atribuição do que
o CRM produziu, e isso casa exatamente com o que o slide FLUXOS da OLX já admitia em 28/08:
*"teste de campanha paga para WhatsApp: entra tudo como Direto"*. O canal Direto, maior fatia do
mix com 36%, engorda com o que o CRM e a mídia produzem e não conseguem reivindicar.

**Custo 3 · capacidade.** É trabalho humano repetido a cada disparo, executado por um time de três
pessoas que hoje são duas e meia.

## 🟠 6. O dado que chega ao Marketing Cloud é qualificado para vender, não para falar

O arquiteto do Campana é explícito (09/09, 00:38:56): o dado que desce para o marketing é
*"qualificado para que a gente consiga fazer uma venda e não necessariamente um dado que vai estar
super ultra limpo"*. E Michelle completa o motivo (10/09, 00:10:30): a sanitização anterior foi
feita *"com a cabeça muito de billing"*, ou seja, o suficiente para cobrar.

O resultado, na base de disparo:

| Defeito | Tamanho declarado |
|---|---|
| CEP ausente | **mais de 50%** `[E]` |
| Nome em caixa alta/baixa, duplicado, `undefined`, nome sobre nome | percentual não lembrado na sala |
| Documento gravado em campo de nome | sem número |
| Telefone duplicado e sem máscara | sem número |
| Data em formatos distintos | sem número |

**Contradição interna a resolver:** Michelle trata o CEP como campo mandatório da qualificação do
bot; Juliana Arndt diz que dá para disparar sem ele, o fluxo só demora mais (10/09, 00:09:23). Ou o
CEP é bloqueio, ou é atrito, e as duas leituras produzem decisões diferentes sobre a base elegível.

**O que já andou:** Evelyn Milare automatizou a higienização dentro do Marketing Cloud, sem tocar no
arquivo-fonte. Pronto para Autos, previsto para Imóveis na semana de 15/09.

## 🟠 7. O CRM não enxerga o produto do cliente

> **Michelle Morais** (10/09, 00:06:55): "quais são os campos hoje que eu não tenho acesso [...] em
> relação aos planos desses clientes, quantidades de anúncios, o quanto eles estão usando. Então
> esses dados hoje a gente não tem acesso, **a gente não trabalha a jornada em cima disso**."

A segmentação disponível é cadastral: contato, nome, documento, status ativo/inativo/novo, tempo de
inatividade, localização, inside ou field sales. **Nada de uso.**

Isso é o que torna estruturalmente impossível a jornada mais óbvia dessa operação: falar com quem
comprou e não publicou. A jornada de 28/08 registra os dois sintomas, a fatia que sai no primeiro
mês sem publicar (os 12% de [denominador em disputa](../PENDENCIAS.md)) e os **89% dos anúncios de
Imóveis que não recebem nenhum lead** `[D]`. Nenhum dos dois gatilhos existe hoje no CRM, porque o
campo que os dispararia não chega até lá.

## 🟠 8. A jornada de quem contrata e não anuncia foi testada, funcionou e foi desligada

> **Michelle Morais** (10/09, 00:31:38): "hoje a gente tem um percentual muito grande de clientes
> que contratam o plano, não anunciam e vão embora. E a gente fez alguns disparos pontuais para
> testar [...] com estímulo ele entraria e **eles responderam bastante bem**. A gente falou que a
> gente tem que automatizar, só que a gente começou a automatizar e já veio a migração e aí meio
> que não tá rodando."

Existe, portanto, uma ação com **evidência de resposta positiva**, gerada pela própria OLX, que
parou por causa da migração. Não é hipótese da V4 sobre o que funcionaria: é um teste do cliente que
foi interrompido. Pedir o resultado desse teste é prioridade da camada analítica.

## 🟠 9. O canal mais barato foi desligado, e o único canal ativo encarece em outubro

O e-mail saiu da aquisição na migração: *"o e-mail hoje tá esquecido, a gente não faz mais nenhum
tipo de disparo de e-mail para aquisição"* (10/09, 00:14:04). Sobrou WhatsApp, com custo por
mensagem, e a Meta muda a regra de cobrança **até outubro**, encarecendo o disparo.

A própria Michelle já desenhou a saída: e-mail primeiro, WhatsApp como segunda tentativa para quem
não respondeu. O que falta é o fluxo de atendimento para o lead que chega por e-mail, que não
existe hoje. [Pendência 35](../PENDENCIAS.md).

## 🟠 10. Não existe CDP, e o dado está pulverizado

> **Eduardo Santos** (09/09, 00:28:50): "nós não temos uma CDP única hoje, então hoje tá tudo
> pulverizado os dados. Então eu tenho dificuldade de saber onde estão cada um dos dados e como que
> eu construo essas jornadas."

O Campana unificou **três orgs de Salesforce** (OLX, Zap, VivaReal) em uma, o que resolve a
padronização de campo e objeto dentro do Salesforce. Não resolve a camada de perfil de cliente, e é
o dono técnico quem diz isso.

## 🟠 11. Três plataformas de relacionamento existem no GTM e não apareceram em duas horas de CRM

A [auditoria (vii)](auditoria-vii-rastreamento.md) encontrou, na instrumentação, três ferramentas
além do Salesforce. Nas duas sessões de CRM, com todo o time da área presente, **nenhuma das três
foi citada**. Só Salesforce Marketing Cloud e Blip.

| Ferramenta | O que o GTM mostra | O que as sessões de CRM dizem |
|---|---|---|
| **Insider** | Tag `[TAG] CRM Web Push - Insider`, **ativa**, em `GTM-KGFGVFC` (Planos Profissionais) e `GTM-MJX9PG4` (Conecta Autos). Sem gate de consentimento num dos dois ([achado 10 de (vii)](auditoria-vii-rastreamento.md)) | Nunca citada. **Mas o mapa de jornadas de Imóveis tem gatilhos de web push** na jornada de carrinho abandonado, e web push não é um recurso do Marketing Cloud em uso ali |
| **Braze** | 14 tags, instrumentação completa de CRM, **7 de 7 confirmadas pausadas em produção** ([achado 14](auditoria-vii-rastreamento.md)) | Nunca citada |
| **RD Station** | Contêiner dedicado `GTM-MVQWQJFB` em `materiais.olx.com.br` | Nunca citada |

**A hipótese mais provável para o Insider é que ele seja o web push do mapa de jornadas**, operado
por outra área ou herdado do B2C. Precisa ser confirmado, porque muda quem é o dono do canal.

O achado 14 de (vii) tinha deixado uma pergunta em aberto, *"implantação em espera ou projeto
abandonado?"*, dizendo que a resposta muda a leitura da camada de retenção. A resposta desta camada
experiencial é indireta e vale como evidência: **o time que deveria operar não sabe que existe**.

## 🟠 12. No ritmo declarado, o CRM só volta a operar inteiro no fim do Ciclo 1

Aritmética da V4 sobre uma taxa declarada pelo cliente, não projeção do cliente:

| | |
|---|---|
| Jornadas mapeadas no Miro | **15** (9 em Imóveis, 6 em Autos) |
| Temas de migração declarados | **5**: onboarding · carrinho abandonado · inativos e cancelados · upsell · pós-cadastro e nutrição |
| Ritmo declarado | *"mais ou menos duas semanas para cada um"* `[E]` (10/09, 00:37:50) |
| **Projeção** | **cerca de 10 semanas** a partir de 10/09, ou seja, **meados de novembro/2026** `[E]` |

O Ciclo 1 fecha no **Comitê 3, em 01/12**. A camada de ciclo de vida do CRM, portanto, volta a
existir **no último mês do ciclo**, e a migração de clientes de Imóveis para o Campana corre em
ondas **até o fim do ano**.

**Consequência para o método:** qualquer injeção que dependa de jornada automatizada de CRM não é
executável dentro deste ciclo em escala. Isso não desqualifica o CRM como trava, ao contrário,
mas obriga a Árvore de Pré-Requisitos a tratar a migração como **obstáculo com data**, e o forecast
a não contar com ganho de retenção via CRM antes de dezembro.

## 🟡 13. Existe jornada desenhada que ninguém consegue reconstruir

A máquina de inbound de Imóveis (lead score, nutrição e venda) não usa o recurso nativo do Marketing
Cloud: foi customizada no Salesforce. Michelle, sobre a tentativa de migrá-la:

> "mesmo com a documentação, ela não foi suficiente [...] mesmo documentada ela não ficou tão óbvia
> assim para poder ser replicada" (10/09, 00:33:02).

E convivem **duas versões** dela: a antiga, ligada, e a nova, revisitada e parada por dependência
técnica. A antiga foi mantida no ar *"para não ficar sem nenhuma"*.

## 🟡 14. A documentação é reconhecidamente insuficiente, e está sendo refeita por engenharia reversa

> **Michelle Morais** (10/09, 00:25:29): "a gente tem um processo de documentação muito pobre,
> assim, a OLX como um todo não é boa em documentar."

O padrão novo, decidido na sessão, tem duas peças: **Miro** para o fluxo visual e **Confluence**
para a especificação textual (nomes, segmentação, motivo, passos manuais, tags e UTMs), escrita pela
C3C conforme migra. O Miro atual **não registra tempo**: os intervalos entre toques só existem no
texto.

Como achado de maturidade, isso é mais relevante do que parece: a migração está custando dois meses
a mais porque a regra de segmentação precisa ser redescoberta a partir da ferramenta.

## 🟡 15. Quase não há teste A/B, e a automação vai reduzir o improviso que hoje faz as vezes de teste

> **Michelle Morais** (10/09, 00:59:14): "a gente hoje [...] faz pouquíssimos testes A/B [...] faz
> um pouquinho quando a gente fala na parte de aquisição, mas nos demais assim não faz."

O contraponto que o próprio time levanta é honesto e precisa entrar na injeção: o processo manual
tem *"muita liberdade poética"* para trocar copy e horário no meio do disparo, e a automação tira
isso. Automatizar sem instalar um rito de teste troca improviso por rigidez, e não por aprendizado.

## 🟡 16. O ambiente legado não é legado: é o B2C em produção

Detalhe de arquitetura que muda o desenho de qualquer correção: a BU antiga do Marketing Cloud
segue **viva e ativa**, porque é o ambiente atual do B2C (10/09, 00:16:35). Cliente B2B que entrou
numa jornada antes da migração continua recebendo até o fim dela. Ou seja, hoje convivem dois CRMs
B2B, um que só esvazia e outro que quase não enche.

---

## O mapa das jornadas, consolidado

Estado em 10/09/2026. O desenho completo está na
[ata da parte 2](../06-reunioes/2026-09-10-crm-jornadas.md#o-mapa-das-jornadas-do-miro).

| Vertical | Jornadas mapeadas | No ar no ambiente novo | Canais |
|---|---|---|---|
| **Imóveis** | 9 | **1** (onboarding) + a recuperação que o time faz à mão por WhatsApp | E-mail, quase exclusivo. Canal Pro **não tem push** |
| **Autos** | 6 | **0**, a primeira em teste desde 11/09 | E-mail **e push**, porque o profissional usa o app da OLX |

**Regra de canal declarada:** *"a gente gasta o WhatsApp quando tem receita"*. Engajamento e
divulgação de produto vão por e-mail e push. As exceções são **CredAluga** (garantia locatícia, com
compromisso contratual anual de produção) e **Autos 360** (hub do lojista, gratuito nos planos
premium, integra o anúncio a mais de 50 portais), os dois com meta de engajamento e adesão baixa só
por e-mail.

## O que o bloco B fecha, e o que segue aberto

| Item | Antes | Agora | Por quê |
|---|---|---|---|
| **B1** · Acesso de visualização | ⚪ | 🟠 | Declarado concedido em 10/09, **sem conferência na ferramenta** ([pendência 18](../PENDENCIAS.md)) |
| **B2** · Arquitetura de Data Extensions e lógica de segmentação | ⚪ | 🟡 | Descrita em detalhe nas duas sessões, incluindo o comparativo DEX legado vs. Campana. **Os slides não foram recebidos**, só apresentados em tela |
| **B3** · Relatórios de performance de e-mail, 12 meses | ⚪ | ⚪ | Nada recebido. E o achado 9 muda o sentido do pedido: em aquisição o e-mail está desligado, então a série de 12 meses é de ciclo de vida, não de aquisição |
| **B4** · Tamanho e saúde da base opt-in | ⚪ | 🟡 | A **saúde** foi descrita (achado 6) e é ruim. O **tamanho** não foi dito em nenhuma das duas sessões |

## O que falta para fechar (i)

Prioridade por valor para o Comitê 1, não por facilidade:

1. **A coorte sem ciclo de vida** ([pendência 30](../PENDENCIAS.md)): quantos clientes novos
   entraram no Campana desde abril em Autos e desde julho em Imóveis, e qual o churn deles contra o
   da coorte imediatamente anterior. É o número que transforma o achado 1 em dimensionamento.
2. **O resultado do teste de "contratou e não anunciou"** (achado 8): volume, resposta e receita
   recuperada.
3. **Performance das jornadas que ainda rodavam antes da migração** (B3): abertura, clique e
   conversão do onboarding e da recuperação, para estimar o que a parada custou.
4. **Tamanho da base opt-in por vertical** (B4), e a perda efetiva na higienização.
5. **Console do Marketing Cloud** (B1 conferido): quantas jornadas ativas existem de fato em cada
   BU, o que confirma ou derruba o inventário declarado.
6. **Quem opera Insider, Braze e RD Station** (achado 11).

## Para onde os achados vão

**Nenhuma trava é pontuada neste documento.** A pontuação é do POP de diagnóstico de trava, e a
regra 6 exige evidência formal para nota acima de 3: fala em reunião não é evidência formal.

| Trava | O que esta auditoria entrega | Dimensão que ela toca |
|---|---|---|
| **Retenção** | Achados 1, 7, 8, 12, 16. A jornada formal de pós-venda **existe desenhada e não está no ar**, num sistema cujo churn se concentra no primeiro mês | Jornada formal de pós-venda · Política clara de continuidade · Estratégia ativa de expansão |
| **Interesse** | Achados 1, 9, 13, 15. Nutrição, educacional e carrinho abandonado desligados; e-mail fora do ar na aquisição | Profundidade da jornada por etapa |
| **Cegueira** | Achados 3, 5, 10, 11. A parada não foi detectada; sem tag de campanha não há atribuição de CRM; sem CDP não há fonte única | Confirma a leitura já registrada em [trava-cegueira.md](trava-cegueira.md), dimensões D e E |
| **Qualificação** | Achado 6. O bot exige CEP e mais de metade da base não tem | Critério de qualificação e atrito |
| **Compromisso** | Achado 1, jornada de pós-cadastro. O lead cadastrado na landing page fica no limbo até o comercial ligar, sem nenhum toque | Continuidade do contato |
| **CRT** | Achado 2, na formulação de política implícita | Causa candidata |
| **FRT/PRT** | Achado 12: a migração é obstáculo **com data**, não risco genérico | Obstáculo |
| **Forecast** | Achado 12: sem ganho de retenção via CRM automatizado antes de dezembro | Premissa |

## Ressalvas de leitura

1. **Fonte única.** Tudo veio de duas reuniões conduzidas pela mesma pessoa. Não há contraditório de
   dado, só de percepção, e o contraditório que apareceu (achado 2) é justamente sobre quem faz o
   quê, não sobre o que aconteceu.
2. **Sem gravação em 09/09.** Só transcrição automática. Trechos podem estar ausentes.
3. **Nenhum material foi recebido.** Slides, Miro, Confluence e os dois dashboards do Looker foram
   apresentados em tela e prometidos. Até 14/09, nada chegou ([pendência 32](../PENDENCIAS.md)).
4. **Duas datas para a mesma ativação.** O onboarding de Imóveis aparece como 31/05 no resumo
   automático e como "dia 31" recente na transcrição ([pendência 34](../PENDENCIAS.md)).
5. **A contagem de 15 jornadas é do que foi mostrado no Miro**, não de um inventário do console. O
   número real pode ser maior.

## Como este diagnóstico fecha

(i) fecha em **17/09** com, no mínimo:

- [ ] Console do Marketing Cloud aberto e o inventário de jornadas ativas conferido contra o Miro
- [ ] Itens 1 e 2 de [o que falta](#o-que-falta-para-fechar-i) respondidos, ou registrados em
      PENDENCIAS com DRI e prazo
- [ ] B3 recebido ou declarado inexistente, porque inexistência também é evidência
- [ ] Os 16 achados revisados contra o que a camada analítica mostrar, com os que caírem marcados
      como derrubados, e não apagados
