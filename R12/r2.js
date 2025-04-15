// Define la matriz del supermercado y la lista de compras
const supermercado = [];
let contador = 0;
for (let i = 0; i < 8; i++) {
  const fila = [];
  for (let j = 0; j < 8; j++) {
    fila.push(contador++);
  }
  supermercado.push(fila);
}

// Define los productos con sus coordenadas en la matriz
const listaDeCompras = [
  { nombre: "Leche", coordenadas: { x: 2, y: 5 } },
  { nombre: "Pan", coordenadas: { x: 6, y: 3 } },
  { nombre: "Huevos", coordenadas: { x: 4, y: 7 } },
  { nombre: "Manzanas", coordenadas: { x: 1, y: 2 } },
];

// Función para calcular la distancia Manhattan entre dos puntos
const distanciaManhattan = (x1, y1, x2, y2) =>
  Math.abs(x1 - x2) + Math.abs(y1 - y2);

// Función para encontrar la ruta más óptima usando un enfoque voraz
const encontrarRutaOptima = () => {
  const inicio = { x: 0, y: 0 }; // Punto de partida en la entrada del supermercado
  let ruta = []; // Almacena la ruta optimizada
  let posicionesVisitadas = new Set(); // Un conjunto para rastrear las posiciones visitadas
  posicionesVisitadas.add(`${inicio.x},${inicio.y}`);

  let posicionActual = inicio;

  while (ruta.length < listaDeCompras.length) {
    let productoMasCercano = null;
    let distanciaMasCorta = Infinity;

    // Encuentra el producto más cercano no visitado
    for (const producto of listaDeCompras) {
      if (
        !posicionesVisitadas.has(
          `${producto.coordenadas.x},${producto.coordenadas.y}`
        )
      ) {
        const distancia = distanciaManhattan(
          posicionActual.x,
          posicionActual.y,
          producto.coordenadas.x,
          producto.coordenadas.y
        );
        if (distancia < distanciaMasCorta) {
          distanciaMasCorta = distancia;
          productoMasCercano = producto;
        }
      }
    }

    // Si se encontró un producto más cercano, agrégalo a la ruta
    if (productoMasCercano) {
      ruta.push(productoMasCercano);
      posicionActual = productoMasCercano.coordenadas;
      posicionesVisitadas.add(`${posicionActual.x},${posicionActual.y}`);
    }
  }

  return ruta;
};

// Encuentra y muestra la ruta optimizada
const rutaOptima = encontrarRutaOptima();
console.log("Ruta optimizada para recoger los productos:");
rutaOptima.forEach((producto, indice) => {
  console.log(
    `${indice + 1}. ${producto.nombre} en posición (${
      producto.coordenadas.x
    }, ${producto.coordenadas.y})`
  );
});
