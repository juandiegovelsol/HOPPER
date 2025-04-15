const fs = require("fs");

function validarCompra(compra) {
  if (!Number.isInteger(compra.id) || compra.id <= 0) {
    console.warn(
      `Advertencia: El ID de compra "${compra.id}" no es un entero positivo. Ignorando compra.`
    );
    return false;
  }

  if (!Number.isInteger(compra.total) || compra.total <= 0) {
    console.warn(
      `Advertencia: El total de la compra "${compra.id}" no es un número positivo. Ignorando compra.`
    );
    return false;
  }

  if (Object.keys(compra.productos).length === 0) {
    console.warn(
      `Advertencia: La compra "${compra.id}" no contiene productos. Ignorando compra.`
    );
    return false;
  }

  for (const [producto, cantidad] of Object.entries(compra.productos)) {
    if (!Number.isInteger(cantidad) || cantidad <= 0) {
      console.warn(
        `Advertencia: La cantidad del producto "${producto}" en la compra "${compra.id}" no es un entero positivo. Ignorando producto.`
      );
      return false;
    }
  }

  return true;
}

function encontrarProductoMenosVendido(compras, min, max) {
  let productoMenosVendido = null;
  let cantidadMenosVendida = Infinity;

  for (const compra of compras) {
    if (compra.total >= min && compra.total <= max) {
      for (const [producto, cantidad] of Object.entries(compra.productos)) {
        if (cantidad < cantidadMenosVendida) {
          productoMenosVendido = producto;
          cantidadMenosVendida = cantidad;
        }
      }
    }
  }

  return {
    producto: productoMenosVendido,
    cantidad: cantidadMenosVendida,
  };
}

function procesarCompras(compras) {
  const comprasValidas = [];

  for (const compra of compras) {
    if (validarCompra(compra)) {
      comprasValidas.push(compra);
    }
  }

  const productoMenosVendido0a100 = encontrarProductoMenosVendido(
    comprasValidas,
    0,
    100
  );
  const productoMenosVendido100a200 = encontrarProductoMenosVendido(
    comprasValidas,
    100,
    200
  );
  const productoMenosVendido200oMas = encontrarProductoMenosVendido(
    comprasValidas,
    200,
    Infinity
  );

  console.log(
    `Producto menos vendido en compras de $0-$100: ${productoMenosVendido0a100.producto} (Cantidad: ${productoMenosVendido0a100.cantidad})`
  );
  console.log(
    `Producto menos vendido en compras de $100-$200: ${productoMenosVendido100a200.producto} (Cantidad: ${productoMenosVendido100a200.cantidad})`
  );
  console.log(
    `Producto menos vendido en compras de $200 o más: ${productoMenosVendido200oMas.producto} (Cantidad: ${productoMenosVendido200oMas.cantidad})`
  );
}

fs.readFile("compras.json", "utf8", (err, data) => {
  if (err) {
    console.error("Error al leer el archivo JSON:", err);
    return;
  }

  try {
    const compras = JSON.parse(data);
    procesarCompras(compras);
  } catch (parseError) {
    console.error("Error al parsear el archivo JSON:", parseError);
  }
});
