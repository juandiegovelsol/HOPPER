const readline = require("readline");

// Constantes del juego
const WIDTH = 20;
const HEIGHT = 10;
const INTERVAL = 100;

// Inicialización del juego
let board = Array.from({ length: HEIGHT }, () => Array(WIDTH).fill(" "));
let snake = [[3, 3]]; // Posición inicial de la serpiente
let direction = "RIGHT";
let food = getRandomFoodPosition();
let score = 0;
let gameOver = false;

// Inicializa la interfaz de lectura de teclado
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Función para colocar la comida en un lugar aleatorio
function getRandomFoodPosition() {
  let foodPosition;
  do {
    foodPosition = [
      Math.floor(Math.random() * WIDTH),
      Math.floor(Math.random() * HEIGHT),
    ];
  } while (
    snake.some(
      (segment) =>
        segment[0] === foodPosition[0] && segment[1] === foodPosition[1]
    )
  );
  return foodPosition;
}

// Dibuja el tablero de juego
function drawBoard() {
  console.clear();
  console.log(`Score: ${score}`);
  board.forEach((row, y) => {
    row.forEach((cell, x) => {
      if (x === 0 || x === WIDTH - 1 || y === 0 || y === HEIGHT - 1) {
        console.log("="); // Bordes del juego
      } else {
        // Dibujar la serpiente
        if (snake.some((segment) => segment[0] === x && segment[1] === y)) {
          if (direction === "RIGHT") console.log(">");
          else if (direction === "LEFT") console.log("<");
          else if (direction === "UP") console.log("^");
          else console.log("v");
        } else if ([...food] === [x, y]) {
          console.log("$"); // Dibujar la comida
        } else {
          console.log(".");
        }
      }
    });
  });
}

// Actualiza la posición de la serpiente
function updateSnake() {
  if (gameOver) return;

  const head = snake[0];
  const newHead = [head[0], head[1]];

  switch (direction) {
    case "RIGHT":
      newHead[0]++;
      break;
    case "LEFT":
      newHead[0]--;
      break;
    case "UP":
      newHead[1]--;
      break;
    case "DOWN":
      newHead[1]++;
      break;
  }

  // Colisión con los bordes
  if (
    newHead[0] < 1 ||
    newHead[0] >= WIDTH - 1 ||
    newHead[1] < 1 ||
    newHead[1] >= HEIGHT - 1
  ) {
    gameOver = true;
    console.log("Game Over! La serpiente chocó con un borde.");
    return;
  }

  // Colisión consigo misma
  if (
    snake.some(
      (segment) => segment[0] === newHead[0] && segment[1] === newHead[1]
    )
  ) {
    gameOver = true;
    console.log("Game Over! La serpiente chocó consigo misma.");
    return;
  }

  // Comprobar si la serpiente come la comida
  if (newHead[0] === food[0] && newHead[1] === food[1]) {
    score += 10;
    snake.unshift(newHead);
    food = getRandomFoodPosition();
  } else {
    snake.unshift(newHead);
    snake.pop();
  }

  drawBoard();
}

// Controla la recepción de entrada del teclado
rl.on("line", (input) => {
  switch (input.trim()) {
    case "w":
      direction = "UP";
      break;
    case "s":
      direction = "DOWN";
      break;
    case "a":
      direction = "LEFT";
      break;
    case "d":
      direction = "RIGHT";
      break;
  }
});

// Inicio del juego
drawBoard();
const gameInterval = setInterval(updateSnake, INTERVAL);

// Manejo de final del juego
rl.on("close", () => {
  clearInterval(gameInterval);
  process.exit();
});
