const fs = require("fs");
const path = require("path");

// Función para validar la fecha
function validarFecha(fecha) {
  console.log(fecha);
  const partes = fecha.split("/");
  if (partes.length !== 3) return false;
  const [dia, mes, anio] = partes.map(Number);
  const fechaCompleta = new Date(anio, mes - 1, dia);
  if (
    isNaN(fechaCompleta.getTime()) ||
    dia !== fechaCompleta.getDate() ||
    mes !== fechaCompleta.getMonth() + 1 ||
    anio !== fechaCompleta.getFullYear()
  ) {
    return false;
  }
  return true;
}

// Función para validar el identificador del activo
function validarIdActivo(id) {
  return /^[A-Za-z0-9]{4}$/.test(id);
}

// Función para validar el precio
function validarPrecio(precio) {
  return typeof precio === "number" && precio > 0;
}

// Función para calcular los promedios
function calcularPromedios(compras) {
  const promediosDiarios = {};
  const promediosTotales = {};
  const totalPesos = {};
  const conteoPesos = {};
  console.log(compras);

  compras.forEach((compra) => {
    console.log(compra);
    const { fecha, idActivo, precio } = compra;
    if (
      !validarFecha(fecha) ||
      !validarIdActivo(idActivo) ||
      !validarPrecio(precio)
    ) {
      console.error(`Dato inválido: ${JSON.stringify(compra)}`);
      return;
    }

    if (!promediosDiarios[fecha]) {
      promediosDiarios[fecha] = {};
    }
    if (!promediosTotales[idActivo]) {
      promediosTotales[idActivo] = { totalPesos: 0, conteoPesos: 0 };
    }

    promediosDiarios[fecha][idActivo] =
      (promediosDiarios[fecha][idActivo] || 0) + precio;
    promediosTotales[idActivo].totalPesos += precio;
    promediosTotales[idActivo].conteoPesos++;
  });

  for (const fecha in promediosDiarios) {
    for (const idActivo in promediosDiarios[fecha]) {
      promediosDiarios[fecha][idActivo] /= 1;
    }
  }

  for (const idActivo in promediosTotales) {
    promediosTotales[idActivo].promedio =
      promediosTotales[idActivo].totalPesos /
      promediosTotales[idActivo].conteoPesos;
  }

  return { promediosDiarios, promediosTotales };
}

// Función para leer el archivo JSON y calcular los promedios
function procesarArchivoJSON(archivoPath) {
  try {
    const datos = JSON.parse(fs.readFileSync(archivoPath, "utf8"));
    if (!Array.isArray(datos.compras)) {
      throw new Error("La clave 'compras' no es un array.");
    }
    const { promediosDiarios, promediosTotales } = calcularPromedios(
      datos.compras
    );

    console.log("Promedios diarios de compra por activo:");
    Object.entries(promediosDiarios).forEach(([fecha, activos]) => {
      console.log(`Fecha: ${fecha}`);
      Object.entries(activos).forEach(([idActivo, promedio]) => {
        console.log(`  Activo ${idActivo}: ${promedio.toFixed(2)}`);
      });
    });

    console.log("\nPromedios totales de compra por activo:");
    Object.entries(promediosTotales).forEach(([idActivo, { promedio }]) => {
      console.log(`Activo ${idActivo}: ${promedio.toFixed(2)}`);
    });
  } catch (error) {
    console.error("Error al procesar el archivo JSON:", error.message);
  }
}

// Ruta al archivo JSON
const archivoPath = path.join(__dirname, "compras.json");

// Llamada a la función para procesar el archivo JSON
procesarArchivoJSON(archivoPath);
