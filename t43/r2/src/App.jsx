import React, { useState } from "react";
import "./App.css";

function App() {
  const [artists, setArtists] = useState([{ name: "", percentage: "" }]);

  const handleInputChange = (index, field, value) => {
    const updatedArtists = [...artists];
    if (field === "percentage" && value !== "") {
      value = parseInt(value, 10);
      if (isNaN(value) || value < 0) return;
    }
    updatedArtists[index][field] = value;
    setArtists(updatedArtists);
  };

  const addArtist = () => {
    setArtists([...artists, { name: "", percentage: "" }]);
  };

  const removeArtist = (index) => {
    const updatedArtists = artists.filter((_, i) => i !== index);
    setArtists(updatedArtists);
  };

  const calculateRemaining = () => {
    const total = artists.reduce((sum, artist) => {
      return sum + (parseInt(artist.percentage, 10) || 0);
    }, 0);
    return 100 - total;
  };

  return (
    <div className="App">
      <h1>Distribución de Ganancias</h1>
      {artists.map((artist, index) => (
        <div key={index} className="artist-row">
          <input
            type="text"
            placeholder="Nombre del artista"
            value={artist.name}
            onChange={(e) => handleInputChange(index, "name", e.target.value)}
          />
          <input
            type="number"
            placeholder="Porcentaje"
            value={artist.percentage}
            onChange={(e) =>
              handleInputChange(index, "percentage", e.target.value)
            }
            disabled={index === artists.length - 1}
          />
          {index === artists.length - 1 ? (
            <span>{calculateRemaining()}%</span>
          ) : (
            <button onClick={() => removeArtist(index)}>Eliminar</button>
          )}
        </div>
      ))}
      <button onClick={addArtist}>Agregar Artista</button>
      <div>
        <h2>Resumen</h2>
        {artists.map((artist, index) => (
          <div key={index}>
            <span>{artist.name ? artist.name : "Artista sin nombre"} - </span>
            <span>
              {index === artists.length - 1
                ? calculateRemaining()
                : artist.percentage || 0}
              %
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
