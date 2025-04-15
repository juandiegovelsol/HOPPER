function procesarInfoAlumnos(jsonData) {
  const alumnos = JSON.parse(jsonData);
  const resultadosFinales = [];

  for (const alumno of alumnos) {
    const validacion = validarAlumno(alumno);
    if (!validacion.valido) {
      console.error(
        `Error en alumno ${alumno.nombre || "sin nombre"}: ${
          validacion.mensaje
        }`
      );
      continue;
    }

    const media = calcularMedia(alumno.cursos);
    resultadosFinales.push({
      id: alumno.id,
      nombre: alumno.nombre,
      semestre: alumno.semestre,
      promedio: media,
    });
  }

  return resultadosFinales;
}

function validarAlumno(alumno) {
  if (!alumno.nombre || alumno.nombre.trim() === "") {
    return { valido: false, mensaje: "El nombre no puede estar vacío." };
  }

  if (!Number.isInteger(alumno.id) || alumno.id <= 0) {
    return {
      valido: false,
      mensaje: "El ID debe ser un entero mayor que cero.",
    };
  }

  if (
    !alumno.cursos ||
    !Array.isArray(alumno.cursos) ||
    alumno.cursos.length === 0
  ) {
    return {
      valido: false,
      mensaje: "El alumno debe estar inscrito en al menos un curso.",
    };
  }

  for (let i = 0; i < alumno.cursos.length; i++) {
    const curso = alumno.cursos[i];
    if (!Number.isInteger(curso.id) || curso.id <= 0) {
      return {
        valido: false,
        mensaje: `El ID del curso ${i + 1} debe ser un entero mayor que cero.`,
      };
    }

    if (!curso.nombre || curso.nombre.trim() === "") {
      return {
        valido: false,
        mensaje: `El nombre del curso ${i + 1} no puede estar vacío.`,
      };
    }

    if (typeof curso.nota !== "number" || curso.nota < 0 || curso.nota > 10) {
      return {
        valido: false,
        mensaje: `La nota del curso ${i + 1} debe estar entre 0 y 10.`,
      };
    }
  }

  return { valido: true };
}

function calcularMedia(cursos) {
  const sumaNotas = cursos.reduce((acum, curso) => acum + curso.nota, 0);
  return sumaNotas / cursos.length;
}

function leerYProcesarArchivo(rutaArchivo) {
  const fs = require("fs");
  try {
    const contenido = fs.readFileSync(rutaArchivo, "utf8");
    return procesarInfoAlumnos(contenido);
  } catch (error) {
    console.error("Error al acceder al archivo:", error);
    return [];
  }
}

const resultados = leerYProcesarArchivo("estudiantes.json");
console.log(resultados);

module.exports = {
  procesarInfoAlumnos,
  leerYProcesarArchivo,
};
