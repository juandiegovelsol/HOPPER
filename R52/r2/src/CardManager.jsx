// CardManager.js

import React, { useState } from "react";
import CardGenerator from "./CardGenerator";

function CardManager() {
  const [numCards, setNumCards] = useState(3);
  const [cards, setCards] = useState([]);
  const [sortSteps, setSortSteps] = useState([]);

  const handleInputChange = (e) => {
    const value = parseInt(e.target.value, 10);
    if (value >= 3 && value <= 10) {
      setNumCards(value);
    }
  };

  const generateCards = () => {
    const newCards = Array.from({ length: numCards }, () =>
      CardGenerator.generateCard()
    );
    setCards(newCards);
    setSortSteps([]);
  };

  const bubbleSort = (arr) => {
    let sortedArray = [...arr];
    let steps = [];
    let swapped;

    do {
      swapped = false;

      for (let i = 0; i < sortedArray.length - 1; i++) {
        if (sortedArray[i].número > sortedArray[i + 1].número) {
          [sortedArray[i], sortedArray[i + 1]] = [
            sortedArray[i + 1],
            sortedArray[i],
          ];
          swapped = true;
          steps.push([...sortedArray]);
        }
      }
    } while (swapped);

    return steps;
  };

  const sortCards = () => {
    const steps = bubbleSort(cards);
    setSortSteps(steps);
  };

  return (
    <div>
      <input
        type="number"
        min="3"
        max="10"
        value={numCards}
        onChange={handleInputChange}
      />
      <button onClick={generateCards}>Generar Cartas</button>
      <button onClick={sortCards}>Ordenar Cartas</button>

      <h3>Cartas Generadas:</h3>
      <ul>
        {cards.map((card, index) => (
          <li
            key={index}
          >{`{palo: "${card.palo}", número: ${card.número}}`}</li>
        ))}
      </ul>

      <h3>Pasos de Ordenamiento (Bubble Sort):</h3>
      {sortSteps.length > 0 && (
        <ul>
          {sortSteps.map((step, stepIndex) => (
            <li key={stepIndex}>
              {step.map((card, cardIndex) => (
                <span
                  key={cardIndex}
                >{`{palo: "${card.palo}", número: ${card.número}} `}</span>
              ))}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default CardManager;
