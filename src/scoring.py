"""Quick-Scan DRA Scoring Engine.

Aligned with DRA framework (src/scoring.py in DRA repo).
7 questions, 3 Knowledge Areas (DMBOK2), scale 0-4 (CMM simplified), scoring 0-100%.
"""

from src.models import (
    KAScore,
    KnowledgeArea,
    NivelMadurez,
    QuickScanForm,
    QuickScanResult,
)

QUESTIONS = ["q1", "q2", "q3", "q4", "q5", "q6", "q7"]

QUESTION_LABELS = {
    "q1": "Gobernanza de Datos",
    "q2": "Control de Acceso",
    "q3": "Proteccion Tecnica",
    "q4": "Flujo de Datos",
    "q5": "Consentimiento y Derechos ARCOP",
    "q6": "Capacitacion",
    "q7": "Respuesta a Incidentes",
}

# Mapping: question → Knowledge Area (DMBOK2)
KA_MAPPING: dict[str, KnowledgeArea] = {
    "q1": KnowledgeArea.GOVERNANCE,
    "q2": KnowledgeArea.SECURITY,
    "q3": KnowledgeArea.SECURITY,
    "q4": KnowledgeArea.INTEGRATION,
    "q5": KnowledgeArea.INTEGRATION,
    "q6": KnowledgeArea.GOVERNANCE,
    "q7": KnowledgeArea.SECURITY,
}

KA_NAMES = {
    KnowledgeArea.GOVERNANCE: "Data Governance",
    KnowledgeArea.SECURITY: "Data Security",
    KnowledgeArea.INTEGRATION: "Data Integration & Interoperability",
}

LEVELS = [
    (0, 25, NivelMadurez.CRITICO, "DRA Assessment urgente — minimo 3 Knowledge Areas. Alto riesgo regulatorio ante la Ley 21.719."),
    (26, 50, NivelMadurez.BAJO, "DRA Assessment recomendado — priorizar las Knowledge Areas con peor score para cerrar brechas criticas."),
    (51, 75, NivelMadurez.MEDIO, "DRA Assessment selectivo — foco en gaps especificos identificados en las areas mas debiles."),
    (76, 100, NivelMadurez.ALTO, "Buen nivel de madurez. Recomendamos DRA lite o monitoreo periodico para mantener el cumplimiento."),
]


def calcular_score(form: QuickScanForm) -> QuickScanResult:
    """Calculate Quick-Scan DRA score from form submission."""

    responses = {q: getattr(form, q) for q in QUESTIONS}
    total = sum(responses.values())
    max_score = len(QUESTIONS) * 4  # 28
    percentage = round((total / max_score) * 100)

    # Determine level
    nivel = NivelMadurez.CRITICO
    recommendation = ""
    for low, high, lv, rec in LEVELS:
        if low <= percentage <= high:
            nivel = lv
            recommendation = rec
            break

    # Calculate KA scores
    ka_totals: dict[KnowledgeArea, list[int]] = {}
    ka_questions: dict[KnowledgeArea, list[str]] = {}
    for q in QUESTIONS:
        ka = KA_MAPPING[q]
        ka_totals.setdefault(ka, []).append(responses[q])
        ka_questions.setdefault(ka, []).append(q)

    ka_scores = []
    ka_averages: dict[KnowledgeArea, float] = {}
    for ka in [KnowledgeArea.GOVERNANCE, KnowledgeArea.SECURITY, KnowledgeArea.INTEGRATION]:
        scores = ka_totals.get(ka, [0])
        avg = sum(scores) / len(scores)
        pct = round((avg / 4) * 100)
        ka_averages[ka] = avg
        ka_scores.append(KAScore(
            ka=ka,
            name=KA_NAMES[ka],
            average=round(avg, 2),
            percentage=pct,
            questions=ka_questions.get(ka, []),
        ))

    # Critical area (lowest KA average)
    critical_area = min(ka_averages, key=lambda k: ka_averages[k])

    # Suggested KAs sorted by score ascending (most needy first)
    suggested_kas = sorted(ka_averages, key=lambda k: ka_averages[k])

    # Financial exposure
    if nivel == NivelMadurez.CRITICO:
        exposure = "USD $350,000 - $1,400,000 (multas graves a gravisimas)"
    elif nivel == NivelMadurez.BAJO:
        exposure = "USD $50,000 - $700,000 (multas leves a graves)"
    elif nivel == NivelMadurez.MEDIO:
        exposure = "Exposicion moderada — brechas especificas pueden generar multas leves"
    else:
        exposure = "Riesgo financiero bajo con controles actuales"

    return QuickScanResult(
        nombre_contacto=form.nombre_contacto,
        email=form.email,
        empresa=form.empresa,
        tamano=form.tamano,
        sector=form.sector,
        cargo=form.cargo,
        score_total=total,
        score_max=max_score,
        score_percentage=percentage,
        nivel=nivel,
        ka_scores=ka_scores,
        critical_area=critical_area,
        suggested_kas=suggested_kas,
        recommendation=recommendation,
        exposure=exposure,
        responses=responses,
    )
