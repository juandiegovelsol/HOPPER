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
  return codeSnippets[id]
    ? JSON.stringify({
        id,
        language: codeSnippets[id].language,
        description: codeSnippets[id].description,
        code: codeSnippets[id].code,
      })
    : JSON.stringify({ message: "Fragmento no encontrado" });
}

// Función para enumerar todos los fragmentos de un lenguaje específico
function enumerateSnippetsByLanguage(language) {
  return codeSnippets
    ? codeSnippets[language]
      ? codeSnippets[language].split(/\n/g).map((snippet) => ({
          id: Object.keys(codeSnippets)[
            codeSnippets[language].indexOf(snippet) + 1
          ],
          language,
          description: snippet.match(/\s*description:\s*(.*)/)[1] || "",
          code: snippet.match(/\s*code:\s*(.*)/)[1] || "",
        }))
      : []
    : [];
}

// Ejemplo de uso
console.log(getSnippetById("2")); // JSON con fragmento encontrado
console.log(getSnippetById("1")); // JSON con mensaje de fragmento no encontrado
console.log(enumerateSnippetsByLanguage("JavaScript")); // JSON con fragmentos en JavaScript

console.log(codeSnippets[1]);
