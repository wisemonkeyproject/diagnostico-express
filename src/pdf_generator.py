"""PDF report generator for Ley 21.719 diagnostic results.

Uses fpdf2 to generate a branded report with scoring, risk levels, and recommendations.
"""

import os
from pathlib import Path

from fpdf import FPDF

from src.models import DiagnosticoResult, NivelRiesgo

OUTPUT_DIR = Path(__file__).parent.parent / "data" / "reports"
CALENDLY_URL = os.getenv("CALENDLY_URL", "https://calendly.com/twmp")


class DiagnosticoPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "The Wise Monkey Project", align="L")
        self.cell(0, 8, "Diagnostico Express - Ley 21.719", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 102, 204)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Pagina {self.page_no()}/{{nb}}", align="C")


def _color_for_risk(nivel: NivelRiesgo) -> tuple[int, int, int]:
    if nivel == NivelRiesgo.ALTO:
        return (220, 53, 69)
    elif nivel == NivelRiesgo.MEDIO:
        return (255, 193, 7)
    return (40, 167, 69)


def _color_for_pct(pct: float) -> tuple[int, int, int]:
    if pct > 45:
        return (220, 53, 69)
    elif pct > 20:
        return (255, 193, 7)
    return (40, 167, 69)


def generar_pdf(result: DiagnosticoResult) -> str:
    """Generate PDF report and return file path."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in result.empresa)
    filename = f"diagnostico_{safe_name}_{result.score_normalizado:.0f}pct.pdf"
    filepath = OUTPUT_DIR / filename

    pdf = DiagnosticoPDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=20)

    # Title
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 12, "Reporte de Diagnostico Express", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "Proteccion y Gobernanza de Datos - Ley 21.719", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # Company info box
    pdf.set_fill_color(245, 245, 250)
    pdf.set_draw_color(200, 200, 210)
    y_start = pdf.get_y()
    pdf.rect(10, y_start, 190, 30, style="DF")
    pdf.set_xy(15, y_start + 3)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(90, 7, f"Empresa: {result.empresa}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(15)
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(90, 6, f"Contacto: {result.nombre_contacto}", new_x="END")
    pdf.cell(0, 6, f"Cargo: {result.cargo or 'No especificado'}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(15)
    pdf.cell(90, 6, f"Sector: {result.sector.value.title()}", new_x="END")
    pdf.cell(0, 6, f"Tamano: {result.tamano.value.replace('_', '/').title()}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(y_start + 33)

    # Risk level banner
    r, g, b = _color_for_risk(result.nivel_riesgo)
    pdf.set_fill_color(r, g, b)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 14, f"  Nivel de Riesgo: {result.nivel_riesgo.value}", fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    # Score summary
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 7, f"Score Global: {result.score_total}/{result.score_max} ({result.score_normalizado}%)", new_x="LMARGIN", new_y="NEXT")

    if result.gatillos_activados:
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(220, 53, 69)
        pdf.cell(0, 7, "ALERTAS CRITICAS DETECTADAS:", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 10)
        for gatillo in result.gatillos_activados:
            pdf.cell(0, 6, f"  ! {gatillo}", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(5)

    # Dimension scores with bar chart
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Score por Dimension", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    bar_width = 100
    bar_height = 8
    label_width = 70

    for dim in result.dimensiones:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(label_width, bar_height, f"{dim.nombre} [{dim.peso}]", new_x="END")

        # Background bar
        x_bar = pdf.get_x()
        y_bar = pdf.get_y()
        pdf.set_fill_color(230, 230, 235)
        pdf.rect(x_bar, y_bar, bar_width, bar_height, style="F")

        # Filled bar
        fill_width = (dim.porcentaje / 100) * bar_width
        r, g, b = _color_for_pct(dim.porcentaje)
        pdf.set_fill_color(r, g, b)
        if fill_width > 0:
            pdf.rect(x_bar, y_bar, fill_width, bar_height, style="F")

        # Percentage text
        pdf.set_xy(x_bar + bar_width + 3, y_bar)
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(r, g, b)
        pdf.cell(15, bar_height, f"{dim.porcentaje:.0f}%", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(8)

    # Top gaps
    if result.brechas_principales:
        pdf.set_text_color(30, 30, 30)
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Principales Brechas Identificadas", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 10)
        for i, brecha in enumerate(result.brechas_principales, 1):
            pdf.set_text_color(80, 80, 80)
            pdf.cell(0, 7, f"  {i}. {brecha}", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(5)

    # Financial exposure
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 10, "Estimacion de Exposicion Financiera", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 7, result.estimacion_exposicion)
    pdf.ln(5)

    # Recommendation
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 10, "Recomendacion", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 7, result.recomendacion)
    pdf.ln(8)

    # CTA
    pdf.set_fill_color(0, 102, 204)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 12, f"  Agendar conversacion de 30 min: {CALENDLY_URL}", fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # Disclaimer
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.multi_cell(0, 5,
        "Este diagnostico es orientativo y no constituye una auditoria legal. "
        "Los resultados son preliminares y deben complementarse con un analisis "
        "profundo para determinar el estado real de cumplimiento. "
        "Confidencial - The Wise Monkey Project."
    )

    pdf.output(str(filepath))
    return str(filepath)
