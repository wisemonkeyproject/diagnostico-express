# PROPUESTA: Diagnostico de Cumplimiento Ley 21.719

---

## Informacion del Proyecto

| Campo               | Valor                |
| ------------------- | -------------------- |
| **Cliente**         | {EMPRESA}            |
| **Contacto**        | {NOMBRE}, {CARGO}    |
| **Fecha propuesta** | {FECHA}              |
| **Validez**         | 15 dias              |
| **Propuesta #**     | TWMP-LEY21719-{NNNN} |

---

## 1. Situacion Actual

### Resultado del Diagnostico Rapido

| Indicador                 | Valor                           |
| ------------------------- | ------------------------------- |
| **Score de cumplimiento** | {X}/20                          |
| **Nivel de madurez**      | {CRITICO/BAJO/INTERMEDIO/BUENO} |
| **Dias hasta vigencia**   | {DIAS} dias (1 dic 2026)        |

### Brechas Criticas Identificadas

1. **{BRECHA_1}**
   
   - Estado actual: {descripcion}
   - Riesgo asociado: {multa_estimada}

2. **{BRECHA_2}**
   
   - Estado actual: {descripcion}
   - Riesgo asociado: {multa_estimada}

3. **{BRECHA_3}**
   
   - Estado actual: {descripcion}
   - Riesgo asociado: {multa_estimada}

### Riesgo Estimado Total

| Tipo Infraccion     | Multa Potencial       |
| ------------------- | --------------------- |
| Leve (Art. 34)      | $350,000 USD          |
| Grave (Art. 34)     | $700,000 USD          |
| Gravisima (Art. 34) | $1,400,000 USD        |
| Reincidencia        | 2-4% ingresos anuales |

**Exposicion estimada para {EMPRESA}:** ${EXPOSICION_TOTAL} USD

---

## 2. Solucion Propuesta

### Diagnostico de Cumplimiento Ley 21.719

Un proyecto de consultoria de 3 semanas para llevar a {EMPRESA} de su estado actual a un roadmap claro de cumplimiento.

### Alcance

```
Semana 0: PREPARACION
├── Onboarding + NDA
├── Envio de Pre-Assessment Worksheet al cliente
└── Revision de documentacion existente

Semana 1: DISCOVERY + ENTREVISTAS
├── Entrevista Data Governance (45 min)
├── Entrevista Data Security (45 min)
├── Entrevista Data Integration (45 min)
└── Inventario de datos y sistemas

Semana 2: ANALISIS + SCORING
├── Scoring de madurez CMM 0-5 por KA y subdimension
├── Gap analysis vs requisitos Ley 21.719 (Current vs Target Profile)
├── Evaluacion de riesgos priorizada
└── Identificacion de quick wins

Semana 3: ENTREGABLES + PRESENTACION
├── Reporte ejecutivo DRA
├── Roadmap de adecuacion en 3 fases
├── Presentacion final al equipo directivo (60 min)
└── Entrega de 7 documentos listos para implementar
```

### Entregables

| #   | Entregable                                | Descripcion                                                                                      |
| --- | ----------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 1   | **Reporte Ejecutivo DRA**                 | Score de madurez CMM (0-5) por area, brechas criticas, riesgo financiero cuantificado, quick wins |
| 2   | **Matriz de Gap Analysis**                | Current vs Target por KA y subdimension, mapeado a 10 obligaciones de la Ley 21.719              |
| 3   | **Roadmap de Adecuacion (3 fases)**       | Quick wins (0-3 meses), acciones core (3-6 meses), mejora continua (6-12 meses) con responsables |
| 4   | **Template RAT Pre-Poblado**              | Registro de Actividades de Tratamiento con ejemplos tipicos de su sector (9 columnas formato SGD) |
| 5   | **Inventario de Datos Validado**          | Inventario completo de sistemas, datos, terceros y flujos de datos de {EMPRESA}                  |
| 6   | **Guia AIPD Simplificada** (si aplica)    | Arbol de decision + metodologia de evaluacion de impacto para tratamientos de alto riesgo         |
| 7   | **Benchmarks de Retencion por Sector**    | Periodos de conservacion por tipo de dato basados en normativa chilena vigente                    |

### Metodologia

Este proyecto utiliza el **Data Readiness Assessment (DRA)**, basado en 3 frameworks internacionales:

- **DAMA-DMBOK2** — QUE evaluar: 3 Knowledge Areas clave (Governance, Security, Integration)
- **NIST Privacy Framework** — CONTRA QUE comparar: Current Profile vs Target Profile
- **CMM/CMMI** — COMO medir: scoring de madurez 0-5 con criterios observables

Evaluacion en 3 KAs x 5 subdimensiones (roles, procesos, herramientas, calidad, riesgos) = **15 puntos de evaluacion**.

**Alineado con las 10 recomendaciones de la WikiGuia del Gobierno Digital** (95% de cobertura).

---

## 3. Inversion

### Opcion Recomendada

