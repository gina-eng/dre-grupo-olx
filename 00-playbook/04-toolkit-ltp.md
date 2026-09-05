# Toolkit LTP · Logical Thinking Process

O LTP não é um conjunto de ferramentas visuais. É um **processo disciplinado de raciocínio**
baseado em causa e efeito, criado para transformar intuição difusa em lógica explícita.

Origem: Teoria das Restrições (Goldratt), formalizado por **H. William Dettmer**.
Enquanto a TOC responde *onde focar*, o LTP responde *como pensar*.

> **Os diagramas não são o pensamento, são a representação dele.** Quando o foco se desloca para o
> desenho, o método se perde.

## Quando usar

O LTP é desnecessário para problemas simples e ineficiente para problemas puramente técnicos.
Seu campo são os **problemas complexos**: múltiplos efeitos indesejáveis simultâneos, relações de
causa não óbvias, conflitos legítimos entre objetivos, soluções anteriores que pioraram a situação,
forte carga política ou emocional.

## Sequência canônica

| Etapa | Pergunta que responde | Obrigatória? |
|---|---|---|
| **Goal Tree / IO Map** | Onde queremos chegar? | Sim |
| **UDEs** | Quais são os sintomas reais? | Sim |
| **CRT** | Por que o sistema produz os resultados atuais? | Sim |
| **Nuvem de Conflito** | Qual conflito estrutural mantém a trava ativa? | Quando há conflito |
| **Injeção** | Qual nova regra elimina a causa-raiz? | Sim |
| **FRT** | O que acontece quando a injeção é verdadeira? | Sim |
| **PRT** | O que pode impedir a injeção de acontecer? | Quando há obstáculos |
| **Árvore de Transição** | O que fazer, em que ordem? | Sim |

> **Ordem importa.** Cada etapa prepara cognitivamente a próxima. Pular etapas gera análises frágeis
> e soluções enviesadas.

## 1. UDEs · Efeitos Indesejáveis

Ponto de partida. Um UDE é um **padrão recorrente**, não um evento isolado.

**Pergunta estruturante:** *"O que hoje na sua operação te incomoda, te trava ou gera frustração?"*

**Formato correto:**
- Descreve um efeito negativo real
- É verificável
- **Não contém solução embutida**

Coletar **8 a 15 UDEs**. Somente fatos observáveis, nunca opiniões.

**Validação de cada UDE:** *"Isso acontece com frequência?"* · *"Se isso não acontecesse, o resultado melhoraria?"*

*Exemplos:* leads chegam mas não convertem · o time comercial reclama da qualidade dos leads ·
vendas demoram para fechar · CAC está alto · o cliente não consegue escalar investimento.

## 2. CRT · Árvore da Realidade Atual

**Estrutura:** Causas-raízes → Efeitos intermediários → Efeitos indesejáveis (UDEs)

**Passo a passo:**
1. Coletar e validar os UDEs.
2. **Identificar efeitos convergentes**: vários problemas apontando para a mesma causa. Pergunta-chave: *"Se corrigirmos isso, quantos desses problemas deixam de existir?"* Quando um ponto explica vários efeitos → possível trava.
3. **Diferenciar causa de sintoma**: teste lógico: *"Isso acontece PORQUE outra coisa está acontecendo?"* Se sim, é efeito, não causa-raiz.
4. **Chegar às causas-raízes**: normalmente falhas de estrutura, processo, definição estratégica ou priorização. **Nunca "as pessoas não fazem".**
5. **Validar com o cliente**: *"Se essa causa-raiz não existisse, esses efeitos desapareceriam?"*

**Como explicar ao cliente:**
> "Aqui não estamos buscando culpados. Estamos mostrando como o sistema está configurado hoje
> para produzir exatamente esses resultados."

**Saída:** poucos pontos de origem que sustentam a maioria dos problemas + evidência lógica da trava.
A causa-raiz é sempre formulada como **política implícita**.

## 3. Nuvem de Conflito (Evaporating Cloud)

**Quando aplicar:** decisões recorrentes que travam o sistema · oscilação entre duas estratégias ·
conflito entre áreas · tentativas repetidas que não resolvem · CRT indicando causa-raiz ligada a
escolha estrutural.

**Estrutura:**
```
Objetivo Comum (A)
├── Necessidade B → Ação D
└── Necessidade C → Ação D'
```
As ações D e D' parecem necessárias, mas são mutuamente excludentes.

