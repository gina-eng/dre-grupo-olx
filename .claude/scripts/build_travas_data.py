#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_travas_data.py: gera o asset do Placar das 8 Travas para o portal.

Le o estado de maquina produzido pela skill dre-diagnostico-trava e escreve
portal/assets/travas-data.js. O portal nunca guarda numero proprio: tudo que a
tela mostra vem daqui, e regerar o asset e a unica forma de atualizar a tela.

Campos exportados sao os que existem no JSON. Em particular NAO existe grau
probatorio por dimensao ([D] declarado, apurado, formal): esse grau vive dentro
do texto de `evidencia`, em prosa, e e por isso que a tela mostra a evidencia
inteira em vez de um selo derivado, que seria dado inventado (regra 1).

Uso:
    python3 .claude/scripts/build_travas_data.py
"""
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
ENTRADA = RAIZ / "dados" / "outputs" / "dre-diagnostico-travas.json"
SAIDA = RAIZ / "portal" / "assets" / "travas-data.js"

# A regra 6 do repositorio limita a nota a 3 sem evidencia formal. O teto por
# dimensao e 3, entao o maximo praticavel de uma trava com as 5 dimensoes
# pontuadas e 15, e nao os 25 da escala do playbook.
TETO_POR_DIMENSAO = 3
ESCALA_PLAYBOOK = 25


def normaliza(score, pontuadas):
    """Equivalente na escala de 25 do playbook, so quando as 5 dimensoes existem.

    Com dimensao faltando nao ha denominador: devolve None em vez de estimar,
    que e o que o proprio dossie faz nas seis travas incompletas.
    """
    if score is None or pontuadas != 5:
        return None
    return round(score / (pontuadas * TETO_POR_DIMENSAO) * ESCALA_PLAYBOOK, 1)


def main():
    if not ENTRADA.exists():
        sys.exit(f"nao encontrei {ENTRADA}")
    d = json.loads(ENTRADA.read_text(encoding="utf-8"))

    travas = []
    for t in d["travas"]:
        dims = t.get("dimensoes", [])
        notas = [x.get("nota") for x in dims]
        pontuadas = [n for n in notas if n is not None]
        travas.append({
            "nome": t["nome"],
            "score_total": t.get("score_total"),
            "pontuadas": len(pontuadas),
            "total_dimensoes": len(dims),
            "soma_atribuida": sum(pontuadas) if pontuadas else None,
            "maximo_praticavel": len(pontuadas) * TETO_POR_DIMENSAO if pontuadas else None,
            # Unica comparacao defensavel entre travas com numero diferente de
            # dimensoes pontuadas, e o proprio dossie a usa nesse papel.
            "media_por_dimensao": round(sum(pontuadas) / len(pontuadas), 2) if pontuadas else None,
            "normalizado_25": normaliza(t.get("score_total"), len(pontuadas)),
            "confiabilidade": t.get("confiabilidade"),
            "escala": t.get("score_parcial") or "",
            "politica_implicita": t.get("politica_implicita") or "",
            "interpretacao": t.get("interpretacao") or "",
            "o_que_falta": t.get("o_que_falta") or "",
            "dimensoes": [{
                "nome": x["dimensao"],
                "nota": x.get("nota"),
                "natureza": x.get("natureza"),
                "evidencia": x.get("evidencia") or "",
            } for x in dims],
        })

    payload = {
        "meta": d.get("meta", {}),
        "teto_por_dimensao": TETO_POR_DIMENSAO,
        "travas": travas,
        "candidata_a_restricao": d.get("candidata_a_restricao") or "",
        "por_que_nao_e_conclusiva": d.get("por_que_nao_e_conclusiva") or "",
        "gate_consolidacao": d.get("gate_consolidacao") or "",
        "alerta_denominador_publicacao": d.get("alerta_denominador_publicacao") or "",
    }

    cabecalho = (
        "// GERADO POR .claude/scripts/build_travas_data.py, NAO EDITE A MAO.\n"
        "// Fonte: dados/outputs/dre-diagnostico-travas.json\n"
        f"// Estado da fonte: {payload['meta'].get('estado', 'nao declarado')}\n"
    )
    corpo = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    SAIDA.write_text(f"{cabecalho}const TRAVAS = {corpo};\n", encoding="utf-8")

    sem_score = [t["nome"] for t in travas if t["score_total"] is None]
    print(f"  {SAIDA.relative_to(RAIZ)}  ({SAIDA.stat().st_size:,} bytes)")
    print(f"  {len(travas)} travas · {len(travas) - len(sem_score)} com score fechado")
    print(f"  sem score: {', '.join(sem_score)}")


if __name__ == "__main__":
    main()
