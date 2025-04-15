const express = require("express");
const app = express();
const PORT = 3000;

app.use(express.json());

const categoriasPredefinidas = {
  Alimentos: {
    keywords: ["manzana", "banana", "pan", "arroz", "carne"],
    precio: 250,
  },
  Electrónica: {
    keywords: ["celular", "televisor", "computador", "tablet"],
    precio: 1500,
  },
  Ropa: {
    keywords: ["polera", "pantalón", "zapato", "chaqueta"],
    precio: 500,
  },
};

function clasificarProducto(producto) {
  const nombreLower = producto.nombre.toLowerCase();
  for (const [categoria, datos] of Object.entries(categoriasPredefinidas)) {
    for (const keyword of datos.keywords) {
      if (nombreLower.includes(keyword)) {
        return categoria;
      }
    }
  }
  return "Otros";
}

app.post("/ventas", (req, res) => {
  const productos = req.body.productos;
  if (!Array.isArray(productos) || productos.length === 0) {
    return res
      .status(400)
      .json({ error: "La lista de productos debe ser un arreglo no vacío." });
  }
  for (let i = 0; i < productos.length; i++) {
    const producto = productos[i];
    if (
      !producto.nombre ||
      typeof producto.nombre !== "string" ||
      producto.nombre.trim() === ""
    ) {
      return res.status(400).json({
        error: `El producto en la posición ${i} debe tener un nombre no vacío.`,
      });
    }
    if (
      typeof producto.cantidad !== "number" ||
      !Number.isInteger(producto.cantidad) ||
      producto.cantidad < 0
    ) {
      return res.status(400).json({
        error: `El producto en la posición ${i} debe tener una cantidad entera mayor o igual a cero.`,
      });
    }
  }
  const resultado = {};
  for (const categoria in categoriasPredefinidas) {
    resultado[categoria] = { productos: [], subtotal: 0 };
  }
  resultado["Otros"] = { productos: [], subtotal: 0 };
  productos.forEach((producto) => {
    const categoria = clasificarProducto(producto);
    const precio = categoriasPredefinidas[categoria]
      ? categoriasPredefinidas[categoria].precio
      : 0;
    const subtotalProducto = precio * producto.cantidad;
    resultado[categoria].productos.push({
      nombre: producto.nombre,
      cantidad: producto.cantidad,
      precio: precio,
      subtotal: subtotalProducto,
    });
    resultado[categoria].subtotal += subtotalProducto;
  });
  res.json({ categorias: resultado });
});

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
