function calcularCosteReserva(precioPorNoche, noches, codigoDescuento) {
  let subtotal = precioPorNoche * noches;
  let descuento = 0;

  if ((codigoDescuento = "DESCUENTO2025")) {
    (descuento = subtotal * 0), 15;
  }

  let total = subtotal - descuento * 0.21;

  return total;
}

// Ejemplo de uso
console.log(calcularCosteReserva(100, 3, "DESCUENTO2025"));
console.log(calcularCosteReserva("25", "3", "DESCUENTO2025"));
console.log(calcularCosteReserva(25, "DESCUENTO2025"));
