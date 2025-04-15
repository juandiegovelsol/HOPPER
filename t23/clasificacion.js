const express = require("express");

const app = express();
const PORT = 3000;

app.use(express.json());

app.post("/clasificar", (req, res) => {
  const prendas = req.body.prendas;

  if (!prendas || !Array.isArray(prendas)) {
    return res.status(400).json({ error: "Se requiere un arreglo de prendas" });
  }

  for (const prenda of prendas) {
    if (typeof prenda !== "string" || prenda.trim() === "") {
      return res
        .status(400)
        .json({ error: "Todas las prendas deben ser cadenas no vacías" });
    }
  }

  const categorias = {
    camisetas: ["polera", "polo", "remera"],
    pantalones: ["pantalón", "blue jean", "jeans", "legging", "pantalones"],
    abrigos: [
      "abrigo",
      "chaqueta",
      "parka",
      "cazadora",
      "sudadera",
      "suéter",
      "chaleco",
    ],
    calzado: ["zapato", "zapatillas", "zapatilla", "bota", "sandalia", "chala"],
    accesorios: [
      "gorro",
      "sombrero",
      "bufanda",
      "guante",
      "cinturón",
      "corbata",
      "pañuelo",
    ],
  };

  const clasificacion = {
    camisetas: [],
    pantalones: [],
    abrigos: [],
    calzado: [],
    accesorios: [],
    otros: [],
  };

  prendas.forEach((prenda) => {
    let categorizado = false;
    const prendaLower = prenda.toLowerCase();

    for (const [categoria, palabrasClave] of Object.entries(categorias)) {
      if (
        !categorizado &&
        palabrasClave.some((palabra) => prendaLower.includes(palabra))
      ) {
        clasificacion[categoria].push(prenda);
        categorizado = true;
      }
    }

    if (!categorizado) {
      clasificacion.otros.push(prenda);
    }
  });

  res.json({ clasificacion });
});

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
