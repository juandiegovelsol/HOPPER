import React, { useState } from "react";
import "./App.css";

function App() {
  // Inicializa el estado del jugador actual como "X"
  const [currentPlayer, setCurrentPlayer] = useState("X");

  // Inicializa el estado de las partidas pequeñas como una matriz de 9x9 con valores nulos
  const [smallBoardStates, setSmallBoardStates] = useState(
    Array(9)
      .fill(null)
      .map(() => Array(9).fill(null))
  );

  // Inicializa el estado de los ganadores de las partidas pequeñas como un array de 9 elementos nulos
  const [smallBoardWinners, setSmallBoardWinners] = useState(
    Array(9).fill(null)
  );

  // Inicializa el estado del tablero principal como un array de 9 elementos nulos
  const [mainBoardState, setMainBoardState] = useState(Array(9).fill(null));

  // Inicializa el estado para saber si el juego está activo
  const [gameActive, setGameActive] = useState(true);

  // Inicializa el mensaje para el siguiente turno
  const [message, setMessage] = useState("Siguiente turno: X");

  // Inicializa el estado de la línea ganadora en nulo
  const [winningLine, setWinningLine] = useState(null);

  function checkWinner(board) {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];
    for (let line of lines) {
      const [a, b, c] = line;
      if (board[a] && board[a] === board[b] && board[a] === board[c]) {
        return { winner: board[a], line };
      }
    }
    return null;
  }

  function handleCellClick(superIndex, cellIndex) {
    if (
      !gameActive ||
      smallBoardWinners[superIndex] ||
      smallBoardStates[superIndex][cellIndex]
    ) {
      return;
    }

    const newSmallBoardStates = smallBoardStates.map((board, idx) => {
      if (idx === superIndex) {
        const newBoard = [...board];
        newBoard[cellIndex] = currentPlayer;
        return newBoard;
      }
      return board;
    });
    // Actualiza el estado de los tableros pequeños
    setSmallBoardStates(newSmallBoardStates);

    const smallWinner = checkWinner(newSmallBoardStates[superIndex]);
    const newSmallBoardWinners = [...smallBoardWinners];
    const newMainBoardState = [...mainBoardState];
    if (smallWinner) {
      newSmallBoardWinners[superIndex] = smallWinner.winner;
      newMainBoardState[superIndex] = smallWinner.winner;

      // Establece el nuevo estado de los ganadores
      setSmallBoardWinners(newSmallBoardWinners);

      // Establece el nuevo estado del tablero principal
      setMainBoardState(newMainBoardState);

      const mainWinner = checkWinner(newMainBoardState);
      if (mainWinner) {
        // Establece el mensaje de victoria y actualiza el estado del juego
        setMessage(`El jugador ${mainWinner.winner} gana el juego!`);

        // Actualiza el estado para terminar el juego
        setGameActive(false);

        // Actualiza la línea ganadora para mostrarla
        setWinningLine(mainWinner.line);
        return;
      }
    }

    const nextPlayer = currentPlayer === "X" ? "O" : "X";

    // Actualiza el estado del jugador actual
    setCurrentPlayer(nextPlayer);

    // Actualiza el mensaje del turno siguiente
    setMessage(`Siguiente turno: ${nextPlayer}`);
  }

  function resetGame() {
    if (gameActive) {
      const xWins = smallBoardWinners.filter((winner) => winner === "X").length;
      const oWins = smallBoardWinners.filter((winner) => winner === "O").length;
      if (xWins > oWins) {
        alert("El jugador X gana la partida no terminada!");
      } else if (oWins > xWins) {
        alert("El jugador O gana la partida no terminada!");
      }
    }

    // Reinicia el jugador actual al valor incial
    setCurrentPlayer("X");

    // Restablece el estado de los tableros pequeños
    setSmallBoardStates(
      Array(9)
        .fill(null)
        .map(() => Array(9).fill(null))
    );

    // Restablece los ganadores de los tableros pequeños
    setSmallBoardWinners(Array(9).fill(null));

    // Restablece el estado del tablero principal
    setMainBoardState(Array(9).fill(null));

    // Reinicia el estado del juego a activo
    setGameActive(true);

    // Restablece el mensaje
    setMessage("Siguiente turno: X");

    // Reinicia la línea ganadora a nula
    setWinningLine(null);
  }

  return (
    <div className="container">
      <h1>Súper Gato</h1>
      <div className="super-grid" id="superGrid">
        {Array.from({ length: 9 }).map((_, superIndex) => (
          <div
            key={superIndex}
            className="super-cell"
            data-super-index={superIndex}
          >
            <div className="sub-grid" data-grid-index={superIndex}>
              {Array.from({ length: 9 }).map((_, cellIndex) => (
                <div
                  key={cellIndex}
                  className="cell"
                  data-cell-index={cellIndex}
                  onClick={() => handleCellClick(superIndex, cellIndex)}
                >
                  {smallBoardStates[superIndex][cellIndex]}
                </div>
              ))}
            </div>
            {smallBoardWinners[superIndex] && (
              <div className="small-winner">
                {smallBoardWinners[superIndex]}
              </div>
            )}
          </div>
        ))}
        {winningLine && (
          <div className={`winning-line line-${winningLine.join("-")}`}></div>
        )}
      </div>
      <p id="message">{message}</p>
      <button id="resetButton" onClick={resetGame}>
        Reiniciar Juego
      </button>
    </div>
  );
}

export default App;
