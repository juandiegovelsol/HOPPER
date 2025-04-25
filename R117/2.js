// Helper functions
function matrixTranspose(matrix) {
  const rows = matrix.length;
  const cols = matrix[0].length;
  const transposed = Array.from({ length: cols }, () => Array(rows).fill(0));

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      transposed[j][i] = matrix[i][j];
    }
  }
  return transposed;
}

function matrixMultiply(A, B) {
  const rowsA = A.length;
  const colsA = A[0].length;
  const colsB = B[0].length;
  const result = Array.from({ length: rowsA }, () => Array(colsB).fill(0));

  for (let i = 0; i < rowsA; i++) {
    for (let j = 0; j < colsB; j++) {
      for (let k = 0; k < colsA; k++) {
        result[i][j] += A[i][k] * B[k][j];
      }
    }
  }
  return result;
}

function invertMatrix(matrix) {
  // Algoritmo de inversión de matriz simple para 2x2
  const det = determinant(matrix);
  if (det === 0) throw new Error("La matriz no es invertible");
  const inv = [
    [matrix[1][1] / det, -matrix[0][1] / det],
    [-matrix[1][0] / det, matrix[0][0] / det],
  ];
  return inv;
}

function determinant(matrix) {
  return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
}

// Clase principal para la regresión lineal
class RegressionModel {
  constructor(X, Y) {
    this.X = X;
    this.Y = Y;
    this.coefficients = null;
    this.fit();
  }

  fit() {
    const Xt = matrixTranspose(this.X);
    const XtX = matrixMultiply(Xt, this.X);
    const XtX_inv = invertMatrix(XtX);
    const XtY = matrixMultiply(Xt, this.Y);
    this.coefficients = matrixMultiply(XtX_inv, XtY);
  }

  predict(newX) {
    const bias = [1];
    const inputVector = matrixMultiply(
      matrixTranspose([bias.concat(newX)]),
      this.coefficients
    );
    return inputVector[0][0]; // Retornamos el valor escalar predicho
  }
}

// Datos
const x = [
  [1, 2],
  [2, 1],
  [4, 3],
  [3, 5],
  [5, 4],
];

const y = [[5], [6], [10], [13], [14]];

// Preprocesamiento de datos
function addBiasTerm(data) {
  return data.map((fila) => [1].concat(fila));
}

const x_con_bias = addBiasTerm(x);

// Uso del modelo
const model = new RegressionModel(x_con_bias, y);
console.log("Coeficientes:");
console.log(model.coefficients);

const nuevaEntrada = [3, 2];
const prediccion = model.predict(nuevaEntrada);
console.log("Predicción:", prediccion);
