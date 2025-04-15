const fs = require("fs");
const csvFile = process.argv[2] || "data.csv";

fs.readFile(csvFile, "utf8", (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  let lines = data.trim().split("\n");
  if (lines.length === 0) {
    console.error("No hay registros en el archivo CSV");
    process.exit(1);
  }

  if (lines[0].toLowerCase().includes("tiempo")) {
    lines.shift();
  }

  if (lines.length === 0) {
    console.error("No hay registros en el archivo CSV");
    process.exit(1);
  }

  let speedTotals = {};
  let totalDistance = 0;
  let totalTime = 0;
  const timeRegex = /^\d{2} \d{2} \d{2}$/;

  lines.forEach((line, index) => {
    let parts = line.split(",");
    if (parts.length !== 2) {
      console.error(`Error en la línea ${index + 1}: formato incorrecto`);
      process.exit(1);
    }

    let timeStr = parts[0].trim();
    let speedStr = parts[1].trim();

    if (!timeRegex.test(timeStr)) {
      console.error(
        `Error en la línea ${
          index + 1
        }: el tiempo debe tener el formato numérico HH MM SS`
      );
      process.exit(1);
    }

    let [hh, mm, ss] = timeStr.split(" ").map(Number);
    if (isNaN(hh) || isNaN(mm) || isNaN(ss)) {
      console.error(
        `Error en la línea ${
          index + 1
        }: el tiempo contiene valores no numéricos`
      );
      process.exit(1);
    }

    let seconds = hh * 3600 + mm * 60 + ss;
    let hours = seconds / 3600;

    let speed = parseFloat(speedStr);
    if (isNaN(speed) || speed <= 0) {
      console.error(
        `Error en la línea ${
          index + 1
        }: la velocidad debe ser un número positivo`
      );
      process.exit(1);
    }

    let distance = speed * hours;

    if (!speedTotals[speed]) {
      speedTotals[speed] = { time: 0, distance: 0 };
    }

    speedTotals[speed].time += hours;
    speedTotals[speed].distance += distance;
    totalDistance += distance;
    totalTime += hours;
  });

  for (let speed in speedTotals) {
    console.log(
      `Velocidad: ${speed} km/h, Tiempo total: ${speedTotals[
        speed
      ].time.toFixed(2)} horas, Distancia recorrida: ${speedTotals[
        speed
      ].distance.toFixed(2)} km`
    );
  }
  console.log(`Distancia total recorrida: ${totalDistance.toFixed(2)} km`);
  console.log(`Tiempo total: ${totalTime.toFixed(2)} horas`);
});
