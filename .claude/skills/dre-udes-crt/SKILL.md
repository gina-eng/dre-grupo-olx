---
name: dre-udes-crt
description: "Coleta 8-15 UDEs (efeitos indesejaveis) e monta a Arvore da Realidade Atual ate as causas-raiz formuladas como politica implicita. Valida ou refuta a restricao apontada na consolidacao. Use quando o operador disser /dre-udes-crt ou 'levantar UDEs' ou 'montar a CRT' ou 'arvore da realidade atual'."
dependencies:
  - dre-consolidacao-causal
tools: []
fase: "2, Otimizar"
estimated_time: "4h (workshop) + 2h de estruturacao"
output_file: "dre-crt.json"
---

# DR-E · UDEs e CRT

Aqui a hipotese de restricao encontra sua validacao logica. A CRT e o unico ponto do metodo onde a trava governante e **confirmada**, o score e a consolidacao apenas apontaram.

> Voce e facilitador do processo de pensar, nao especialista no problema do cliente. Sua funcao e **proteger a logica**, nao impor conclusao. Ver `00-playbook/04-toolkit-ltp.md`, secao 8.

## Passo 0 · Goal Tree

Antes dos UDEs, feche o alvo: **onde o sistema quer chegar**. Sem meta declarada, "efeito indesejavel" nao tem referencia, indesejavel em relacao a que?

Registre: objetivo do sistema em 12 meses, condicoes necessarias para atingi-lo, e quem valida esse objetivo (normalmente o decisor).

## Passo 1 · Coletar UDEs

Pergunta estruturante para o cliente:

> *"O que hoje na sua operacao te incomoda, te trava ou gera frustracao?"*

Colete **8 a 15**. Somente fatos observaveis, nunca opinioes.

Um UDE valido:
- Descreve um efeito negativo **real**
- E **verificavel**
- **Nao contem solucao embutida**

| Ruim | Bom |
|---|---|
| "Falta um CRM decente" (solucao embutida) | "Nao sabemos quantos leads foram contatados na semana" |
| "O time e desorganizado" (opiniao) | "Propostas ficam abertas em media 47 dias sem retorno" |
| "O mercado esta dificil" (nao acionavel) | "O CAC subiu 38% em 12 meses sem aumento de ticket" |

Valide cada UDE com duas perguntas: *"Isso acontece com frequencia?"* e *"Se isso nao acontecesse, o resultado melhoraria?"*

Cruze os UDEs coletados com os `sintomas_confirmados[]` dos diagnosticos de trava. UDE que o diagnostico nao viu e sinal de dado faltante; sintoma que ninguem cita como UDE merece checagem.

## Passo 2 · Montar a CRT

Estrutura: **causas-raiz → efeitos intermediarios → UDEs**.

1. Distribua os UDEs no topo.
2. **Identifique efeitos convergentes.** Pergunta-chave: *"Se corrigirmos isso, quantos desses problemas deixam de existir?"* Ponto que explica varios efeitos e candidato a trava.
3. **Diferencie causa de sintoma.** Teste: *"Isso acontece PORQUE outra coisa esta acontecendo?"* Se sim, e efeito.
4. **Chegue as causas-raiz.** Elas sao falhas de estrutura, processo, definicao estrategica ou priorizacao. **Nunca "as pessoas nao fazem".**
5. **Valide com o cliente:** *"Se essa causa-raiz nao existisse, esses efeitos desapareceriam?"*

### Rigor de linguagem

No LTP, linguagem e logica. Cada seta e uma afirmacao "SE ... ENTAO ...". Antes de aceitar uma seta, teste:

- **Entidade existe?** A causa e o efeito sao verificaveis?
- **Causalidade e suficiente?** Essa causa sozinha produz o efeito, ou falta um elemento?
- **Existe causa alternativa?** Outro caminho produz o mesmo efeito?
- **Ha inversao causa-efeito?**

Frase mal formulada gera relacao causal falsa. Clareza semantica aqui e exigencia metodologica, nao estetica.

## Passo 3 · Confrontar com a consolidacao

Compare a causa-raiz da CRT com `restricao_identificada` e `politica_implicita` do `dados/client.json`:

- **Convergem** → restricao **validada**. Segue.
- **Divergem** → a CRT ganha. Atualize a restricao e registre a correcao em `history[]` com a evidencia logica. Avise o operador antes do comite, mudanca de restricao muda o plano inteiro.

## Como conduzir com o cliente

> "Aqui nao estamos buscando culpados. Estamos mostrando como o sistema esta configurado hoje para produzir exatamente esses resultados."

Se o workshop derivar para defesa de area ou busca de responsavel, pare e reancore nessa frase. CRT com carga politica nao produz causa-raiz honesta.

## Output

Salve `dados/outputs/dre-crt.json` seguindo `.claude/shared-templates/PADRAO-OUTPUT.md` mais:

- `goal_tree`: `objetivo`, `condicoes_necessarias[]`, `validado_por`
- `udes[]`: `id`, `texto`, `verificavel`, `frequencia`, `fonte`, `trava_associada`
- `nos[]`: `id`, `tipo` (`causa_raiz | efeito_intermediario | ude`), `texto`
- `setas[]`: `de`, `para`, `suficiencia`, `causa_alternativa_descartada`
- `causas_raiz[]`: `texto`, `politica_implicita`, `udes_explicados[]`, `cobertura_pct`
- `restricao_validada`: `trava`, `convergiu_com_consolidacao` (boolean), `justificativa`
- `workshop`: data, participantes, facilitador

## Checklist antes de fechar

- [ ] 8 a 15 UDEs, todos verificaveis e sem solucao embutida
- [ ] Toda seta passou nos testes de suficiencia e causa alternativa
- [ ] Causas-raiz sao estruturais, nao comportamentais
- [ ] A causa-raiz principal explica a maioria dos UDEs (registre `cobertura_pct`)
- [ ] Cliente validou a leitura em voz alta
- [ ] Convergencia (ou divergencia) com a consolidacao esta registrada

## Finalizacao

1. Salve `dados/outputs/dre-crt.json`
2. Atualize `dados/client.json`: `restricao_identificada`, version++, `history[]`
3. Escreva a versao humana em `03-estrategia/crt.md`
4. Se ha conflito estrutural por tras da causa-raiz, sugira `/dre-nuvem-conflito`. Se a injecao ja e evidente pela lacuna estrutural, sugira `/dre-frt-prt`
