const fs = require("fs");
const csv = require("csv-parser");

function processTournamentData(filePath) {
  const teams = {};

  fs.createReadStream(filePath)
    .pipe(csv())
    .on("data", (row) => {
      const teamA = row.equipoA;
      const teamB = row.equipoB;
      const scoreA = parseInt(row.puntuacionA);
      const scoreB = parseInt(row.puntuacionB);
      const duration = parseInt(row.duracion);

      if (teamA && teamB && scoreA > 0 && scoreB > 0 && duration > 0) {
        if (!teams[teamA]) {
          teams[teamA] = {
            partidasJugadas: 0,
            partidasGanadas: 0,
            puntosTotales: 0,
          };
        }
        if (!teams[teamB]) {
          teams[teamB] = {
            partidasJugadas: 0,
            partidasGanadas: 0,
            puntosTotales: 0,
          };
        }

        teams[teamA].partidasJugadas++;
        teams[teamB].partidasJugadas++;
        teams[teamA].puntosTotales += scoreA;
        teams[teamB].puntosTotales += scoreB;

        if (scoreA > scoreB) {
          teams[teamA].partidasGanadas++;
        } else if (scoreB > scoreA) {
          teams[teamB].partidasGanadas++;
        }
      }
    })
    .on("end", () => {
      const resultado = Object.keys(teams).map((team) => {
        const data = teams[team];
        return {
          equipo: team,
          partidasJugadas: data.partidasJugadas,
          partidasGanadas: data.partidasGanadas,
          promedioPuntos: (data.puntosTotales / data.partidasJugadas).toFixed(
            2
          ),
        };
      });

      resultado.sort((a, b) => b.partidasGanadas - a.partidasGanadas);
      console.log(resultado);
    });
}

processTournamentData("tournament.csv");
