const player = document.getElementById("player");
const objective = document.getElementById("objective");
const enemy = document.getElementById("enemy");
const restartButton = document.getElementById("restart-button");

let playerPos = { x: 0, y: 0 };
let objectivePos = { x: 0, y: 0 };
let enemyPos = { x: 0, y: 0 };
let gameActive = true;
let sequenceIndex = 0;
const sequences = [
  // Primera secuencia de 5 pares objetivo-enemigo
  [
    { x: 1, y: 1 },
    { x: 3, y: 1 },
  ],
  [
    { x: 2, y: 2 },
    { x: 2, y: 4 },
  ],
  [
    { x: 0, y: 3 },
    { x: 4, y: 3 },
  ],
  [
    { x: 1, y: 5 },
    { x: 3, y: 5 },
  ],
  [
    { x: 2, y: 6 },
    { x: 2, y: 7 },
  ],
];

// Función para actualizar la posición del jugador
function updatePlayerPosition(event) {
  if (!gameActive) return;

  const key = event.key;
  let newX = playerPos.x;
  let newY = playerPos.y;

  if (key === "ArrowUp") newY = playerPos.y - 1;
  if (key === "ArrowDown") newY = playerPos.y + 1;
  if (key === "ArrowLeft") newX = playerPos.x - 1;
  if (key === "ArrowRight") newX = playerPos.x + 1;

  // Evita que el jugador se mueva fuera de los límites de la cuadrícula
  if (newX >= 0 && newX < 10 && newY >= 0 && newY < 10) {
    playerPos.x = newX;
    playerPos.y = newY;
  }

  checkCollisions();
}

// Función para colocar objetivos y enemigos en sus posiciones
function placeObjectivesAndEnemies() {
  const sequence = sequences[sequenceIndex];
  objectivePos = sequence[0];
  enemyPos = sequence[1];
}

// Inicialización del juego
function restartGame() {
  playerPos = { x: 0, y: 0 };
  sequenceIndex = 0;
  placeObjectivesAndEnemies();
  gameActive = true;
  player.style.gridRow = `${playerPos.y + 1}`;
  player.style.gridColumn = `${playerPos.x + 1}`;
  objective.style.gridRow = `${objectivePos.y + 1}`;
  objective.style.gridColumn = `${objectivePos.x + 1}`;
  enemy.style.gridRow = `${enemyPos.y + 1}`;
  enemy.style.gridColumn = `${enemyPos.x + 1}`;
  restartButton.style.display = "none";
}

// Verifica si hay colisiones entre el jugador, objetivos o enemigos
function checkCollisions() {
  // Verifica colisión con el objetivo
  if (playerPos.x === objectivePos.x && playerPos.y === objectivePos.y) {
    scorePoint();
  }

  // Verifica colisión con el enemigo
  if (playerPos.x === enemyPos.x && playerPos.y === enemyPos.y) {
    gameOver();
  }
}

// Función para anotar un punto cuando el jugador alcanza un objetivo
function scorePoint() {
  sequenceIndex = (sequenceIndex + 1) % sequences.length;
  placeObjectivesAndEnemies();
  objective.style.gridRow = `${objectivePos.y + 1}`;
  objective.style.gridColumn = `${objectivePos.x + 1}`;
  enemy.style.gridRow = `${enemyPos.y + 1}`;
  enemy.style.gridColumn = `${enemyPos.x + 1}`;
}

// Función que se ejecuta cuando el jugador choca con un enemigo
function gameOver() {
  gameActive = false;
  restartButton.style.display = "block";
}

// Eventos para manejar el movimiento del jugador con las flechas del teclado
window.addEventListener("keydown", updatePlayerPosition);

// Inicializa el juego al cargar la página
window.onload = restartGame;
