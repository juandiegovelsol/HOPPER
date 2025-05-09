const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse");

// Expresiones regulares para validar los datos
const regexPrecio = /^\d+(?:\.\d{2})?$/;
const regexCantidad = /^\d+$/;

// Función para validar cada fila del CSV
function validarFila(fila) {
  const [nombreActivo, precioCompraStr, precioVentaStr, cantidadStr] = fila;

  if (!nombreActivo) {
    throw new Error(`El nombre del activo no puede estar vacío`);
  }

  if (!regexPrecio.test(precioCompraStr) || !regexPrecio.test(precioVentaStr)) {
    throw new Error(
      `Los precios deben ser numéricos con dos decimales, valor: ${precioCompraStr} o ${precioVentaStr}`
    );
  }

  if (!regexCantidad.test(cantidadStr)) {
    throw new Error(
      `La cantidad debe ser un número entero, valor: ${cantidadStr}`
    );
  }

  const precioCompra = parseFloat(precioCompraStr);
  const precioVenta = parseFloat(precioVentaStr);
  const cantidad = parseInt(cantidadStr, 10);

  if (precioCompra <= 0 || precioVenta <= 0 || cantidad <= 0) {
    throw new Error(`Los precios y la cantidad deben ser mayores que cero`);
  }

  return {
    nombreActivo,
    precioCompra: parseFloat(precioCompraStr),
    precioVenta: parseFloat(precioVentaStr),
    cantidad: parseInt(cantidadStr, 10),
  };
}

// Función para calcular las ganancias o pérdidas totales
function calcularGananciasPerdidas(transacciones) {
  let totalGanancias = 0;

  transacciones.forEach((transaccion) => {
    const { nombreActivo, precioCompra, precioVenta, cantidad } = transaccion;
    const gananciaPorUnidad = precioVenta - precioCompra;
    const gananciaTotal = gananciaPorUnidad * cantidad;
    totalGanancias += gananciaTotal;
  });

  return totalGanancias;
}

// Función principal para procesar el archivo CSV
function procesarArchivoCSV(archivoCSV, callback) {
  const parser = fs.createReadStream(archivoCSV).pipe(parse({ columns: true }));
  let transacciones = [];

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
    console.log(`Total de ganancias: $${totalGanancias.toFixed(2)}`);
    callback();
  });

  parser.on("error", (error) => {
    console.error(`Error al leer el archivo CSV: ${error.message}`);
    callback();
  });
}

// Ejemplo de uso
const archivoCSV = path.join(__dirname, "transacciones.csv");

procesarArchivoCSV(archivoCSV, () => {
  console.log("Procesamiento completo.");
});
