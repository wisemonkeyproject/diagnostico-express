"""Pydantic models for Quick-Scan DRA diagnostic system.

Aligned with DRA framework: 7 questions, 3 Knowledge Areas (DMBOK2),
scale 0-4 (CMM simplified), scoring 0-100%.
"""

from enum import Enum
from pydantic import BaseModel, EmailStr, Field


class TamanoEmpresa(str, Enum):
    MICRO_PYME = "micro_pyme"
    MEDIANA = "mediana"
    GRANDE = "grande"


class Sector(str, Enum):
    FINTECH = "fintech"
    SALUD = "salud"
    RETAIL = "retail"
    EDUCACION = "educacion"
    SERVICIOS = "servicios"
    OTRO = "otro"


class NivelMadurez(str, Enum):
    CRITICO = "Critico"
    BAJO = "Bajo"
    MEDIO = "Medio"
    ALTO = "Alto"


class KnowledgeArea(str, Enum):
    GOVERNANCE = "governance"
    SECURITY = "security"
    INTEGRATION = "integration"


SECTOR_TIPO_DATOS = {
    Sector.FINTECH: "datos financieros y crediticios de clientes",
    Sector.SALUD: "historiales medicos y datos de salud",
    Sector.RETAIL: "datos de consumo y programas de fidelizacion",
    Sector.EDUCACION: "datos de estudiantes y menores de edad",
    Sector.SERVICIOS: "datos de clientes y proveedores",
    Sector.OTRO: "datos personales de clientes y colaboradores",
}


class QuickScanForm(BaseModel):
    """Form submitted by user taking the Quick-Scan DRA."""

    # Contact info
    nombre_contacto: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    empresa: str = Field(..., min_length=2, max_length=100)
    tamano: TamanoEmpresa
    sector: Sector
    cargo: str = Field(default="", max_length=100)

    # 7 Quick-Scan questions (scale 0-4)
    q1: int = Field(..., ge=0, le=4, description="Gobernanza de Datos")
    q2: int = Field(..., ge=0, le=4, description="Control de Acceso")
    q3: int = Field(..., ge=0, le=4, description="Proteccion Tecnica")
    q4: int = Field(..., ge=0, le=4, description="Flujo de Datos")
    q5: int = Field(..., ge=0, le=4, description="Preparacion Ley 21.719")
    q6: int = Field(..., ge=0, le=4, description="Capacitacion")
    q7: int = Field(..., ge=0, le=4, description="Respuesta a Incidentes")


class KAScore(BaseModel):
    """Score for a single Knowledge Area."""

    ka: KnowledgeArea
    name: str
    average: float
    percentage: int
    questions: list[str]


class QuickScanResult(BaseModel):
    """Complete result of a Quick-Scan DRA evaluation."""

    # Identification
    nombre_contacto: str
    email: str
    empresa: str
    tamano: TamanoEmpresa
    sector: Sector
    cargo: str

    # Scores
    score_total: int
    score_max: int
    score_percentage: int
    nivel: NivelMadurez
    ka_scores: list[KAScore]
    critical_area: KnowledgeArea
    suggested_kas: list[KnowledgeArea]

    # Analysis
    recommendation: str
    exposure: str
    responses: dict[str, int]


class ProspectoCSV(BaseModel):
    """Prospect from CSV file."""

    nombre: str
    cargo: str
    email: str
    linkedin: str = ""
    empresa: str
    sector: str
    telefono: str = ""


class CampaignStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    OPENED = "opened"
    REPLIED = "replied"
    BOUNCED = "bounced"
    OPTED_OUT = "opted_out"
