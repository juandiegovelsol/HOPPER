function validarDatos(recetas, cocinas) {
  if (!Array.isArray(recetas)) {
    throw new Error("El arreglo de recetas debe ser un arreglo.");
  }
  if (!Array.isArray(cocinas)) {
    throw new Error("El arreglo de cocinas debe ser un arreglo.");
  }
  recetas.forEach((receta, i) => {
    if (typeof receta !== "string" || receta.trim() === "") {
      throw new Error(
        `Receta inválida en la posición ${i}: debe ser una cadena no vacía.`
      );
    }
  });
  cocinas.forEach((cocina, i) => {
    if (typeof cocina !== "string" || cocina.trim() === "") {
      throw new Error(
        `Cocina inválida en la posición ${i}: debe ser una cadena no vacía.`
      );
    }
    if (/\s/.test(cocina)) {
      throw new Error(
        `Cocina inválida en la posición ${i}: no debe contener espacios.`
      );
    }
  });
}

function clasificarRecetas(recetas, cocinas) {
  const clasificacion = cocinas.reduce((acc, cocina) => {
    acc[cocina] = [];
    return acc;
  }, {});
  clasificacion["Otros"] = [];
  recetas.forEach((receta) => {
    const encontrada = cocinas.find((cocina) =>
      receta.toLowerCase().includes(cocina.toLowerCase())
    );
    if (encontrada) {
      clasificacion[encontrada].push(receta);
    } else {
      clasificacion["Otros"].push(receta);
    }
  });
  return clasificacion;
}

function organizarRecetasPorCocina(recetas, cocinas) {
  try {
    validarDatos(recetas, cocinas);
    const recetasClasificadas = clasificarRecetas(recetas, cocinas);
    console.log(recetasClasificadas);
  } catch (error) {
    console.error("Error al procesar los datos:", error.message);
  }
}

const recetas = [
  "Pizza italiana con pepperoni",
  "Sushi japonés de salmón",
  "Tacos mexicanos al pastor",
  "Paella española de mariscos",
  "Pad Thai con camarones",
  "Tacos Fusión Mexicana / Japonesa",
];
const tiposCocina = [
  "Italiana",
  "Japonesa",
  "Mexicana",
  "Española",
  "Tailandesa o Thai",
];

organizarRecetasPorCocina(recetas, tiposCocina);
