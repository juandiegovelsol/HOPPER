function evaluarColmena(
  hiveName,
  daysSinceLastHarvest,
  dailyHoneyYield,
  harvestThreshold,
  healthIndex,
  environmentFactor
) {
  if (typeof hiveName !== "string" || hiveName.trim() === "") {
    return "Error: El nombre de la colmena debe ser una cadena no vacía.";
  }
  if (
    typeof daysSinceLastHarvest !== "number" ||
    isNaN(daysSinceLastHarvest) ||
    daysSinceLastHarvest < 0
  ) {
    return "Error: Los días transcurridos deben ser un número no negativo.";
  }
  if (
    typeof dailyHoneyYield !== "number" ||
    isNaN(dailyHoneyYield) ||
    dailyHoneyYield <= 0
  ) {
    return "Error: El rendimiento diario debe ser un número positivo.";
  }
  if (
    typeof harvestThreshold !== "number" ||
    isNaN(harvestThreshold) ||
    harvestThreshold <= 0
  ) {
    return "Error: El umbral de cosecha debe ser un número positivo.";
  }
  if (
    typeof healthIndex !== "number" ||
    isNaN(healthIndex) ||
    healthIndex < 0 ||
    healthIndex > 100
  ) {
    return "Error: El índice de salud debe ser un número entre 0 y 100.";
  }
  if (
    typeof environmentFactor !== "number" ||
    isNaN(environmentFactor) ||
    environmentFactor <= 0
  ) {
    return "Error: El factor ambiental debe ser un número positivo.";
  }

  // Cálculo simplificado de la producción
  let currentYield =
    dailyHoneyYield *
    daysSinceLastHarvest *
    (healthIndex / 100) *
    environmentFactor;
  let futureYield =
    dailyHoneyYield *
    harvestThreshold *
    (healthIndex / 100) *
    environmentFactor;

  let mensaje = "";
  if (daysSinceLastHarvest >= harvestThreshold) {
    mensaje += "La colmena '" + hiveName + "' está lista para cosechar.\n";
    mensaje +=
      "Producción estimada: " + currentYield.toFixed(2) + " libras de miel.";
  } else {
    let daysRemaining = harvestThreshold - daysSinceLastHarvest;
    mensaje += "La colmena '" + hiveName + "' NO está lista para cosechar.\n";
    mensaje += "Faltan " + daysRemaining + " día(s).\n";
    mensaje +=
      "Producción actual: " + currentYield.toFixed(2) + " libras de miel.\n";
    mensaje +=
      "Proyección a " +
      harvestThreshold +
      " días: " +
      futureYield.toFixed(2) +
      " libras.";
  }

  return mensaje;
}

console.log(evaluarColmena("Colmena A", 12, 2.5, 10, 90, 1.2), "\n");
console.log(evaluarColmena("Colmena B", 5, 2.0, 10, 80, 1.0), "\n");
console.log(evaluarColmena("Colmena C", 10, 1.8, 10, 100, 1.5), "\n");
console.log(evaluarColmena("Colmena D", 8, 3.0, 12, 70, 0.9), "\n");
