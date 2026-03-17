/**
 * Google Apps Script - Receptor Quick-Scan DRA
 *
 * INSTRUCCIONES DE SETUP:
 * 1. Crea un Google Sheet nuevo
 * 2. Ve a Extensiones > Apps Script
 * 3. Pega este codigo completo
 * 4. Click en "Implementar" > "Nueva implementacion"
 * 5. Tipo: "Aplicacion web"
 * 6. Ejecutar como: "Yo" (tu cuenta)
 * 7. Acceso: "Cualquier persona"
 * 8. Click "Implementar" y copia la URL
 * 9. Pega esa URL en GOOGLE_SHEET_URL del archivo quick-scan-dra.html
 */

function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var data = JSON.parse(e.postData.contents);

    // Crear headers si la hoja esta vacia
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        "Timestamp", "Nombre", "Email", "Empresa", "Cargo",
        "Tamano", "Sector",
        "Q1 Gobernanza", "Q2 Acceso", "Q3 Proteccion", "Q4 Flujos",
        "Q5 Consentimiento/ARCOP", "Q6 Capacitacion", "Q7 Incidentes",
        "Score %", "Nivel", "Area Critica", "KAs Sugeridas",
        "KA Governance %", "KA Security %", "KA Integration %",
        "Estado Lead"
      ]);
      var headerRange = sheet.getRange(1, 1, 1, 22);
      headerRange.setFontWeight("bold");
      headerRange.setBackground("#1e1e2e");
      headerRange.setFontColor("#ffffff");
      sheet.setFrozenRows(1);
    }

    sheet.appendRow([
      data.timestamp || new Date().toISOString(),
      data.nombre || "",
      data.email || "",
      data.empresa || "",
      data.cargo || "",
      data.tamano || "",
      data.sector || "",
      data.q1 != null ? data.q1 : "",
      data.q2 != null ? data.q2 : "",
      data.q3 != null ? data.q3 : "",
      data.q4 != null ? data.q4 : "",
      data.q5 != null ? data.q5 : "",
      data.q6 != null ? data.q6 : "",
      data.q7 != null ? data.q7 : "",
      data.score_pct || 0,
      data.nivel || "",
      data.area_critica || "",
      data.kas_sugeridas || "",
      data.ka_governance_pct || 0,
      data.ka_security_pct || 0,
      data.ka_integration_pct || 0,
      "NUEVO"
    ]);

    // Colorear celda de nivel
    var lastRow = sheet.getLastRow();
    var nivelCell = sheet.getRange(lastRow, 16);
    var nivel = (data.nivel || "").toLowerCase();
    if (nivel === "critico") {
      nivelCell.setBackground("#fde8ea").setFontColor("#dc3545").setFontWeight("bold");
    } else if (nivel === "bajo") {
      nivelCell.setBackground("#fff3e0").setFontColor("#e65100").setFontWeight("bold");
    } else if (nivel === "medio") {
      nivelCell.setBackground("#e8f5e9").setFontColor("#28a745").setFontWeight("bold");
    } else if (nivel === "alto") {
      nivelCell.setBackground("#e3f2fd").setFontColor("#1565c0").setFontWeight("bold");
    }

    enviarNotificacion(data);

    return ContentService
      .createTextOutput(JSON.stringify({ status: "ok" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: "ok", message: "Quick-Scan DRA API activa" }))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * Notificacion por email cuando alguien completa el Quick-Scan.
 * Email HTML con resumen visual y CTAs para actuar rapido.
 */
