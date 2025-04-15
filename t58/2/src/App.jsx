import React, { useState } from "react";
import "./App.css";

function App() {
  const [proyectos, setProyectos] = useState({
    porIniciar: [],
    enEjecucion: [],
    terminados: [],
  });

  const [nuevoProyecto, setNuevoProyecto] = useState("");

  const handleInputChange = (e) => {
    setNuevoProyecto(e.target.value);
  };

  const agregarProyecto = () => {
    if (nuevoProyecto.trim() !== "") {
      setProyectos({
        ...proyectos,
        porIniciar: [...proyectos.porIniciar, nuevoProyecto],
      });
      setNuevoProyecto("");
    }
  };

  const moverProyecto = (e, estadoDestino) => {
    const proyectoActual =
      e.target.parentElement.parentElement.parentElement.id;
    if (e.target.classList.contains("por-iniciar")) {
      setProyectos({
        ...proyectos,
        porIniciar: proyectos.porIniciar.filter(
          (proyecto) => proyecto !== proyectoActual
        ),
        [estadoDestino]: [...proyectos[estadoDestino], proyectoActual],
      });
    } else if (e.target.classList.contains("en-ejecucion")) {
      setProyectos({
        ...proyectos,
        enEjecucion: proyectos.enEjecucion.filter(
          (proyecto) => proyecto !== proyectoActual
        ),
        [estadoDestino]: [...proyectos[estadoDestino], proyectoActual],
      });
    } else if (e.target.classList.contains("terminados")) {
      setProyectos({
        ...proyectos,
        terminados: proyectos.terminados.filter(
          (proyecto) => proyecto !== proyectoActual
        ),
        [estadoDestino]: [...proyectos[estadoDestino], proyectoActual],
      });
    }
  };

  return (
    <div className="app">
      <h1>Control de Proyectos</h1>
      <div className="formulario">
        <input
          type="text"
          value={nuevoProyecto}
          onChange={handleInputChange}
          placeholder="Nuevo proyecto"
        />
        <button onClick={agregarProyecto}>Agregar</button>
      </div>
      <div className="contenedor-columnas">
        <div className="columna" id="por-iniciar">
          <h2>Por Iniciar</h2>
          {proyectos.porIniciar.length > 0 ? (
            proyectos.porIniciar.map((proyecto) => (
              <div
                key={proyecto}
                id={proyecto}
                className="tarjeta"
                draggable
                onDragStart={(e) => e.target.classList.add("dragging")}
                onDragEnd={(e) => e.target.classList.remove("dragging")}
              >
                {proyecto}
              </div>
            ))
          ) : (
            <p>No hay proyectos por iniciar</p>
          )}
        </div>
        <div className="columna" id="en-ejecucion">
          <h2>En Ejecución</h2>
          {proyectos.enEjecucion.length > 0 ? (
            proyectos.enEjecucion.map((proyecto) => (
              <div
                key={proyecto}
                id={proyecto}
                className="tarjeta"
                draggable
                onDragStart={(e) => e.target.classList.add("dragging")}
                onDragEnd={(e) => e.target.classList.remove("dragging")}
              >
                {proyecto}
              </div>
            ))
          ) : (
            <p>No hay proyectos en ejecución</p>
          )}
        </div>
        <div className="columna" id="terminados">
          <h2>Terminados</h2>
          {proyectos.terminados.length > 0 ? (
            proyectos.terminados.map((proyecto) => (
              <div
                key={proyecto}
                id={proyecto}
                className="tarjeta"
                draggable
                onDragStart={(e) => e.target.classList.add("dragging")}
                onDragEnd={(e) => e.target.classList.remove("dragging")}
              >
                {proyecto}
              </div>
            ))
          ) : (
            <p>No hay proyectos terminados</p>
          )}
        </div>
      </div>
      <div className="contenedor-botones">
        <button onClick={(e) => moverProyecto(e, "enEjecucion")}>
          &#8593;
        </button>
        <button onClick={(e) => moverProyecto(e, "terminados")}>&#8594;</button>
      </div>
    </div>
  );
}

export default App;
