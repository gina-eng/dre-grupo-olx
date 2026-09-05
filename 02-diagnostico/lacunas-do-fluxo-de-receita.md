# Lacunas do fluxo de receita: caderno vivo

Caderno de campo do mapeamento. **Cresce a cada material que a OLX apresenta** e só fecha quando o
`mapeamento-fluxo-receita.md` tiver volume, taxa e tempo em cada etapa.

Duas listas: **L** = o que falta ou está errado no fluxo · **F** = o que entra ou muda no
[formulário de kick-off](../portal/assets/form-data.js).

| Origem | Material | Registro |
|---|---|---|
| 28/08 | Jornada do cliente profissional, 6 etapas | [jornada-do-cliente-profissional.md](jornada-do-cliente-profissional.md) · original versionado |
| 28/08 | **FLUXOS: Autos & Imóveis**, três versões do diagrama de canais | esta página · ⚠️ arquivo-fonte não versionado (**L28**) |
| 28/08 | **Transcrição da sessão**, 01:05:30, com nome em cada fala | [2026-08-28-jornada-do-cliente-transcricao.md](../06-reunioes/2026-08-28-jornada-do-cliente-transcricao.md) |

**Placar após a transcrição:** 6 lacunas fechadas · 6 avançaram · 16 novas. O caderno cresceu
porque o material é bom: quanto mais preciso o mapa, mais visível o que falta nele.

---

## 1. O diagrama de FLUXOS reconcilia: e isso é um achado

A terceira versão do slide traz a decomposição por canal, e **a aritmética fecha nó a nó**:

| Conta | Confere |
|---|---|
| CRM 29% = 27% (com campanha → WhatsApp) + 2% (→ LPs) | ✅ |
| Direto 36% = 26% (sem campanha) + 10% (→ LPs) | ✅ |
| 26% sem campanha = 15% (WhatsApp) + 3% (Telefone) + 8% (Outros) | ✅ |
| LPs MKT 41% = 2 + 10 (Direto) + 16 (Pago) + 5 (Orgânico) + 1 (Outros) + 7 (Canal Pro) | ✅ |
| Mix de canais: 29 + 36 + 16 + 5 + 11 | **97%** |
| Canais de entrada: WhatsApp 42 + Telefone 3 + Outros 8 + Formulário 44 | **97%** |

Um mapa que fecha em dois caminhos independentes no mesmo 97% não é chute: é leitura de sistema.
**Isso resolve L7 e sobe muito a confiança no material.** Restam os 3 pontos de diferença (**L29**).

## 2. O maior canal do mapa é um artefato de mensuração

O próprio slide traz duas anotações de alerta, ambas apontando para **Direto**:

> **!** *Teste de campanha paga para WhatsApp, **entra tudo como Direto***
> **!** *Perde atribuição: **entra tudo como Direto***, usuário tem o contato salvo ou chama pelo
> número, e não clica no link

Consequência direta: **Direto (36%) é o maior canal do mapa e está inflado por mídia paga**, e
**Pago (16%) está subestimado na mesma proporção**. Enquanto isso durar, CAC por canal não existe,
qualquer decisão de realocação de verba é cega, e o teste de campanha paga para WhatsApp não pode
ser lido, ele se esconde dentro do canal que deveria medi-lo.

Isso é **Trava de Cegueira com evidência formal**, documentada pelo próprio cliente no material que
ele apresentou. Nota acima de 3 no score de trava exige evidência formal: aqui ela existe.

---

## L · Fluxo de receita

### Fechadas nesta sessão

| # | Estava aberto | Resposta, com fonte |
|---|---|---|
| **L7** | Atribuição dos percentuais aos canais | A terceira versão do slide decompõe e a aritmética fecha (§1). Barras = mix de MQL por canal; setas = destino |
| **L8** | "Vitrine apenas ZAP/VR" | Imóveis tem plataforma separada (**Canal Pro**), com cadastro e senha, acessível só após pagar. Em Autos a jornada roda dentro do login OLX que o usuário já tem, com POS **MyPlan**, Leonardo Costa, 00:30:12 e 00:37:08 |
| **L10** | MQL e SQL sem definição | **MQL** = dados básicos: nome, e-mail, telefone, em alguns canais documento. **SQL** = elegibilidade comercial, em Imóveis só se vende para imobiliária e corretor, exige CNPJ do setor. Fluxo refinado há ~4 meses, automatizado por bot, reaproveita histórico de inativo, Carolina e Michelle, 00:44:38 |
| **L11** | Incentivos na área logada: aquisição ou expansão? | **Expansão.** Michelle, 00:36:13: *"aqui a gente está falando essencialmente de clientes que já são nossos… é muito mais um upgrade, uma venda one shot de um destaque, cota para festival. Aqui a gente não fala muito em aquisição"* |
| **L12** | O que compõe "Outros" | Canal Pro (área logada de Imóveis), MyPlan (área logada de Autos), **eventos**, o time de trade é forte, e fontes pequenas. Michelle, 00:35:02 |
| **L13** | O que é POS | **Point of sale online**: login → vitrine → checkout. Existe POS de MyPlan em Autos. Michelle, 00:33:44 |

