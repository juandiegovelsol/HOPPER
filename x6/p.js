function calcularTotal(carrito, descuentoGlobal, impuestos) {
  if (
    !Array.isArray(carrito) ||
    typeof descuentoGlobal !== "number" ||
    typeof impuestos !== "number"
  ) {
    throw new Error("Entrada inválida");
  }
  if (descuentoGlobal < 0 || impuestos < 0) {
    throw new Error(
      "Los valores de descuento e impuestos no pueden ser negativos"
    );
  }
  if (carrito.length === 0) {
    return 0;
  }

  let subtotal = carrito.reduce((total, producto) => {
    if (producto.precio < 0 || producto.cantidad < 0) {
      throw new Error("Precios y cantidades no pueden ser negativos");
    }
    return total + producto.precio * producto.cantidad;
  }, 0);

  let totalConDescuento = subtotal - subtotal * (descuentoGlobal / 100);
  let totalFinal = totalConDescuento + totalConDescuento * (impuestos / 100);

  return Math.round(totalFinal * 100) / 100;
}

console.log(
  calcularTotal(
    [
      { precio: 10, cantidad: 1 },
      { precio: 5, cantidad: 3 },
    ],
    10
  )
);
