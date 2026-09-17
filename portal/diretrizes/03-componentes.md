# Componentes

Catálogo do que já existe. Antes de desenhar peça nova, procure aqui.
Cada entrada diz onde ela está definida hoje.

## Grade de fio

**A assinatura visual do portal.** Uma grade cujo `gap` de 1px mostra o fundo `--border`, com os
filhos pintados de `--card`. Produz linhas perfeitas de 1px sem borda em cada célula e sem sombra.

```html
<div class="stats">
  <div class="stat"><b>4</b><span>ciclos de 90 dias</span></div>
  <div class="stat"><b>12</b><span>comitês: 3 por ciclo</span></div>
  <div class="stat"><b>9</b><span>diagnósticos contratados</span></div>
  <div class="stat"><b>78</b><span>métricas no dicionário</span></div>
</div>
```

```css
.stats{display:grid;gap:1px;background:var(--border);border:1px solid var(--border);
  border-radius:var(--radius);overflow:hidden;grid-template-columns:repeat(2,1fr)}
@media(min-width:760px){.stats{grid-template-columns:repeat(4,1fr)}}
.stat{background:var(--card);padding:1.15rem 1.2rem}
.stat b{display:block;font-size:1.85rem;font-weight:600;letter-spacing:-.035em;
  font-variant-numeric:tabular-nums;line-height:1.1}
.stat span{display:block;margin-top:.25rem;font-size:.8rem;color:var(--muted-fg)}
```

Sempre 2 colunas no estreito e 4 no largo. O mesmo padrão aparece como `.status` (painel, sobre o
vermelho), `.phases` (5 colunas), `.repl` (4 colunas) e `.acs-l` (2 colunas).
Definido em `_src/cronograma.html` e `_src/metricas.html`, duplicado.

**Número sem fonte não entra aqui.** Se o valor não existe, a célula não existe. Regra 1 do
[CLAUDE.md](../../CLAUDE.md).

## Cabeçalho de seção

```html
<div class="blk-h"><h2>Título da seção</h2><span class="eyebrow">carimbo</span></div>
<p class="lead">Uma frase dizendo o que a seção resolve.</p>
```

Filete inferior de **2px sólido `--fg`**, não `--border`. É o que separa seção de cartão: seção
tem régua preta, cartão tem fio cinza. Em `_src/destrava.html` a régua é de 1px `--border`, para
uma aba ainda em construção; as três abas maduras usam 2px.

## Cartão

`.card` é a base: `--card`, fio `--border`, raio `--radius`, `--shadow-card`. Nunca use sozinha,
sempre com uma classe de papel ao lado.

| Papel | Classe | Forma |
|---|---|---|
| Bloco de leitura | `.note` | Título `h3` + `<ul>` de argumentos |
| Aviso | `.note.warn` / `.warnbox` | Fundo `--warn-bg`, fio e título `--warn` |
| Regra contratual | `.rule` | Rótulo mono à esquerda, com `min-width:7.5rem`, parágrafo à direita |
| Comitê | `.com` | Cabeçalho com data mono, linha `.decide` em `--accent`, depois a lista |
| Definição | `.cbox` | `<dl>` de duas colunas, termo mono em `--brand-ink` |
| Modelo de dado | `.tpl` | Parágrafo com `<code>` sobre `--muted` |

```html
<div class="two">
  <div class="card note">
    <h3>Por que 90 dias</h3>
    <ul><li>É o menor intervalo em que uma mudança estrutural aparece em métrica de receita.</li></ul>
  </div>
  <div class="card note warn">
    <h3>Riscos de calendário</h3>
    <ul><li>O Ciclo 1 perde três segundas-feiras.</li></ul>
  </div>
</div>
```

`.two` é o par de colunas a partir de 900px. Definido em `_src/cronograma.html`.

## Tag

Pílula mono de `.66rem` para carimbar severidade e estado.

| Classe | Aparência | Significado |
|---|---|---|
| `.tag` | fio `--border-strong` sobre `--muted` | Neutro, rótulo |
| `.tag-p0` | sólida `--brand`, texto branco | Prioridade máxima |
| `.tag-p1` | `--warn-bg` com texto `--warn` | Prioridade média |
| `.tag-crit` | `--accent` com texto `--brand-ink` | Crítico, bloqueia |
| `.tag-ok` | `--ok-bg` com texto `--ok` | Fechado, concedido |
| `.tag-off` | `--muted` | Desligado, fora de escopo |

`.tag`, `.tag-p0`, `.tag-p1` e `.tag-crit` estão em `base.css`; `.tag-ok` e `.tag-off` em
`_src/cronograma.html`. As quatro primeiras são globais, use-as.

## Botões e controles

| Classe | Onde | Forma |
|---|---|---|
| `.btn` | ação secundária | fio `--border-strong`, raio `--radius-sm`, `.82rem` |
| `.btn-primary` | ação principal | `--brand` sólido, hover `--brand-deep` |
| `.icobtn` | chrome | sem fio, `2.25rem` de altura, hover `--muted` |
| `.fbtn` | filtro | pílula, `aria-pressed="true"` pinta de `--brand` |
| `.chip` | atalho para seção | pílula leve, hover pinta o fio de `--brand` |

Filtro usa `aria-pressed`, não uma classe `.ativo`. O estado visual é derivado do atributo de
acessibilidade, nunca o contrário. Mesma regra no trilho e nas abas, que usam `aria-current`.

## Tabela

