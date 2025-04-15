const fs = require("fs");

function procesarArchivoJSON(rutaArchivo) {
  try {
    const jsonString = fs.readFileSync(rutaArchivo, "utf8");

    return procesarPedidos(jsonString);
  } catch (error) {
    console.error("Error:", error.message);
    return null;
  }
}

function procesarPedidos(jsonString) {
  try {
    const pedidos = JSON.parse(jsonString);

    if (!Array.isArray(pedidos)) {
      throw new Error(
        "El formato JSON no es válido. Se espera un array de pedidos."
      );
    }

    validarEstructuraPedidos(pedidos);

    const { totalVentas, productoMasVendido } = analizarPedidos(pedidos);

    console.log(`Total vendido: $${totalVentas.toLocaleString("es-CL")} CLP`);
    console.log(
      `Producto más vendido: ID ${productoMasVendido.id} (${productoMasVendido.cantidad} unidades)`
    );

    return {
      totalVentas,
      productoMasVendido,
    };
  } catch (error) {
    console.error("Error al procesar el archivo:", error.message);
    return null;
  }
}

function validarEstructuraPedidos(pedidos) {
  const idsPedidos = new Set();

  for (let i = 0; i < pedidos.length; i++) {
    const pedido = pedidos[i];

    if (
      !pedido.id ||
      typeof pedido.id !== "number" ||
      pedido.id <= 0 ||
      !Number.isInteger(pedido.id)
    ) {
      throw new Error(`Pedido #${i + 1}: El ID debe ser un entero positivo`);
    }

    if (idsPedidos.has(pedido.id)) {
      throw new Error(`Pedido #${i + 1}: El ID ${pedido.id} está duplicado`);
    }
    idsPedidos.add(pedido.id);

    if (!pedido.fecha || typeof pedido.fecha !== "string") {
      throw new Error(`Pedido #${i + 1}: Falta fecha o formato incorrecto`);
    }

    if (!Array.isArray(pedido.items)) {
      throw new Error(`Pedido #${i + 1}: El campo 'items' debe ser un array`);
    }

    for (let j = 0; j < pedido.items.length; j++) {
      const item = pedido.items[j];

      if (
        !item.idProducto ||
        typeof item.idProducto !== "number" ||
        item.idProducto <= 0 ||
        !Number.isInteger(item.idProducto)
      ) {
        throw new Error(
          `Pedido #${i + 1}, Item #${
            j + 1
          }: El ID del producto debe ser un entero positivo`
        );
      }

      if (
        !item.cantidad ||
        typeof item.cantidad !== "number" ||
        item.cantidad <= 0
      ) {
        throw new Error(`Pedido #${i + 1}, Item #${j + 1}: Cantidad inválida`);
      }

      if (!item.precio || typeof item.precio !== "number" || item.precio <= 0) {
        throw new Error(`Pedido #${i + 1}, Item #${j + 1}: Precio inválido`);
      }
    }
  }
}

function analizarPedidos(pedidos) {
  let totalVentas = 0;
  const ventasPorProducto = {};

  pedidos.forEach((pedido) => {
    pedido.items.forEach((item) => {
      const subtotal = item.precio * item.cantidad;
      totalVentas += subtotal;

      if (!ventasPorProducto[item.idProducto]) {
        ventasPorProducto[item.idProducto] = 0;
      }
      ventasPorProducto[item.idProducto] += item.cantidad;
    });
  });

  let maxCantidad = 0;
  let productoMasVendido = null;

  Object.entries(ventasPorProducto).forEach(([idProducto, cantidad]) => {
    if (cantidad > maxCantidad) {
      maxCantidad = cantidad;
      productoMasVendido = { id: parseInt(idProducto), cantidad };
    }
  });

  return {
    totalVentas,
    productoMasVendido,
  };
}

if (require.main === module) {
  const rutaArchivo = process.argv[2] || "pedidos.json";
  console.log(`Procesando archivo: ${rutaArchivo}`);
  procesarArchivoJSON(rutaArchivo);
}

module.exports = {
  procesarArchivoJSON,
  procesarPedidos,
};
