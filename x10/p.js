var matriz1 = [
  [0, 0],
  [1, 1],
  [1, 2],
  [2, 1],
  [2, 2],
  [3, 2],
];

//Sumar los elementos de la lista
function sumaElementosLista(nueva_lista) {
  let sum = 0;
  for (let i = 0; i < nueva_lista.length; i++) {
    //Sumando elementos de la lista
    sum += nueva_lista[i];
  }
  return sum;
}

//Insertar la lista en la matriz en orden ascendente
function insertarEnLista(nueva_lista) {
  //Obteniendo el total de la nueva lista
  const suma_nueva_lista = sumaElementosLista(nueva_lista);
  //Esta variable indicara en donde debe insertarse la nueva lista en la matriz
  indice = -1;
  for (let i = 0; i < matriz1.length; i++) {
    //Obteniendo la suma de cada lista de la matriz
    suma_temporal = sumaElementosLista(matriz1[i]);
    //Validando si la nueva lista es mayor que alguna en la matriz
    console.log(suma_nueva_lista, suma_temporal, i);
    if (suma_nueva_lista >= suma_temporal) {
      //Se captura el indice donde se debe insertar la nueva lista

      indice = i;
    }
  }
  console.log(indice);
  if (indice > -1) {
    //Se inserta la lista en la matriz
    matriz1.splice(indice, 0, nueva_lista);
  }
}

console.log("Antes:", matriz1);
insertarEnLista([0, 1]); // Suma: 1
console.log("Después:", matriz1);
