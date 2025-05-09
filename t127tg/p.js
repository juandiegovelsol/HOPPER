const fs = require("fs");

class TaskTracker {
  constructor() {
    this.tasks = [];
  }

  loadTasks(filePath) {
    try {
      const data = fs.readFileSync(filePath, "utf8");
      const tasks = JSON.parse(data);

      if (!Array.isArray(tasks)) {
        throw new Error("El archivo JSON debe contener un arreglo de tareas");
      }

      this.tasks = tasks.filter((task) => this.validateTask(task));
      return true;
    } catch (error) {
      console.error(`Error al cargar las tareas: ${error.message}`);
      return false;
    }
  }

  validateTask(task) {
    if (!task) {
      console.error("Alerta: Tarea nula o indefinida");
      return false;
    }

    if (typeof task !== "object") {
      console.error("Alerta: Tarea no es un objeto");
      return false;
    }

    if (!task.descripcion || typeof task.descripcion !== "string") {
      console.error("Alerta: Descripción inválida o vacía");
      return false;
    }

    if (!task.persona || typeof task.persona !== "string") {
      console.error("Alerta: Persona inválida o vacía");
      return false;
    }

    if (typeof task.entregada !== "boolean") {
      console.error("Alerta: Estado de entrega inválido");
      return false;
    }

    return true;
  }

  getResumen() {
    const total = this.tasks.length;
    const entregadas = this.tasks.filter((task) => task.entregada).length;
    const pendientes = total - entregadas;

    return {
      total,
      entregadas,
      pendientes,
    };
  }

  getPersonasConTareasPendientes() {
    const personas = {};

    this.tasks.forEach((task) => {
      if (!task.entregada) {
        if (!personas[task.persona]) {
          personas[task.persona] = 0;
        }
        personas[task.persona]++;
      }
    });

    return personas;
  }

  imprimirResumen() {
    const resumen = this.getResumen();
    console.log("\n--- RESUMEN DE TAREAS ---");
    console.log(`Total de tareas: ${resumen.total}`);
    console.log(`Tareas entregadas: ${resumen.entregadas}`);
    console.log(`Tareas pendientes: ${resumen.pendientes}`);

    console.log("\n--- PERSONAS CON TAREAS PENDIENTES ---");
    const personasPendientes = this.getPersonasConTareasPendientes();

    if (Object.keys(personasPendientes).length === 0) {
      console.log("No hay tareas pendientes");
    } else {
      for (const persona in personasPendientes) {
        console.log(
          `${persona}: ${personasPendientes[persona]} tarea(s) pendiente(s)`
        );
      }
    }
  }
}

const tracker = new TaskTracker();
tracker.loadTasks("./tareas.json");
tracker.imprimirResumen();

module.exports = TaskTracker;
