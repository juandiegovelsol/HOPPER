const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

// Función para validar y transformar datos CSV a un objeto de partidos
const procesarPartidos = (err, data) => {
  /* if (err) {
    throw err;
  } */

  // Mapa para contar partidos ganados por jugador
  const partidosGanados = new Map();

  // Procesar cada fila del CSV
  console.log(data);
  data.forEach((row, index) => {
    if (index === 0) return; // Omitir encabezado

    const [jugador1, jugador2, setsJugador1, setsJugador2] = row;

    // Validar número de sets
    if (
      isNaN(setsJugador1) ||
      isNaN(setsJugador2) ||
      setsJugador1 < 0 ||
      setsJugador2 < 0
    ) {
      console.warn(
        `Advertencia: Fila ${index + 1} tiene un formato de sets inválido.`
      );
      return;
    }

    // Determinar el ganador del partido
    let ganador;
    if (setsJugador1 > setsJugador2) {
      ganador = jugador1;
    } else if (setsJugador2 > setsJugador1) {
      ganador = jugador2;
    } else {
      console.warn(
        `Advertencia: Fila ${index + 1} tiene un marcador inválido.`
      );
      return;
    }

    // Actualizar conteo de partidos ganados
    partidosGanados.set(ganador, (partidosGanados.get(ganador) || 0) + 1);
  });

  // Convertir el mapa a una lista y ordenar por partidos ganados
  const jugadoresOrdenados = Array.from(partidosGanados)
    .sort((a, b) => b[1] - a[1]) // Ordenar descendente por partidos ganados
    .map(([jugador, partidos]) => ({ jugador, partidos }));

  // Imprimir resultados
  console.log("\nResultados del Torneo:");
  jugadoresOrdenados.forEach(({ jugador, partidos }, index) => {
    console.log(`${index + 1}. ${jugador}: ${partidos} partidos ganados`);
  });
};

// Ruta al archivo CSV (asumiendo que está en el mismo directorio que este script)
const archivoPartidos = path.join(__dirname, "partidos.csv");

// Leer y procesar el archivo CSV
fs.createReadStream(archivoPartidos)
  .pipe(parse({ columns: true })) // Automáticamente convierte la primera fila en encabezados
  .on("data", procesarPartidos);
