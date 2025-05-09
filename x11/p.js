function validarPuntajes(datos, umbralAprobado = 5.0) {
  if (typeof datos !== "object" || datos === null) {
    throw new TypeError("El parámetro 'datos' debe ser un objeto");
  }

  const aprobados = [];
  const reprobados = [];
  const errores = [];

  for (const alumno in datos) {
    const puntajes = datos[alumno];

    if (typeof alumno !== "string" || alumno.trim() === "") {
      errores.push(alumno);
      continue;
    }

    if (!Array.isArray(puntajes) || puntajes.length === 0) {
      errores.push(alumno);
      continue;
    }

    let suma = 0.0;
    let valido = true;

    for (const p of puntajes) {
      if (typeof p !== "number" || p < 0 || p > 10) {
        valido = false;
        break;
      }
      suma += p;
    }

    if (!valido) {
      errores.push(alumno);
      continue;
    }

    const promedio = suma / puntajes.length;

    if (promedio >= umbralAprobado) {
      aprobados.push(alumno);
    } else {
      reprobados.push(alumno);
    }
  }

  return {
    aprobados,
    reprobados,
    errores,
  };
}

module.exports = validarPuntajes;

// Ejemplo de uso
const datosEjemplo = {
  Juan: [6, 7, 8],
  Maria: [9, 9, 10],
  Luis: [4, 5, 6],
};

const resultados = validarPuntajes(datosEjemplo);
console.log(resultados);
console.log("Aprobados:", resultados.aprobados);
console.log("Reprobados:", resultados.reprobados);
console.log("Errores:", resultados.errores);
