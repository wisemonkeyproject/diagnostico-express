"""Email templates for the 4-email campaign sequence."""

SECTOR_TIPO_DATOS = {
    "fintech": "datos financieros y crediticios de clientes",
    "salud": "historiales medicos y datos de salud",
    "retail": "datos de consumo y programas de fidelizacion",
    "educacion": "datos de estudiantes y menores de edad",
    "servicios": "datos de clientes y proveedores",
    "otro": "datos personales de clientes y colaboradores",
}


def _tipo_datos(sector: str) -> str:
    return SECTOR_TIPO_DATOS.get(sector.lower(), SECTOR_TIPO_DATOS["otro"])


def email_1(nombre: str, empresa: str, sector: str, diagnostico_url: str) -> tuple[str, str]:
    """Email 1: Awareness + dato impactante (Day 0)."""
    subject = f"{empresa} - 71% no estan preparadas"
    body = f"""
    <html><body style="font-family: Arial, sans-serif; color: #333; line-height: 1.7;">
    <p>Hola {nombre},</p>

    <p>Un estudio de la FEN de la Universidad de Chile revela que el <strong>71% de las empresas
    chilenas NO tienen una estrategia clara</strong> de proteccion de datos personales.</p>

    <p>Con la Ley 21.719 entrando en vigencia en diciembre 2026, las empresas tienen
    menos de 11 meses para prepararse.</p>

    <p>{empresa} maneja {_tipo_datos(sector)}. Una pregunta directa:</p>

    <ul>
        <li>Tienen documentado que datos personales manejan?</li>
        <li>Saben como responder si un cliente pide que eliminen sus datos?</li>
        <li>Tienen un proceso para notificar brechas de seguridad en 72 horas?</li>
    </ul>

    <p>Si la respuesta a alguna es "no estoy seguro", te invito a realizar nuestro
    <strong>Diagnostico Express gratuito</strong> (10 minutos):</p>

    <p><a href="{diagnostico_url}" style="background-color: #0066cc; color: white;
    padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block;">
    Realizar Diagnostico Express</a></p>

    <p>Obtendras un reporte automatico con tu nivel de riesgo y recomendaciones.</p>

    <p>Saludos,<br>
    <strong>Karim</strong><br>
    The Wise Monkey Project</p>

    <p style="font-size: 12px; color: #999;">
    P.D. - El estudio completo: FEN Universidad de Chile, 2024.</p>
    </body></html>
    """
    return subject, body


def email_2(nombre: str, empresa: str, diagnostico_url: str) -> tuple[str, str]:
    """Email 2: Urgencia financiera (Day 3)."""
    subject = f"Multa minima: $350K USD"
    body = f"""
    <html><body style="font-family: Arial, sans-serif; color: #333; line-height: 1.7;">
    <p>Hola {nombre},</p>

    <p>Te escribi hace unos dias sobre la Ley 21.719. Quiero compartir algo
    que creo es importante para {empresa}.</p>

    <p>El regimen de sanciones de la nueva ley es significativo:</p>

    <table style="border-collapse: collapse; margin: 16px 0;">
        <tr style="background: #fde8ea;">
            <td style="padding: 8px 16px; border: 1px solid #ddd;"><strong>Infraccion LEVE</strong></td>
            <td style="padding: 8px 16px; border: 1px solid #ddd;">hasta $350,000 USD</td>
        </tr>
        <tr style="background: #fff8e1;">
            <td style="padding: 8px 16px; border: 1px solid #ddd;"><strong>Infraccion GRAVE</strong></td>
            <td style="padding: 8px 16px; border: 1px solid #ddd;">hasta $700,000 USD</td>
        </tr>
        <tr style="background: #fde8ea;">
            <td style="padding: 8px 16px; border: 1px solid #ddd;"><strong>Infraccion GRAVISIMA</strong></td>
            <td style="padding: 8px 16px; border: 1px solid #ddd;">hasta $1,400,000 USD</td>
        </tr>
        <tr>
            <td style="padding: 8px 16px; border: 1px solid #ddd;"><strong>Reincidencia</strong></td>
            <td style="padding: 8px 16px; border: 1px solid #ddd;">2-4% ingresos anuales</td>
        </tr>
    </table>

    <p>Para ponerlo en perspectiva:</p>
    <ul>
        <li>Costo de un diagnostico de cumplimiento: $5,000 - $15,000 USD</li>
        <li>Costo de UNA multa leve: $350,000 USD</li>
    </ul>

    <p><strong>La matematica es simple.</strong></p>

    <p>Si aun no has evaluado donde esta {empresa}, nuestro diagnostico express
    gratuito es un buen punto de partida:</p>

    <p><a href="{diagnostico_url}" style="background-color: #0066cc; color: white;
    padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block;">
    Evaluar mi Nivel de Riesgo</a></p>

    <p>Saludos,<br>
    <strong>Karim</strong><br>
    The Wise Monkey Project</p>

    <p style="font-size: 12px; color: #999;">
    P.D. - Las empresas que se preparan ahora tendran ventaja competitiva.</p>
    </body></html>
    """
    return subject, body


