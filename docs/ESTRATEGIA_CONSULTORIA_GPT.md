# Estrategia de Consultoría - Ley 21.719
## Extraído de conversación GPT + adaptaciones

---

## 1. POSICIONAMIENTO

**No vendemos "cumplimiento legal"**, vendemos:
- Claridad, control y trazabilidad del uso de datos
- Gobernanza de datos como activo estratégico
- Reducción de riesgos legales, operativos y reputacionales

**Rol del consultor**:
- Arquitecto de gobernanza de datos
- Traductor entre ley, negocio y datos
- Consultor estratégico en data-driven compliance

**Frase comercial potente**:
> "Muchas empresas creen que esto es un tema legal o tecnológico. En realidad, es un problema de organización, procesos y toma de decisiones."

---

## 2. SERVICIOS Y PRICING

### Servicio 1: Diagnóstico Express (LEAD MAGNET)
- **Modalidad**: Autoservicio online (formulario web)
- **Duración**: 10 minutos
- **Precio**: Gratis
- **Output**: Reporte automático + alerta para seguimiento

### Servicio 2: Diagnóstico Profundo
- **Duración**: 2-3 semanas
- **Precio**: USD 1,500 - 3,000
- **Entregables**:
  - Informe ejecutivo (10-15 slides)
  - Mapa de flujos de datos
  - Matriz de riesgos priorizados
  - Recomendaciones de corto plazo

### Servicio 3: Roadmap Estratégico (CORE)
- **Duración**: 6-8 semanas
- **Precio**: USD 4,000 - 8,000 (nosotros: $5K-$15K)
- **Entregables**:
  - Roadmap en fases (3-6-12 meses)
  - Modelo de gobernanza de datos
  - Matriz RACI
  - Priorización de iniciativas

### Servicio 4: Acompañamiento Implementación
- **Modalidad**: Bolsa mensual de horas
- **Precio**: USD 800 - 2,000/mes
- **Incluye**:
  - Reuniones quincenales/mensuales
  - Apoyo en priorización
  - Traducción legal ↔ negocio ↔ datos ↔ tecnología

### Servicio 5: Evaluaciones de Impacto (EIPD)
- **Precio**: USD 1,500 - 3,000 por evaluación
- **Aplica para**: datos sensibles, perfilamiento, tratamientos masivos

---

## 3. DIAGNÓSTICO EXPRESS - DISEÑO COMPLETO

### 3.1 Dimensiones y Preguntas (20 total)

#### Dimensión 0 - Contexto (no puntúa, segmenta)
- P0.1: Tamaño de empresa (Micro/Pyme, Mediana, Grande)
- P0.2: Sector (Servicios, Comercio, Salud, Educación, Financiero, Otro)
- P0.3: Rol del respondente

#### Dimensión 1 - Gobernanza y Responsabilidad (peso MUY ALTO)
- P1.1: ¿Existe responsable formal de protección de datos?
  - Sí, claramente definido → 0 pts
  - Existe informalmente → 5 pts
  - No existe → 15 pts ⚠️ GATILLO CRÍTICO
- P1.2: ¿Alta dirección involucrada en decisiones de datos?
  - Sí, regularmente → 0 pts
  - Solo casos puntuales → 5 pts
  - No → 10 pts
- P1.3: ¿Existen lineamientos internos claros?
  - Sí, documentados y conocidos → 0 pts
  - Parciales o poco conocidos → 5 pts
  - No existen → 10 pts

#### Dimensión 2 - Bases Legales y Transparencia (peso MUY ALTO)
- P2.1: ¿Pueden justificar por qué usan los datos que recolectan?
  - Sí, claramente → 0 pts
  - En algunos casos → 10 pts
  - No → 20 pts ⚠️ GATILLO CRÍTICO
- P2.2: ¿Consentimiento explícito y demostrable?
  - Sí → 0 pts
  - No siempre / no documentado → 10 pts
  - No → 15 pts
- P2.3: ¿Las personas saben para qué se usan sus datos?
  - Sí, claramente → 0 pts
  - Más o menos → 5 pts
  - No → 10 pts

