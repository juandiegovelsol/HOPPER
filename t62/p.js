const fs = require("fs");

function verificarPedido(pedido) {
  if (Object.keys(pedido.zapatos).length === 0) {
    console.warn(
      `Alerta: El pedido con ID "${pedido.id}" no contiene zapatos. Se omitirá.`
    );
    return false;
  }
  if (!Number.isInteger(pedido.id) || pedido.id <= 0) {
    console.warn(
      `Alerta: El identificador "${pedido.id}" no es un entero positivo. Se descartará este pedido.`
    );
    return false;
  }
  if (!Number.isInteger(pedido.total) || pedido.total <= 0) {
    console.warn(
      `Alerta: El total del pedido con ID "${pedido.id}" no es un número positivo. Se ignorará.`
    );
    return false;
  }
  for (const [modelo, cantidad] of Object.entries(pedido.zapatos)) {
    if (!Number.isInteger(cantidad) || cantidad <= 0) {
      console.warn(
        `Alerta: La cantidad del modelo "${modelo}" en el pedido "${pedido.id}" no es válida. Se descartará.`
      );
      return false;
    }
  }
  return true;
}

function obtenerModeloConMenorVentas(pedidos, minimo, maximo) {
  const conteoModelos = {};
  for (const pedido of pedidos) {
    if (pedido.total > minimo && pedido.total <= maximo) {
      for (const [modelo, cantidad] of Object.entries(pedido.zapatos)) {
        if (!conteoModelos[modelo]) {
          conteoModelos[modelo] = 0;
        }
        conteoModelos[modelo] += cantidad;
      }
    }
  }
  let modeloMenor = null;
  let cantidadMinima = Infinity;
  for (const [modelo, cantidad] of Object.entries(conteoModelos)) {
    if (cantidad < cantidadMinima) {
      modeloMenor = modelo;
      cantidadMinima = cantidad;
    }
  }
  return cantidadMinima === Infinity
    ? null
    : { modelo: modeloMenor, cantidad: cantidadMinima };
}

function procesarPedidos(pedidos) {
  const pedidosValidos = [];
  for (const pedido of pedidos) {
    if (verificarPedido(pedido)) {
      pedidosValidos.push(pedido);
    }
  }
  const modeloMenor0a100 = obtenerModeloConMenorVentas(pedidosValidos, 0, 100);
  const modeloMenor100a200 = obtenerModeloConMenorVentas(
    pedidosValidos,
    100,
    200
  );
  const modeloMenor200oMas = obtenerModeloConMenorVentas(
    pedidosValidos,
    200,
    Infinity
  );
  console.log(
    modeloMenor0a100
      ? `Modelo de zapatos con menor ventas en pedidos de $0-$100: ${modeloMenor0a100.modelo} (Cantidad: ${modeloMenor0a100.cantidad})`
      : "No hay pedidos en el rango de precios $0-$100."
  );
  console.log(
    modeloMenor100a200
      ? `Modelo de zapatos con menor ventas en pedidos de $100-$200: ${modeloMenor100a200.modelo} (Cantidad: ${modeloMenor100a200.cantidad})`
      : "No hay pedidos en el rango de precios $100-$200."
  );
  console.log(
    modeloMenor200oMas
      ? `Modelo de zapatos con menor ventas en pedidos de $200 o más: ${modeloMenor200oMas.modelo} (Cantidad: ${modeloMenor200oMas.cantidad})`
      : "No hay pedidos en el rango de precios $200 o más."
  );
}

fs.readFile("pedidos.json", "utf8", (err, data) => {
  if (err) {
    console.error("Error al leer el archivo JSON de pedidos:", err);
    return;
  }
  try {
    const pedidos = JSON.parse(data);
    procesarPedidos(pedidos);
  } catch (error) {
    console.error("Error al interpretar el archivo JSON de pedidos:", error);
  }
});
