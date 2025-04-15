const fs = require("fs");

class TaskManager {
  constructor(filename = "tasks.json") {
    this.filename = filename;
    this.tasks = this.loadTasks();
  }

  loadTasks() {
    return fs.existsSync(this.filename)
      ? JSON.parse(fs.readFileSync(this.filename, "utf8"))
      : [];
  }

  saveTasks() {
    try {
      fs.writeFileSync(
        this.filename,
        JSON.stringify(this.tasks, null, 4),
        "utf8"
      );
    } catch (error) {
      console.error("Error al guardar las tareas:", error);
    }
  }

  addTask(description) {
    if (description.trim() === "") {
      console.error("La descripción de la tarea no puede estar vacía.");
      return;
    }
    this.tasks.push({
      id: this.tasks.length + 1,
      description,
      completed: false,
    });
    this.saveTasks();
  }

  listTasks() {
    console.log("\nLista de tareas:");
    this.tasks.forEach((task) =>
      console.log(
        `${task.id}. [${task.completed ? "X" : " "}] ${task.description}`
      )
    );
  }

  completeTask(id) {
    const task = this.tasks.find((t) => t.id === id);
    if (!task) {
      console.error("ID de tarea no válido.");
      return;
    }
    task.completed = true;
    this.saveTasks();
  }

  deleteTask(id) {
    const taskIndex = this.tasks.findIndex((t) => t.id === id);
    if (taskIndex === -1) {
      console.error("ID de tarea no válido.");
      return;
    }
    this.tasks.splice(taskIndex, 1);
    this.saveTasks();
  }

  run() {
    console.log("\nGestor de Tareas - Opciones:");
    console.log("1. Agregar tarea");
    console.log("2. Listar tareas");
    console.log("3. Marcar tarea como completada");
    console.log("4. Eliminar tarea");
    console.log("5. Salir");

    const readline = require("readline").createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    readline.question("\nElige una opción: ", (option) => {
      readline.pause(); // Pausar el input para manejarlo en los callbacks

      if (option === "1") {
        readline.question("Escribe la tarea: ", (description) => {
          this.addTask(description);
          readline.close();
          this.run();
        });
      } else if (option === "2") {
        this.listTasks();
        this.run(); // No hay necesidad de cerrar readline antes de un nuevo run
      } else if (option === "3") {
        readline.question("Ingresa el ID de la tarea completada: ", (id) => {
          const parsedId = parseInt(id);
          if (isNaN(parsedId) || parsedId < 1) {
            console.error("Por favor, ingresa un ID válido.");
            readline.close();
            this.run();
            return;
          }
          this.completeTask(parsedId);
          readline.close();
          this.run();
        });
      } else if (option === "4") {
        readline.question("Ingresa el ID de la tarea a eliminar: ", (id) => {
          const parsedId = parseInt(id);
          if (isNaN(parsedId) || parsedId < 1) {
            console.error("Por favor, ingresa un ID válido.");
            readline.close();
            this.run();
            return;
          }
          this.deleteTask(parsedId);
          readline.close();
          this.run();
        });
      } else if (option === "5") {
        console.log("Saliendo...");
        readline.close();
      } else {
        console.error("Opción no válida. Inténtalo de nuevo.");
        this.run(); // Reiniciar el ciclo si la opción no es válida
      }
    });
  }
}

const manager = new TaskManager();
manager.run();
