class Nodo {
  constructor(valor) {
    this.valor = valor;
    this.vecinos = [];
  }
}

class Grafo {
  constructor() {
    this.nodos = new Map(); // Map para guardar todos los nodos con sus conexiones
  }

  // Agrega un nuevo nodo al grafo
  agregarNodo(valor) {
    if (!this.nodos.has(valor)) {
      this.nodos.set(valor, new Nodo(valor));
    }
  }

  // Elimina un nodo del grafo
  eliminarNodo(valor) {
    if (this.nodos.has(valor)) {
      const nodoASumar = this.nodos.get(valor);
      // Remover conexión desde los vecinos al nodo eliminado
      nodoASumar.vecinos.forEach((vecino) =>
        this.desconectar(valor, vecino.valor)
      );
      this.nodos.delete(valor);
    }
  }

  // Conecta dos nodos bidireccionalmente
  conectarNodos(valor1, valor2) {
    const nodo1 = this.obtenerNodo(valor1);
    const nodo2 = this.obtenerNodo(valor2);
    if (nodo1 && nodo2) {
      nodo1.agregarVecino(nodo2);
      nodo2.agregarVecino(nodo1);
    }
  }

  // Desconecta dos nodos bidireccionalmente
  desconectarNodos(valor1, valor2) {
    const nodo1 = this.obtenerNodo(valor1);
    const nodo2 = this.obtenerNodo(valor2);
    if (nodo1 && nodo2) {
      nodo1.eliminarVecino(nodo2);
      nodo2.eliminarVecino(nodo1);
    }
  }

  // Devuelve una lista de todos los valores de los nodos en el grafo
  obtenerValoresNodos() {
    return Array.from(this.nodos.keys());
  }

  // Ayudante para obtener un nodo, creándolo si no existe
  obtenerNodo(valor) {
    if (!this.nodos.has(valor)) {
      this.agregarNodo(valor);
    }
    return this.nodos.get(valor);
  }
}

// Uso de pruebas
const grafo = new Grafo();
grafo.agregarNodo("A");
grafo.agregarNodo("B");
grafo.conectarNodos("A", "B");
console.log(grafo.obtenerValoresNodos()); // ['A', 'B']
grafo.eliminarNodo("A");
console.log(grafo.obtenerValoresNodos()); // ['B']
