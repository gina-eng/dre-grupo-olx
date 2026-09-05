# Sprint dos diagnósticos · 09 a 23/09

Replanejado em **04/09/2026**. A entrega de acessos prometida para as 17h de 03/09 **não ocorreu**.
Em reunião de alinhamento sobre a estrutura de GA4 e GTM, a equipe responsável da OLX se
comprometeu a passar a **atualização dos acessos na terça, 08/09**, o que desbloqueia os nove
diagnósticos de uma vez.

> Este documento substitui o `sprint-diagnosticos-04-a-18-09.md`, que assumia entrega em 03/09.
> Ele **não substitui** o [cronograma do Ciclo 1](cronograma-e-marcos.md), detalha, em dias, a
> janela em que a granularidade semanal não serve.

---

## O tamanho real da janela

| | |
|---|---|
| Atualização dos acessos | terça, **08/09/2026**, comprometida pela equipe da OLX |
| Início dos diagnósticos | quarta, **09/09/2026** |
| Fechamento dos nove | quarta, **23/09/2026** |
| Prazo declarado | **15 dias corridos** |
| **Dias úteis dentro deles** | **11**: 09, 10, 11, 14, 15, 16, 17, 18, 21, 22 e 23 |
| Apresentação dos diagnósticos | terça, **29/09/2026** |
| **Comitê 1** | terça, **06/10/2026** |

**O atraso de cinco dias corridos custou menos do que parece:** o feriado de 7 de setembro saiu de
dentro da janela, que ganhou **um dia útil**, passou de 10 para 11. O que escorregou foi a data de
início, não a capacidade de trabalho.

---

## Onde estamos hoje, 04/09

Nem tudo está parado. Com o que já foi concedido, GA4 em leitura, uma conta de GTM com 11 exports,
a MCC de Google Ads e o data room, **quatro diagnósticos avançam** e **quatro estão totalmente
parados**.

| Diagnóstico | Hoje | O que falta para fechar |
|---|---|---|
| **(vii) Rastreamento** | 🟡 Avança, 5 dos 11 exports ainda na fila de auditoria | As 3 contas de GTM nunca lidas: `Checkout Unificado - PRO`, `VivaReal` e o resto da `ZapImóveis` |
| **(ii) CRO e SEO** | 🟡 Avança, a camada pública dos 5 domínios B2B não pede acesso a ninguém | Google Search Console |
| **(viii) Páginas de captura** | 🟡 Avança, inventário de LPs e conversão por página saem do GA4 | Mouseflow e Unbounce |
| **(vi) Mídia paga** | 🟡 Avança, o mapa de contas já é o achado | As 2 contas de Meta e a conta de Google Ads da captação de anunciante |
| **(ix) Pré-vendas** | 🔴 Parado | CRM, cadências e 10–15 gravações com consentimento |
| **(i) CRM Marketing** | 🔴 Parado | Salesforce Marketing Cloud |
| **(v) Redes sociais** | 🔴 Parado | Meta Business Suite e LinkedIn |
| **(iv) Criativos** | 🔴 Parado | Contas de Meta e a biblioteca de 6–12 meses |
| **(iii) GEO** | ⚪ Disponível, não decisivo | Nada. Fecha por último por escolha |

> **Nenhum dos quatro que avançam fecha antes de 08/09.** Todos param na mesma parede: falta o
> acesso que dá a camada onde mora a causa, não o sintoma.

---

## O que muda no critério de priorização

A sprint anterior ordenava a janela por **habilitação**, valia o que fechava com o acesso que já
existia. Com o lote completo, esse critério perde a função: **os nove passam a estar habilitados ao
mesmo tempo**.

