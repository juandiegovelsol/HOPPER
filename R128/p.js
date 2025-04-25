class ServicioCarga {
  constructor() {
    this.entregas = [];
  }

  static formatearEuros(valor) {
    const parteNumerica = ServicioCarga.formatearNumero(valor);
    return `${parteNumerica} €`;
  }

  static formatearNumero(valor) {
    return valor
      .toFixed(2)
      .replace(".", ",")
      .replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  }

  static parsearFecha(fechaStr) {
    const [dia, mes, anio] = fechaStr.split("/").map(Number);
    if (!dia || !mes || !anio) throw new Error("Formato de fecha inválido");
    const fecha = new Date(anio, mes - 1, dia);
    if (isNaN(fecha.getTime())) throw new Error("Fecha no válida");
    return fecha;
  }

  static validarDireccion(direccion) {
    return (
      typeof direccion === "string" &&
      /^[\p{L}\d\s,ºª.\-]+$/u.test(direccion.trim())
    );
  }

  static calcularDias(fechaInicio, fechaFin) {
    const msDia = 1000 * 60 * 60 * 24;
    return Math.round((fechaFin - fechaInicio) / msDia);
  }

  registrar(pesoKg, direccion, fechaSalidaStr, fechaEntregaStr, valorEUR) {
    if (typeof pesoKg !== "number" || pesoKg <= 0)
      throw new Error("Peso inválido");
    if (!ServicioCarga.validarDireccion(direccion))
      throw new Error("Dirección inválida");
    if (typeof valorEUR !== "number" || valorEUR <= 0)
      throw new Error("Valor de entrega inválido");

    const fechaSalida = ServicioCarga.parsearFecha(fechaSalidaStr);
    const fechaEntrega = ServicioCarga.parsearFecha(fechaEntregaStr);

    if (fechaEntrega < fechaSalida)
      throw new Error(
        "La fecha de entrega no puede ser anterior a la de salida"
      );

    const dias = ServicioCarga.calcularDias(fechaSalida, fechaEntrega);

    const entrega = {
      pesoKg,
      direccion,
      fechaSalidaStr,
      fechaEntregaStr,
      valorEUR,
      dias,
    };

    this.entregas.push(entrega);
    this.imprimirResumen(entrega);
  }

  imprimirResumen(entrega) {
    console.log(`Entrega registrada con éxito:
- Destino: ${entrega.direccion}
- Peso transportado: ${ServicioCarga.formatearNumero(entrega.pesoKg)} kg
- Fecha de salida: ${entrega.fechaSalidaStr}
- Fecha de entrega: ${entrega.fechaEntregaStr}
- Tiempo de transporte: ${entrega.dias} día(s)
- Valor del servicio: ${ServicioCarga.formatearEuros(entrega.valorEUR)}
`);
  }
}

const gestor = new ServicioCarga();

function registrarCarga(
  pesoKg,
  direccion,
  fechaSalida,
  fechaEntrega,
  valorEUR
) {
  try {
    gestor.registrar(pesoKg, direccion, fechaSalida, fechaEntrega, valorEUR);
  } catch (error) {
    console.log(`Error al registrar carga: ${error.message}`);
  }
}

registrarCarga(1250.5, "Calle Mayor 45", "12/04/2025", "14/04/2025", 349.99);
console.log("\n");
registrarCarga(
  800,
  "Avenida del Puerto 22, Valencia",
  "01/05/2025",
  "03/05/2025",
  -275.75
);
console.log("\n");
registrarCarga(
  450.25,
  "Plaza Cataluña 9, Barcelona",
  "20/04/2025",
  "21/04/2025",
  1,
  20
);
console.log("\n");
registrarCarga(
  920.8,
  "Camino de Ronda 78, Granada",
  "10/04/2026",
  "12/04/2025",
  312.5
);
