"""SQLite database for leads, diagnostics, and campaign tracking."""

import json
import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "ley21719.db"


def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS diagnosticos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_contacto TEXT NOT NULL,
            email TEXT NOT NULL,
            empresa TEXT NOT NULL,
            cargo TEXT DEFAULT '',
            tamano TEXT NOT NULL,
            sector TEXT NOT NULL,
            score_total INTEGER NOT NULL,
            score_max INTEGER NOT NULL,
            score_normalizado REAL NOT NULL,
            nivel_riesgo TEXT NOT NULL,
            gatillos_activados TEXT DEFAULT '[]',
            brechas_principales TEXT DEFAULT '[]',
            estimacion_exposicion TEXT DEFAULT '',
            recomendacion TEXT DEFAULT '',
            dimensiones_json TEXT DEFAULT '[]',
            pdf_path TEXT DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS campaign_emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prospecto_nombre TEXT NOT NULL,
            prospecto_email TEXT NOT NULL,
            prospecto_empresa TEXT NOT NULL,
            prospecto_sector TEXT NOT NULL,
            email_number INTEGER NOT NULL,
            status TEXT DEFAULT 'pending',
            scheduled_date TEXT NOT NULL,
            sent_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE INDEX IF NOT EXISTS idx_diagnosticos_email ON diagnosticos(email);
        CREATE INDEX IF NOT EXISTS idx_diagnosticos_riesgo ON diagnosticos(nivel_riesgo);
        CREATE INDEX IF NOT EXISTS idx_campaign_status ON campaign_emails(status);
        CREATE INDEX IF NOT EXISTS idx_campaign_scheduled ON campaign_emails(scheduled_date);
    """)
    conn.commit()
    conn.close()


def save_diagnostico(result) -> int:
    conn = get_db()
    cursor = conn.execute(
        """INSERT INTO diagnosticos
        (nombre_contacto, email, empresa, cargo, tamano, sector,
         score_total, score_max, score_normalizado, nivel_riesgo,
         gatillos_activados, brechas_principales, estimacion_exposicion,
         recomendacion, dimensiones_json)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            result.nombre_contacto,
            result.email,
            result.empresa,
            result.cargo,
            result.tamano.value,
            result.sector.value,
            result.score_total,
            result.score_max,
            result.score_normalizado,
            result.nivel_riesgo.value,
            json.dumps(result.gatillos_activados),
            json.dumps(result.brechas_principales),
            result.estimacion_exposicion,
            result.recomendacion,
            json.dumps([d.model_dump() for d in result.dimensiones]),
        ),
    )
    conn.commit()
    row_id = cursor.lastrowid
    conn.close()
    return row_id


def update_diagnostico_pdf(diag_id: int, pdf_path: str):
    conn = get_db()
    conn.execute(
        "UPDATE diagnosticos SET pdf_path = ? WHERE id = ?",
        (pdf_path, diag_id),
    )
    conn.commit()
    conn.close()


def get_all_diagnosticos() -> list[dict]:
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM diagnosticos ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_diagnosticos_by_riesgo(nivel: str) -> list[dict]:
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM diagnosticos WHERE nivel_riesgo = ? ORDER BY created_at DESC",
        (nivel,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_diagnostico_stats() -> dict:
    conn = get_db()
    total = conn.execute("SELECT COUNT(*) FROM diagnosticos").fetchone()[0]
    alto = conn.execute(
        "SELECT COUNT(*) FROM diagnosticos WHERE nivel_riesgo = 'ALTO RIESGO'"
    ).fetchone()[0]
    medio = conn.execute(
        "SELECT COUNT(*) FROM diagnosticos WHERE nivel_riesgo = 'RIESGO MEDIO'"
    ).fetchone()[0]
    bajo = conn.execute(
        "SELECT COUNT(*) FROM diagnosticos WHERE nivel_riesgo = 'BAJO RIESGO'"
    ).fetchone()[0]
    conn.close()
    return {"total": total, "alto": alto, "medio": medio, "bajo": bajo}


# Campaign operations

def save_campaign_email(nombre: str, email: str, empresa: str, sector: str,
                        email_number: int, scheduled_date: str) -> int:
    conn = get_db()
    cursor = conn.execute(
        """INSERT INTO campaign_emails
        (prospecto_nombre, prospecto_email, prospecto_empresa, prospecto_sector,
         email_number, scheduled_date)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (nombre, email, empresa, sector, email_number, scheduled_date),
    )
    conn.commit()
    row_id = cursor.lastrowid
    conn.close()
    return row_id


def update_campaign_status(email_id: int, status: str):
    conn = get_db()
    sent_at = datetime.now().isoformat() if status == "sent" else None
    if sent_at:
        conn.execute(
            "UPDATE campaign_emails SET status = ?, sent_at = ? WHERE id = ?",
            (status, sent_at, email_id),
        )
    else:
        conn.execute(
            "UPDATE campaign_emails SET status = ? WHERE id = ?",
            (status, email_id),
        )
    conn.commit()
    conn.close()


def get_pending_emails(scheduled_date: str) -> list[dict]:
    conn = get_db()
    rows = conn.execute(
        """SELECT * FROM campaign_emails
        WHERE status = 'pending' AND scheduled_date <= ?
        ORDER BY email_number, prospecto_empresa""",
        (scheduled_date,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_campaign_stats() -> dict:
    conn = get_db()
    total = conn.execute("SELECT COUNT(*) FROM campaign_emails").fetchone()[0]
    sent = conn.execute(
        "SELECT COUNT(*) FROM campaign_emails WHERE status = 'sent'"
    ).fetchone()[0]
    pending = conn.execute(
        "SELECT COUNT(*) FROM campaign_emails WHERE status = 'pending'"
    ).fetchone()[0]
    by_email = conn.execute(
        """SELECT email_number, COUNT(*) as total,
        SUM(CASE WHEN status = 'sent' THEN 1 ELSE 0 END) as sent
        FROM campaign_emails GROUP BY email_number ORDER BY email_number"""
    ).fetchall()
    conn.close()
    return {
        "total": total,
        "sent": sent,
        "pending": pending,
        "by_email": [dict(r) for r in by_email],
    }
