class Mesa {
  constructor(id, capacidad, ubicacion) {
    this.id = id;
    this.capacidad = capacidad;
    this.ubicacion = ubicacion;
    this.estado = "disponible"; // Puede ser 'disponible', 'ocupada' o 'reservada'
    this.reservada = false;
    this.reservada_hasta = null;
  }
}

class Restaurante {
  constructor() {
    this.mesas = [
      new Mesa(1, 2, "cerca de la ventana"),
      new Mesa(2, 4, "terraza"),
      new Mesa(3, 6, "vereda"),
      // Añadir más mesas según sea necesario
    ];
  }

  asignarMesa(comensales, preferencias) {
    const { cercaDeLaVentana, terraza, vereda } = preferencias;

    // Filter mesas based on capacity and location preference
    const mesasDisponibles = this.mesas.filter(
      (mesa) =>
        mesa.capacidad >= comensales &&
        (!mesa.reservada ||
          (mesa.estado !== "ocupada" &&
            new Date(mesa.reservada_hasta) < new Date()))
    );

    const mesaPreferida = mesasDisponibles.find(
      (mesa) =>
        mesa.ubicacion === cercaDeLaVentana ||
        mesa.ubicacion === terraza ||
        mesa.ubicacion === vereda
    );

    if (mesaPreferida) {
      this.reservarMesa(mesaPreferida, comensales);
      return {
        mesaAsignada: mesaPreferida.id,
        estado: "mesa asignada",
      };
    } else if (mesasDisponibles.length > 0) {
      // Si no hay mesa preferida disponible, asignar la primera disponible
      const mesaDisponible = mesasDisponibles[0];
      this.reservarMesa(mesaDisponible, comensales);
      return {
        mesaAsignada: mesaDisponible.id,
        estado: "mesa asignada",
      };
    } else {
      return {
        mesaAsignada: null,
        estado: "espera",
        tiempoEstimado: "15 minutos", // Tiempo estimado de espera
      };
    }
  }

  reservarMesa(mesa, comensales, tiempoEspera = 15) {
    mesa.estado = "reservada";
    mesa.reservada = true;
    mesa.reservada_hasta = new Date(Date.now() + tiempoEspera * 60000); // Tiempo de espera en minutos

    // Bloquear la mesa hasta que llegue el cliente
    setTimeout(() => {
      if (mesa.estado === "reservada") {
        mesa.estado = "disponible";
        mesa.reservada = false;
        mesa.reservada_hasta = null;
      }
    }, tiempoEspera * 60000); // Milisegundos para bloquear la mesa
  }

  reasignarMesa(mesaId, nuevosComensales) {
    const mesa = this.mesas.find((m) => m.id === mesaId);
    if (
      mesa &&
      mesa.estado === "ocupada" &&
      mesa.capacidad >= nuevosComensales
    ) {
      // Actualizar capacidad si es necesario
      return this.asignarMesa(nuevosComensales, mesa.ubicacion);
    }
    return {
      mesaAsignada: null,
      estado: "error",
      mensaje: "No se pudo reasignar la mesa",
    };
  }
}

// Ejemplo de uso:
const restaurante = new Restaurante();

// Asignación normal
const reserva = restaurante.asignarMesa(4, { cercaDeLaVentana: true });
console.log(reserva); // { mesaAsignada: 2, estado: 'mesa asignada' }

// Asignación con espera
const reservaEnEspera = restaurante.asignarMesa(8, { terraza: true });
console.log(reservaEnEspera); // { mesaAsignada: null, estado: 'espera', tiempoEstimado: '15 minutos' }

// Reasignación de mesa
const reasignacion = restaurante.reasignarMesa(2, 3);
console.log(reasignacion); // { mesaAsignada: null, estado: 'error', mensaje: 'No se pudo reasignar la mesa' }
