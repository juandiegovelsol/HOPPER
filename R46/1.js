// Ejercicio: Contar casillas visitadas en una cuadrícula

// Definimos las instrucciones como un array de caracteres
const instrucciones = "^v^^<j<v<<gv><v".split("");

// Objeto para guardar las posiciones visitadas, con coordenadas como claves
let visitado = {};

// Coordenadas iniciales en la cuadrícula
let x = 0;
let y = 0;

// Marcamos la posición inicial como visitada
visitado[`${x},${y}`] = 1;

// Recorrer cada instrucción en el array
for (let i = 0; i < instrucciones.length; i++) {
  const direccion = instrucciones[i];

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
      console.log("Dirección inválida"); // Mensaje en caso de instrucción desconocida
  }

  // Guardar la nueva posición en el objeto visitado
  // Usamos coordenadas como clave única para cada posición
  visitado[`${x},${y}`] = 1;
}

// Calcular el número total de casillas visitadas
// Usamos reduce para contar los valores en el objeto visitado
let visitasTotales = Object.values(visitado).reduce((a, b) => a + b, 0);
console.log(visitado);
// Imprimir el resultado final
console.log(`Casillas visitadas: ${visitasTotales}`);
