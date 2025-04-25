const fs = require("fs");
const { parse } = require("csv-parse/sync");

function procesarDatosPacientes(rutaArchivo) {
  const contenido = fs.readFileSync(rutaArchivo, "utf8");
  const registros = parse(contenido, {
    columns: true,
    skip_empty_lines: true,
  });

  let contadores = {
    baja: 0,
    media: 0,
    alta: 0,
    critica: 0,
    errores: [],
  };

  registros.forEach((paciente, index) => {
    try {
      validarPaciente(paciente);

      const prioridad = parseInt(paciente.prioridad);

      if (prioridad >= 0 && prioridad <= 25) {
        contadores.baja++;
      } else if (prioridad >= 26 && prioridad <= 50) {
        contadores.media++;
      } else if (prioridad >= 51 && prioridad <= 75) {
        contadores.alta++;
      } else if (prioridad >= 76 && prioridad <= 100) {
        contadores.critica++;
      }
    } catch (error) {
      contadores.errores.push({
        linea: index + 2,
        error: error.message,
        datos: paciente,
      });
    }
  });

  return contadores;
}

function validarPaciente(paciente) {
  if (!paciente.id || !paciente.nombre || !paciente.apellido) {
    throw new Error("Datos básicos incompletos");
  }

  if (!paciente.medico) {
    throw new Error("Médico no asignado");
  }

  if (!paciente.tratamiento) {
    throw new Error("Tratamiento no asignado");
  }

  const prioridad = parseInt(paciente.prioridad);

  if (isNaN(prioridad)) {
    throw new Error("Prioridad no es un número");
  }

  if (prioridad < 0 || prioridad > 100) {
    throw new Error("Prioridad fuera de rango (0-100)");
  }
}

function main() {
  const args = process.argv.slice(2);

  if (args.length < 1) {
    console.error("Uso: node procesador-pacientes.js <ruta-archivo-csv>");
    process.exit(1);
  }

  const rutaArchivo = args[0];

  try {
    const resultado = procesarDatosPacientes(rutaArchivo);

    console.log("\n=== RESUMEN DE PACIENTES POR PRIORIDAD ===");
    console.log(`Prioridad BAJA (0-25): ${resultado.baja} pacientes`);
    console.log(`Prioridad MEDIA (26-50): ${resultado.media} pacientes`);
    console.log(`Prioridad ALTA (51-75): ${resultado.alta} pacientes`);
    console.log(`Prioridad CRÍTICA (76-100): ${resultado.critica} pacientes`);

    if (resultado.errores.length > 0) {
      console.log("\n=== ERRORES ENCONTRADOS ===");
      resultado.errores.forEach((err) => {
        console.log(`Error en línea ${err.linea}: ${err.error}`);
        console.log("Datos:", err.datos);
        console.log("---");
      });
    }
  } catch (error) {
    console.error(`Error al procesar el archivo: ${error.message}`);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = { procesarDatosPacientes };
