function calcularHerencia(totalMonto, porcentajes) {
  // Verifica que la suma de los porcentajes sea 100
  let sumaPorcentajes = porcentajes.reduce(
    (acumulador, porcentaje) => acumulador + porcentaje,
    0
  );
  if (sumaPorcentajes !== 100) {
    throw new Error("La suma de los porcentajes debe ser 100.");
  }

  let montos = {};
  let cantidadRestante = totalMonto;

  porcentajes.forEach((porcentaje, index) => {
    let montoIndividual = (porcentaje / 100) * totalMonto;
    montos[`persona${index + 1}`] = montoIndividual.toFixed(2);
    cantidadRestante -= montoIndividual;
  });

  // Asignar el resto a la última persona
  montos["persona5"] += cantidadRestante.toFixed(2);

  return montos;
}

// Ejemplo de uso:
let totalHerencia = 5000;
let porcentajes = [20, 15, 16, 25];

try {
  let resultado = calcularHerencia(totalHerencia, porcentajes);
  console.log(resultado);
} catch (error) {
  console.error(error.message);
}
