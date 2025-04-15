class DynamicObject {
  constructor(initialProperties) {
    // Propiedades iniciales del objeto
    this.properties = initialProperties;
    // Objeto para guardar métodos dinámicos
    this.methods = {};
  }

  // Método para agregar un método dinámico
  addMethod(methodName, callback) {
    if (typeof methodName !== "string") {
      throw new Error("El nombre del método debe ser un string");
    }
    if (typeof callback !== "function") {
      throw new Error("El callback debe ser una función");
    }
    // Guarda la función de callback con el nombre dado en el objeto methods
    this.methods[methodName] = callback;
  }

  // Método para remover un método dinámico
  removeMethod(methodName) {
    if (typeof methodName !== "string") {
      throw new Error("El nombre del método debe ser un string");
    }
    // Elimina el método con el nombre dado del objeto methods, si existe
    delete this.methods[methodName];
  }

  // Método para llamar a un método dinámico
  callMethod(methodName, ...args) {
    if (typeof methodName !== "string") {
      throw new Error("El nombre del método debe ser un string");
    }
    if (!this.methods.hasOwnProperty(methodName)) {
      throw new Error(`El método "${methodName}" no está definido`);
    }
    // Llama al método con el nombre dado, pasando los argumentos necesarios
    return this.methods[methodName].apply(this, args);
  }
}

// Crear una instancia de DynamicObject con una propiedad inicial
const dynamicObj = new DynamicObject({ prop1: "valor inicial" });

// Agregar métodos dinámicos
dynamicObj.addMethod("greet", function (name) {
  console.log(`Hola, ${name}! Propiedades: ${JSON.stringify(this.properties)}`);
});

dynamicObj.addMethod("addProp", function (propName, value) {
  this.properties[propName] = value;
});

// Llamar a los métodos dinámicos
dynamicObj.callMethod("greet", "Alice");
dynamicObj.callMethod("addProp", "prop2", "valor nuevo");
dynamicObj.callMethod("greet", "Bob");

// Remover un método
dynamicObj.removeMethod("greet");

// Intentar llamar un método eliminado
try {
  dynamicObj.callMethod("greet", "Charlie");
} catch (error) {
  console.error(error.message);
}
