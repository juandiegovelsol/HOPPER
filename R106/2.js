class Node {
  constructor(value) {
    this.value = value;
    this.neighbors = [];
  }
}

class Graph {
  constructor() {
    this.nodesMap = new Map();
  }

  addNode(value) {
    if (!this.nodesMap.has(value)) {
      this.nodesMap.set(value, new Node(value));
    }
    return this;
  }

  removeNode(value) {
    if (this.nodesMap.has(value)) {
      const nodeToRemove = this.nodesMap.get(value);

      // Remove connections
      nodeToRemove.neighbors.forEach((neighbor) =>
        neighbor.neighbors.splice(neighbor.neighbors.indexOf(nodeToRemove), 1)
      );

      // Remove isolated node connections
      this.nodesMap.forEach((node, key) => {
        node.neighbors = node.neighbors.filter((n) => n !== nodeToRemove);
      });

      this.nodesMap.delete(value);
    }
    return this;
  }

  addEdge(value1, value2) {
    if (this.nodesMap.has(value1) && this.nodesMap.has(value2)) {
      const node1 = this.nodesMap.get(value1);
      const node2 = this.nodesMap.get(value2);

      if (!node1.neighbors.some((n) => n.value === value2)) {
        node1.neighbors.push(node2);
        node2.neighbors.push(node1); // Undirected graph
      }
    }
    return this;
  }

  removeEdge(value1, value2) {
    if (this.nodesMap.has(value1) && this.nodesMap.has(value2)) {
      const node1 = this.nodesMap.get(value1);
      const node2 = this.nodesMap.get(value2);

      node1.neighbors = node1.neighbors.filter((n) => n.value !== value2);
      node2.neighbors = node2.neighbors.filter((n) => n.value !== value1);
    }
    return this;
  }

  getNodes() {
    return Array.from(this.nodesMap.keys());
  }
}

// 1. Crear un grafo y añadir nodos
const g1 = new Graph();
g1.addNode("A").addNode("B").addNode("C");
console.log(g1.getNodes());
// → ['A', 'B', 'C']

// 2. Añadir aristas (edges) y ver sus vecinos
g1.addEdge("A", "B").addEdge("B", "C");

// Vecinos de 'A'
console.log(g1.nodesMap.get("A").neighbors.map((n) => n.value));
// → ['B']

// Vecinos de 'B'
console.log(g1.nodesMap.get("B").neighbors.map((n) => n.value));
// → ['A', 'C']

// 3. Prevenir duplicados al añadir la misma arista varias veces
g1.addEdge("A", "B");
console.log(g1.nodesMap.get("A").neighbors.map((n) => n.value));
// → ['B']  (sigue habiendo sólo una conexión A–B)

// 4. Eliminar una arista y comprobar que se rompe en ambos sentidos
g1.removeEdge("A", "B");

console.log(g1.nodesMap.get("A").neighbors.map((n) => n.value));
// → []

console.log(g1.nodesMap.get("B").neighbors.map((n) => n.value));
// → ['C']
