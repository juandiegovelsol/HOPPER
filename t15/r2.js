const fs = require("fs");

// Función para categorizar los productos
const categorizarProductos = (productos, categorias) => {
  // Crea un objeto para almacenar los productos por categoría
  const categorizado = categorias.reduce((acc, categoria) => {
    acc[categoria] = [];
    return acc;
  }, {});

  // Itera sobre cada producto para asignarlo a una categoría
  productos.forEach((producto) => {
    // Para cada producto, busca la primera categoría que coincida
    const categoriaEncontrada = categorias.find((categoria) =>
      producto.toLowerCase().includes(categoria.toLowerCase())
    );
    if (categoriaEncontrada) {
      // Si se encuentra una categoría, agrega el producto a esa categoría
      categorizado[categoriaEncontrada].push(producto);
    } else {
      // Si no se encuentra categoría, agrega el producto a 'Otros'
      categorizado["Otros"] = categorizado["Otros"] || [];
      categorizado["Otros"].push(producto);
    }
  });

  return categorizado;
};

// Función para leer los archivos JSON y categorizar los productos
const organizarProductosPorCategoria = async () => {
  try {
    // Lee el archivo de productos
    const datosProductos = fs.readFileSync("productos.json");
    const productos = JSON.parse(datosProductos);

    // Lee el archivo de categorías
    const datosCategorias = fs.readFileSync("categorias.json");
    const categorias = JSON.parse(datosCategorias);

    // Categoriza los productos
    const productosCategorizados = categorizarProductos(productos, categorias);

    // Imprime los productos categorizados
    console.log(productosCategorizados);
  } catch (error) {
    console.error("Error al procesar los archivos:", error);
  }
};

// Ejecuta el proceso de organización de productos
organizarProductosPorCategoria();
