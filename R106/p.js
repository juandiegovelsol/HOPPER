class Nodo {
  constructor(valor) {
    this.valor = valor;
    this.vecinos = [];
  }
}

class Grafo {
  constructor() {
    this.mapa = new Map();
  }

  agregar(valor) {
    if (!this.mapa.has(valor)) {
      let nodo = new Nodo(valor);
      this.mapa.set(valor, nodo);
    }
  }

  eliminar(valor) {
    if (this.mapa.has(valor)) {
      let nodo = this.mapa.get(valor);

      for (let i = 0; i < nodo.vecinos.length; i++) {
        let vecino = nodo.vecinos[i];
        for (let j = 0; j < vecino.vecinos.length; j++) {
          if (vecino.vecinos[j] === nodo) {
            vecino.vecinos.splice(j, 1);
          }
        }
      }

      this.mapa.delete(valor);

      for (let i = 0; i < nodo.vecinos.length; i++) {
        let vecino = nodo.vecinos[i];
        let existe = false;
        for (let j = 0; j < vecino.vecinos.length; j++) {
          if (vecino.vecinos[j] !== nodo) {
            existe = true;
          }
        }
        if (!existe) {
          this.eliminar(vecino.valor);
        }
      }
    }
  }

  conectar(valor1, valor2) {
    if (this.mapa.has(valor1) && this.mapa.has(valor2)) {
      let nodo1 = this.mapa.get(valor1);
      let nodo2 = this.mapa.get(valor2);

      let encontrado = false;
      for (let i = 0; i < nodo1.vecinos.length; i++) {
        if (nodo1.vecinos[i] === nodo2) {
          encontrado = true;
        }
      }

      if (!encontrado) {
        nodo1.vecinos.push(nodo2);
      }

      encontrado = false;
      for (let i = 0; i < nodo2.vecinos.length; i++) {
        if (nodo2.vecinos[i] === nodo1) {
          encontrado = true;
        }
      }

      if (!encontrado) {
        nodo2.vecinos.push(nodo1);
      }
    }
  }

  desconectar(valor1, valor2) {
    if (this.mapa.has(valor1) && this.mapa.has(valor2)) {
      let nodo1 = this.mapa.get(valor1);
      let nodo2 = this.mapa.get(valor2);

      let i1 = -1,
        i2 = -1;
      for (let i = 0; i < nodo1.vecinos.length; i++) {
        if (nodo1.vecinos[i] === nodo2) {
          i1 = i;
        }
      }

      for (let i = 0; i < nodo2.vecinos.length; i++) {
        if (nodo2.vecinos[i] === nodo1) {
          i2 = i;
        }
      }

      if (i1 !== -1) nodo1.vecinos.splice(i1, 1);
      if (i2 !== -1) nodo2.vecinos.splice(i2, 1);
    }
  }

  obtenerNodos() {
    let arreglo = [];
    for (let clave of this.mapa.keys()) {
      arreglo.push(clave);
    }
    return arreglo;
  }
}

// 1. Crear un grafo y agregar nodos
const g1 = new Grafo();
g1.agregar("A");
g1.agregar("B");
g1.agregar("C");
console.log(g1.obtenerNodos());
// → ['A', 'B', 'C']

// 2. Conectar nodos y ver sus vecinos
g1.conectar("A", "B");
g1.conectar("B", "C");
// Vecinos de 'A':
console.log(g1.mapa.get("A").vecinos.map((n) => n.valor));
// → ['B']
// Vecinos de 'B':
console.log(g1.mapa.get("B").vecinos.map((n) => n.valor));
// → ['A', 'C']

// 3. Intentar duplicar una arista (no debería producir duplicados)
g1.conectar("A", "B");
console.log(g1.mapa.get("A").vecinos.map((n) => n.valor));
// → ['B']  (sigue con un solo 'B')

// 4. Desconectar dos nodos
g1.desconectar("A", "B");
console.log(g1.mapa.get("A").vecinos.map((n) => n.valor));
// → []
console.log(g1.mapa.get("B").vecinos.map((n) => n.valor));
// → ['C']

// 5. Eliminar un nodo sin vecinos restantes
//    Primero conectemos B y C de nuevo
g1.conectar("B", "C");
//    Ahora eliminamos 'B'
g1.eliminar("B");
//    'B' desaparece y 'C' queda aislado, así que también se elimina
console.log(g1.obtenerNodos());
// → []
