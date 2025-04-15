const gameBoard = document.getElementById("gameBoard");
const boardGrid = Array.from({ length: 30 }, () => Array(10).fill(null));
let currentBlock = null;
let currentBlockX = 0;
let currentBlockY = 0;

function createBlock() {
  currentBlock = document.createElement("div");
  currentBlock.classList.add("block");
  gameBoard.appendChild(currentBlock);
  currentBlockX = 4; // Start from the middle
  currentBlockY = 0;
  drawBlock();
  setTimeout(moveBlockDown, 1000);
}

function drawBlock() {
  currentBlock.style.gridRow = `${currentBlockY} / span 1`;
  currentBlock.style.gridColumn = `${currentBlockX + 1} / span 1`;
}

function moveBlockDown() {
  if (!canMove(currentBlockX, currentBlockY + 1)) {
    currentBlock.classList.remove("block");
    updateBoard(currentBlockX, currentBlockY);
    createBlock();
  } else {
    currentBlockY++;
    drawBlock();
    setTimeout(moveBlockDown, 100);
  }
}

function moveBlock(dir) {
  if (canMove(currentBlockX + dir, currentBlockY)) {
    currentBlockX += dir;
    drawBlock();
  }
}

function canMove(x, y) {
  if (y >= 30 || x < 0 || x >= 10) return false;
  return boardGrid[y]?.[x] === null;
}

function updateBoard(x, y) {
  if (boardGrid[y][x] === null) {
    boardGrid[y][x] = true;
  }
}

document.addEventListener("keydown", (e) => {
  switch (e.key) {
    case "ArrowRight":
      moveBlock(1);
      break;
    case "ArrowLeft":
      moveBlock(-1);
      break;
  }
});

createBlock();
