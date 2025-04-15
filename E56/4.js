// Definir la matriz de tareas
let projectTasks = [
  {
    taskID: 1,
    taskName: "Diseño de maqueta",
    assignedTo: "Alice",
    dueDate: "2024-02-01",
    status: "en progreso",
    priority: "alta",
  },
  {
    taskID: 2,
    taskName: "Desarrollar API",
    assignedTo: "Bob",
    dueDate: "2024-02-15",
    status: "no iniciado",
    priority: "media",
  },
  {
    taskID: 3,
    taskName: "Pruebas",
    assignedTo: "Charlie",
    dueDate: "2024-02-20",
    status: "completado",
    priority: "baja",
  },
];

// Función para filtrar tareas por estado y prioridad
function filterTasks(state, priority) {
  const filteredTasks = projectTasks.filter((task) => {
    return task.status === state && task.priority === priority;
  });

  // Si no se encontraron tareas, devolver un mensaje
  if (filteredTasks.length === 0) {
    return {
      message: "No se encontraron tareas que coincidan con los criterios.",
    };
  }

  return filteredTasks;
}

// Ejemplo de uso
const filteredTasks = filterTasks("no iniciado", "media");
console.log(JSON.stringify(filteredTasks, null, 2));
