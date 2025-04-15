import React, { useState } from "react";
import "./Formulario.css";

const Formulario = ({ agregarProyecto }) => {
  const [nombreProyecto, setNombreProyecto] = useState("");

  const manejarClick = () => {
    if (nombreProyecto.trim()) {
      agregarProyecto({
        nombre: nombreProyecto,
        id: Date.now().toString(),
      });
      setNombreProyecto("");
    }
  };

  return (
    <div className="formulario">
      <input
        type="text"
        value={nombreProyecto}
        onChange={(e) => setNombreProyecto(e.target.value)}
        placeholder="Nombre del proyecto"
      />
      <button onClick={manejarClick}>Agregar Proyecto</button>
    </div>
  );
};

export default Formulario;
