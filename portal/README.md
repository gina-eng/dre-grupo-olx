# Portal DR-E: Grupo OLX

Sistema único com os três módulos do projeto. Site estático, sem build step.

```
portal/
├── index.html          Painel: status do ciclo, portas e pendências
├── kickoff/            Formulário de kick-off (interno)
├── cronograma/         Cronograma de 12 meses (cliente)
├── metricas/           Dicionário de métricas (cliente)
├── assets/             base.css · shell.css · shell.js · logo.svg · dados
├── _src/               Fragmentos-fonte (não publicados)
├── build.py            Gera as páginas a partir de _src/
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
