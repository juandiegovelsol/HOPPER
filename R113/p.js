const indicadoresCrimen = {
  "Nivel de crimen": 88.68,
  "Crimen aumentando en los últimos 5 años": 86.53,
  "Preocupación por robo en casa": 82.76,
  "Preocupación por ser asaltado o robado": 82.89,
  "Preocupación por robo de coche": 80.53,
  "Preocupación por robo dentro del coche": 79.51,
  "Preocupación por ser atacado": 76.64,
  "Preocupación por ser insultado": 62.07,
  "Preocupación por ataque físico debido a discriminación": 62.67,
  "Problemas con uso o venta de drogas": 73.7,
  "Problemas con crímenes contra la propiedad": 82.31,
  "Problemas con crímenes violentos": 87.3,
  "Problemas con corrupción y soborno": 91.33,
};

let sumaTotal = 0;
let cantidadIndicadores = 0;
for (const clave in indicadoresCrimen) {
  if (Object.hasOwnProperty.call(indicadoresCrimen, clave)) {
    sumaTotal += indicadoresCrimen[clave];
    cantidadIndicadores += 1;
  }
}

const indiceCrimenActual = sumaTotal / cantidadIndicadores;
console.log(
  `Índice actual de criminalidad (2024): ${indiceCrimenActual.toFixed(2)}`
);

const valoresSimuladosUltimos5Años = [81.2, 82.1, 83.7, 85.0, 86.8];

function calcularProyeccionConEWMA(datos, alpha, añosFuturos) {
  const resultados = {};
  let valorAnterior = datos[datos.length - 1];
  for (let i = 1; i <= añosFuturos; i++) {
    console.log(i);
    const nuevoValor =
      alpha * valorAnterior + (1 - alpha) * datos[datos.length - 1];
    resultados[2024 + i] = nuevoValor;
    datos.push(nuevoValor);
    valorAnterior = nuevoValor;
  }
  return resultados;
}

const alpha = 0.6;
const proyeccionesFuturas = calcularProyeccionConEWMA(
  [...valoresSimuladosUltimos5Años],
  alpha,
  10
);

console.log(
  `\nProyección estimada del índice de criminalidad para Los Ángeles (2025–2029):`
);
for (let año = 2025; año <= 2034; año++) {
  const indice = proyeccionesFuturas[año];
  let severidad = "";

  if (indice < 40) {
    severidad = "Bajo";
  } else if (indice >= 40 && indice < 60) {
    severidad = "Moderado";
  } else if (indice >= 60 && indice < 80) {
    severidad = "Alto";
  } else {
    severidad = "Muy Alto";
  }

  console.log(`${año}: ${indice.toFixed(2)} (${severidad})`);
}
