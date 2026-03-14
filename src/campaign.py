"""Campaign engine for email outreach to prospects.

CLI tool to schedule and send campaign emails to prospects from CSV.
Usage:
    python -m src.campaign schedule         # Schedule all 4 emails for all prospects
    python -m src.campaign send             # Send all emails due today
    python -m src.campaign send --test      # Send test email to yourself
    python -m src.campaign status           # Show campaign status
"""

import asyncio
import csv
import logging
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.database import (
    get_campaign_stats,
    get_pending_emails,
    init_db,
    save_campaign_email,
    update_campaign_status,
)
from src.email_sender import send_email
from src.templates_email import CADENCE_DAYS, EMAIL_TEMPLATES

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

CSV_PATH = Path(__file__).parent.parent / "data" / "prospectos_ley21719.csv"
DIAGNOSTICO_URL = os.getenv("DIAGNOSTICO_URL", "https://your-app.onrender.com/diagnostico")
RATE_LIMIT_SECONDS = 5  # seconds between emails to avoid SMTP throttling


def load_prospects() -> list[dict]:
    """Load prospects from CSV."""
    prospects = []
    with open(CSV_PATH, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("email"):
                prospects.append({
                    "nombre": row.get("nombre", "").strip(),
                    "email": row.get("email", "").strip(),
                    "empresa": row.get("empresa", "").strip(),
                    "sector": row.get("sector", "").strip(),
                    "cargo": row.get("cargo", "").strip(),
                })
    return prospects


def schedule_campaign(start_date: str | None = None):
    """Schedule all 4 emails for all prospects in CSV."""
    init_db()
    prospects = load_prospects()
    base_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else datetime.now()

    total = 0
    for prospect in prospects:
        nombre_parts = prospect["nombre"].split()
        first_name = nombre_parts[0] if nombre_parts else prospect["nombre"]

        for email_num, days_offset in CADENCE_DAYS.items():
            scheduled = (base_date + timedelta(days=days_offset)).strftime("%Y-%m-%d")
            save_campaign_email(
                nombre=first_name,
                email=prospect["email"],
                empresa=prospect["empresa"],
                sector=prospect["sector"],
                email_number=email_num,
                scheduled_date=scheduled,
            )
            total += 1

    logger.info(f"Scheduled {total} emails for {len(prospects)} prospects")
    logger.info(f"Base date: {base_date.strftime('%Y-%m-%d')}")
    for num, days in CADENCE_DAYS.items():
        d = (base_date + timedelta(days=days)).strftime("%Y-%m-%d")
        logger.info(f"  Email {num}: {d}")


async def send_pending(test_mode: bool = False):
    """Send all emails scheduled for today or earlier."""
    init_db()
    today = datetime.now().strftime("%Y-%m-%d")

    if test_mode:
        test_email = os.getenv("OUTLOOK_EMAIL", "")
        if not test_email:
            logger.error("Set OUTLOOK_EMAIL to run test mode")
            return
        logger.info(f"TEST MODE: Sending test email to {test_email}")
        subject, body = EMAIL_TEMPLATES[1](
            nombre="Test",
            empresa="Test Company",
            sector="fintech",
            diagnostico_url=DIAGNOSTICO_URL,
        )
        success = await send_email(test_email, subject, body)
        logger.info(f"Test email {'sent' if success else 'FAILED'}")
        return

    pending = get_pending_emails(today)
    logger.info(f"Found {len(pending)} pending emails for {today}")

    sent = 0
    failed = 0
    for record in pending:
        email_num = record["email_number"]
        template_fn = EMAIL_TEMPLATES[email_num]

        # Build template args (email_2 doesn't take sector)
        if email_num in (1, 3, 4):
            subject, body = template_fn(
                nombre=record["prospecto_nombre"],
                empresa=record["prospecto_empresa"],
                sector=record["prospecto_sector"],
                diagnostico_url=DIAGNOSTICO_URL,
            )
        else:
            subject, body = template_fn(
                nombre=record["prospecto_nombre"],
                empresa=record["prospecto_empresa"],
                diagnostico_url=DIAGNOSTICO_URL,
            )

        success = await send_email(record["prospecto_email"], subject, body)

        if success:
            update_campaign_status(record["id"], "sent")
            sent += 1
        else:
            update_campaign_status(record["id"], "bounced")
            failed += 1

        time.sleep(RATE_LIMIT_SECONDS)

    logger.info(f"Done: {sent} sent, {failed} failed out of {len(pending)}")


def show_status():
    """Print campaign status summary."""
    init_db()
    stats = get_campaign_stats()
    print(f"\n=== Campaign Status ===")
    print(f"Total emails: {stats['total']}")
    print(f"Sent:         {stats['sent']}")
    print(f"Pending:      {stats['pending']}")
    if stats["by_email"]:
        print(f"\nBy email wave:")
        for wave in stats["by_email"]:
            print(f"  Email {wave['email_number']}: {wave['sent']}/{wave['total']} sent")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m src.campaign [schedule|send|status]")
        print("  schedule [YYYY-MM-DD]  Schedule campaign (optional start date)")
        print("  send [--test]          Send pending emails")
        print("  status                 Show campaign stats")
        sys.exit(1)

    command = sys.argv[1]

    if command == "schedule":
        start = sys.argv[2] if len(sys.argv) > 2 else None
        schedule_campaign(start)
    elif command == "send":
        test = "--test" in sys.argv
        asyncio.run(send_pending(test_mode=test))
    elif command == "status":
        show_status()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
