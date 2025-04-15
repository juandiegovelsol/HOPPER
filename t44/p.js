const fs = require("fs");

function procesarInfoSensores(jsonData) {
  const sensores = JSON.parse(jsonData);
  const resultadosFinales = [];

  for (const sensor of sensores) {
    const validacion = validarSensor(sensor);
    if (!validacion.valido) {
      console.error(
        `Error en sensor ${sensor.nombre || "sin nombre"}: ${
          validacion.mensaje
        }`
      );
      continue;
    }

    const mediaLecturas = calcularMedia(sensor.lecturas);
    resultadosFinales.push({
      id: sensor.id,
      nombre: sensor.nombre,
      ubicacion: sensor.ubicacion,
      mediaLecturas: mediaLecturas,
    });
  }

  console.log(sensores);
  const mediasTotales = calcularMediaTotal(sensores);

  return { resultadosFinales, mediasTotales };
}

function validarSensor(sensor) {
  if (!sensor.nombre || sensor.nombre.trim() === "") {
    return { valido: false, mensaje: "El nombre no puede estar vacío." };
  }

  if (!Number.isInteger(sensor.id) || sensor.id <= 0) {
    return {
      valido: false,
      mensaje: "El ID debe ser un entero mayor que cero.",
    };
  }

  if (
    !sensor.lecturas ||
    !Array.isArray(sensor.lecturas) ||
    sensor.lecturas.length === 0
  ) {
    return {
      valido: false,
      mensaje: "El sensor debe tener al menos una lectura.",
    };
  }

  for (let i = 0; i < sensor.lecturas.length; i++) {
    const lectura = sensor.lecturas[i];
    if (!Number.isInteger(lectura.id) || lectura.id <= 0) {
      return {
        valido: false,
        mensaje: `El ID de la lectura ${
          i + 1
        } debe ser un entero mayor que cero.`,
      };
    }

    if (typeof lectura.valor !== "number") {
      return {
        valido: false,
        mensaje: `El valor de la lectura ${i + 1} debe ser un número.`,
      };
    }
  }

  return { valido: true };
}

function calcularMedia(lecturas) {
  const sumaValores = lecturas.reduce(
    (acum, lectura) => acum + lectura.valor,
    0
  );
  return +(sumaValores / lecturas.length).toFixed(2);
}

function calcularMediaTotal(sensores) {
  const ubicaciones = {};

  for (const sensor of sensores) {
    const ubicacion = sensor.ubicacion;
    if (!ubicaciones[ubicacion]) {
      ubicaciones[ubicacion] = {
        sumaValores: 0,
        cantidadLecturas: 0,
      };
    }
    for (const lectura of sensor.lecturas) {
      ubicaciones[ubicacion].sumaValores += lectura.valor;
      ubicaciones[ubicacion].cantidadLecturas += 1;
    }
  }

  const resultadoFinal = [];
  for (const ubicacion in ubicaciones) {
    const mediaTotal =
      ubicaciones[ubicacion].sumaValores /
      ubicaciones[ubicacion].cantidadLecturas;
    resultadoFinal.push({
      ubicacion: ubicacion,
      mediaTotal: +mediaTotal.toFixed(2),
    });
  }

  return resultadoFinal;
}

function leerYProcesarArchivo(rutaArchivo) {
  try {
    const contenido = fs.readFileSync(rutaArchivo, "utf8");
    return procesarInfoSensores(contenido);
  } catch (error) {
    console.error("Error al acceder al archivo:", error);
    return [];
  }
}

const resultados = leerYProcesarArchivo("sensores.json");
console.log(resultados);
