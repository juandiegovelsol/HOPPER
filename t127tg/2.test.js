const fs = require("fs");
const path = require("path");

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

module.exports = TaskTracker;

// Pruebas unitarias
const assert = require("assert"); // Para hacer las validaciones de las pruebas
const path = require("path"); // Para obtener la ruta del archivo
const fs = require("fs"); // Para el manejo de archivos

// Crear una instancia de TaskTracker
const tracker = new TaskTracker();

describe("Pruebas de TaskTracker", () => {
  // Antes de todas las pruebas, crear un archivo de prueba
  beforeEach(() => {
    const filePath = path.join(__dirname, "tareas.json");
    const data = [
      { descripcion: "Estudiar Node.js", persona: "Juan", entregada: false },
      { descripcion: "Hacer ejercicio", persona: "Ana", entregada: true },
      { descripcion: "Leer un libro", persona: "Pedro", entregada: false },
    ];
    return fs.promises.writeFile(filePath, JSON.stringify(data));
  });

  it("Debe cargar y validar tareas correctamente desde el archivo JSON", () => {
    const filePath = path.join(__dirname, "tareas.json");
    const result = tracker.loadTasks(filePath);

    // Validar que las tareas se carguen correctamente
    assert.strictEqual(result, true);
    assert.strictEqual(tracker.getResumen().total, 3);
    assert.strictEqual(tracker.getResumen().entregadas, 1);
    assert.strictEqual(tracker.getResumen().pendientes, 2);
  });

  // Después de todas las pruebas, borrar el archivo creado
  afterEach(() => {
    const filePath = path.join(__dirname, "tareas.json");
    return fs.promises.unlink(filePath);
  });
});
