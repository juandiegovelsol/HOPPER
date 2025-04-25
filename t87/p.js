const fs = require("fs");

function readMatchesFromFile(filePath) {
  const data = fs.readFileSync(filePath);
  return JSON.parse(data);
}

function calculateLeagueWinner(matches) {
  const teams = {};

  matches.forEach((match, index) => {
    const { team1, goals1, team2, goals2 } = match;

    if (
      typeof team1 !== "string" ||
      !team1 ||
      typeof team2 !== "string" ||
      !team2
    ) {
      console.error(
        `Error en partido #${index + 1}: Nombres de equipos inválidos`
      );
      return;
    }

    if (
      !Number.isInteger(goals1) ||
      goals1 < 0 ||
      !Number.isInteger(goals2) ||
      goals2 < 0
    ) {
      console.error(
        `Error en partido #${
          index + 1
        }: Goles inválidos para ${team1} vs ${team2}`
      );
      return;
    }

    if (!teams[team1])
      teams[team1] = {
        won: 0,
        goalsFor: 0,
        goalsAgainst: 0,
        drawn: 0,
        lost: 0,
        points: 0,
      };
    if (!teams[team2])
      teams[team2] = {
        won: 0,
        goalsFor: 0,
        goalsAgainst: 0,
        drawn: 0,
        lost: 0,
        points: 0,
      };

    teams[team1].goalsFor += goals1;
    teams[team1].goalsAgainst += goals2;
    teams[team2].goalsFor += goals2;
    teams[team2].goalsAgainst += goals1;

    if (goals1 > goals2) {
      teams[team1].won += 1;
      teams[team1].points += 3;
      teams[team2].lost += 1;
    } else if (goals1 < goals2) {
      teams[team2].won += 1;
      teams[team2].points += 3;
      teams[team1].lost += 1;
    } else {
      teams[team1].drawn += 1;
      teams[team2].drawn += 1;
      teams[team1].points += 1;
      teams[team2].points += 1;
    }
  });

  if (Object.keys(teams).length === 0) {
    console.log("No hay datos válidos para calcular un ganador");
    return;
  }

  const winner = Object.entries(teams).reduce((prev, curr) =>
    curr[1].points > prev[1].points ? curr : prev
  );

  console.log(`Ganador: ${winner[0]}`);
  console.log(`Partidos ganados: ${winner[1].won}`);
  console.log(`Goles a favor: ${winner[1].goalsFor}`);
  console.log(`Goles en contra: ${winner[1].goalsAgainst}`);
  console.log(`Partidos empatados: ${winner[1].drawn}`);
  console.log(`Partidos perdidos: ${winner[1].lost}`);
}

const matches = readMatchesFromFile("partidos.json");
calculateLeagueWinner(matches);
