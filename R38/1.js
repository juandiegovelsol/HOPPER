function calcularHerencia(total, porcentajes) {
  // Sumar los porcentajes existentes
  const sumaPorcentajes = porcentajes.reduce((acc, p) => acc + p, 0);

  // Calcular el porcentaje para la quinta persona
  const porcentajeQuintaPersona = 100 - sumaPorcentajes;

  // Añadir el porcentaje de la quinta persona al arreglo
  porcentajes.push(porcentajeQuintaPersona);

  // Calcular el monto correspondiente para cada persona
  const montos = porcentajes.map((p) => (total * p) / 100);

  return {
    porcentajes,
    montos,
  };
}

// Ejemplo de uso
const totalHerencia = 6000; // Total a repartir
const porcentajesPersonas = [20, 15, 16, 25]; // Porcentajes de las primeras 4 personas

const resultado = calcularHerencia(totalHerencia, porcentajesPersonas);

console.log("Porcentajes: ", resultado.porcentajes);
console.log("Montos: ", resultado.montos);
