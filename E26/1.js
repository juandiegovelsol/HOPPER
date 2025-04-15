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

function addSnippet(id, language, description, code) {
  if (!codeSnippets[id]) {
    codeSnippets[id] = { language, description, code };
    console.log(`Fragmento agregado exitosamente: ${id}`);
  } else {
    console.log(`El fragmento con ID ${id} ya existe.`);
  }
}

function getSnippet(id) {
  if (codeSnippets[id]) {
    return JSON.stringify(codeSnippets[id], null, 2);
  } else {
    return JSON.stringify({ message: "Fragmento no encontrado" });
  }
}

function listSnippets(language) {
  return codeSnippets[language] || [];
}

// Ejemplos de uso
addSnippet(
  "4",
  "JavaScript",
  "Función para multiplicar dos números",
  "function multiply(a, b) { return a * b; }"
);
console.log(getSnippet("2"));
console.log(getSnippet("9"));
console.log(listSnippets("Python"));
console.log(listSnippets("JavaScript"));
