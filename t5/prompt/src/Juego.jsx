import React, { useState, useEffect, useRef } from "react";
import "./Juego.css";

const posicionesIniciales = [
  { top: 0, left: 0 },
  { top: 0, left: 550 },
  { top: 0, left: 300 },
  { top: 550, left: 0 },
  { top: 550, left: 300 },
  { top: 300, left: 0 },
  { top: 300, left: 550 },
  { top: 100, left: 100 },
  { top: 500, left: 500 },
  { top: 100, left: 500 },
];

const Juego = () => {
  const [balas, setBalas] = useState([]);
  const [enemigos, setEnemigos] = useState([]);
  const [puntaje, setPuntaje] = useState(0);
  const [juegoTerminado, setJuegoTerminado] = useState(false);
  const [posicionCursor, setPosicionCursor] = useState({ x: 300, y: 300 });
  const [estaDisparando, setEstaDisparando] = useState(false);
  const [ultimoTiempoDisparo, setUltimoTiempoDisparo] = useState(0);
  const referenciaPersonaje = useRef(null);
  const intervaloGeneracionEnemigos = useRef(null);
  const intervaloDisparo = useRef(null);
  const velocidadEnemigo = 1;
  const velocidadBala = 5;

  useEffect(() => {
    intervaloGeneracionEnemigos.current = setInterval(generarEnemigo, 1000);
    return () => clearInterval(intervaloGeneracionEnemigos.current);
  }, []);

  useEffect(() => {
    const manejarTeclaPresionada = (e) => {
      if (e.code === "Space" && !juegoTerminado && !estaDisparando) {
        setEstaDisparando(true);
        disparar();
        intervaloDisparo.current = setInterval(() => {
          disparar();
        }, 100);
      }
    };

    const manejarTeclaLevantada = (e) => {
      if (e.code === "Space") {
        setEstaDisparando(false);
        if (intervaloDisparo.current) {
          clearInterval(intervaloDisparo.current);
          intervaloDisparo.current = null;
        }
      }
    };

    document.addEventListener("keydown", manejarTeclaPresionada);
    document.addEventListener("keyup", manejarTeclaLevantada);

    return () => {
      document.removeEventListener("keydown", manejarTeclaPresionada);
      document.removeEventListener("keyup", manejarTeclaLevantada);
      if (intervaloDisparo.current) {
        clearInterval(intervaloDisparo.current);
      }
    };
  }, [juegoTerminado, estaDisparando]);

  useEffect(() => {
    const manejarMovimientoCursor = (e) => {
      const rect = document
        .querySelector(".contenedor")
        .getBoundingClientRect();
      setPosicionCursor({ x: e.clientX - rect.left, y: e.clientY - rect.top });
    };
    document.addEventListener("mousemove", manejarMovimientoCursor);
    return () =>
      document.removeEventListener("mousemove", manejarMovimientoCursor);
  }, []);

  const obtenerAnguloCursor = () => {
    return Math.atan2(posicionCursor.y - 300, posicionCursor.x - 300);
  };

  const disparar = () => {
    if (!juegoTerminado) {
      const tiempoActual = Date.now();
      if (tiempoActual - ultimoTiempoDisparo >= 100) {
        const nuevaBala = { x: 300, y: 300, angulo: obtenerAnguloCursor() };
        setBalas((actual) => [...actual, nuevaBala]);
        setUltimoTiempoDisparo(tiempoActual);
      }
    }
  };

  const generarEnemigo = () => {
    if (!juegoTerminado) {
      const posicion =
        posicionesIniciales[
          Math.floor(Math.random() * posicionesIniciales.length)
        ];
      setEnemigos((actual) => [...actual, { ...posicion }]);
    }
  };

  const verificarColisionJugador = (enemigos) => {
    for (const enemigo of enemigos) {
      const dx = Math.abs(enemigo.left - 285);
      const dy = Math.abs(enemigo.top - 285);
      const distancia = Math.sqrt(dx * dx + dy * dy);

      if (distancia < 30) {
        return true;
      }
    }
    return false;
  };

  const actualizar = () => {
    setEnemigos((actual) => {
      const nuevosEnemigos = actual.map((enemigo) => {
        const dx = 285 - enemigo.left;
        const dy = 285 - enemigo.top;
        const angulo = Math.atan2(dy, dx);
        return {
          ...enemigo,
          top: enemigo.top + velocidadEnemigo * Math.sin(angulo),
          left: enemigo.left + velocidadEnemigo * Math.cos(angulo),
        };
      });

      if (verificarColisionJugador(nuevosEnemigos)) {
        setJuegoTerminado(true);
        clearInterval(intervaloGeneracionEnemigos.current);
        if (intervaloDisparo.current) {
          clearInterval(intervaloDisparo.current);
        }
      }

      return nuevosEnemigos;
    });

    setBalas((actual) => {
      const nuevasBalas = actual.map((bala) => ({
        ...bala,
        x: bala.x + velocidadBala * Math.cos(bala.angulo),
        y: bala.y + velocidadBala * Math.sin(bala.angulo),
      }));
      return nuevasBalas.filter(
        (bala) => bala.x >= 0 && bala.x <= 600 && bala.y >= 0 && bala.y <= 600
      );
    });
  };

  const verificarColisiones = () => {
    const nuevasBalas = [];
    const nuevosEnemigos = [...enemigos];
    let eliminados = 0;
    balas.forEach((bala) => {
      let impacto = false;
      for (let i = 0; i < nuevosEnemigos.length; i++) {
        const enemigo = nuevosEnemigos[i];
        if (
          bala.x >= enemigo.left &&
          bala.x <= enemigo.left + 30 &&
          bala.y >= enemigo.top &&
          bala.y <= enemigo.top + 30
        ) {
          impacto = true;
          nuevosEnemigos.splice(i, 1);
          eliminados++;
          break;
        }
      }
      if (!impacto) {
        nuevasBalas.push(bala);
      }
    });
    if (eliminados > 0) {
      setPuntaje((previo) => previo + eliminados);
      setEnemigos(nuevosEnemigos);
      setBalas(nuevasBalas);
    }
  };

  useEffect(() => {
    if (!juegoTerminado) {
      const id = requestAnimationFrame(() => {
        actualizar();
        verificarColisiones();
      });
      return () => cancelAnimationFrame(id);
    }
  }, [juegoTerminado, balas, enemigos]);

  return (
    <div className="contenedor">
      <div ref={referenciaPersonaje} className="personaje"></div>
      {enemigos.map((enemigo, indice) => (
        <div
          key={indice}
          className="enemigo"
          style={{ top: enemigo.top, left: enemigo.left }}
        ></div>
      ))}
      {balas.map((bala, indice) => (
        <div
          key={indice}
          className="bala"
          style={{ left: bala.x, top: bala.y }}
        ></div>
      ))}
      {juegoTerminado && (
        <div className="perdiste">Perdiste! Enemigos eliminados: {puntaje}</div>
      )}
    </div>
  );
};

export default Juego;
