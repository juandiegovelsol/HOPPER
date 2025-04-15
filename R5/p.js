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
    this.tasks.find((t) => t.id === id).completed = true;
    this.saveTasks();
  }

  deleteTask(id) {
    this.tasks = this.tasks.filter((t) => t.id !== id);
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
      if (option === "1") {
        readline.question("Escribe la tarea: ", (description) => {
          this.addTask(description);
          readline.close();
          this.run();
        });
      } else if (option === "2") {
        this.listTasks();
        readline.close();
        this.run();
      } else if (option === "3") {
        readline.question("Ingresa el ID de la tarea completada: ", (id) => {
          this.completeTask(parseInt(id));
          readline.close();
          this.run();
        });
      } else if (option === "4") {
        readline.question("Ingresa el ID de la tarea a eliminar: ", (id) => {
          this.deleteTask(parseInt(id));
          readline.close();
          this.run();
        });
      } else if (option === "5") {
        console.log("Saliendo...");
        readline.close();
      } else {
        readline.close();
        this.run();
      }
    });
  }
}

const manager = new TaskManager();
manager.run();
