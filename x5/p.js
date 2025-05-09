class Nodo {
  constructor(x, y, transitable = true) {
    this.x = x;
    this.y = y;
    this.transitable = transitable;
    this.g = 0;
    this.h = 0;
    this.f = 0;
    this.padre = null;
  }
}

class AEstrella {
  constructor(mapa, inicio, fin) {
    this.mapa = mapa;
    this.inicio = inicio;
    this.fin = fin;
    this.abiertos = [inicio];
    this.cerrados = [];
  }

  heuristica(a, b) {
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
  }

  vecinos(nodo) {
    const direcciones = [
      [0, -1],
      [1, 0],
      [0, 1],
      [-1, 0],
    ];
    const vecinos = [];

    for (let [dx, dy] of direcciones) {
      let x = nodo.x + dx;
      let y = nodo.y + dy;
      if (
        y >= 0 &&
        y < this.mapa.length &&
        x >= 0 &&
        x < this.mapa[0].length &&
        this.mapa[y][x].transitable
      ) {
        vecinos.push(this.mapa[y][x]);
      }
    }

    return vecinos;
  }

  ejecutar() {
    while (this.abiertos.length > 0) {
      let menor = 0;
      for (let i = 1; i < this.abiertos.length; i++) {
        if (this.abiertos[i].f < this.abiertos[menor].f) {
          menor = i;
        }
      }

      let actual = this.abiertos[menor];

      if (actual === this.fin) {
        const camino = [];
        let temp = actual;
        while (temp.padre) {
          camino.push(temp);
          temp = temp.padre;
        }
        return camino.reverse();
      }

      this.abiertos.splice(menor, 1);
      this.cerrados.push(actual);

      const vecinos = this.vecinos(actual);
      for (let vecino of vecinos) {
        if (this.cerrados.includes(vecino)) continue;

        let gTemporal = actual.g + 1;

        if (!this.abiertos.includes(vecino)) {
          this.abiertos.push(vecino);
        } else if (gTemporal >= vecino.g) {
          continue;
        }

        vecino.g = gTemporal;
        vecino.h = this.heuristica(vecino, this.fin);
        vecino.f = vecino.g + vecino.h;
        vecino.padre = actual;
      }
    }

    return null;
  }
}

function simular(datosMapa, coordInicio, coordFin) {
  const mapa = datosMapa.map((fila, y) =>
    fila.map((valor, x) => new Nodo(x, y, valor === 0))
  );
  const inicio = mapa[coordInicio[1]][coordInicio[0]];
  const fin = mapa[coordFin[1]][coordFin[0]];

  const algoritmo = new AEstrella(mapa, inicio, fin);
  const camino = algoritmo.ejecutar();

  console.log("Mapa:");
  for (let y = 0; y < mapa.length; y++) {
    let fila = "";
    for (let x = 0; x < mapa[0].length; x++) {
      const celda = mapa[y][x];
      if (celda === inicio) fila += "I ";
      else if (celda === fin) fila += "F ";
      else if (!celda.transitable) fila += "█ ";
      else if (camino && camino.find((p) => p.x === x && p.y === y))
        fila += "* ";
      else fila += ". ";
    }
    console.log(fila);
  }

  if (camino) {
    console.log("\nCamino encontrado:");
    console.log(camino.map((p) => `[${p.x}, ${p.y}]`).join(" → "));
  } else {
    console.log("\nNo se encontró un camino.");
  }
}

const escenario = [
  [0, 0, 0, 0, 1],
  [1, 1, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 1, 0],
];

const inicio = [0, 0];
const fin = [4, 4];

simular(escenario, inicio, fin);
