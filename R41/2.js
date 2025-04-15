// Objeto para representar el menú del restaurante
const menu = [
  {
    id: 1,
    nombre: "Pizza Margarita",
    descripcion: "Pizza clásica con tomate, mozzarella y albahaca.",
    precio: 8.0,
    personalizable: true,
    opciones: {
      tamaño: {
        pequeño: 0.8,
        mediano: 1.0,
        grande: 1.2,
      },
      adicionalDeQueso: true,
      extraIngrediente: [
        { nombre: "Aceitunas", precio: 0.5 },
        { nombre: "Pimientos", precio: 0.7 },
        { nombre: "Jamón", precio: 1.0 },
      ],
    },
  },
  {
    id: 2,
    nombre: "Ensalada César",
    descripcion: "Ensalada de lechuga, pollo, crutones y aderezo César.",
    precio: 6.5,
    personalizable: false,
  },
];

// Función para calcular el precio final del pedido
function calcularPrecioFinal(pedido) {
  let precioFinal = pedido.producto.precio;

  if (pedido.producto.personalizable) {
    // Ajustar el precio según las opciones seleccionadas
    if (pedido.tamaño === "mediano") {
      precioFinal += pedido.producto.opciones.tamaño.mediano;
    } else if (pedido.tamaño === "grande") {
      precioFinal += pedido.producto.opciones.tamaño.grande;
    }

    if (pedido.adicionalDeQueso) {
      precioFinal += pedido.producto.opciones.adicionalDeQueso;
    }

    if (pedido.ingredientesSeleccionados) {
      pedido.ingredientesSeleccionados.forEach((ingrediente) => {
        precioFinal += ingrediente.precio;
      });
    }
  }

  return precioFinal.toFixed(2);
}

// Función para procesar pedidos de los clientes
function realizarPedido(cliente, productoSeleccionado, detallesPedido) {
  const producto = menu.find((p) => p.id === productoSeleccionado);

  if (!producto) {
    console.error("Producto no encontrado");
    return;
  }

  const pedido = {
    cliente: cliente,
    producto: producto,
    comentarios: detallesPedido.comentarios || "",
    tamaño: detallesPedido.tamaño || "pequeño",
    adicionalDeQueso: detallesPedido.adicionalDeQueso || false,
    ingredientesSeleccionados: detallesPedido.ingredientesSeleccionados || [],
  };

  const precioFinal = calcularPrecioFinal(pedido);

  console.log("Pedido realizado:");
  console.log("Cliente:", cliente);
  console.log("Producto:", producto.nombre);
  console.log("Comentarios:", pedido.comentarios);
  console.log("Precio final: $" + precioFinal);
}

// Ejemplo de uso
const cliente = "Juan Pérez";
const productoSeleccionado = 1; // ID del producto (Pizza Margarita)
const detallesPedido = {
  comentarios: "Sin albahaca por favor",
  tamaño: "mediano",
  adicionalDeQueso: true,
  ingredientesSeleccionados: [
    { nombre: "Aceitunas", precio: 0.5 },
    { nombre: "Jamón", precio: 1.0 },
  ],
};

realizarPedido(cliente, productoSeleccionado, detallesPedido);
