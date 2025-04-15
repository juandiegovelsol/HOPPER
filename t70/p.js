const fs = require("fs");

function listCsvFiles() {
  return fs
    .readdirSync(".")
    .filter((file) => /^data\d{2}-\d{2}-\d{4}\.csv$/.test(file))
    .sort((a, b) => {
      const dateA = new Date(a.slice(4, 14).replace(/-/g, "/"));
      const dateB = new Date(b.slice(4, 14).replace(/-/g, "/"));
      return dateB - dateA;
    });
}

function calculateFromFiles(files) {
  let rateTotals = {};
  let totalPaid = 0;
  let totalTime = 0;

  files.forEach((csvFile) => {
    const data = fs.readFileSync(csvFile, "utf8");
    let lines = data.trim().split("\n");
    if (lines[0].toLowerCase().includes("tiempo")) lines.shift();
    const timeRegex = /^\d{2} \d{2} \d{2}$/;
    lines.forEach((line, index) => {
      let parts = line.split(",");
      let timeStr = parts[0].trim();
      let rateStr = parts[1].trim();
      if (!timeRegex.test(timeStr)) process.exit(1);
      let [hh, mm, ss] = timeStr.split(" ").map(Number);
      let seconds = hh * 3600 + mm * 60 + ss;
      let hoursWorked = seconds / 3600;
      let rate = parseFloat(rateStr);
      if (isNaN(rate) || rate <= 0) process.exit(1);
      if (!rateTotals[rate]) {
        rateTotals[rate] = { paid: 0, time: 0 };
      }
      let subtotal = rate * hoursWorked;
      rateTotals[rate].paid += subtotal;
      rateTotals[rate].time += hoursWorked;
      totalPaid += subtotal;
      totalTime += hoursWorked;
    });
  });

  for (let rate in rateTotals) {
    console.log(
      `Tasa: ${rate} USD, Tiempo trabajado: ${rateTotals[rate].time.toFixed(
        2
      )} horas, Subtotal pagado: $${rateTotals[rate].paid.toFixed(2)} USD`
    );
  }
  console.log(`Total pagado: $${totalPaid.toFixed(2)} USD`);
  console.log(`Total de tiempo trabajado: ${totalTime.toFixed(2)} horas`);
}

function main() {
  const files = listCsvFiles();
  console.log("Seleccione una opción:");
  console.log("1. Calcular el total del último día registrado");
  console.log("2. Calcular el total de los últimos 7 días");
  console.log("3. Calcular el total de todos los registros");
  const stdin = process.stdin;
  stdin.setEncoding("utf-8");
  stdin.on("data", (input) => {
    input = input.trim();
    if (input === "1") {
      calculateFromFiles(files.slice(0, 1));
    } else if (input === "2") {
      calculateFromFiles(files.slice(0, 7));
    } else if (input === "3") {
      calculateFromFiles(files);
    } else {
      console.log("Opción no válida.");
    }
    stdin.pause();
  });
}

main();
