import React, { useState, useEffect, useRef } from "react";
import "./Game.css";

const positions = [
  { top: 0, left: 0 },
  { top: 0, left: 550 },
  { top: 0, left: 300 },
  { top: 550, left: 0 },
  { top: 550, left: 300 },
  { top: 300, left: 0 },
  { top: 300, left: 550 },
  { top: 100, left: 100 },
  { top: 500, left: 500 },
  { top: 100, left: 500 },
];

const Game = () => {
  const [bullets, setBullets] = useState([]);
  const [enemies, setEnemies] = useState([]);
  const [score, setScore] = useState(0);
  const [gameOver, setGameOver] = useState(false);
  const [mousePos, setMousePos] = useState({ x: 300, y: 300 });
  const [isShooting, setIsShooting] = useState(false);
  const [lastShotTime, setLastShotTime] = useState(0);
  const characterRef = useRef(null);
  const spawnInterval = useRef(null);
  const shootingInterval = useRef(null);
  const enemySpeed = 1;
  const bulletSpeed = 5;

  useEffect(() => {
    spawnInterval.current = setInterval(spawnEnemy, 1000);
    return () => clearInterval(spawnInterval.current);
  }, []);

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.code === "Space" && !gameOver && !isShooting) {
        setIsShooting(true);
        shoot();
        shootingInterval.current = setInterval(() => {
          shoot();
        }, 333);
      }
    };

    const handleKeyUp = (e) => {
      if (e.code === "Space") {
        setIsShooting(false);
        if (shootingInterval.current) {
          clearInterval(shootingInterval.current);
          shootingInterval.current = null;
        }
      }
    };

    document.addEventListener("keydown", handleKeyDown);
    document.addEventListener("keyup", handleKeyUp);

    return () => {
      document.removeEventListener("keydown", handleKeyDown);
      document.removeEventListener("keyup", handleKeyUp);
      if (shootingInterval.current) {
        clearInterval(shootingInterval.current);
      }
    };
  }, [gameOver, isShooting]);

  useEffect(() => {
    const handleMouseMove = (e) => {
      const rect = document.querySelector(".game").getBoundingClientRect();
      setMousePos({ x: e.clientX - rect.left, y: e.clientY - rect.top });
    };
    document.addEventListener("mousemove", handleMouseMove);
    return () => document.removeEventListener("mousemove", handleMouseMove);
  }, []);

  const getMouseAngle = () => {
    return Math.atan2(mousePos.y - 300, mousePos.x - 300);
  };

  const shoot = () => {
    if (!gameOver) {
      const currentTime = Date.now();
      if (currentTime - lastShotTime >= 333) {
        const newBullet = { x: 300, y: 300, angle: getMouseAngle() };
        setBullets((curr) => [...curr, newBullet]);
        setLastShotTime(currentTime);
      }
    }
  };

  const spawnEnemy = () => {
    if (!gameOver) {
      const position = positions[Math.floor(Math.random() * positions.length)];
      setEnemies((curr) => [...curr, { ...position }]);
    }
  };

  const checkPlayerCollision = (enemies) => {
    for (const enemy of enemies) {
      const dx = Math.abs(enemy.left - 285);
      const dy = Math.abs(enemy.top - 285);
      const distance = Math.sqrt(dx * dx + dy * dy);

      if (distance < 30) {
        return true;
      }
    }
    return false;
  };

  const update = () => {
    setEnemies((curr) => {
      const newEnemies = curr.map((enemy) => {
        const dx = 285 - enemy.left;
        const dy = 285 - enemy.top;
        const angle = Math.atan2(dy, dx);
        return {
          ...enemy,
          top: enemy.top + enemySpeed * Math.sin(angle),
          left: enemy.left + enemySpeed * Math.cos(angle),
        };
      });

      if (checkPlayerCollision(newEnemies)) {
        setGameOver(true);
        clearInterval(spawnInterval.current);
        if (shootingInterval.current) {
          clearInterval(shootingInterval.current);
        }
      }

      return newEnemies;
    });

    setBullets((curr) => {
      const newBullets = curr.map((bullet) => ({
        ...bullet,
        x: bullet.x + bulletSpeed * Math.cos(bullet.angle),
        y: bullet.y + bulletSpeed * Math.sin(bullet.angle),
      }));
      return newBullets.filter(
        (bullet) =>
          bullet.x >= 0 && bullet.x <= 600 && bullet.y >= 0 && bullet.y <= 600
      );
    });
  };

  const checkCollisions = () => {
    const newBullets = [];
    const newEnemies = [...enemies];
    let eliminated = 0;
    bullets.forEach((bullet) => {
      let hit = false;
      for (let i = 0; i < newEnemies.length; i++) {
        const enemy = newEnemies[i];
        if (
          bullet.x >= enemy.left &&
          bullet.x <= enemy.left + 30 &&
          bullet.y >= enemy.top &&
          bullet.y <= enemy.top + 30
        ) {
          hit = true;
          newEnemies.splice(i, 1);
          eliminated++;
          break;
        }
      }
      if (!hit) {
        newBullets.push(bullet);
      }
    });
    if (eliminated > 0) {
      setScore((prev) => prev + eliminated);
      setEnemies(newEnemies);
      setBullets(newBullets);
    }
  };

  useEffect(() => {
    if (!gameOver) {
      const id = requestAnimationFrame(() => {
        update();
        checkCollisions();
      });
      return () => cancelAnimationFrame(id);
    }
  }, [gameOver, bullets, enemies]);

  return (
    <div className="game">
      <div ref={characterRef} className="character"></div>
      {enemies.map((enemy, index) => (
        <div
          key={index}
          className="enemy"
          style={{ top: enemy.top, left: enemy.left }}
        ></div>
      ))}
      {bullets.map((bullet, index) => (
        <div
          key={index}
          className="bullet"
          style={{ left: bullet.x, top: bullet.y }}
        ></div>
      ))}
      {gameOver && (
        <div className="game-over">Perdiste! Enemigos eliminados: {score}</div>
      )}
    </div>
  );
};

export default Game;
