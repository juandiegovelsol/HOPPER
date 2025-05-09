const Decimal = require("decimal.js");
const fs = require("fs");
function validarOperacion(operacion) {
  if (
    !operacion ||
    !("name" in operacion) ||
    !("entryPrice" in operacion) ||
    !("exitPrice" in operacion) ||
    !("quantity" in operacion) ||
    !("isLong" in operacion)
  ) {
    return false;
  }

  try {
    new Decimal(operacion.entryPrice);
    new Decimal(operacion.exitPrice);
    new Decimal(operacion.quantity);
  } catch (error) {
    return false;
  }

  if (new Decimal(operacion.quantity).lessThanOrEqualTo(0)) {
    return false;
  }

  if (typeof operacion.isLong !== "boolean") {
    return false;
  }

  return true;
}

try {
  let trades;
  try {
    const datos = fs.readFileSync("operaciones.json", "utf8");
    trades = JSON.parse(datos);
    if (!Array.isArray(trades)) {
      throw new Error("El archivo no contiene un arreglo de operaciones");
    }
  } catch (error) {
    console.error(`Error al leer o parsear el archivo: ${error.message}`);
    process.exit(1);
  }

  let total = new Decimal(0);
  let operacionesValidas = 0;
  let operacionesIgnoradas = 0;
  for (let i = 0; i < trades.length; i++) {
    const operacion = trades[i];

    if (!validarOperacion(operacion)) {
      console.log(
        `Ignorando operación #${i + 1} con datos incorrectos: ${JSON.stringify(
          operacion
        )}`
      );
      operacionesIgnoradas++;
      continue;
    }

    const { name, entryPrice, exitPrice, quantity, isLong } = operacion;

    try {
      const entryPriceDec = new Decimal(entryPrice);
      const exitPriceDec = new Decimal(exitPrice);
      const quantityDec = new Decimal(quantity);

      const profitDec = isLong
        ? exitPriceDec.sub(entryPriceDec).mul(quantityDec)
        : entryPriceDec.sub(exitPriceDec).mul(quantityDec);
      console.log(`${name}: ${profitDec.toFixed(2)}`);

      total = total.add(profitDec);
      operacionesValidas++;
    } catch (error) {
      console.log(`Error al procesar la operación "${name}": ${error.message}`);
      operacionesIgnoradas++;
    }
  }

  console.log(`\nResumen:`);
  console.log(`- Operaciones procesadas: ${operacionesValidas}`);
  console.log(`- Operaciones ignoradas: ${operacionesIgnoradas}`);
  console.log(`- Total: ${total.toFixed(2)}`);
} catch (error) {
  console.error(`Error inesperado: ${error.message}`);
  process.exit(1);
}

module.exports = validarOperacion;
