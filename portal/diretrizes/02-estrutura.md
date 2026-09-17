# Estrutura

Como uma página do portal é montada, de fora para dentro.

## 1. O build

O portal é estático e o HTML publicado é gerado. **Nunca edite um `index.html`**, ele é
sobrescrito. Edite o fragmento em `_src/` e rode `python3 build.py` na pasta `portal/`.

Cada fragmento começa por uma linha de metadados de cinco campos separados por `|`:

```
<!--@ slug | título da aba | título da página | descrição | meta lateral -->
```

| Campo | Vai para |
|---|---|
| `slug` | Destino do arquivo e aba ativa na navegação. Precisa existir em `NAV`, no `build.py` |
| título da aba | `<title>` |
| título da página | `<h1>` da faixa de contexto. Vazio suprime a faixa inteira |
| descrição | `<meta name="description">` e o texto de apoio da faixa |
| meta lateral | Carimbo à direita da faixa: versão, período, estado |

O `build.py` envolve o fragmento, injeta a topbar, a gaveta, a faixa de contexto, o trilho de
índice e o rodapé, e versiona todo asset com um hash de conteúdo (`base.css?v=a1b2c3d4`). O hash
existe porque `/assets/*` é servido com `max-age=31536000, immutable`: sem ele, um deploy novo
não chega a quem já visitou.

Isso vale também para asset citado dentro do fragmento: escreva `src="/assets/form-data.js"`
e o build converte. Caminho com `?` já escrito à mão não é tocado.

## 2. Chrome do sistema

Ordem fixa no `<body>`, montada pelo `build.py`:

```
header.topbar          barra fixa, 3.5rem de altura
nav.drawer + .drawer-bd gaveta de navegação e fundo escuro
div.crumb              faixa de contexto (se a página tiver título)
div.doc                conteúdo + trilho de índice
footer                 confidencialidade e contrato
```

### Topbar

Fixa no topo, `z-index: 50`, altura `3.5rem`, largura interna `80rem`. Duas variantes:

| Variante | Onde | Fundo | Logo |
|---|---|---|---|
| padrão | todas as abas de conteúdo | `--bg` a 85% com `blur(20px)` | `logo-dark.svg`, tinta escura |
| `.topbar--red` | só o painel (`/`) | gradiente vermelho | `logo.svg`, tinta branca |

A troca de logo é por CSS, as duas imagens estão sempre no DOM. `.logo-escuro` é o arquivo de
tinta escura para fundo claro; `.logo-claro` é o branco para fundo vermelho.

Conteúdo, da esquerda para a direita: botão de gaveta, marca, abas (`≥768px`), espaçador,
botão de tema. As abas somem abaixo de 768px e a navegação passa a ser só a gaveta.

### Gaveta

Aberta pelo hambúrguer **em qualquer largura**, não só no mobile. `20rem`, entra da esquerda,
fecha com Esc, clique no fundo ou clique num link. Trava o scroll do body enquanto aberta e
devolve o foco ao botão ao fechar. Repete a navegação principal e, abaixo, o índice da página.

### Faixa de contexto

`.crumb` é a única linha entre o chrome e o conteúdo: `h1` da página, descrição em
`--muted-fg`, e o carimbo mono à direita. É ela que responde "que documento é este e de quando".
Suprimida no painel, que tem título próprio.

### Layout de documentação

```
.doc            grid, máx. 80rem
├── .doc-main   minmax(0,1fr)
└── .rail       224px, só a partir de 1100px
```

O trilho lista os `<h2>` da página, realça o visível por `IntersectionObserver` e pode ser
recolhido. O estado fica em `localStorage` (`dre-olx-trilho`) e, recolhido, o conteúdo passa a
ocupar a largura toda. Uma aba vertical fixa à direita traz o índice de volta.

Nada disso é escrito à mão: o `shell.js` monta o índice a partir dos `<h2>` e dá `id` a cada um.
**Consequência prática: a hierarquia de uma página é definida pelos seus `h2`.** Seção que
precisa aparecer no índice é `h2`; subtítulo que não precisa é `h3`.

