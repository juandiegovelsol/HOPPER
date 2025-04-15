function sigmoid(x) {
  return 1 / (1 + Math.exp(-x));
}

function sigmoidDerivative(x) {
  return x * (1 - x);
}

class NeuralNetwork {
  constructor() {
    // Inicialización de pesos aleatorios para una red simple
    this.inputLayerSize = 2;
    this.hiddenLayerSize = 2;
    this.outputLayerSize = 1;

    // Pesos entre la capa de entrada y la capa oculta
    this.weightsInputHidden = [
      [Math.random(), Math.random()],
      [Math.random(), Math.random()],
    ];

    // Pesos entre la capa oculta y la capa de salida
    this.weightsHiddenOutput = [Math.random(), Math.random()];
  }

  train(inputs, expectedOutput, iterations) {
    for (let i = 0; i < iterations; i++) {
      const predictions = inputs.map((input) => this.feedforward(input));
      this.backpropagate(inputs, predictions, expectedOutput);
    }
  }

  feedforward(input) {
    // Calcular la salida de la capa oculta
    const hiddenLayerOutputs = this.weightsInputHidden.map((weights, i) =>
      sigmoid(weights[0] * input[0] + weights[1] * input[1])
    );

    // Calcular la salida final de la red
    const output = sigmoid(
      hiddenLayerOutputs[0] * this.weightsHiddenOutput[0] +
        hiddenLayerOutputs[1] * this.weightsHiddenOutput[1]
    );

    return {
      hiddenLayerOutputs,
      output,
    };
  }

  backpropagate(inputs, predictions, expectedOutputs) {
    for (let i = 0; i < inputs.length; i++) {
      const { hiddenLayerOutputs, output } = predictions[i];
      const input = inputs[i];
      const expectedOutput = expectedOutputs[i];

      // Error en la salida
      const outputError = expectedOutput - output;

      // Error de la capa oculta
      const hiddenErrors = this.weightsHiddenOutput.map(
        (weight, i) =>
          outputError * weight * sigmoidDerivative(hiddenLayerOutputs[i])
      );

      // Actualizar pesos entre la capa oculta y de salida
      this.weightsHiddenOutput = this.weightsHiddenOutput.map(
        (weight, j) =>
          weight +
          hiddenLayerOutputs[j] * outputError * sigmoidDerivative(output)
      );

      // Actualizar pesos entre la capa de entrada y la capa oculta
      for (let j = 0; j < this.hiddenLayerSize; j++) {
        this.weightsInputHidden[j] = this.weightsInputHidden[j].map(
          (weight, k) => weight + input[k] * hiddenErrors[j]
        );
      }
    }
  }

  predict(input) {
    const { output } = this.feedforward(input);
    return output > 0.5 ? 1 : 0;
  }
}

// Ejemplo de uso:
const nn = new NeuralNetwork();
const trainingInputs = [
  [0, 0],
  [0, 1],
  [1, 0],
  [1, 1],
];
const trainingOutputs = [0, 1, 1, 0];

nn.train(trainingInputs, trainingOutputs, 10000);

console.log(nn.predict([0, 0])); // Debería estar cerca de 0
console.log(nn.predict([0, 1])); // Debería estar cerca de 1
console.log(nn.predict([1, 0])); // Debería estar cerca de 1
console.log(nn.predict([1, 1])); // Debería estar cerca de 0
