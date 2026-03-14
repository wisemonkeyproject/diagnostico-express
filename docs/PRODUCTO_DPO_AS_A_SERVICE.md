# Producto: DPO-as-a-Service

## The Wise Monkey Project — Febrero 2026

---

## Fundamento Legal (Ley 21.719)

El producto está anclado en tres artículos de la ley que forman un sistema:

### Art. 49 — Modelo de Prevención de Infracciones

Los responsables de datos **podrán voluntariamente** adoptar un modelo de prevención consistente en un programa de cumplimiento. El programa debe contener **al menos**:

| Elemento                                          | Lo que exige la ley                                    | Lo que nosotros entregamos         |
| ------------------------------------------------- | ------------------------------------------------------ | ---------------------------------- |
| a) Designación de delegado de protección de datos | Obligatorio dentro del modelo                          | **Nosotros somos el delegado**     |
| b) Medios y facultades del delegado               | Definidos por la empresa                               | Template de resolución + SLA       |
| c) Identificación de datos tratados               | Tipo, territorio, categoría, bases de datos, titulares | **Inventario de datos (RAT)**      |
| d) Identificación de actividades de riesgo        | Procesos habituales o esporádicos con riesgo           | **Mapa de riesgos de tratamiento** |
| e) Protocolos y procedimientos                    | Para prevenir infracciones                             | **Manual de procedimientos**       |
| f) Mecanismos de reporte                          | Interno + hacia la Agencia (Art. 14 sexies)            | **Protocolo de brechas**           |
| g) Sanciones internas                             | Procedimientos de denuncia/castigo                     | **Reglamento interno de datos**    |

**Dato clave**: La ley dice "voluntariamente", pero el Art. 36 establece que tener un modelo certificado es **circunstancia atenuante** (punto 5). Tenerlo puede ser la diferencia entre una multa de $700K y una amonestación.

### Art. 50 — Atribuciones del Delegado

La ley define **8 funciones obligatorias** del delegado:

| #   | Función legal (Art. 50)                                                    | Entregable DPO-aaS                                               |
| --- | -------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| a   | Informar y asesorar al responsable, encargados, mandatarios y dependientes | **Canal de consultas + asesoría permanente**                     |
| b   | Promover y participar en la política de protección de datos                | **Política de protección de datos (redacción + revisión anual)** |
| c   | Supervisar cumplimiento de la ley y políticas internas                     | **Auditoría trimestral de cumplimiento**                         |
| d   | Formación permanente del personal                                          | **Programa de capacitación semestral**                           |
| e   | Asistir en identificación de riesgos y medidas                             | **Evaluación de Impacto (EIPD) por evento**                      |
| f   | Desarrollar plan anual de trabajo y rendir cuenta                          | **Plan anual + reporte de gestión**                              |
| g   | Absolver consultas y solicitudes de titulares                              | **Gestión de derechos ARCO-POL**                                 |
| h   | Cooperar y ser punto de contacto con la Agencia                            | **Representación ante la Agencia**                               |

### Art. 51 — Certificación

- La Agencia **certifica** que el modelo cumple los requisitos
- Las entidades certificadas se inscriben en el **Registro Nacional de Sanciones y Cumplimiento**
- Los certificados tienen **vigencia de 3 años** (Art. 52)
- Estar certificado = **atenuante de responsabilidad** (Art. 36.5)

**Implicación comercial**: Nuestro servicio DPO-aaS no solo "cumple la ley" — **prepara para la certificación**, que es el escudo real contra multas.

### Requisitos del Delegado (Art. 50)

| Requisito              | Qué dice la ley                                                 | Cómo lo cumplimos                           |
| ---------------------- | --------------------------------------------------------------- | ------------------------------------------- |
| Designación            | Por la máxima autoridad directiva                               | Resolución firmada por gerente general      |
| Autonomía              | No sujeto a instrucciones en materias de protección             | Contrato con cláusula de independencia      |
| Idoneidad              | Requisitos de idoneidad, capacidad y conocimientos específicos  | CV + certificaciones del consultor asignado |
| Secreto                | Estricto secreto y confidencialidad                             | NDA incluido en el contrato                 |
| Recursos               | Medios y facultades suficientes según tamaño de la entidad      | Definidos en SLA por plan                   |
| Conflicto de intereses | Puede tener otras funciones si no hay conflicto                 | Garantizado al ser externo                  |
| Grupo empresarial      | Un delegado para todo el grupo si operan bajo mismos estándares | Plan Enterprise lo contempla                |

