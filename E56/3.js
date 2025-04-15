const projectTasks = [
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

function addTask(taskID, taskName, assignedTo, dueDate, status, priority) {
  const newTask = {
    taskID,
    taskName,
    assignedTo,
    dueDate,
    status,
    priority,
  };
  projectTasks.push(newTask);
  console.log(`Tarea agregada: ${taskName}`);
}

function filterTasks(status, priority) {
  const filteredTasks = projectTasks.filter((task) => {
    return task.status === status && task.priority === priority;
  });

  if (filteredTasks.length === 0) {
    return {
      message: "No se encontraron tareas que coincidan con los criterios",
    };
  }

  return JSON.stringify(filteredTasks, null, 2);
}

// Ejemplos de uso
addTask(4, "Integración", "David", "2024-02-25", "en progreso", "alta");

console.log(projectTasks);
console.log(filterTasks("no iniciado", "media"));
console.log(filterTasks("completado", "baja"));
console.log(filterTasks("en progreso", "alta"));
console.log(filterTasks("no iniciado", "baja"));
