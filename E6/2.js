let codeSnippets = {};

// Función para agregar un nuevo fragmento de código
function addSnippet(id, language, description, code) {
  if (codeSnippets[id]) {
    console.log("Error: El ID del fragmento ya existe.");
    return;
  }
  codeSnippets[id] = { language, description, code };
  console.log(`Fragmento añadido con ID: ${id}`);
}

// Función para recuperar un fragmento por su ID
function getSnippetById(id) {
  const snippet = codeSnippets[id];
  if (snippet) {
    return JSON.stringify({ id, ...snippet }, null, 2);
  } else {
    return JSON.stringify({ message: "Fragmento no encontrado" });
  }
}

// Función para listar todos los fragmentos de un lenguaje específico
function listSnippetsByLanguage(language) {
  const filteredSnippets = Object.values(codeSnippets).filter(
    (snippet) => snippet.language.toLowerCase() === language.toLowerCase()
  );
  if (filteredSnippets.length > 0) {
    return JSON.stringify(filteredSnippets, null, 2);
  } else {
    return JSON.stringify({
      message: `No se encontraron fragmentos en ${language}`,
    });
  }
}

// Ejemplos de uso
addSnippet(
  "1",
  "JavaScript",
  "Función para sumar dos números",
  "function add(a, b) { return a + b; }"
);
addSnippet(
  "2",
  "Python",
  "Función para sumar dos números",
  "def add(a, b): return a + b"
);
addSnippet(
  "3",
  "Java",
  "Función para sumar dos números",
  "public int add(int a, int b) { return a + b; }"
);

console.log(getSnippetById("2")); // Salida del fragmento con ID "2"
console.log(getSnippetById("4")); // Mensaje de fragmento no encontrado
console.log(listSnippetsByLanguage("JavaScript")); // Lista de fragmentos en JavaScript
console.log(listSnippetsByLanguage("Ruby")); // Mensaje de no encontrar fragmentos en Ruby
