# Entregáveis ao cliente

Material produzido pela V4 e enviado ao Grupo OLX. Não confundir com
[`assets/originais/`](../../assets/originais/), que é o caminho inverso: o que a OLX
nos entregou.

## A lista de pendentes, 03/09/2026

`V4 x Grupo OLX - Acessos Pendentes.docx` é o terceiro documento e o mais simples: uma tabela de
**ferramenta × auditoria × nível necessário × status**, com 4 acessos parciais, 17 pendentes e 4 já
concedidos. Existe para conferência, não para argumentação, os dois documentos abaixo é que
argumentam.

> ⚠️ **Ele é uma fotografia datada.** Foi gerado em 03/09 às 15h, **antes** da entrega do lote
> combinada para as 17h daquele dia. Depois da conferência de 04/09 ele precisa ser regerado, senão
> vira uma cobrança de coisas que já chegaram. A distinção parcial/pendente existe porque acesso já
> chegou concedido e não utilizável duas vezes: GA4 em nível Leitor, e portfólio Meta sem ativo
> conectado.

```
.venv/bin/python gera-docx-pendentes.py    # escreve o .docx no ~/Desktop
```

Editar a constante `PENDENTES` no gerador, nunca o `.docx`.

## O par de acessos, revisão de 25/08/2026

Dois documentos que se complementam e são enviados juntos. Um argumenta, o outro se trabalha.
Cada um remete ao outro no rodapé.

| Documento | Função | Artifact |
|---|---|---|
| **Acessos e níveis de dado** | A argumentação: a escala de três níveis de profundidade de dado, os 5 itens já liberados que não bastam, os 7 não liberados, o bloco K de dados de retenção, e o resumo por responsável | <https://claude.ai/code/artifact/a74e7701-a506-47b8-ab7a-ee460c4bf015> |
| **Checklist de liberação** | A lista de trabalho: as 12 pendências de acesso com ação, responsável e prazo, em formato de checklist | <https://claude.ai/code/artifact/1156768d-f06b-432a-9401-3d5d6b652fdd> |

### A tese dos dois documentos

A palavra "nível" aparece em dois sentidos, e eles pedem coisas diferentes do cliente.

**Nível de permissão.** Cinco itens exigem administrativo ou proprietário, não para alterar
nada, mas porque estabelecer uma integração com o V4MOS é ato administrativo no Google e na
Meta. Depois de conectada, a integração apenas lê, e o acesso pode voltar a leitura.

| Acesso | Basta analisar | Nível pedido |
|---|---|---|
| Google Analytics 4 | Analista | Editor, ou Administrador com vínculo Google Ads |
| Google Tag Manager | Leitura | Publicar, ou Admin se server-side |
| Google Search Console | Usuário completo | Proprietário |
| Meta Ads, as 2 contas | Ver desempenho | Admin do Business Manager |
| Google Ads de captação | Somente leitura | Administrativo |
| CRM e Marketing Cloud | Leitura | Leitura com exportação |

**Profundidade do dado.** Quatro itens já entregues estão em nível 1 ou 2 da escala:
material consolidado (slide, PDF) → relatório agregado → dado na linha ou a ferramenta.
Só o nível 3 permite fazer perguntas novas.

### Prazo

Único, e vale para tudo: idealmente **26/08/2026**. As nove auditorias funcionam em cadeia.
O lote completo de acessos chegou em **10/09**, os nove diagnósticos fecham em **18/09**, e a
apresentação e o Comitê 1 acontecem numa sessão única em **23/09**, confirmada pela OLX em
11/09. As datas de 24/09 e 01/10, do planejamento de 03/09, não valem mais.

## Arquivos

| Arquivo | O que é |
|---|---|
| `acessos-e-niveis-de-dado.html` | Fonte do primeiro artifact |
| `checklist-de-liberacao.html` | Fonte do segundo artifact |
| `V4 x Grupo OLX - Acessos e Niveis de Dado.docx` | Versão para anexar em e-mail |
| `V4 x Grupo OLX - Checklist de Liberacao.docx` | Versão para anexar em e-mail |
| `V4 x Grupo OLX - Acessos Pendentes.docx` | A lista crua, para conferência item a item |
| `gera-docx.py` | Gerador dos dois primeiros `.docx` |
| `gera-docx-pendentes.py` | Gerador do terceiro, importa os helpers do `gera-docx.py` |

Os `.docx` são gerados, não editados à mão. Quando um dado mudar (uma liberação sair, o status
de uma conta mudar), edite as constantes `PERMISSOES`, `PROFUNDIDADE`, `DESTRAVA`, `CONTAS` e
`BLOCOS_CHK` no `gera-docx.py` e regenere: assim as duas versões não divergem.

```
python3 -m venv .venv && .venv/bin/pip install python-docx
.venv/bin/python gera-docx.py     # escreve os dois .docx no ~/Desktop
```

Os HTML são republicados pelo mesmo caminho de arquivo, o que mantém as URLs acima estáveis.

## Cuidado ao atualizar

O conteúdo destes documentos deriva de três fontes do repositório. Se alterar lá, reflita aqui:

- [`dados/acessos.json`](../../dados/acessos.json), fonte da verdade dos acessos
- [`02-diagnostico/checklist-dados-e-acessos.md`](../../02-diagnostico/checklist-dados-e-acessos.md), blocos A a J
- [`PENDENCIAS.md`](../../PENDENCIAS.md), itens 6, 11 e 12

O `acessos.json` e o `01-cliente/acessos-e-ferramentas.md` estavam divergentes em 24/08 quanto ao
aceite do MCC VivaReal. Estes entregáveis seguem o `acessos.json`, que é o correto.

## Premissas a confirmar

Os dois documentos assumem que **Mirella Mendonça é a decisora** e que **Autos está no escopo**.
Se o kick-off tiver mudado alguma das duas coisas, a seção de responsáveis do primeiro documento
e as linhas de Autos dos dois precisam ser revistas antes de qualquer reenvio.

## Histórico

- **24/08**: primeira versão, construída sobre a escala de profundidade de dado. Afirmava que
  nenhum pedido envolvia permissão de escrita.
- **25/08**: revisão. A integração com o V4MOS exige nível administrativo em cinco itens, o que
  invalidou aquela afirmação. Os documentos passaram a separar os dois sentidos de "nível",
  o prazo virou único (26/08), Leonardo Rosa entrou nas contas de domínio, e a estrutura passou a
  espelhar a do e-mail enviado à Michelle Morais.

## Divergência a resolver

O e-mail de 25/08 pede as concessões de medição (Analytics, Tag Manager, Search Console) para
`gina@v4company.com`. O [`dados/acessos.json`](../../dados/acessos.json) registra a decisão de
24/08 de pedir todo acesso novo para `rafael.corazza-ext@olxbr.com`, que é conta do domínio da
OLX e dispensa aprovação de parceiro externo. Os dois caminhos funcionam, mas convém escolher um
antes que metade dos acessos chegue em cada conta.