Página que não quer trilho desliga com CSS no próprio fragmento, como faz `_src/receita.html`,
onde a árvore precisa da largura inteira.

## 3. Grade e larguras

| Medida | Valor |
|---|---|
| Largura máxima do conteúdo | `80rem` |
| Recuo lateral | `1rem`, e `1.5rem` a partir de 768px |
| Coluna do trilho | `224px`, com `2.5rem` de calha |
| Largura de leitura de texto corrido | `56rem` ou `68ch`, o que a peça declarar |

**Quirk conhecido:** `cronograma`, `metricas` e `kickoff` abrem o corpo com
`<main class="wrap"><div class="page">` dentro de `.doc-main`, que já tem recuo. O resultado é
`2rem` de recuo lateral em vez de `1.5rem`. Não quebra nada e é consistente entre as três; se for
padronizar algum dia, padronize as três de uma vez. `destrava` não faz isso e é o modelo limpo.

Também por herança, `.wrap` está declarada duas vezes: `72rem` em `base.css` e `80rem` em
`shell.css`. Vale `80rem`. Ao mexer em `base.css`, não "conserte" a primeira sem checar a segunda.

### Breakpoints

Os pontos de quebra foram escolhidos por componente, não por sistema. O conjunto real em uso:

| Ponto | Quem usa |
|---|---|
| `430px` / `560px` | Ajustes de barra fixa estreita no kick-off e nas métricas |
| `720px` | Empilhamento do cabeçalho de pergunta |
| `760px` | Grade de fio: 2 colunas passa a 4 |
| `768px` | Chrome: abas aparecem, recuo lateral aumenta |
| `820px` | Blocos de duas colunas |
| `900px` | Grades de 3, 4 e 5 colunas |
| `1100px` | Trilho de índice aparece |

Ao criar componente novo, prefira reusar `768px`, `900px` e `1100px`. Não acrescente ponto novo
sem motivo que não caiba nos existentes.

## 4. Anatomia de uma aba de conteúdo

Padrão que as abas seguem, do topo para baixo:

1. Linha de metadados
2. `<style>` da própria página, com o que só ela usa
3. Faixa de estatísticas (`.stats`), quando existe número que resume o documento
4. `<section class="blk">` repetidas, cada uma com `.blk-h` + `h2` e um `.lead`
5. Componentes dentro de cada seção
6. `<script>` da própria página, no fim

```html
<section class="blk">
  <div class="blk-h"><h2>Título da seção</h2><span class="eyebrow">carimbo</span></div>
  <p class="lead">Uma frase que diz o que esta seção resolve e para quem.</p>
  ...
</section>
```

`section.blk` leva `margin-top: 3.5rem` e `scroll-margin-top: 5rem`, para que o link do índice
não pare embaixo da barra fixa.

## 5. CSS por página, e quando promover

Cada fragmento carrega o próprio `<style>`. É deliberado: o Gantt, a árvore de receita e o
formulário não se parecem com nada mais e não deveriam ocupar o CSS global.

Promova uma regra para `base.css` ou `shell.css` quando ela aparecer **na terceira página**.
Hoje já passaram desse ponto e continuam duplicadas em cada fragmento: `.blk-h`, `.lead`,
`.stats`/`.stat`, `section.blk` e o `.toast`. Quem for mexer nelas mexe em todas, ou promove.

## 6. Cabeçalhos e publicação

`vercel.json` fixa `cleanUrls`, `noindex` e uma CSP restritiva: `default-src 'self'`, fontes só
do Google Fonts, nada de `connect-src` externo. **Consequência de projeto: o portal não busca
dado de terceiro em runtime.** Dado novo entra como arquivo em `assets/` (`form-data.js`,
`metrics-data.js`) ou por função interna em `api/`.

O acesso é por Basic Auth no `middleware.js`, validando pares usuário e senha da variável
`PORTAL_CREDENCIAIS`. Detalhes de publicação em [PUBLICACAO.md](../PUBLICACAO.md).
