class DynamicObject {
  constructor(initialProperties) {
    // Definir las propiedades iniciales del objeto
    Object.assign(this, initialProperties);

    // Guardar métodos personalizados en un objeto separado
    this.methods = {};
  }

  // Método para añadir un método personalizado
  addMethod(methodName, callback) {
    if (typeof callback === "function") {
      this.methods[methodName] = callback;
    } else {
      console.error(`El callback para ${methodName} no es una función válida.`);
    }
  }

  // Método para remover un método personalizado
  removeMethod(methodName) {
    if (this.methods[methodName]) {
      delete this.methods[methodName];
    } else {
      console.error(`El método ${methodName} no existe en el objeto.`);
    }
  }

  // Método para llamar a un método personalizado
  callMethod(methodName, ...args) {
    const method = this.methods[methodName];
    if (method) {
      // Llamar el método con los argumentos proporcionados
      return method.apply(this, args);
    } else {
      console.error(`El método ${methodName} no existe en el objeto.`);
      return null;
    }
  }
}

// Crear un objeto DynamicObject inicial
const initialProperties = {
  name: "Juan",
  age: 30,
};

const obj = new DynamicObject(initialProperties);

// Añadir métodos personalizados
obj.addMethod("greet", function () {
  console.log(`Hola, mi nombre es ${this.name}.`);
});

obj.addMethod("farewell", function () {
  console.log(`Hasta luego, ${this.name}. Tienes ${this.age} años.`);
});

// Llamar los métodos personalizados
obj.callMethod("greet"); // Output: Hola, mi nombre es Juan.
obj.callMethod("farewell"); // Output: Hasta luego, Juan. Tienes 30 años.

// Remover un método y tratar de llamarlo de nuevo
obj.removeMethod("greet");
obj.callMethod("greet"); // Output: Error - El método greet no existe en el objeto.
