function analizarCosecha(viñedos, condicionesClima) {
  const resultados = [];

  for (const viñedo of viñedos) {
    const region = viñedo.region;
    const clima = condicionesClima[region];

    let puntuacion = 0;

    switch (viñedo.variedad) {
      case "Tempranillo":
        puntuacion = 85;
        break;
      case "Garnacha":
        puntuacion = 82;
        break;
      case "Albariño":
        puntuacion = 88;
        break;
      case "Verdejo":
        puntuacion = 84;
        break;
      default:
        puntuacion = 80;
    }

    if (clima.temperaturaMedia >= 14 && clima.temperaturaMedia <= 16) {
      puntuacion += 8;
    } else if (clima.temperaturaMedia > 16 && clima.temperaturaMedia <= 18) {
      puntuacion += 5;
    } else if (clima.temperaturaMedia > 18 && clima.temperaturaMedia <= 20) {
      puntuacion += 2;
    } else if (clima.temperaturaMedia < 14) {
      puntuacion -= 3;
    }

    if (clima.precipitacionAnual >= 400 && clima.precipitacionAnual <= 600) {
      puntuacion += 6;
    } else if (
      clima.precipitacionAnual > 600 &&
      clima.precipitacionAnual <= 800
    ) {
      puntuacion += 2;
    } else if (
      clima.precipitacionAnual < 400 &&
      clima.precipitacionAnual >= 300
    ) {
      puntuacion -= 2;
    } else if (
      clima.precipitacionAnual < 300 ||
      clima.precipitacionAnual > 800
    ) {
      puntuacion -= 5;
    }

    puntuacion += Math.floor(clima.horasSolAnuales / 100);

    let denominacion;
    if (puntuacion >= 100) {
      denominacion = "Gran Reserva";
    } else if (puntuacion >= 90) {
      denominacion = "Reserva";
    } else if (puntuacion >= 85) {
      denominacion = "Crianza";
    } else if (puntuacion >= 80) {
      denominacion = "Joven";
    } else {
      denominacion = "Mesa";
    }

    resultados.push({
      viñedo: viñedo.nombre,
      puntuacion: puntuacion,
      denominacion: denominacion,
    });
  }

  return resultados;
}

const viñedos = [
  { nombre: "Viña del Sol", region: "Rioja", variedad: "Tempranillo" },
  { nombre: "Bodegas Atlántico", region: "Galicia", variedad: "Albariño" },
  {
    nombre: "Viñedos Castellanos",
    region: "Castilla La Mancha",
    variedad: "Garnacha",
  },
  {
    nombre: "Cepas del Duero",
    region: "Ribera Del Duero",
    variedad: "Tempranillo",
  },
  { nombre: "Bodegas Levante", region: "Valencia", variedad: "Monastrell" },
];

const condicionesClima = {
  Rioja: {
    temperaturaMedia: 15.5,
    precipitacionAnual: 450,
    horasSolAnuales: 2200,
  },
  Galicia: {
    temperaturaMedia: 13.2,
    precipitacionAnual: 900,
    horasSolAnuales: 1800,
  },
  "Castilla La Mancha": {
    temperaturaMedia: 17.8,
    precipitacionAnual: 320,
    horasSolAnuales: 2600,
  },
  "Ribera Del Duero": {
    temperaturaMedia: 14.2,
    precipitacionAnual: 490,
    horasSolAnuales: 2100,
  },
  Valencia: {
    temperaturaMedia: 19.5,
    precipitacionAnual: 280,
    horasSolAnuales: 2800,
  },
};

// Casos de prueba

console.log(
  JSON.stringify(analizarCosecha([viñedos[0]], condicionesClima), null, 2)
);
console.log(
  JSON.stringify(analizarCosecha([viñedos[1]], condicionesClima), null, 2)
);
console.log(
  JSON.stringify(analizarCosecha([viñedos[2]], condicionesClima), null, 2)
);
console.log(
  JSON.stringify(analizarCosecha([viñedos[3]], condicionesClima), null, 2)
);
console.log(
  JSON.stringify(analizarCosecha([viñedos[4]], condicionesClima), null, 2)
);
console.log(
  JSON.stringify(analizarCosecha(viñedos, condicionesClima), null, 2)
);
