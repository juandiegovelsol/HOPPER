let codeSnippets = {};

// Función para agregar un nuevo fragmento de código
function addSnippet(id, language, description, code) {
  codeSnippets[id] = { language, description, code };
}

// Función para recuperar un fragmento por ID
function getSnippetById(id) {
  const snippet = codeSnippets[id];
  if (snippet) {
    return JSON.stringify({ id, ...snippet }, null, 2);
  } else {
    return JSON.stringify({ message: "Fragmento no encontrado" });
  }
}

// Función para enumerar todos los fragmentos de un lenguaje específico
function listSnippetsByLanguage(language) {
  const snippets = Object.values(codeSnippets).filter(
    (snippet) => snippet.language === language
  );
  return JSON.stringify(snippets, null, 2);
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
addSnippet(
  "4",
  "JavaScript",
  "Función para sumar dos números",
  "function add(a, b) { return a + b; }"
);

console.log(codeSnippets);
console.log(getSnippetById("2")); // Salida: Fragmento con ID "2"
console.log(getSnippetById("4")); // Salida: Fragmento no encontrado
console.log(listSnippetsByLanguage("JavaScript")); // Salida: Fragmento con ID "1"
