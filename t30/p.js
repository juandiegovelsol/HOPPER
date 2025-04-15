const fs = require("fs");

function leerCSV(nombreArchivo) {
  return new Promise((resolve, reject) => {
    fs.readFile(nombreArchivo, "utf8", (err, contenido) => {
      if (err) return reject(err);
      resolve(contenido);
    });
  });
}

function procesarPrestamos(contenido) {
  let filas = contenido.trim().split("\n");
  if (filas.length === 0) {
    throw new Error("El archivo CSV no contiene registros.");
  }

  if (
    filas[0].toLowerCase().includes("tiempo") ||
    filas[0].toLowerCase().includes("costo")
  ) {
    filas.shift();
  }

  if (filas.length === 0) {
    throw new Error("No hay registros después del encabezado en el CSV.");
  }

  const resumenCostos = {};
  let tiempoTotal = 0;
  let gananciasTotales = 0;
  const patronTiempo = /^\d{2} \d{2} \d{2}$/;

  filas.forEach((fila, indice) => {
    const columnas = fila.split(",");
    if (columnas.length !== 2) {
      throw new Error(`Error en la línea ${indice + 1}: formato incorrecto`);
    }

    const tiempoStr = columnas[0].trim();
    const costoStr = columnas[1].trim();

    if (!patronTiempo.test(tiempoStr)) {
      throw new Error(
        `Error en la línea ${
          indice + 1
        }: el tiempo debe tener el formato HH MM SS`
      );
    }

    const [hh, mm, ss] = tiempoStr.split(" ").map(Number);
    if (isNaN(hh) || isNaN(mm) || isNaN(ss)) {
      throw new Error(
        `Error en la línea ${
          indice + 1
        }: el tiempo contiene valores no numéricos`
      );
    }

    const segundos = hh * 3600 + mm * 60 + ss;
    const horas = segundos / 3600;

    const costo = parseFloat(costoStr);
    if (isNaN(costo) || costo <= 0) {
      throw new Error(
        `Error en la línea ${indice + 1}: el costo debe ser un número positivo`
      );
    }

    const ganancias = costo * horas;

    if (!resumenCostos[costo]) {
      resumenCostos[costo] = { tiempo: 0, ganancias: 0 };
    }
    resumenCostos[costo].tiempo += horas;
    resumenCostos[costo].ganancias += ganancias;

    tiempoTotal += horas;
    gananciasTotales += ganancias;
  });

  return { resumenCostos, tiempoTotal, gananciasTotales };
}

const archivoCSV = process.argv[2] || "data.csv";

leerCSV(archivoCSV)
  .then((contenido) => {
    const { resumenCostos, tiempoTotal, gananciasTotales } =
      procesarPrestamos(contenido);

    for (const costo in resumenCostos) {
      console.log(
        `Costo del libro: ${costo} CLP, Tiempo total: ${resumenCostos[
          costo
        ].tiempo.toFixed(2)} horas, Ganancias: ${resumenCostos[
          costo
        ].ganancias.toFixed(2)} CLP`
      );
    }
    console.log(`Tiempo total de préstamos: ${tiempoTotal.toFixed(2)} horas`);
    console.log(`Ganancias totales: ${gananciasTotales.toFixed(2)} CLP`);
  })
  .catch((error) => {
    console.error("Error:", error.message);
    process.exit(1);
  });
