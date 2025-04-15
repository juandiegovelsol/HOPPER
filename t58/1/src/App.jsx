import React, { useState, useEffect } from "react";
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
          { nombre: nombreProyecto, id: Date.now() },
        ],
      }));
      setNombreProyecto("");
    }
  };

  const moverProyecto = (origen, destino, proyecto) => {
    setProyectos((prev) => {
      const origenArray = prev[origen].filter((p) => p.id !== proyecto.id);
      const destinoArray = [...prev[destino], proyecto];
      return {
        ...prev,
        [origen]: origenArray,
        [destino]: destinoArray,
      };
    });
  };

  const cambiarNombreProyecto = (id, nuevoNombre) => {
    setProyectos((prev) => {
      const proyectosActualizados = prev[id].map((p) =>
        p.id === id ? { ...p, nombre: nuevoNombre } : p
      );
      return { ...prev, [id]: proyectosActualizados };
    });
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
        <div className="columna" id="porIniciar">
          <h2>Por Iniciar</h2>
          {proyectos.porIniciar.map((proyecto) => (
            <div
              key={proyecto.id}
              className="proyecto"
              draggable
              onDragStart={(e) => {
                e.dataTransfer.setData("proyecto", JSON.stringify(proyecto));
              }}
            >
              {proyecto.nombre}
            </div>
          ))}
        </div>
        <div className="columna" id="enEjecucion">
          <h2>En Ejecución</h2>
          {proyectos.enEjecucion.map((proyecto) => (
            <div
              key={proyecto.id}
              className="proyecto"
              draggable
              onDragStart={(e) => {
                e.dataTransfer.setData("proyecto", JSON.stringify(proyecto));
              }}
            >
              {proyecto.nombre}
            </div>
          ))}
        </div>
        <div className="columna" id="terminados">
          <h2>Terminados</h2>
          {proyectos.terminados.map((proyecto) => (
            <div
              key={proyecto.id}
              className="proyecto"
              draggable
              onDragStart={(e) => {
                e.dataTransfer.setData("proyecto", JSON.stringify(proyecto));
              }}
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