| Concepto                        | Valor                 |
| ------------------------------- | --------------------- |
| **DRA Assessment Completo**     | $1.500.000 - $3.000.000 CLP |
| **Duracion**                    | 3 semanas             |
| **Sesiones con cliente**        | 3 entrevistas (45 min) + 1 presentacion (60 min) |
| **Modalidad**                   | 100% remoto           |
| **Entregables**                 | 7 documentos listos para implementar |

### Condiciones de Pago

| Hito          | Porcentaje | Monto           | Momento                   |
| ------------- | ---------- | --------------- | ------------------------- |
| Anticipo      | 50%        | ${ANTICIPO} USD | Firma de contrato         |
| Entrega final | 50%        | ${SALDO} USD    | Aprobacion de entregables |

### Servicios Adicionales (Opcionales)

| Servicio                  | Precio              | Descripcion                                  |
| ------------------------- | ------------------- | -------------------------------------------- |
| Implementacion Quick Wins | +${PRECIO_QW} USD   | Apoyo en implementar las acciones de 30 dias |
| Capacitacion equipo       | +${PRECIO_CAP} USD  | 2 sesiones de capacitacion a personal clave  |
| Acompanamiento mensual    | +${PRECIO_MENS}/mes | Seguimiento mensual post-diagnostico         |

---

## 4. ROI del Proyecto

### Analisis Costo-Beneficio

| Factor                                 | Valor         |
| -------------------------------------- | ------------- |
| **Costo del diagnostico**              | ${PRECIO} USD |
| **Costo de NO cumplir** (multa minima) | $350,000 USD  |
| **Ratio costo/riesgo**                 | {RATIO}%      |

### Calculo de Retorno

```
Escenario: Evitar UNA multa leve

Multa evitada:        $350,000 USD
Inversion:            $  {PRECIO} USD
                      ─────────────
Retorno:              ${RETORNO} USD
ROI:                  {ROI_PERCENT}%
```

### Beneficios Adicionales

- **Ventaja competitiva**: Demostrar cumplimiento antes que competidores
- **Confianza de clientes**: Proteccion de datos como diferenciador
- **Eficiencia operacional**: Procesos de datos documentados y optimizados
- **Reduccion de riesgos**: Preparacion ante fiscalizaciones

---

## 5. Timeline

### Cronograma Propuesto

| Semana    | Actividades                                    | Entregable                          |
| --------- | ---------------------------------------------- | ----------------------------------- |
| 0         | Onboarding + Pre-Assessment Worksheet          | NDA firmado, documentacion recibida |
| 1         | 3 entrevistas (Governance, Security, Integration) | Inventario de datos borrador     |
| 2         | Scoring CMM + Gap Analysis + Roadmap           | Borrador reporte DRA                |
| 3         | Consolidacion + Presentacion final (60 min)    | **6 entregables finales**           |

### Hitos Clave

| Hito                | Fecha Propuesta     |
| ------------------- | ------------------- |
| Firma contrato      | {FECHA_FIRMA}       |
| Kick-off            | {FECHA_KICKOFF}     |
| Revision intermedia | {FECHA_INTERMEDIA}  |
| **Entrega final**   | **{FECHA_ENTREGA}** |

---

## 6. Equipo

### Consultor Principal

**{TU_NOMBRE}**

- Especialista en gestion de datos, procesos y transformacion digital
- Metodologia DRA basada en DAMA-DMBOK2, NIST Privacy Framework y CMM/CMMI
- Experiencia en proyectos de compliance y gobierno de datos

### Compromiso

- Dedicacion: {HORAS} horas semanales
- Disponibilidad: Respuesta en menos de 24 horas habiles
- Comunicacion: Reuniones semanales de seguimiento

---

## 7. Proximos Pasos

### Para Avanzar

1. **Confirmar aceptacion** de esta propuesta
2. **Firma de contrato** de servicios
3. **Pago de anticipo** (50%)
4. **Agendar kick-off** para semana de {SEMANA_KICKOFF}

### Contacto

Para consultas o aclaraciones:

- **Email:** {TU_EMAIL}
- **Telefono:** {TU_TELEFONO}
- **LinkedIn:** {TU_LINKEDIN}

---

## Terminos y Condiciones

### Confidencialidad

Toda la informacion compartida durante el proyecto sera tratada como confidencial. Se firmara NDA si el cliente lo requiere.

### Propiedad Intelectual

Los entregables del proyecto son propiedad de {EMPRESA} una vez pagados en su totalidad. La metodologia DRA (Data Readiness Assessment) es propiedad de The Wise Monkey Project.

### Validez

Esta propuesta es valida por 15 dias calendario desde la fecha de emision.

---

**Aceptacion de Propuesta**

Por la presente, {EMPRESA} acepta los terminos de esta propuesta.

| Campo  | Firma                         |
| ------ | ----------------------------- |
| Nombre | _____________________________ |
| Cargo  | _____________________________ |
| Fecha  | _____________________________ |
| Firma  | _____________________________ |

---

*Propuesta preparada por The Wise Monkey Project*
*Basado en DRA (Data Readiness Assessment) — DAMA-DMBOK2, NIST PF, CMM/CMMI*
*{FECHA}*
