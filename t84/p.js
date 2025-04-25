const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

const partidosGanados = new Map();
const archivoPartidos = path.join(__dirname, "partidos.csv");

const parser = parse({
  columns: true,
  skip_empty_lines: true,
});

parser.on("readable", () => {
  let record;
  while ((record = parser.read()) !== null) {
    const {
      jugador1,
      jugador2,
      setsJugador1: setsJugador1Str,
      setsJugador2: setsJugador2Str,
    } = record;

    const setsJugador1 = parseInt(setsJugador1Str, 10);
    const setsJugador2 = parseInt(setsJugador2Str, 10);

    if (
      isNaN(setsJugador1) ||
      isNaN(setsJugador2) ||
      setsJugador1 < 0 ||
      setsJugador2 < 0
    ) {
      console.warn(
        `Advertencia: Fila ${index + 1} tiene un formato de sets inválido.`
      );
      continue;
    }

    let ganador = null;
    if (setsJugador1 === 3 && setsJugador1 > setsJugador2) {
      ganador = jugador1;
    } else if (setsJugador2 === 3 && setsJugador2 > setsJugador1) {
      ganador = jugador2;
    } else {
      console.warn(
        `Advertencia: Fila ${index + 1} tiene un marcador inválido.`
      );
      continue;
    }

    if (ganador) {
      partidosGanados.set(ganador, (partidosGanados.get(ganador) || 0) + 1);
    }
  }
});

parser.on("end", () => {
  const jugadoresOrdenados = Array.from(partidosGanados)
    .sort((a, b) => b[1] - a[1])
    .map(([jugador, partidos]) => ({ jugador, partidos }));

  console.log("Resultados del Torneo:");
  jugadoresOrdenados.forEach(({ jugador, partidos }, index) => {
    console.log(`${index + 1}. ${jugador}: ${partidos} partidos ganados`);
  });
});

parser.on("error", (err) => {
  console.error("Error procesando el CSV:", err.message);
});

fs.createReadStream(archivoPartidos).pipe(parser);