### Avançaram

| # | O que mudou | O que ainda falta |
|---|---|---|
| **L1** | **Confirmado como achado.** Carolina, 00:05:42: *"50% da base chega por prospecção comercial"*. O dashboard abre por times comerciais, mas o diagrama de canais continua sem a prospecção | O desenho do caminho da prospecção ativa, com etapas próprias |
| **L2** | Existe pós-venda: jornada de boas-vindas, 10 vídeos educacionais gravados, GT de onboarding para atacar o churn imediato. Login agora só depois de pagar | O desenho das etapas e as taxas de cada uma |
| **L3** | Os dashboards filtram por vertical, autos, goods, imóveis | O fluxo desenhado separado por vertical |
| **L5** | O dashboard olha **12 meses** por padrão, com filtro de período. O slide diz "todo o período histórico" | Reconciliar: os percentuais do slide são de 12 meses ou de tudo? |
| **L6** | **As taxas existem.** O dashboard tem taxa de qualificação (MQL→SQL), conversão em vendas (SQL→venda), volumetria diária e receita, por canal e por vertical, Lu Machim, 00:07:00 a 00:08:59 | Deixou de ser coleta e virou **extração**. Depende dos links dos dashboards |
| **L9** | **Tem dono.** O investimento de mídia **não está** no dashboard. Mirella, 00:10:08: *"isso é outro controle que a gente tem"* | O controle da Mirella. Sem ele não há CAC por canal, e com **L15** ele nem assim fecha |

### Novas

| # | Achado ou lacuna | Por que importa |
|---|---|---|
| **L15** | **Direto (36%) inflado por mídia paga sem atribuição** (§2) | A maior fatia do mapa não é um canal, é um buraco de mensuração. Trava de Cegueira com evidência formal |
| **L16** | **Conflito no registro sobre transbordo.** O slide diz *"apenas ZAP/Viva Real"*; na transcrição Carolina responde *"não é só imóveis"* e a conversa termina com Michelle concluindo o contrário, 00:43:40 | O transbordo de carrinho abandonado vale 17% da entrada. Saber se existe em Autos muda o desenho |
| **L17** | **O 12% sem publicar é média, e as pontas são muito distantes**: até **20%** no canal online, **8–10%** em inside e field sales. Leonardo Costa estima que 80–90% dos 12% vêm do online, 00:15:30 | O vazamento é do autosserviço, não da venda assistida. Muda onde se age |
| **L18** | **Definição de churn contra-intuitiva:** cliente que paga e não usa **não** é churn, é inativo gerando receita, Carolina e Leonardo Rosa, 00:22:16 | Os 8–10% medem interrupção de pagamento, não abandono. A insatisfação silenciosa não aparece na métrica |
| **L19** | **Esquecimento explica 20% dos *atrasos*, não do churn**, Carolina, 00:22:16 | O slide da jornada sugere o contrário ao pôr "boleto facilita esquecimento" na caixa de churn |
| **L20** | **Metade da base paga por boleto**, ~40% cartão, resto Pix, e **não há diferenciação de preço por meio de pagamento**, *"a gente sabe que deveria, mas hoje não"* | Meio de pagamento é alavanca de retenção não usada. Iuna já decidiu: cliente pequeno só cartão ou Pix; migração compulsória de crônico em atraso em avaliação; mudança estrutural só em 2027 |
| **L21** | **Ticket de Imóveis acima de R$ 50 mil não cabe no cartão**: plano periódico de 3, 6 ou 12 meses com desconto progressivo de ~20%, 01:03:19 | O meio de pagamento bloqueia justamente a venda de maior valor e maior compromisso |
| **L22** | **Não existe upgrade self-service.** Todo adicional passa por humano, Michelle, 00:41:15 | A expansão, que é o crescimento mais barato que existe, depende de capacidade humana |
| **L23** | **Destaque está saturado e é a demanda nº 1 de upgrade.** Leonardo Costa: lá fora 50% da receita de marketplace vem de destaque, e o balanceamento da OLX é bem diferente, 00:59:26 | Há debate interno de reempacotamento (plano recorrente × SVA não recorrente) e de tornar destaque escasso. Toca direto a alavanca de expansão |
| **L24** | **Canibalização privado × profissional**, via fluxo *Sweet Step*. A OLX testa reduzir a gratuidade de Autos de 4 para 2 anúncios/ano, Iuna, 00:52:15 | Receita profissional vazando para o gratuito. Muda a contagem da base endereçável |
| **L25** | **App não é incentivado no B2B.** Autos: 60–70% usam o app OLX. Imóveis: 20–30% usam o app Zap/VivaReal. Nenhum touch point de ativação | Canal de engajamento com adoção assimétrica e sem gestão |
| **L26** | **A entrega ao cliente é medida por proxy.** Marcação de vendido raramente vem de integrador; em Imóveis é pior, porque n imobiliárias anunciam o mesmo imóvel. Proxy da OLX: **3 leads em 7 dias**. Em Imóveis não há número, 00:53:50 | Se baixa performance é o principal motivo de churn, e performance é medida por proxy, **a causa declarada do churn não é medida diretamente** |
| **L27** | **O arquivo da jornada está no Drive**: Carolina, 01:04:33 | Buscar e versionar o original em vez de depender de captura de tela |
| **L28** | O slide de FLUXOS não veio como arquivo, só como imagem | Mesma coisa: pedir o original |
| **L29** | O mix fecha em **97%**, nos dois caminhos | Faltam 3 pontos. Pode ser arredondamento ou canal não rotulado |
| **L30** | O Formulário recebe 24% + 3% + 17% | Conferir se o transbordo é subconjunto dos 41% ou entrada adicional |

