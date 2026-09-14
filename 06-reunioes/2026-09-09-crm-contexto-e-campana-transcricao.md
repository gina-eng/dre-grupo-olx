# Transcrição · CRM e V4 consultoria · apresentação CRM (parte 1 de 2)

> ⚠️ **Confidencial.** Registro literal de uma reunião com o Grupo OLX. Cobre o aviso de
> confidencialidade das comunicações da OLX e a cláusula 5.3 do contrato. Não sai deste repositório
> privado, não vai para serviço externo e não entra em material que circule fora do projeto sem
> autorização escrita.

Documento-fonte da [ata de 09/09](2026-09-09-crm-contexto-e-campana.md). Insumo bruto, sem edição:
o arquivo abaixo da linha é byte a byte o que o Gemini gerou. A leitura da V4 vive em
[`02-diagnostico/auditoria-i-crm-marketing.md`](../02-diagnostico/auditoria-i-crm-marketing.md).

## Procedência

| Item | Detalhe |
|---|---|
| Encontro | CRM e V4 consultoria · apresentação CRM (online), **parte 1 de 2** |
| Data | 09/09/2026, 15h01 GMT-03 |
| Duração registrada | 01:02:42 |
| Formato | 100% remoto |
| Origem | Anotações e transcrição automáticas do **Gemini** no Google Meet. Evento na agenda de `michelle.morais@olxbr.com` |
| Arquivo original | `CRM e V4 consultoria - apresentação CRM - 2026_09_09 15_01 GMT-03_00 - Notes by Gemini.md` |
| SHA-256 do original | `1d3854c0c3c4b3ed2ae0da1f2f0f65a100ec41a69a8e4c8f4898126f650dee6a` |
| Recebido em | 14/09/2026 |
| Gravação | **Não houve.** Michelle Morais confirma na parte 2: *"a gente não tinha gravado ontem, a gente só transcreveu"* |

**Quem fala no registro.** OLX: Michelle Morais (CRM, conduziu), Eduardo Santos (Core Solutions),
Mirella Mendonça (marketing), Matheus Albuquerque (especialista Salesforce, Core Solutions),
Evelyn Milare (CRM, três semanas na área), Pietro Barbosa (CRM, em transição para Zap/VR),
Juliana Arndt (CRM Imóveis). V4: Leonardo Rosa (consultor focal), Rafael Corazza (coordenador),
Guilherme Lippert (cofundador, produtos de tech), Matheus Gomes de Souza Netto (engenharia de dados).
C3C: Augusto Vasconcelos e Gabriel Lopes constam do convite; **não falam** nesta parte.

## Como ler este registro

Cada fala tem nome, atribuir citação é seguro. Valem os cuidados de transcrição automática. O
vocabulário que mais se deforma:

| Aparece como | É |
|---|---|
| *Seos Cloud · seus force · sal force · seios force · Seus Force* | Salesforce (Sales Cloud, Service Cloud, Marketing Cloud) |
| *ensai seios · fio de seios · field seos* | inside sales · field sales |
| *DEX · DE · detextation · data extations · dar extensation* | Data Extension |
| *BP · bli · blip* | Blip, a plataforma de disparo de WhatsApp |
| *turn · turnito · turníssima · churne* | churn |
| *upsel · upscell · UPSEL* | upsell |
| *bote* | bot de qualificação |
| *leíd · rids* | lead |
| *MKL · STL* | MQL · SQL |
| *altos* | autos |
| *ORG · orgos forces* | org do Salesforce |
| *BU · BUUS* | business unit do Marketing Cloud |
| *one shot* | venda avulsa de destaque |
| *Mi · Michele* | Michelle Morais · *Mirela* é Mirella Mendonça, pessoa diferente |
| *Edu* | Eduardo Santos |
| *Ev · Evely · Evelyin* | Evelyn Milare |
| *Coraz · Rafa* | Rafael Corazza |

**Três pessoas chamadas Matheus circulam no projeto**: Matheus Albuquerque (OLX, Core Solutions,
fala aqui), Matheus Gomes de Souza Netto (V4, dados, fala aqui) e Matheus Rodrigues (OLX, FP&A, não
está nesta sala). Quando a transcrição diz só "Mateus", o contexto decide, e a ata marca quando fica
ambíguo.

Número dito aqui é **declarado**, não apurado (regra 1 do repositório).

---

# **📝 Observações**

set. 9, 2026

## **CRM e V4 consultoria \- apresentação CRM**

convidado [leonardo.rosa@v4company.com](mailto:leonardo.rosa@v4company.com) [rafael.loureiro@v4company.com](mailto:rafael.loureiro@v4company.com) [Matheus Albuquerque](mailto:matheus.gomes@olxbr.com) [Michelle Morais](mailto:michelle.morais@olxbr.com) [Mirella Mendonça](mailto:mirella.mendonca@olxbr.com) [Eduardo Santos](mailto:edu.santos@olxbr.com) [Pietro Barbosa](mailto:pietro.barbosa@olxbr.com) [Evelyn Milare](mailto:evelyn.milare@olxbr.com) [augusto.vasconcelos@c3csoftware.com.br](mailto:augusto.vasconcelos@c3csoftware.com.br) [gabriel.lopes@c3csoftware.com.br](mailto:gabriel.lopes@c3csoftware.com.br) [Juliana Arndt](mailto:juliana.arndt@olxbr.com) [guilherme@v4company.com](mailto:guilherme@v4company.com) [matheus.aparecido@v4company.com](mailto:matheus.aparecido@v4company.com) [matheus.netto@v4company.com](mailto:matheus.netto@v4company.com) [isabela.corsi@v4company.com](mailto:isabela.corsi@v4company.com)

