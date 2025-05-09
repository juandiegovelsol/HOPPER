const fs = require("fs");
const path = require("path");
const calcularEstadisticasLiga = require("./ganadorLiga.js"); // Verifica que el módulo está siendo exportado en el archivo original

describe("calcularEstadisticasLiga", () => {
  let rutaArchivoJSON;
  let consoleSpy;
  let consoleErrorSpy;

  beforeEach(() => {
    rutaArchivoJSON = path.join(__dirname, "partidos.json");
    fs.writeFileSync(rutaArchivoJSON, ""); // Inicializa el archivo JSON antes de cada prueba

    // Espía la salida de console.log y console.error antes de cada prueba
    consoleSpy = jest.spyOn(console, "log").mockImplementation();
    consoleErrorSpy = jest.spyOn(console, "error").mockImplementation();
  });

  afterEach(() => {
    fs.unlinkSync(rutaArchivoJSON); // Elimina el archivo JSON después de cada prueba
    consoleSpy.mockRestore(); // Restaura console.log después de cada prueba
    consoleErrorSpy.mockRestore(); // Restaura console.error después de cada prueba
  });

  test("Datos correctos - Determina el equipo ganador correctamente", () => {
    const datosPartidos = [
      {
        equipoLocal: "Real Madrid",
        golesLocal: 3,
        equipoVisitante: "Barcelona",
        golesVisitante: 1,
      },
      {
        equipoLocal: "Real Madrid",
        golesLocal: 2,
        equipoVisitante: "Atletico",
        golesVisitante: 2,
      },
      {
        equipoLocal: "Barcelona",
        golesLocal: 2,
        equipoVisitante: "Atletico",
        golesVisitante: 0,
      },
    ];
    fs.writeFileSync(rutaArchivoJSON, JSON.stringify(datosPartidos));

    calcularEstadisticasLiga(rutaArchivoJSON);

    // Verifica que se llamó a console.log con los valores esperados (línea por línea)
    expect(consoleSpy).toHaveBeenNthCalledWith(
      1,
      "Estadísticas del equipo ganador: Real Madrid"
    );
    expect(consoleSpy).toHaveBeenNthCalledWith(2, "Partidos ganados: 1");
    expect(consoleSpy).toHaveBeenNthCalledWith(3, "Goles a favor: 5");
    expect(consoleSpy).toHaveBeenNthCalledWith(4, "Goles en contra: 3");
    expect(consoleSpy).toHaveBeenNthCalledWith(5, "Partidos empatados: 1");
    expect(consoleSpy).toHaveBeenNthCalledWith(6, "Partidos perdidos: 0");
  });

  test("Datos correctos - Determina el equipo ganador con empates", () => {
    const datosPartidos = [
      {
        equipoLocal: "Real Madrid",
        golesLocal: 1,
        equipoVisitante: "Barcelona",
        golesVisitante: 1,
      },
      {
        equipoLocal: "Real Madrid",
        golesLocal: 0,
        equipoVisitante: "Atletico",
        golesVisitante: 0,
      },
      {
        equipoLocal: "Barcelona",
        golesLocal: 1,
        equipoVisitante: "Atletico",
        golesVisitante: 1,
      },
    ];
    fs.writeFileSync(rutaArchivoJSON, JSON.stringify(datosPartidos));

    calcularEstadisticasLiga(rutaArchivoJSON);

    // Verifica que se llamó a console.log con los valores esperados (línea por línea)
    expect(consoleSpy).toHaveBeenNthCalledWith(
      1,
      "Estadísticas del equipo ganador: Real Madrid"
    );
    expect(consoleSpy).toHaveBeenNthCalledWith(2, "Partidos ganados: 0");
    expect(consoleSpy).toHaveBeenNthCalledWith(3, "Goles a favor: 1");
    expect(consoleSpy).toHaveBeenNthCalledWith(4, "Goles en contra: 1");
    expect(consoleSpy).toHaveBeenNthCalledWith(5, "Partidos empatados: 2");
    expect(consoleSpy).toHaveBeenNthCalledWith(6, "Partidos perdidos: 0");
  });

  test("Datos inválidos - Maneja errores en los datos del JSON", () => {
    const datosPartidos = [
      {
        equipoLocal: "Real Madrid",
        golesLocal: "tres",
        equipoVisitante: "Barcelona",
        golesVisitante: 1,
      },
    ];
    fs.writeFileSync(rutaArchivoJSON, JSON.stringify(datosPartidos));

    calcularEstadisticasLiga(rutaArchivoJSON);

    // Solo verificamos que se imprimió el mensaje de error en consola
    expect(consoleErrorSpy).toHaveBeenCalledWith(
      "Error al calcular las estadísticas:",
      "Datos del partido inválidos."
    );
  });
});
