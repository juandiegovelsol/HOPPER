const fs = require("fs");

const validarArchivos = (productos, categorias) => {
  if (!Array.isArray(productos)) {
    throw new Error("El archivo de productos debe contener un array");
  }

  if (!Array.isArray(categorias)) {
    throw new Error("El archivo de categorías debe contener un array");
  }

  productos.forEach((producto, index) => {
    if (typeof producto !== "string" || producto.trim() === "") {
      throw new Error(
        `Producto inválido en posición ${index}: debe ser una string no vacía`
      );
    }
  });

  categorias.forEach((categoria, index) => {
    if (typeof categoria !== "string" || categoria.trim() === "") {
      throw new Error(
        `Categoría inválida en posición ${index}: debe ser una string no vacía`
      );
    }
    if (/\s/.test(categoria)) {
      throw new Error(
        `Categoría inválida en posición ${index}: no debe contener espacios`
      );
    }
  });

  return true;
};

const categorizarProductos = (productos, categorias) => {
  const categorizado = categorias.reduce((acc, categoria) => {
    acc[categoria] = [];
    return acc;
  }, {});

  productos.forEach((producto) => {
    const categoriaEncontrada = categorias.find((categoria) =>
      producto.toLowerCase().includes(categoria.toLowerCase())
    );

    if (categoriaEncontrada) {
      categorizado[categoriaEncontrada].push(producto);
    } else {
      categorizado["Otros"] = categorizado["Otros"] || [];
      categorizado["Otros"].push(producto);
    }
  });

  return categorizado;
};

const organizarProductosPorCategoria = async () => {
  try {
    const datosProductos = fs.readFileSync("productos.json");
    const productos = JSON.parse(datosProductos);

    const datosCategorias = fs.readFileSync("categorias.json");
    const categorias = JSON.parse(datosCategorias);

    validarArchivos(productos, categorias);

    const productosCategorizados = categorizarProductos(productos, categorias);

    console.log(productosCategorizados);
  } catch (error) {
    console.error("Error al procesar los archivos:", error);
  }
};

organizarProductosPorCategoria();