### Excepción PYMEs (Art. 50 inc. 3)

> "En las micro, pequeñas y medianas empresas, el dueño o sus máximas autoridades podrán asumir personalmente las tareas de delegado de protección de datos."

**Implicación**: Las PYMEs no están obligadas a tener DPO externo. Pero si quieren el **modelo de prevención certificado** (Art. 49+51), que es atenuante (Art. 36), necesitan alguien con idoneidad. Ahí entramos nosotros: *"Tú puedes ser tu propio DPO, pero ¿tienes tiempo y conocimiento? Nosotros lo hacemos por ti."*

---

## Diseño del Producto

### Arquitectura del Servicio

```
ONBOARDING (Mes 1)                    OPERACIÓN RECURRENTE (Mes 2+)
┌─────────────────────┐               ┌──────────────────────────┐
│ 1. Diagnóstico base │               │ Supervisión continua     │
│ 2. Inventario datos  │               │ Gestión derechos ARCO    │
│ 3. Mapa de riesgos  │               │ Canal de consultas       │
│ 4. Gap analysis      │               │ Reportes trimestrales    │
│ 5. Plan de trabajo   │               │ Capacitación semestral   │
│ 6. Docs fundacionales│               │ Auditoría de cumplimiento│
└─────────┬───────────┘               │ Actualización regulatoria│
          │                            └──────────┬───────────────┘
          ▼                                       ▼
    ENTREGABLES                              HACIA
    INICIALES                            CERTIFICACIÓN
    (one-shot)                              (Art. 51)
```

### Onboarding: Lo que se entrega el Mes 1

| #   | Entregable                                       | Descripción                                                                | Esfuerzo estimado |
| --- | ------------------------------------------------ | -------------------------------------------------------------------------- | ----------------- |
| 1   | **Diagnóstico de cumplimiento**                  | Evaluación completa vs. los 7 elementos del Art. 49                        | 8-12 horas        |
| 2   | **Registro de Actividades de Tratamiento (RAT)** | Inventario completo: qué datos, para qué, base legal, retención, acceso    | 12-20 horas       |
| 3   | **Mapa de riesgos**                              | Procesos con riesgo de infracción (Art. 49.d), clasificación por severidad | 6-8 horas         |
| 4   | **Política de protección de datos**              | Documento maestro, aprobado por dirección                                  | 6-8 horas         |
| 5   | **Protocolo de brechas**                         | Procedimiento de detección, contención, notificación (72h) y registro      | 4-6 horas         |
| 6   | **Protocolo de derechos ARCO-POL**               | Procedimiento para recibir, evaluar y responder solicitudes de titulares   | 4-6 horas         |
| 7   | **Resolución de designación**                    | Documento formal nombrando al DPO externo                                  | 2 horas           |
| 8   | **Plan anual de trabajo**                        | Cronograma de actividades del delegado (Art. 50.f)                         | 3-4 horas         |
|     | **TOTAL ONBOARDING**                             |                                                                            | **45-65 horas**   |

### Operación Mensual: Lo que se entrega cada mes/trimestre

| Actividad                          | Frecuencia | Horas/mes | Plan Esencial | Plan Profesional | Plan Enterprise |
| ---------------------------------- | ---------- | --------- |:-------------:|:----------------:|:---------------:|
| Canal de consultas (email/chat)    | Permanente | 2-4h      | SI            | SI               | SI              |
| Gestión solicitudes ARCO-POL       | Por evento | 1-3h      | SI            | SI               | SI              |
| Supervisión de cumplimiento        | Mensual    | 2-4h      | SI            | SI               | SI              |
| Actualización regulatoria          | Mensual    | 1-2h      | SI            | SI               | SI              |
| Reporte trimestral a dirección     | Trimestral | 3-4h      | -             | SI               | SI              |
| Auditoría interna de cumplimiento  | Trimestral | 4-8h      | -             | SI               | SI              |
| Capacitación al personal           | Semestral  | 4-6h      | -             | SI               | SI              |
| Evaluación de impacto (EIPD)       | Por evento | 8-16h     | -             | -                | SI              |
| Simulacro de brecha                | Semestral  | 3-4h      | -             | -                | SI              |
| Revisión de contratos con terceros | Trimestral | 4-8h      | -             | -                | SI              |
| Preparación para certificación     | Anual      | 20-40h    | -             | -                | SI              |
| **TOTAL horas/mes (promedio)**     |            |           | **5-8h**      | **12-20h**       | **25-40h**      |