O que ordena a janela agora volta a ser a lógica original do método, a investigação
**de baixo para cima** no fluxo de ganho
([Regra de Goldratt](../00-playbook/01-fundamentos-dr-ote.md#lógica-de-investigação-de-baixo-para-cima)),
com um segundo filtro que agora é o binding:

> **Hora do time da OLX.** O gargalo desta janela deixou de ser acesso e deixou de ser hora da V4.
> Passou a ser a agenda de quem, do lado da OLX, precisa dar entrevista, liberar gravação e validar
> achado.

Por isso a grade abaixo separa os nove em **dois grupos pelo custo que impõem ao cliente**, e não
pela ordem de contrato.

---

## Os nove na janela

### Grupo 1 · custo baixo de hora do cliente: abre em 04/09

| # | Diagnóstico | Janela | O que consome da OLX |
|---|---|---|---|
| **vii** | Rastreamento (GA4/GTM) | 09–14 set | Só os exports das 3 contas de GTM que faltam. A análise já está 80% escrita |
| **ii** | CRO/SEO · domínios B2B | 09–15 set | Search Console. A camada pública já rodou e não custa nada |
| **viii** | Páginas de captura | 09–18 set | Export do Unbounce e acesso ao Mouseflow. Leitura é da V4 |

### Grupo 2 · custo alto de hora do cliente: entra escalonado

| # | Diagnóstico | Janela | O que consome da OLX |
|---|---|---|---|
| **vi** | Mídia paga (Google e Meta) | 10–21 set | Mapa de contas e finalidade de cada uma. Depende de ingestão no V4MOS |
| **ix** | Pré-vendas e qualificação | 10–23 set | **Entrevistas + gravações de call com consentimento.** O mais caro dos nove |
| **i** | CRM Marketing (Salesforce MC) | 14–22 set | Entrevista com o time de automação; leitura de jornadas |
| **iv** | Criativos e mensagens | 16–22 set | Entrega do acervo de peças e do racional de campanha |
| **v** | Redes e conteúdo orgânico | 16–22 set | Business Suite e LinkedIn concedidos; pouca entrevista |
| **iii** | GEO · buscas generativas | 21–23 set | Nada. Roda de fora, e fecha por último por depender do posicionamento |

### Carga em paralelo: a regra que este plano quebra

O método limita a **três diagnósticos abertos por vez**, e a regra existe justamente para proteger a
agenda do cliente. Nesta janela ela não é cumprida:

| Pico no período | 09–11/09 | 14–15/09 | 16–18/09 |
|---|---|---|---|
| Abertos ao mesmo tempo | 4 | 5 | **6** |
| **Que cobram hora da OLX** | 3 | 4 | **5** |

Nos dias 16, 17 e 18/09 há **cinco frentes simultâneas de cobrança** sobre o time do Grupo OLX, contra o
teto de três do método. Isso é consequência direta do prazo de 15 dias e está registrado aqui como
decisão consciente, não como descuido de planejamento.

**A mitigação é de concentração, não de redução:** as entrevistas de (ix), (i) e (iv) são agendadas
em **dois blocos fechados**, quarta 16 e quinta 17, em vez de espalhadas pela semana. O pico de carga
e os blocos caem no mesmo dia de propósito: uma agenda tomada por duas manhãs é mais barata para o
cliente do que cinco frentes cutucando todo dia durante uma semana.

---

## O plano, dia a dia

| Dia | V4 executa | O que precisa vir do Grupo OLX |
|---|---|---|
| **sex 04/09** | Avança (vii) pelos 5 exports na fila, (ii) pela camada pública, (viii) pelo inventário de LPs no GA4 e (vi) pelo mapa de contas | - |
| **seg 07/09** | *Feriado da Independência* | - |
| **ter 08/09** | Conferência do lote, **abrindo cada ferramenta**, não lendo o e-mail de concessão | 🔴 **Atualização dos acessos.** E o **dono da revisão de qualidade definido**, sem o qual não há revisão em 28/09 |
| **qua 09/09** | Abre (viii) e retoma (vii) e (ii) com as contas de GTM e o Search Console | Escalar no mesmo dia o que vier em nível insuficiente |
| **qui 10/09** | Abre (vi) com as contas certas e (ix) pelo desenho da coleta | Autorização às gravações e confirmação do trâmite de consentimento |
| **sex 11/09** | Ingestão das contas de mídia no V4MOS. **Reporte escrito semanal** | - |
| **seg 14/09** | Fecha (vii). Abre (i) | - |
| **ter 15/09** | Fecha (ii). (ix) e (i) em profundidade | Acervo de criativos entregue |
| **qua 16/09** | **Bloco de entrevistas 1.** Abre (iv) e (v) | Time de pré-vendas e de CRM disponível |
| **qui 17/09** | **Bloco de entrevistas 2** | Time de conteúdo e de mídia disponível |
| **sex 18/09** | Fecha (viii). **Reporte escrito semanal** | - |
| **seg 21/09** | Fecha (vi). Abre (iii) | Validação dos achados que precisam de confirmação factual |
| **ter 22/09** | Fecha (i), (iv) e (v) | - |
| **qua 23/09** | Fecha (ix) e (iii). **Os nove fechados** | - |
| **qui 24 · sex 25/09** | Consolidação causal: score das 8 travas e trava governante candidata | - |
| **seg 28/09** | **Revisão de qualidade** do material da apresentação | - |
| **ter 29/09** | **Apresentação dos diagnósticos**, presencial | Decisores presentes: Mirella Mendonça, Dener Lippert, Gustavo Figueiredo |
| **qua 30/09 a sex 02/10** | Árvore da Realidade Atual sobre as UDEs colhidas nas entrevistas. Nuvem de Conflito e injeção | Confirmação dos efeitos indesejados que a CRT usar |
| **seg 05/10** | **Matriz aprovada**: gate obrigatório, bloqueio duro da regra 4 | - |
| **ter 06/10** | **Comitê 1 · Validação e Otimização** | Decisor presente. Sai com a restrição nomeada em ata e o plano de 30 dias com DRI |

---

## Os três riscos desta janela

**1. O acesso pode chegar concedido e não utilizável.** É o risco mais provável, porque já aconteceu
duas vezes: o GA4 veio em nível Leitor, que sustenta diagnóstico de sintoma mas não abre as telas de
Administração onde mora a causa; e o portfólio Meta apareceu sem ativo conectado. A conferência de
08/09 é feita abrindo cada ferramenta, e o que vier em nível insuficiente é escalado **no mesmo dia**,
não na semana seguinte, porque não há semana seguinte sobrando.

**2. (ix) Pré-vendas tinha três semanas de janela por um motivo, e agora tem dez dias úteis.** A janela
original era longa porque gravação de call envolve consentimento e LGPD, e esse trâmite não acelera
com pressão de cronograma. É o único dos nove cujo prazo depende de um processo jurídico do cliente.
Se ele escorregar, (ix) fecha sem a camada experiencial e isso entra como limitação declarada, a
Trava de Qualificação fica pontuada só pela camada analítica, o que sustenta uma nota, mas
[não sustenta nota acima de 3](../CLAUDE.md).

**3. A revisão de qualidade não tem dono.** O método exige que o material de comitê seja validado
por **alguém que não participou da análise**, é a única proteção contra material fraco chegar ao
Board, numa conta que compra exatamente rigor metodológico. São **duas revisões**: 28/09 para a
apresentação e 05/10 para a Matriz do Comitê 1, esta com bloqueio duro pela regra 4 do repositório.
Definir o revisor até **08/09** ([pendência 8](../PENDENCIAS.md)).

> ⚠️ **O que este plano não resolve.** O **bloco A**, Visão de Negócio e Fluxo de Receita, não é
> acesso a ferramenta, é entrega de dado, e segue sem nenhum item recebido. Nenhuma concessão de 17h
> o destrava. Sem A1–A3 não há mapeamento do fluxo de receita e não há matemática de forecast, e isso
> vale igual com os nove diagnósticos fechados. Pedir junto com a conferência de 08/09.
