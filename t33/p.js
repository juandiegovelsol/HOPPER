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

    const { totalVentas, platoMasVendido } = analizarPedidos(pedidos);

    console.log(`Total vendido: $${totalVentas.toLocaleString("es-CL")} CLP`);
    console.log(
      `Plato más vendido: ID ${platoMasVendido.id} (${platoMasVendido.cantidad} unidades)`
    );

    return {
      totalVentas,
      platoMasVendido,
    };
  } catch (error) {
    console.error("Error al procesar el archivo:", error.message);
    return null;
  }
}

function validarEstructuraPedidos(pedidos) {
  for (let i = 0; i < pedidos.length; i++) {
    const pedido = pedidos[i];

    if (!pedido.id || typeof pedido.id !== "string") {
      throw new Error(
        `Pedido #${i + 1}: Falta ID de pedido o formato incorrecto`
      );
    }

    if (!pedido.fecha || typeof pedido.fecha !== "string") {
      throw new Error(`Pedido #${i + 1}: Falta fecha o formato incorrecto`);
    }

    if (!Array.isArray(pedido.items)) {
      throw new Error(`Pedido #${i + 1}: El campo 'items' debe ser un array`);
    }

    for (let j = 0; j < pedido.items.length; j++) {
      const item = pedido.items[j];

      if (!item.idPlato || typeof item.idPlato !== "string") {
        throw new Error(
          `Pedido #${i + 1}, Item #${
            j + 1
          }: Falta ID de plato o formato incorrecto`
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
  const ventasPorPlato = {};

  pedidos.forEach((pedido) => {
    pedido.items.forEach((item) => {
      const subtotal = item.precio * item.cantidad;
      totalVentas += subtotal;

      if (!ventasPorPlato[item.idPlato]) {
        ventasPorPlato[item.idPlato] = 0;
      }
      ventasPorPlato[item.idPlato] += item.cantidad;
    });
  });

  let maxCantidad = 0;
  let platoMasVendido = null;

  Object.entries(ventasPorPlato).forEach(([idPlato, cantidad]) => {
    if (cantidad > maxCantidad) {
      maxCantidad = cantidad;
      platoMasVendido = { id: idPlato, cantidad };
    }
  });

  return {
    totalVentas,
    platoMasVendido,
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
