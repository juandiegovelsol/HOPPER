// Objeto para almacenar los fragmentos de código
let codeSnippets = {
  1: {
    language: "JavaScript",
    description: "Función para sumar dos números",
    code: "function add(a, b) { return a + b; }",
  },
  2: {
    language: "Python",
    description: "Función para sumar dos números",
    code: "def add(a, b): return a + b",
  },
  3: {
    language: "Java",
    description: "Función para sumar dos números",
    code: "public int add(int a, int b) { return a + b; }",
  },
};

// Función para recuperar un fragmento por su ID
function getSnippetById(id) {
  const snippet = codeSnippets[id];
  if (snippet) {
    return JSON.stringify({
      id,
      language: snippet.language,
      description: snippet.description,
      code: snippet.code,
    });
  } else {
    return JSON.stringify({
      message: "Fragmento no encontrado",
    });
  }
}

// Función para enumerar todos los fragmentos de un lenguaje específico
function enumerateSnippetsByLanguage(language) {
  return codeSnippets
    .filter((snippet) => snippet.language === language)
    .map((snippet) => ({
      id: snippet.id,
      language: snippet.language,
      description: snippet.description,
      code: snippet.code,
    }));
}

// Ejemplos de uso
console.log(getSnippetById("2")); // JSON con el fragmento de Python
console.log(getSnippetById("99")); // JSON indicando que el fragmento no fue encontrado
console.log(enumerateSnippetsByLanguage("JavaScript")); // Lista de fragmentos en JavaScript
