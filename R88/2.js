const ROWS = 10; // Número de filas en la cuadrícula
const COLS = 20; // Número de columnas en la cuadrícula
const DIRECTIONS = {
  LEFT: { dx: 0, dy: -1, symbol: "<" },
  RIGHT: { dx: 0, dy: 1, symbol: ">" },
  UP: { dx: -1, dy: 0, symbol: "^" },
  DOWN: { dx: 1, dy: 0, symbol: "v" },
};

let snake = [{ x: 5, y: 5 }]; // Posiciones iniciales de la serpiente
let currentDirection = DIRECTIONS.RIGHT;
let food = { x: 0, y: 0 };
let score = 0;

// Generar posición inicial de la comida
function placeFood() {
  food.x = Math.floor(Math.random() * ROWS);
  food.y = Math.floor(Math.random() * COLS);
}

// Dibuja el tablero
function drawBoard() {
  console.clear();
  for (let i = 0; i <= ROWS + 1; i++) {
    let row = "";
    for (let j = 0; j <= COLS + 1; j++) {
      if (i === 0 || i === ROWS + 1 || j === 0 || j === COLS + 1) {
        row += "=";
      } else if (i === snake[0].x && j === snake[0].y) {
        row += currentDirection.symbol;
      } else if (snake.some((part) => part.x === i && part.y === j)) {
        row += "#";
      } else if (i === food.x && j === food.y) {
        row += "$";
      } else {
        row += " ";
      }
    }
    console.log(row);
  }
  console.log(`Puntuación: ${score}`);
}

// Actualiza la posición de la serpiente
function moveSnake() {
  const head = { ...snake[0] };
  head.x += currentDirection.dx;
  head.y += currentDirection.dy;

  if (
    head.x === 0 ||
    head.y === 0 ||
    head.x === ROWS + 1 ||
    head.y === COLS + 1 ||
    snake.some((part) => part.x === head.x && part.y === head.y)
  ) {
    console.log("¡Juego terminado!");
    process.exit();
  }

  if (head.x === food.x && head.y === food.y) {
    score++;
    placeFood();
  } else {
    snake.pop();
  }
  snake.unshift(head);
}

// Cambia la dirección de la serpiente
function changeDirection(newDirection) {
  const opposite = {
    LEFT: "RIGHT",
    RIGHT: "LEFT",
    UP: "DOWN",
    DOWN: "UP",
  };
  if (newDirection !== opposite[currentDirection]) {
    currentDirection = DIRECTIONS[newDirection];
  }
}

// Escucha eventos de teclado
function handleInput() {
  const readline = require("readline");
  readline.emitKeypressEvents(process.stdin);
  process.stdin.setRawMode(true);

  process.stdin.on("keypress", (chunk, key) => {
    if (key && key.name === "q") {
      process.exit();
    }

    if (key && key.name) {
      switch (key.name) {
        case "w":
          changeDirection("UP");
          break;
        case "s":
          changeDirection("DOWN");
          break;
        case "a":
          changeDirection("LEFT");
          break;
        case "d":
          changeDirection("RIGHT");
          break;
      }
    }
  });
}

// Inicia el juego
function gameLoop() {
  setInterval(() => {
    moveSnake();
    drawBoard();
  }, 500);
}

function startGame() {
  placeFood();
  handleInput();
  gameLoop();
}

startGame();
