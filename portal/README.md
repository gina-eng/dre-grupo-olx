# Portal DR-E: Grupo OLX

Sistema único com os três módulos do projeto. Site estático, sem build step.

```
portal/
├── index.html          Painel: status do ciclo, portas e pendências
├── kickoff/            Formulário de kick-off (interno)
├── cronograma/         Cronograma de 12 meses (cliente)
├── metricas/           Dicionário de métricas (cliente)
├── receita/            Árvore de produção de receita (mapa de trabalho)
├── destrava/           Descobertas do ciclo, por fase do método
├── diagnosticos/       Acompanhamento dos nove + biblioteca de documentos
├── assets/             base.css · shell.css · shell.js · logo.svg · dados
├── _src/               Fragmentos-fonte (não publicados)
├── build.py            Gera as páginas a partir de _src/ e da BIBLIOTECA
├── md.py               Markdown → HTML, sem dependência externa
└── vercel.json         cleanUrls, noindex e cabeçalhos de segurança
```

## Editar

Nunca edite os `index.html` gerados: eles são sobrescritos. Edite o fragmento
correspondente em `_src/` e rode:

```bash
python3 build.py
```

Cada fragmento abre com uma linha de metadados que alimenta o `<head>` e a faixa de contexto:

```
<!--@ slug | título da aba | título da página | descrição | meta lateral -->
```

O conteúdo do formulário vive em `assets/form-data.js`; o das métricas, em `assets/metrics-data.js`.
Alterar uma pergunta ou uma métrica é editar o array, o HTML se regenera sozinho no navegador.

## Biblioteca: publicar documento do repositório

A aba **Diagnósticos** tem duas partes. O acompanhamento dos nove diagnósticos é markup à mão, em
`_src/diagnosticos.html`. A biblioteca abaixo dele é gerada: a lista `BIBLIOTECA`, em `build.py`,
diz quais arquivos `.md` do repositório viram página do portal, e o marcador `<!--@biblioteca-->`
no fragmento recebe os cartões.

Para publicar mais um documento, acrescente uma linha na `BIBLIOTECA` e rode o build:

```python
dict(slug="url-no-portal", grupo="sistema",
     origem="02-diagnostico/arquivo.md",
     titulo="Como aparece no cartão", selo="estado", tom="ok",
     resumo="Uma frase sobre o que o documento é."),
```

Três coisas valem a pena saber antes de acrescentar uma linha:

- **A lista é o filtro de confidencialidade.** Não há varredura de pasta: o que não está na
  `BIBLIOTECA` não é publicado. Transcrição integral, `PENDENCIAS.md`, contrato e material de
  método da V4 ficam de fora de propósito.
- **Link entre documentos se resolve sozinho.** Link para arquivo que está na lista vira URL do
  portal, com âncora; link para arquivo que não está perde o destino e continua como texto, com
  ressalva no `title`.
- **Todo HTML dentro do Markdown é escapado**, então documento com `<script>` no meio do texto sai
  como texto. Âncoras de título seguem a regra do GitHub, que é o que faz `#secao` continuar
  apontando para o lugar certo.

## Rodar local

```bash
python3 -m http.server 8899 --directory .
```

## Publicar

```bash
vercel --prod
```

O projeto tem **proteção por senha** ativa: o link só abre com a senha. Sem isso, os valores do
contrato e os dados do Grupo OLX ficariam numa URL pública e indexável.
