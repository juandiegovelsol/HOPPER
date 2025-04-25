const fs = require("fs");
const { FileManager } = require("./FileManager"); // Ajusta el path según tu proyecto

describe("FileManager", () => {
  let fileManager;
  let tempFilePath;

  beforeEach(() => {
    tempFilePath = `./test_file_${FileUtil.randomword(10)}.txt`;
    fileManager = new FileManager(tempFilePath);
  });

  afterEach(() => {
    fs.unlinkSync(tempFilePath);
  });

  test("debe permitir la escritura y lectura de un archivo de texto con contenido válido", () => {
    const content = "Este es un contenido de prueba";

    // Escribe en el archivo
    fileManager.write(content);

    // Lee el contenido del archivo
    const readContent = fileManager.read();

    expect(readContent).toBe(content + "\n");
  });

  test("no debe permitir la escritura de un archivo que no sea de texto (.txt)", () => {
    expect(() => new FileManager("./nonTextFile.jpg")).toThrow(
      "File path must end with .txt"
    );
  });

  test("no debe permitir escribir contenido que no sea de tipo string", () => {
    expect(() => fileManager.write(12345)).toThrow("Content must be a string");
  });

  test("no debe permitir escribir contenido que exceda los 100 caracteres", () => {
    const longContent = "a".repeat(101); // 101 caracteres
    expect(() => fileManager.write(longContent)).toThrow(
      "Content length exceeds 100 characters"
    );
  });

  test("no debe permitir escribir null o undefined como contenido", () => {
    expect(() => fileManager.write(null)).toThrow(
      "Content cannot be null or undefined"
    );
    expect(() => fileManager.write(undefined)).toThrow(
      "Content cannot be null or undefined"
    );
  });
});
