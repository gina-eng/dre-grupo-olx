---
name: dre-nuvem-conflito
description: "Monta a Nuvem de Conflito (Evaporating Cloud) sobre a causa-raiz, explicita as premissas que sustentam o conflito e gera a Injecao. Use quando o operador disser /dre-nuvem-conflito ou 'nuvem de conflito' ou 'evaporating cloud' ou 'gerar a injecao'."
dependencies:
  - dre-udes-crt
tools: []
fase: "2, Otimizar"
estimated_time: "3h"
output_file: "dre-nuvem-conflito.json"
---

# DR-E · Nuvem de Conflito e Injecao

A CRT mostrou **o que** trava. A Nuvem mostra **por que continua travado**, o conflito estrutural que faz a organizacao repetir a mesma escolha, mesmo sabendo que ela custa caro.

## Quando aplicar

- Decisoes recorrentes que travam o sistema
- Oscilacao entre duas estrategias
- Conflito entre areas
- Tentativas repetidas que nao resolvem
- CRT indicando causa-raiz ligada a escolha estrutural

Se nao ha conflito, a causa-raiz e uma lacuna pura (falta uma estrutura que nunca existiu), pule para `/dre-frt-prt`, gerando a injecao direto da lacuna.

## Estrutura

```
Objetivo Comum (A)
├── Necessidade B → Acao D
└── Necessidade C → Acao D'
```

D e D' parecem ambas necessarias, e sao mutuamente excludentes.

## Passo a passo

1. **Identificar o conflito central.** Pergunta: *"Onde voces sentem que precisam escolher entre duas coisas importantes?"* Exemplos tipicos: crescer rapido vs. manter qualidade; escalar midia vs. manter ROI; padronizar a oferta vs. atender o pedido do cliente grande.
2. **Definir o objetivo comum (A).** Precisa ser algo que os dois lados assinam embaixo. Se um lado nao reconhece o objetivo, a nuvem esta mal montada.
3. **Identificar as necessidades (B e C).** *"Por que cada lado acredita que sua escolha e necessaria?"* Necessidade nao e acao, e a condicao que a acao busca proteger.
4. **Identificar as acoes em conflito (D e D').**
5. **Validar o conflito com o cliente.** Leia a nuvem em voz alta: "Para atingir A precisamos de B, e para ter B fazemos D. Ao mesmo tempo, para atingir A precisamos de C, e para ter C fazemos D'. Mas D e D' nao cabem juntos." O cliente precisa dizer "e exatamente isso".
6. **Identificar as premissas.** Para cada seta (A-B, A-C, B-D, C-D', D-D'), pergunte: *"Por que acreditam que essa acao e a unica forma? Isso e sempre verdade? O que teria que mudar para que ambas as necessidades fossem atendidas?"*
7. **Desafiar as premissas e gerar a Injecao.**

> A premissa mais produtiva de atacar quase sempre esta em **B-D** ou **C-D'**: a crenca de que aquela necessidade so pode ser atendida por aquela acao. O conflito D-D' costuma ser real; a exclusividade da acao raramente e.

## A Injecao

A Injecao e a **nova regra do sistema**, mudanca de politica, criterio ou logica decisoria que elimina a causa-raiz. Nao e uma acao isolada, nao e um projeto, nao e uma ferramenta.

Uma boa injecao:
- **Resolve o problema central** (ataca a causa-raiz da CRT, nao um efeito)
- **Nao cria novos conflitos** (checar na FRT)
- **E logicamente inevitavel** a luz da analise, o cliente ouve e responde "nao tem outro jeito mesmo"

Exemplo: *"Focar em ICP restrito e diferenciacao clara em vez de volume por preco."*

Origens possiveis: quebra de premissa da nuvem · lacuna estrutural direta da CRT · requisito inexistente na Goal Tree · ausencia objetiva de estrutura apontada por auditoria.

### Teste da injecao antes de seguir

- [ ] E uma **regra**, nao uma tarefa? (se cabe num card de sprint, ainda nao e injecao)
- [ ] Ela seria falsa hoje? (se ja e verdade na operacao, nao muda nada)
- [ ] Qual premissa ela quebra? (nomeie)
- [ ] Que politica implicita ela substitui? (parear com `politica_implicita` da consolidacao)

## Como conduzir com o cliente

> "Voces nao tem um problema de execucao. Estao presos a um conflito que obriga o sistema a escolher entre duas coisas importantes. A solucao surge quando quebramos a premissa que faz esse conflito existir."

## Output

Salve `dados/outputs/dre-nuvem-conflito.json` com:

- `objetivo_comum` (A)
- `necessidade_b`, `acao_d`, `necessidade_c`, `acao_d_linha`
- `premissas[]`: `seta`, `premissa`, `sempre_verdade` (boolean), `evidencia_contraria`
- `premissa_quebrada`: a que sustenta o conflito
- `injecao`: `texto`, `politica_substituida`, `premissa_quebrada`, `passou_nos_testes` (boolean)
- `validacao_cliente`: data, quem validou, frase de confirmacao

## Finalizacao

1. Salve `dados/outputs/dre-nuvem-conflito.json`
2. Atualize `dados/client.json`, version++, `history[]`
3. Escreva a versao humana em `03-estrategia/nuvem-de-conflito.md`
4. Sugira `/dre-frt-prt`, nenhuma solucao e valida sem passar pela FRT
