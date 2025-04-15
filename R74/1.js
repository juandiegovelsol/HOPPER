class Neurona {
  constructor(peso1, peso2, bias) {
    this.peso1 = peso1 || Math.random() * 2 - 1;
    this.peso2 = peso2 || Math.random() * 2 - 1;
    this.bias = bias || Math.random() * 2 - 1;
  }

  activacion(suma) {
    // Usamos la función sigmoide como función de activación
    return 1 / (1 + Math.exp(-suma));
  }

  predecir(entrada1, entrada2) {
    const suma = this.peso1 * entrada1 + this.peso2 * entrada2 + this.bias;
    return this.activacion(suma);
  }
}

class RedNeuronal {
  constructor() {
    // Inicializamos las neuronas con pesos aleatorios
    this.neuronaOculta1 = new Neurona();
    this.neuronaOculta2 = new Neurona();
    this.neuronaSalida = new Neurona();
  }

  entrenar(entradas, salidasEsperadas, iteraciones, tasaAprendizaje) {
    for (let i = 0; i < iteraciones; i++) {
      for (let j = 0; j < entradas.length; j++) {
        const [e1, e2] = entradas[j];
        const salidaEsperada = salidasEsperadas[j];

        // Propagación hacia adelante
        const salidaOculta1 = this.neuronaOculta1.predecir(e1, e2);
        const salidaOculta2 = this.neuronaOculta2.predecir(e1, e2);
        const salidaFinal = this.neuronaSalida.predecir(
          salidaOculta1,
          salidaOculta2
        );

        // Cálculo del error
        const error = salidaEsperada - salidaFinal;

        // Retropropagación
        const deltaSalida = error * salidaFinal * (1 - salidaFinal);
        const deltaOculta1 =
          deltaSalida *
          this.neuronaSalida.peso1 *
          salidaOculta1 *
          (1 - salidaOculta1);
        const deltaOculta2 =
          deltaSalida *
          this.neuronaSalida.peso2 *
          salidaOculta2 *
          (1 - salidaOculta2);

        // Actualización de pesos
        this.neuronaSalida.peso1 +=
          tasaAprendizaje * deltaSalida * salidaOculta1;
        this.neuronaSalida.peso2 +=
          tasaAprendizaje * deltaSalida * salidaOculta2;
        this.neuronaSalida.bias += tasaAprendizaje * deltaSalida;

        this.neuronaOculta1.peso1 += tasaAprendizaje * deltaOculta1 * e1;
        this.neuronaOculta1.peso2 += tasaAprendizaje * deltaOculta1 * e2;
        this.neuronaOculta1.bias += tasaAprendizaje * deltaOculta1;

        this.neuronaOculta2.peso1 += tasaAprendizaje * deltaOculta2 * e1;
        this.neuronaOculta2.peso2 += tasaAprendizaje * deltaOculta2 * e2;
        this.neuronaOculta2.bias += tasaAprendizaje * deltaOculta2;
      }
    }
  }

  predecir(entrada1, entrada2) {
    const salidaOculta1 = this.neuronaOculta1.predecir(entrada1, entrada2);
    const salidaOculta2 = this.neuronaOculta2.predecir(entrada1, entrada2);
    const salidaFinal = this.neuronaSalida.predecir(
      salidaOculta1,
      salidaOculta2
    );
    return salidaFinal >= 0.5 ? 1 : 0;
  }
}

// Ejemplo de uso
const entradas = [
  [0, 0],
  [0, 1],
  [1, 0],
  [1, 1],
];
const salidasEsperadas = [0, 1, 1, 0];
const redNeuronal = new RedNeuronal();

// Entrenar la red neuronal
redNeuronal.entrenar(entradas, salidasEsperadas, 10000, 0.1);

// Probar la red neuronal
console.log("Predicciones:");
entradas.forEach((entrada) => {
  const [e1, e2] = entrada;
  console.log(
    `Entrada: ${e1}, ${e2} -- Predicción: ${redNeuronal.predecir(e1, e2)}`
  );
});
