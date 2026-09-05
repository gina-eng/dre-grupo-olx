# De/para — clientes do repo × workspaces do eKyte

Levantado em 2026-08-10 via MCP (`list_short_workspaces`) contra `clientes/*/client.json`.
**24 clientes no repo · 45 workspaces no eKyte · 22 pares confirmados.**

O casamento foi feito à mão porque as grafias divergem entre os dois lados (ver
[Grafias divergentes](#grafias-divergentes)). Não dá para casar por slug automaticamente.

> **Atualizado em 2026-08-21:** entrou o 25º cliente do repo, `casa-flutuante`, que não existia
> quando este de/para foi levantado. Workspace `149800` e projeto `324795` criados nesta data.
> **O projeto está clonado mas NÃO planejado**, então nenhuma das 8 tarefas já entregues pôde
> receber baixa: ver [Casa Flutuante](#casa-flutuante-2026-08-21).
>
> **Atualizado em 2026-08-18:** segunda passada de conciliação. 15 tarefas fechadas
> (8 em `lucena-advisory`, 7 em `neo-solucoes`), todas com entregável novo no repo desde
> 12/08. Restam **97 abertas** nos 15 projetos. O estado vigente está em
> [Projetos EE 3.0 no sistema](#projetos-ee-30-no-sistema-2026-08-12) — **é essa a seção a
> consultar**, não a tabela histórica de 2026-08-10 abaixo.

**Três pares só existem por informação da operação, não por semelhança de nome** — o
workspace usa a razão social ou outro nome comercial do mesmo cliente. Confirmados pela
Regina em 2026-08-10; nenhuma busca textual acharia:

| cliente no repo | workspace eKyte |
|---|---|
| Paraná Control | `FM Zahra` (147943) |
| Bombachas Farroupilha | `Tapparo Industria` (147939) |
| ARX Cyber | `Brasiline (ARX Cyber)` (148876) — criado em 2026-08-10 |

## Armadilha: `meta.workspace_id` é do V4MOS, não do eKyte

Três clientes têm `meta.workspace_id` preenchido com um **UUID**, enquanto o eKyte usa
**inteiro** (`147933`). Verificado no código: é o **`organizationId` da API V4MOS**
(`https://api.data.v4.marketing/v1`) — o nome `workspaceId` foi descontinuado em 2026, mas
o repo segue gravando com a chave antiga. Ver
[plugins/v4-estruturacao-ia/CLAUDE.md](../../plugins/v4-estruturacao-ia/CLAUDE.md) linha 29.

- `arx-cyber` → `80acf61a-a356-4f6e-9a1a-4cbd206f5bc9`
- `farroupilha-bombachas` → `5b3a7a61-645d-4734-97bf-c41b2f1431cd`
- `lucena-advisory` → `d782cb07-f4c3-424a-8dfb-2d38890d41b3`

**Sobrescrever esse campo com o id do eKyte desliga a integração V4MOS do cliente.** O
`scripts/v4mos_fetch.sh` aborta com `SKIP: cliente sem integração V4MOS` quando o campo está
vazio ou inválido, e o mesmo valor é a chave de lookup em `.credentials/clients.json`.

Para gravar o id do eKyte no `client.json`, use uma chave separada — `ekyte_workspace_id`.

## Tabela

`modelo` = modelo de projeto EE 3.0 a clonar, derivado de `meta.modelo_venda`:
inside-sales → `320045` · e-commerce → `320126` · pdv → `320134`.

| slug (repo) | workspace eKyte | id | modelo_venda | modelo | entregas |
|---|---|---|---|---|---|
| amado-galantini | Amado Galantini ADV | 147923 | inside-sales | 320045 | 23/23 |
| arx-cyber | Brasiline (ARX Cyber) | 148876 | inside-sales | 320045 | 10/23 |
| bantur-viagens | Ban Tur VIagens | 147926 | inside-sales | 320045 | 5/23 |
| casa-flutuante | Casa Flutuante | 149800 | inside-sales | 320045 | 5/24 |
| cheirin-bao-shopping-via-sul | *fora de escopo* | — | pdv | — | 5/22 |
| farroupilha-bombachas | Tapparo Industria | 147939 | *(vazio)* | — | 16/22 |
| global-comercio-balancas | Global Comércio de Balanças | 147931 | inside-sales | 320045 | 24/24 |
| grupo-lamon | Lamon Peças Agrícolas | 147909 | inside-sales | 320045 | 23/23 |
| grupo-smk | GrupoSMK Log | 147912 | inside-sales | 320045 | 23/24 |
| ilha-service | Ilha Service | 147910 | inside-sales | 320045 | 22/23 |
| infinit-telecom | Infiniti Telecom | 147928 | *(sem client.json)* | — | — |
| jioji-cavalera | Jioji Cavalera | 147916 | *(vazio)* | — | 20/24 |
| jl-mecanica | JL Auto Mecânica | 147911 | pdv | 320134 | 5/22 |
| lilo-decor | Liló Decor | 147917 | e-commerce | 320126 | 22/22 |
| lucena-advisory | Lucena Advisory | 147907 | inside-sales | 320045 | 14/25 |
| luizy-souza | Consultora Luizy Souza | 147925 | inside-sales | 320045 | 23/23 |
| neo-solucoes | Neo Soluções | 147934 | inside-sales | 320045 | 14/23 |
| parana-control | FM Zahra | 147943 | inside-sales | 320045 | 24/24 |
| petterson-representacoes | Petterson Representacoes | 147933 | inside-sales | 320045 | 10/23 |
| raizes-e-folhas | Raízes e Folhas | 147920 | pdv | 320134 | 5/22 |
| santua-confeccoes | Santuá Confecções | 147941 | inside-sales | 320045 | 23/23 |
| selva-acai | Selva Açai | 147913 | inside-sales | 320045 | 14/23 |
| shop-saldo-olimpia | Shop Saldo Olímpia | 147922 | pdv | 320134 | 6/22 |
| vera-cruz-coworking | Vera Cruz Coworking | 147937 | inside-sales | 320045 | 22/23 |
| vital-glass | Grupo Vital (Vital Glass) | 147918 | inside-sales | 320045 | 6/23 |

## Projetos EE 3.0 no sistema (2026-08-12)

**16 projetos ativos** (15 até 2026-08-18, mais `casa-flutuante` em 2026-08-21). Os outros clones de 2026-08-10 foram descartados pela operação porque
não correspondiam ao produto que seria entregue. `list_projects` com `active=0` e `active=2`
mostra o que sobrou fora do ar:

| projeto | alias | workspace | estado | observação |
|---|---|---|---|---|
| `322372` | EE3-arx | Brasiline (ARX Cyber) | **inativo** (`active=0`) | substituído pelo `322467`; a operação pediu arquivamento, mas o registro está como inativo, não arquivado (`active=2`) |
| `321998` | EE3-Petterson | Petterson Representacoes | arquivado (`active=2`) | 30 tarefas |
| `321996` | EE3-Petterson | Petterson Representacoes | arquivado (`active=2`) | 1 tarefa, clone abortado |

`petterson-representacoes` ficou **sem projeto ativo** — os 10 entregáveis dele não têm onde
ser refletidos até a operação subir o projeto certo.

### De/para projeto × cliente, com a conclusão aplicada

| slug (repo) | workspace | id ws | projeto EE 3.0 | concluídas | inferidas |
|---|---|---|---|---|---|
| amado-galantini | Amado Galantini ADV | 147923 | `322371` | 26/30 | 2 |
| arx-cyber | Brasiline (ARX Cyber) | 148876 | `322467` | 14/30 | 2 |
| casa-flutuante | Casa Flutuante | 149800 | `324795` | **0/30 (não planejado)** | 0 |
| global-comercio-balancas | Global Comércio de Balanças | 147931 | `322374` | 27/30 | 2 |
| grupo-lamon | Lamon Peças Agrícolas | 147909 | `322375` | 27/30 | 2 |
| grupo-smk | GrupoSMK Log | 147912 | `322376` | 25/30 | 2 |
| ilha-service | Ilha Service | 147910 | `322377` | 24/30 | 2 |
| lilo-decor | Liló Decor | 147917 | `322379` | 24/27 | 2 |
| lucena-advisory | Lucena Advisory | 147907 | `322380` | 26/30 | 2 |
| luizy-souza | Consultora Luizy Souza | 147925 | `322381` | 27/30 | 2 |
| neo-solucoes | Neo Soluções | 147934 | `322382` | 25/30 | 2 |
| parana-control | FM Zahra | 147943 | `322383` | 26/30 | 2 |
| raizes-e-folhas | Raízes e Folhas | 147920 | `322384` | 7/27 | 1 |
| santua-confeccoes | Santuá Confecções | 147941 | `322385` | 27/30 | 1 |
| selva-acai | Selva Açai | 147913 | `322386` | 18/30 | 2 |
| vera-cruz-coworking | Vera Cruz Coworking | 147937 | `322388` | 24/30 | 1 |

`arx-cyber` (Brasiline) é o caso novo: o projeto `322467` foi criado em 2026-08-12 no workspace
`148876`, já **planejado** (30/30 tarefas com `currentDueDate`, `startDate` 2026-07-03), e
carrega alias `estruturação-e` e nome `Estruturação Estratégica 3.0 - Inside Sales` — fora do
padrão `EE3-<slug>` dos outros 14. **Não renomeamos** porque o alias `EE3-arx` ainda está preso
ao projeto inativo `322372`; decidir se libera o alias antes de normalizar.

### Como a conclusão foi decidida

Uma tarefa só foi concluída com **evidência no repo**. A regra, por tipo:

- **Entregável em `clientes/<slug>/outputs/`** — `ee-s1-swot.json` → `86897`,
  `ee-s1-auditoria-comunicacao.json` → `86898`, `ee-s1-persona-icp.json` → `86899`,
  `ee-s1-arquitetura-presenca.json` → `86900`, `ee-s2-pesquisa-mercado.json` → `86901`,
  `ee-s2-diagnostico-midia.json` → `86905`, `ee-s2-diagnostico-organico-ig.json` → `86906`,
  `ee-s2-diagnostico-criativos.json` → `86907`, `ee-s1-diagnostico-maturidade.json` → `86908`,
  `ee-s2-posicionamento.json` → `86909`, `ee-s2-diagnostico-cro.json` → `86911`,
  `ee-s4-cliente-oculto.json` → `86912`, `ee-s4-diagnostico-comercial.json` → `86913`,
  `ee-s3-is-metricas-funil.json` → `86914`, `ee-s3-is-pipeline.json` → `86915`,
  `ee-s3-crm-setup.json` → `86916`, `ee-s5-scripts-sdr.json`/`ee-s5-sdr-ia-config.json` →
  `86917`, `ee-s3-landing-page.json` → `86918`/`86953`,
  `ee-s3-manual-marca.json` (ou `ee-s3-brandbook.json`/`ee-s3-identidade-visual.json`) →
  `86920`, `ee-s3-copy-anuncios.json` → `86921`, `ee-s3-criativos-anuncios.json` → `86922`,
  `ee-s3-forecast-midia.json` → `86923`, `ee-s3-gmb-otimizacao.json` → `86952`, e os cinco
  `ee-s3-ecom-*.json` → `86936`, `86941`, `86942`, `86943`, `86945`.
- **Ata em `clientes/<slug>/base-de-conhecimento/`** — arquivo com `kickoff` no nome → `86894`;
  arquivo com `s1`/`s2`/`s3`/`s4` + `entrega`/`reuniao` → `86903` (1ª e 2ª semana), `86924`
  (3ª), `86919` (4ª); arquivo com `v4mos`/`formulario` → `86893`.
- **Inferência declarada** (2 tipos, 27 tarefas) — `86892` "Criar Grupo + Boas-Vindas"
  concluído onde existe ata de kickoff, e `86895` "Solicitação de acesso" concluído onde
  existem os diagnósticos de mídia paga **e** orgânico, que só se produzem com acesso
  concedido. Não é entregável; é dedução. **É o primeiro lugar a revisar** se algum número
  parecer otimista.

`raizes-e-folhas` fecha em 7/27 e `arx-cyber` em 14/30 porque a execução mesmo está atrasada,
não porque o mapeamento falhou: são 5 e 10 entregáveis no repo, respectivamente.

### Mecanismo: conclusão é `situation=30`, não mudança de fase

`update_task_phase` **não serve** para dar baixa nessas tarefas. Cada tipo do modelo EE 3.0 tem
**uma única fase ativa** no fluxo — `Execução Consultor [CN]` (88705) nos entregáveis,
`Entrega [CN]` (88703) nos 4 de onboarding. Não existe `Finalizado` no `flow[]` delas, então
não há para onde mover.

O que dá baixa é `update_task` com
`patchDoc: [{"op":"replace","path":"/situation","value":30}]`. Verificado: `accomplishedTasksCount`
do projeto sobe e `overduePlannedProjectTasksCount` cai. **`concludedDate` continua `null`** —
o MCP não grava data de conclusão nesse caminho, então não conte com esse campo para relatório.

### As 97 tarefas que continuam abertas — 2026-08-18

| tarefa aberta | clientes | nº |
|---|---|---|
| Reunião de Apresentação da Quarta Semana | amado-galantini, arx-cyber, global-comercio-balancas, grupo-lamon, grupo-smk, ilha-service, lilo-decor, lucena-advisory, luizy-souza, neo-solucoes, parana-control, raizes-e-folhas, santua-confeccoes, selva-acai, vera-cruz-coworking | 15 |
| Preenchimento do V4 Marekting | amado-galantini, arx-cyber, global-comercio-balancas, grupo-lamon, grupo-smk, ilha-service, lilo-decor, luizy-souza, neo-solucoes, parana-control, raizes-e-folhas, santua-confeccoes, selva-acai, vera-cruz-coworking | 14 |
| Reunião de Apresentação da Terceira Semana | amado-galantini, arx-cyber, grupo-lamon, grupo-smk, ilha-service, lucena-advisory, luizy-souza, neo-solucoes, raizes-e-folhas, selva-acai, vera-cruz-coworking | 11 |
| Cliente Oculto (Avaliação do Atendimento) | amado-galantini, arx-cyber, grupo-smk, ilha-service, lucena-advisory, neo-solucoes, selva-acai, vera-cruz-coworking | 8 |
| Reunião de Apresentação da Primeira Semana | grupo-smk, ilha-service, lilo-decor, lucena-advisory, neo-solucoes, parana-control, raizes-e-folhas, selva-acai | 8 |
| Reunião de Apresentação da Segunda Semana | arx-cyber, global-comercio-balancas, ilha-service, parana-control, raizes-e-folhas | 5 |
| 4 Criativos para Campanha | arx-cyber, raizes-e-folhas, selva-acai | 3 |
| Banco de Copy para Anúncios | arx-cyber, raizes-e-folhas, selva-acai | 3 |
| Forecast e Elaboração de Planejamento de Mídia (6 Meses) | arx-cyber, raizes-e-folhas, selva-acai | 3 |
| Manual de Marca Unificado (Brandbook + MIV) | arx-cyber, raizes-e-folhas, selva-acai | 3 |
| Criar Grupo com o Cliente + Boas-Vindas | santua-confeccoes, vera-cruz-coworking | 2 |
| Implementação de Landing Page | arx-cyber, selva-acai | 2 |
| Implementação ou Otimização de CRM | arx-cyber, selva-acai | 2 |
| Scripts SDR AI-First (com fallback humano) | arx-cyber, selva-acai | 2 |
| Definição de Métricas e Critérios do Funil | arx-cyber | 1 |
| Diagnóstico Comercial e Etapas do Funil | arx-cyber | 1 |
| Diagnóstico Orgânico (Redes Sociais) | raizes-e-folhas | 1 |
| Diagnóstico da Base Ativa e Controle de Vendas | raizes-e-folhas | 1 |
| Diagnóstico de CRO (Site/LP) | arx-cyber | 1 |
| Diagnóstico de Criativos | raizes-e-folhas | 1 |
| Diagnóstico de Experiência do PDV | raizes-e-folhas | 1 |
| Diagnóstico de GMN (Google Meu Negócio / Perfil da Empresa) | raizes-e-folhas | 1 |
| Diagnóstico de Maturidade Digital | raizes-e-folhas | 1 |
| Diagnóstico de Mídia Paga | raizes-e-folhas | 1 |
| Diagnóstico ou Implementação de Landing Page | raizes-e-folhas | 1 |
| Pipeline Comercial + Réguas + Script Consultivo | arx-cyber | 1 |
| Posicionamento Estratégico + PUV + Taglines | raizes-e-folhas | 1 |
| Reunião para alinhamento e Cronograma [KickOff] | vera-cruz-coworking | 1 |
| Régua de WhatsApp e Fluxo de Loja (Pré, Durante, Pós-visita) | raizes-e-folhas | 1 |
| Solicitação de acesso de canais e ferramentas do cliente | raizes-e-folhas | 1 |

Eram 113 em 12/08. Saíram 15 na passada de 18/08 (7 entregáveis de S3/S5 em `lucena-advisory`
e 7 em `neo-solucoes`, mais a reunião de 2ª semana da Lucena, cuja ata já existia e escapou da
primeira varredura porque `Primeira` e `Segunda Semana` compartilham o tipo `86903`) e 1 na
conclusão avulsa de `santua-confeccoes`.

Três leituras que valem ação da operação:

1. **"Reunião de Apresentação da Quarta Semana" está aberta nos 15 projetos** e "Terceira
   Semana" em 11. Não existe nenhuma ata de S4 no repo. Ou as reuniões não aconteceram, ou
   acontecem sem registro — e nesse caso o repo não serve como fonte de verdade para elas.
2. **"Preenchimento do V4 Marekting" está aberta em 14 de 15** (só `lucena-advisory` tem
   `2026-05-25-formulario-v4mos.md`). O título tem typo no próprio tipo `86893` no eKyte.
3. **`santua-confeccoes` e `vera-cruz-coworking` não têm ata de kickoff no repo** — só
   `passagem-bastao`/`call-vendas` —, então boas-vindas segue aberto nos dois e o kickoff na
   `vera-cruz-coworking`, mesmo com 27 e 24 entregas concluídas. É lacuna de registro, quase
   certamente não de execução.

## Casa Flutuante (2026-08-21)

O 25º cliente do repo, cadastrado em `clientes/casa-flutuante/` em 2026-08-17, não tinha nada no
eKyte. Foi criado nesta data:

| item | id | observação |
|---|---|---|
| workspace | `149800` | nome `Casa Flutuante`, `externalId: "casa-flutuante"`, `access=0` |
| projeto | `324795` | alias `EE3-casaflut`, clonado de `320045` (Inside Sales), `startDate` 2026-08-03 |

**As 30 tarefas nasceram não planejadas e por isso não deu para dar baixa em nenhuma.** Isso
confirma ao vivo o achado já registrado em [Projetos](#projetos--modelos-da-matriz-estão-fora-de-uso):
tarefa de projeto clonada não é tarefa. Os sintomas, todos verificados no `324795`:

- `list_project_tasks` devolve as 30 com ids numa faixa própria (`3089959` a `3089988`), não na
  faixa de taskId (`10.1M`);
- `get_detailed_task` com esses ids devolve `{}`;
- `list_tasks` do workspace `149800` devolve `[]`;
- `update_task` com `situation=30` devolve `{"id": 10, "text": "A tarefa não foi encontrada."}`;
- `unplannedProjectTasksCount` fica em 30 e `plannedProjectTasksCount` em 0.

**Passar `startDate` no clone não planeja.** O `324795` foi criado com `startDate: 2026-08-03` e
mesmo assim veio 30/30 não planejado. Os outros 15 projetos aparecem planejados porque alguém
planejou na UI depois, não por causa do parâmetro.

Não existe tool de planejamento entre as 94: `update_project` só aceita `/name`, `/alias`,
`/description`, `/startDate`, `/endDate`, `/active`, `/createdById`, `/workspaceId`, `/avatarId`,
`/artifacts`, `/budgetCalculationMethod` e `/hourlyBudget`. **Planejar é passo obrigatório de UI.**

### As 8 tarefas a concluir assim que o projeto for planejado

Aplicando a mesma regra de evidência das outras 15 conciliações:

| tipo | tarefa | evidência no repo |
|---|---|---|
| 86892 | Criar Grupo com o Cliente + Boas-Vindas | inferência: existe ata de kick-off |
| 86894 | Reunião para alinhamento e Cronograma [KickOff] | `2026-08-06-kickoff-resumo.md` e `-transcricao.md` |
| 86897 | Análise de Concorrente e SWOT Estratégica | `outputs/ee-s1-swot.json` |
| 86898 | Auditoria de Comunicação no Digital | `outputs/ee-s1-auditoria-comunicacao.json` |
| 86899 | Persona & ICP | `outputs/ee-s1-persona-icp.json` |
| 86900 | Arquitetura de Presença Digital | `outputs/ee-s1-arquitetura-presenca.json` |
| 86901 | Pesquisa de Mercado (TAM/SAM/SOM + Marketshare) | `outputs/ee-s2-pesquisa-mercado.json` |
| 86903 | Reunião de Apresentação da Primeira Semana | `2026-08-17-entregas-s1-transcricao.md` |

A lista está repetida na `description` do projeto `324795`, que é o único lugar do eKyte onde ela
sobrevive enquanto as tarefas não existem.

**`86895` (Solicitação de acesso) fica aberta de propósito.** A inferência usada nos outros
projetos, de que acesso foi concedido quando existem os diagnósticos de mídia paga e orgânico,
não se aplica: os dois diagnósticos não existem, e a reunião de 17/08 registrou a coleta de
acessos como próximo passo do Leonardo. `86893` (V4 Marketing) também segue aberta, sem arquivo.

## `externalId` — a chave que resolve o de/para de vez

`create_workspace` e `update_workspace` aceitam **`externalId`**, um identificador livre para
sistema integrado. **Grave o slug da pasta do repo nele.** Foi o que fizemos em
`Brasiline (ARX Cyber)` (`externalId: "arx-cyber"`).

Com isso o de/para deixa de depender de semelhança de nome — que já falhou três vezes hoje —
e passa a ser consulta direta. Os outros 22 workspaces estão com `externalId: null`; vale
preencher todos numa passada, usando esta tabela como fonte.

## Pendências que travam a ação em massa

**`cheirin-bao-shopping-via-sul` está fora de escopo** por decisão da operação em 2026-08-10 —
não deve ser vinculado nem receber projeto.

**2 clientes sem `modelo_venda`**, o que impede escolher o modelo de projeto:
`jioji-cavalera` (campo vazio) e `infinit-telecom` (não tem `client.json` — só a pasta).

**1 divergência de nome que pode ser rebrand:** a pasta e o workspace dizem `Selva Açai`,
mas o `client.json` diz `meta.name: "Amazu"`. Confirmar qual é o nome vigente antes de
renomear o workspace.

## Grafias divergentes

Valem normalização no eKyte, e explicam por que o casamento automático por nome não funciona:

| repo | eKyte | observação |
|---|---|---|
| Bantur Viagens | `Ban Tur VIagens` | separado e com typo (`VIagens`) |
| Petterson Representações | `Petterson Representacoes` | sem cedilha nem til |
| Infinit Telecom | `Infiniti Telecom` | `Infinit` vs `Infiniti` |
| Grupo SMK | `GrupoSMK Log` | junto, com sufixo |
| Amado & Galantini | `Amado Galantini ADV` | sem `&`, com sufixo |
| Vital Glass | `Grupo Vital (Vital Glass)` | invertido |
| Neo Soluções Empresariais | `Neo Soluções` | truncado |
| Lamon Peças Agrícolas | `Lamon Peças Agrícolas` | o repo usa slug `grupo-lamon` |

## 22 workspaces do eKyte sem cliente no repo

Art das Malhas · Capta EAD · Castelinho SPA · Cervejaria Germânia · Clinica Veterinaria
Zenvet · Cogno Psiquiatria · Comvida Soluções · Flora Barigui · Hortifruti 9 de Julho ·
Ice Dream Gelo · Ju Ribeiro Confecções · Lider Gas · Liderplan (Grupo Líder) · Maria Biju ·
Mender Pro · NW DRONES · Panobianco · Peças Cummins · Sushi Carvalho · TruckMe ·
Vertical House · Vincenzo Pizzaria

Atenção: esta lista **não é confiável como "não é cliente da EE"**. `FM Zahra` e `Tapparo
Industria` estavam aqui até 2026-08-10, quando a operação revelou que são Paraná Control e
Bombachas Farroupilha. Qualquer nome desta lista pode ser um cliente do repo sob outra razão
social. Confirme com a operação antes de tratar como órfão.

Vieram da carga em massa do `Workspace em massa - modelo-workspaces-ekyte.csv`. Não têm
contrapartida em `clientes/` — ou são de outra cadeira, ou nunca entraram na Estruturação
Estratégica. Não devem ser alvo de clone de projeto EE 3.0 sem confirmação.
