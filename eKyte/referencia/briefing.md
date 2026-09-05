# Formato padrão da descrição de tarefa

Fonte da verdade do briefing. **Toda** tarefa criada via MCP usa este formato no campo
`description` — sem exceção, sem variação por pessoa.

## Por que no `description`

Nenhum tipo de tarefa do fluxo `22597` tem formulário (`ctcTaskFormIds: []`) e a fase
`Briefing [CN]` (88690) está `active=0`. Ou seja: não existe hoje
nenhum outro campo estruturado onde o briefing possa morar. Enquanto isso não mudar,
o `description` **é** o briefing, e é a única barreira contra "só me faz uma peça".

O campo aceita HTML. Use só `h3`, `p`, `ul`, `li`, `strong`, `hr` — o resto pode não
renderizar no eKyte.

---

## Bloco comum — obrigatório em todos os tipos

```html
<h3>Solicitação</h3>
<p><strong>Solicitante:</strong> NOME — CADEIRA</p>
<p><strong>Pedido em:</strong> AAAA-MM-DD</p>

<h3>Objetivo</h3>
<p>O que essa entrega precisa provocar. Uma frase, em resultado, não em tarefa.</p>

<h3>Destino</h3>
<p>Onde exatamente isso vai ser usado.</p>

<h3>Mensagem central</h3>
<p>O que precisa ser dito.</p>

<h3>Especificações</h3>
<ul>
  <li><strong>Formato:</strong> </li>
  <li><strong>Quantidade:</strong> </li>
  <li><strong>Tom:</strong> </li>
</ul>

<h3>Referências</h3>
<ul>
  <li></li>
</ul>

<h3>Restrições</h3>
<ul>
  <li></li>
</ul>

<h3>Critério de aceite</h3>
<ul>
  <li></li>
</ul>

<h3>Pré-requisitos pendentes</h3>
<ul>
  <li></li>
</ul>
```

### Regras de cada campo

**`Solicitante`** — nome e cadeira de quem pediu. Redundante se o token do eKyte
identificar usuário; obrigatório enquanto isso não estiver confirmado, porque é a única
forma de saber quem pediu o quê. Ver [[ekyte-mcp-limites-e-ids]].

**`Destino`** — **bloqueia a criação se vazio ou genérico.** Decisão registrada: só é
output legítimo se o destino for real. "Acervo", "para ter", "depois a gente vê" não são
destinos. Exige nome concreto: qual campanha, qual conjunto de anúncios, qual perfil e
data, qual reunião com qual cliente.

**`Mensagem central`** — **obrigatório nos tipos que produzem peça, nunca inferido pela AI.**
A cadeira de Conteúdo saiu do meio da produção: o texto sai junto com a peça, na mão do
Design com AI. Não há copywriter no caminho corrigindo direção de mensagem. Se o
solicitante não sabe o que precisa ser dito, o briefing não está pronto e a tarefa não
deve ser criada.

Obrigatório em: `86882` · `86891` · `86890` · `86886` · `86885`.
Dispensado em: `86889` · `86888` · `86883` — tarefas técnicas, sem peça de comunicação.
Nesses três, preencher `— NÃO SE APLICA —`. Descoberto no teste de 2026-08-03: o campo
travava a criação de uma tarefa de traqueamento, onde não existe mensagem nenhuma.

**`Critério de aceite`** — o que a Aprovação Interna vai conferir. Sem isso a aprovação
vira opinião.

**`Pré-requisitos pendentes`** — o que precisa existir antes de alguém puxar a tarefa:
acesso a conta, verba aprovada, material do cliente, aprovação anterior. Se houver item
aqui, a tarefa nasce bloqueada e isso tem que estar visível antes de entrar em execução —
não depois que o executor abriu e descobriu que não tem acesso. Deixe vazio se não houver.

