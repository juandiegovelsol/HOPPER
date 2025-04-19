import React from "react";

function Square({ piece, onClick }) {
  const backgroundColor = piece === "r" || piece === "b" ? "gray" : "white";
  return (
    <div
      onClick={onClick}
      style={{
        backgroundColor,
        width: "40px",
        height: "40px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      {piece && <Piece type={piece} />}
    </div>
  );
}

function Piece({ type }) {
  const color = type === "r" ? "red" : "black";
  return (
    <div
      style={{
        backgroundColor: color,
        borderRadius: "50%",
        width: "30px",
        height: "30px",
      }}
    />
  );
}

export default Square;
