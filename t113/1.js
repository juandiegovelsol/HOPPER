const fs = require("fs");

const trades = JSON.parse(fs.readFileSync("operaciones.json", "utf8"));

let total = 0;
const factor = 100; // Factor para manejar dos decimales

for (const { name, entryPrice, exitPrice, quantity, isLong } of trades) {
  // Multiplicamos por el factor para evitar imprecisiones decimales
  const entryPriceInt = entryPrice * factor;
  const exitPriceInt = exitPrice * factor;
  const quantityInt = quantity * factor;

  // Realizamos el cálculo utilizando enteros
  const profitInt =
    (isLong ? exitPriceInt - entryPriceInt : entryPriceInt - exitPriceInt) *
    quantityInt;

  // Convertimos de nuevo el resultado a su forma original dividiendo por el factor
  const profit = profitInt / (factor * factor);

  console.log(`${name}: ${profit.toFixed(2)}`); // Usar toFixed solo para mostrar, no para calcular
  total += profit;
}

console.log(`Total: ${total.toFixed(2)}`);
