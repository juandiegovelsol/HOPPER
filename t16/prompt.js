const fs = require("fs");

const validarArchivos = (libros, generos) => {
  if (!Array.isArray(libros)) {
    throw new Error("El archivo de libros debe contener un array");
  }

  if (!Array.isArray(generos)) {
    throw new Error("El archivo de géneros debe contener un array");
  }

  libros.forEach((libro, index) => {
    if (typeof libro !== "string" || libro.trim() === "") {
      throw new Error(
        `Libro inválido en posición ${index}: debe ser una string no vacía`
      );
    }
  });

  generos.forEach((genero, index) => {
    if (typeof genero !== "string" || genero.trim() === "") {
      throw new Error(
        `Género inválido en posición ${index}: debe ser una string no vacía`
      );
    }
    if (/\s/.test(genero)) {
      throw new Error(
        `Género inválido en posición ${index}: no debe contener espacios`
      );
    }
  });

  return true;
};

const categorizarLibros = (libros, generos) => {
  const categorizado = generos.reduce((acc, genero) => {
    acc[genero] = [];
    return acc;
  }, {});

  libros.forEach((libro) => {
    const generoEncontrado = generos.find((genero) =>
      libro.toLowerCase().includes(genero.toLowerCase())
    );

    if (generoEncontrado) {
      categorizado[generoEncontrado].push(libro);
    } else {
      categorizado["Otros"] = categorizado["Otros"] || [];
      categorizado["Otros"].push(libro);
    }
  });

  return categorizado;
};

const organizarLibrosPorGenero = async () => {
  try {
    const datosLibros = fs.readFileSync("libros.json");
    const libros = JSON.parse(datosLibros);

    const datosGeneros = fs.readFileSync("generos.json");
    const generos = JSON.parse(datosGeneros);

    validarArchivos(libros, generos);

    const librosCategorizados = categorizarLibros(libros, generos);

    console.log(librosCategorizados);
  } catch (error) {
    console.error("Error al procesar los archivos:", error);
  }
};

organizarLibrosPorGenero();
