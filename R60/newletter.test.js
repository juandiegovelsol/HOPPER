const { registrarSuscripcion, _test } = require("./newsletter");

describe("registrarSuscripcion", () => {
  beforeEach(() => _test());

  it("debería registrar correctamente un email válido", () => {
    const resultado = registrarSuscripcion("usuario@example.com", [
      "tech",
      "salud",
    ]);
    expect(resultado.email).toBe("usuario@example.com");
    expect(resultado.preferencias).toContain("tech");
    expect(resultado.fechaAlta).toMatch(
      /^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$/
    );
  });

  it("debería lanzar error si el email es inválido", () => {
    expect(() => registrarSuscripcion("no-es-un-email", ["tech"])).toThrow(
      "Email no válido"
    );
  });

  it("debería lanzar error si el email ya está registrado", () => {
    registrarSuscripcion("usuario@example.com", []);
    expect(() => registrarSuscripcion("usuario@example.com", ["tech"])).toThrow(
      "El email ya está suscrito"
    );
  });

  it("debería eliminar duplicados en las preferencias", () => {
    const resultado = registrarSuscripcion("nuevo@example.com", [
      "tech",
      "tech",
      "salud",
    ]);
    expect(resultado.preferencias).toEqual(["tech", "salud"]);
  });

  it("debería lanzar error si las preferencias no son un array de strings", () => {
    expect(() =>
      registrarSuscripcion("nuevo@example.com", ["tech", 42])
    ).toThrow("Las preferencias deben ser un array de strings");
  });
});
