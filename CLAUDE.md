# DR-E · Grupo OLX — instruções do repositório

Repositório central do projeto **Destrava Receita Estratégico (DR-E)** da V4 Company para o **Grupo OLX**.

## Confidencialidade (leia antes de qualquer coisa)

- As comunicações da OLX carregam aviso de confidencialidade que **proíbe compartilhamento com terceiros sem autorização escrita**. O repositório é **privado** por isso e deve continuar privado.
- Cláusula 5.3 do contrato: é vedado subcontratar atividades de tratamento de dados sem autorização expressa prévia da OLX.
- Acessos de plataforma são concedidos **apenas** a `gina@v4company.com`.
- **Nenhuma credencial no repositório.** O `.gitignore` bloqueia `.env*`, `.credentials/`, `*credentials*.json`, `service-account*.json`, `*.pem`, `*.key`. Se precisar de segredo, use variável de ambiente.
- Não publique conteúdo deste repo em serviço externo (artifact, gist, paste) sem pedido explícito.

## Estrutura

| Pasta | Conteúdo | Quem escreve |
|---|---|---|
| `00-playbook/` | Método DR-OTE/DR-E. **Fonte da verdade metodológica** | Só muda se o método da V4 mudar |
| `01-cliente/` | Perfil, stakeholders, acessos, histórico de onboarding | Humano + `dre-onboarding` |
| `02-diagnostico/` | Checklist de dados, auditorias contratadas, dossiês de trava | Skills de diagnóstico |
| `03-estrategia/` | CRT, nuvem, FRT/PRT, plano de 90 dias, forecast, matriz de expansão | Skills da fase 2–4 |
| `04-execucao/` | Contrato e escopo, cronograma e marcos | Humano |
| `05-resultados/` | Revisões de ciclo, previsto vs. realizado | `dre-revisao-ciclo` |
| `06-reunioes/` | Pautas e atas | `dre-comite`, `dre-tira-duvidas` |
| `dados/` | **Estado de máquina**: `client.json`, `outputs/`, `cache/` | Só skills |
| `.claude/skills/` | Skills `dre-*` (próprias) e `ee-*` (reaproveitadas) | — |
| `PENDENCIAS.md` | Bloqueios abertos, com severidade, dono e prazo | Todos |

**Dois níveis de registro, sempre em par:** `dados/outputs/*.json` é a versão de máquina; o `.md` na pasta temática é a versão que o humano lê e que vira material de comitê. Skill que gera um sem o outro está incompleta.

## Estado

`dados/client.json` é a fonte única de estado. Toda skill que o altera deve:

1. incrementar `meta.version`
2. atualizar `meta.atualizado_em`
3. acrescentar entrada em `history[]` com data e o que mudou

`progress.skills` usa `pending | in_progress | completed`. **`approved` é exclusivo da Matriz do GP.**

## Regras do método que valem como regras do repositório

1. **Nada de número sem fonte.** Campo sem dado fica `null` e vira linha em `PENDENCIAS.md` com dono e prazo — nunca um valor inventado ou "aproximado".
2. **Estimativa é marcada.** `[E]` no texto, `"estimado": true` no JSON.
3. **Uma restrição por vez.** O sistema tem uma trava governante. Material que aponta "três focos" está errado.
4. **Não há comitê sem Matriz aprovada.** Bloqueio duro, verificado por `dre-comite`.
5. **Causa-raiz é política, não pessoa.** "As pessoas não fazem" nunca é causa-raiz.
6. **Nota acima de 3 exige evidência formal** no score de trava. Percepção do time não sustenta 4 ou 5.
7. **Travas são citadas pelo nome**, nunca pelo número — os documentos-fonte da V4 usam três numerações conflitantes (ver `00-playbook/02-travas-de-receita.md` e `PENDENCIAS.md`).
8. **A receita derivada do funil bate com a declarada.** Divergência acima de 5% significa dado inconsistente, não faturamento errado.
9. **Toda decisão vai para ata.** Decisão que só existe na memória da reunião não existe.

## Por onde começar

`/dre-continuar` lê o estado e diz qual é o próximo passo. Índice das skills em `.claude/skills/README.md`.