---

## Planes y Pricing

### Plan Esencial — "Cumplimiento Base"

**Target**: Micro y pequeña empresa (<50 personas) con datos no sensibles.

| Componente               | Detalle                                               |
| ------------------------ | ----------------------------------------------------- |
| **Precio**               | USD $500-800/mes (contrato anual)                     |
| **Onboarding**           | Incluido en primeros 2 meses (sin cobro adicional)    |
| **Horas mensuales**      | 5-8 horas                                             |
| **DPO designado**        | Sí (consultor asignado)                               |
| **Canal de consultas**   | Email, respuesta en 48h hábiles                       |
| **Gestión ARCO-POL**     | Hasta 5 solicitudes/mes                               |
| **Supervisión**          | Checklist mensual de cumplimiento                     |
| **Documentos incluidos** | RAT, política, protocolo brechas, protocolo ARCO      |
| **Capacitación**         | No incluida (add-on $300/sesión)                      |
| **Reportes**             | Resumen semestral                                     |
| **No incluye**           | EIPD, auditoría trimestral, certificación, simulacros |

**Mensaje de venta**: *"Todo lo mínimo que necesitas para cumplir la ley desde el día 1, sin contratar a nadie full-time."*

### Plan Profesional — "Gestión Activa"

**Target**: Mediana empresa (50-200 personas) o empresa con datos sensibles.

| Componente               | Detalle                                                    |
| ------------------------ | ---------------------------------------------------------- |
| **Precio**               | USD $1.200-2.000/mes (contrato anual)                      |
| **Onboarding**           | Incluido en primeros 2 meses                               |
| **Horas mensuales**      | 12-20 horas                                                |
| **DPO designado**        | Sí (consultor senior asignado + backup)                    |
| **Canal de consultas**   | Email + videollamada mensual, respuesta en 24h hábiles     |
| **Gestión ARCO-POL**     | Hasta 15 solicitudes/mes                                   |
| **Supervisión**          | Auditoría trimestral de cumplimiento                       |
| **Documentos incluidos** | Todo Esencial + reglamento interno, contratos con terceros |
| **Capacitación**         | 2 sesiones/año incluidas (hasta 20 personas)               |
| **Reportes**             | Reporte trimestral para directorio                         |
| **EIPD**                 | 1 evaluación/año incluida (adicionales $800 c/u)           |
| **No incluye**           | Simulacros, preparación certificación                      |

**Mensaje de venta**: *"Gestión profesional de protección de datos con visibilidad para tu directorio y preparación real para fiscalización."*

### Plan Enterprise — "Camino a Certificación"

**Target**: Empresa grande (200+ personas), grupo empresarial, o empresa con alto volumen de datos sensibles.

| Componente               | Detalle                                                      |
| ------------------------ | ------------------------------------------------------------ |
| **Precio**               | USD $3.000-5.000/mes (contrato anual)                        |
| **Onboarding**           | Incluido en primeros 3 meses (más extenso)                   |
| **Horas mensuales**      | 25-40 horas                                                  |
| **DPO designado**        | Consultor senior dedicado + equipo de soporte                |
| **Canal de consultas**   | Email + chat + videollamada semanal, respuesta en 8h hábiles |
| **Gestión ARCO-POL**     | Ilimitadas                                                   |
| **Supervisión**          | Auditoría trimestral + monitoreo continuo                    |
| **Documentos incluidos** | Todo Profesional + todos los elementos del Art. 49 completos |
| **Capacitación**         | 4 sesiones/año + e-learning para toda la organización        |
| **Reportes**             | Reporte mensual + dashboard de cumplimiento                  |
| **EIPD**                 | Hasta 4/año incluidas                                        |
| **Simulacros**           | 2 simulacros de brecha/año                                   |
| **Certificación**        | Preparación completa para certificación Art. 51              |
| **Contratos terceros**   | Revisión trimestral de cláusulas con proveedores/mandatarios |
| **Grupo empresarial**    | Un DPO para múltiples entidades (Art. 50)                    |

**Mensaje de venta**: *"El camino completo hacia la certificación ante la Agencia. El máximo escudo contra multas y el máximo valor reputacional."*

---

## Comparativa Rápida

