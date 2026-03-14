# CLAUDE.md - Ley 21.719 Prospeccion (Alineado con DRA)

## Estado del Proyecto (2026-02-24)

### Contexto
Plataforma de prospeccion comercial para servicios DRA (Data Readiness Assessment). El Quick-Scan DRA es el punto de entrada gratuito al funnel de servicios de The Wise Monkey Project para cumplimiento Ley 21.719.

**Funnel:** Email manual → Quick-Scan DRA (gratis, autoservicio) → Follow-up personalizado → DRA Assessment completo (servicio pagado)

### Estado: OPERATIVO - Listo para prospectar
- Quick-Scan DRA live en GitHub Pages
- Google Apps Script deployado (v2, email HTML con CTAs)
- 106 contactos con email listos para contactar
- Secuencia de 4 emails con valores reales configurados
- Checkbox de consentimiento de datos (Ley 21.719 compliant)

### URLs en Produccion
- **Quick-Scan DRA**: https://wisemonkeyproject.github.io/diagnostico-express/
- **Repo GitHub**: https://github.com/wisemonkeyproject/diagnostico-express
- **Apps Script (v2)**: Deployado, envia email HTML con barras de score, urgencia y CTAs (Email/WhatsApp)
- **Google Sheet**: Vinculado al Apps Script (CRM con 22 columnas, colores por nivel)

### Alineacion con DRA Framework
- **Repo DRA (padre)**: `/home/karim/Escritorio/TheWiseMonkeyProject/Consultoria/DRA/`
- **Ubicacion**: `DRA/Ley21719-Prospeccion/` (sub-proyecto dentro del repo DRA)
- **Scoring**: Replica de `QuickScanScoring` del DRA (`DRA/src/scoring.py`)
- **Frameworks**: DAMA-DMBOK2 + NIST Privacy Framework + CMM/CMMI
- **Knowledge Areas**: Governance, Security, Integration (3 KAs MVP)
- **Escala**: 0-4 (CMM simplificado), 7 preguntas, score 0-100%

### Decision Arquitectonica
- **Elegido**: HTML estatico (GitHub Pages) + Google Sheets backend (cero costo)
- **Email de notificacion**: Google Apps Script (HTML con CTAs, urgencia por nivel)
- **Follow-up al prospecto**: Manual desde Outlook (karim@wisemonkeygroup.com) usando CTAs del email de notificacion
- **Descartado**: Netlify, Render, Google Forms, n8n, Power Automate, email automatico al prospecto

### Flujo Operativo
1. Karim envia emails manualmente usando templates de `docs/EMAIL_SEQUENCE_LEY21719.md`
2. Lista de contactos en `docs/CONTACTOS_PROSPECCION.md` (106 con email, 4 sectores)
3. Prospecto abre link al Quick-Scan DRA en GitHub Pages
4. 7 preguntas, escala 0-4, scoring se calcula en el browser (JavaScript)
5. Prospecto ve resultados inmediatos: score %, nivel, area critica, KAs sugeridas
6. Prospecto acepta consentimiento de datos antes de enviar
7. Datos se envian a Google Sheet via Apps Script (22 columnas, colores por nivel)
8. Karim recibe email HTML con: score, barras por KA, prioridad, botones Email/WhatsApp pre-redactados
9. Karim hace follow-up manual usando los botones del email (sale desde wisemonkeygroup.com)

### Archivos Principales
- `docs/Netlify/index.html` - Formulario Quick-Scan DRA (version local, sincronizada con GitHub repo)
- `docs/google-apps-script.js` - Apps Script v2 (22 columnas, email HTML con CTAs, urgencia por nivel)
- `docs/EMAIL_SEQUENCE_LEY21719.md` - Secuencia 4 emails con valores reales (link, WhatsApp, firma)
- `docs/CONTACTOS_PROSPECCION.md` - 106 contactos con email por sector, con columna de estado

