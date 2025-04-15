let block = document.getElementById("block");
let gameoverText = document.getElementById("gameover");
let gameContainer = document.getElementById("game");
let groundHeight = gameContainer.offsetHeight - 10;
let blockPosition = 0;
let currentBlockBottom = groundHeight;
let falling = true;
let blocks = [];
let lastBlockLeft = null;

function dropBlock() {
  if (falling) {
    blockPosition += 5;
    block.style.top = blockPosition + "px";
    if (blockPosition + 50 >= currentBlockBottom) {
      let currentLeft = block.offsetLeft;

      if (blocks.length > 0) {
        if (Math.abs(currentLeft - lastBlockLeft) >= 50) {
          endGame();
          return;
        }
      }

      lastBlockLeft = currentLeft;
      blocks.push(block);

      currentBlockBottom = blockPosition;
      falling = false;
      setTimeout(() => {
        createNewBlock();
      }, 1000);
    } else {
      requestAnimationFrame(dropBlock);
    }
  }
}

function createNewBlock() {
  block = document.createElement("div");
  block.className = "block";
  block.style.width = "50px";
  block.style.height = "50px";
  block.style.backgroundColor = "#e94e77";
  block.style.position = "absolute";
  block.style.left = Math.random() * (gameContainer.offsetWidth - 50) + "px";
  block.style.top = "0px";
  gameContainer.appendChild(block);
  blockPosition = 0;
  falling = true;
  dropBlock();
}

function endGame() {
  gameoverText.style.display = "block";
  falling = false;
}

window.addEventListener("keydown", (e) => {
  if (falling) {
    if (e.key === "ArrowLeft") {
      block.style.left = Math.max(0, block.offsetLeft - 10) + "px";
    } else if (e.key === "ArrowRight") {
      block.style.left =
        Math.min(gameContainer.offsetWidth - 50, block.offsetLeft + 10) + "px";
    }
  }
});

createNewBlock();
