const fs = require("fs");

function verificarOrden(orden) {
  if (Object.keys(orden.articulos).length === 0) {
    console.warn(
      `Alerta: La orden con ID "${orden.id}" no contiene artículos. Se omitirá.`
    );
    return false;
  }
  if (!Number.isInteger(orden.id) || orden.id <= 0) {
    console.warn(
      `Alerta: El identificador "${orden.id}" no es un entero positivo. Se descartará esta orden.`
    );
    return false;
  }
  if (!Number.isInteger(orden.importe) || orden.importe <= 0) {
    console.warn(
      `Alerta: El importe de la orden con ID "${orden.id}" no es un número positivo. Se ignorará.`
    );
    return false;
  }
  for (const [articulo, cantidad] of Object.entries(orden.articulos)) {
    if (!Number.isInteger(cantidad) || cantidad <= 0) {
      console.warn(
        `Alerta: La cantidad del artículo "${articulo}" en la orden "${orden.id}" no es válida. Se descartará.`
      );
      return false;
    }
  }
  return true;
}

function obtenerProductoConMenorVentas(ordenes, minimo, maximo) {
  let articuloMenor = null;
  let cantidadMinima = Infinity;
  for (const orden of ordenes) {
    if (orden.importe >= minimo && orden.importe <= maximo) {
      for (const [articulo, cantidad] of Object.entries(orden.articulos)) {
        if (cantidad < cantidadMinima) {
          articuloMenor = articulo;
          cantidadMinima = cantidad;
        }
      }
    }
  }
  return { producto: articuloMenor, cantidad: cantidadMinima };
}

function procesarOrdenes(ordenes) {
  const ordenesValidas = [];
  for (const orden of ordenes) {
    if (verificarOrden(orden)) {
      ordenesValidas.push(orden);
    }
  }
  const productoMenor0a100 = obtenerProductoConMenorVentas(
    ordenesValidas,
    0,
    100
  );
  const productoMenor100a200 = obtenerProductoConMenorVentas(
    ordenesValidas,
    100,
    200
  );
  const productoMenor200oMas = obtenerProductoConMenorVentas(
    ordenesValidas,
    200,
    Infinity
  );
  console.log(
    `Producto con menor ventas en órdenes de $0-$100: ${productoMenor0a100.producto} (Cantidad: ${productoMenor0a100.cantidad})`
  );
  console.log(
    `Producto con menor ventas en órdenes de $100-$200: ${productoMenor100a200.producto} (Cantidad: ${productoMenor100a200.cantidad})`
  );
  console.log(
    `Producto con menor ventas en órdenes de $200 o más: ${productoMenor200oMas.producto} (Cantidad: ${productoMenor200oMas.cantidad})`
  );
}

fs.readFile("ordenes.json", "utf8", (err, data) => {
  if (err) {
    console.error("Error al leer el archivo JSON:", err);
    return;
  }
  try {
    const ordenes = JSON.parse(data);
    procesarOrdenes(ordenes);
  } catch (error) {
    console.error("Error al interpretar el archivo JSON:", error);
  }
});
