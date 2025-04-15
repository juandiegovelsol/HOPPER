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
  let rateTotals = {};
  let totalPaid = 0;
  let totalTime = 0;
  const timeRegex = /^\d{2} \d{2} \d{2}$/;
  lines.forEach((line, index) => {
    let parts = line.split(",");
    if (parts.length !== 2) {
      console.error(`Error en la línea ${index + 1}: formato incorrecto`);
      process.exit(1);
    }
    let timeStr = parts[0].trim();
    let rateStr = parts[1].trim();
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
    let hoursWorked = seconds / 3600;
    let rate = parseFloat(rateStr);
    if (isNaN(rate) || rate <= 0) {
      console.error(
        `Error en la línea ${index + 1}: la tasa debe ser un número positivo`
      );
      process.exit(1);
    }
    if (!rateTotals[rate]) {
      rateTotals[rate] = { paid: 0, time: 0 };
    }
    let subtotal = rate * hoursWorked;
    rateTotals[rate].paid += subtotal;
    rateTotals[rate].time += hoursWorked;
    totalPaid += subtotal;
    totalTime += hoursWorked;
  });
  for (let rate in rateTotals) {
    console.log(
      `Tasa: ${rate} CLP, Tiempo trabajado: ${rateTotals[rate].time.toFixed(
        2
      )} horas, Subtotal pagado: ${rateTotals[rate].paid.toFixed(2)} CLP`
    );
  }
  console.log(`Total pagado: ${totalPaid.toFixed(2)} CLP`);
  console.log(`Total de tiempo trabajado: ${totalTime.toFixed(2)} horas`);
});
