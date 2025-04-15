const instrucciones = "^^<j<v<<gv><v".split("");

let visitado = {};
let [x, y] = [0, 0];

visitado[`${x},${y}`] = 1;

for (let direccion of instrucciones) {
  if (direccion === "^") y--;
  else if (direccion === "v") y++;
  else if (direccion === ">") x++;
  else if (direccion === "<") x--;
  else console.log("Dirección inválida");

  visitado[`${x},${y}`] = 1;
}

let visitasTotales = Object.values(visitado).reduce((a, b) => a + b, 0);

console.log(visitado);
console.log(`Casillas visitadas: ${visitasTotales}`);