---

## F · Formulário

### Já respondidas pela sessão: atualizar o formulário

| Bloco | Pergunta que fecha | Resposta |
|---|---|---|
| 04 | Estágios do pipeline e definição objetiva | MQL e SQL definidos, ver **L10** |
| 04 | Estrutura do time comercial | Inside sales e field sales, field focado em cliente de maior valor; up, down e cancelamento só via time comercial |
| 3B | O que faz a fatura crescer | Destaque, espaços adicionais, cotas de festival de autos e de imóveis |
| 3B | O que define cliente ativo e como uma conta morre | Renovação automática; pré-pago morre por não pagar; pagar e não usar **não** é churn, ver **L18** |
| 05 | Quais são os canais e o peso de cada um | Os cinco canais com mix, ver §1 |
| 06 | Onde vive o dado do funil | Dashboards de funil B2B e de canal online, processados às 3h, com filtro por vertical, canal, time e período |
| 01 | Ponto focal | **Leonardo Rosa** assumiu como consultor focal; Michelle aciona direto no grupo, 00:58:27 |

### A acrescentar

| # | Bloco | Pergunta | Nasce de |
|---|---|---|---|
| **F1** | 04 | "Onde entra a prospecção ativa no fluxo desenhado?" | L1 |
| **F3** | 04 | "Qual é o desenho de pós-venda: publicação, entrega de lead, renovação?" | L2 |
| **F4** | 05 | "Investimento mensal por canal, últimos 12 meses", o controle está com a Mirella, fora do dashboard | L9 |
| **F10** | 03 | "A mesma visão de canais em 12 meses com corte mensal, e o mix fechando 100%" | L5, L29 |
| **F11** | 02 | "O fluxo pode ser separado por vertical?" | L3 |
| **F12** | 06 | **"Quanto do canal Direto é campanha paga sem atribuição? Dá para dimensionar?"** | L15 |
| **F13** | 04 | "Qual proxy mede a entrega ao cliente em cada vertical, e por que Imóveis não tem?" | L26 |
| **F14** | 3B | "Qual a participação de destaque e SVA não recorrente na receita, por vertical?" | L23 |
| **F15** | 04 | "Por que não existe upgrade self-service, e o que bloqueia?" | L22 |
| **F16** | 02 | "Qual o tamanho da canibalização privado × profissional, e quanto o teste de gratuidade recupera?" | L24 |
| **F17** | 3B | "Meio de pagamento entra na precificação? Qual o plano para o ticket acima de R$ 50 mil?" | L20, L21 |
| **F18** | 04 | "Existe transbordo de carrinho abandonado em Autos, ou só em ZAP/VivaReal?" | L16 |
| **F19** | 04 | "A taxa de não publicação por canal: 20% no online contra 8–10% no assistido, confirma?" | L17 |

---

## Como alimentar este caderno

1. Material novo → linha na tabela de origem, com onde o original está versionado.
2. Lacuna nova ganha ID **L**; a pergunta correspondente ganha **F**, com referência cruzada.
3. Lacuna que vira compromisso com DRI e prazo **sai daqui** e vira linha de
   [PENDENCIAS.md](../PENDENCIAS.md). Este caderno é o que ainda não tem dono.
4. IDs nunca são reciclados. Fechada, a lacuna migra para a tabela de fechadas com a fonte.
