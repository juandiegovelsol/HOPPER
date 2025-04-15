const fs = require("fs");

function leerArchivoJson(rutaArchivo) {
  try {
    const datos = fs.readFileSync(rutaArchivo, "utf8");
    return JSON.parse(datos);
  } catch (error) {
    console.error("Error al leer el archivo JSON:", error);
    return null;
  }
}

function buscarCortes(datos) {
  const alertas = [];

  for (const timestamp in datos) {
    const mediciones = datos[timestamp];

    for (const sensorId in mediciones) {
      const medicionActual = mediciones[sensorId];

      if (medicionActual < 0.5 * (ultimaMedicion[sensorId] || medicionActual)) {
        alertas.push({
          timestamp: timestamp,
          sensorId: sensorId,
          medicion: medicionActual,
        });
      }

      if (ultimaMedicion) {
        ultimaMedicion[sensorId] = medicionActual;
      } else {
        ultimaMedicion = { [sensorId]: medicionActual };
      }
    }
  }

  return alertas;
}

function generarAlertas(alertas) {
  alertas.forEach((alerta) => {
    console.log(
      `Alerta: Posible corte en el sensor ${alerta.sensorId} a las ${alerta.timestamp}. Medición: ${alerta.medicion} kWh`
    );
  });
}

const rutaArchivoJson = "datos_potencia.json";
const datosJson = leerArchivoJson(rutaArchivoJson);

if (datosJson) {
  const alertas = buscarCortes(datosJson);
  generarAlertas(alertas);
}
