import React, { useState } from "react";
import TablaProyectos from "./TablaProyectos";
import FormularioAgregarProyecto from "./FormularioAgregarProyecto";
import "./App.css";

const App = () => {
  const [proyectos, setProyectos] = useState({
    porIniciar: [],
    enEjecucion: [],
    terminados: [],
  });

  const agregarProyecto = (nombre) => {
    setProyectos((prev) => ({
      ...prev,
      porIniciar: [...prev.porIniciar, { nombre, id: Date.now().toString() }],
    }));
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
      <FormularioAgregarProyecto agregarProyecto={agregarProyecto} />
      <TablaProyectos proyectos={proyectos} moverProyecto={moverProyecto} />
    </div>
  );
};

export default App;
