const fs = require("fs");
const InventarioValidator = require("./p.js");

// Espia para consola
const consoleLogSpy = jest.spyOn(console, "log");
const consoleErrorSpy = jest.spyOn(console, "error");

describe("InventarioValidator", () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  test("Carga de inventario con datos correctos", () => {
    const inventarioCorrecto = JSON.stringify([
      {
        nombre: "Calamares a la Romana",
        categoria: "Entrantes",
        precio: 11.5,
        disponible: true,
        ingredientes: ["calamar", "harina", "huevo", "limón", "sal"],
      },
      {
        nombre: "Churros con Chocolate",
        categoria: "Postres",
        precio: 6.5,
        disponible: true,
        ingredientes: [
          "harina",
          "agua",
          "sal",
          "aceite",
          "chocolate",
          "azúcar",
        ],
      },
    ]);

    // Simulamos la lectura del archivo JSON
    jest.spyOn(fs, "readFileSync").mockReturnValue(inventarioCorrecto);

    const validator = new InventarioValidator();
    const cargado = validator.cargarInventario("inventario.json");

    expect(cargado).toBe(true);
    validator.imprimirResumen();
    expect(consoleLogSpy).toHaveBeenCalled(); // Comprobamos que se haya llamado a console.log

    expect(consoleLogSpy).toHaveBeenCalledWith(
      expect.stringContaining("Total de platos: 2")
    ); // Verifica que se imprima el total correcto
  });

  test("Carga de inventario con datos incorrectos", () => {
    const inventarioIncorrecto = JSON.stringify([
      {
        nombre: null,
        categoria: "Entrantes",
        precio: -5,
        disponible: "sí",
        ingredientes: [],
      },
    ]);

    // Simulamos la lectura del archivo JSON
    jest.spyOn(fs, "readFileSync").mockReturnValue(inventarioIncorrecto);

    const validator = new InventarioValidator();
    const cargado = validator.cargarInventario("inventario.json");

    expect(cargado).toBe(true);
    expect(consoleErrorSpy).toHaveBeenCalled(); // Comprobamos que se haya llamado a console.error
    expect(consoleErrorSpy).toHaveBeenCalledWith(
      expect.stringContaining("Alerta: Nombre inválido o vacío")
    );
  });
});
