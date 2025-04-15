import React, { useState } from "react";
import "./styles.css";

function App() {
  const [artistas, setArtistas] = useState([{ nombre: "", porcentaje: 0 }]);

  const handleInputChange = (index, field, value) => {
    const newArtistas = [...artistas];
    if (field === "nombre") {
      newArtistas[index].nombre = value;
    } else if (field === "porcentaje" && index < artistas.length - 1) {
      let numValue = parseInt(value, 10);
      if (isNaN(numValue) || numValue < 0) numValue = 0;
      newArtistas[index].porcentaje = numValue;
    }
    setArtistas(newArtistas);
  };

  const addArtist = () => {
    setArtistas([...artistas, { nombre: "", porcentaje: 0 }]);
  };

  const calculateRemainingPercentage = () => {
    return Math.max(
      100 -
        artistas
          .slice(0, -1)
          .reduce((sum, artist) => sum + artist.porcentaje, 0),
      0
    );
  };

  return (
    <div className="container">
      <h1>Distribución de Ganancias</h1>
      {artistas.map((artista, index) => (
        <div key={index} className="artista">
          <input
            type="text"
            placeholder="Nombre del Artista"
            value={artista.nombre}
            onChange={(e) => handleInputChange(index, "nombre", e.target.value)}
          />
          {index < artistas.length - 1 ? (
            <input
              type="number"
              placeholder="Porcentaje"
              min="0"
              max="100"
              value={artista.porcentaje}
              onChange={(e) =>
                handleInputChange(index, "porcentaje", e.target.value)
              }
            />
          ) : (
            <span>{calculateRemainingPercentage()}%</span>
          )}
        </div>
      ))}
      <button onClick={addArtist}>Añadir Artista</button>
      <div className="resultado">
        <h2>Resultados</h2>
        {artistas.map((artista, index) => (
          <div key={index}>
            <span>
              {artista.nombre}:{" "}
              {index < artistas.length - 1
                ? artista.porcentaje
                : calculateRemainingPercentage()}
              %
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
