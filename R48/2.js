function filtrarExperimentos(datos) {
  const experimentos = new Map();

  // Almacena los eventos en el mapa, organizados por ID
  datos.forEach(({ fechaHora, tipo_evento, id }) => {
    if (!experimentos.has(id)) {
      experimentos.set(id, []);
    }
    experimentos.get(id).push({ fechaHora: new Date(fechaHora), tipo_evento });
  });

  const resultado = [];

  // Recorre los eventos para filtrar las expiraciones
  experimentos.forEach((eventos, id) => {
    eventos.sort((a, b) => a.fechaHora - b.fechaHora);

    // Calcula la duración de la expiración
    const duracionDias =
      (eventos[eventos.length - 1].fechaHora - eventos[0].fechaHora) /
      (1000 * 60 * 60 * 24);
    if (duracionDias <= 100) return;

    // Encuentra el índice del último evento tipo 5
    let ultimoIndice = eventos.length - 1;
    while (ultimoIndice >= 0 && eventos[ultimoIndice].tipo_evento !== 5) {
      ultimoIndice--;
    }
    if (ultimoIndice === -1) return;

    // Asegura que la secuencia final de eventos se complete en un día
    const secuenciaFinal = eventos.slice(ultimoIndice);
    const tiempoInicioFinal = secuenciaFinal[0].fechaHora;
    const tiempoFinFinal = secuenciaFinal[secuenciaFinal.length - 1].fechaHora;
    const duracionSecuenciaFinalDias =
      (tiempoFinFinal - tiempoInicioFinal) / (1000 * 60 * 60 * 24);
    if (duracionSecuenciaFinalDias > 1) return;

    // Verifica que los eventos restantes sean tipo 0 o un evento tipo 1 seguido de solo tipo 0
    const antesDeSecuenciaFinal = eventos.slice(0, ultimoIndice + 1);
    let valido = antesDeSecuenciaFinal.every(
      (evento) => evento.tipo_evento === 0
    );
    if (!valido) {
      const indicePrimerUno = antesDeSecuenciaFinal.findIndex(
        (evento) => evento.tipo_evento === 1
      );
      if (indicePrimerUno !== -1) {
        valido = antesDeSecuenciaFinal
          .slice(indicePrimerUno + 1)
          .every((evento) => evento.tipo_evento === 0);
      } else {
        valido = false;
      }
    }

    if (valido) resultado.push(id);
  });

  return resultado;
}

const datos = [
  { fechaHora: "2025-01-01T08:00:00Z", tipo_evento: 0, id: 1 },
  { fechaHora: "2025-01-10T09:00:00Z", tipo_evento: 2, id: 1 },
  { fechaHora: "2025-02-15T10:00:00Z", tipo_evento: 3, id: 1 },
  { fechaHora: "2025-05-01T11:00:00Z", tipo_evento: 5, id: 1 }, // Finaliza dentro de los 100 días
  { fechaHora: "2025-01-05T08:30:00Z", tipo_evento: 0, id: 2 },
  { fechaHora: "2025-06-15T09:45:00Z", tipo_evento: 1, id: 2 },
  { fechaHora: "2025-06-16T10:15:00Z", tipo_evento: 0, id: 2 },
  { fechaHora: "2025-06-17T11:30:00Z", tipo_evento: 5, id: 2 }, // Duración válida y tipo_evento correcto
  { fechaHora: "2025-03-01T07:15:00Z", tipo_evento: 0, id: 3 },
  { fechaHora: "2025-03-02T08:20:00Z", tipo_evento: 1, id: 3 },
  { fechaHora: "2025-03-03T09:25:00Z", tipo_evento: 2, id: 3 },
  { fechaHora: "2025-03-04T10:30:00Z", tipo_evento: 5, id: 3 }, // Se descarta por no cumplir duración
  { fechaHora: "2025-01-01T06:10:00Z", tipo_evento: 0, id: 4 },
  { fechaHora: "2025-07-01T07:15:00Z", tipo_evento: 5, id: 4 }, // Excede los 100 días
  { fechaHora: "2025-02-20T06:30:00Z", tipo_evento: 0, id: 5 },
  { fechaHora: "2025-06-30T07:45:00Z", tipo_evento: 0, id: 5 },
  { fechaHora: "2025-07-01T08:00:00Z", tipo_evento: 1, id: 5 },
  { fechaHora: "2025-07-02T08:30:00Z", tipo_evento: 0, id: 5 },
  { fechaHora: "2025-07-03T09:00:00Z", tipo_evento: 5, id: 5 }, // Cumple condiciones
];

console.log(filtrarExperimentos(datos));
