const clasificarCalificaciones = require("./clasificar");

describe("clasificarCalificaciones", () => {
  let notaMaxima;

  beforeEach(() => {
    notaMaxima = 10;
  });

  const datosValidos = {
    Ana: [9, 8, 9],
    Luis: [7, 6, 7],
    Maria: [5, 5, 5],
    Juan: [10, 9, 10],
  };

  const datosParcialmenteValidos = {
    Ana: [9, 8, 9],
    Luis: [7, "seis", 7], // Error: una nota no es un número
    Maria: [5, 5, 5],
    Juan: [10, 9, 10],
    Carmen: [], // Error: no hay notas
  };

  const datosInvalidos = {
    Carlos: [11, 5, 9], // Error: una nota es mayor que la nota máxima
    Ana: [], // Error: no hay notas
    Roberto: [-1, 7, 8], // Error: una nota es negativa
  };

  test("debe clasificar correctamente cuando todos los registros son válidos", () => {
    const resultado = clasificarCalificaciones(datosValidos, notaMaxima);

    expect(resultado).toEqual({
      sobresalientes: ["Juan"],
      notables: ["Ana"],
      aprobados: ["Luis", "Maria"],
      suspensos: [],
      errores: [],
    });
  });

  test("debe manejar errores y clasificar notas cuando hay registros con errores", () => {
    const resultado = clasificarCalificaciones(
      datosParcialmenteValidos,
      notaMaxima
    );

    expect(resultado).toEqual({
      sobresalientes: ["Juan"],
      notables: ["Ana"],
      aprobados: ["Maria"],
      suspensos: [],
      errores: ["Luis", "Carmen"], // Errores: Luis (nota no número), Carmen (sin notas)
    });
  });

  test("debe devolver solo errores cuando todos los registros son inválidos", () => {
    const resultado = clasificarCalificaciones(datosInvalidos, notaMaxima);

    expect(resultado).toEqual({
      sobresalientes: [],
      notables: [],
      aprobados: [],
      suspensos: [],
      errores: ["Carlos", "Ana", "Roberto"],
    });
  });
});
