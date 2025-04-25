const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

const inputFilePath = path.join(__dirname, "partidas.csv");
const outputFilePath = path.join(__dirname, "resultado_tournament.json");

parse = parse({ columns: true }, (err, data) => {
  if (err) {
    console.error("Error al parsear el CSV:", err);
    return;
  }

  const equipos = {};

  data.forEach((partida) => {
    const { equipo1, equipo2, puntuacion1, puntuacion2, duracion } = partida;

    // Validación de datos
    if (
      !equipo1 ||
      !equipo2 ||
      isNaN(puntuacion1) ||
      isNaN(puntuacion2) ||
      isNaN(duracion) ||
      puntuacion1 <= 0 ||
      puntuacion2 <= 0 ||
      duracion <= 0
    ) {
      return;
    }

    // Inicializar los equipos si no existen
    if (!equipos[equipo1]) {
      equipos[equipo1] = {
        partidasJugadas: 0,
        partidasGanadas: 0,
        totalPuntos: 0,
      };
    }
    if (!equipos[equipo2]) {
      equipos[equipo2] = {
        partidasJugadas: 0,
        partidasGanadas: 0,
        totalPuntos: 0,
      };
    }

    // Registrar partida jugada
    equipos[equipo1].partidasJugadas++;
    equipos[equipo2].partidasJugadas++;

    // Actualizar puntos
    equipos[equipo1].totalPuntos += puntuacion1;
    equipos[equipo2].totalPuntos += puntuacion2;

    // Determinar la partida ganada
    if (puntuacion1 > puntuacion2) {
      equipos[equipo1].partidasGanadas++;
    } else if (puntuacion2 > puntuacion1) {
      equipos[equipo2].partidasGanadas++;
    }
  });

  // Calcular el promedio de puntos por partida
  for (const equipo in equipos) {
    equipos[equipo].promedioPuntos = (
      equipos[equipo].totalPuntos / equipos[equipo].partidasJugadas
    ).toFixed(2);
    delete equipos[equipo].totalPuntos; // Eliminar totalPuntos para dejar solo las estadísticas finales
  }

  // Convertir el objeto de equipos a un array y ordenarlo
  const clasificacion = Object.keys(equipos)
    .map((equipo) => ({
      equipo,
      ...equipos[equipo],
    }))
    .sort((a, b) => b.partidasGanadas - a.partidasGanadas);

  // Escribir el JSON en el archivo de salida
  fs.writeFileSync(outputFilePath, JSON.stringify(clasificacion, null, 2));

  console.log("Clasificación generada en:", outputFilePath);
});

fs.createReadStream(inputFilePath).pipe(parse);
