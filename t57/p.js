const fs = require("fs");

function cargarOrdenes(archivo) {
  const datos = fs.readFileSync(archivo);
  return JSON.parse(datos);
}

function validarOrden(orden) {
  return (
    orden &&
    typeof orden.total === "number" &&
    orden.total > 0 &&
    Array.isArray(orden.platos) &&
    orden.platos.every(
      (plato) =>
        typeof plato.nombre === "string" &&
        plato.nombre.trim() !== "" &&
        typeof plato.cantidad === "number" &&
        plato.cantidad > 0
    )
  );
}

function analizarVentas(ordenes) {
  const categoriasVentas = {
    baja: {},
    media: {},
    alta: {},
  };

  for (const clave in ordenes) {
    const orden = ordenes[clave];
    if (validarOrden(orden)) {
      const { total, platos } = orden;
      let categoria = "";
      if (total <= 50) categoria = "baja";
      else if (total <= 100) categoria = "media";
      else categoria = "alta";
      for (const plato of platos) {
        categoriasVentas[categoria][plato.nombre] =
          (categoriasVentas[categoria][plato.nombre] || 0) + plato.cantidad;
      }
    } else {
      console.log(
        `Alerta: La orden con clave ${clave} no cumple con los requisitos de validación y no será procesada.`
      );
    }
  }

  for (const categoria in categoriasVentas) {
    const platoMasPedido = Object.entries(categoriasVentas[categoria]).reduce(
      (a, b) => (b[1] > a[1] ? b : a),
      ["", 0]
    );
    console.log(
      `Plato más pedido en ${categoria}: ${platoMasPedido[0]} (Cantidad: ${platoMasPedido[1]})`
    );
  }
}

const ordenes = cargarOrdenes("ordenes.json");
analizarVentas(ordenes);