#### Dimensión 3 - Procesos Operativos (peso ALTO)
- P3.1: ¿Proceso para responder solicitudes acceso/eliminación?
  - Sí → 0 pts
  - Parcial/informal → 5 pts
  - No → 15 pts
- P3.2: ¿Saben cuánto tiempo conservan los datos?
  - Sí → 0 pts
  - Algunos datos → 5 pts
  - No → 10 pts
- P3.3: ¿Qué pasa si ocurre filtración de datos?
  - Procedimiento definido → 0 pts
  - Se resolvería "sobre la marcha" → 10 pts
  - No se ha pensado → 15 pts ⚠️ GATILLO CRÍTICO

#### Dimensión 4 - Tecnología y Seguridad (peso MEDIO)
- P4.1: ¿Accesos a datos personales controlados?
  - Sí → 0 pts
  - Parcialmente → 5 pts
  - No → 10 pts
- P4.2: ¿Herramientas externas con contratos claros?
  - Sí, con contratos claros → 0 pts
  - Sí, sin claridad contractual → 10 pts
  - No estoy seguro → 10 pts

#### Dimensión 5 - Cultura y Conciencia (peso MEDIO)
- P5.1: ¿Saben que mal uso de datos puede generar sanciones?
  - Sí → 0 pts
  - Algunas personas → 5 pts
  - No → 10 pts
- P5.2: ¿Se ha capacitado al equipo?
  - Sí → 0 pts
  - Parcialmente → 5 pts
  - Nunca → 10 pts

### 3.2 Lógica de Scoring

```python
# Gatillos críticos (override a ALTO RIESGO)
gatillo_gobernanza = p1_1_score == 15  # No existe responsable
gatillo_bases_legales = p2_1_score == 20  # No justifican uso datos
gatillo_incidentes = p3_3_score == 15  # No hay plan incidentes

if any([gatillo_gobernanza, gatillo_bases_legales, gatillo_incidentes]):
    nivel = "ALTO RIESGO"
else:
    score_normalizado = (score_total / score_max) * 100
    if score_normalizado <= 20:
        nivel = "BAJO RIESGO"
    elif score_normalizado <= 45:
        nivel = "RIESGO MEDIO"
    else:
        nivel = "ALTO RIESGO"
```

### 3.3 Umbrales Finales

| Nivel | Score Normalizado | Lectura |
|-------|-------------------|---------|
| 🟢 Bajo riesgo | 0 - 20% | Buen control inicial |
| 🟡 Riesgo medio | 21 - 45% | Brechas relevantes |
| 🔴 Alto riesgo | > 45% | Exposición crítica |

---

## 4. STACK TÉCNICO RECOMENDADO

| Función | Herramienta |
|---------|-------------|
| Formulario | Typeform |
| Automatización/Scoring | Make (Integromat) |
| Reporte | Google Docs → PDF |
| Email | Brevo / Gmail |
| CRM | Notion |
| Agenda | Calendly |

### Flujo Técnico
1. Usuario completa Typeform
2. Make recibe respuestas → calcula scoring → determina nivel
3. Se genera reporte personalizado (PDF)
4. Email automático al usuario con reporte
5. Registro en CRM (Notion)
6. Si 🔴 → alerta inmediata al consultor

---

## 5. COPYS DE EMAIL

### 5.1 Mailing de Invitación (Principal)

**Asunto**: ¿Tu empresa está preparada para la nueva ley de datos en Chile?

```
Hola {{Nombre}},

En Chile ya se aprobó la nueva ley de protección de datos personales,
y muchas empresas están empezando a preguntarse si realmente tienen
control sobre cómo usan, gestionan y protegen los datos personales.

Más allá del cumplimiento legal, el desafío hoy es organizacional:
👉 saber qué datos se usan, para qué, quién decide y cómo se responde ante riesgos.

Por eso preparamos un Diagnóstico Express de Protección y Gobernanza
de Datos, que te permite en 10 minutos obtener una visión clara y
preliminar del nivel de riesgo de tu organización.

🔍 ¿Qué obtienes?
- Una evaluación orientativa del nivel de riesgo
- Un reporte automático con resultados y recomendaciones
- Claridad para decidir próximos pasos

👉 Accede al diagnóstico aquí:
[Realizar Diagnóstico Express]

Este diagnóstico es confidencial, no constituye una auditoría legal
y está pensado como una primera herramienta de orientación.

Un saludo,
Karim
The Wise Monkey Project
```

