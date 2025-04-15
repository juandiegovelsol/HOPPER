function calcularCosteReserva(precioPorNoche, noches, codigoDescuento) {
  // Validación de entrada
  if (
    !/^\d+$/.test(precioPorNoche) ||
    !/^\d+$/.test(noches) ||
    typeof codigoDescuento !== "string"
  ) {
    throw new Error(
      "Parámetros inválidos. Introduzca un precio y número de noches válidos y un código de descuento como cadena."
    );
  }

  precioPorNoche = parseFloat(precioPorNoche);
  noches = parseInt(noches, 10);

  let subtotal = precioPorNoche * noches;
  let descuento = 0;

  // Aplicar descuento si el código es válido
  if (codigoDescuento.toUpperCase() === "DESCUENTO2025") {
    descuento = subtotal * 0.15;
  }

  // Calcular el total con IVA (21%) aplicado al subtotal después de descontar
  let total = (subtotal - descuento) * 1.21;

  return total;
}

// Ejemplo de uso
console.log(calcularCosteReserva(100, 3, "")); // Debería imprimir 330.75
console.log(calcularCosteReserva("100", 3, "DESCUENTO2025".toUpperCase())); // También debería imprimir 330.75
console.log(calcularCosteReserva(100, 3, false)); // Debería imprimir 363.00 (sin descuento)
