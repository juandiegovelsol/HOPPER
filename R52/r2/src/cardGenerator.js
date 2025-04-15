// CardGenerator.js

import React from "react";

function generateRandomNumber() {
  return Math.floor(Math.random() * 13) + 1;
}

function generateRandomSuit() {
  const suits = ["espadas", "corazones", "diamantes", "picas"];
  const randomIndex = Math.floor(Math.random() * suits.length);
  return suits[randomIndex];
}

class CardGenerator extends React.Component {
  static generateCard() {
    return {
      palo: generateRandomSuit(),
      número: generateRandomNumber(),
    };
  }
}

export default CardGenerator;
