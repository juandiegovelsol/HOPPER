const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

// Función para parsear el archivo CSV y devolver una lista de partidos
const obtenerPartidosDesdeCSV = (archivoCsv) => {
  return new Promise((resolver, rechazar) => {
    const registros = [];
    parse(
      archivoCsv,
      { columns: true, skip_empty_lines: true },
      (err, data) => {
        if (err) rechazar(err);
        data.forEach((fila) => {
          const { jugador1, jugador2, setsJugador1, setsJugador2 } = fila;
          registros.push({
            jugador1: jugador1.trim(),
            jugador2: jugador2.trim(),
            setsJugador1: parseInt(setsJugador1, 10),
            setsJugador2: parseInt(setsJugador2, 10),
          });
        });
        resolver(registros);
      }
    );
  });
};

// Función para determinar el ganador de un partido
const determinarGanador = (partido) => {
  if (partido.setsJugador1 > partido.setsJugador2) {
    return partido.jugador1;
  } else if (partido.setsJugador2 > partido.setsJugador1) {
    return partido.jugador2;
  } else {
    return null; // Igualdad
  }
};

// Función para calcular las estadísticas de los jugadores
const calcularEstadisticas = (partidos) => {
  const estadisticas = {};

  partidos.forEach((partido) => {
    const ganador = determinarGanador(partido);
    if (ganador) {
      estadisticas[ganador] = (estadisticas[ganador] || 0) + 1;
    }
  });

  return estadisticas;
};

// Función para ordenar los jugadores por el número de partidos ganados
const obtenerRankingJugadores = (estadisticas) => {
  return Object.entries(estadisticas)
    .sort((a, b) => b[1] - a[1]) // Ordena de forma descendente
    .map(([jugador, partidosGanados]) => ({ jugador, partidosGanados }));
};

// Función principal para procesar el archivo CSV y devolver el ranking
const procesarArchivoCsv = async (rutaArchivoCsv) => {
  try {
    const partidos = await obtenerPartidosDesdeCSV(rutaArchivoCsv);
    const estadisticas = calcularEstadisticas(partidos);
    const rankingJugadores = obtenerRankingJugadores(estadisticas);

    // Imprime el ranking de jugadores
    console.log("Ranking de jugadores (jugador: partidos ganados):");
    rankingJugadores.forEach(({ jugador, partidosGanados }) => {
      console.log(`${jugador}: ${partidosGanados}`);
    });

    return rankingJugadores;
  } catch (error) {
    console.error("Error al procesar el archivo CSV:", error);
    throw error;
  }
};

// Especifica la ruta al archivo CSV que contiene los datos de los partidos
const rutaArchivoCsv = path.join(__dirname, "partidos.csv");

// Ejecuta el procesamiento del archivo CSV
(async () => {
  try {
    await procesarArchivoCsv(rutaArchivoCsv);
  } catch (error) {
    console.error("Se produjo un error durante el procesamiento:", error);
  }
})();
