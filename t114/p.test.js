/* const validarOperacion = require("./p.js").validarOperacion; // Asegúrate de tener exportada la función desde tu archivo.

test("Caso correcto: operación válida", () => {
  const operacionValida = {
    name: "A/USD",
    entryPrice: 45000,
    exitPrice: 47000,
    quantity: 0.1,
    isLong: true,
  };
  expect(validarOperacion(operacionValida)).toBe(true);
});

test("Caso incorrecto 1: quantity menor o igual a cero", () => {
  const operacionInvalidaQuantity = {
    name: "B/USD",
    entryPrice: 3000,
    exitPrice: 2800,
    quantity: 0, // Valor incorrecto
    isLong: true,
  };
  expect(validarOperacion(operacionInvalidaQuantity)).toBe(false);
});

test("Caso incorrecto 2: falta isLong", () => {
  const operacionInvalidaSinIsLong = {
    name: "C/USD",
    entryPrice: 0.8,
    exitPrice: 0.6,
    quantity: 1000,
    // Falta la propiedad isLong
  };
  expect(validarOperacion(operacionInvalidaSinIsLong)).toBe(false);
});
 */

const validarOperacion = require("./p.js");

describe("validarOperacion", () => {
  let operacionValida;
  let operacionFaltante;
  let operacionPriceInvalido;
  let operacionCantidadInvalida;
  let operacionLongInvalido;

  beforeEach(() => {
    operacionValida = {
      name: "Test/USD",
      entryPrice: "100",
      exitPrice: "110",
      quantity: "1",
      isLong: true,
    };

    operacionFaltante = {};

    operacionPriceInvalido = {
      name: "Test/USD",
      entryPrice: "invalid",
      exitPrice: "110",
      quantity: "1",
      isLong: true,
    };

    operacionCantidadInvalida = {
      name: "Test/USD",
      entryPrice: "100",
      exitPrice: "110",
      quantity: "0",
      isLong: true,
    };

    operacionLongInvalido = {
      name: "Test/USD",
      entryPrice: "100",
      exitPrice: "110",
      quantity: "1",
      isLong: "true", // Nota: aquí en el archivo JSON estaba bool, pero en el código se evalúa como string
    };
  });

  test("debe validar una operación correcta", () => {
    expect(validarOperacion(operacionValida)).toBe(true);
  });

  test("debe invalidar operación faltante de campos", () => {
    expect(validarOperacion(operacionFaltante)).toBe(false);
  });

  test("debe invalidar operación con precio inválido", () => {
    expect(validarOperacion(operacionPriceInvalido)).toBe(false);
  });

  test("debe invalidar operación con cantidad inválida", () => {
    expect(validarOperacion(operacionCantidadInvalida)).toBe(false);
  });

  test("debe invalidar operación con isLong inválido", () => {
    expect(validarOperacion(operacionLongInvalido)).toBe(false);
  });
});
