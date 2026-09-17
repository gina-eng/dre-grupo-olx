# Regras de uso

## 1. Semântica de estado

O portal usa quatro estados, com as mesmas cores em toda parte. Um estado novo precisa caber
num destes quatro ou justificar por que não cabe.

| Estado | Cor | Kick-off (`.pa-st`) | Árvore (`.nd[data-s]`) | Painel (`.acs-i b`) | Tag |
|---|---|---|---|---|---|
| Fechado | `--ok` sobre `--ok-bg` | `concedido` | `confirmado` | `.ok` | `.tag-ok` |
| Em meio caminho | `--warn` sobre `--warn-bg` | `parcial` | `hipotese` | `.pr` | `.tag-p1` |
| Em aberto | `--brand-ink` sobre `--accent` | `pendente` | `aberto` | `.pd` | `.tag-crit` |
| Morto | `--muted-fg` sobre `--muted` | `inexistente` | - | - | `.tag-off` |

Duas regras que caem daí:

- **Pendência não é erro.** O que está aberto é vermelho de marca, não vermelho de alarme. O
  portal registra lacuna o tempo todo, e uma parede de alertas ensinaria o leitor a ignorá-los.
- **"Em aberto" é visível, nunca ausente.** Campo sem dado vira `.vazio`, `.tag-crit` ou um traço,
  nunca uma seção que some. É a regra 1 do [CLAUDE.md](../../CLAUDE.md) traduzida em pixel: número
  sem fonte fica `null` e vira pendência, não um valor inventado.

Estimativa carrega a marca `[E]` também na tela, como no texto. No cronograma isso aparece como
`<span class="est">` ao lado do rótulo.

## 2. Acessibilidade

Não é opcional, e boa parte já está resolvida no chrome. O que precisa continuar valendo:

- **Estado vem de atributo ARIA.** `aria-current` na aba, no item de navegação e no trilho;
  `aria-pressed` no filtro; `aria-expanded` no acordeão e na gaveta. O CSS lê o atributo. Nunca
  crie uma classe `.ativo` paralela.
- **Contraste:** texto vermelho usa `--brand-ink`, nunca `--brand`. Sobre a superfície vermelha,
  branco puro ou branco com alfa mínimo de `.82`. O comentário sobre `saturate()` no `base.css`
  documenta uma falha real de contraste, não o remova.
- **Foco sempre visível**, com anel `--brand` de 2px e `outline-offset: 2px`. Sobre o vermelho,
  anel branco.
- **Gaveta e diálogo** travam o scroll, fecham com Esc e devolvem o foco ao gatilho.
- **Movimento** respeita `prefers-reduced-motion`.
- **Alvos de toque** com pelo menos `2.25rem` de altura, é a medida do `.icobtn`.
- `<svg>` decorativo leva `aria-hidden="true"`; botão só de ícone leva `aria-label`.

## 3. Redação na interface

Vale o [CLAUDE.md](../../CLAUDE.md) inteiro, com três pontos que a tela cobra mais:

- **Travessão (`—`) é proibido**, inclusive no portal. Use vírgula, dois-pontos, ponto médio `·`
  em rótulo ao lado de rótulo, e hífen `-` em célula vazia. A meia-risca `–` continua valendo
  para intervalo: `8–10%`, `S2–S3`, `09–14 set`.
- **Rótulo mono é curto e em maiúsculas.** "Próximo marco", não "Qual é o próximo marco do ciclo".
- **O `.lead` de cada seção diz o que a seção resolve**, não o que ela contém. Comparar:
  "As 78 métricas por camada e prioridade, com fonte e formato de entrega" resolve; "Lista de
  métricas" não.

Data por extenso abreviada e em mono: `24 ago 2026`, `6 out 2026`. Período com meia-risca:
`24 ago 2026 → 24 ago 2027` usa seta porque é travessia, não intervalo fechado.

## 4. Dado na tela

- Conteúdo que muda com frequência vive num array em `assets/*.js` (`form-data.js`,
  `metrics-data.js`, `acessos.js`), não no HTML. Mudar uma pergunta ou uma métrica é editar o
  array; a página se remonta sozinha no navegador.
- A CSP proíbe `connect-src` externo. Dado de terceiro não entra em runtime.
- Data relativa ("em 4 dias", "há 2 semanas") é calculada no cliente a partir de uma data fixa no
  código. Cronograma que mostra data errada é pior que nenhum: a linha de "hoje" do Gantt existe
  por isso.
- Estado do usuário vai para `localStorage` com chave prefixada por `dre-olx-`:
  `dre-olx-tema`, `dre-olx-trilho`, `dre-olx-kickoff-v1`.

## 5. Confidencialidade aplicada ao visual

O portal carrega dado do Grupo OLX e valores de contrato. Isso restringe o que pode aparecer:

- `noindex, nofollow` em toda página, por `<meta>` e por cabeçalho HTTP.
- O rodapé repete o aviso de confidencialidade em toda página. **Não remova o rodapé de uma
  página nova.** Ele vem do `build.py`, então o caminho para perdê-lo é montar HTML fora do build.
- Nenhuma credencial, token ou senha em markup, comentário, captura de tela ou nome de arquivo.
- A aba Kick-off é **interna**: contém pendências contratuais e a divergência de valores. Se um
  material sair para a OLX, confira o que essa aba expõe.

## 6. O que não fazer

| Não | Por quê |
|---|---|
| Editar `index.html` gerado | O build sobrescreve na próxima execução |
| Escrever hex de cor no fragmento | Quebra o tema escuro em silêncio |
| Usar `--brand` em texto pequeno | Não passa em contraste. Use `--brand-ink` |
| Pôr sombra em filho de grade de fio | Duplica a separação e suja a linha de 1px |
| Criar breakpoint novo | Já são sete. Reuse 768, 900 e 1100 |
| Inventar a quinta cor de estado | Quatro estados cobrem o método. Um quinto vira ruído |
| Trocar a família tipográfica | IBM Plex é padrão V4, declarado no CLAUDE.md |
| Carregar biblioteca externa | A CSP bloqueia, e o portal é estático de propósito |
| Escrever o índice da página à mão | O `shell.js` monta a partir dos `<h2>` |
| Esconder pendência para a página ficar bonita | O portal existe para mostrar o que falta |

## 7. Checklist de página nova

1. Fragmento em `_src/<slug>.html` com a linha de metadados completa, cinco campos.
2. `slug` acrescentado ao `NAV` em [`build.py`](../build.py), com rótulo e caminho.
3. Conteúdo em `<section class="blk">`, cada uma abrindo por `.blk-h` com `h2` e um `.lead`.
4. Nenhuma cor fora dos tokens: `grep -nE '#[0-9a-fA-F]{3,6}' _src/<slug>.html` não retorna nada
   que não seja `#fff` sobre a superfície vermelha.
5. Tabela dentro de `.card.scrollx`; número em `.num`.
6. Testado nos dois temas pelo botão da topbar, e a 400px de largura.
7. Testado com o trilho recolhido e com ele aberto.
8. `python3 build.py`, conferir o arquivo gerado, e só então `vercel deploy --prod`.
9. Nenhum número novo sem fonte. O que não tem fonte vira linha em
   [PENDENCIAS.md](../../PENDENCIAS.md) com dono e prazo.
