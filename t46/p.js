const fs = require("fs");

function isValidDate(dateString) {
  const regex = /^(\d{2})\/(\d{2})\/(\d{4})$/;
  if (!regex.test(dateString)) return false;
  const [day, month, year] = dateString.split("/").map(Number);
  const date = new Date(year, month - 1, day);
  return (
    date.getDate() === day &&
    date.getMonth() === month - 1 &&
    date.getFullYear() === year
  );
}

function isValidCompras(compras) {
  return Array.isArray(compras);
}

function isValidActivoId(id) {
  return /^[A-Za-z0-9]{4}$/.test(id);
}

function isValidPrecio(precio) {
  return typeof precio === "number" && precio > 0;
}

function calculateAverages(data) {
  const dailyAverages = {};
  const overallData = {};

  data.forEach((entry) => {
    if (!isValidDate(entry.fecha) || !isValidCompras(entry.compras)) return;

    const day = entry.fecha;
    dailyAverages[day] = dailyAverages[day] || {};

    entry.compras.forEach((compra) => {
      if (!isValidActivoId(compra.id) || !isValidPrecio(compra.precio)) return;

      dailyAverages[day][compra.id] = dailyAverages[day][compra.id] || {
        total: 0,
        count: 0,
      };
      dailyAverages[day][compra.id].total += compra.precio;
      dailyAverages[day][compra.id].count++;

      overallData[compra.id] = overallData[compra.id] || { total: 0, count: 0 };
      overallData[compra.id].total += compra.precio;
      overallData[compra.id].count++;
    });
  });

  console.log("Promedio Diario:");
  for (const day in dailyAverages) {
    console.log(`Fecha: ${day}`);
    for (const id in dailyAverages[day]) {
      const average =
        dailyAverages[day][id].total / dailyAverages[day][id].count;
      console.log(`Activo ID: ${id}, Promedio: ${average.toFixed(2)}`);
    }
  }

  console.log("\nPromedio Total:");
  for (const id in overallData) {
    const average = overallData[id].total / overallData[id].count;
    console.log(`Activo ID: ${id}, Promedio: ${average.toFixed(2)}`);
  }
}

fs.readFile("compras.json", "utf8", (err, data) => {
  if (err) throw err;
  const jsonData = JSON.parse(data);
  calculateAverages(jsonData);
});
