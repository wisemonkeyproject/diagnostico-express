"""Email sender via Outlook SMTP (M365)."""

import os
import logging
from email.message import EmailMessage
from pathlib import Path

import aiosmtplib

logger = logging.getLogger(__name__)

SMTP_HOST = "smtp.office365.com"
SMTP_PORT = 587
OUTLOOK_EMAIL = os.getenv("OUTLOOK_EMAIL", "")
OUTLOOK_PASSWORD = os.getenv("OUTLOOK_PASSWORD", "")


async def send_email(
    to_email: str,
    subject: str,
    body_html: str,
    attachment_path: str | None = None,
) -> bool:
    """Send email via Outlook SMTP. Returns True on success."""
    if not OUTLOOK_EMAIL or not OUTLOOK_PASSWORD:
        logger.error("OUTLOOK_EMAIL or OUTLOOK_PASSWORD not configured")
        return False

    msg = EmailMessage()
    msg["From"] = f"Karim - The Wise Monkey Project <{OUTLOOK_EMAIL}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body_html, subtype="html")

    if attachment_path:
        path = Path(attachment_path)
        if path.exists():
            with open(path, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="pdf",
                    filename=path.name,
                )

    try:
        await aiosmtplib.send(
            msg,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            start_tls=True,
            username=OUTLOOK_EMAIL,
            password=OUTLOOK_PASSWORD,
        )
        logger.info(f"Email sent to {to_email}: {subject}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email to {to_email}: {e}")
        return False


async def send_diagnostico_report(
    to_email: str,
    nombre: str,
    empresa: str,
    nivel_riesgo: str,
    pdf_path: str,
    calendly_url: str,
) -> bool:
    """Send diagnostic report email with PDF attachment."""
    if nivel_riesgo == "ALTO RIESGO":
        intro = (
            "Segun los resultados, la organizacion presenta brechas relevantes "
            "en control, gobernanza y justificacion del uso de datos personales."
        )
    elif nivel_riesgo == "RIESGO MEDIO":
        intro = (
            "Los resultados muestran areas de mejora en la gestion de datos personales "
            "que conviene abordar antes de la entrada en vigencia de la ley."
        )
    else:
        intro = (
            "Los resultados muestran un buen nivel de control inicial. "
            "Recomendamos mantener las buenas practicas y revisar periodicamente."
        )

    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
        <p>Hola {nombre},</p>
        <p>Gracias por completar el Diagnostico Express de Proteccion de Datos.</p>
        <p>Adjunto encontraras tu reporte personalizado con los resultados del diagnostico
        para <strong>{empresa}</strong>.</p>
        <p>{intro}</p>
        <p>El siguiente paso no es implementar tecnologia ni generar documentos de inmediato,
        sino entender donde estan los riesgos reales y como abordarlos de forma ordenada.</p>
        <p>Si quieres profundizar, puedes agendar una conversacion de 30 minutos:</p>
        <p><a href="{calendly_url}" style="background-color: #0066cc; color: white;
        padding: 10px 20px; text-decoration: none; border-radius: 5px;">
        Agendar Conversacion</a></p>
        <br>
        <p>Un saludo,<br>
        <strong>Karim</strong><br>
        The Wise Monkey Project</p>
        <hr style="border: none; border-top: 1px solid #ddd;">
        <p style="font-size: 11px; color: #999;">
        Este diagnostico es orientativo y no constituye una auditoria legal.
        </p>
    </body>
    </html>
    """

    return await send_email(
        to_email=to_email,
        subject="Resultados de tu Diagnostico Express de Proteccion de Datos",
        body_html=body,
        attachment_path=pdf_path,
    )
