import React, { useState } from "react";

const Atributos = () => {
  const [atributos, setAtributos] = useState({
    ataque: 5,
    defensa: 5,
    agilidad: 5,
    inteligencia: 5,
    carisma: 5,
  });

  const [puntos, setPuntos] = useState(20);

  const aumentarAtributo = (atributo) => {
    if (puntos > 0) {
      setAtributos((prev) => ({
        ...prev,
        [atributo]: prev[atributo] + 1,
      }));
      setPuntos(puntos - 1);
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Pantalla de Atributos</h1>
      <table style={styles.table}>
        <thead>
          <tr>
            <th>Atributo</th>
            <th>Nivel</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          {Object.keys(atributos).map((key) => (
            <tr key={key}>
              <td style={styles.cell}>
                {key.charAt(0).toUpperCase() + key.slice(1)}
              </td>
              <td style={styles.cell}>{atributos[key]}</td>
              <td style={styles.cell}>
                <button
                  style={styles.button}
                  onClick={() => aumentarAtributo(key)}
                >
                  +
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <div style={styles.pointsContainer}>
        <span style={styles.pointsText}>Puntos: </span>
        <span style={styles.pointsValue}>{puntos}</span>
      </div>
    </div>
  );
};

const styles = {
  container: {
    backgroundColor: "#001f3f", // Azul oscuro
    color: "#fff", // Texto blanco
    padding: "20px",
    textAlign: "center",
    borderRadius: "10px",
    maxWidth: "600px",
    margin: "auto",
    marginTop: "50px",
  },
  title: {
    color: "#ffdc00", // Texto amarillo
  },
  table: {
    margin: "20px auto",
    borderCollapse: "collapse",
    width: "100%",
  },
  cell: {
    padding: "10px",
    border: "1px solid #ffffff",
  },
  button: {
    cursor: "pointer",
    backgroundColor: "#007bff",
    color: "#fff",
    border: "none",
    padding: "5px 10px",
    borderRadius: "5px",
    fontSize: "16px",
  },
  pointsContainer: {
    marginTop: "20px",
  },
  pointsText: {
    fontSize: "20px",
  },
  pointsValue: {
    fontSize: "20px",
    fontWeight: "bold",
  },
};

export default Atributos;
