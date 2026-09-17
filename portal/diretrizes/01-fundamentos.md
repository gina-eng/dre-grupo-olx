# Fundamentos

Tudo aqui está declarado em [`assets/base.css`](../assets/base.css), no bloco `:root`.
Nenhuma página deve escrever um valor de cor, raio ou sombra fora destes tokens, com uma
exceção declarada adiante: a superfície vermelha.

## 1. Cor

### Tokens de superfície

| Token | Claro | Escuro | Uso |
|---|---|---|---|
| `--bg` | `#fcfcfa` | `#0b0b0d` | Fundo da página |
| `--fg` | `#0f1216` | `#f3f3f4` | Texto principal |
| `--card` | `#ffffff` | `#141417` | Superfície de cartão, tabela, barra |
| `--card-2` | `#ffffff` | `#17171b` | Cartão em estado resolvido (pergunta respondida) |
| `--muted` | `#f0f2f4` | `#1a1a1e` | Fundo de apoio: cabeçalho de tabela, chip, hover |
| `--muted-fg` | `#5a5e63` | `#a3a3ac` | Texto secundário, rótulo, legenda |
| `--border` | `#e3e4e6` | `#27272b` | Fio padrão |
| `--border-strong` | `#d3d5d8` | `#35353b` | Fio de contorno de controle |
| `--input` | `#e7e8ea` | `#27272b` | Borda de campo editável |

O fundo claro é `#fcfcfa`, levemente quente, não branco puro. Cartão em branco sobre ele é o
que cria a separação sem precisar de sombra pesada.

### Tokens de marca

| Token | Claro | Escuro | Uso |
|---|---|---|---|
| `--brand` | `#df2225` | igual | Preenchimento sólido: botão primário, tag P0, barra de progresso |
| `--brand-deep` | `#970005` | igual | Hover do botão primário |
| `--brand-soft` | `#ff716b` | igual | Reservado, sem uso hoje |
| `--brand-ink` | `#c31a1d` | `#ff5d5f` | **Vermelho de texto.** Link, rótulo, número em destaque |
| `--accent` | `#f8efee` | `#2a1315` | Fundo de realce discreto: aba ativa, linha de comitê |
| `--accent-fg` | `#361715` | `#ffdedc` | Texto sobre `--accent` |

**A distinção que mais erra:** `--brand` é para preencher, `--brand-ink` é para escrever.
Vermelho `#df2225` em texto pequeno sobre fundo claro não passa em contraste; `--brand-ink` passa.
Só `--brand-ink` e `--accent` invertem no tema escuro, os outros três são fixos porque só aparecem
sobre branco ou sobre o vermelho.

### Tokens de estado

| Token | Claro | Escuro | Significado |
|---|---|---|---|
| `--ok` / `--ok-bg` | `#1f7a4d` / `#eaf6ef` | `#5fd39a` / `#12251c` | Confirmado, concedido, fechado |
| `--warn` / `--warn-bg` | `#8a5a00` / `#fdf3e2` | `#f0b45e` / `#2a2013` | Parcial, hipótese, atenção |

Não existe token de erro. O portal não tem estado de erro visual: o que estaria vermelho de erro
em outro sistema aqui é **pendência**, e pendência usa `--accent` com `--brand-ink`. A escala de
severidade do projeto vive nas tags (ver [03-componentes.md](03-componentes.md)).

Mapa completo de estado por componente está em [04-regras.md](04-regras.md).

### A superfície vermelha

O painel (`/`) e a topbar dele são a única superfície que não segue os tokens. É a identidade
Destrava Receita, e o gradiente é literal:

```css
background:
  radial-gradient(80% 60% at 20% 10%, rgba(214,17,49,.85), transparent 60%),
  radial-gradient(70% 50% at 85% 20%, rgba(183,0,38,.85), transparent 55%),
  radial-gradient(100% 70% at 50% 110%, rgba(120,0,4,.90), transparent 60%),
  linear-gradient(135deg,#970013,#d6002e);
```

Regras sobre ele:

- Todo texto é `#fff` ou `rgba(255,255,255,.82–.95)`. Nunca `--fg`.
- Toda borda é `rgba(255,255,255,.16–.28)`. Nunca `--border`.
- **Nada de `saturate()`.** Já foi tentado: `saturate(170%)` levava `rgb(200,20,45)` a
  `rgb(255,0,34)` e derrubava o contraste do texto que passa por cima para cerca de 2,4:1.
  O comentário no CSS registra isso, não remova.
- O painel força `:root{color-scheme:dark}` e `body{background:#5c0009}`. Sem isso a barra de
  rolagem fica branca colada na borda da página vermelha, e o repique de overscroll do macOS
  mostra o fundo do body.

### Como misturar

Tom intermediário se faz com `color-mix`, nunca com um hex novo:

```css
background: color-mix(in srgb, var(--brand) 76%, var(--muted-fg));   /* ciclo 2 do Gantt */
border-color: color-mix(in srgb, var(--brand) 45%, transparent);      /* contorno de fase ativa */
box-shadow: 0 0 0 3px color-mix(in srgb, var(--brand) 14%, transparent); /* anel de foco de campo */
```

A escala de quatro ciclos do cronograma é exatamente isto: `--brand` puro, depois 76%, 54% e 34%
misturados com `--muted-fg`. Qualquer série de quatro itens deve reusar essa escala.

