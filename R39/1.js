class CalculadoraDePromedio {
  constructor() {
    // Inicialización de los exámenes como un arreglo de objetos
    this.examenes = [
      { nombre: "Examen 1", calificacion: 0 },
      { nombre: "Examen 2", calificacion: 0 },
      { nombre: "Examen 3", calificacion: 0 },
      { nombre: "Examen 4", calificacion: 0 },
      { nombre: "Examen 5", calificacion: 0 },
    ];
  }

  agregarCalificaciones() {
    const readline = require("readline-sync");

    this.examenes.forEach((examen) => {
      let calificacion;
      while (true) {
        // Solicitar al usuario ingresar la calificación
        calificacion = parseFloat(
          readline.question(`Ingresa la calificación para ${examen.nombre}: `)
        );
        if (!isNaN(calificacion) && calificacion >= 0 && calificacion <= 10) {
          examen.calificacion = calificacion;
          break;
        } else {
          console.log("Por favor ingresa un número válido entre 0 y 10.");
        }
      }
    });
  }

  calcularPromedio() {
    let suma = 0;

    console.log("\nCalificaciones de los exámenes:");
    this.examenes.forEach((examen) => {
      console.log(`${examen.nombre}: ${examen.calificacion}`);
      suma += examen.calificacion;
    });

    console.log("\n");

    const promedio = suma / this.examenes.length;
    console.log(`Promedio de calificaciones: ${promedio.toFixed(2)}`);
  }
}

// Ejemplo de uso
const calculadora = new CalculadoraDePromedio();
calculadora.agregarCalificaciones();
calculadora.calcularPromedio();
