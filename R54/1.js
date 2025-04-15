class Venta {
  constructor(nombreCliente, cedulaCliente, productos, total) {
    if (!this.validarNombre(nombreCliente)) {
      throw new Error(
        "Nombre inválido. Debe contener solo letras y no puede estar vacío."
      );
    }
    if (!this.validarCedula(cedulaCliente)) {
      throw new Error("Cédula inválida. Debe contener exactamente 10 números.");
    }
    if (!this.validarProductos(productos)) {
      throw new Error(
        "Productos inválidos. Deben contener solo letras y no pueden estar vacíos."
      );
    }
    if (!this.validarTotal(total)) {
      throw new Error("El total de la venta debe ser un número.");
    }

    this.nombreCliente = nombreCliente;
    this.cedulaCliente = cedulaCliente;
    this.productos = productos;
    this.total = total;
  }

  validarNombre(nombre) {
    return /^[a-zA-Z\s]+$/.test(nombre) && nombre.trim() !== "";
  }

  validarCedula(cedula) {
    return /^\d{10}$/.test(cedula);
  }

  validarProductos(productos) {
    return /^[a-zA-Z\s,]+$/.test(productos) && productos.trim() !== "";
  }

  validarTotal(total) {
    return typeof total === "number" && total > 0;
  }
}

class Restaurante {
  constructor() {
    this.ventas = [];
  }

  registrarVenta(nombreCliente, cedulaCliente, productos, total) {
    try {
      const venta = new Venta(nombreCliente, cedulaCliente, productos, total);
      this.ventas.push(venta);
      console.log("Venta registrada exitosamente.");
    } catch (error) {
      console.error(error.message);
    }
  }

  consultarVentas() {
    if (this.ventas.length === 0) {
      console.log("No hay ventas registradas.");
      return;
    }
    console.table(
      this.ventas.map((venta, index) => ({
        ID: index + 1,
        "Nombre Cliente": venta.nombreCliente,
        "Cédula Cliente": venta.cedulaCliente,
        Productos: venta.productos,
        Total: venta.total.toFixed(2),
      }))
    );
  }

  buscarVentasPorCedula(cedulaCliente) {
    const ventasEncontradas = this.ventas.filter(
      (venta) => venta.cedulaCliente === cedulaCliente
    );

    if (ventasEncontradas.length === 0) {
      console.log(`No se encontraron ventas para la cédula: ${cedulaCliente}`);
      return;
    }

    console.table(
      ventasEncontradas.map((venta, index) => ({
        ID: index + 1,
        "Nombre Cliente": venta.nombreCliente,
        "Cédula Cliente": venta.cedulaCliente,
        Productos: venta.productos,
        Total: venta.total.toFixed(2),
      }))
    );
  }
}

// Ejemplo de uso:
const miRestaurante = new Restaurante();
miRestaurante.registrarVenta(
  "Juan Perez  @ ",
  "0123456789",
  "Pizza, Soda",
  150
);
miRestaurante.registrarVenta(
  "Maria Gomez",
  "9876543210",
  "Hamburguesa, Papas",
  120
);
miRestaurante.consultarVentas();
miRestaurante.buscarVentasPorCedula("9876543210");
