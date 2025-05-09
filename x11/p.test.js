const validarPuntajes = require("./p.js");

describe("Procesador de Puntajes", () => {
  it("debe procesar correctamente los puntajes de los estudiantes", () => {
    const datos = {
      Juan: [6, 7, 8],
      Maria: [9, 9, 10],
      Luis: [4, 5, 6],
    };
    const resultado = validarPuntajes(datos);
    expect(resultado).toEqual({
      aprobados: ["Juan", "Maria"],
      reprobados: ["Luis"],
      errores: [],
    });
  });

  it("debe manejar datos con errores", () => {
    const datos = {
      Juan: [6, 7.5, 8], // Puntaje decimal no válido
      Maria: [9, "N/A", 10], // Valor no numérico
      Luis: [4, 5, 6],
      "": [1, 2, 3], // Nombre de estudiante vacío
    };
    const resultado = validarPuntajes(datos);
    expect(resultado).toEqual({
      aprobados: ["Luis"],
      reprobados: [],
      errores: ["Juan", "Maria", ""],
    });
  });

  it("debe manejar entradas nulas", () => {
    const datos = null;
    expect(() => validarPuntajes(datos)).toThrow(TypeError);
  });

  it("debe manejar datos sin entradas", () => {
    const datos = {};
    const resultado = validarPuntajes(datos);
    expect(resultado).toEqual({
      aprobados: [],
      reprobados: [],
      errores: [],
    });
  });
});
