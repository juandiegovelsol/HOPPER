const fs = require("fs");
const path = require("path");

// Función para validar el formato de la hora
function validarHora(hora) {
  const partes = hora.split(":");
  if (partes.length !== 3) return false;
  const [horas, minutos, segundos] = partes.map(Number);
  return (
    horas >= 0 &&
    horas < 24 &&
    minutos >= 0 &&
    minutos < 60 &&
    segundos >= 0 &&
    segundos < 60
  );
}

// Función para calcular el tiempo en segundos
function calcularTiempoEnSegundos(hora) {
  const [horas, minutos, segundos] = hora.split(":").map(Number);
  return horas * 3600 + minutos * 60 + segundos;
}

// Función para calcular el costo del tiempo extra
function calcularCostoTiempoExtra(tiempoExtraSegundos, tasa) {
  const costoPorSegundo = tasa / 3600; // Tasa por hora convertida a costo por segundo
  return tiempoExtraSegundos * costoPorSegundo;
}

// Función para procesar el archivo CSV y calcular las penalidades
function procesarArchivoCSV(archivoCSV) {
  return new Promise((resolver, rechazar) => {
    fs.readFile(archivoCSV, "utf-8", (err, data) => {
      if (err) return rechazar(err);

      const lineas = data.trim().split("\n");
      if (lineas.length < 2) return resolver({ totalPenalidades: 0 });

      const encabezados = lineas[0].split(",");
      console.log(
        encabezados,
        !encabezados.includes("id"),
        !encabezados.includes("tiempo"),
        !encabezados.includes("tasa")
      );
      if (
        !encabezados.includes("id") ||
        !encabezados.includes("tiempo") ||
        !encabezados.includes("tasa\r")
      ) {
        return resolver({
          totalPenalidades: 0,
          errores: "Formato de encabezados incorrecto",
        });
      }

      const datos = lineas.slice(1).map((linea) => linea.split(","));
      const resultados = [];
      let totalPenalidades = 0;
      let hayErrores = false;

      for (const dato of datos) {
        if (dato.length !== 3) {
          hayErrores = true;
          continue;
        }

        const [id, tiempo, tasaStr] = dato;
        if (
          !id ||
          typeof id !== "string" ||
          !validarHora(tiempo) ||
          isNaN(tasaStr)
        ) {
          hayErrores = true;
          continue;
        }

        const tasa = parseFloat(tasaStr);
        if (tasa <= 0) {
          hayErrores = true;
          continue;
        }

        const tiempoExtraSegundos = calcularTiempoEnSegundos(tiempo);
        const costoTiempoExtra = calcularCostoTiempoExtra(
          tiempoExtraSegundos,
          tasa
        );
        totalPenalidades += costoTiempoExtra;

        resultados.push({
          id,
          tiempoExtraSegundos,
          costoTiempoExtra,
        });
      }

      resolver({
        resultados,
        totalPenalidades,
        errores: hayErrores ? "Errores en el procesamiento de datos" : null,
      });
    });
  });
}

// Ejemplo de uso
const archivoCSV = path.join(__dirname, "habitaciones.csv");

procesarArchivoCSV(archivoCSV)
  .then((resultado) => {
    console.log("Resultado del procesamiento:", resultado);
  })
  .catch((error) => {
    console.error("Error al procesar el archivo CSV:", error);
  });

// Nota: Asegúrate de que el archivo `habitaciones.csv` exista en el mismo directorio que el script y que tenga el formato adecuado.