|                                        | Esencial  | Profesional     | Enterprise         |
| -------------------------------------- |:---------:|:---------------:|:------------------:|
| **Precio/mes**                         | $500-800  | $1.200-2.000    | $3.000-5.000       |
| DPO designado formalmente              | SI        | SI              | SI                 |
| Onboarding (RAT, política, protocolos) | SI        | SI              | SI                 |
| Canal consultas                        | Email 48h | Email+video 24h | Multicanal 8h      |
| Gestión ARCO-POL                       | 5/mes     | 15/mes          | Ilimitado          |
| Capacitación                           | Add-on    | 2/año           | 4/año + e-learning |
| Auditoría trimestral                   | -         | SI              | SI                 |
| Reporte para directorio                | Semestral | Trimestral      | Mensual            |
| EIPD                                   | -         | 1/año           | 4/año              |
| Simulacro de brecha                    | -         | -               | SI                 |
| Preparación certificación              | -         | -               | SI                 |
| Revisión contratos terceros            | -         | -               | SI                 |

---

## Proceso de Venta: Del Diagnóstico Express al DPO-aaS

```
DIAGNÓSTICO EXPRESS (gratis, 10 min)
    │
    ▼
Score + Brechas identificadas
    │
    ├── Score ALTO RIESGO ──────────► Llamada urgente
    │                                  "Necesitas DPO ya"
    │                                       │
    ├── Score MEDIO RIESGO ─────────► Llamada consultiva
    │                                  "Tienes gaps específicos"
    │                                       │
    └── Score BAJO RIESGO ──────────► Follow-up educativo
                                       "Bien, pero revisa esto"
                                            │
                                            ▼
                                  DIAGNÓSTICO PROFUNDO
                                  (USD $1.500-3.000, 2-3 semanas)
                                  = Onboarding del DPO-aaS
                                            │
                                            ▼
                                  ┌─────────────────────┐
                                  │ PROPUESTA DPO-aaS   │
                                  │                     │
                                  │ "El diagnóstico     │
                                  │  profundo que       │
                                  │  acabamos de hacer  │
                                  │  ES el onboarding.  │
                                  │  Ya tienes el RAT,  │
                                  │  la política, los   │
                                  │  protocolos.        │
                                  │                     │
                                  │  ¿Por qué parar     │
                                  │  aquí? Por $X/mes   │
                                  │  mantenemos todo    │
                                  │  actualizado."      │
                                  └─────────────────────┘
```

**Insight clave**: El diagnóstico profundo one-shot ($1.5-3K) **es** el onboarding del DPO-aaS. El cliente ya pagó por los entregables iniciales. La conversión a recurrente es natural: *"Ya hicimos el trabajo duro. Ahora solo hay que mantenerlo vivo."*

---

## Argumentario de Venta

### Para el que dice "No necesito DPO, soy PYME"

> "Tienes razón, la ley dice que puedes ser tu propio DPO. Pero también dice que el DPO debe tener 'idoneidad, capacidad y conocimientos específicos' (Art. 50). ¿Tienes tiempo para mantenerte al día con los reglamentos, gestionar solicitudes ARCO, hacer auditorías trimestrales y ser punto de contacto con la Agencia? Por $500/mes, nosotros hacemos todo eso."

### Para el que dice "Ya tengo abogado"

> "Perfecto. Tu abogado redacta las políticas legales. Nosotros las implementamos en tus procesos reales. ¿Quién revisa que el área de marketing realmente pida consentimiento? ¿Quién capacita al equipo de ventas? ¿Quién responde cuando un cliente pide que borres sus datos? Eso es lo que hace un DPO. Trabajamos con tu abogado, no lo reemplazamos."

### Para el que dice "Esperaré a que empiece a funcionar la Agencia"

> "La Agencia se instala en junio 2026, 6 meses antes de la vigencia. Cuando arranque va a necesitar casos ejemplares para mostrar que funciona. ¿Quieres ser ese ejemplo, o quieres estar preparado? Además, implementar un modelo de prevención toma 3-6 meses. Si empiezas en septiembre, no llegas."

### Para el que dice "Es muy caro"

> "Un DPO interno en Chile gana entre $2.000-5.000/mes más cargas sociales. Un abogado externo cobra $200-400/hora. Nuestro Plan Esencial cuesta $500/mes por un servicio completo con 5-8 horas de dedicación. Y si no tienes nada implementado y la Agencia te multa, la infracción más leve parte en $350.000 USD."

### Para el que llega por "cascada de proveedores" (H4)

