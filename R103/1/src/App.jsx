import React, { useState } from "react";
import Board from "./Board";

const initialBoard = [
  // Define aquí la configuración inicial del tablero
  ["b", null, "b", null, "b", null, "b", null],
  [null, "b", null, "b", null, "b", null, "b"],
  ["b", null, "b", null, "b", null, "b", null],
  [null, null, null, null, null, null, null, null],
  [null, null, null, null, null, null, null, null],
  ["r", null, "r", null, "r", null, "r", null],
  [null, "r", null, "r", null, "r", null, "r"],
  ["r", null, "r", null, "r", null, "r", null],
];

function App() {
  const [board, setBoard] = useState(initialBoard);
  const [history, setHistory] = useState([initialBoard]);
  const [turn, setTurn] = useState("r"); // 'r' para rojo y 'b' para negro

  const undoMove = () => {
    if (history.length > 1) {
      const newHistory = history.slice(0, -1);
      setHistory(newHistory);
      setBoard(newHistory[newHistory.length - 1]);
      setTurn(turn === "r" ? "b" : "r");
    }
  };

  const makeMove = (from, to) => {
    // Implementar lógica para mover una pieza de "from" a "to"
  };

  return (
    <div>
      <Board board={board} turn={turn} makeMove={makeMove} />
      <button onClick={undoMove}>Deshacer</button>
    </div>
  );
}

export default App;
