import React, { useState } from "react";
import "./App.css";

const App = () => {
  const [proyectos, setProyectos] = useState({
    porIniciar: [],
    enEjecucion: [],
    terminados: [],
  });

  const [nombreProyecto, setNombreProyecto] = useState("");

  const agregarProyecto = () => {
    if (nombreProyecto.trim()) {
      setProyectos((prev) => ({
        ...prev,
        porIniciar: [
          ...prev.porIniciar,
          { nombre: nombreProyecto, id: Date.now().toString() },
        ],
      }));
      setNombreProyecto("");
    }
  };

  const moverProyecto = (origen, destino, proyectoId) => {
    setProyectos((prev) => {
      let proyectoMovido = null;
      const ArregloOrigen = prev[origen].filter((p) => {
        if (p.id === proyectoId) {
          proyectoMovido = p;
          return false;
        }
        return true;
      });

      if (!proyectoMovido) return prev;

      const ArregloDestino = [...(prev[destino] || []), proyectoMovido];

      return {
        ...prev,
        [origen]: ArregloOrigen,
        [destino]: ArregloDestino,
      };
    });
  };

  const handleDragStart = (e, proyecto, origenColumnaId) => {
    const data = JSON.stringify({
      proyectoId: proyecto.id,
      origen: origenColumnaId,
    });
    e.dataTransfer.setData("application/react-dnd-proyecto", data);
    e.dataTransfer.effectAllowed = "move";
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = "move";
  };

  const handleDrop = (e, destinoColumnaId) => {
    e.preventDefault();
    const dataString = e.dataTransfer.getData("application/react-dnd-proyecto");
    if (!dataString) return;

    try {
      const { proyectoId, origen } = JSON.parse(dataString);
      if (origen !== destinoColumnaId) {
        moverProyecto(origen, destinoColumnaId, proyectoId);
      }
    } catch (error) {
      console.error("Error convirtiendo los datos:", error);
    }
  };

  return (
    <div className="app">
      <h1>Administración de Proyectos</h1>
      <div className="formulario">
        <input
          type="text"
          value={nombreProyecto}
          onChange={(e) => setNombreProyecto(e.target.value)}
          placeholder="Nombre del proyecto"
        />
        <button onClick={agregarProyecto}>Agregar Proyecto</button>
      </div>
      <div className="contenedor-columnas">
        <div
          className="columna"
          id="porIniciar"
          onDragOver={handleDragOver}
          onDrop={(e) => handleDrop(e, "porIniciar")}
        >
          <h2>Por Iniciar</h2>
          {proyectos.porIniciar.map((proyecto) => (
            <div
              key={proyecto.id}
              className="proyecto"
              draggable
              onDragStart={(e) => handleDragStart(e, proyecto, "porIniciar")}
            >
              {proyecto.nombre}
            </div>
          ))}
        </div>
        <div
          className="columna"
          id="enEjecucion"
          onDragOver={handleDragOver}
          onDrop={(e) => handleDrop(e, "enEjecucion")}
        >
          <h2>En Ejecución</h2>
          {proyectos.enEjecucion.map((proyecto) => (
            <div
              key={proyecto.id}
              className="proyecto"
              draggable
              onDragStart={(e) => handleDragStart(e, proyecto, "enEjecucion")}
            >
              {proyecto.nombre}
            </div>
          ))}
        </div>
        <div
          className="columna"
          id="terminados"
          onDragOver={handleDragOver}
          onDrop={(e) => handleDrop(e, "terminados")}
        >
          <h2>Terminados</h2>
          {proyectos.terminados.map((proyecto) => (
            <div
              key={proyecto.id}
              className="proyecto"
              draggable
              onDragStart={(e) => handleDragStart(e, proyecto, "terminados")}
            >
              {proyecto.nombre}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;
