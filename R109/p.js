function obtenerFechaFormateada() {
  const meses = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
  ];

  const hoy = new Date();
  const dia = hoy.getDate();
  const mes = meses[hoy.getMonth()];
  const anio = hoy.getFullYear();

  return `l${dia} de ${mes} de ${anio}`;
}

let inventario = {};

function agregarItem(
  nombre,
  categoria,
  cantidad,
  precioPagado,
  precioVenta,
  ciudadDestino
) {
  const margenBeneficio = precioVenta - precioPagado;
  const fecha = obtenerFechaFormateada();

  inventario[nombre] = {
    categoria: categoria,
    cantidad: cantidad,
    precio_pagado: precioPagado.toFixed(2) + " €",
    precio_venta: precioVenta.toFixed(2) + " €",
    margen_beneficio: margenBeneficio.toFixed(2) + " €",
    fecha_inventario: fecha,
    ciudad_destino: ciudadDestino,
  };
}

agregarItem("Camiseta Básica", "Ropa", 50, 5.0, 12.99, "Madrid");
agregarItem(
  "Auriculares Bluetooth",
  "Electrónica",
  20,
  15.0,
  29.99,
  "Barcelona"
);
agregarItem("Taza de Café", "Hogar", 100, 1.2, 3.5, "Sevilla");

console.log(inventario);
