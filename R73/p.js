class NeuralNetwork {
  constructor() {
    this.weights = [Math.random() - 0.5, Math.random() - 0.5];
    this.bias = Math.random() - 0.5;
    this.learningRate = 0.1;
  }

  sigmoid(x) {
    return 1 / (1 + Math.exp(-x));
  }

  predict(inputs) {
    if (inputs.length !== 2) {
      throw new Error("Debe proporcionar exactamente 2 entradas");
    }

    const sum =
      inputs[0] * this.weights[0] + inputs[1] * this.weights[1] + this.bias;

    return this.sigmoid(sum);
  }

  train(trainingData, epochs) {
    for (let epoch = 0; epoch < epochs; epoch++) {
      let totalError = 0;

      for (const example of trainingData) {
        const inputs = example.inputs;
        const target = example.output;

        const prediction = this.predict(inputs);

        const error = target - prediction;
        totalError += Math.abs(error);

        for (let i = 0; i < this.weights.length; i++) {
          this.weights[i] += this.learningRate * error * inputs[i];
        }
        this.bias += this.learningRate * error;
      }

      if ((epoch + 1) % 100 === 0) {
        console.log(
          `Etapa ${epoch + 1}, Error Promedio: ${
            totalError / trainingData.length
          }`
        );
      }
    }
  }
}

const nn = new NeuralNetwork();

const trainingData = [
  { inputs: [0, 0], output: 1 },
  { inputs: [0, 1], output: 1 },
  { inputs: [1, 0], output: 1 },
  { inputs: [1, 1], output: 0 },
];

console.log("Entrenando...");
nn.train(trainingData, 1000);

console.log("\nPrediciendo:");
trainingData.forEach((example) => {
  const prediction = nn.predict(example.inputs);
  console.log(
    `Entradas: ${example.inputs}, Resultado: ${prediction.toFixed(
      4
    )}, Esperado: ${example.output}`
  );
});
