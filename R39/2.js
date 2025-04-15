class CalculadoraDePromedio {
  constructor() {
    // Inicializamos un arreglo para almacenar las calificaciones de 5 exámenes
    // Cada examen es un objeto con 'nombre' y 'calificacion'
    this.examenes = new Array(5).fill({ nombre: "", calificacion: 0 });
  }

  // Método para agregar calificaciones
  agregarCalificaciones() {
    const readline = require("readline");

    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    const preguntas = [
      "Ingrese el nombre y la calificación del examen 1: ",
      "Ingrese el nombre y la calificación del examen 2: ",
      "Ingrese el nombre y la calificación del examen 3: ",
      "Ingrese el nombre y la calificación del examen 4: ",
      "Ingrese el nombre y la calificación del examen 5: ",
    ];

    const realizarPregunta = (indice) => {
      if (indice < preguntas.length) {
        rl.question(preguntas[indice], (respuesta) => {
          const [nombre, calificacion] = respuesta
            .split(",")
            .map((str) => str.trim());
          this.examenes[indice] = {
            nombre,
            calificacion: parseFloat(calificacion),
          };
          realizarPregunta(indice + 1);
        });
      } else {
        rl.close();
      }
    };

    realizarPregunta(0);
  }

  // Método para calcular el promedio de las calificaciones
  calcularPromedio() {
    let suma = 0;
    console.log("Calificaciones de los exámenes:");

    this.examenes.forEach((examen, indice) => {
      console.log(
        `Examen ${indice + 1}: ${examen.nombre} - ${examen.calificacion}`
      );
      suma += parseFloat(examen.calificacion);
    });

    const promedio = suma / this.examenes.length;
    console.log("\nPromedio final:", promedio);
  }
}

// Crear una instancia de la clase y usar los métodos
const calculadora = new CalculadoraDePromedio();

// Llamar a agregarCalificaciones para ingresar las notas
calculadora.agregarCalificaciones();

// Calcular y mostrar el promedio (se puede llamar después de agregar las calificaciones)
calculadora.calcularPromedio();
