function sumaElementosLista(nueva_lista) {
  let sum = 0;
  for (let i = 0; i < nueva_lista.length; i++) {
    sum += nueva_lista[i];
  }
  return sum;
}

function insertarEnLista(nueva_lista) {
  const suma_nueva_lista = sumaElementosLista(nueva_lista);
  indice = -1;
  for (let i = 0; i < matriz1.length; i++) {
    suma_temporal = sumaElementosLista(matriz1[i]);
    if (suma_nueva_lista >= suma_temporal) {
      indice = i + 1;
    }
  }
  if (indice > -1) {
    matriz1.splice(indice, 0, nueva_lista);
  }
}

var matriz1 = [
  [0, 0],
  [1, 1],
  [1, 2],
  [2, 1],
  [2, 2],
  [3, 2],
];
//Prueba 1
insertarEnLista([1, 3]);
console.log(matriz1);
//Prueba 2
insertarEnLista([1, 2]);
console.log(matriz1);
//Prueba 3
insertarEnLista([6, 3]);
console.log(matriz1);
//Prueba 4
insertarEnLista([6, 7]);
console.log(matriz1);
