// Clase Venta que representa una transacción de venta
class Venta {
  constructor(nombreCliente, cedulaCliente, productos, totalVenta) {
    // Validaciones de entrada
    if (!nombreCliente || nombreCliente.trim() === "") {
      throw new Error(
        "El nombre del cliente no puede estar vacío y solo debe contener letras."
      );
    }
    if (
      !cedulaCliente ||
      cedulaCliente.trim() === "" ||
      isNaN(cedulaCliente) ||
      cedulaCliente.length !== 10
    ) {
      throw new Error(
        "La cédula del cliente debe ser de 10 dígitos numéricos."
      );
    }
    if (!productos || productos.trim() === "") {
      throw new Error(
        "La lista de productos no puede estar vacía y debe contener solo letras."
      );
    }
    if (!totalVenta || isNaN(totalVenta) || totalVenta < 0) {
      throw new Error("El total de la venta debe ser un número positivo.");
    }

    this.nombreCliente = nombreCliente;
    this.cedulaCliente = cedulaCliente;
    this.productos = productos;
    this.totalVenta = totalVenta;
  }
}

// Clase Restaurante que administra las ventas
class Restaurante {
  constructor() {
    this.ventas = [];
  }

  // Método para registrar una nueva venta
  registrarVenta(nombreCliente, cedulaCliente, productos, totalVenta) {
    const nuevaVenta = new Venta(
      nombreCliente,
      cedulaCliente,
      productos,
      totalVenta
    );
    this.ventas.push(nuevaVenta);
    console.log("Venta registrada exitosamente.");
  }

  // Método para consultar todas las ventas
  consultarVentas() {
    if (this.ventas.length === 0) {
      console.log("No hay ventas registradas.");
      return;
    }

    console.log("Todas las ventas:");
    this.ventas.forEach((venta, index) => {
      console.log(
        `${index + 1}. Nombre: ${venta.nombreCliente}, Cédula: ${
          venta.cedulaCliente
        }, Productos: ${venta.productos}, Total: ${venta.totalVenta}`
      );
    });
  }

  // Método para buscar ventas por cédula de cliente
  buscarVentasPorCedula(cedulaCliente) {
    if (!cedulaCliente || isNaN(cedulaCliente) || cedulaCliente.length !== 10) {
      throw new Error(
        "Debe ingresar una cédula de 10 dígitos numéricos para buscar."
      );
    }

    const ventasCliente = this.ventas.filter(
      (venta) => venta.cedulaCliente === cedulaCliente
    );

    if (ventasCliente.length === 0) {
      console.log(`No se encontraron ventas para la cédula ${cedulaCliente}.`);
      return;
    }

    console.log(`Ventas para la cédula ${cedulaCliente}:`);
    ventasCliente.forEach((venta, index) => {
      console.log(
        `${index + 1}. Nombre: ${venta.nombreCliente}, Productos: ${
          venta.productos
        }, Total: ${venta.totalVenta}`
      );
    });
  }
}

// Creando una instancia de Restaurante
const miRestaurante = new Restaurante();

// Ejemplo de uso
try {
  miRestaurante.registrarVenta(
    "Juan Pérez123@",
    "1234567890",
    "Pizza y refresco",
    500
  );
  miRestaurante.registrarVenta(
    "María López",
    "0987654321",
    "Ensalada y postre",
    350
  );

  console.log("\nTodas las ventas:");
  miRestaurante.consultarVentas();

  console.log("\nBuscando ventas por cédula 1234567890:");
  miRestaurante.buscarVentasPorCedula("1234567890");
} catch (error) {
  console.error(error.message);
}
