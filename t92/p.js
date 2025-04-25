const fs = require("fs");
const csv = require("csv-parser");

function processTournamentData(filePath) {
  const teams = {};

  fs.createReadStream(filePath)
    .pipe(csv())
    .on("data", (row) => {
      const teamA = row.equipoA;
      const teamB = row.equipoB;
      const scoreA = +row.puntuacionA;
      const scoreB = +row.puntuacionB;
      const duration = +row.duracion;

      if (
        teamA &&
        teamB &&
        scoreA > 0 &&
        scoreB > 0 &&
        duration > 0 &&
        Number.isInteger(scoreA) &&
        Number.isInteger(scoreB)
      ) {
        if (!teams[teamA]) {
          teams[teamA] = {
            playedMatches: 0,
            wonMatches: 0,
            totalPoints: 0,
          };
        }
        if (!teams[teamB]) {
          teams[teamB] = {
            playedMatches: 0,
            wonMatches: 0,
            totalPoints: 0,
          };
        }

        teams[teamA].playedMatches++;
        teams[teamB].playedMatches++;
        teams[teamA].totalPoints += scoreA;
        teams[teamB].totalPoints += scoreB;

        if (scoreA > scoreB) {
          teams[teamA].wonMatches++;
        } else if (scoreB > scoreA) {
          teams[teamB].wonMatches++;
        }
      }
    })
    .on("end", () => {
      const resultado = Object.keys(teams).map((team) => {
        const data = teams[team];
        return {
          equipo: team,
          partidasJugadas: data.playedMatches,
          partidasGanadas: data.wonMatches,
          promedioPuntos: (data.totalPoints / data.playedMatches).toFixed(2),
        };
      });

      resultado.sort((a, b) => b.partidasGanadas - a.partidasGanadas);
      console.log(resultado);
    });
}

processTournamentData("torneo.csv");
