import React, { useState } from "react";

const FormularioAgregarProyecto = ({ agregarProyecto }) => {
  const [nombreProyecto, setNombreProyecto] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (nombreProyecto.trim()) {
      agregarProyecto(nombreProyecto);
      setNombreProyecto("");
    }
  };

  return (
    <form className="formulario" onSubmit={handleSubmit}>
      <input
        type="text"
        value={nombreProyecto}
        onChange={(e) => setNombreProyecto(e.target.value)}
        placeholder="Nombre del proyecto"
      />
      <button type="submit">Agregar Proyecto</button>
    </form>
  );
};

export default FormularioAgregarProyecto;
