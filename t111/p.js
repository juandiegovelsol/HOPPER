const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

const regexNumeroPositivo = /^\d*\.?\d+$/;

function validarFila(fila) {
  const {
    nombreActivo,
    precioCompra: precioCompraStr,
    precioVenta: precioVentaStr,
    cantidad: cantidadStr,
  } = fila;

  if (!nombreActivo || nombreActivo.trim() === "") {
    throw new Error(`El nombre del activo no puede estar vacío`);
  }

  if (
    !regexNumeroPositivo.test(precioCompraStr) ||
    !regexNumeroPositivo.test(precioVentaStr) ||
    !regexNumeroPositivo.test(cantidadStr)
  ) {
    throw new Error(
      `Los precios y la cantidad deben ser valores numéricos positivos. Valores recibidos: precioCompra=${precioCompraStr}, precioVenta=${precioVentaStr}, cantidad=${cantidadStr}`
    );
  }

  const precioCompra = parseFloat(precioCompraStr);
  const precioVenta = parseFloat(precioVentaStr);
  const cantidad = parseFloat(cantidadStr);

  if (precioCompra <= 0 || precioVenta <= 0 || cantidad <= 0) {
    throw new Error(`Los precios y la cantidad deben ser mayores que cero`);
  }

  return {
    nombreActivo,
    precioCompra,
    precioVenta,
    cantidad,
  };
}

function calcularGananciasPerdidas(transacciones) {
  let totalGanancias = 0;

  transacciones.forEach((transaccion) => {
    const { precioCompra, precioVenta, cantidad } = transaccion;
    const gananciaPorUnidad = precioVenta - precioCompra;
    const gananciaTotal = gananciaPorUnidad * cantidad;
    totalGanancias += gananciaTotal;
  });

  return totalGanancias;
}

function procesarArchivoCSV(archivoCSV, callback) {
  const parser = fs.createReadStream(archivoCSV).pipe(parse({ columns: true }));
  const transacciones = [];

  parser.on("data", (fila) => {
    try {
      const transaccionValida = validarFila(fila);
      transacciones.push(transaccionValida);
    } catch (error) {
      console.error(
        `Error al procesar la fila: ${JSON.stringify(fila)} - ${error.message}`
      );
    }
  });

  parser.on("end", () => {
    const totalGanancias = calcularGananciasPerdidas(transacciones);
    console.log(`Total de ganancias: €${totalGanancias.toFixed(2)}`);
    callback();
  });

  parser.on("error", (error) => {
    console.error(`Error al leer el archivo CSV: ${error.message}`);
    callback();
  });
}

const archivoCSV = path.join(__dirname, "transacciones.csv");

procesarArchivoCSV(archivoCSV, () => {
  console.log("Procesamiento completo.");
});

module.exports = { procesarArchivoCSV };
