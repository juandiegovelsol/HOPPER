let codeSnippets = {};

function addSnippet(id, language, description, code) {
  if (
    typeof id !== "string" ||
    typeof language !== "string" ||
    typeof description !== "string" ||
    typeof code !== "string"
  ) {
    return { message: "Formato de entrada inválido" };
  }
  if (id in codeSnippets) {
    return { message: "El ID ya existe" };
  }
  codeSnippets[id] = { language, description, code };
  return { message: "Fragmento agregado correctamente" };
}

function getSnippet(id) {
  if (!id in codeSnippets) {
    return { message: "Fragmento no encontrado" };
  }
  return { ...codeSnippets[id] };
}

function getSnippetsByLanguage(language) {
  return Object.values(codeSnippets).filter(
    (snippet) => snippet.language === language
  );
}

console.log(
  addSnippet(
    "1",
    "JavaScript",
    "Función para sumar dos números",
    "function add(a, b) { return a + b; }"
  )
); // { message: 'Fragmento agregado correctamente' }
console.log(
  addSnippet(
    "2",
    "Python",
    "Función para sumar dos números",
    "def add(a, b): return a + b"
  )
); // { message: 'Fragmento agregado correctamente' }
console.log(
  addSnippet(
    "3",
    "Java",
    "Función para sumar dos números",
    "public int add(int a, int b) { return a + b; }"
  )
); // { message: 'Fragmento agregado correctamente' }
console.log(getSnippet("2")); // { "id": "2", "language": "Python", "description": "Función para sumar dos números", "code": "def add(a, b): return a + b" }
console.log(getSnippet("4")); // { message: 'Fragmento no encontrado' }
console.log(getSnippetsByLanguage("JavaScript")); // [{ "id": "1", "language": "JavaScript", "description": "Función para sumar dos números", "code": "function add(a, b) { return a + b; }" }]
console.log(getSnippetsByLanguage("Python")); // [{ "id": "2", "language": "Python", "description": "Función para sumar dos números", "code": "def add(a, b): return a + b" }]
console.log(getSnippetsByLanguage("Ruby")); // []
