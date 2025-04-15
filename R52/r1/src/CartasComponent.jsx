import React, { useState } from "react";
import BarajaComponent from "./BarajaComponent";

const CaballerosCartasComponent = ({ generarNumeroCartas }) => {
  const [inputValue, setInputValue] = useState("");
  const [cartas, setCartas] = useState([]);
  const [paso, setPaso] = useState([]);

  const generarCartas = () => {
    const numeroCartas = parseInt(inputValue, 10);
    if (
      Number.isInteger(numeroCartas) &&
      numeroCartas >= 3 &&
      numeroCartas <= 10
    ) {
      const cartasGeneradas = Array.from({ length: numeroCartas }, () => (
        <BarajaComponent />
      ));
      setCartas(cartasGeneradas);
    }
  };

  const bubbleSortCartas = () => {
    const cartasSorteadas = [...cartas];
    let intercambioRealizado;

    do {
      intercambioRealizado = false;
      for (let i = 0; i < cartasSorteadas.length - 1; i++) {
        const carta1 = cartasSorteadas[i];
        const carta2 = cartasSorteadas[i + 1];

        if (carta1.props.numero > carta2.props.numero) {
          [cartasSorteadas[i], cartasSorteadas[i + 1]] = [carta2, carta1];
          intercambioRealizado = true;
        }
      }
      if (intercambioRealizado) {
        setPaso([...paso, cartasSorteadas]);
      }
    } while (intercambioRealizado);

    setCartas(cartasSorteadas);
  };

  return (
    <div>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        maxLength="2"
        pattern="\d*"
        placeholder="3-10"
      />
      <button onClick={generarCartas}>Generar cartas</button>
      <button onClick={bubbleSortCartas}>Ordenar cartas</button>
      <ul>
        {cartas.map((carta, index) => (
          <li key={index}>
            {carta.props.palo}: {carta.props.numero}
          </li>
        ))}
      </ul>
      {paso.map((carta, index) => (
        <div key={index}>
          <h4>Paso {index + 1}</h4>
          <ul>
            {carta.map((c, idx) => (
              <li key={idx}>
                {c.props.palo}: {c.props.numero}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};

export default CaballerosCartasComponent;
