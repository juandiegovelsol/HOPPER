function tiempoDesdeFecha(fechaInput) {
  // Convertir la fecha de entrada a un objeto Date
  const [dia, mes, anio, hora, minuto] = fechaInput.split("-").map(Number);
  const fechaObjetivo = new Date(
    Date.UTC(anio, mes - 1, dia, hora + 3, minuto)
  ); // Ajuste de horario a UTC-3 (hora de Chile)

  const ahora = new Date();
  const diferenciaMs = fechaObjetivo - ahora;

  const diferenciaSegundos = Math.floor(diferenciaMs / 1000);
  const diferenciaMinutos = Math.floor(diferenciaSegundos / 60);
  const diferenciaHoras = Math.floor(diferenciaMinutos / 60);
  const diferenciaDias = Math.floor(diferenciaHoras / 24);

  if (diferenciaMs > 0) {
    // La fecha está en el futuro
    if (diferenciaDias > 0) {
      return `Faltan ${diferenciaDias} días para la fecha.`;
    } else if (diferenciaHoras > 0) {
      return `Faltan ${diferenciaHoras} horas para la fecha.`;
    } else if (diferenciaMinutos > 0) {
      return `Faltan ${diferenciaMinutos} minutos para la fecha.`;
    } else {
      return `Faltan unos segundos para la fecha.`;
    }
  } else {
    // La fecha está en el pasado
    const diferenciaNegativa = -diferenciaMs;
    const diferenciaNegativaSegundos = Math.floor(diferenciaNegativa / 1000);
    const diferenciaNegativaMinutos = Math.floor(
      diferenciaNegativaSegundos / 60
    );
    const diferenciaNegativaHoras = Math.floor(diferenciaNegativaMinutos / 60);
    const diferenciaNegativaDias = Math.floor(diferenciaNegativaHoras / 24);

    if (diferenciaNegativaDias > 0) {
      return `Fue hace ${diferenciaNegativaDias} días.`;
    } else if (diferenciaNegativaHoras > 0) {
      return `Fue hace ${diferenciaNegativaHoras} horas.`;
    } else if (diferenciaNegativaMinutos > 0) {
      return `Fue hace ${diferenciaNegativaMinutos} minutos.`;
    } else {
      return `Fue hace unos segundos.`;
    }
  }
}

// Ejemplo de uso:
console.log(tiempoDesdeFecha("12-10-2023-15-30")); // Cambia la fecha según necesites
// Ejemplo de uso:
console.log(tiempoDesdeFecha("30-04-2025-23-00")); // Cambia la fecha según necesites
