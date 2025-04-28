// emailDuplicateChecker.test.js
const { findDuplicateEmails } = require("./emailDuplicateChecker");

describe("findDuplicateEmails", () => {
  // Prueba para lista vacía
  test("should return false for empty array", () => {
    const emails = [];
    const result = findDuplicateEmails(emails);
    expect(result).toEqual({ duplicates: [], hasDuplicates: false });
  });

  // Prueba para lista sin duplicados
  test("should return false for unique emails", () => {
    const emails = ["test@example.com", "user@domain.com", "email@host.net"];
    const result = findDuplicateEmails(emails);
    expect(result).toEqual({ duplicates: [], hasDuplicates: false });
  });

  // Prueba para lista con duplicados exactos (considerando el normalizado)
  test("should return true for exact duplicates", () => {
    const emails = ["Test@example.com", "test@example.com", "Test@example.com"];
    const result = findDuplicateEmails(emails);
    expect(result).toEqual({
      duplicates: ["test@example.com"],
      hasDuplicates: true,
    });
  });

  // Prueba para lista con variaciones en mayúsculas
  test("should group duplicates with different cases", () => {
    const emails = ["test@example.com", "TEST@example.com", "test@example.com"];
    const result = findDuplicateEmails(emails);
    expect(result).toEqual({
      duplicates: ["test@example.com"],
      hasDuplicates: true,
    });
  });

  // Prueba para lista con duplicados debido a espacios
  test("should group duplicates with spaces", () => {
    const emails = [
      " test@example.com",
      "test@example.com ",
      "test@example.com",
    ];
    const result = findDuplicateEmails(emails);
    expect(result).toEqual({
      duplicates: ["test@example.com"],
      hasDuplicates: true,
    });
  });

  // Prueba cuando el input no es un arreglo válido
  test("should throw TypeError for non-array input", () => {
    const emails = "invalid-input";
    expect(() => findDuplicateEmails(emails)).toThrow(TypeError);
  });
});
