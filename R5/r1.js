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
    fs.writeFileSync(
      this.filename,
      JSON.stringify(this.tasks, null, 4),
      "utf8"
    );
  }

  addTask(description) {
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
    if (task) {
      task.completed = true;
      this.saveTasks();
    } else {
      console.log(`\nTarea con ID ${id} no encontrada.`);
    }
  }

  deleteTask(id) {
    const initialLength = this.tasks.length;
    this.tasks = this.tasks.filter((t) => t.id !== id);
    if (this.tasks.length < initialLength) {
      this.saveTasks();
      console.log(`\nTarea con ID ${id} eliminada.`);
    } else {
      console.log(`\nTarea con ID ${id} no encontrada.`);
    }
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
      if (option === "1") {
        readline.question("Escribe la tarea: ", (description) => {
          if (description.trim().length === 0) {
            // Verificar si la descripción no está vacía.
            console.log("\nLa descripción de la tarea no puede estar vacía.");
          } else {
            this.addTask(description);
          }
          readline.close();
          this.run();
        });
      } else if (option === "2") {
        this.listTasks();
        readline.close();
        this.run();
      } else if (option === "3") {
        readline.question("Ingresa el ID de la tarea completada: ", (id) => {
          const parsedId = parseInt(id);
          if (isNaN(parsedId)) {
            // Validar que el ID sea un número.
            console.log("\nPor favor, ingresa un ID numérico válido.");
          } else {
            this.completeTask(parsedId);
          }
          readline.close();
          this.run();
        });
      } else if (option === "4") {
        readline.question("Ingresa el ID de la tarea a eliminar: ", (id) => {
          const parsedId = parseInt(id);
          if (isNaN(parsedId)) {
            // Validar que el ID sea un número.
            console.log("\nPor favor, ingresa un ID numérico válido.");
          } else {
            this.deleteTask(parsedId);
          }
          readline.close();
          this.run();
        });
      } else if (option === "5") {
        console.log("Saliendo...");
        readline.close();
      } else {
        console.log("\nOpción no válida. Intenta de nuevo.");
        // Repetir si la opción no es válida.
        readline.close();
        this.run();
      }
    });
  }
}

const manager = new TaskManager();
manager.run();
