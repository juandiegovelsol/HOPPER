import React, { useState } from "react";
import "./App.css";

function App() {
  const initialAttributes = {
    ataque: 5,
    defensa: 5,
    agilidad: 5,
    inteligencia: 5,
    carisma: 5,
  };

  const [puntos, setPuntos] = useState(15);
  const [atributos, setAtributos] = useState(initialAttributes);

  const asignarPuntos = (atributo, valor) => {
    if (puntos >= valor && puntos > 10) {
      setAtributos({
        ...atributos,
        [atributo]: atributos[atributo] + 1,
      });
      setPuntos(puntos - valor);
    }
  };

  return (
    <div className="App">
      <h1 className="titulo">Atributos</h1>
      <div className="container-tabla">
        <table>
          <thead>
            <tr>
              <th>Atributo</th>
              <th>Nivel</th>
              <th>+</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Ataque</td>
              <td>{atributos.ataque}</td>
              <td>
                <button onClick={() => asignarPuntos("ataque", 1)}>+</button>
              </td>
            </tr>
            <tr>
              <td>Defensa</td>
              <td>{atributos.defensa}</td>
              <td>
                <button onClick={() => asignarPuntos("defensa", 1)}>+</button>
              </td>
            </tr>
            <tr>
              <td>Agilidad</td>
              <td>{atributos.agilidad}</td>
              <td>
                <button onClick={() => asignarPuntos("agilidad", 1)}>+</button>
              </td>
            </tr>
            <tr>
              <td>Inteligencia</td>
              <td>{atributos.inteligencia}</td>
              <td>
                <button onClick={() => asignarPuntos("inteligencia", 1)}>
                  +
                </button>
              </td>
            </tr>
            <tr>
              <td>Carisma</td>
              <td>{atributos.carisma}</td>
              <td>
                <button onClick={() => asignarPuntos("carisma", 1)}>+</button>
              </td>
            </tr>
            <tr>
              <td>Puntos</td>
              <td>{puntos}</td>
              <td></td> <span className="gris">Sin botón</span>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
