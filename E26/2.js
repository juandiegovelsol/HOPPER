// Objeto para almacenar fragmentos de código
let codeSnippets = {};

// Función para agregar un nuevo fragmento de código
function addCodeSnippet(id, language, description, code) {
  // Validar que todos los campos estén presentes y sean válidos
  if (!id || !language || !description || !code) {
    return { message: "Todos los campos son requeridos" };
  }

  // Validar que el ID no esté duplicado
  if (codeSnippets[id]) {
    return { message: "ID ya existe" };
  }

  // Agregar el fragmento al objeto
  codeSnippets[id] = { language, description, code };
  return { message: "Fragmento agregado exitosamente" };
}

// Función para recuperar un fragmento de código por su ID
function getCodeSnippet(id) {
  // Verificar si el ID existe en el objeto
  if (!codeSnippets[id]) {
    return { message: "Fragmento no encontrado" };
  }

  // Devolver el fragmento en formato JSON
  return JSON.stringify(codeSnippets[id], null, 2);
}

// Función para enumerar todos los fragmentos de código en un lenguaje específico
function listCodeSnippets(language) {
  // Filtrar los fragmentos por el lenguaje especificado
  const filteredSnippets = Object.keys(codeSnippets).filter(
    (id) => codeSnippets[id].language === language
  );

  // Si no hay fragmentos en el lenguaje especificado, devolver un mensaje adecuado
  if (filteredSnippets.length === 0) {
    return { message: `No hay fragmentos en ${language}` };
  }

  // Devolver los fragmentos en formato JSON
  return JSON.stringify(filteredSnippets, null, 2);
}

// Ejemplo de uso
console.log(
  addCodeSnippet(
    "1",
    "JavaScript",
    "Función para sumar dos números",
    "function add(a, b) { return a + b; }"
  )
); // { message: "Fragmento agregado exitosamente" }
console.log(getCodeSnippet("1")); // { "id": "1", "language": "JavaScript", "description": "Función para sumar dos números", "code": "function add(a, b) { return a + b; }" }
console.log(listCodeSnippets("JavaScript")); // [ { "id": "1", "language": "JavaScript", "description": "Función para sumar dos números", "code": "function add(a, b) { return a + b; }" } ]
console.log(getCodeSnippet("2")); // { "id": "2", "language": "Python", "description": "Función para sumar dos números", "code": "def add(a, b): return a + b" }
console.log(listCodeSnippets("Python")); // [ { "id": "2", "language": "Python", "description": "Función para sumar dos números", "code": "def add(a, b): return a + b" } ]
console.log(getCodeSnippet("3")); // { message: "Fragmento no encontrado" }
console.log(listCodeSnippets("Java")); // { message: "No hay fragmentos en Java" }
