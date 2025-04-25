const assert = require("assert");

describe("agregarItem", () => {
  let inventario;

  afterEach(() => {
    inventario = {};
  });

  it("debería agregar un artículo con información completa", () => {
    agregarItem("Camiseta Básica", "Ropa", 50, 5.0, 12.99, "Madrid");
    assert.deepStrictEqual(inventario["Camiseta Básica"], {
      categoria: "Ropa",
      cantidad: 50,
      precio_pagado: "5.00 €",
      precio_venta: "12.99 €",
      margen_beneficio: "7.99 €",
      fecha_inventario: "l1 de octubre de 2024",
      ciudad_destino: "Madrid",
    });
  });

  it("no debería agregar un artículo si el nombre está vacío", () => {
    agregarItem("", "Ropa", 50, 5.0, 12.99, "Madrid");
    assert.deepStrictEqual(inventario, {});
  });

  it("no debería agregar un artículo si la cantidad es negativa", () => {
    agregarItem("Camiseta Básica", "Ropa", -50, 5.0, 12.99, "Madrid");
    assert.deepStrictEqual(inventario, {});
  });

  it("debería manejar la fecha incorrectamente formateada y setearla por defecto", () => {
    const obtenerFechaFormateadaIncorrecta = () => "Fecha Incorrecta";
    global.obtenerFechaFormateada = obtenerFechaFormateadaIncorrecta;

    agregarItem("Camiseta Básica", "Ropa", 50, 5.0, 12.99, "Madrid");

    assert.deepStrictEqual(inventario["Camiseta Básica"], {
      categoria: "Ropa",
      cantidad: 50,
      precio_pagado: "5.00 €",
      precio_venta: "12.99 €",
      margen_beneficio: "7.99 €",
      fecha_inventario: "Fecha Incorrecta",
      ciudad_destino: "Madrid",
    });

    global.obtenerFechaFormateada = obtenerFechaFormateada; // Restaurar la función original
  });

  it("no debería agregar un artículo si faltan parámetros", () => {
    agregarItem("Camiseta Básica", "Ropa", 50, 5.0, 12.99);
    assert.deepStrictEqual(inventario, {});
  });

  it("no debería agregar un artículo si se le pasa un número incorrecto de argumentos (5)", () => {
    agregarItem("Camiseta Básica", "Ropa", 50, 5.0, 12.99, "Madrid", "Extra");
    assert.deepStrictEqual(inventario, {});
  });

  it("no debería agregar un artículo si se le pasa un número incorrecto de argumentos (7)", () => {
    agregarItem(
      "Camiseta Básica",
      "Ropa",
      50,
      5.0,
      12.99,
      "Madrid",
      "Extra",
      "Más Extra"
    );
    assert.deepStrictEqual(inventario, {});
  });

  it("debería manejar algunos parámetros nulos correctamente", () => {
    agregarItem("Camiseta Básica", null, 50, null, 12.99, null);
    assert.deepStrictEqual(inventario["Camiseta Básica"], {
      categoria: null,
      cantidad: 50,
      precio_pagado: "0.00 €",
      precio_venta: "12.99 €",
      margen_beneficio: "12.99 €",
      fecha_inventario: "l1 de octubre de 2024",
      ciudad_destino: null,
    });
  });

  it("no debería agregar un artículo si el precioPagado es mayor que precioVenta", () => {
    agregarItem("Camiseta Básica", "Ropa", 50, 12.99, 5.0, "Madrid");
    assert.deepStrictEqual(inventario, {});
  });
});
