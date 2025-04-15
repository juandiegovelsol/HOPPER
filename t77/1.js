const fs = require("fs");
const readline = require("readline");

function validarTiempo(tiempo) {
  const partes = tiempo.split(":");
  if (partes.length !== 3) return false;
  const [horas, minutos, segundos] = partes.map(Number);
  if (
    !Number.isInteger(horas) ||
    !Number.isInteger(minutos) ||
    !Number.isInteger(segundos)
  )
    return false;
  return (
    horas >= 0 &&
    horas < 24 &&
    minutos >= 0 &&
    minutos < 60 &&
    segundos >= 0 &&
    segundos < 60
  );
}

function validarTasa(tasa) {
  return parseFloat(tasa) > 0;
}

function calcularPenalidad(tiempo, tasa) {
  const [horas, minutos, segundos] = tiempo.split(":").map(Number);
  const totalHoras = horas + minutos / 60 + segundos / 3600;
  return parseFloat(tasa) * totalHoras;
}

async function procesarCSV(rutaArchivo) {
  const archivoStream = fs.createReadStream(rutaArchivo);
  const lineas = readline.createInterface({ input: archivoStream });
  const penalidades = {};
  let totalPenalidades = 0;

  for await (const linea of lineas) {
    const [id, tiempo, tasa] = linea.split(",");
    if (penalidades.hasOwnProperty(id)) continue;
    if (!validarTiempo(tiempo) || !validarTasa(tasa)) continue;
    const penalidad = calcularPenalidad(tiempo, tasa);
    penalidades[id] = penalidad;
    totalPenalidades += penalidad;
  }

  return { penalidades, totalPenalidades };
}

procesarCSV("huéspedes.csv").then((resultados) => {
  console.log("Penalidades por huésped:", resultados.penalidades);
  console.log("Total de penalidades del día:", resultados.totalPenalidades);
});
