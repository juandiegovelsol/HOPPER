import React, { useState } from "react";
import "./App.css";
import Formulario from "./Formulario";
import Tabla from "./Tabla";

const App = () => {
  const [proyectos, setProyectos] = useState({
    porIniciar: [],
    enEjecucion: [],
    terminados: [],
  });

  const agregarProyecto = (proyecto) => {
    setProyectos((prev) => ({
      ...prev,
      porIniciar: [...prev.porIniciar, proyecto],
    )));
  };

  const moverProyecto = (origen, destino, proyectoId) => {
    setProyectos((prev) => {
      let proyectoMovido = null;
      const arregloOrigen = prev[origen].filter((p) => {
        if (p.id === proyectoId) {
          proyectoMovido = p;
          return false;
        }
        return true;
      });

      if (!proyectoMovido) return prev;

      const arregloDestino = [...(prev[destino] || []), proyectoMovido];

      return {
        ...prev,
        [origen]: arregloOrigen,
        [destino]: arregloDestino,
      };
    });
  };

  return (
    <div className="aplicacion">
      <h1>Administración de Proyectos</h1>
      <Formulario agregarProyecto={agregarProyecto} />
      <Tabla proyectos={proyectos} moverProyecto={moverProyecto} />
    </div>
  );
};

export default App;