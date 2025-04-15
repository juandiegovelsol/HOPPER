const fs = require("fs");

// Función para validar los datos de una compra
function validarCompra(compra) {
  if (!Number.isInteger(compra.id) || compra.id <= 0) {
    console.warn(
      `Advertencia: La ID de compra "${compra.id}" no es un entero positivo.`
    );
    return false;
  }
  if (typeof compra.total !== "number" || compra.total <= 0) {
    console.warn(
      `Advertencia: El total de la compra "${compra.id}" no es un número positivo.`
    );
    return false;
  }
  if (Object.keys(compra.productos).length === 0) {
    console.warn(
      `Advertencia: La compra "${compra.id}" no contiene productos.`
    );
    return false;
  }
  for (let [nombreProducto, cantidad] of Object.entries(compra.productos)) {
    if (!Number.isInteger(cantidad) || cantidad <= 0) {
      console.warn(
        `Advertencia: La cantidad del producto "${nombreProducto}" en la compra "${compra.id}" no es un entero positivo.`
      );
      return false;
    }
  }
  return true;
}

// Función para analizar las compras y encontrar el producto menos vendido en diferentes rangos de precio
function analizarCompras(datos) {
  let comprasValidas = datos.filter(validarCompra);

  let rango0a100 = { total: 0, productos: {} };
  let rango100a200 = { total: 0, productos: {} };
  let rangoMayora200 = { total: 0, productos: {} };

  comprasValidas.forEach((compra) => {
    let productos = compra.productos;
    let totalCompra = compra.total;

    if (totalCompra >= 0 && totalCompra <= 100) {
      rango0a100.total += totalCompra;
      for (let [nombreProducto, cantidad] of Object.entries(productos)) {
        if (!rango0a100.productos[nombreProducto]) {
          rango0a100.productos[nombreProducto] = 0;
        }
        rango0a100.productos[nombreProducto] += cantidad;
      }
    } else if (totalCompra > 100 && totalCompra <= 200) {
      rango100a200.total += totalCompra;
      for (let [nombreProducto, cantidad] of Object.entries(productos)) {
        if (!rango100a200.productos[nombreProducto]) {
          rango100a200.productos[nombreProducto] = 0;
        }
        rango100a200.productos[nombreProducto] += cantidad;
      }
    } else {
      rangoMayora200.total += totalCompra;
      for (let [nombreProducto, cantidad] of Object.entries(productos)) {
        if (!rangoMayora200.productos[nombreProducto]) {
          rangoMayora200.productos[nombreProducto] = 0;
        }
        rangoMayora200.productos[nombreProducto] += cantidad;
      }
    }
  });

  function encontrarProductoMenosVendido(productos) {
    let productoMenosVendido = null;
    let cantidadMenosVendida = Infinity;
    for (let [nombreProducto, cantidad] of Object.entries(productos)) {
      if (cantidad < cantidadMenosVendida) {
        cantidadMenosVendida = cantidad;
        productoMenosVendido = nombreProducto;
      }
    }
    return { producto: productoMenosVendido, cantidad: cantidadMenosVendida };
  }

  let menosVendido0a100 = encontrarProductoMenosVendido(rango0a100.productos);
  let menosVendido100a200 = encontrarProductoMenosVendido(
    rango100a200.productos
  );
  let menosVendidoMayora200 = encontrarProductoMenosVendido(
    rangoMayora200.productos
  );

  console.log(
    `Producto menos vendido en compras de $0 a $100: ${menosVendido0a100.producto} (Cantidad: ${menosVendido0a100.cantidad})`
  );
  console.log(
    `Producto menos vendido en compras de $100 a $200: ${menosVendido100a200.producto} (Cantidad: ${menosVendido100a200.cantidad})`
  );
  console.log(
    `Producto menos vendido en compras de más de $200: ${menosVendidoMayora200.producto} (Cantidad: ${menosVendidoMayora200.cantidad})`
  );
}

// Leer el archivo JSON
fs.readFile("compras.json", "utf8", (err, data) => {
  if (err) {
    console.error("Error al leer el archivo JSON:", err);
    return;
  }
  try {
    let datos = JSON.parse(data);
    analizarCompras(datos);
  } catch (error) {
    console.error("Error al parsear los datos JSON:", error);
  }
});
