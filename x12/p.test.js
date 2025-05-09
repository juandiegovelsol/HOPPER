const clasificarAsistencia = require("./rutaAlArchivoDelaFunción"); // Asegúrate de ajustar la ruta

describe("clasificarAsistencia", () => {
  // Prueba 1: Todos los datos son correctos
  test("Clasifica correctamente cuando todos los datos son válidos", () => {
    const empleados = {
      Juan: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], // 10 días
      Maria: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], // 15 días
      Pedro: [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
      ], // 20 días
    };

    const resultado = clasificarAsistencia(empleados);

    expect(resultado.puntuales).toEqual(["Pedro"]); // 100% asistencia
    expect(resultado.regulares).toEqual(["Juan", "Maria"]); // Juan y Maria tienen 50% y 75% respectivamente
    expect(resultado.absentistas).toEqual([]); // No hay absentistas
    expect(resultado.errores).toEqual([]); // No hay errores
  });

  // Prueba 2: Algunos datos son incorrectos
  test("Registra errores y clasifica cuando algunos datos son inválidos", () => {
    const empleados = {
      Juan: [1, 2, 3, 4, 5, 6, 7, 32], // 8 días, uno inválido
      Maria: [], // 0 días
      Pedro: [1, 2, 3, 4, 5, 6, "siete"], // 6 días, uno no numérico
    };

    const resultado = clasificarAsistencia(empleados);

    expect(resultado.puntuales).toEqual([]); // Ninguno puntual
    expect(resultado.regulares).toEqual([]); // Ninguno regular
    expect(resultado.absentistas).toEqual([]); // Ninguno absentista
    expect(resultado.errores).toEqual(["Juan", "Maria", "Pedro"]); // Todos tienen errores
  });

  // Prueba 3: Todos los datos son incorrectos
  test("Todos los empleados tienen datos inválidos y se registra en errores", () => {
    const empleados = {
      Juan: [],
      Maria: ["uno", "dos", "tres"], // datos inválidos
      Pedro: [-1, 0, 32], // todos inválidos
    };

    const resultado = clasificarAsistencia(empleados);

    expect(resultado.puntuales).toEqual([]); // Ninguno puntual
    expect(resultado.regulares).toEqual([]); // Ninguno regular
    expect(resultado.absentistas).toEqual([]); // Ninguno absentista
    expect(resultado.errores).toEqual(["Juan", "Maria", "Pedro"]); // Todos son errores
  });
});