### Archivos Backend (referencia)
- `src/scoring.py` - Quick-Scan DRA scoring engine (Python, replica de DRA/src/scoring.py QuickScanScoring)
- `src/models.py` - Modelos Pydantic (QuickScanForm, QuickScanResult, KAScore, NivelMadurez, KnowledgeArea)

### Archivos Legacy (app FastAPI original, referencia)
- `templates/diagnostico.html` - Formulario Jinja2 original
- `templates/resultado.html` - Resultados Jinja2 original
- `static/style.css` - Estilos base

### Prospeccion: Estado Actual
- **Total prospectos**: 163 (106 con email contactable)
- **Fintech**: 39 con email (5 ya contactados con Email 1)
- **Salud**: 24 con email (0 contactados)
- **Retail**: 30 con email (0 contactados)
- **Educacion**: 13 con email (0 contactados)
- **Archivo eliminado**: `EMAILS_TANDA1_FINTECH.md` (reemplazado por templates + lista de contactos)

### Scoring Engine (referencia rapida)
- 7 preguntas, escala 0-4, max 28 puntos
- Score = (suma / 28) x 100 → porcentaje de madurez
- Niveles: Critico (0-25%), Bajo (26-50%), Medio (51-75%), Alto (76-100%)
- 3 Knowledge Areas: Governance (Q1,Q5,Q6), Security (Q2,Q3,Q7), Integration (Q4)
- Area critica = KA con menor promedio
- KAs sugeridas = ordenadas de menor a mayor score

### Estrategia de Negocio (sesion 2026-02-06)
- **Documento**: `ESTRATEGIA_5_HIPOTESIS_WISEMONKEY.md` - Estrategia completa basada en 5 hipotesis
- **Investigacion**: Super-research con datos de Encuesta PwC Chile 2025, Comision Ministerial, Chambers & Partners
- **Hipotesis articuladas**: H1 Posicionamiento (no legal, organizacional) → H3 Mercado (PYMEs) → H4 Motor de demanda (cascada proveedores) → H2 Producto recurrente (DPO-as-a-Service) → H5 Crecimiento (exportar LATAM)
- **Producto nuevo propuesto**: DPO-as-a-Service ($500-5K/mes recurrente)
- **Fases**: Lanzar (Feb-Abr) → Escalar (May-Jul) → Consolidar (Ago-Nov) → Expandir (Dic+)

### Producto DPO-as-a-Service (sesion 2026-02-06)
- **Documento**: `PRODUCTO_DPO_AS_A_SERVICE.md` - Diseno completo del producto recurrente
- **Base legal**: Arts. 49 (modelo prevencion), 50 (delegado, 8 funciones), 51 (certificacion), 36 (atenuantes)
- **3 planes**: Esencial ($500-800/mes), Profesional ($1.2-2K/mes), Enterprise ($3-5K/mes)
- **Insight de conversion**: DRA Assessment one-shot = onboarding del DPO-aaS

### Documentacion Comercial Existente
- `PRODUCTO_DPO_AS_A_SERVICE.md` - Producto DPO-as-a-Service completo
- `ESTRATEGIA_5_HIPOTESIS_WISEMONKEY.md` - Estrategia de negocio con 5 hipotesis
- `ESTRATEGIA_CONSULTORIA_GPT.md` - Estrategia comercial original
- `CHECKLIST_DIAGNOSTICO_RAPIDO.md` - Checklist manual 30min
- `GUION_CONVERSACION_INICIAL.md` - Script llamada 15min
- `TEMPLATE_PROPUESTA_LEY21719.md` - Propuesta formal

### Proximos pasos
1. **Enviar emails**: Usar templates + lista de contactos, empezar por Fintech (34 pendientes)
2. **Monitorear**: Revisar Google Sheet y emails de notificacion para follow-up
3. **Iterar**: Ajustar templates segun respuestas y tasas de conversion
4. **Escalar**: Generar mas prospectos cuando se agoten los 106 actuales
