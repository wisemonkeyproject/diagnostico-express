"""FastAPI application for Ley 21.719 diagnostic system."""

import hashlib
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.database import (
    get_all_diagnosticos,
    get_campaign_stats,
    get_diagnostico_stats,
    get_diagnosticos_by_riesgo,
    init_db,
    save_diagnostico,
    update_diagnostico_pdf,
)
from src.email_sender import send_diagnostico_report
from src.models import DiagnosticoForm
from src.pdf_generator import generar_pdf
from src.scoring import calcular_score

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent.parent
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin21719")
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
CALENDLY_URL = os.getenv("CALENDLY_URL", "https://calendly.com/twmp")

app = FastAPI(title="Ley 21.719 - Diagnostico Express", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.on_event("startup")
def startup():
    init_db()
    logger.info("Database initialized")


def _admin_token() -> str:
    return hashlib.sha256(f"{SECRET_KEY}:admin".encode()).hexdigest()[:32]


def _is_admin(request: Request) -> bool:
    return request.cookies.get("admin_token") == _admin_token()


# --- Public routes ---

@app.get("/", response_class=HTMLResponse)
async def home():
    return RedirectResponse(url="/diagnostico")


@app.get("/diagnostico", response_class=HTMLResponse)
async def diagnostico_form(request: Request):
    return templates.TemplateResponse("diagnostico.html", {"request": request})


@app.post("/diagnostico/result", response_class=HTMLResponse)
async def diagnostico_result(
    request: Request,
    nombre_contacto: str = Form(...),
    email: str = Form(...),
    empresa: str = Form(...),
    cargo: str = Form(""),
    tamano: str = Form(...),
    sector: str = Form(...),
    p1_1: int = Form(...),
    p1_2: int = Form(...),
    p1_3: int = Form(...),
    p2_1: int = Form(...),
    p2_2: int = Form(...),
    p2_3: int = Form(...),
    p3_1: int = Form(...),
    p3_2: int = Form(...),
    p3_3: int = Form(...),
    p4_1: int = Form(...),
    p4_2: int = Form(...),
    p5_1: int = Form(...),
    p5_2: int = Form(...),
):
    form = DiagnosticoForm(
        nombre_contacto=nombre_contacto,
        email=email,
        empresa=empresa,
        cargo=cargo,
        tamano=tamano,
        sector=sector,
        p1_1=p1_1, p1_2=p1_2, p1_3=p1_3,
        p2_1=p2_1, p2_2=p2_2, p2_3=p2_3,
        p3_1=p3_1, p3_2=p3_2, p3_3=p3_3,
        p4_1=p4_1, p4_2=p4_2,
        p5_1=p5_1, p5_2=p5_2,
    )

    result = calcular_score(form)

    # Save to DB
    diag_id = save_diagnostico(result)
    logger.info(f"Diagnostico #{diag_id}: {empresa} - {result.nivel_riesgo.value}")

    # Generate PDF
    pdf_path = generar_pdf(result)
    update_diagnostico_pdf(diag_id, pdf_path)
    logger.info(f"PDF generated: {pdf_path}")

    # Send email (async, don't block on failure)
    try:
        await send_diagnostico_report(
            to_email=email,
            nombre=nombre_contacto,
            empresa=empresa,
            nivel_riesgo=result.nivel_riesgo.value,
            pdf_path=pdf_path,
            calendly_url=CALENDLY_URL,
        )
    except Exception as e:
        logger.error(f"Email send failed: {e}")

    return templates.TemplateResponse("resultado.html", {
        "request": request,
        "result": result,
        "calendly_url": CALENDLY_URL,
    })


# --- Admin routes ---

@app.get("/admin/login", response_class=HTMLResponse)
async def admin_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})


@app.post("/admin/login")
async def admin_login(request: Request, password: str = Form(...)):
    if password == ADMIN_PASSWORD:
        response = RedirectResponse(url="/admin", status_code=303)
        response.set_cookie("admin_token", _admin_token(), httponly=True, max_age=86400)
        return response
    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "Password incorrecto",
    })


@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request, filter: str | None = None):
    if not _is_admin(request):
        return RedirectResponse(url="/admin/login")

    stats = get_diagnostico_stats()
    campaign_stats = get_campaign_stats()

    if filter:
        diagnosticos = get_diagnosticos_by_riesgo(filter)
    else:
        diagnosticos = get_all_diagnosticos()

    return templates.TemplateResponse("admin.html", {
        "request": request,
        "stats": stats,
        "campaign_stats": campaign_stats,
        "diagnosticos": diagnosticos,
        "filter": filter,
    })


@app.get("/admin/logout")
async def admin_logout():
    response = RedirectResponse(url="/admin/login")
    response.delete_cookie("admin_token")
    return response
