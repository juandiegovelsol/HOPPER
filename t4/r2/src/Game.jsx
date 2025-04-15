import { useState, useEffect } from "react";
import "./Game.css";

const GAME_WIDTH = 600;
const GAME_HEIGHT = 600;
const ENEMY_SIZE = 20;
const PLAYER_SIZE = 30;
const ENEMY_SPEED = 2;
const BULLET_SPEED = 5;
const BULLET_MAX_INTERVAL = 333; // 3 disparos por segundo

function Game() {
  const [playerPosition, setPlayerPosition] = useState({
    x: GAME_WIDTH / 2,
    y: GAME_HEIGHT - 40,
  });
  const [enemies, setEnemies] = useState([]);
  const [bullets, setBullets] = useState([]);
  const [score, setScore] = useState(0);
  const [gameOver, setGameOver] = useState(false);
  const [lastBulletTime, setLastBulletTime] = useState(0);

  const enemyPositions = [
    { x: 100, y: -ENEMY_SIZE },
    { x: 200, y: -ENEMY_SIZE },
    { x: 300, y: -ENEMY_SIZE },
    { x: 400, y: -ENEMY_SIZE },
    { x: 500, y: -ENEMY_SIZE },
    { x: 100, y: -ENEMY_SIZE + 100 },
    { x: 200, y: -ENEMY_SIZE + 100 },
    { x: 300, y: -ENEMY_SIZE + 100 },
    { x: 400, y: -ENEMY_SIZE + 100 },
    { x: 500, y: -ENEMY_SIZE + 100 },
  ];

  useEffect(() => {
    if (enemies.length === 0) {
      setEnemies(enemyPositions.map((pos) => ({ ...pos, alive: true })));
    }
  }, [enemies.length]);

  useEffect(() => {
    if (gameOver) {
      alert(`Game Over! Enemies eliminated: ${score}`);
    }
  }, [gameOver]);

  const handleMouseMove = (event) => {
    setPlayerPosition({ x: event.clientX, y: playerPosition.y });
  };

  const handleKeyDown = (event) => {
    if (event.code === "Space" && !gameOver) {
      const now = Date.now();
      if (now - lastBulletTime > BULLET_MAX_INTERVAL) {
        setBullets([
          ...bullets,
          { x: playerPosition.x, y: playerPosition.y - PLAYER_SIZE / 2 },
        ]);
        setLastBulletTime(now);
      }
    }
  };

  useEffect(() => {
    if (bullets.length > 0) {
      setBullets(
        bullets
          .map((bullet) => {
            if (bullet.y < 0) {
              return null;
            }
            return { x: bullet.x, y: bullet.y - BULLET_SPEED };
          })
          .filter((bullet) => bullet !== null)
      );
    }
  }, [bullets]);

  useEffect(() => {
    const enemyToRemove = enemies.filter((enemy) => !enemy.alive);
    setEnemies(enemies.filter((enemy) => enemy.alive));
    if (enemyToRemove.length > 0) {
      setScore((prevScore) => prevScore + enemyToRemove.length);
    }
  }, [enemies]);

  useEffect(() => {
    const interval = setInterval(() => {
      setEnemies(
        enemies.map((enemy) => {
          if (enemy.y > GAME_HEIGHT / 2) {
            return { ...enemy, alive: false };
          }
          return { ...enemy, y: enemy.y + ENEMY_SPEED };
        })
      );
    }, 50);

    return () => clearInterval(interval);
  }, [enemies]);

  useEffect(() => {
    setGameOver(
      enemies.some(
        (enemy) =>
          enemy.x === playerPosition.x &&
          enemy.y > GAME_HEIGHT - ENEMY_SIZE - PLAYER_SIZE
      )
    );
  }, [enemies, playerPosition]);

  return (
    <div
      className="game-container"
      onMouseMove={handleMouseMove}
      onKeyDown={handleKeyDown}
    >
      <div
        className="player"
        style={{
          left: `${playerPosition.x - PLAYER_SIZE / 2}px`,
          top: `${playerPosition.y - PLAYER_SIZE / 2}px`,
        }}
      ></div>
      {bullets.map((bullet, index) => (
        <div
          key={index}
          className="bullet"
          style={{ left: `${bullet.x - 2}px`, top: `${bullet.y - 2}px` }}
        ></div>
      ))}
      {enemies.map((enemy, index) => (
        <div
          key={index}
          className="enemy"
          style={{
            left: `${enemy.x - ENEMY_SIZE / 2}px`,
            top: `${enemy.y - ENEMY_SIZE / 2}px`,
          }}
        ></div>
      ))}
    </div>
  );
}

export default Game;