**Nunca preencher com suposição.** Se o solicitante não respondeu, o campo fica com
`<p>— NÃO INFORMADO —</p>` visível. É melhor a lacuna aparecer na tarefa do que a AI
inventar e o Design executar em cima da invenção.

---

## Blocos extras por tipo

Anexar depois do bloco comum, conforme o `ctcTaskTypeId`.

### Campanha de Tráfego (86882 Meta · 86881 Google) e Troca de Criativo (86891)

```html
<h3>Campanha</h3>
<ul>
  <li><strong>Objetivo de campanha:</strong> </li>
  <li><strong>Público:</strong> </li>
  <li><strong>Verba e período:</strong> </li>
  <li><strong>Campanha/conjunto de destino:</strong> </li>
  <li><strong>URL de destino:</strong> </li>
</ul>
```

### Otimização de Campanha (86889 Meta · 86888 Google)

```html
<h3>Diagnóstico</h3>
<ul>
  <li><strong>Campanha:</strong> </li>
  <li><strong>Métrica fora da meta:</strong> </li>
  <li><strong>Valor atual x meta:</strong> </li>
  <li><strong>Janela analisada:</strong> </li>
  <li><strong>Hipótese:</strong> </li>
</ul>
```

### Planejamento de Conteúdo (86890)

```html
<h3>Escopo do planejamento</h3>
<ul>
  <li><strong>Mês de referência:</strong> </li>
  <li><strong>Revisar linha editorial?</strong> sim | não</li>
  <li><strong>Nº de posts previstos:</strong> </li>
  <li><strong>Canais:</strong> </li>
</ul>
```

`Revisar linha editorial? = sim` → `estimatedTime` 260. `não` → 200.

### Criativos Social Media - Publicação (86885)

```html
<h3>Publicação</h3>
<ul>
  <li><strong>Perfil e canal:</strong> </li>
  <li><strong>Data e hora da publicação:</strong> </li>
  <li><strong>Legenda e hashtags:</strong> </li>
  <li><strong>Origem no planejamento:</strong> </li>
</ul>
```

### Elaboração Criativo Avulso (86886)

```html
<h3>Peça</h3>
<ul>
  <li><strong>Uso previsto:</strong> </li>
  <li><strong>Formatos e dimensões:</strong> </li>
  <li><strong>Reaproveita peça existente?</strong> </li>
</ul>
```

Este é o tipo mais convidativo do catálogo para virar atalho sem briefing. É justamente
onde `Destino` e `Mensagem central` são mais exigidos.

### Configuração de Traqueamento (86883)

```html
<h3>Rastreamento</h3>
<ul>
  <li><strong>Domínio/propriedade:</strong> </li>
  <li><strong>Eventos a configurar:</strong> </li>
  <li><strong>Acessos já liberados?</strong> </li>
  <li><strong>Como validar:</strong> </li>
</ul>
```

---

## Bloco de retorno — append, nunca sobrescreve

Quem devolve a tarefa **acrescenta** este bloco ao final do `description` existente
(`update_task` com `/description`, colando o HTML atual + o bloco novo). O histórico de
retornos fica visível na tarefa.

```html
<hr>
<h3>Retorno — AAAA-MM-DD</h3>
<p><strong>Origem:</strong> Cliente | Interno</p>
<p><strong>Motivo:</strong> </p>
<p><strong>O que muda:</strong> </p>
```

**`Origem` é obrigatório e é a métrica.** As fases se chamam "Alteração", então não há
distinção estrutural entre pedido do cliente e erro nosso — separar em fases geraria 6
colunas. Este campo é o único lugar onde a taxa de defeito fica visível:
`Interno` = refação, erro nosso. `Cliente` = alteração, mudança de escopo.

Atenção: as fases de `Alteração` (88697, 88698, 88699) continuam `active=0` no fluxo `22597`.
Enquanto continuarem inativas, o retorno não tem fase para onde ir e este bloco é o único
registro do retrabalho.