> "Tu cliente grande te mandó una carta pidiendo cumplimiento. Si no respondes, pierdes el contrato. Si inventas algo improvisado, no pasa la auditoría. Nosotros implementamos todo en 4-6 semanas y te damos un certificado de cumplimiento que puedes enviar a tu cliente."

---

## Entregables Tipo (Templates Necesarios)

### Para Onboarding

| #   | Template                                     | Estado    |
| --- | -------------------------------------------- | --------- |
| 1   | Registro de Actividades de Tratamiento (RAT) | Por crear |
| 2   | Política de Protección de Datos Personales   | Por crear |
| 3   | Protocolo de Gestión de Brechas de Seguridad | Por crear |
| 4   | Protocolo de Derechos ARCO-POL               | Por crear |
| 5   | Resolución de Designación del DPO            | Por crear |
| 6   | Contrato de Servicios DPO Externo            | Por crear |
| 7   | Plan Anual de Trabajo del DPO                | Por crear |
| 8   | Mapa de Riesgos de Tratamiento de Datos      | Por crear |
| 9   | Reglamento Interno de Protección de Datos    | Por crear |
| 10  | Formulario de Consentimiento Modelo          | Por crear |

### Para Operación Recurrente

| #   | Template                             | Frecuencia | Estado    |
| --- | ------------------------------------ | ---------- | --------- |
| 11  | Checklist de Supervisión Mensual     | Mensual    | Por crear |
| 12  | Reporte Trimestral para Directorio   | Trimestral | Por crear |
| 13  | Informe de Auditoría de Cumplimiento | Trimestral | Por crear |
| 14  | Formulario de Solicitud ARCO-POL     | Por evento | Por crear |
| 15  | Registro de Solicitudes ARCO-POL     | Continuo   | Por crear |
| 16  | Evaluación de Impacto (EIPD)         | Por evento | Por crear |
| 17  | Informe de Simulacro de Brecha       | Semestral  | Por crear |
| 18  | Plan Anual de Capacitación           | Anual      | Por crear |
| 19  | Acta de Capacitación (asistencia)    | Por sesión | Por crear |
| 20  | Informe Anual de Gestión del DPO     | Anual      | Por crear |

---

## Unit Economics Detallados

### Costo de Servir (por cliente/mes)

| Concepto                       | Esencial     | Profesional      | Enterprise       |
| ------------------------------ | ------------ | ---------------- | ---------------- |
| Horas consultor/mes            | 5-8h         | 12-20h           | 25-40h           |
| Costo hora consultor (interno) | ~$25         | ~$35             | ~$45             |
| **Costo de servir**            | **$125-200** | **$420-700**     | **$1.125-1.800** |
| **Precio cobrado**             | **$500-800** | **$1.200-2.000** | **$3.000-5.000** |
| **Margen bruto**               | **60-75%**   | **65-75%**       | **63-72%**       |

### Proyección de Ingresos

| Escenario                  | Clientes                  | MRR          | ARR         | Margen bruto |
| -------------------------- | ------------------------- | ------------ | ----------- | ------------ |
| **Mes 6** (arranque)       | 8 Esen + 2 Prof           | $6.4K-10.4K  | $77-125K    | ~70%         |
| **Mes 12** (crecimiento)   | 15 Esen + 6 Prof + 2 Ent  | $21.6K-35.2K | $259-422K   | ~70%         |
| **Mes 18** (escala)        | 25 Esen + 10 Prof + 4 Ent | $36.5K-60K   | $438-720K   | ~68%         |
| **Mes 24** (consolidación) | 35 Esen + 15 Prof + 6 Ent | $53.5K-89K   | $642K-1.07M | ~67%         |

### Capacidad Operativa

| Métrica                             | Valor                                          |
| ----------------------------------- | ---------------------------------------------- |
| Horas disponibles por consultor/mes | ~160h                                          |
| Clientes Esencial por consultor     | 20-30                                          |
| Clientes Profesional por consultor  | 8-12                                           |
| Clientes Enterprise por consultor   | 4-6                                            |
| **Punto de contratación**           | Al llegar a 15 clientes Esencial o equivalente |

---

## Riesgos y Mitigaciones

