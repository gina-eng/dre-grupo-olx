# Publicação

## Portal (canônico)

**<https://portal-dre-grupo-olx.vercel.app>** — protegido por senha.

| | |
|---|---|
| Usuário | qualquer coisa (o middleware só confere a senha) |
| Senha | guardada no gerenciador de senhas; no projeto vive como a variável `PORTAL_SENHA` |
| Projeto Vercel | `portal-dre-grupo-olx`, escopo `gina-6479s-projects` |

Duas camadas, verificadas ponta a ponta:

- **Alias de produção** (`portal-dre-grupo-olx.vercel.app`) → Basic Auth via `middleware.js`.
  É este o link que vai para o Grupo OLX.
- **URLs brutas de cada build** (`portal-dre-grupo-xxxxx-....vercel.app`) → SSO da Vercel.
  Só a conta dona abre. Um link de build vazado não serve para nada.

Password protection nativa da Vercel exigiria o add-on *Advanced Deployment Protection*, que não está
habilitado nem no escopo pessoal nem no time V4 Company — daí o middleware.

### Trocar a senha

```bash
cd portal
vercel env rm PORTAL_SENHA production
printf 'nova-senha' | vercel env add PORTAL_SENHA production
vercel deploy --prod
```

O deploy é necessário: a variável só é lida no build do middleware.

### Republicar

```bash
cd portal
python3 build.py     # se mexeu em _src/ ou nos dados
vercel deploy --prod
```

## Versões em artifact (sem senha)

Publicadas antes do portal. Continuam válidas e são a saída para quando não dá para pedir que alguém
digite senha. Nascem privadas — compartilhar exige ação explícita no menu de cada página.

| Material | Link |
|---|---|
| Formulário de Kick-off | <https://claude.ai/code/artifact/ba21bc7f-17bf-4d09-a9c4-1b91700fdea0> |
| Cronograma de 12 meses | <https://claude.ai/code/artifact/620fdf4e-9ea2-4491-8512-1b3aac924070> |
| Dicionário de Métricas | <https://claude.ai/code/artifact/3330df62-0d81-40b7-8c0f-ddd5090a61a4> |

> O formulário é **interno**. Ele contém o bloco de pendências contratuais, com os valores do contrato
> e a divergência de R$ 12.000. Não compartilhar com a OLX.

## O que cada módulo é

**Painel** — status do ciclo calculado na hora, as três portas e o quadro do que precisa fechar no
kick-off. A porta do kick-off mostra quantas respostas já existem no navegador de quem está olhando.

**Kick-off** (interno) — 88 perguntas em 11 blocos e o checklist dos dez blocos de dados com
responsável e prazo. Cada pergunta declara o que alimenta. Exporta a ata em Markdown para
`06-reunioes/` e para a skill `/dre-onboarding`.

**Cronograma** (cliente) — 4 ciclos de 12 semanas, 24/ago/26 → 23/jul/27, com 4 semanas de reserva.
Fecha duas pendências: **12 comitês** = 3 por ciclo × 4 ciclos, e os **4 presenciais** são o Comitê 2
de cada ciclo. Datas propostas: 17/set, 08/out e 12/nov/2026. Mapeia os riscos de calendário — o
Ciclo 1 perde três segundas (07/set, 12/out, 02/nov) e o Ciclo 3 abre no Carnaval de 2027.

**Métricas** (cliente) — 78 métricas, 51 delas P0, organizadas de baixo para cima no funil, no mesmo
formato do dicionário do Grupo Lupo.

> ⚠️ O dicionário é **v0**. Pressupõe receita B2B por plano ou assinatura de anunciante com motion
> sales-led — leitura ainda não confirmada pela OLX (`briefing.modelo_receita` segue `null` em
> [dados/client.json](../dados/client.json)). As perguntas que confirmam isso estão no bloco 03 do
> formulário; a v1 sai do próprio kick-off.
