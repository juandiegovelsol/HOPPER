const fs = require("fs");

const calcularEstadisticasLiga = (rutaArchivoJSON) => {
  try {
    // Leer el archivo JSON como un objeto
    const datos = JSON.parse(fs.readFileSync(rutaArchivoJSON, "utf8"));

    // Validar la estructura y tipos de datos del JSON
    datos.forEach((partido) => {
      const { equipoLocal, golesLocal, equipoVisitante, golesVisitante } =
        partido;

      if (
        typeof equipoLocal !== "string" ||
        typeof golesLocal !== "number" ||
        typeof equipoVisitante !== "string" ||
        typeof golesVisitante !== "number"
      ) {
        throw new Error("Datos del partido inválidos.");
      }
    });

    // Inicializar estadísticas de equipos
    const estadisticas = {};

    datos.forEach((partido) => {
      const { equipoLocal, golesLocal, equipoVisitante, golesVisitante } =
        partido;

      // Inicializar equipos si no existen en el objeto de estadísticas
      if (!estadisticas[equipoLocal]) {
        estadisticas[equipoLocal] = {
          partidosGanados: 0,
          golesAFavor: 0,
          golesEnContra: 0,
          partidosEmpatados: 0,
          partidosPerdidos: 0,
        };
      }
      if (!estadisticas[equipoVisitante]) {
        estadisticas[equipoVisitante] = {
          partidosGanados: 0,
          golesAFavor: 0,
          golesEnContra: 0,
          partidosEmpatados: 0,
          partidosPerdidos: 0,
        };
      }

      // Actualizar estadísticas de acuerdo al resultado del partido
      if (golesLocal > golesVisitante) {
        estadisticas[equipoLocal].partidosGanados++;
        estadisticas[equipoLocal].golesAFavor += golesLocal;
        estadisticas[equipoLocal].golesEnContra += golesVisitante;
        estadisticas[equipoVisitante].golesEnContra += golesLocal;
        estadisticas[equipoVisitante].golesAFavor += golesVisitante;
      } else if (golesLocal < golesVisitante) {
        estadisticas[equipoVisitante].partidosGanados++;
        estadisticas[equipoVisitante].golesAFavor += golesVisitante;
        estadisticas[equipoVisitante].golesEnContra += golesLocal;
        estadisticas[equipoLocal].golesEnContra += golesVisitante;
        estadisticas[equipoLocal].golesAFavor += golesLocal;
      } else {
        estadisticas[equipoLocal].partidosEmpatados++;
        estadisticas[equipoVisitante].partidosEmpatados++;
        estadisticas[equipoLocal].golesAFavor += golesLocal;
        estadisticas[equipoLocal].golesEnContra += golesVisitante;
        estadisticas[equipoVisitante].golesAFavor += golesVisitante;
        estadisticas[equipoVisitante].golesEnContra += golesLocal;
      }
    });

    // Determinar el equipo ganador de la liga
    let equipoGanador = null;
    let puntosMaximos = -1;
    let partidosGanadosMaximos = -1;

    for (const equipo in estadisticas) {
      const stats = estadisticas[equipo];
      const puntos = stats.partidosGanados * 3 + stats.partidosEmpatados;
      if (
        puntos > puntosMaximos ||
        (puntos === puntosMaximos &&
          stats.partidosGanados > partidosGanadosMaximos)
      ) {
        equipoGanador = equipo;
        puntosMaximos = puntos;
        partidosGanadosMaximos = stats.partidosGanados;
      }
    }

    if (!equipoGanador) {
      throw new Error("No se pudo determinar el equipo ganador.");
    }

    // Imprimir estadísticas del equipo ganador
    const statsGanador = estadisticas[equipoGanador];
    console.log(`Estadísticas del equipo ganador: ${equipoGanador}`);
    console.log(`Partidos ganados: ${statsGanador.partidosGanados}`);
    console.log(`Goles a favor: ${statsGanador.golesAFavor}`);
    console.log(`Goles en contra: ${statsGanador.golesEnContra}`);
    console.log(`Partidos empatados: ${statsGanador.partidosEmpatados}`);
    console.log(`Partidos perdidos: ${statsGanador.partidosPerdidos}`);
  } catch (error) {
    console.error("Error al calcular las estadísticas:", error.message);
  }
};

// Ruta al archivo JSON que contiene los datos de los partidos
const rutaArchivoJSON = "partidos.json";

// Llamar a la función con la ruta del archivo JSON
calcularEstadisticasLiga(rutaArchivoJSON);

module.exports = calcularEstadisticasLiga;
