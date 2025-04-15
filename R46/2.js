/**
 * Programa que simula el movimiento en una cuadrícula según un conjunto de instrucciones.
 * Cuenta el número de casillas visitadas al menos una vez.
 *
 * Instrucciones:
 * - '^' para mover hacia arriba
 * - 'v' para mover hacia abajo
 * - '>' para mover hacia la derecha
 * - '<' para mover hacia la izquierda
 */

// Inicializamos las instrucciones a seguir
const instrucciones = "^v^^<j<v<<gv><v".split("");

// Objeto para rastrear las casillas visitadas, usando coordenadas como claves
let visitado = {};

// Coordenadas iniciales
let x = 0;
let y = 0;

// Marcamos la posición inicial como visitada
visitado[`${x},${y}`] = true;

// Bucle que recorre cada instrucción paso a paso
let indice = 0;
while (indice < instrucciones.length) {
  const direccion = instrucciones[indice];

  switch (direccion) {
    case "^": // Mover hacia arriba
      y--;
      break;
    case "v": // Mover hacia abajo
      y++;
      break;
    case ">": // Mover hacia la derecha
      x++;
      break;
    case "<": // Mover hacia la izquierda
      x--;
      break;
    default:
      console.log("Instrucción inválida");
  }

  // Registramos la nueva posición como visitada
  visitado[`${x},${y}`] = true;

  // Pasamos a la siguiente instrucción
  indice++;
}

// Calculamos el número total de casillas visitadas al menos una vez
let visitasTotales = 0;
for (let clave in visitado) {
  if (visitado[clave]) visitasTotales++;
}

console.log(visitado);
// Mostramos el resultado final en la consola
console.log(`Casillas visitadas: ${visitasTotales}`);
