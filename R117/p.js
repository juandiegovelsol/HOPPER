const math = require("mathjs");

let x = [
  [1, 2],
  [2, 1],
  [4, 3],
  [3, 5],
  [5, 4],
];

let y = [5, 6, 10, 13, 14];

let unos = Array(x.length)
  .fill()
  .map(() => [1]);
let x_con_bias = x.map((fila, i) => unos[i].concat(fila));

let X = math.matrix(x_con_bias);
let Y = math.transpose(math.matrix([y]));

let Xt = math.transpose(X);
let XtX = math.multiply(Xt, X);
let XtX_inv = math.inv(XtX);
let XtY = math.multiply(Xt, Y);
let B = math.multiply(XtX_inv, XtY);

console.log("Coeficientes:");
console.log(B.valueOf());

function predecir(valores) {
  let entrada = [1].concat(valores);
  return math.dot(entrada, B);
}

let nueva_entrada = [3, 2];
let prediccion = predecir(nueva_entrada);

console.log("Predicción:", prediccion);