Anexos [CRM e V4 consultoria - apresentação CRM](https://calendar.google.com/calendar/event?eid=NHB0YzgxNHB2M3QzaGU5Mm9lZ3JsOHR0bG0gbWljaGVsbGUubW9yYWlzQG9seGJyLmNvbQ)

Registros da reunião [Transcrição](https://docs.google.com/document/d/1nSMNNyk2lE6_YXNTfL4YDR168oGyaoD_tUptXjTIt7k/edit?usp=drive_web&tab=t.vt7yij7dz0mu)&nbsp;

&nbsp;

&nbsp;

### **Resumo**

Apresentação da consultoria e análise de gargalos e automação de dados.

**Contexto do Projeto V4**  
Consultoria V4 inicia projeto Destrava Receita para identificar gargalos operacionais no CRM B2B.

**Migração e Arquitetura**  
Migração de jornadas em autos e imóveis gerou interrupções e dependência da plataforma Blip.

**Integração e Ferramentas**  
Equipe discute níveis de acesso ao Salesforce e apresentação de painel analítico para diagnósticos.

&nbsp;

&nbsp;

### **Decisões**

## Precisa de mais conversa

* **Ajuste de cronograma e reunião de CRM** Ajustar o cronograma de diagnósticos da V4 para amanhã e manter uma reunião online de aproximadamente uma hora para finalizar o alinhamento de CRM.

&nbsp;

&nbsp;

### **Próximas etapas**

- [ ] \[Eduardo Santos, Mirella Mendonça\] Discutir Escopo Jornadas: Realizar uma reunião para detalhar o escopo das jornadas e as pendências da consultoria C3C. Garantir o alinhamento técnico entre os times envolvidos.

- [ ] \[Matheus Albuquerque\] Agendar Fórum Técnico: Organizar uma reunião para aprofundar na arquitetura do projeto Campana e fluxos do Sales Cloud. Detalhar as integrações de sistemas para os integrantes da V4 Consultoria.

- [ ] \[Mirella Mendonça\] Enviar Plano Mídia: Encaminhar o planejamento de mídia para Eduardo Santos validar. Facilitar o entendimento das estratégias atuais do time.

- [ ] \[Evelyn Milare\] Limpar dados de imóveis: Executar o tratamento e a limpeza da base de dados de imóveis para viabilizar o consumo do marketing até a próxima semana.

- [ ] \[Eduardo Santos\] Discutir integração e automação: Reunir com Paloma e Etienne para tratar da viabilização da automação dos disparos de WhatsApp e incluir Mateus no convite.

- [ ] \[Leonardo Rosa\] Reportar acessos pendentes: Enviar para Michelle a relação de permissões e níveis de acesso ainda não recebidos que impactam o cronograma de diagnósticos.

- [ ] \[O grupo\] Realizar reunião de CRM: Conduzir sessão online para finalizar a análise dos pontos pendentes relacionados ao CRM.

&nbsp;

&nbsp;

### **Detalhes**

* **Apresentação inicial e contexto da consultoria V4**: Michelle Morais iniciou a reunião apresentando os participantes da V4 Consultoria (Leonardo Rosa, Rafael Corazza, Guilherme Lippert e Matheus Gomes de Souza Netto) e os membros da equipe interna da OLX (Eduardo Santos, Matheus Albuquerque e Mirella Mendonça). A consultoria V4 foi contratada para executar o projeto "Destrava Receita", focado em eficiência operacional e em identificar gargalos de receita no ecossistema B2B da OLX ([00:00:02](#00:00:02)) ([00:04:55](#00:04:55)).

* **Objetivos e escopo da atuação da V4 no CRM B2B**: Michelle Morais detalhou que a V4 fará uma varredura completa por aquisição, estratégias de vendas, canais de entrada e atendimento para propor melhorias de receita ([00:06:10](#00:06:10)) ([00:10:12](#00:10:12)). Eduardo Santos e Mirella Mendonça discutiram o alinhamento necessário entre as soluções corporativas, a área de produtos liderada por Letícia e as frentes da consultoria para garantir suporte adequado ([00:08:58](#00:08:58)) ([00:12:57](#00:12:57)).

* **Estrutura da equipe interna de CRM e verticais de atuação**: Michelle Morais apresentou a equipe de CRM composta por Evelyn Milare (com três semanas na empresa), Juliana Arndt (focada em imóveis) e Pietro Barbosa (em transição para B2C) ([00:13:57](#00:13:57)). Evelyn Milare assumirá uma visão transversal (cross) para otimizar processos entre as verticais de autos e imóveis, sendo que a aquisição, upsell e vendas focam quase integralmente no WhatsApp (99 a 100%) para alimentar o time de inside sales (DBM) ([00:15:05](#00:15:05)).

* **Objetivos centrais do Projeto Campana e automação de dados**: Michelle Morais apontou que o Projeto Campana visa automatizar a integração de dados com o Salesforce Sales Cloud, melhorar a confiabilidade das informações, personalizar comunicações e eliminar silos legados de dados para superar gargalos operacionais e falta de testes A/B ([00:17:50](#00:17:50)).

* **Cronograma e lacunas na migração de jornadas em Autos e Imóveis**: Michelle Morais relatou que a migração em autos começou no final de março e em imóveis em julho, gerando uma interrupção nas jornadas automatizadas de CRM para novos clientes desde março, pois as campanhas permaneceram no ambiente legado ([00:23:38](#00:23:38)) ([00:26:09](#00:26:09)). Eduardo Santos, Mirella Mendonça e Michelle Morais debateram sobre as responsabilidades técnicas e de marketing na reconstrução das jornadas no Marketing Cloud, evidenciando desalinhamentos sobre quem deveria configurar as segmentações e fluxos ([00:28:50](#00:28:50)).

* **Arquitetura técnica legada versus unificada no Projeto Campana**: Matheus Albuquerque explicou a arquitetura técnica, destacando a unificação de três organizações (orgs) do Salesforce (OLX, Zap e VivaReal) em uma única org do Campana para padronizar processos, objetos (como contratos) e campos ([00:36:40](#00:36:40)). Matheus Albuquerque detalhou a camada de proxy e a distribuição dos dados qualificados para o Marketing Cloud, permitindo a segmentação para disparo de notificações ([00:38:56](#00:38:56)).

* **Critérios de segmentação de bases e extração de dados**: Michelle Morais apresentou os critérios utilizados para extração de bases de dados (contatos, e-mails, celulares, status de atividade, localização e regras inside sales/field sales), apontando que o processo dependia de relatórios manuais de contas e contratos extraídos por Business Intelligence ([00:40:22](#00:40:22)).

* **Tratamento de dados, limpeza e dependência da plataforma Blip**: Evelyn Milare descreveu o processo automatizado criado via automações no Marketing Cloud para sanitizar dados (correção de caixa alta/baixa, remoção de duplicatas, padronização de datas e celulares) para uso nos disparos de WhatsApp ([00:47:06](#00:47:06)) ([00:50:51](#00:50:51)). Mirella Mendonça e Eduardo Santos levantaram preocupações sobre riscos de conformidade com a LGPD e sobre a dependência da plataforma externa Blip para os disparos, sendo que Eduardo Santos pontuou que a Blip apresenta instabilidades (downtime) e deve ser substituída no primeiro trimestre (Q1) ([00:48:35](#00:48:35)) ([00:52:42](#00:52:42)).

* **Alinhamentos de integração e próximos passos da agenda**: Michelle Morais informou que há reuniões agendadas com Paloma e Etienne para tratar da integração da Blip com o Marketing Cloud e resolver bloqueios operacionais ([00:56:14](#00:56:14)). Leonardo Rosa propôs reorganizar o cronograma presencial do dia seguinte, uma vez que a V4 ainda pendencia de acessos para apresentar diagnósticos, acordando manter uma sessão online de cerca de uma hora para concluir a revisão de CRM ([00:58:12](#00:58:12)).

* **Níveis de Acesso e Integração de Ferramentas**: Leonardo Rosa aponta que a equipe ainda possui pendências referentes aos níveis de acesso com Carol. Mirella Mendonça questiona a equipe da V4 sobre a necessidade de acessos específicos de CRM para compreender a operação. Leonardo Rosa argumenta que, embora estejam compreendendo o contexto para o diagnóstico, é essencial entender a arquitetura anterior à migração, o papel de ferramentas como Blip e Marketing Cloud, e como integrá-las à ferramenta Vamos para extrair os melhores indicadores ([00:59:09](#00:59:09)). Guilherme Lippert complementa que, como há o uso de Salesforce (Marketing Cloud e CRM), a integração partirá disso, sugerindo uma conversa específica sobre a lógica do CRM e as integrações após o próximo alinhamento ([01:00:23](#01:00:23)).

* **Esclarecimento sobre a Ferramenta de Análise da V4**: Mirella Mendonça indaga sobre a natureza da ferramenta citada pela equipe da V4. Leonardo Rosa esclarece que se trata de um painel analítico para consolidação de dashboards, geração de diagnósticos e mapeamento de sete possíveis travas nas jornadas, e não de um CRM. Guilherme Lippert complementa informando que a V4 possui um próprio CRM, mas que ele não é comercializado ([01:01:25](#01:01:25)).

* **Agendamento da Próxima Reunião de Alinhamento**: Michelle Morais propõe e agenda uma reunião para o dia seguinte às 15 horas, com o propósito de examinar as jornadas de forma granular e verificar eventuais pendências operacionais para o prosseguimento das atividades. Leonardo Rosa e os demais participantes confirmam o horário combinado para o dia seguinte ([01:01:25](#01:01:25)).

&nbsp;

&nbsp;

*Revise as anotações do Gemini para checar se estão corretas. [Confira dicas e saiba como o Gemini faz anotações](https://support.google.com/meet/answer/14754931)*

*Como está a qualidade de **destas observações?** [Responda a uma breve pesquisa](https://google.qualtrics.com/jfe/form/SV_5bXzKQfylMIhSXc?confid=bMTEY37aASEPwMdGmF2IDxIXOBEBMgUIigIgABgFCA&detailLevel=standard&hasImages=False&entryPoint=footerMain&isGoogler=False) para nos dar seu feedback, incluindo o quanto as observações foram úteis para o que você precisa.*

# **📖 Transcrição**

set. 9, 2026

## **CRM e V4 consultoria \- apresentação CRM \- Transcrição**

### **00:00:02** {#00:00:02}

&nbsp;

**Michelle Morais:** Boa tarde, gente. Tudo bem?

**Leonardo Rosa:** Oi, Michelle, tudo bem?

**Michelle Morais:** Tudo ótimo. Eu vou pedir um minutinho para pegar um copo de água.

**Leonardo Rosa:** Claro,

**Michelle Morais:** Eu já venho.

**Leonardo Rosa:** sem problema.

**Michelle Morais:** Eu tô aqui falando 1:30. Espera só um segundinho.

**Leonardo Rosa:** Sei como é que é. M.

**Matheus Albuquerque:** Boa tarde.

**Rafael Corazza:** Po, boa tarde. Tudo bem,

**Leonardo Rosa:** Boa tarde,

**Matheus Albuquerque:** He.

**Leonardo Rosa:** Matheus.

**Guilherme Lippert:** M.

**Michelle Morais:** Oi, gente, de volta aqui. Boa tarde.

**Leonardo Rosa:** Boa tarde,

**Rafael Corazza:** Boa tarde,

**Matheus Albuquerque:** mesmo.

**Leonardo Rosa:** He.

**Guilherme Lippert:** А

**Michelle Morais:** Boa, bom. Deixa, eu acho que vem mais gente aqui do do meu time. A Mirella vai entrar na na próxima meia horinha, mas eu vou aqui só apresentar um pouco aqui, pedir para vocês falarem um pouquinho aqui quem vocês são, mas eu vou trazer aqui um contexto geral. Eu tô vendo que não tem ninguém da C3C, gente. Vou esperar um minuto que eles são, a gente tem uma daily antes que é o time que vai entrar aqui tá nessa. Certeza que eles são enrolados lá.

&nbsp;

&nbsp;

### **00:02:14**

&nbsp;

**Leonardo Rosa:** Entendi.

**Michelle Morais:** Quando chegar vão vir cinco pessoas para cá. Eu já tô, já tô até vendo. Então, só pra gente evitar aqui a a repetição do tema. Ping aqui a galera.

**Eduardo Santos:** Boa tarde,

**Michelle Morais:** A conseguiu tudo bem, gente?

**Rafael Corazza:** Boa tarde.

**Michelle Morais:** A gente tá esperando o pessoal da C3C conseguir chegar, amiga. Acho que eles estão fazendo a nossa daily aqui no Vieram, mas eu já vou começar que já estamos 3:05.

**Eduardo Santos:** Tá ótima.

**Michelle Morais:** Bom, gente, boa tarde. Eh, o que que é essa agenda aqui? Hoje a gente tem um grupo bem misto aqui de participantes. A gente tem o time aqui da V4 Consultoria. Depois vou pedir para vocês falarem rapidamente aqui o papel de vocês. Ali temos aqui o nosso time interno eh de core solutions, né, que trabalha com toda essa parte nossa, né, de de dados, que tá cuidando muito da integração do projeto Campana, que a gente fala aqui, que é um projeto de eficiência operacional, né, de conexão entre várias plataformas para que a gente tenha uma eficiência eh em atendimento, em visão de de cliente. Então, um processo complexo de falar em um em um tweet aqui, né?

&nbsp;

&nbsp;

### **00:03:48**

&nbsp;

**Michelle Morais:** Eu fiz uma tentativa muito rápida, mas eu vou deixar depois pro time falar. A Mirela, que vocês já conhecem, eh, e vai entrar aqui também a C3C, que é a consultoria que tá dando suporte pra gente aqui em CRM, no Marketing Cloud, nesse processo de imigração sistêmica. Então, eh, não vai ser talvez uma agenda de CRM tão trivial, porque é uma agenda que vai contextualizar o momento em que a gente está, muito mais,

**Leonardo Rosa:** Legal.

**Michelle Morais:** muito mais do que o que a gente tem em termos de jornada somente. Acho que é muito mais eh o contexto e as dores disso, de passar por um processo de melhoria, né, mas que depende de algo maior antes disso, tá? Querem falar um pouquinho o pessoal aqui da da V4 se apresentar?

**Leonardo Rosa:** Claro, pessoal. Então, muito boa tarde. Meu nome é Leonardo Rosa, eu sou consultor estratégico que tá à frente do projeto aqui do Destrava Receita Estratégico com LX. Tô junto aí do restante do time. Vou deixar ele falar rapidinho aí.

**Rafael Corazza:** Só cumplementando aqui no meu lado. Prazer, meu nome é Coraz, eu sou coordenador do time e tá atuando diretamente com vocês. Então, fico aqui bastante com o Léo, como vocês podem ver ali na câmera dele.

&nbsp;

&nbsp;

### **00:04:55** {#00:04:55}

&nbsp;

**Rafael Corazza:** Eu estou literalmente atrás dele. Eh, é onde a gente tá próximo aqui. Eu tô aqui mais para uma uma um direcionamento de projeto junto ao time operacional, realmente junto aqui com com o Léo e com os demais. Do nosso lado ainda tem o Gui.

**Guilherme Lippert:** Boa tarde. Boa tarde, pessoal. Aqui é Guilherme Lippert, cofundador da V4 e hoje cuido de produtos de ITEC aqui. Então vou est acompanhando também paraa gente poder ir entendendo como que a gente consegue fazer as integrações necessárias depois tanto do nosso produto que é o V4 Marketing Operational System, o vamos AI eh, com o CRM de vocês e a gente conseguir trabalhar em conjunto da melhor No.

**Matheus Gomes de Souza Netto:** E aí pessoal, boa tarde. Eu sou Mateus, sou engenheiro de dados aqui na V4 Company, tanto matriz e tanto de produto também. Tô à frente do Vamos.

**Michelle Morais:** Gente,

**Matheus Gomes de Souza Netto:** Yeah.

**Michelle Morais:** antes de passar pro time da OLX e da C3C, eu quero trazer um breve contexto aqui, né? estão sendo dando um passinho para trás aqui antes. A V4 consultoria é uma consultoria de B2B que foi contratada pra gente conseguir tocar aqui um projeto que eles têm vários módulos de atendimento aqui, uma uma expertise bastante grande, especialmente em fluxos de B2B, que que chama destrava receita.

&nbsp;

&nbsp;

### **00:06:10** {#00:06:10}

&nbsp;

**Michelle Morais:** Então esse esse módulo, como o próprio nome diz, ele é bem autoexplicativo, né? Ele vai passar por toda a nossa jornada, por todos os nossos processos de aquisição, canais de entrada, como que o atendimento acontece, estratégias de de vendas, como a gente consome os dados, como a gente faz o atendimento. Então, assim, eles fazem uma varredura por todas as áreas e processos para entender aonde existe um potencial de receita que está travado. E diante disso eles fazem propostas do que que a gente consegue fazer para então destravar. E uma dessas leituras nesse grande mapa que eles estão fazendo é a parte CRM. Por isso que a gente tá nesse capítulo aqui agora. Então tô só voltando um pouquinho atrás aqui porque eu já pude fazer isso com algumas pessoas que estão aqui, mas não com todos que estão aqui, tá? Então é só para poder voltar aqui para não. Então de novo, esse é o objetivo. Então eles vão fazer muitas perguntas aqui sobre o nosso CRM B2B e a gente vai tentar aqui ajudá-los nesse processo, tá? Eh, eu vou então quiser Edu quiser fazer as vezes aqui para apresentar o time de código uma maneira mais consolidada, mas acho que pode ser bacana.

**Eduardo Santos:** É, eu eu ainda tô sem contexto, mas aqui a gente tem uma área de core solutions que ela olha para toda a parte da jornada aqui do cliente de venda e pós-venda.

&nbsp;

&nbsp;

### **00:07:27**

&nbsp;

**Eduardo Santos:** Então, toda a parte de sales force, nuvem de salos e de service fica aqui com os meus times. Então, acho que a gente olha para toda essa parte de jornada, experiência, pós-venda, né? Aquisição, aquisição. Acho que a gente tem a integração ali com marketing, mas daí toda a parte de venda e pós-venda tá para cá e experiência do cliente. Ча.

**Michelle Morais:** E eu vou apresentar aqui de uma maneira mais cross o time de CRM que a gente tem aqui, a Juliana, a Evelyn e o Pietro. Eh, a gente tá tem uma uma divisão aqui, né, entre quem olha a parte de atendimento do profissional eh de real estate, né, a partir de imóveis para venda de planos e toda a parte de jornadas e ciclo de vida do do cliente de imóveis. E tem um espelho disso que é a parte de autos, né? A mesma coisa, toda a parte de aquisição, a upscell, a parte de vendas isoladas, que a gente chama de one shot, toda a parte de jornadas também desses clientes. Eh, e como a gente tá passando por um processo atual de migração de ambiente do marketing cloud, então a gente tá com apoio aqui do Augusto, que é da consultoria C3C, que tá fazendo essa frente técnica de marketing cloud. Então, junto aqui eh nesse processo pra gente, então, a parte de migração de data extensions e toda a parte de migração agora de jornadas, de revisão de processos, quando a gente tá falando bem tecnicamente de marketing cloud específico,

&nbsp;

&nbsp;

### **00:08:58** {#00:08:58}

&nbsp;

**Michelle Morais:** Yeah. de de forma mais específica, tá? Eh, eu vou começar a falar um pouquinho da área. Não sei se vocês querem algum O Edu tá entrando na cab. Você tem alguma outra dúvida, Edu, sobre contexto que você gostaria que eu desse aqui agora em relação ao projeto ou a gente pode tocar aqui em relação a CRM?

**Eduardo Santos:** Então, acho que na verdade eu eh eu não sei o que que fica mais fácil para eu conseguir entender aqui quais são os pontos, né? Porque a gente tá num monte de tratativas ali também que a gente tá fazendo junto com a C3C referente ao Marketing Cloud, B2B. Eh, a gente tem um plano bastante amplo aqui, que eu não sei o quanto você tá participando ali também, que a gente tá construindo junto com a Letícia. Então, a Letícia é minha para aqui de produto. Eh, e aí é mais para eu ter os o contexto aqui e acho que só para trazer o Mateus Albuquerque, que é aqui do meu time também, ele é especialista em seios force, eh, aqui da área. E mas daí eu não sei, Mi, o que ficar mais fácil, o que que você entender que faz mais sentido assim para eu ter o contexto, até para eu entender eh qual que é o papel, que projeto é esse da V4.

&nbsp;

&nbsp;

### **00:10:12** {#00:10:12}

&nbsp;

**Eduardo Santos:** Eu acho que seria seria interessante a gente entender até pra gente saber como que a gente consegue ajudar

**Michelle Morais:** É sim.

**Eduardo Santos:** mais melhor aqui. M.

**Michelle Morais:** Eh, vou voltar aqui um pouquinho que eu tinha comentado antes. Então, e a a V4 ela veio, Edu, de uma necessidade da gente conseguir melhorar a nossa os nossos resultados, né, ou a nossa performance de um modo geral, nossos resultados em receita mesmo, né, para como que a gente faz para conseguir ter melhores resultados e indicadores eh em termos de receita na nossa operação B2B, né, quando a gente fala desde a venda de planos, a retenção de clientes, então, como que a gente consegue ser mais eh dentro desse processo mais eficiente de alguma forma pensando em tudo que a gente faz e que pode tangir esse aspecto. Então, por isso que eu disse, eles vão eh passar, né, de uma maneira bastante ampla por todas as etapas nesse processo de aquisição, né, de venda de planos, de ch, de modelo comercial, eles vão ajudar a gente, com essa visão e esse conhecimento deles, a entender oportunidades que a gente tem nesse processo. Então, vou dar aqui alguns exemplos, tá? a gente vai compartilhar com eles como vem sendo a nossa estratégia de mídia de performance, por exemplo, para eles entenderem, fazerem questionamentos, pegarem a expertise deles, como eles já fizeram com outros clientes, para trazer novas orientações, eh, ideias, eh questionamentos, críticas pra gente se consegue otimizar o que a gente já vem fazendo.

&nbsp;

&nbsp;

### **00:11:50**

&nbsp;

**Michelle Morais:** Então, vai acontecer o que nesse capítulo de hoje aqui, isso com CRM. Então eles eles querem ter primeiro um entendimento. Vou tentar dar um banho de loja aqui rápido para eles, pelo menos do contexto do que que é o nosso CRM hoje para o B2B, que que a gente faz, como é que a gente faz o processo, em que momento que a gente tá, quais são as dificuldades para eles falar assim:"Ah, entendi como que é minimamente isso é rim aqui de vocês". Então eles estão dando, eles estão pegando acesso o nosso G4, o nosso, nossas informações, os nossos déches. Então, para eles conseguirem ler os nossos indicadores, eles estão falando com o time comercial para entender como que é abordagem de vendas, como que é o pit comercial, como que o time hoje é organizado. Eh, então assim, tem um um aprofundamento em cada uma dessas etapas para que eles saiam com um diagnóstico e uma orientação pra gente, entendeu? Eh, é essa a intenção dessa consultoria e a ideia é que a gente consiga fazer com que eles somem aqui a a expertise aos nossos esforços que a gente já já tá fazendo hoje em cada canal, em cada frente, tá bom? Vou então dar andamento aqui,

**Eduardo Santos:** Tá ótimo. Qualquer coisa a gente vai.

&nbsp;

&nbsp;

### **00:12:57** {#00:12:57}

&nbsp;

**Michelle Morais:** gente. Isso.

**Eduardo Santos:** Eu vou te questionando aqui.

**Michelle Morais:** Vamos levantando a mão.

**Eduardo Santos:** Não,

**Michelle Morais:** Exatamente.

**Eduardo Santos:** fica tranquilo.

**Michelle Morais:** Exatamente.

**Eduardo Santos:** Valeu.

**Mirella Mendonça:** Acho que é aqui, Edu, se tiver alguma pergunta mais técnica, eu certamente vocês vão conseguir ajudar, né, a responder. Acho que mais isso assim.

**Michelle Morais:** Exatamente.

**Eduardo Santos:** Ah, tranquilo. Essa é a parte fácil. Ô, ô, Mirela.

**Mirella Mendonça:** Posso para vocês, pra gente não. Às vezes faz uma reunião com vocês,

**Eduardo Santos:** Boa.

**Michelle Morais:** É isso.

**Mirella Mendonça:** parece que vocês estão falando outro idioma.

**Michelle Morais:** É isso aí.

**Eduardo Santos:** É bom que daí a gente se complementa sempre e dá bom.

**Mirella Mendonça:** Exatamente.

**Michelle Morais:** Eh,

**Mirella Mendonça:** Vou mandar você próxima vez. Eu vou mandar um plano de mídia para você aprovar para mim aí, para você ver que é fácil.

**Eduardo Santos:** Nossa, a gente tem que tornar mais fácil todas essas esses termos, né, de que a gente usa diferente aqui, tornar Так.

**Michelle Morais:** é verdade. Ó, gente, esse material, tá, é um material que ele tem até, tá, desculpa, tá um pouquinho lenta a minha internet aqui, eu tive uma questão com a Clara manhã toda, mas vamos, vamos que vai dar certo.

&nbsp;

&nbsp;

### **00:13:57** {#00:13:57}

&nbsp;

**Michelle Morais:** Eh, ele tá até com projeto campana aqui, porque a gente tá se organizando aqui, inclusive com eh com todas essas mudanças aqui que estão impactando bastante a parte de de B2B. Por isso que a apresentação da área de CRM tá com o projeto campana aqui pra gente, tá? Mas é é só uma fatia. E eu vou falar exclusivamente aqui, como tá bem escrito aqui embaixo, a a migração e a revisão estratégica da jornadas B2B de CRM, tá? Eh, nesse material eu não tenho organograma, mas o time que tá aqui hoje é o time que dentro de CRM são os representantes e que eh estão atuando hoje no B2B. Então, a gente tem aqui a Evelyn que vocês viram, né, que é super nova de casa. Evelyn tem três semanas de OLX, então ela é super jovem aqui no no nosso grupo e

**Evelyn Milare:** Oi, gente.

**Michelle Morais:** é aqui,

**Evelyn Milare:** Sim. Tô engatinhando.

**Michelle Morais:** mas já tá, ó, já tá surfando umas ondas altas aqui. Já tá, tá indo, tá indo que tá. Eh, e ela vai olhar eh paraas as duas verticais. A ideia é que ela tem um olhar um pouco mais cross para que a gente consiga ter otimizações, verificações de processos.

&nbsp;

&nbsp;

### **00:15:05** {#00:15:05}

&nbsp;

**Michelle Morais:** Então, o que que como é que a gente faz, o que que a gente faz bem em um lugar que a gente pode replicar para outro? Então, compartilhar um pouco como a gente os times acabam sendo um pouco mais eh isolados nessas iniciativas, né, quando o time comercial. Então, a ideia é que a gente tenha um ponto focal que consiga trazer uma uma visão mais cross. E a Juliana que tá com o foco um pouco mais aqui em imóveis, né? Então, olhando mais para tudo que é de imóveis especificamente. O Pietro vinha com background já de um olhar mais para altos, só que a gente vai, ele tá fazendo uma movimentação interna aqui, tá indo para o time de B2C de móveis. Então, ele tá passando essa parte de altos para Evelyin também. Então ela fica com essa frente de altos, mas com olhar um pouco mais cross. Então hoje temos Evely, Pietro e Juliana, mas em breve vai ficar mais focado na Evely e na Juliana, tá? Para vocês terem aqui quem são as pessoas. Bom, eh, hoje a gente, eh, trabalha aqui dentro de de CRM, eh, em, eu, eu vou fazer duas divisões aqui, porque elas têm uma atuação e um esforço de de times diferentes aqui um pouco.

&nbsp;

&nbsp;

### **00:16:19**

&nbsp;

**Michelle Morais:** A gente tem um uma frente bastante focada na parte de aquisição de planos, a parte de vendas, né, eh, mais exclusivamente. Então, é onde a gente tem o esforço aqui, a gente é um é um dos canais mais importantes aqui quando a gente fala especialmente pro time de DBM, que é o é o time de inside sales, que faz as vendas de planos menores ali, né? Eh, então o canal de CRM ele é muito é um dos maiores aí para conseguir entregar MQLs, enfim, toda a parte de leads qualificados para que eles consigam fazer as vendas. Então, a gente tem uma dedicação muito grande disso nesse processo. Ele hoje, basicamente é todo feito por meio de WhatsApp, assim, 99%, para não falar 100\. Então, basicamente é assim que a gente atua paraa aquisição, para UPSEL e para vendas one shot, que é venda de destaque. Dentro da nossa estratégia atual, CRM tinha uma ponderação, no começo do ano, era um pouquinho mais equilibrado os desphos que a gente fazia paraa aquisição, para one shot e pra parte eh de de upsel de, né, de de upsel de de planos, mas hoje em dia ele tá bem mais desequilibrado propositalmente. Então, como o próprio time ali de farmer, eles estão dando conta de fazer a parte de up por conta própria, é CRM tá com a missão maior aqui, aonde tem um gap maior comercial, que é conseguir leads para aquisição, tá?

&nbsp;

&nbsp;

### **00:17:50** {#00:17:50}

&nbsp;

**Michelle Morais:** Então, a nossa base, a nossa segmentação, a nossa estratégia tá muito focada na aquisição de planos, planos novos, tá? Isso. altos, isso para imóveis. Então, a gente tem essa frente que ela é um processo, porque por que que tá o campana também aqui? É um processo hoje muito manual, embora a gente tenha uma ferramenta que permite aqui uma automação, que é o marketing cloud, eh a gente tinha, por isso que o Campan existe, é a todo o próprio Seos Cloud, a forma como a gente fazia segmentações, a origem dos dados, eles vinham de tabelas apartadas, eles vinham de outras fontes que não estavam eventualmente no marketing cloud. Então tinha todo um acabou ali por trás que fazia com que esse processo operacional ele fosse sempre todo muito manual. Então a gente fazia várias extrações de base, fazia cruzamento, entendia mensalmente, né, uma parte estratégica ali de como que a gente faz isso, quem são, o que que a gente vai falar, com qual segmento, quem são os mais quentes, quem vai trabalhar com o que, né? O time comercial vai trabalhar com qual público, a gente vai trabalhar com qual público. Então entendi um pouco isso para não massacrar o cliente, né? Todo mundo faz abordagem não para ter uma estratégia por trás disso, mas na hora de operacionalizar tudo bastante manual, desde limpeza de dados, de filtros.

&nbsp;

&nbsp;

### **00:19:06**

&nbsp;

**Michelle Morais:** E aí a, né, e e aí como que a gente ia fazer esses disparos até a ponta, né? Vai subir na na ferramenta Blip, tudo muito manual. Eh, então aí eu vou trazer um pouco desse contexto de como é a fotografia do hoje para o que a gente fale em campana. Então, um dos grandes objetivos do Campana é que a gente automatize esse processo, né? A gente tenha uma plena integração ali com o Seos Cloud para que a gente consiga receber essa base, essas informações o mais limpo possível, o mais confiável possível e a gente consiga gerar aqui as segmentações e fazer os disparos de uma maneira fluida, tá? Então, acho que essa é um dos nossos primeiros objetivos que a gente tem aqui. Um outro objetivo é que a gente tem muita oportunidade de usar melhor e trabalhar melhor as informações que a gente tem em relação aos nossos clientes B2B. A gente tem total consciência disso, né? tanto pra gente eh personalizar mais as comunicações, pra gente ter novos gatilhos e falar de uma forma mais específica e mais estratégica de como a gente faz hoje, falar mais em relação aos planos que a gente tem, que os clientes, os planos que ele já t hoje. Então, conversar mais com ele, com as comunicações, conseguir passar mais dados e conseguir ter gatilhos mais estratégicos pro ciclo de vida desse cliente no, né, de acordo, desde para desde a abordagem mesmo de compra, quanto em todo o processo depois desse life cycle, quando a gente fala em em eh em outras jornadas, tá?

&nbsp;

&nbsp;

### **00:20:38**

&nbsp;

**Michelle Morais:** Então, de novo, automatizar como objetivo e o segundo objetivo, mas não menos importante, usar melhor os dados que a gente tem desses clientes, tá? É isso que a gente tá tentando mirar agora nesse processo agora que a gente fala de campana para CRM, tá? Eh, então eu meio que dei uma resumidinha do que a gente tem aqui e vou dar um pouco de andamento, né? Então, quando a gente tem aqui, falando em nosso ambiente legado, né, que a gente já tá deixando ele mais aqui para trás, a gente tinha então silos de informações e ausência de padronização. Então os dados não sanitizados, assim, uma configuração, espaçamentos, nomes maiúsculo e minúsculo, nomes que se repetem, eh, informações faltantes. Então, tem toda uma questão que eh se eu for explicar a parte de dados, a gente vai ficar só nisso, nessa agenda. não é o meu objetivo aqui, mas eu só queria trazer isso como uma dor importante aqui pra gente, que a gente tá em processo também de limpeza disso, né? Tanto para conseguir ter uma segmentação mais correta, quanto personalizar de uma forma melhor também, né? quando a gente quer trazer isso para as comunicações de CRM, eh, comunicações desatualizadas e fluxos inessados, a gente não tem uma uma boa cadência hoje, né, como a gente gostaria para conseguir rodar teste, fazer mais teste AB, experimentar mais formatos distintos.

&nbsp;

&nbsp;

### **00:22:04**

&nbsp;

**Michelle Morais:** Como a gente tem uma carga, um time muito inxuto e uma carga operacional muito grande, a gente perde, né, em time para conseguir rodar melhor testes e de novo a automação tende a agilizar um pouco mais esse processo hoje, tá? Fazemos, mas muito menos do que a gente poderia e gostaria de fazer. Disparos com muita intervenção manual e a subutilização no histórico de comportamento desse cliente B2B, como eu disse aqui antes, no Campana. A ideia é que a gente consiga ter uma visão única desse cliente profissional com dados centralizados e acessíveis, campos que podem ser otimizados por uma segmentação mais inteligente, mais dinâmica e mais quebrada, mais personalizado. Quando a gente fala em jornada B2B reativadas, por que isso, gente? Porque quando a gente, como é que foi assim, tentando também trazer história longa mais curta, campana, a gente eh fez uma migração aqui importante de como os dados desses clientes estão sendo eh visualizados, armazenados, tratados dentro do Seos Cloud, tá? Quando a gente vai para esse novo ambiente de seios cloud, automaticamente o marketing cloud tem que começar a beber de uma de uma de um outro lugar. a gente teve uma nova BU aqui de marketing cloud para começar a consumir então esses dados eh que foram migrados, né, para esse novo ambiente de Seos Cloud e aí sim fazer essa integração.

&nbsp;

&nbsp;

### **00:23:38** {#00:23:38}

&nbsp;

**Michelle Morais:** Eh, quando isso aconteceu, as nossas jornadas estavam todas e estão ainda no ambiente legado. Então, todas as jornadas que a gente tem de autos e de imóveis, a gente vai ter que migrar para ambiente novo, para essa BU nova, porque eu tô num outro lugar, consumindo de uma outra fonte. Então, a gente tá aqui correndo quanto tempo, porque eu tenho vários clientes que estão vivendo a vida aí sem ser impactado por nada em termos de jornada, tá? Para vocês terem uma ideia, né? Agora que a gente tá conseguindo melhorar, tem a a C3C aqui participando, a gente conseguiu fazer a a migração da nossa primeira jornada de onboarding de imóveis que tava eh como que tá aqui a jornada, só para eles entenderem, né? Os clientes que já entraram nela no ambiente legado, eles seguem nela, tá? Quem entrou continua, vai até o final e segue o fluxo completo. Mas o cliente novo que está no ambiente novo, que eu tô chamando de campana aqui, tá? O cliente que entrou, contratou um plano, tá no campana, já não tava mais recebendo nada em termos de impacto de CRM. Então agora ele vai passar a receber o nosso onboard. A gente sabe o quanto onbard é importante num processo de quando a gente tem um turnito alto de usuário, né, para receber ele, para explicar como são os planos, como que isso acontece.

&nbsp;

&nbsp;

### **00:24:52**

&nbsp;

**Michelle Morais:** E aqui eu tô falando muito de jornada eh perdão, promocional, tá gente? Então assim, o nosso CRM ele faz os disparos promocionais. Existem disparos que são transacionais, que aí eles acontecem diretamente pelo time de produtos, conectado com o time aqui também do Edu, pelo Mateus, que viabilizam esse algumas dessas desses disparos. E a gente também tem disparos que acontecem eh eh por exemplo de billing, né? A parte de pagamento, pagou, fez a cobrança, não fez. Então existe toda uma jornada também ali que acontece transacional do time de Billing. Então eu quero muito ter um tempinho aqui dos minutinhos para também mostrar um pouco a nossa cozinha porque essa é a intenção também aqui para vocês verem como que vem sendo hoje uma experiência desse cliente recebendo essas esses disparos que não são só nossos, eles são de vários lugares diferentes da empresa, tá? Eh, e aí a gente quer fazer o quê? Uma personalização profunda em tempo real. baseada em histórico. Eu tô falando muito. Tá, tá claro, gente, assim, tem alguma dúvida, algum questionamento até agora?

**Leonardo Rosa:** Por quanto tempo vocês estão fazendo essa? Há quanto tempo, aliás, vocês estão fazendo essa migração?

**Michelle Morais:** Em autos?

&nbsp;

&nbsp;

### **00:26:09** {#00:26:09}

&nbsp;

**Michelle Morais:** Ela começou no final de março.

**Leonardo Rosa:** Так.

**Michelle Morais:** Eh, então a gente vem fazendo desde então ali dentro de autos. batemos muito cabeça, enfim, depois a gente vai passar um pouco por esse slide aqui. E aí a gente começou agora em imóveis em julho,

**Leonardo Rosa:** Угу.

**Michelle Morais:** né? E finalizamos agora. A gente acabou de fazer o teste dessa migração da migração. E o que que eu tô chamando de migração aqui, gente? É o data extension para permitir que os meus disparos de aquisição aconteçam nesse nessa BU nova. Ou seja, eu faço os meus disparos de WhatsApp para vender os planos e a fonte desses dados já estão dentro do marketing cloud. É isso que eu tô querendo dizer no ambiente novo. Tá? Agora, desde março, quando os disparos começaram, quando com essa quando essa migração de autos aconteceu, quando a gente migrou, né, os clientes começaram a a serem cadastrados os novos clientes no ambiente novo, no Campana Novo. A gente já parou de disparar para ele as novas jornadas, por exemplo, de autos. Elas elas ficaram no ambiente velho e não ligaram ainda, viu? Nenhum nenhum nenhuma mãe tá ligou. a gente tá desde março, desde abril até agora, sem conversar dentro de um círculo de vida com esse cliente de autos, por exemplo, entendeu?

&nbsp;

&nbsp;

### **00:27:38**

&nbsp;

**Michelle Morais:** Assim,

**Leonardo Rosa:** Угуm.

**Michelle Morais:** para vocês entenderem qual qual como que tá a eh a gravidade e a parte de imóveis desde julho, porque a gente em julho, então quem já tava nessa jornada, ela tava participando dela. Então, a gente faz algum disparo pontual de algum produto que a gente quer, algum lançamento, mas a gente não tem a parte de jornada, tá?

**Leonardo Rosa:** Угу.

**Michelle Morais:** Vai, Edu.

**Eduardo Santos:** Ô, e todo o trabalho que a gente fez ali com a C3C não contemplou essas jornadas, mas o que que a gente fez com eles?

**Michelle Morais:** Ele tá acontecendo agora.

**Eduardo Santos:** Então não não to tudo que a gente fez,

**Michelle Morais:** A gente, a gente foi só a de

**Eduardo Santos:** porque de autos a gente fez lá atrás em março.

**Michelle Morais:** Edu.

**Eduardo Santos:** E aí a gente fez a gente tava com problema da questão dos dados. A gente fez uma reunião, a gente pegou ali quais eram os dados e a gente criou ali em sei lá,

**Michelle Morais:** Isso.

**Eduardo Santos:** dois dias, a galera fez todos todas as jornadas ali, né? Porque hoje o que a gente tem nada mais do que é uma integração com o sales cloud para vocês buscarem as informações ali pro marketing cloud. O ponto é, nós não temos uma CDP única hoje, então hoje tá tudo pulverizado os dados.

&nbsp;

&nbsp;

### **00:28:50** {#00:28:50}

&nbsp;

**Eduardo Santos:** Então eu tenho dificuldade de saber onde estão cada um dos dados e como que eu construo essas jornadas. Mas eu entendo que o que existia de jornada do legado a gente reconstruiu dentro de campana,

**Michelle Morais:** Ainda não, Edu.

**Eduardo Santos:** porque a gente deu o OK,

**Michelle Morais:** A gente tá começando agora.

**Eduardo Santos:** inclusive para autos, né?

**Michelle Morais:** A gente deu OK. A gente migrou a DEX, só a data extension, Edu, só os dados para conseguir fazer os disparos de aquisição. Naquela época a gente não tinha conseguido parar para fazer ainda nenhuma jornada. Tudo que a gente ficou patinando ali foi para conseguir trazer os dados para pro ambiente novo, entendeu?

**Mirella Mendonça:** Mas aí,

**Michelle Morais:** Então a gente

**Mirella Mendonça:** pera aí. Então, é uma questão de jornada da gente montar as jornadas do marketing cloud novamente, o e-mail, os disparos e é isso que a gente não tá fazendo desde abril.

**Michelle Morais:** só um minutinho, gente.

**Eduardo Santos:** อ

**Michelle Morais:** É isso que a gente não faz desde abril, porque a gente não fez essa migração. A gente tá com o o time fazendo escopo para conseguir começar a fazer essa migração. Isso não não tá acontecendo desde então.

**Mirella Mendonça:** Tá.

&nbsp;

&nbsp;

### **00:29:57**

&nbsp;

**Mirella Mendonça:** Mas quando você fala migração, é a migração das comunicações, é, é, é o setup, é a configuração da comunicação dentro do marketing cloud.

**Michelle Morais:** Isso.

**Mirella Mendonça:** Então assim,

**Michelle Morais:** Exatamente. Exatamente.

**Mirella Mendonça:** do ponto de vista de dependência de engenharia aqui, isso foi em abril, porque a a a montar a comunicação dentro do market cloud é coisa de marketing, depende da gente.

**Michelle Morais:** Não, a a gente precisa do conhecimento técnico. É isso que a CC tá fazendo aqui pra gente, inclusive, porque na hora de montar a jornada, a gente tem que montar as segmentações delas. E para montar as segmentações, a gente precisa do conhecimento técnico, entendeu? Mi? E aí?

**Mirella Mendonça:** Mas a segmentação você não faz a partir da da data extension. O dado já tá indo para lá. Você faz a segmentação dentro do data extension.

**Eduardo Santos:** Esse era o meu entendimento.

**Michelle Morais:** Mas é

**Eduardo Santos:** também. Por isso que para mim tava tudo certo. Talvez eh a gente precisa entender qual é esse escopo de fato que a gente eh tem faltando pra gente entender qual é o problema e a gente atuar em cima do problema, porque talvez a gente esteja fazendo um monte de coisa, mas não é o que vai resolver o nosso problema, né?

&nbsp;

&nbsp;

### **00:31:09**

&nbsp;

**Michelle Morais:** gente, assim, eu vou até eh até pedir para que se o Augusto quiser trazer um pouco mais de tudo que ele tá trazendo aqui. Mas de novo, quando a gente teve essa migração de de dados, a gente sempre precisou dessa pessoa mais técnica para poder trazer isso pra gente e como criar essas segmentações dentro do marketing cloud, porque ela não é uma segmentação tão trivial assim. a gente precisa de uma, a gente sempre teve uma pessoa técnica que faz isso pra gente. Então, desde abril para cá, a gente tava primeiro tentando primeiro trazer esses dados e esses dados vieram para cá mais ou menos em maio.

**Eduardo Santos:** Ja.

**Michelle Morais:** Se se o Pietro pode até me corrigir aqui, quando a gente conseguiu terminar a data extension de autos pi, foi mais ou menos maio, não foi

**Pietro Barbosa:** Isso mesmo. Até então, a gente tinha ficava dependendo do time de inteligência operacional compartilhar as planilhas pra gente poder usar a base.

**Michelle Morais:** isso? Isso. Então, o que que a gente começou? A gente começou essa etapa e fechou aqui em maio e depois a gente começou a e fazer o mesmo, ou seja, a gente a gente tava na na data extension só, tá gente? A gente não tava fazendo nada de jornada, a gente tava tentando sanar a parte da aquisição.

&nbsp;

&nbsp;

### **00:32:18**

&nbsp;

**Michelle Morais:** Quando a gente sanou, a gente começou a parte de imóveis.

**Eduardo Santos:** Eh É, não, eu acho que a gente tem que puxar um papo à parte até pra gente fazer isso. Acho que a Flor já pediu isso pra gente inclusive no num outro fórum. Eh, e a gente detalhar isso pra gente caminhar no pro lugar certo, porque eu senão acho que a gente vai ficar eh tem coisa que talvez não seja claro eh de marketing que não é claro pra gente aqui e talvez coisas daqui que não é claro lá, porque a gente não tem imigração, a gente não tem mais nada disso. Migração aconteceu lá em Campana. Então, o que a gente foi, é o que a Mirela comentou, a gente colocou as data extations lá na minha minha visão, o Pietro tava criando todas as jornadas ali a partir dessas datas extension e fazendo os disparos. Então isso era o que tava na minha cabeça.

**Michelle Morais:** É, é o

**Eduardo Santos:** E aí eu acho que vale a gente ter esse papo pra gente se aprofundar um pouco nisso, entender o que a gente precisa e aí a gente consegue colocar as pessoas para fazer isso,

**Michelle Morais:** Eh,

**Eduardo Santos:** porque me parece que deveria ser simples,

**Michelle Morais:** Edu.

**Eduardo Santos:** né?

**Michelle Morais:** Eh, a gente fez esse papo com a Seios Fós lá atrás, assim, inclusive com Petro trouxe até um diagnóstico, não sei se você vai lembrar, imagina que tava Carol, você a seus sócios.

&nbsp;

&nbsp;

### **00:33:28**

&nbsp;

**Michelle Morais:** a gente abriu todas as jornadas, inclusive lá, assim, eh, foi quando a gente mostrou esse cenário todo, mas enfim,

**Eduardo Santos:** Não,

**Michelle Morais:** a gente faz novamente se para caso precisar,

**Eduardo Santos:** mas é,

**Mirella Mendonça:** Ah.

**Eduardo Santos:** eu acho que é esse que é o ponto.

**Michelle Morais:** tá?

**Eduardo Santos:** Acho que eh que na nossa cabeça as jornadas, a parte técnica, beleza, eu acho que a gente tava resolvendo ali com a C3C. Então acho que a integração, a gente resolveu bem rápido a integração e aí depois teve a parte do detextation que a gente tava patinando lá, a gente pegou lá desse time de BI,

**Michelle Morais:** Mhm.

**Eduardo Santos:** replicamos ali e resolvemos dar extensation. Foi bem rápido depois que a gente chegou nesse nesse concerto, mas a criação das jornadas para mim era o Pietro que tava fazendo.

**Michelle Morais:** É, não,

**Eduardo Santos:** Então acho que isso a gente precisa entender,

**Michelle Morais:** ele não

**Eduardo Santos:** porque daí a gente precisa de alguém para criar as jornadas, mas daí não é um trabalho técnico,

**Michelle Morais:** é,

**Eduardo Santos:** daí é um trabalho ali do marketing, né?

**Michelle Morais:** mas a gente sempre teve isso com uma pessoa técnica fazendo pra gente, tá, Edu? assim. Então, eh, tanto que hoje quem tá tá montando a jornada é o Augusto que tá puxando, que tá montando a segmentação.

&nbsp;

&nbsp;

### **00:34:24**

&nbsp;

**Michelle Morais:** Então, assim, eh, mas fala mi

**Eduardo Santos:** Não, acho que tá tudo bem,

**Mirella Mendonça:** Ai, não, não. เอ

**Eduardo Santos:** mas eu acho que a gente só precisa ter isso claro pra gente conseguir eh separar e e fazer o que a gente precisa fazer, porque eu acho que a gente tá acho que tem um monte de coisa acontecendo separada e a gente não tá

**Michelle Morais:** Eh,

**Eduardo Santos:** conseguindo juntar tudo isso.

**Michelle Morais:** mas tá, quando o próprio Artur ele trouxe a proposta da C3C, ele trouxe com as jornadas ali dentro, tá? Ele trouxe aquele escopo que ele apresentou pra gente, o cronograma dele tinham lá dentro as jornadas também, tá? Então, só para Mas beleza, a gente pode chamar numa próxima agenda, não tem nenhum problema.

**Mirella Mendonça:** ia falar, vamos voltar pra agenda aqui, Mia. Aí eu acho que tem um até eu quero entender com a C3C,

**Michelle Morais:** Tá bom?

**Mirella Mendonça:** o escopo também direitinho, porque isso me parece ser algo bem simples, tá gente? Так.

**Michelle Morais:** Tá bom. Bom, eh, eu não sei se você, se a gente passa aqui com mais detalhe, acho que essa parte do do Campana não, não era minha intenção passar para por essa por essa migração, essa explicação aqui, assim, tudo bem a gente passar para eu poder focar um pouco mais aqui em CRM ou vocês acham que é importante passar para explicar o que era a arquitetura campana e e como que isso evoluiu?

&nbsp;

&nbsp;

### **00:35:37**

&nbsp;

**Michelle Morais:** um pouco para entender aqui com a própria eh V4. Vocês querem entender um pouco mais esse contexto ou se eu posso focar mais aqui na nas ações de

**Leonardo Rosa:** Eu eu acho que pra gente é muito interessante

**Michelle Morais:** CRM?

**Leonardo Rosa:** entender o que que tava acontecendo na na no ano no início do ano, vamos colocar assim, na primeira metade ali do ano,

**Michelle Morais:** Угуm.

**Leonardo Rosa:** entender essa arquitetura, como que tava montada, qual que era a ferramenta, qual que era a jornada. Yeah. E aí sim, esse contexto de imigração, eu entendo que ele ainda tá ongoing. Então tem muita coisa que vocês ainda vão precisar validar interno, vocês ainda tão precisando de algumas validações para dar os próximos passos. Eh, entender o pé que tá paraa gente já tá bom assim. É, é mais porque como a gente vai entrar nos diagnósticos agora de CRM, a gente vai precisar integrar isso com o Vamos também para fazer essa leitura completa eh de dados de resultados mesmo. A gente vai precisar entender como que tava a jornada até então.

**Michelle Morais:** Tá bom. Eh, já que o time tá aqui que olha campana, assim, não sei se Edu, o próprio Mateus, vocês querem passar um pouquinho por essa arquitetura aqui para poder dar um contexto, então, pro pessoal da da V4?

&nbsp;

&nbsp;

### **00:36:40** {#00:36:40}

&nbsp;

**Matheus Albuquerque:** Posso tentar comentar aqui em alguns tweets. É, gente, assim, é muito extenso o que a gente tinha no começo do ano, então vou tentar dar uma resumida, mas qualquer coisa acho que talvez vale até um fórum separado só pra gente falar tecnicamente, tá? se for surgindo dúvidas, talvez passar aqui mais rápido, depois a gente voltar pra parte de negócio. Mas basicamente a gente tem n sistemas internos aqui que no final de tudo vai se unir dentro de um sales cloud ou service cloud que vai ser o sal force. Então a gente tem um sistema de conta, a gente tem um sistema de cobrança, a gente tem um sistema de notificação de e-mail, a gente tem ns sistemas aqui e tudo aquilo que vem do online ou que vem do offline vai acabar caindo paraos seus foros de alguma forma. Então, um carinha deixou, um cara foi fazer uma compra e deixou o carrinho abandonado, vira um lead para dentro dos seus forces. O cara efetivou uma compra, vai virar uma conta e vai virar um contrato dentro dos seus forces junto com os produtos que ele contratou. E nessa estrutura de objetos, de tabelas que a gente tem dentro do seus force, ele vai cair pro market, onde a gente vai fazer segmentação e fazer os disparos. Então, de forma macro é isso.

&nbsp;

&nbsp;

### **00:37:47**

&nbsp;

**Matheus Albuquerque:** Com o Campana a gente tinha três orgos forces, uma de eh OLX, outra de Zap e uma de P. E a gente unificou tudo isso em uma única ORG pra gente conseguir padronizar tanto os campos que a gente tinha quanto processo. Então, também visando trazer uma eficiência operacional para todo mundo ali, pra gente ter uma linguagem única de fluxo dentro dos seus forces e até mesmo no final das contas a gente acaba ganhando agilidade em questão de desenvolvimento, porque uma vez que eh no legado eu tenho um objeto chamado contract e um objeto chamado service contract, que no final dos contos faz a mesma coisa, faz sentido a gente acabar unificando isso. Então o campana veio para isso. Missa, pode passar pro próximo slide, por favor? Então essa imagem meio que resume tudo. A gente tem ali os nossos sistemas internos que a gente tem conta, cobrança, notificação, geração de contratos e assim por diante. A gente tem uma camada que a gente chama de proxy que vai entender para qual ambiente ele tem que fazer o disparo, para qual ambiente ele tem que fazer a tem que gravar o registro. É campana, manda pro campana. ainda é alguma coisa que a gente não migrou, que tá no legado, manda pros legados e assim por diante.

&nbsp;

&nbsp;

### **00:38:56** {#00:38:56}

&nbsp;

**Matheus Albuquerque:** E no fim de tudo, a gente tem a camada de marketing que vai se destravar nas BUUS. Então o que a gente tem de dado de OLX, Bux. O que a gente tem dado de Zap, o dado de Zap. E o que a gente tem de BU do campana, que já são os dois dados unificados que de migração que a gente fez, vai cair tudo na org campana, que também vai cair pra do campana. Eh, e isso a gente pensa quando a gente fala de dado, também importante ressaltar isso, quando a gente fala de dado para campana, processo seos force, a gente tá falando de um dado qualificado para que a gente consiga fazer uma venda e não necessariamente um dado que vai est super ultra limpo para que a gente consiga fazer um disparo totalmente formatado com o nome do cliente, sem distinguir maiúsculo, minúsculo ou sem tipo de máscara, melhor explicando. Então esse é o dado mais, abre aspas assim bruto que vai chegar na camada de de marketing cloud para aí sim a gente criar segmentações e fazer com que o cliente caia nas jornadas de de notificações, seja por e-mail, WhatsApp, push e assim por diante. Dei uma breve resumida, tá? Mas se vocês quiserem, como eu comentei, eu acho que vale a pena a gente qualquer coisa marcar um outro fórum que aí eu posso acabar entrando mais no detalhe de cada cada tópico e até mesmo como que funcionava fluxo de venda no legado, como vai funcionar fluxo de venda no campana e assim por diante.

&nbsp;

&nbsp;

### **00:40:22** {#00:40:22}

&nbsp;

**Matheus Albuquerque:** Ah, e aí é uma telinha básica dos objetos principais que a gente acaba utilizando para fazer uma venda. Então, cliente entra como leíd, a gente cria uma conta, contato, uma oportunidade, passar por prospecção, cria uma acutação, inclui os produtos, a gente gera um pedido e a partir a camada de pedido é o onde a gente tem diversas integrações. Então, é onde a gente manda notificação pro cliente, é onde a gente cria cobrança, é onde a gente vai acabar fazendo ativação de produto pro cliente quando ele paga. E depois que ele paga, gera contrato, ativa e aí parte já do do marketing para fazer fluxo de onboarding e os fluxos que tiverem desenhados lá.

**Michelle Morais:** Bom,

**Matheus Albuquerque:** Não

**Michelle Morais:** aqui a gente tem mais alguns detalhes, na verdade, como a gente eh como que a gente faz hoje para extrair essa base ainda manual, como a gente disse, no nosso data extension, né, pelo marketing cloud, que agora a gente tá extraindo tanto de autos quanto de imóveis, essa essa parte da da migração da data extension já está OK, resolvida. Eh, e quais são as regras de de negócio hoje que a gente considera para segmentações, tá? Então, dados de contato, e-mail, celular, dos dados pessoais, nome, documento, CP, eh, status, né, são clientes ativos, inativos ou novos, porque a gente quebra muitas segmentações de disparos muito por aqui.

&nbsp;

&nbsp;

### **00:41:45**

&nbsp;

**Michelle Morais:** Eh, a inatividade dele, né, para poder entender que tipo de abordagem a gente faz com esses clientes e o quão mais quentes ou mais frios eles eles são. a localização, se a gente tem alguma campanha mais regionalizada, alguma coisa mais específica, alguma ação por região, o tipo inside seos ou field seos e alguma regra específica conforme algum objetivo de comunicação que a gente tenha. Esses são essas são as regras que a gente vem usando hoje em dia, como eu disse, eh com muita oportunidade aqui de colocar novos campos, né, de usar outras informações adicionais para enriquecer aqui essas jornadas em Business Intelligence. aqui a gente tem eh isso era eh quando a gente is o time de DBM hoje ele também, né, eles eles também são eles que nos orientam na verdade na estratégia quando a gente vê isso de forma conjunta, como que a gente vai fazer esses disparos, né, de acordo com a meta mensal, de acordo com as campanhas que a gente tem, de acordo com o capacity que o time tem. Então a gente sempre calibra ele ali com eles, porque os nossos disparos eles basicamente, como eu disse, vão pro atendimento offline. Eles vão pro processo ali de automação pelo bote, né? Uma qualificação ali automatizada de MQL para SQL. Então tem um processo que hoje ele é automático, mas no final do dia o cliente que tá interessado, ele vai pro atendimento humano, ele vai paraa venda humana.

&nbsp;

&nbsp;

### **00:43:06**

&nbsp;

**Michelle Morais:** Então, e aqui a gente tem, eh, antes, né, de ter essa integração, quando a gente ia fazer o disparo sem a integração, a gente pedia a base pro time de business intelligence. E quando a gente pedia, eh, eles usavam, eh, havia uma extração de dois pontos distintos, então eles iam em relatórios diferentes, um de contas e um de contratos. Eh, eles a gente tinha, então assim, eh, a gente usava campos parecidos, mas eventualmente, ô, perdão, quando a gente fala aqui, dura que fica bem na frente, a gente não consegue ler, né? Quando a gente fala que a parte de de filtro, a gente tinha que fazer muitos filtros manuais, muitas exportações. Então existia um processo extremamente burocrático que a gente até para que a gente a uma das grandes dificuldades que a gente teve nessa implantação, inclusive, né, para conseguir criar nossa DE era como que a gente conseguia eh chegar no resultado que business inteligência chegava fazendo um monte de recortes de várias tabelas distintas. Então essa era uma foi uma dor importante ali na época que inclusive honerou um pouco mais aqui o nosso processo, mas a gente conseguiu chegar num resultado aqui num num resultado final que a gente tem essas bases eh independentemente de onde elas são a hoje, de onde elas são extraídas, né, elas elas têm o mesma mesma volumetria, uma mesma qualidade e a gente tem confiança sobre elas, tá?

&nbsp;

&nbsp;

### **00:44:35**

&nbsp;

**Michelle Morais:** Eh, aqui tem alguns critérios que a gente usa, então eu não vou passar isso com mais detalhes hoje, mas aqui é o que que a gente faz hoje, né, o nosso passo a passo aqui pra gente eh fazer essa extração eh de contas, né, os relatórios que a gente considera, como que a gente monta essa base. Então, tem aqui as regrinhas mais específicas. Eh, aqui um pouco quando a gente faz um comparativo, né, dessa DEX legado que a gente tinha na DEX legado e o que a gente tem na na DE nova. Quando a gente fala aqui em autos, tá, esse especificamente de autos, a gente faz um comparativo de eh da qualidade de dados que a gente tinha, que a gente tem agora, né? Então, tem alguns que t uma equivalência, não tem nenhum tipo de alteração, mas a gente tem vários enriquecimentos. Então assim, na minha base legado, a data e início de contato era praticamente nula essa informação. E agora a gente tem esse dado que ele é muito importante pra gente fazer a abordagem mais específica pro cliente. Então aqui mostra um pouco o nível de qualidade que a gente foi adquirindo quando a gente migrou aqui pro campana, tá? Algumas coisas ainda estão parciais, são novos campos que a gente precisa de uma de uma de um treinamento ali, né, de uma de uma cultura de preenchimento melhor também do próprio time comercial, né?

&nbsp;

&nbsp;

### **00:45:53**

&nbsp;

**Michelle Morais:** Então acho que isso é uma questão que vai ter que evoluir também para que o campo também ele seja registrado. Então muitas vezes ele existe, mas ele tá com muito, ele tá muito vazio. Então o nosso uso também para ele acaba ficando prejudicado. Vamos, vamos fazer aqui o de real estate, o de imóveis. Eh, aqui um pouquinho como que a gente faz. E aqui, pessoal, ainda ainda estamos falando do do dos nossos disparos de aquisição, tá? aquele puro de WhatsApp que eu tinha comentado antes. Então, a gente extrai essa base, vai nessa data extension aqui nosso endereço, aplica as regras de negócio, quais são os filtros de elegibilidade que a gente vai colocar ali na hora. Hoje a gente exporta essa base para viabilizar os tratamentos que ainda estão manuais. a gente tá, a Evelyn que tá automatizando muitos desses processos aqui, tá melhorando essa qualidade de como a gente trabalha os dados, porque são eh é uma limpeza para consumo do marketing, né? Como que dados limpos para melhor consumo do marketing. Então, ela tá fazendo isso, fez para autos e deve fazer até a próxima semana aqui também para imóveis. Então, o que que é o tratamento e limpeza que a gente faz, né?

&nbsp;

&nbsp;

### **00:47:06** {#00:47:06}

&nbsp;

**Michelle Morais:** correção de nomes em caixa alta, caixa baixa, remoção de nomes duplicados, catamento de nomes como que tão como undefined, a remoção de nomes contendo documentos, então campos preenchidos em em lugares errados, ã preenchimento de CEPs que não estão disponíveis hoje tanto quanto a gente precisa, uma padronização de data, né, que às vezes a gente não tem padrões distintos, isso influencia na hora que a gente vai fazer uma segundação e organização de colunas conforme uma estrutura que a gente precisa para colocar na Blip, que uma das etapas também que ainda são, é um blocker de integração, é a gente fazer a integração do marketing cloud com a plataforma Blip pros disparos ficarem automatizados. Eh, um processo que ainda é manual aqui são essas exclusões e blocklists que a gente tem que fazer desses clientes hoje. Então, ainda precisa de uma ação aqui manual. Eh, aqui uma regra de quebra e rotatividade, né? Ou seja, essa base que ela é elegível, a gente tem que quebrar, tem que fazer a essa divisão de acordo com o volume diário. Então, a gente tá fazendo de uma maneira mais fluida também isso, mas é uma coisa que a gente tem que entender o capacity operacional. Isso não é inteligente e automatizado ainda hoje a gente pretende que isso fique, mas nós não temos ainda os nossos disparos inteligentes o suficiente pro capacite naquele dia e naquele momento de atendimento, né?

&nbsp;

&nbsp;

### **00:48:35** {#00:48:35}

&nbsp;

**Michelle Morais:** Então, se eu tenho menos pessoas ou mais pessoas, pessoas doentes, pessoas mais dispostas, menos dispostas, então a gente deveria calibrar o disparo para que o lead time fosse sempre, né, aquele que a gente gostaria. E a gente tem algumas eh isso, esse é um processo ainda hoje que não é automatizado. A gente tem que ir entendendo manualmente como é que tá o dia a dia e calibrando nos disparos conforme isso. E como eu disse, os disparos hoje feitos mandatoriamente do WhatsApp. Pode falar, amigo.

**Mirella Mendonça:** Ô Mi, eu acho que aqui tem um ponto Edu pra gente falar depois. Eu acho que é legal esse processo que a MI colocou aqui nessas caixinhas, né? O item quatro, cinco, o sete e o oito, digamos assim, eles são super críticos porque envolve LGPD, envolve inúmeros outros riscos aqui pra gente, né? Eh, então assim, eu tô entendendo que o item 4 e o item C, eh, na medida em que a C3C, eh, fez a integração da dos seus force com marketing cloud e que a gente recebe isso dentro de uma data extension, a gente resolve um problema que a gente não tem que ficar, né, tem independência dos outros times e tudo mais.

&nbsp;

&nbsp;

### **00:49:51**

&nbsp;

**Mirella Mendonça:** Então, primeira conexão, checked, don. Só que esse tratamento e limpeza aqui é um pouco do que a gente bateu um papo com o Mateus. Muitas vezes é a formatação que a gente precisa fazer a limpeza para poder fazer o disparo correto? Então é um telefone de um DDD que tá 11\. 9999 tracinho 00123, né? E aí o time tem que ficar fazendo ali quase que um substituir o dado numa planilha de Excel para jogar, para ir fazer o disparo. Esse processo manual aqui, eu tô entendendo que a gente encontrou um caminho, certo, Michele? Via data extension para fazer a correção a nível de data extension e não na nível da base que tá no seus force,

**Michelle Morais:** Isso.

**Mirella Mendonça:** certo?

**Michelle Morais:** Ev, você quer explicar um pouquinho que você que tá fazendo isso?

**Mirella Mendonça:** Não, eh, seu áudio tá sumiu.

**Michelle Morais:** Meu áudio sumiu. Voltou, gente.

**Mirella Mendonça:** Sumiu.

**Evelyn Milare:** voltou para mim.

**Michelle Morais:** Voltou,

**Evelyn Milare:** Tá OK.

**Mirella Mendonça:** Ô,

**Juliana Arndt:** para mim também.

&nbsp;

&nbsp;

### **00:50:51** {#00:50:51}

&nbsp;

**Michelle Morais:** voltou,

**Mirella Mendonça:** Evely,

**Juliana Arndt:** M.

**Michelle Morais:** voltou, gente. Tão me ouvindo?

**Evelyn Milare:** Aham.

**Mirella Mendonça:** para mim sumiu.

**Michelle Morais:** Sim.

**Leonardo Rosa:** 100%

**Mirella Mendonça:** Ah, não, desculpa, gente. Foi o meu. É o meu.

**Michelle Morais:** Que susto.

**Mirella Mendonça:** Meu fone que saiu de um,

**Michelle Morais:** Falei:

**Evelyn Milare:** O fone tá

**Michelle Morais:** "Meu Deus,

**Mirella Mendonça:** foi pro outro.

**Evelyn Milare:** ouvindo?

**Mirella Mendonça:** Então,

**Michelle Morais:** foi, foi. Eu, eu ia pedir para,

**Mirella Mendonça:** os fone F.

**Michelle Morais:** paraa Evelyn rapidamente que ela que tá fazendo esse processo. Acho que vale ela compartilhar com a gente aqui.

**Evelyn Milare:** Boa, gente. Basicamente o que eu fiz foi pegar os dados que a gente tem já integrados, os seus fors ali no marketing cloud. se a gente já tem essas bases, tudo certo. E aí o que eu tô fazendo é através de uma automação, eu pego esses dados, como eles estão vindo do seu esforço e faço essa tratativa através da automação que me gera uma nova base, já com os dados no formato que a gente precisa consumir para esses disparos manuais que a gente tá fazendo no WhatsApp hoje.

&nbsp;

&nbsp;

### **00:51:41**

&nbsp;

**Evelyn Milare:** Então, basicamente, o que eu automatizei foi a tratativa que o pessoal fazia manualmente lá no cheits antes. Então, a base já vem praticamente pronta, precisando adicionar uma coisa ou outra que é o tag da campanha, algumas coisas que não tem como a gente puxar isso automaticamente hoje.

**Mirella Mendonça:** Tá?

**Evelyn Milare:** Fou mais claro?

**Mirella Mendonça:** Então eu diria que tem tinha e porque isso foi tema do que a gente falou com o Mateus. Então isso aqui a gente encontrou um caminho para não ter que ficar fazendo downloads de planilhas e fazendo manipulação, certo? Tem um outro ponto aqui do que é importante é um pouco da discussão. Eh, não sei se você tava no comitê de métricas hoje que a gente tava falando, que é a gente pega essa planilha e a gente não tem uma integração com a Blip, Marketing Cloud, Blip, para fazer esse disparo, a segmentação e o disparo diretamente utilizando ali a interface da Seus Force, né, do marketing cloud. Então o time tem que pegar essa base também, quando colocar ali de forma manual na blip, né, para que o disparo seja feito. Correto?

**Eduardo Santos:** Eu não sei como tá isso lá,

**Mirella Mendonça:** Correto,

&nbsp;

&nbsp;

### **00:52:42** {#00:52:42}

&nbsp;

**Michelle Morais:** Correto,

**Mirella Mendonça:** gente.

**Michelle Morais:** correto, correto.

**Eduardo Santos:** mas teoricamente a BP vai morrer, né?

**Mirella Mendonça:** É, então esse é um ponto importante aqui da gente pacificar, porque pelo que eu entendi hoje na reunião, isso não táfic pacificado de que Blip vai morrer, né? O que tá lá é não, Blip vai ser utilizado para eh paraa parte de atendimento, para esse disparo aqui de aquisição. Pelo que eu entendi, isso é um tema que não tá pacificado. Então, acho que tem um tema aqui, Edu, que eh exige ainda, né, um processo manual que eu acho que a gente vai ter que colocar na mesa para tomar uma decisão, pra gente conseguir melhorar essa operação aqui que tá, né, eh, a gente tá tendo evoluções, mas eu acho que esse é um ponto de atenção,

**Eduardo Santos:** Sim.

**Mirella Mendonça:** tá?

**Eduardo Santos:** E a gente não vai conseguir melhorar isso com blip, não funciona. Esse é o grande problema que a gente tem. a gente tem um down time muito grande com eles. Então assim, a gente pode ali, o negócio pode tomar a decisão de querer seguir com blip, mas aí a gente vai ter que ver como que a gente vai fazer com essa com essa solução, porque não funciona.

&nbsp;

&nbsp;

### **00:53:48**

&nbsp;

**Eduardo Santos:** Então o ponto que existe hoje é que a gente tá ainda com campana, a gente já tá fazendo toda a migração do que é atendimento. Então, atendimento já vai ficar 100% seos force. Eh, e a gente não consegue puxar ali as discussões para fazer a migração de blip comercial. Então, isso é o que tá impedindo a gente de fazer esse ano. Então, ela tá prevista para acontecer em Q1, mas toda discussão com o comercial ainda precisa acontecer. O ponto que a gente tem discutido lá com a Iuna, com a Carol da LOL e tudo mais, é que não se perde nenhuma funcionalidade do que eles têm hoje. Então, acho que esse é o grande ponto. Mas a gente não deveria ter uma influência por qual solução seguir e sim qual problema eu tenho que resolver. Eu resolvi o problema. Não deveria ser um um problema a gente tirar a blip, até porque todo time que eu tenho hoje é referente a blip ali, então não faz o menor sentido alguém querer seguir com a ferramenta, entendeu? Mas é de fato essa discussão ainda ela não aconteceu. Então eu concordo contigo. A gente precisa fazer essas discussões acontecer e a gente tirar isso, porque daí a gente não tem, porque eu não tenho uma integração fácil com BP, nem uma integração que funcione.

&nbsp;

&nbsp;

### **00:55:08**

&nbsp;

**Eduardo Santos:** Então isso vai ser um grande problema. Eles já nem tão participando do bid de disparo. Então assim, a gente tá construindo comercial, tá con compras, né? tá construindo um bid para questão de disparo de WhatsApp. Eh, e eles nem participam porque não faz não faz sentido a gente seguir com eles para

**Mirella Mendonça:** Aí é,

**Eduardo Santos:** nada.

**Mirella Mendonça:** então acho que é Importante só dentro desse fluxo que a MI colocou aqui pro pessoal da V4 ter essência, né, que é o item 4 e cinco. Tô entendendo que a gente vai eh ir até o set, né? Na medida em que a gente limpa a base, que a gente, né, fazer esse processo que a Evelyn fez, ele vai ser um processo muito mais fluido e a gente vai conseguir automatizar muita coisa. Então isso é uma diferença do que que acontece. E esse item oito aqui, que é o disparo que a gente faz por fora, digamos assim, via bli, ele num horizonte, vamos colocar aqui, de um ano, né, ele deveria mudar, né, a gente tem essa intenção, né, enquanto companhia de fazer a migração para para seus force, né, para fazer o disparo ali por dentro também. Então, acho que essa é a informação importante de vocês terem.

&nbsp;

&nbsp;

### **00:56:14** {#00:56:14}

&nbsp;

**Michelle Morais:** Boa. De toda forma, gente, até que a gente tenha isso formalizado, a gente segue com o plano. Então, a gente tem uma agenda essa semana para falar de integração da Blip com o marketing cloud, tá? Então isso tá, porque a gente tem ali alguns dois blockers que a gente entendeu que não são uns um um grande eixo, é uma adaptação sistêmica para viabilizar essa automação, né, para conseguir colocar as tags ali de campanhas, para conseguir fazer toda a parte de atribuição de forma correta, conseguir fazer algumas quebras ali de público que hoje a gente não consegue no formato que tá hoje e tá endereçado ali com o time. A gente vai endereçar com o time, na verdade, essa semana para entender um pouco de tempos e movimentos.

**Eduardo Santos:** Quem tá nesse papo,

**Michelle Morais:** Então que a ideia é que a gente não a Paloma e a ETiene.

**Eduardo Santos:** ô, ô Michele?

**Michelle Morais:** A gente deu muitas voltas para conseguir chegar nelas, viu do assim, depois de algumas conversas com Venâncio,

**Eduardo Santos:** É,

**Michelle Morais:** com outro time, eh, voltou para elas e entendi que são com elas ali.

**Eduardo Santos:** tá, mas assim, a gente não deveria ter essa premissa de integração com Blip, eu deveria ter a premissa da de ter o disparo, entendeu?

&nbsp;

&nbsp;

### **00:57:16**

&nbsp;

**Eduardo Santos:** Então,

**Michelle Morais:** É,

**Eduardo Santos:** eh,

**Michelle Morais:** é,

**Eduardo Santos:** isso não deveria ser uma premissa.

**Michelle Morais:** é porque assim,

**Eduardo Santos:** Mas beleza, eu vou puxar,

**Michelle Morais:** hoje é,

**Eduardo Santos:** eu vou puxar elas aqui e a gente a gente discute isso. De qualquer forma, coloca o Mateus nesse nesse papo também, por favor.

**Michelle Morais:** tá bom,

**Eduardo Santos:** Eh,

**Michelle Morais:** combinado.

**Eduardo Santos:** e eu vou falar com elas aqui.

**Michelle Morais:** Eh, ele ele tem participado de quase todos, né, Mateus? Acho que só esse que eu não tinha colocado ele, mas eu coloco com certeza e a gente entende só que do porque de novo, se a gente quer automatizar eh esse esse ponto é realmente mandatório aqui pra gente, porque de novo, senão eu vou ter que ficar pegando a base, subindo lá na blip e eu continuo com processo manual ali,

**Eduardo Santos:** Não, não,

**Michelle Morais:** entendeu?

**Eduardo Santos:** não, não, não é isso que eu quero. Eu quero que tudo aconteça automatizado. O ponto é que nós não deveríamos estar preocupados de uma integração do marketing cloud com BP. É esse que é o meu ponto. A gente não deveria ter esse problema. Isso deveria ser transparente ali para vocês.

&nbsp;

&nbsp;

### **00:58:12** {#00:58:12}

&nbsp;

**Michelle Morais:** É isso.

**Eduardo Santos:** Mas beleza.

**Michelle Morais:** É isso.

**Eduardo Santos:** É o o a Blip,

**Michelle Morais:** A gente conversa assim.

**Eduardo Santos:** ela deveria ser utilizada como um broker aqui pra gente.

**Michelle Morais:** Uhum.

**Eduardo Santos:** É.

**Michelle Morais:** Boa. Eh, gente, a gente tá no nosso tempo, tem coisa para passar. Acho que eu vou ter que fazer uma segunda rodada. Não sei se a gente a gente vai ter a agenda presencial amanhã.

**Leonardo Rosa:** Eu ia, na verdade, abordar esse assunto hã pra gente reorganizar o nosso cronograma, porque como a gente ainda tá pendente de alguns acessos, até mandar uma mensagem lá no grupo hoje pra gente ver isso, a gente vai precisar esticar um pouco mais paraa frente sobre os os diagnósticos. A gente não vai ter o que apresentar para vocês amanhã nível de diagnóstico, porque a gente ainda tá pendente de alguns acessos ali.

**Michelle Morais:** Tá. Então eu, se a gente vai ter que ajustar, eu manteria pelo menos uma hora, uma horinha e pouco pra gente zerar a parte do CRM.

**Leonardo Rosa:** Pode ser, não tem problema. Aí a gente usa aquela agenda e fica online mesmo. Não tem problema. A gente pra gente zerar o CRM.

**Michelle Morais:** Tá bom. Tem mais assim depois vocês passam para mim o que que ainda tá muito pendente, gente, para eu tentar ajudar aqui na a puxar,

&nbsp;

&nbsp;

### **00:59:09** {#00:59:09}

&nbsp;

**Leonardo Rosa:** Tá, eu vou te colocar.

**Michelle Morais:** organizar, tá?

**Leonardo Rosa:** Não sei se não, tu não tá já, Michele. Acho que não. No fluxo de meio que eu tô com a Carol.

**Michelle Morais:** Não é esse? que é uma outra frente em que ela é a o herwer mesmo, mas eventualmente se eu puder dar alguma força aqui também você me dá um toque.

**Leonardo Rosa:** É, é mais com ela ali que a gente tá pendente mesmo da da dos níveis de acesso que a gente já tinha recebido e tem alguns que a gente ainda não recebeu mesmo. Aí tá naquela naquela trash de meio com ela ali.

**Michelle Morais:** Tá boa. Você quer falar, amig?

**Mirella Mendonça:** Não, eu ia falar para para você puxar isso, M, o que que tá faltando de de nível de excesso, principalmente o que que foi de marketing aqui para você eh eh coordenar com as outras pessoas, mas eu queria ouvir do time da V4 aqui se tem algo específico que vocês

**Leonardo Rosa:** Так.

**Mirella Mendonça:** queiram V.

**Leonardo Rosa:** Eu

**Mirella Mendonça:** ter acesso aqui do ponto de vista do CRM, eh, para entender mais da operação da gente ou se esse caminho aqui ele ele tá eh atendendo. M.

**Leonardo Rosa:** acho que eu tô conseguindo pegar um contexto muito interessante pra gente ter a contextualização do que que tá acontecendo e entender também a a leitura do diagnóstico da maneira correta do que a gente vai fazer, mas ainda vai ser muito importante a gente entender a arquitetura do que tava acontecendo até então,

&nbsp;

&nbsp;

### **01:00:23** {#01:00:23}

&nbsp;

**Leonardo Rosa:** antes dessa migração, por exemplo, quais são as ferramentas, quais são os papéis delas. e como que elas impactam isso eh nessa jornada total do cliente. Qual que é o papel da Blip? Qual que é o papel do market cloud? O que que ele faz? Como que a gente vai integrar isso também à nossa ferramenta, né? Ou vamos. Até o Guit tá aqui justamente para isso, para entender como que desse eh desse ecossistema todo, como que a gente consegue extrair os melhores as melhores indicadores aqui pra gente integrar eh como que a gente consegue integrar no vamos pra gente poder extrair os melhores indicadores. É verdade.

**Guilherme Lippert:** É, só falando sobre isso brevemente aqui, né? Já tá até bastante claro isso para para mim, né? Olhando que vocês estão com sales force, tanto marketing cloud como como CRM mesmo, pelo que eu entendi, né, até aqui, ah, boa parte dessa da da nossa integração vai partir disso, né? A gente vai integrar esse seus force e a gente vai conseguir ter ah esses dados posteriormente para serem analisados. Mas aí eu acho que entra depois que a gente ter esse próximo papo, a gente entender toda a lógica do CRM. Aí a gente pode ter um uma conversa específica só das integrações, como vai funcionar e tudo mais.

&nbsp;

&nbsp;

### **01:01:25** {#01:01:25}

&nbsp;

**Leonardo Rosa:** Ja.

**Mirella Mendonça:** Mas o que que seria essa ferramenta de vocês? Vocês podem explicar?

**Leonardo Rosa:** Aqui a gente apresentou para vocês na nossa primeira reunião presencial, que é o todo aquele painel de onde a gente vai fazer todos os dashboards, onde vão sair todas as informações, como que a gente vai resumir todos os dados que a gente precisa para gerar os diagnósticos.

**Mirella Mendonça:** Ah, é o dash, um dash analítico ali.

**Leonardo Rosa:** Isso,

**Mirella Mendonça:** É isso.

**Leonardo Rosa:** isso que tem todas as as jornadas,

**Mirella Mendonça:** Pronto.

**Leonardo Rosa:** tem todas, a gente vai passar por todas as sete possíveis travas ali por ele também.

**Mirella Mendonça:** Achei que fosse um CRM de vocês,

**Leonardo Rosa:** Não, não,

**Mirella Mendonça:** algo do gênero.

**Leonardo Rosa:** não.

**Michelle Morais:** Gente, então eu vou

**Guilherme Lippert:** A gente até tem o nosso CRM, mas a gente não vende ele.

**Mirella Mendonça:** Vocês têm tudo, né, Guilherme? M.

**Michelle Morais:** pessoal, eu vou então manter esse mesmo grupo na agenda de amanhã, que espero que que todos consigam aqui.

**Leonardo Rosa:** Perfeito.

**Michelle Morais:** Eu vou continuar porque depois a gente vai de fato pras jornadas, vai falar um pouco de uma maneira mais granular e aí a gente entende se fica alguma coisa pendente para

**Leonardo Rosa:** Ótimo.

**Michelle Morais:** prosseguir, tá bom?

**Leonardo Rosa:** Perfeito. a gente mantém então às 3 amanhã,

**Michelle Morais:** Isso,

**Leonardo Rosa:** tá?

**Michelle Morais:** combinado.

**Leonardo Rosa:** Fechou?

**Michelle Morais:** Obrigada,

**Leonardo Rosa:** Obrigado,

**Eduardo Santos:** Valeu,

**Leonardo Rosa:** viu,

**Michelle Morais:** gente.

**Leonardo Rosa:** pessoal?

**Eduardo Santos:** valeu, gente.

**Guilherme Lippert:** V

**Evelyn Milare:** ส

&nbsp;

&nbsp;

### **A transcrição foi encerrada após 01:02:42**

&nbsp;

*Esta transcrição editável foi gerada por computador e pode conter erros. As pessoas também podem alterar o texto depois que ele for criado.*