## 2. Tipografia

**IBM Plex, só IBM Plex.** Carregada do Google Fonts em [`build.py`](../build.py):

```
IBM Plex Sans: 300, 400, 500, 600, 700, itálico 400
IBM Plex Mono: 400, 500, 600
```

| Token | Valor |
|---|---|
| `--sans` | `"IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif` |
| `--mono` | `"IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace` |

### A divisão de trabalho entre as duas

Não é decoração. A mono marca **o que é dado e não é prosa**:

| Mono | Sans |
|---|---|
| Rótulo de seção (`.eyebrow`, `.side-label`, `th`) | Qualquer frase |
| Data, prazo, intervalo (`24 ago 2026`, `S2–S3`) | Título |
| Número tabular (`.num`, `.stat b`, contagem) | Texto de cartão |
| Tag, chip, pílula de estado | Texto de tabela |
| Identificador (código de métrica, ID de bloco) | Legenda em frase |

Todo número que entra em coluna ou compara com outro número leva
`font-variant-numeric: tabular-nums`.

### Escala

| Papel | Tamanho | Peso | Tracking |
|---|---|---|---|
| Título do painel | `clamp(1.9rem, 4.6vw, 3.15rem)` | 600 | `-.025em`, `line-height 1.06` |
| Título da faixa de contexto (`.crumb h1`) | `1.15rem` | 600 | `-.025em` |
| Título de seção (`h2` em `.blk-h`) | `1.35–1.45rem` | 600 | `-.01em` |
| Título de cartão (`h3`) | `.98–1.05rem` | 600 | - |
| Corpo | `16px`, `line-height 1.55` | 400 | - |
| Texto de apoio (`.lead`) | `.94rem`, cor `--muted-fg` | 400 | máx. `68ch` |
| Texto dentro de cartão | `.83–.89rem` | 400 | - |
| Tabela | `.86rem` | 400 | - |
| Número grande (`.stat b`) | `1.85rem` | 600 | `-.035em`, tabular |
| Rótulo mono | `.64–.68rem` maiúsculas | 500/600 | `.08–.14em` |
| Tag | `.66rem` mono | 500 | `.04em` |

Título grande recebe tracking negativo; rótulo mono pequeno recebe tracking positivo. É o que dá
ao conjunto a aparência de documento técnico e não de site.

`h1..h4` já vêm com `text-wrap: balance`, `margin: 0` e peso 600. Espaçamento vertical é
responsabilidade do contêiner, nunca da margem do título.

## 3. Forma

| Token | Valor | Uso |
|---|---|---|
| `--radius-sm` | `.5rem` | Botão, campo, nó da árvore |
| `--radius` | `.75rem` | Cartão, tabela emoldurada, diálogo |
| `--radius-lg` | `1rem` | Porta do painel |
| pílula | `9999px` | Tag, chip, barra de progresso, toast, botão de filtro |

Sombra: uma só, `--shadow-card`.

```css
--shadow-card: 0 1px 2px rgba(15,18,22,.04), 0 8px 24px rgba(15,18,22,.05);
```

No escuro ela troca para `rgba(0,0,0,.4)` e `rgba(0,0,0,.3)`. Cartão dentro de uma grade de fio
(ver [03-componentes.md](03-componentes.md)) **não leva sombra**: quem separa é o fio de 1px.

Elevação por blur, não por sombra, é o recurso da superfície vermelha e das barras fixas:
`backdrop-filter: blur(8–20px)` sempre com o prefixo `-webkit-` ao lado.

## 4. Movimento

| Situação | Duração |
|---|---|
| Hover de cor e fundo | `.14s` |
| Transformação de cartão (porta do painel) | `.16s ease` |
| Toast, barra de progresso, seta de acordeão | `.18–.25s` |
| Gaveta de navegação | `.3s cubic-bezier(.2,.8,.2,1)` |

`base.css` desliga tudo em `prefers-reduced-motion: reduce`. A animação dos blocos de vidro do
painel também respeita a preferência e pausa quando a aba vai para segundo plano.

## 5. Foco

```css
:focus-visible { outline: 2px solid var(--brand); outline-offset: 2px; border-radius: 4px }
```

Sobre a superfície vermelha vira `outline: 2px solid #fff`. Campo editável troca o anel por
borda `--brand` mais `box-shadow: 0 0 0 3px color-mix(in srgb, var(--brand) 14%, transparent)`.
Nenhum elemento remove o foco sem colocar outro no lugar.

## 6. O que existe no CSS e não é usado

Registrado para que ninguém construa em cima achando que é padrão vivo:

- `.hero`, `.hero-inner`, `.hero-logo`, `.hero-meta`, `.atmos` em `base.css`: sobraram das versões
  em artifact, anteriores ao painel. Nenhum fragmento em `_src/` usa. O gradiente delas foi
  reescrito dentro de `_src/painel.html` como `.red-bg`.
- `.pill`: sem uso. O que se parece com ela hoje é `.st-pill`, definida no painel.
- `--brand-soft`: declarada, nunca referenciada.
- `.wrap` está definida duas vezes, `72rem` em `base.css` e `80rem` em `shell.css`. Vale a
  segunda, porque `shell.css` carrega depois. Ver [02-estrutura.md](02-estrutura.md).
