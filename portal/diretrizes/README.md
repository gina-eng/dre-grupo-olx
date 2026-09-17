# Diretrizes visuais do Portal DR-E

Descrição da linguagem visual que já está publicada em
<https://portal-dre-grupo-olx.vercel.app>. Serve para que uma página nova nasça igual às cinco
que existem, e para que quem mexer numa delas saiba o que pode mudar sem quebrar o conjunto.

**A fonte da verdade é o CSS, não este texto.** Os tokens vivem em
[`assets/base.css`](../assets/base.css) e o chrome em [`assets/shell.css`](../assets/shell.css).
Se um valor aqui divergir do arquivo, o arquivo está certo e este texto está velho: corrija o texto.

| Arquivo | O que responde |
|---|---|
| [01-fundamentos.md](01-fundamentos.md) | Cor, tema claro e escuro, tipografia, escala, raio, sombra, foco |
| [02-estrutura.md](02-estrutura.md) | Chrome do sistema, layout de página, grade, como o build monta tudo |
| [03-componentes.md](03-componentes.md) | Catálogo com o markup de cada peça recorrente |
| [04-regras.md](04-regras.md) | Semântica de estado, acessibilidade, redação, o que não fazer |
| [amostra.html](amostra.html) | Folha de espécimes viva, carrega o CSS real do portal |

## Como usar

Antes de desenhar uma aba nova, leia [02-estrutura.md](02-estrutura.md) e copie a anatomia de
`_src/destrava.html`, que é o fragmento mais limpo. Antes de inventar um componente, procure em
[03-componentes.md](03-componentes.md): quase tudo que uma página de diagnóstico precisa já existe.

Para ver o sistema renderizado, com alternância de tema:

```bash
cd portal
python3 -m http.server 8899 --directory .
# abre http://localhost:8899/diretrizes/amostra.html
```

A amostra aponta para `../assets/base.css` e `../assets/shell.css`, então os tokens nunca
divergem do portal. Só o markup dela pode envelhecer.

## O que esta pasta não é

Não é o manual de marca da V4 nem o do Grupo OLX. É a descrição de um sistema específico,
construído para este portal. As decisões de marca que ele herda, vermelho V4 e IBM Plex, estão
registradas em [CLAUDE.md](../../CLAUDE.md) na seção de redação e tipografia.

Esta pasta não é publicada: está em [`.vercelignore`](../.vercelignore).
