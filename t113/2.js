const Decimal = require("decimal.js"); // Importar decimal.js

const fs = require("fs");

// Leer el archivo JSON y parsearlo
const trades = JSON.parse(fs.readFileSync("operaciones.json", "utf8"));

// Inicializar el total con un número decimal
let total = new Decimal(0);

// Iterar sobre cada operación
for (const { name, entryPrice, exitPrice, quantity, isLong } of trades) {
  // Utilizar números decimales para evitar problemas de precisión
  const entryPriceDec = new Decimal(entryPrice);
  const exitPriceDec = new Decimal(exitPrice);
  const quantityDec = new Decimal(quantity);

  const profitDec = isLong
    ? exitPriceDec.sub(entryPriceDec).mul(quantityDec)
    : entryPriceDec.sub(exitPriceDec).mul(quantityDec);

  // Mostrar el beneficio de la operación
  console.log(`${name}: ${profitDec}`);

  // Sumar el beneficio al total
  total = total.add(profitDec);
}

// Mostrar el total
console.log(`Total: ${total}`);