### 5.2 Email Entrega Reporte (🔴 Alto Riesgo)

**Asunto**: Resultados de tu Diagnóstico Express de Protección de Datos

```
Hola {{Nombre}},

Gracias por completar el Diagnóstico Express.

👉 Descargar reporte: [Link PDF]

Según los resultados, la organización presenta brechas relevantes
en control, gobernanza y justificación del uso de datos personales.

Esto suele ocurrir cuando:
- los datos se usan en múltiples procesos
- no existen roles claramente definidos
- los criterios de uso y resguardo no están formalizados

El siguiente paso no es implementar tecnología ni generar documentos
de inmediato, sino entender dónde están los riesgos reales y cómo
abordarlos de forma ordenada.

👉 Si quieres profundizar, puedes agendar una conversación de 30 minutos:
[Agendar conversación]

Un saludo,
Karim
The Wise Monkey Project
```

### 5.3 Seguimiento Proactivo WhatsApp (🔴)

```
Hola {{Nombre}}, ¿cómo estás?

Revisé tu diagnóstico express y aparecen algunos puntos relevantes
en cómo se están usando y gobernando los datos personales.

Si te parece, podemos conversar 30 minutos para revisarlos con calma
y ver cómo avanzar sin sobredimensionar esfuerzos.

Te dejo el link por si te hace sentido 👉 {{Calendly}}

Abrazo,
Karim
```

---

## 6. SISTEMA COMERCIAL

### 6.1 Estructura Conversación 30 min

| Minuto | Objetivo |
|--------|----------|
| 0-5 | Contexto y encuadre |
| 5-15 | Lectura del diagnóstico |
| 15-25 | Escenarios y caminos posibles |
| 25-30 | Próximo paso claro |

### 6.2 Apertura (Script)

> "Gracias por el tiempo. La idea de esta conversación no es venderte nada,
> sino ayudarte a interpretar el diagnóstico y ver si tiene sentido hacer algo más."

### 6.3 Pregunta Bisagra (muy potente)

> "Si mañana alguien les pidiera justificar cómo usan estos datos,
> ¿quién respondería y con qué criterio?"

### 6.4 Manejo de Objeciones

| Objeción | Respuesta |
|----------|-----------|
| "Tenemos abogado / TI" | "Perfecto. Esto no reemplaza eso. Lo ordena." |
| "Ahora no es prioridad" | "Justamente por eso conviene ordenar sin urgencia." |
| "¿Y si esperamos?" | "Esperar no reduce el trabajo, solo cambia el momento." |

---

## 7. GOBIERNO DEL SISTEMA

### 7.1 Política de Datos del Diagnóstico
- Leads 🟢 sin contacto → eliminar a los 6 meses
- Leads 🟡/🔴 sin cierre → anonimizar a los 12 meses
- Clientes → según relación contractual

### 7.2 Métricas Mínimas (Dashboard Mensual)
- Diagnósticos enviados
- % completados
- % que agenda llamada
- % que avanza a proyecto
- Score promedio del mercado (contenido para LinkedIn)

### 7.3 Iteración
Cada 20-30 diagnósticos, revisar:
- Preguntas que no discriminan
- Scores extremos
- Feedback de llamadas

---

## 8. PRÓXIMOS PASOS PENDIENTES

1. [ ] Expandir encuesta de 6 a ~12 preguntas
2. [ ] Implementar gatillos críticos en scoring
3. [ ] Crear formulario en Typeform
4. [ ] Configurar Make para automatización
5. [ ] Diseñar template de reporte PDF
6. [ ] Configurar secuencia de emails
7. [ ] Setup CRM en Notion
8. [ ] Probar flujo end-to-end

---

*Documentado: 2026-01-27*
*Fuente: Conversación GPT + adaptaciones proyecto Ley21719*