| Riesgo                                                                 | Probabilidad | Impacto | Mitigación                                                                                 |
| ---------------------------------------------------------------------- | ------------ | ------- | ------------------------------------------------------------------------------------------ |
| Cliente demanda al DPO externo por brecha                              | Media        | Alto    | Seguro de responsabilidad civil profesional + cláusula de limitación en contrato           |
| Reglamentos cambian el alcance del DPO                                 | Alta         | Medio   | Cláusula de revisión de pricing ante cambios regulatorios                                  |
| Cliente no colabora / no implementa recomendaciones                    | Alta         | Medio   | Registro documentado de recomendaciones + carta de descargo                                |
| Conflicto de intereses por atender múltiples clientes del mismo sector | Baja         | Alto    | Política de muralla china + límite de clientes por sector                                  |
| Agencia exige DPO interno (no externo)                                 | Baja         | Alto    | La ley no lo prohíbe; monitorear reglamentos. Pivotar a modelo de "asesor del DPO interno" |
| Escala excede capacidad operativa                                      | Media        | Medio   | Contratación escalonada + herramientas de automatización                                   |

---

## Próximos Pasos para Lanzar

### Fase 0 — Fundamentos (2-3 semanas)

| #   | Acción                                                         | Prioridad |
| --- | -------------------------------------------------------------- | --------- |
| 1   | Crear los 10 templates de onboarding                           | Crítica   |
| 2   | Redactar contrato de servicios DPO externo                     | Crítica   |
| 3   | Definir SLA por plan (tiempos de respuesta, horas, etc.)       | Crítica   |
| 4   | Crear página de servicio (landing page o sección en sitio web) | Alta      |
| 5   | Cotizar seguro de responsabilidad civil profesional            | Alta      |

### Fase 1 — Piloto (4-6 semanas)

| #   | Acción                                                              | Prioridad |
| --- | ------------------------------------------------------------------- | --------- |
| 6   | Ofrecer DPO-aaS a los primeros 3-5 clientes del diagnóstico express | Crítica   |
| 7   | Ejecutar onboarding completo con precio piloto (20-30% descuento)   | Alta      |
| 8   | Iterar templates y proceso basándose en experiencia real            | Alta      |
| 9   | Documentar caso de éxito del primer cliente                         | Alta      |

### Fase 2 — Comercialización (post-piloto)

| #   | Acción                                                         | Prioridad |
| --- | -------------------------------------------------------------- | --------- |
| 10  | Incorporar DPO-aaS en la secuencia de emails y pitch de ventas | Crítica   |
| 11  | Crear materiales de venta (one-pager, comparativa de planes)   | Alta      |
| 12  | Establecer alianza con estudio jurídico para referidos mutuos  | Alta      |
| 13  | Crear los 10 templates de operación recurrente                 | Media     |

---

## Resumen Ejecutivo

**DPO-as-a-Service** es un producto de ingreso recurrente anclado en los artículos 49, 50 y 51 de la Ley 21.719. Ofrece a empresas chilenas un delegado de protección de datos externo con todas las funciones que exige la ley, desde $500/mes.

**Diferenciación**: No vendemos "cumplimiento legal" — vendemos el modelo de prevención certificable que es la mejor defensa contra multas y la llave para mantener contratos con clientes grandes.

**El insight de conversión**: El diagnóstico profundo ($1.5-3K) ya genera los entregables del onboarding. Convertir ese cliente one-shot a DPO recurrente es la transición natural: *"Ya hicimos el trabajo duro. Por $X/mes, lo mantenemos vivo."*

**Proyección**: 15 clientes Esencial + 6 Profesional + 2 Enterprise al mes 12 = **$21-35K MRR** con **~70% margen bruto**.

---

*Documento generado por Wise Monkey (super-research + análisis legal) | Febrero 2026*
*Basado en: Ley 21.719 (Arts. 36, 49, 50, 51, 52), modelos DPO-aaS europeos (DataGuard, DPO Centre), Encuesta PwC Chile 2025*

**Fuentes legales**:

- [Ley 21.719 texto completo — BCN](https://www.bcn.cl/leychile/navegar?idNorma=1209272)
- [Guía Gobierno Digital Chile](https://wikiguias.digital.gob.cl/datos-personales/guia-practica-implementacion-nueva-ley-datos-personales)

**Fuentes de mercado**:

- [Captain Compliance — DPO Costs Guide](https://captaincompliance.com/education/data-protection-officer-costs/)
- [DataGuard — Outsourced DPO Services](https://www.dataguard.com/outsourced-dpo-services/)
- [DPO Centre — Outsourced DPO](https://www.dpocentre.com/services/outsourced-dpo-services/)
