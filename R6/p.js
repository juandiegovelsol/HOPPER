function calcularLanzamientoJabalina(fuerza, angulo) {
  let rad = (angulo * Math.PI) / 180;
  let distancia = Math.round(fuerza * rad * 1.5);
  let direccion = Math.round(angulo + rad * 5);

  return { distancia, direccion };
}

console.log("Caso 1:", calcularLanzamientoJabalina(30, 15));
console.log("Caso 2:", calcularLanzamientoJabalina(55, 20));
console.log("Caso 3:", calcularLanzamientoJabalina(70, 25));