```html
<div class="card scrollx">
  <table>
    <thead><tr><th>Métrica</th><th style="width:5rem">Unidade</th></tr></thead>
    <tbody><tr><td>Receita nova</td><td class="num">R$</td></tr></tbody>
  </table>
</div>
```

- Sempre dentro de `.card.scrollx`. Tabela larga rola dentro do cartão, a página não rola de lado.
- `th` é mono, maiúsculo, `.68rem`, `--muted-fg`, com `white-space: nowrap`.
- Largura de coluna vai no `th` por `style="width:..."`, é o padrão em uso.
- Número ou data em célula leva `.num` (mono + tabular).
- `tr.grp` é a linha de grupo: fundo `--muted`, texto mono maiúsculo `--brand-ink`.
- Última linha perde o fio inferior automaticamente.

Definida em `base.css`, vale em todo o portal.

## Barra fixa secundária

Filtros e ações de página ficam numa barra grudada **abaixo** da topbar:

```css
.filters{position:sticky;top:3.5rem;z-index:30;
  background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(16px);
  border-bottom:1px solid var(--border)}
```

`top: 3.5rem` é a altura da topbar, `z-index` sempre abaixo de 40. Quem usa barra assim precisa
subir o `scroll-margin-top` das seções, senão o link do índice para debaixo dela. No kick-off
isso chega a `10rem` abaixo de 430px.

## Estado vazio

```html
<div class="vazio">
  <b>Formato visual em definição</b>
  <span>O conteúdo entra assim que o formato for decidido.</span>
</div>
```

Fio tracejado `--border-strong` sobre `--muted`, centralizado. É como o portal admite que algo
ainda não existe. Melhor que uma seção ausente: o leitor vê o lugar reservado.
Definido em `_src/destrava.html`.

## Cartão de fase

Cinco fases do ciclo, uma ativa:

```html
<div class="fases">
  <div class="fase ativa"><span class="n">Fase 1</span><h3>Identificar</h3>
    <p>Uma linha sobre o que a fase produz.</p><span class="st">em andamento</span></div>
</div>
```

A fase ativa recebe fio `color-mix(in srgb, var(--brand) 45%, transparent)` e a pílula `.st` vira
sólida `--brand`. Definido em `_src/destrava.html`. Não confundir com `.phases`/`.phase` do
cronograma, que é grade de fio e não tem estado ativo.

## Porta

Cartão de navegação do painel, só sobre o vermelho. Vidro sobre vidro: dois gradientes
sobrepostos, `backdrop-filter: blur(16px)`, `box-shadow` interno branco a 22% simulando a borda
de cima iluminada, e `translateY(-3px)` no hover. Fecha com um rodapé de "Abrir →" mais uma
pílula de estado (`.st-pill`, com variante `.warn`). Definido em `_src/painel.html`.

## Barra de progresso

```html
<div class="progress"><span class="pbar"><i id="pfill"></i></span><span id="pcount">0/88</span></div>
```

`5px`, pílula, trilho `--muted`, preenchimento `--brand`. O kick-off usa duas camadas: `--brand`
sólido para respondido e `color-mix(--brand 32%)` para parcial. Três estados, não dois: campo
com "Não tratado" tem texto mas não é resposta.

## Toast e diálogo

Toast: pílula fixa no rodapé central, `--fg` sobre `--bg` invertidos, entra por `transform`.
Diálogo: `<dialog>` nativo, `max-width: min(62rem, 92vw)`, cabeçalho `.dlg-h` com fio inferior,
corpo `.dlg-b`, `::backdrop` em `rgba(15,18,22,.55)`. Usado para exportar Markdown: cabeçalho,
`<textarea>` mono de `55vh` e botão de copiar.

Duplicados em `_src/kickoff.html` e `_src/metricas.html`, idênticos. São os primeiros candidatos
a promoção para `shell.css`.

## Campo editável

```css
textarea, input[type=text]{width:100%;font:inherit;font-size:.9rem;color:var(--fg);
  background:var(--bg);border:1px solid var(--input);border-radius:var(--radius-sm);
  padding:.55rem .65rem}
textarea:focus,input:focus{border-color:var(--brand);outline:none;
  box-shadow:0 0 0 3px color-mix(in srgb,var(--brand) 14%,transparent)}
```

Variante invisível, na tabela de pendências de acesso: borda transparente, aparece no hover,
vira `--brand` no foco. Serve para uma tabela que também é formulário, sem parecer formulário.

## Peças de uma página só

Não generalize sem necessidade real. Cada uma existe por um motivo específico:

| Peça | Arquivo | O que é |
|---|---|---|
| Gantt de semanas e de dias | `_src/cronograma.html` | Trilha em `position:absolute` sobre grade `repeating-linear-gradient`. Escala de quatro ciclos por `color-mix`, barra tracejada para bloqueio, guia pontilhada de "hoje" calculada no cliente |
| Árvore de receita | `_src/receita.html` | Canvas com pan e zoom, árvore de baixo para cima em flex com conectores por `::before`/`::after`, nó editável com estado no fio esquerdo |
| Formulário de kick-off | `_src/kickoff.html` | 88 perguntas com três estados visuais, progresso em duas camadas, persistência em `localStorage` |
| Filtro de métricas | `_src/metricas.html` | Barra fixa com busca, botões `aria-pressed` e contagem viva |
| Blocos de vidro em deriva | `_src/painel.html` | 12 retângulos com oscilação senoidal e paralaxe de ponteiro, pausados em segundo plano e sob `prefers-reduced-motion` |
