import React, { useState } from "react";
import "./Tabla.css";

const Tabla = ({ proyectos, moverProyecto }) => {
  const manejarInicioDrag = (e, proyecto, origenColumnaId) => {
    const datos = JSON.stringify({
      proyectoId: proyecto.id,
      origen: origenColumnaId,
    });
    e.dataTransfer.setData("application/react-dnd-proyecto", datos);
    e.dataTransfer.effectAllowed = "move";
  };

  const manejarDragOver = (e) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = "move";
  };

  const manejarSoltar = (e, destinoColumnaId) => {
    e.preventDefault();
    const cadenaDatos = e.dataTransfer.getData(
      "application/react-dnd-proyecto"
    );
    if (!cadenaDatos) return;

    try {
      const { proyectoId, origen } = JSON.parse(cadenaDatos);
      if (origen !== destinoColumnaId) {
        moverProyecto(origen, destinoColumnaId, proyectoId);
      }
    } catch (error) {
      console.error("Error convirtiendo los datos:", error);
    }
  };

  return (
    <div className="contenedorColumnas">
      <div
        className="columna"
        id="porIniciar"
        onDragOver={manejarDragOver}
        onDrop={(e) => manejarSoltar(e, "porIniciar")}
      >
        <h2>Por Iniciar</h2>
        {proyectos.porIniciar.map((proyecto) => (
          <div
            key={proyecto.id}
            className="proyecto"
            draggable
            onDragStart={(e) => manejarInicioDrag(e, proyecto, "porIniciar")}
          >
            {proyecto.nombre}
          </div>
        ))}
      </div>
      <div
        className="columna"
        id="enEjecucion"
        onDragOver={manejarDragOver}
        onDrop={(e) => manejarSoltar(e, "enEjecucion")}
      >
        <h2>En Ejecución</h2>
        {proyectos.enEjecucion.map((proyecto) => (
          <div
            key={proyecto.id}
            className="proyecto"
            draggable
            onDragStart={(e) => manejarInicioDrag(e, proyecto, "enEjecucion")}
          >
            {proyecto.nombre}
          </div>
        ))}
      </div>
      <div
        className="columna"
        id="terminados"
        onDragOver={manejarDragOver}
        onDrop={(e) => manejarSoltar(e, "terminados")}
      >
        <h2>Terminados</h2>
        {proyectos.terminados.map((proyecto) => (
          <div
            key={proyecto.id}
            className="proyecto"
            draggable
            onDragStart={(e) => manejarInicioDrag(e, proyecto, "terminados")}
          >
            {proyecto.nombre}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Tabla;
