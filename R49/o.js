class TodoApp {
  constructor() {
    this.tasks = [];
    this.loadTasks();
    this.setupEventListeners();
  }

  loadTasks() {
    this.tasks = JSON.parse(localStorage.getItem("tasks") || "[]");
    this.renderTasks();
  }

  saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(this.tasks));
  }

  addTask(taskText) {
    if (!taskText) return;
    const task = { text: taskText, completed: false };
    this.tasks.push(task);
    this.saveTasks();
    this.renderTasks();
  }

  deleteTask(index) {
    this.tasks.splice(index, 1);
    this.saveTasks();
    this.renderTasks();
  }

  renderTasks() {
    const list = document.getElementById("taskList");
    list.innerHTML = "";
    this.tasks.forEach((task, index) => {
      const li = document.createElement("li");
      li.textContent = task.text;

      const deleteButton = document.createElement("button");
      deleteButton.textContent = "Eliminar";
      deleteButton.addEventListener("click", () => this.deleteTask(index));

      li.appendChild(deleteButton);
      list.appendChild(li);
    });
  }

  setupEventListeners() {
    document.getElementById("addTaskButton").addEventListener("click", () => {
      const input = document.getElementById("taskInput");
      this.addTask(input.value);
      input.value = "";
    });
  }
}

// Inicializar la aplicación
const app = new TodoApp();
