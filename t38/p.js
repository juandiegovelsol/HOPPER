function procesarDatosEstudiantes(jsonData) {
  const estudiantes = JSON.parse(jsonData);
  const resultados = [];

  for (const estudiante of estudiantes) {
    const validacion = validarEstudiante(estudiante);
    if (!validacion.esValido) {
      console.error(
        `Error en estudiante ${estudiante.nombre || "sin nombre"}: ${
          validacion.mensaje
        }`
      );
      continue;
    }

    const promedio = calcularPromedio(estudiante.cursos);
    resultados.push({
      id: estudiante.id,
      nombre: estudiante.nombre,
      semestre: estudiante.semestre,
      promedio: promedio,
    });
  }

  return resultados;
}

function validarEstudiante(estudiante) {
  if (!estudiante.nombre || estudiante.nombre.trim() === "") {
    return { esValido: false, mensaje: "El nombre no puede estar vacío" };
  }

  if (!Number.isInteger(estudiante.id) || estudiante.id <= 0) {
    return { esValido: false, mensaje: "El ID debe ser un entero positivo" };
  }

  if (
    !estudiante.cursos ||
    !Array.isArray(estudiante.cursos) ||
    estudiante.cursos.length === 0
  ) {
    return {
      esValido: false,
      mensaje: "El estudiante debe tener al menos un curso",
    };
  }

  for (let i = 0; i < estudiante.cursos.length; i++) {
    const curso = estudiante.cursos[i];
    if (!Number.isInteger(curso.id) || curso.id <= 0) {
      return {
        esValido: false,
        mensaje: `El ID del curso ${i + 1} debe ser un entero positivo`,
      };
    }

    if (!curso.nombre || curso.nombre.trim() === "") {
      return {
        esValido: false,
        mensaje: `El nombre del curso ${i + 1} no puede estar vacío`,
      };
    }

    if (typeof curso.nota !== "number" || curso.nota < 0 || curso.nota > 10) {
      return {
        esValido: false,
        mensaje: `La nota del curso ${i + 1} debe ser un valor entre 0 y 10`,
      };
    }
  }

  return { esValido: true };
}

function calcularPromedio(cursos) {
  const totalNotas = cursos.reduce((sum, curso) => sum + curso.nota, 0);
  return totalNotas / cursos.length;
}

function leerYProcesarArchivo(rutaArchivo) {
  const fs = require("fs");
  try {
    const datos = fs.readFileSync(rutaArchivo, "utf8");
    return procesarDatosEstudiantes(datos);
  } catch (error) {
    console.error("Error al leer el archivo:", error);
    return [];
  }
}

const resultados = leerYProcesarArchivo("estudiantes.json");
console.log(resultados);

module.exports = {
  procesarDatosEstudiantes,
  leerYProcesarArchivo,
};