**Passo a passo:**
1. Identificar o conflito central, *"Onde vocês sentem que precisam escolher entre duas coisas importantes?"* (crescer rápido vs. manter qualidade; escalar mídia vs. manter ROI)
2. Definir o objetivo comum (A)
3. Identificar necessidades (B e C), *"Por que cada lado acredita que sua escolha é necessária?"*
4. Identificar ações em conflito (D e D')
5. Validar o conflito com o cliente
6. **Identificar premissas**: *"Por que acreditam que essa ação é a única forma? Isso é sempre verdade? O que teria que mudar para que ambas as necessidades fossem atendidas?"*
7. **Desafiar premissas e gerar a injeção**

**Como explicar ao cliente:**
> "Vocês não têm um problema de execução. Estão presos a um conflito que obriga o sistema a
> escolher entre duas coisas importantes. A solução surge quando quebramos a premissa que faz
> esse conflito existir."

## 4. Injeção

A Injeção é a **nova regra do sistema**. Não é uma ação isolada, é mudança de política, critério
ou lógica decisória que elimina a causa-raiz.

**Uma boa injeção:**
- Resolve o problema central
- Não cria novos conflitos
- É logicamente inevitável à luz da análise

*Exemplo:* "Focar em ICP restrito e diferenciação clara em vez de volume por preço."

**Origens possíveis da injeção:** CRT direta (lacuna estrutural) · Goal Tree (requisito inexistente) ·
Nuvem de Conflito (quebra de conflito) · Auditoria/dados (ausência objetiva de estrutura).

## 5. FRT · Árvore da Realidade Futura

**Estrutura:** Injeção → Efeitos intermediários → Efeitos desejados

**Passo a passo:**
1. Posicionar a injeção.
2. Projetar os primeiros efeitos: *SE (injeção) → ENTÃO (efeito positivo)*.
3. **Conectar aos UDEs:** para cada UDE da CRT, *"Esse problema ainda existiria se a injeção fosse verdadeira?"* Conectar o UDE ao efeito desejado que o substitui.
4. Expandir a cadeia até alcançar: previsibilidade, eficiência, crescimento, escala.
5. **Identificar efeitos colaterais:** *"Essa mudança pode gerar novos problemas?"* Se sim, registrar e prever proteção.
6. Validação final: *"Se isso for verdade, o sistema passa a produzir os resultados desejados?"*

**Como explicar ao cliente:**
> "Aqui estamos vendo o sistema funcionando sob novas condições. Não é previsão, é consequência lógica."

**Nenhuma solução é considerada válida sem passar pela FRT.**

## 6. PRT · Árvore de Pré-Requisitos

**Usar somente quando há obstáculos relevantes:** injeção estrutural ou complexa · resistência do
cliente · faltam recursos, pessoas ou sistema · mudança envolve várias áreas · cliente diz "não dá
para fazer agora".

**Não usar quando** a injeção é simples, não há resistência e a implementação é direta, nesse caso,
ir direto para a Árvore de Transição.

**Estrutura:** Injeção → Obstáculos → Condições necessárias para superá-los

| Obstáculo | Condição necessária |
|---|---|
| Time não sabe fazer | Treinamento estruturado |
| Falta CRM | Sistema implementado |
| Faltam dados | Métricas definidas |

**Validação:** *"Se essas condições existirem, a implementação fica viável?"*

**Como explicar ao cliente:**
> "A solução está clara. Agora estamos garantindo que nada impeça ela de acontecer."

## 7. Árvore de Transição

O momento em que o diagnóstico vira **plano executável**.

**Estrutura:** Ação → Efeito intermediário → Novo estado do sistema

**Passo a passo:**
1. Posicionar a injeção validada.
2. *"Qual é o primeiro movimento que precisa acontecer para isso se tornar possível?"*
3. *"Se essa ação acontecer, o que passa a ser possível que antes não era?"*
4. Repetir o ciclo: Ação → Efeito → Nova condição → Próxima ação.
5. **Testar a lógica:** para cada passo, *"Se isso não acontecer, o próximo passo ainda é possível?"* Se não, a ordem está correta.
6. Validar completude: *"Essa sequência garante que a injeção se torne realidade?"*

**Exemplo (injeção: ICP definido e aplicado):**

| Ação | Efeito intermediário | Resultado |
|---|---|---|
| Levantar base de clientes atuais | Identificação de perfis recorrentes | Base para ICP |
| Definir ICP | Clareza de público-alvo | Segmentação possível |
| Ajustar campanhas | Mensagens alinhadas | Leads qualificados |
| Ajustar abordagem comercial | Conversas mais relevantes | Conversão aumenta |
| Otimizar funil | Eficiência melhora | Receita escala |

**Como explicar ao cliente:**
> "Aqui não estamos listando tarefas. Estamos organizando a sequência lógica que faz o sistema
> mudar de estado."

## 8. O papel do facilitador

O facilitador do LTP não é especialista no problema, mas no **processo de pensar**.
Sua função é **proteger a lógica**, não impor conclusões. Exige neutralidade, rigor e coragem intelectual.

**No LTP, linguagem é lógica.** Frases mal formuladas geram relações causais falsas.
Clareza semântica é exigência metodológica, não estética.