function enviarNotificacion(data) {
  var email = "karim@wisemonkeygroup.com";
  var score = data.score_pct || 0;
  var nivel = data.nivel || "Sin nivel";
  var empresa = data.empresa || "Sin empresa";
  var nombre = data.nombre || "-";
  var contactEmail = data.email || "-";
  var cargo = data.cargo || "-";
  var sector = data.sector || "-";
  var tamano = data.tamano || "-";
  var areaCritica = data.area_critica || "-";
  var kasSugeridas = data.kas_sugeridas || "-";
  var govPct = data.ka_governance_pct || 0;
  var secPct = data.ka_security_pct || 0;
  var intPct = data.ka_integration_pct || 0;

  // Color y urgencia segun nivel
  var nivelColor, urgencia, tiempoContacto;
  if (nivel.toLowerCase() === "critico") {
    nivelColor = "#dc3545";
    urgencia = "URGENTE";
    tiempoContacto = "Contactar hoy";
  } else if (nivel.toLowerCase() === "bajo") {
    nivelColor = "#e65100";
    urgencia = "ALTA";
    tiempoContacto = "Contactar en 24h";
  } else if (nivel.toLowerCase() === "medio") {
    nivelColor = "#28a745";
    urgencia = "MEDIA";
    tiempoContacto = "Contactar en 48h";
  } else {
    nivelColor = "#1565c0";
    urgencia = "BAJA";
    tiempoContacto = "Contactar esta semana";
  }

  var subject = "[Quick-Scan DRA] " + urgencia + " | " + nivel + " (" + score + "%) - " + empresa;

  // Barra visual de score por KA
  function barraKA(nombre, pct) {
    var color = pct <= 25 ? "#dc3545" : pct <= 50 ? "#e65100" : pct <= 75 ? "#28a745" : "#1565c0";
    return '<tr>'
      + '<td style="padding:4px 8px;font-size:14px;">' + nombre + '</td>'
      + '<td style="padding:4px 8px;width:60%;"><div style="background:#e9ecef;border-radius:4px;height:16px;"><div style="background:' + color + ';height:16px;border-radius:4px;width:' + pct + '%;"></div></div></td>'
      + '<td style="padding:4px 8px;font-size:14px;font-weight:bold;color:' + color + ';">' + pct + '%</td>'
      + '</tr>';
  }

  var whatsappMsg = encodeURIComponent("Hola " + nombre + ", soy Karim de The Wise Monkey Project. Vi que completaste el Quick-Scan DRA y tu empresa " + empresa + " obtuvo un nivel " + nivel + " (" + score + "%). Me gustaria conversar 15 minutos sobre como podemos ayudarte a cerrar las brechas identificadas. Que horario te acomoda?");
  var whatsappUrl = "https://wa.me/?text=" + whatsappMsg;

  var htmlBody = '<div style="font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;max-width:600px;margin:0 auto;">'

    // Header
    + '<div style="background:#1e1e2e;color:white;padding:16px 24px;border-radius:8px 8px 0 0;">'
    + '<h1 style="margin:0;font-size:18px;">Quick-Scan DRA - Nuevo Lead</h1>'
    + '<p style="margin:4px 0 0;font-size:13px;opacity:0.8;">' + new Date().toLocaleString("es-CL") + '</p>'
    + '</div>'

    // Urgencia banner
    + '<div style="background:' + nivelColor + ';color:white;padding:12px 24px;font-size:14px;font-weight:bold;">'
    + 'Prioridad: ' + urgencia + ' - ' + tiempoContacto
    + '</div>'

    // Score principal
    + '<div style="text-align:center;padding:24px;background:#f5f5fa;">'
    + '<p style="margin:0;font-size:13px;text-transform:uppercase;letter-spacing:1px;color:#6c757d;">Nivel de Madurez</p>'
    + '<h2 style="margin:4px 0;font-size:24px;color:' + nivelColor + ';">' + nivel + '</h2>'
    + '<p style="margin:0;font-size:36px;font-weight:700;color:' + nivelColor + ';">' + score + '%</p>'
    + '</div>'

    // Contacto
    + '<div style="padding:16px 24px;background:white;border-bottom:1px solid #eee;">'
    + '<h3 style="margin:0 0 8px;font-size:15px;color:#1e1e2e;">Contacto</h3>'
    + '<table style="width:100%;font-size:14px;">'
    + '<tr><td style="color:#6c757d;padding:2px 0;width:80px;">Nombre</td><td style="font-weight:600;">' + nombre + '</td></tr>'
    + '<tr><td style="color:#6c757d;padding:2px 0;">Email</td><td><a href="mailto:' + contactEmail + '">' + contactEmail + '</a></td></tr>'
    + '<tr><td style="color:#6c757d;padding:2px 0;">Cargo</td><td>' + cargo + '</td></tr>'
    + '<tr><td style="color:#6c757d;padding:2px 0;">Empresa</td><td style="font-weight:600;">' + empresa + '</td></tr>'
    + '<tr><td style="color:#6c757d;padding:2px 0;">Sector</td><td>' + sector + '</td></tr>'
    + '<tr><td style="color:#6c757d;padding:2px 0;">Tamano</td><td>' + tamano + '</td></tr>'
    + '</table>'
    + '</div>'

    // Scores por KA
    + '<div style="padding:16px 24px;background:white;border-bottom:1px solid #eee;">'
    + '<h3 style="margin:0 0 12px;font-size:15px;color:#1e1e2e;">Score por Knowledge Area</h3>'
    + '<table style="width:100%;">'
    + barraKA("Governance", govPct)
    + barraKA("Security", secPct)
    + barraKA("Integration", intPct)
    + '</table>'
    + '<p style="margin:12px 0 0;font-size:13px;color:#dc3545;font-weight:600;">Area critica: ' + areaCritica + '</p>'
    + '<p style="margin:4px 0 0;font-size:13px;color:#6c757d;">KAs sugeridas: ' + kasSugeridas + '</p>'
    + '</div>'

    // Detalle respuestas
    + '<div style="padding:16px 24px;background:#f9f9fc;border-bottom:1px solid #eee;">'
    + '<h3 style="margin:0 0 8px;font-size:15px;color:#1e1e2e;">Respuestas</h3>'
    + '<table style="width:100%;font-size:13px;">'
    + '<tr><td style="padding:2px 0;color:#6c757d;">Q1 Gobernanza</td><td style="font-weight:600;">' + (data.q1 != null ? data.q1 : "-") + '/4</td>'
    + '<td style="padding:2px 0 2px 16px;color:#6c757d;">Q2 Acceso</td><td style="font-weight:600;">' + (data.q2 != null ? data.q2 : "-") + '/4</td></tr>'
    + '<tr><td style="padding:2px 0;color:#6c757d;">Q3 Proteccion</td><td style="font-weight:600;">' + (data.q3 != null ? data.q3 : "-") + '/4</td>'
    + '<td style="padding:2px 0 2px 16px;color:#6c757d;">Q4 Flujos</td><td style="font-weight:600;">' + (data.q4 != null ? data.q4 : "-") + '/4</td></tr>'
    + '<tr><td style="padding:2px 0;color:#6c757d;">Q5 Consentimiento/ARCOP</td><td style="font-weight:600;">' + (data.q5 != null ? data.q5 : "-") + '/4</td>'
    + '<td style="padding:2px 0 2px 16px;color:#6c757d;">Q6 Capacitacion</td><td style="font-weight:600;">' + (data.q6 != null ? data.q6 : "-") + '/4</td></tr>'
    + '<tr><td style="padding:2px 0;color:#6c757d;">Q7 Incidentes</td><td style="font-weight:600;">' + (data.q7 != null ? data.q7 : "-") + '/4</td>'
    + '<td></td><td></td></tr>'
    + '</table>'
    + '</div>'

    // CTAs
    + '<div style="padding:24px;background:white;text-align:center;">'
    + '<h3 style="margin:0 0 16px;font-size:15px;color:#1e1e2e;">Acciones</h3>'
    + '<a href="mailto:' + contactEmail + '?subject=Quick-Scan%20DRA%20-%20' + encodeURIComponent(empresa) + '&body=' + encodeURIComponent("Hola " + nombre + ",\n\nGracias por completar el Quick-Scan DRA. Tu empresa obtuvo un nivel " + nivel + " (" + score + "%).\n\nMe gustaria agendar 15 minutos para conversar sobre como podemos ayudarte a cerrar las brechas identificadas, especialmente en " + areaCritica + ".\n\nQuedo atento,\nKarim Singer\nThe Wise Monkey Project") + '" style="display:inline-block;padding:10px 24px;background:#0066cc;color:white;text-decoration:none;border-radius:6px;font-weight:600;font-size:14px;margin:4px;">Enviar Email</a> '
    + '<a href="' + whatsappUrl + '" style="display:inline-block;padding:10px 24px;background:#25D366;color:white;text-decoration:none;border-radius:6px;font-weight:600;font-size:14px;margin:4px;">WhatsApp</a>'
    + '</div>'

    // Footer
    + '<div style="padding:12px 24px;background:#f5f5fa;border-radius:0 0 8px 8px;text-align:center;font-size:12px;color:#6c757d;">'
    + 'The Wise Monkey Project - Quick-Scan DRA'
    + '</div>'
    + '</div>';

  MailApp.sendEmail({
    to: email,
    subject: subject,
    htmlBody: htmlBody,
    body: "Nuevo Quick-Scan DRA: " + empresa + " | " + nivel + " (" + score + "%) | Contacto: " + nombre + " <" + contactEmail + "> | Area critica: " + areaCritica + " | " + tiempoContacto
  });
}
