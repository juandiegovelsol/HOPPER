class GrowthAnalyzer {
  constructor() {
    this.errors = [];
  }

  validateRecord(record) {
    if (!record || typeof record !== "object") {
      return "Record must be an object";
    }
    if (
      typeof record.startValue !== "number" ||
      typeof record.endValue !== "number"
    ) {
      return "Start and End values must be numbers";
    }
    if (record.startValue <= 0) {
      return "Start value must be greater than zero";
    }
    if (record.endValue < 0) {
      return "End value cannot be negative";
    }
    return null;
  }

  calculateCAGR(startValue, endValue, periods) {
    if (periods <= 0) {
      throw new Error("Periods must be greater than zero");
    }
    const cagr = Math.pow(endValue / startValue, 1 / periods) - 1;
    return parseFloat((cagr * 100).toFixed(2));
  }

  processRecords(records) {
    if (!Array.isArray(records)) {
      throw new TypeError("Input must be an array of records");
    }

    const results = [];

    records.forEach((record, index) => {
      const validationError = this.validateRecord(record);
      if (validationError) {
        this.errors.push({ index, error: validationError });
        return;
      }

      try {
        const periods = record.periods || 1;
        const growth = this.calculateCAGR(
          record.startValue,
          record.endValue,
          periods
        );
        results.push({ index, growth });
      } catch (error) {
        this.errors.push({ index, error: error.message });
      }
    });

    return {
      results,
      errors: this.errors,
    };
  }
}

module.exports = GrowthAnalyzer;

// Crear una instancia
const analyzer = new GrowthAnalyzer();

// Caso 1: Datos válidos simples
const records1 = [
  { startValue: 100, endValue: 200, periods: 3 }, // 26% CAGR
  { startValue: 50, endValue: 150, periods: 5 }, // 24.57% CAGR
];

const result1 = analyzer.processRecords(records1);
console.log("Caso 1: Datos válidos simples");
console.log(JSON.stringify(result1, null, 2));

// Caso 2: Mezcla de registros válidos e inválidos
const records2 = [
  { startValue: 100, endValue: 300, periods: 4 },
  { startValue: 0, endValue: 100, periods: 2 }, // startValue inválido
  { startValue: 100, endValue: -50, periods: 1 }, // endValue inválido
  { startValue: 80, endValue: 160 }, // periods no especificado (debería tomar 1 por defecto)
];

const analyzer2 = new GrowthAnalyzer(); // Nueva instancia para limpiar errores anteriores
const result2 = analyzer2.processRecords(records2);
console.log("\nCaso 2: Mezcla de válidos e inválidos");
console.log(JSON.stringify(result2, null, 2));

// Caso 3: Input no es un array
try {
  const invalidInput = { startValue: 100, endValue: 200 };
  const result3 = analyzer.processRecords(invalidInput);
} catch (error) {
  console.log("\nCaso 3: Input no es un array");
  console.error(error.message);
}

// Caso 4: Periods igual o menor a cero
const records4 = [
  { startValue: 100, endValue: 120, periods: 0 }, // periods inválido
];

const analyzer4 = new GrowthAnalyzer();
const result4 = analyzer4.processRecords(records4);
console.log("\nCaso 4: Periods inválido (0)");
console.log(JSON.stringify(result4, null, 2));

// Caso 5: Record no es un objeto
const records5 = [
  null,
  123,
  "invalid",
  { startValue: 100, endValue: 120, periods: 2 }, // válido
];

const analyzer5 = new GrowthAnalyzer();
const result5 = analyzer5.processRecords(records5);
console.log("\nCaso 5: Record no es un objeto");
console.log(JSON.stringify(result5, null, 2));

// Caso 6: Valores extremos
const records6 = [
  { startValue: 1, endValue: 1000000, periods: 10 }, // Crecimiento altísimo
  { startValue: 50000, endValue: 50000, periods: 5 }, // Sin crecimiento
];

const analyzer6 = new GrowthAnalyzer();
const result6 = analyzer6.processRecords(records6);
console.log("\nCaso 6: Valores extremos");
console.log(JSON.stringify(result6, null, 2));
