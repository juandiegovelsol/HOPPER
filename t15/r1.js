const fs = require("fs");

function organizarProductos(productosJSON, categoriasJSON) {
  const productos = JSON.parse(productosJSON);
  const categorias = JSON.parse(categoriasJSON);
  const resultado = {};

  categorias.forEach((categoria) => {
    resultado[categoria] = productos.filter((producto) =>
      producto.toLowerCase().includes(categoria.toLowerCase())
    );
  });

  console.log(resultado);
}

// Ejemplos de archivos JSON
const productosJSON = JSON.stringify([
  "Manzana Roja",
  "Banana Amarilla",
  "Leche Deslactosada",
  "Yogur Natural",
  "Aceite de Oliva",
  "Pan Integral",
  123,
]);

const categoriasJSON = JSON.stringify([
  "fruta 1",
  "leche",
  "pan",
  "aceite",
  "atun",
]);

organizarProductos(productosJSON, categoriasJSON);
