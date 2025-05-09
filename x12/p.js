function clasificarAsistencia(empleados, diasLaborables = 20) {
  if (
    typeof empleados !== "object" ||
    empleados === null ||
    Array.isArray(empleados)
  ) {
    throw new TypeError("El parámetro 'empleados' debe ser un objeto.");
  }

  const puntuales = [];
  const regulares = [];
  const absentistas = [];
  const errores = [];

  for (const nombre in empleados) {
    const asistencias = empleados[nombre];

    if (typeof nombre !== "string" || nombre.trim() === "") {
      errores.push(nombre);
      continue;
    }

    if (!Array.isArray(asistencias) || asistencias.length === 0) {
      errores.push(nombre);
      continue;
    }

    let valido = true;
    const diasUnicos = new Set();

    for (const dia of asistencias) {
      if (typeof dia !== "number" || dia < 1 || dia > 31) {
        valido = false;
        break;
      }
      diasUnicos.add(dia);
    }

    if (!valido) {
      errores.push(nombre);
      continue;
    }

    const asistenciaReal = diasUnicos.size;
    const porcentaje = (asistenciaReal / diasLaborables) * 100;

    if (porcentaje >= 90) {
      puntuales.push(nombre);
    } else if (porcentaje >= 75) {
      regulares.push(nombre);
    } else {
      absentistas.push(nombre);
    }
  }

  return {
    puntuales,
    regulares,
    absentistas,
    errores,
  };
}

module.exports = clasificarAsistencia;
// Ejemplo de uso
const plantilla = {
  Juan: [1, 2, 3, 4, 5, 6, 7, 21], // 8 días, uno inválido
  Maria: [], // 0 días
  Pedro: [1, 2, 3, 4, 5, 6, "siete"], // 6 días, uno no numérico
};

const resultados = clasificarAsistencia(plantilla);

console.log("Puntuales:", resultados.puntuales);
console.log("Regulares:", resultados.regulares);
console.log("Absentistas:", resultados.absentistas);
console.log("Errores:", resultados.errores);
