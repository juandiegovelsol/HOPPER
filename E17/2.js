const codeSnippets = {};

// Función para agregar un fragmento de código
function addCodeSnippet(id, language, description, code) {
  if (
    typeof id !== "string" ||
    typeof language !== "string" ||
    typeof description !== "string" ||
    typeof code !== "string"
  ) {
    console.error(
      "Formato de entrada inválido. Todos los campos deben ser cadenas de texto."
    );
    return;
  }
  if (id in codeSnippets) {
    console.error(`Fragmento con ID "${id}" ya existe.`);
    return;
  }
  codeSnippets[id] = {
    language,
    description,
    code,
  };
  console.log(`Fragmento agregado exitosamente: ${id}`);
}

// Función para recuperar un fragmento por ID
function getCodeSnippetById(id) {
  if (id in codeSnippets) {
    const snippet = codeSnippets[id];
    return JSON.stringify(
      {
        id,
        language: snippet.language,
        description: snippet.description,
        code: snippet.code,
      },
      null,
      2
    );
  } else {
    return JSON.stringify({
      message: "Fragmento no encontrado",
    });
  }
}

// Función para enumerar todos los fragmentos en un lenguaje específico
function listCodeSnippetsByLanguage(language) {
  const filteredSnippets = Object.keys(codeSnippets).filter(
    (id) => codeSnippets[id].language === language
  );
  return JSON.stringify(
    filteredSnippets.map((id) => ({
      id,
      language: codeSnippets[id].language,
      description: codeSnippets[id].description,
      code: codeSnippets[id].code,
    })),
    null,
    2
  );
}

// Ejemplo de uso
addCodeSnippet(
  "1",
  "JavaScript",
  "Función para sumar dos números",
  "function add(a, b) { return a + b; }"
);
addCodeSnippet(
  "2",
  "Python",
  "Función para sumar dos números",
  "def add(a, b): return a + b"
);
addCodeSnippet(
  "3",
  "Java",
  "Función para sumar dos números",
  "public int add(int a, int b) { return a + b; }"
);

console.log(getCodeSnippetById("2")); // Salida esperada: { "id": "2", "language": "Python", "description": "Función para sumar dos números", "code": "def add(a, b): return a + b" }
console.log(getCodeSnippetById("4")); // Salida esperada: { "message": "Fragmento no encontrado" }
console.log(listCodeSnippetsByLanguage("Javascript")); // Salida esperada: [ { "id": "1", "language": "JavaScript", "description": "Función para sumar dos números", "code": "function add(a, b) { return a + b; }" } ]
