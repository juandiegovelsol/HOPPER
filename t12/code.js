function organizarListaDeCompras(listaDeCompras) {
  const categorias = {
    "Frutas y verduras": [],
    "Carnes y pescados": [],
    "Lácteos y huevos": [],
    "Panadería y cereales": [],
    Despensa: [],
    Limpieza: [],
    Otros: [],
  };

  listaDeCompras.forEach((item) => {
    const itemLowerCase = item.toLowerCase();
    if (
      itemLowerCase.includes("manzana") ||
      itemLowerCase.includes("plátano") ||
      itemLowerCase.includes("zanahoria") ||
      itemLowerCase.includes("tomate")
    ) {
      categorias["Frutas y verduras"].push(item);
    } else if (
      itemLowerCase.includes("pollo") ||
      itemLowerCase.includes("carne") ||
      itemLowerCase.includes("pescado")
    ) {
      categorias["Carnes y pescados"].push(item);
    } else if (
      itemLowerCase.includes("leche") ||
      itemLowerCase.includes("queso") ||
      itemLowerCase.includes("huevos")
    ) {
      categorias["Lácteos y huevos"].push(item);
    } else if (
      itemLowerCase.includes("pan") ||
      itemLowerCase.includes("arroz") ||
      itemLowerCase.includes("cereal")
    ) {
      categorias["Panadería y cereales"].push(item);
    } else if (
      itemLowerCase.includes("fideos") ||
      itemLowerCase.includes("atún") ||
      itemLowerCase.includes("aceite")
    ) {
      categorias["Despensa"].push(item);
    } else if (
      itemLowerCase.includes("detergente") ||
      itemLowerCase.includes("cloro") ||
      itemLowerCase.includes("jabón")
    ) {
      categorias["Limpieza"].push(item);
    } else {
      categorias["Otros"].push(item);
    }
  });

  return categorias;
}

const listaDeComprasJSON = process.argv[2];
if (!listaDeComprasJSON) {
  console.error("Debes proporcionar la lista de compras como un objeto JSON.");
  process.exit(1);
}

try {
  const listaDeCompras = JSON.parse(listaDeComprasJSON);
  if (!Array.isArray(listaDeCompras)) {
    throw new Error("El JSON debe ser un array.");
  }
  listaDeCompras.forEach((item, index) => {
    if (typeof item !== "string" || item.trim() === "") {
      throw new Error(
        `El elemento en la posición ${index} no es una cadena de texto válida.`
      );
    }
  });
  const listaOrganizada = organizarListaDeCompras(listaDeCompras);
  console.log(JSON.stringify(listaOrganizada, null, 2));
} catch (error) {
  console.error("Error al analizar el objeto JSON:", error.message);
  process.exit(1);
}
