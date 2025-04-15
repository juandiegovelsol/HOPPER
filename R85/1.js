class Mesa {
  constructor(id, capacidad, ubicacion) {
    this.id = id;
    this.capacidad = capacidad; // Capacidad máxima de la mesa
    this.estado = "disponible"; // Estado de la mesa: disponible, ocupada, reservada
    this.ubicacion = ubicacion; // Ubicación: "cerca de la ventana", "terraza", "vereda"
    this.reservada = false; // Indica si la mesa está reservada
    this.reservada_hasta = null; // Hora hasta la que está reservada
  }

  reservar(hasta) {
    this.estado = "reservada";
    this.reservada = true;
    this.reservada_hasta = hasta;
  }

  ocupar() {
    this.estado = "ocupada";
  }

  liberar() {
    this.estado = "disponible";
    this.reservada = false;
    this.reservada_hasta = null;
  }
}

class Restaurante {
  constructor() {
    this.mesas = [];
  }

  agregarMesa(mesa) {
    this.mesas.push(mesa);
  }

  asignarMesa(cantidadComensales, preferenciaUbicacion) {
    const mesaDisponible = this.mesas.find(
      (mesa) =>
        mesa.capacidad >= cantidadComensales &&
        mesa.estado === "disponible" &&
        mesa.ubicacion === preferenciaUbicacion
    );

    if (mesaDisponible) {
      mesaDisponible.ocupar();
      return mesaDisponible.id;
    } else {
      return this.opcionEspera(cantidadComensales);
    }
  }

  opcionEspera(cantidadComensales) {
    // Aquí podrías implementar lógica para calcular el tiempo estimado de espera
    return `No hay mesas disponibles para ${cantidadComensales} comensales. Tiempo estimado de espera: 20 minutos.`;
  }

  reservarMesa(idMesa, duracionReserva) {
    const mesa = this.mesas.find(
      (mesa) => mesa.id === idMesa && mesa.estado === "disponible"
    );

    if (mesa) {
      const ahora = new Date();
      const reservaHasta = new Date(ahora.getTime() + duracionReserva * 60000); // Duración en minutos
      mesa.reservar(reservaHasta);
      return `Mesa ${
        mesa.id
      } reservada hasta ${reservaHasta.toLocaleTimeString()}.`;
    } else {
      return `Mesa no disponible para reserva.`;
    }
  }

  liberarMesa(idMesa) {
    const mesa = this.mesas.find((mesa) => mesa.id === idMesa);

    if (mesa) {
      mesa.liberar();
      return `Mesa ${mesa.id} liberada.`;
    } else {
      return `Mesa no encontrada.`;
    }
  }
}

// Ejemplo de uso
const restaurante = new Restaurante();
restaurante.agregarMesa(new Mesa(1, 4, "cerca de la ventana"));
restaurante.agregarMesa(new Mesa(2, 2, "terraza"));
restaurante.agregarMesa(new Mesa(3, 6, "vereda"));

console.log(restaurante.asignarMesa(2, "terraza")); // Asigna mesa
console.log(restaurante.reservarMesa(1, 30)); // Reserva mesa 1 por 30 minutos
console.log(restaurante.liberarMesa(2)); // Libera mesa 2
