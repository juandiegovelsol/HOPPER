const fs = require("fs");
const path = require("path");
const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const calculateTotals = (csvFiles) => {
  let rateTotals = {};
  let totalPaid = 0;
  let totalTime = 0;
  const timeRegex = /^\d{2} \d{2} \d{2}$/;

  csvFiles.forEach((csvFile) => {
    const data = fs.readFileSync(csvFile, "utf8");
    let lines = data.trim().split("\n");
    if (lines.length === 0) return;

    if (lines[0].toLowerCase().includes("tiempo")) {
      lines.shift();
    }

    lines.forEach((line, index) => {
      let parts = line.split(",");
      if (parts.length !== 2) return;

      let timeStr = parts[0].trim();
      let rateStr = parts[1].trim();
      if (!timeRegex.test(timeStr)) return;

      let [hh, mm, ss] = timeStr.split(" ").map(Number);
      if (isNaN(hh) || isNaN(mm) || isNaN(ss)) return;

      let seconds = hh * 3600 + mm * 60 + ss;
      let hoursWorked = seconds / 3600;
      let rate = parseFloat(rateStr);
      if (isNaN(rate) || rate <= 0) return;

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
};

const menu = () => {
  rl.question(
    "Seleccione una opción:\n1. Total del último día\n2. Total de los últimos 7 días\n3. Total de todos los registros\n",
    (option) => {
      const files = fs
        .readdirSync(".")
        .filter((file) => /^data\d{2}-\d{2}-\d{4}\.csv$/.test(file))
        .sort((a, b) => {
          const dateA = new Date(
            a
              .match(/\d{2}-\d{2}-\d{4}/)[0]
              .split("-")
              .reverse()
              .join("-")
          );
          const dateB = new Date(
            b
              .match(/\d{2}-\d{2}-\d{4}/)[0]
              .split("-")
              .reverse()
              .join("-")
          );
          return dateB - dateA;
        });

      switch (option) {
        case "1":
          if (files.length > 0) {
            calculateTotals([files[0]]);
          } else {
            console.log("No se encontraron archivos CSV.");
          }
          break;
        case "2":
          if (files.length > 0) {
            calculateTotals(files.slice(0, 7));
          } else {
            console.log("No se encontraron archivos CSV.");
          }
          break;
        case "3":
          if (files.length > 0) {
            calculateTotals(files);
          } else {
            console.log("No se encontraron archivos CSV.");
          }
          break;
        default:
          console.log("Opción no válida.");
          break;
      }
      rl.close();
    }
  );
};

menu();
