import React from "react";
import Square from "./Square";

function Board({ board, turn, makeMove }) {
  return (
    <div
      style={{
        width: "320px",
        height: "320px",
        display: "grid",
        gridTemplate: "repeat(8, 1fr) / repeat(8, 1fr)",
      }}
    >
      {board.map((row, rowIndex) =>
        row.map((piece, colIndex) => (
          <Square
            key={`${rowIndex}-${colIndex}`}
            piece={piece}
            onClick={() => handleSquareClick(rowIndex, colIndex)}
          />
        ))
      )}
    </div>
  );

  function handleSquareClick(row, col) {
    // Aquí debes implementar la lógica para gestionar la selección y el movimiento de las piezas
  }
}

export default Board;
