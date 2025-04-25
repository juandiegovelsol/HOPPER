const fs = require("fs");

function calculateScore(player) {
  const weights = {
    age: 0.3,
    value: 0.3,
    goals: 0.2,
    assists: 0.1,
    minutes_played: 0.1,
  };

  const normalizedAge = (35 - player.edad) / (35 - 18);

  const maxValue = 100;
  const maxGoals = 1000;
  const maxAssists = 500;
  const maxMinutes = 5000;

  const normalizedValue = player.valor / maxValue;
  const normalizedGoals = player.goles / maxGoals;
  const normalizedAssists = player.asistencias / maxAssists;
  const normalizedMinutes = player.minutos_jugados / maxMinutes;

  const score =
    weights.age * normalizedAge +
    weights.value * normalizedValue +
    weights.goals * normalizedGoals +
    weights.assists * normalizedAssists +
    weights.minutes_played * normalizedMinutes;

  return score;
}

function findMostValuablePlayer(filePath) {
  const data = fs.readFileSync(filePath, "utf8");
  const players = JSON.parse(data);

  if (!players || !players.length) {
    throw new Error("No player data found");
  }

  let mostValuablePlayer = null;
  let maxScore = -1;

  for (const player of players) {
    const score = calculateScore(player);

    if (score > maxScore) {
      maxScore = score.toFixed(2);
      mostValuablePlayer = player;
    }
  }

  return {
    player: mostValuablePlayer,
    score: maxScore,
  };
}

try {
  console.log(findMostValuablePlayer("archivo1.json"));
  console.log(findMostValuablePlayer("archivo2.json"));
  console.log(findMostValuablePlayer("archivo3.json"));
} catch (error) {
  console.log(error);
}
