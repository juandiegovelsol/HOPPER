function calcularCosteReserva(precioPorNoche, noches, codigoDescuento) {
  // Validación de la existencia y corrección del código de descuento
  if (
    typeof codigoDescuento !== "string" ||
    codigoDescuento !== "DESCUENTO2025"
  ) {
    return "Código de descuento no válido";
  }

  // Validación de los tipos de datos y conversión si es necesario
  const ppn =
    typeof precioPorNoche === "number"
      ? precioPorNoche
      : parseFloat(precioPorNoche);
  const numNoches = typeof noches === "number" ? noches : parseInt(noches, 10);

  if (isNaN(ppn) || isNaN(numNoches) || ppn <= 0 || numNoches <= 0) {
    return "Valores de precio o noches inválidos";
  }

  // Cálculo del subtotal
  let subtotal = ppn * numNoches;
  let descuento = 0;

  // Cálculo del descuento si el código es correcto
  if (codigoDescuento === "DESCUENTO2025") {
    descuento = subtotal * 0.15;
  }

  // Aplicación del IVA (21%) sobre el subtotal después de restar el descuento
  let total = (subtotal - descuento) * 1.21;

  return total.toFixed(2);
}

// Casos de uso
console.log(calcularCosteReserva(100, 3, "")); // Debería mostrar el total con descuento
console.log(calcularCosteReserva("25", "3", "DESCUENTO2025")); // Debería mostrar el total con descuento
console.log(calcularCosteReserva(25, 3, "DESCUENTO2025")); // Debería mostrar el total con descuento
console.log(calcularCosteReserva(100, 3, "DESCUENTO2021")); // Debería mostrar el total sin descuento
console.log(calcularCosteReserva(100, 3, "Hola")); // Debería mostrar el error: "Código de descuento no válido"
console.log(calcularCosteReserva("a", 3, "DESCUENTO2025")); // Debería mostrar el error: "Valores de precio o noches inválidos"
console.log(calcularCosteReserva(100, "b", "DESCUENTO2025")); // Debería mostrar el error: "Valores de precio o noches inválidos"
console.log(calcularCosteReserva(100, 3, "invalido")); // Debería mostrar el error: "Código de descuento no válido"