def email_3(nombre: str, empresa: str, sector: str, diagnostico_url: str) -> tuple[str, str]:
    """Email 3: Propuesta de valor (Day 7)."""
    subject = f"6 semanas para tu roadmap de cumplimiento"
    body = f"""
    <html><body style="font-family: Arial, sans-serif; color: #333; line-height: 1.7;">
    <p>Hola {nombre},</p>

    <p>He trabajado con varias empresas de {sector} que estaban en la misma
    situacion: sabian que tenian que prepararse para la Ley 21.719, pero no
    sabian por donde empezar.</p>

    <p>Lo que hago es simple. <strong>En 4-6 semanas entrego:</strong></p>

    <ol>
        <li><strong>Mapa de procesos de datos</strong> - Todos los procesos de {empresa}
        que manejan datos personales, documentados y clasificados.</li>
        <li><strong>Inventario de datos personales</strong> - Que datos tienen, donde estan,
        para que los usan, con quien los comparten.</li>
        <li><strong>Informe de brechas</strong> - Donde estan hoy vs donde necesitan estar.</li>
        <li><strong>Matriz de riesgos</strong> - Priorizado por probabilidad e impacto.</li>
        <li><strong>Roadmap de implementacion</strong> - Plan de accion con quick wins y fases.</li>
    </ol>

    <p>El resultado: <strong>saben exactamente donde estan y que hacer.</strong> Sin ambiguedades.</p>

    <p>El primer paso es entender tu situacion actual. Nuestro diagnostico express
    gratuito te da una primera lectura en 10 minutos:</p>

    <p><a href="{diagnostico_url}" style="background-color: #0066cc; color: white;
    padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block;">
    Comenzar Diagnostico</a></p>

    <p>Saludos,<br>
    <strong>Karim</strong><br>
    The Wise Monkey Project</p>

    <p style="font-size: 12px; color: #999;">
    P.D. - El primer cliente que trabaje en tu sector puede tener condiciones especiales.</p>
    </body></html>
    """
    return subject, body


def email_4(nombre: str, empresa: str, sector: str, diagnostico_url: str) -> tuple[str, str]:
    """Email 4: Escasez + cierre (Day 14)."""
    subject = f"Ultima oportunidad piloto - {sector}"
    body = f"""
    <html><body style="font-family: Arial, sans-serif; color: #333; line-height: 1.7;">
    <p>Hola {nombre},</p>

    <p>Este es mi ultimo email sobre el tema.</p>

    <p>Estoy buscando <strong>2-3 empresas de {sector}</strong> para trabajar como
    pilotos en diagnosticos de cumplimiento Ley 21.719.</p>

    <p><strong>Las condiciones para pilotos:</strong></p>
    <ul>
        <li>Precio preferencial (hasta 30% descuento)</li>
        <li>Prioridad en agenda</li>
        <li>Caso de estudio anonimo</li>
    </ul>

    <p><strong>A cambio, necesito:</strong></p>
    <ul>
        <li>Decision rapida (esta semana)</li>
        <li>Feedback honesto del proceso</li>
        <li>Referencia futura si el resultado es bueno</li>
    </ul>

    <p>Si {empresa} quiere evaluar donde esta hoy, el diagnostico express
    gratuito es el primer paso:</p>

    <p><a href="{diagnostico_url}" style="background-color: #dc3545; color: white;
    padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block;">
    Realizar Diagnostico Ahora</a></p>

    <p>Si no es el momento, lo entiendo perfectamente. Te deseo exito preparandote para la ley.</p>

    <p>Saludos,<br>
    <strong>Karim</strong><br>
    The Wise Monkey Project</p>

    <p style="font-size: 12px; color: #999;">
    P.D. - El reloj corre. Diciembre 2026 esta a la vuelta de la esquina.</p>
    </body></html>
    """
    return subject, body


EMAIL_TEMPLATES = {
    1: email_1,
    2: email_2,
    3: email_3,
    4: email_4,
}

# Cadence: email_number -> days after campaign start
CADENCE_DAYS = {1: 0, 2: 3, 3: 7, 4: 14}
