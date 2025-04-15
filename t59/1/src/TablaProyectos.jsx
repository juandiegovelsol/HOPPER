import React from "react";

const TablaProyectos = ({ proyectos, moverProyecto }) => {
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
      {["porIniciar", "enEjecucion", "terminados"].map((estado) => (
        <div
          className="columna"
          key={estado}
          onDragOver={manejarDragOver}
          onDrop={(e) => manejarSoltar(e, estado)}
        >
          <h2>{estado.replace(/([A-Z])/g, " $1").trim()}</h2>
          {proyectos[estado].map((proyecto) => (
            <div
              key={proyecto.id}
              className="proyecto"
              draggable
              onDragStart={(e) => manejarInicioDrag(e, proyecto, estado)}
            >
              {proyecto.nombre}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default TablaProyectos;
