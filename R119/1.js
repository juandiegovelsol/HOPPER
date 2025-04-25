let nodos = [
  { nombre: "A", estadoAnimo: 6 },
  { nombre: "B", estadoAnimo: 8 },
  { nombre: "C", estadoAnimo: 4 },
  // más nodos
];

function ordenarNodos(nivelAnimo) {
  switch (nivelAnimo) {
    case "feliz":
      nodos.sort((a, b) => b.estadoAnimo - a.estadoAnimo);
      break;
    case "medio":
      nodos.sort((a, b) => {
        if (a.estadoAnimo >= 7 && b.estadoAnimo < 7) return -1;
        if (a.estadoAnimo <= 5 && b.estadoAnimo > 5) return -1;
        return b.estadoAnimo - a.estadoAnimo;
      });
      break;
    // Agregar casos para 'triste', 'enojado', etc.
  }
  return nodos;
}

console.log(ordenarNodos("feliz"));

console.log(ordenarNodos("medio"));
