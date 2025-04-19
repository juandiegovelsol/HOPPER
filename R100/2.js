const moment = require("moment-timezone");

function fechaColoquial(fechaStr) {
  // Formatea la cadena de fecha al formato deseado
  const fecha = moment.tz(fechaStr, "DD-MM-YYYY-HH-mm", "America/Santiago");

  // Verifica si la fecha es válida
  if (!fecha.isValid()) {
    return "Formato de fecha inválido. Por favor, use DD-MM-YYYY-HH-mm.";
  }

  // Obtiene la fecha y hora actual en Santiago
  const ahora = moment.tz("America/Santiago");

  // Calcula la diferencia entre la fecha dada y la fecha actual
  const diferencia = fecha.diff(ahora);

  // Verifica si la fecha es en el futuro o en el pasado
  if (diferencia > 0) {
    // Calcula cuánto falta
    const años = fecha.year() - ahora.year();
    const meses = fecha.month() - ahora.month();
    const días = fecha.date() - ahora.date();
    const horas = fecha.hour() - ahora.hour();
    const minutos = fecha.minute() - ahora.minute();

    const mensaje = `Falta ${diferencia > 0 ? "" : "más de "} ${años} ${
      años === 1 ? "año" : "años"
    } ${meses === 0 ? "" : `y ${meses} ${meses === 1 ? "mes" : "meses"}`} ${
      días === 0 ? "" : `y ${días} ${días === 1 ? "día" : "días"}`
    } ${horas === 0 ? "" : `y ${horas} ${horas === 1 ? "hora" : "horas"}`} ${
      minutos === 0
        ? ""
        : `y ${minutos} ${minutos === 1 ? "minuto" : "minutos"}`
    }`;
    return mensaje.trim();
  } else {
    // Calcula cuánto ha pasado
    const años = Math.abs(fecha.year() - ahora.year());
    const meses = Math.abs(fecha.month() - ahora.month());
    const días = Math.abs(fecha.date() - ahora.date());
    const horas = Math.abs(fecha.hour() - ahora.hour());
    const minutos = Math.abs(fecha.minute() - ahora.minute());

    const mensaje = `Pasó ${diferencia < 0 ? "más de " : ""} ${años} ${
      años === 1 ? "año" : "años"
    } ${meses === 0 ? "" : `y ${meses} ${meses === 1 ? "mes" : "meses"}`} ${
      días === 0 ? "" : `y ${días} ${días === 1 ? "día" : "días"}`
    } ${horas === 0 ? "" : `y ${horas} ${horas === 1 ? "hora" : "horas"}`} ${
      minutos === 0
        ? ""
        : `y ${minutos} ${minutos === 1 ? "minuto" : "minutos"}`
    }`;
    return mensaje.trim();
  }
}

// Ejemplo de uso:
console.log(fechaColoquial("05-11-2023-12-00")); // Dependiendo de la fecha actual mostrará "Falta ..." o "Pasó ..."

console.log(fechaColoquial("17-04-2025-00-00"));
