class MatrixOperations {
  static transpose(matrix) {
    return matrix[0].map((_, colIndex) => matrix.map((row) => row[colIndex]));
  }

  static multiply(A, B) {
    return A.map((row) =>
      B[0].map((_, colIndex) =>
        row.reduce(
          (sum, element, rowIndex) => sum + element * B[rowIndex][colIndex],
          0
        )
      )
    );
  }

  static inverse(matrix) {
    // Suponiendo que este método operará solo para matrices de 2x2 o matrices 3x3 para el ejemplo.
    if (matrix.length !== matrix[0].length) {
      throw new Error("Solo matrices cuadradas pueden tener una inversa");
    }
    // Implementación básica para matrices 2x2 (ad-bc formula).
    if (matrix.length === 2) {
      const [[a, b], [c, d]] = matrix;
      const determinant = a * d - b * c;
      if (determinant === 0)
        throw new Error("La matriz es singular y no tiene inversa.");
      return [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant],
      ];
    }
    // Aquí podría añadirse una implementación más compleja para matrices superiores.
  }

  static dot(vectorA, vectorB) {
    return vectorA.reduce((sum, a, index) => sum + a * vectorB[index], 0);
  }
}

class LinearRegression {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.coef = this.computeCoefficients();
  }

  addBiasTerm(matrix) {
    let ones = Array(matrix.length)
      .fill()
      .map(() => [1]);
    return matrix.map((row, i) => ones[i].concat(row));
  }

  computeCoefficients() {
    let xWithBias = this.addBiasTerm(this.x);
    let Xt = MatrixOperations.transpose(xWithBias);
    let XtX = MatrixOperations.multiply(Xt, xWithBias);
    let XtX_inv = MatrixOperations.inverse(XtX);
    let XtY = MatrixOperations.multiply(
      Xt,
      this.y.map((yValue) => [yValue])
    );
    return MatrixOperations.multiply(XtX_inv, XtY).map((row) => row[0]);
  }

  predict(input) {
    let withBias = [1].concat(input);
    return MatrixOperations.dot(withBias, this.coef);
  }

  getCoefficients() {
    return this.coef;
  }
}

const x = [
  [1, 2],
  [2, 1],
  [4, 3],
  [3, 5],
  [5, 4],
];

const y = [5, 6, 10, 13, 14];

const regression = new LinearRegression(x, y);
console.log("Coeficientes:");
console.log(regression.getCoefficients());

const nuevaEntrada = [3, 2];
console.log("Predicción: ", regression.predict(nuevaEntrada));
