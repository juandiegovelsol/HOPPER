function clasificarCalificaciones(estudiantes, notaMaxima = 10) {
  if (
    typeof estudiantes !== "object" ||
    estudiantes === null ||
    Array.isArray(estudiantes)
  ) {
    throw new TypeError("El parámetro 'estudiantes' debe ser un objeto.");
  }

  const sobresalientes = [];
  const notables = [];
  const aprobados = [];
  const suspensos = [];
  const errores = [];

  for (const nombre in estudiantes) {
    const notas = estudiantes[nombre];

    if (typeof nombre !== "string" || nombre.trim() === "") {
      errores.push(nombre);
      continue;
    }

    if (!Array.isArray(notas) || notas.length === 0) {
      errores.push(nombre);
      continue;
    }

    let valido = true;
    let sumaNotas = 0;

    for (const nota of notas) {
      if (typeof nota !== "number" || nota < 0 || nota > notaMaxima) {
        valido = false;
        break;
      }
      sumaNotas += nota;
    }

    if (!valido) {
      errores.push(nombre);
      continue;
    }

    const notaMedia = sumaNotas / notas.length;

    if (notaMedia >= 9) {
      sobresalientes.push(nombre);
    } else if (notaMedia >= 7) {
      notables.push(nombre);
    } else if (notaMedia >= 5) {
      aprobados.push(nombre);
    } else {
      suspensos.push(nombre);
    }
  }

  return {
    sobresalientes,
    notables,
    aprobados,
    suspensos,
    errores,
  };
}

module.exports = clasificarCalificaciones;

// Ejemplo de uso
const aula = {
  "María García": [9.5, 8.7, 9.2, 9.8, 9.6], // Media: 9.36 - Sobresaliente
  "Pablo Sánchez": [7.5, 8.0, 7.2, 6.9, 7.8], // Media: 7.48 - Notable
  "Laura Martínez": [6.2, 5.8, 4.9, 6.5, 5.0], // Media: 5.68 - Aprobado
  "Javier López": [4.5, 3.8, 5.2, 4.0, 3.5], // Media: 4.2 - Suspenso
  "Ana Rodríguez": [9.0, "8.5", 9.2], // Dato inválido
  "": [7.5, 8.0, 8.5], // Nombre inválido
};

const resultados = clasificarCalificaciones(aula);
console.log(resultados);
console.log("Sobresalientes:", resultados.sobresalientes);
console.log("Notables:", resultados.notables);
console.log("Aprobados:", resultados.aprobados);
console.log("Suspensos:", resultados.suspensos);
console.log("Errores:", resultados.errores);
