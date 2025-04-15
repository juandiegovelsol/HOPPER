const fs = require("fs");

// Función para validar cada orden
function validarOrden(orden) {
  if (
    !orden.precioTotal ||
    !Number.isInteger(orden.precioTotal) ||
    orden.precioTotal <= 0
  ) {
    console.log("1");
    return false;
  }

  if (!Array.isArray(orden.platos) || !orden.platos.length) {
    console.log("2");
    return false;
  }
  for (const plato of orden.platos) {
    if (
      !plato.nombre ||
      typeof plato.nombre !== "string" ||
      !plato.nombre.trim()
    ) {
      console.log("3");
      return false;
    }
    if (!Number.isInteger(plato.cantidad) || plato.cantidad <= 0) {
      console.log("4");
      return false;
    }
  }
  return true;
}

// Función para clasificar las órdenes según su rango de precio
function clasificarOrden(orden) {
  if (orden.precioTotal <= 50) return "0-50";
  if (orden.precioTotal <= 100) return "50-100";
  return "más de 100";
}

// Función para procesar el archivo JSON de órdenes
function procesarOrdenes(archivoJSON, callback) {
  fs.readFile(archivoJSON, "utf8", (err, data) => {
    if (err) {
      console.error("Error al leer el archivo JSON:", err);
      return;
    }

    try {
      const ordenes = JSON.parse(data);
      if (!Array.isArray(ordenes)) {
        console.error("El archivo JSON no contiene un array de órdenes");
        return;
      }

      const resultados = {
        "0-50": {},
        "50-100": {},
        "más de 100": {},
      };

      ordenes.forEach((orden) => {
        if (!validarOrden(orden)) {
          console.warn("Orden inválida, siendo ignorada:", orden);
          return;
        }

        const claveClasificacion = clasificarOrden(orden);
        for (const plato of orden.platos) {
          if (!resultados[claveClasificacion][plato.nombre]) {
            resultados[claveClasificacion][plato.nombre] = 0;
          }
          resultados[claveClasificacion][plato.nombre] += plato.cantidad;
        }
      });

      callback(resultados);
    } catch (err) {
      console.error("Error al parsear el archivo JSON:", err);
    }
  });
}

// Ejecución del programa
procesarOrdenes("ordenes.json", (resultados) => {
  console.log("Platos más pedidos en cada rango de precio:");
  console.log("Rango 0-50 dólares:", resultados["0-50"]);
  console.log("Rango 50-100 dólares:", resultados["50-100"]);
  console.log("Rango más de 100 dólares:", resultados["más de 100"]);
});
