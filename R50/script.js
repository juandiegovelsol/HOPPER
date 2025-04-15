let editor = document.getElementById("editor");

// Historial para deshacer y rehacer
let undoStack = [];
let redoStack = [];
let isTyping = false;

// Función para aplicar formato al texto seleccionado
function formatText(command) {
  document.execCommand(command, false, null);
  saveState();
}

// Guardar el estado actual del contenido del editor
function saveState() {
  if (isTyping) {
    undoStack.push(editor.innerHTML);
    redoStack = []; // Limpiar el redo stack al añadir nuevo estado
  }
  isTyping = true;
}

// Función para deshacer cambios
function undo() {
  if (undoStack.length > 0) {
    redoStack.push(editor.innerHTML);
    editor.innerHTML = undoStack.pop();
  }
}

// Función para rehacer cambios
function redo() {
  if (redoStack.length > 0) {
    undoStack.push(editor.innerHTML);
    editor.innerHTML = redoStack.pop();
  }
}

// Guardar texto en localStorage
function saveText() {
  localStorage.setItem("editorContent", editor.innerHTML);
}

// Cargar texto de localStorage al cargar la página
window.onload = function () {
  const savedContent = localStorage.getItem("editorContent");
  if (savedContent) {
    editor.innerHTML = savedContent;
  }
};
