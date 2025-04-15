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

function filterTasks(status, priority) {
  return projectTasks.filter((task) => {
    return task.status === status && task.priority === priority;
  });
}

function generateJSON(tasks) {
  return JSON.stringify(tasks, null, 2);
}

// Ejemplo de uso
const filteredTasks = filterTasks("no iniciado", "media");
const jsonResult = generateJSON(filteredTasks);
console.log(jsonResult);
