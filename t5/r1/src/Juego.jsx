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
  const [posicionPersonaje, setPosicionPersonaje] = useState({
    x: 285,
    y: 285,
  });
  const [teclaPresionada, setTeclaPresionada] = useState({
    w: false,
    a: false,
    s: false,
    d: false,
  });
  const velocidadEnemigo = 1;
  const velocidadBala = 5;
  const intervaloGeneracionEnemigos = useRef(null);

  useEffect(() => {
    intervaloGeneracionEnemigos.current = setInterval(generarEnemigo, 1000);
    return () => clearInterval(intervaloGeneracionEnemigos.current);
  }, []);

  useEffect(() => {
    const manejarKeyDown = (e) => {
      if (!juegoTerminado) {
        switch (e.key.toLowerCase()) {
          case "w":
            setTeclaPresionada((prev) => ({ ...prev, w: true }));
            break;
          case "s":
            setTeclaPresionada((prev) => ({ ...prev, s: true }));
            break;
          case "a":
            setTeclaPresionada((prev) => ({ ...prev, a: true }));
            break;
          case "d":
            setTeclaPresionada((prev) => ({ ...prev, d: true }));
            break;
          default:
            break;
        }
      }
    };

    const manejarKeyUp = (e) => {
      switch (e.key.toLowerCase()) {
        case "w":
          setTeclaPresionada((prev) => ({ ...prev, w: false }));
          break;
        case "s":
          setTeclaPresionada((prev) => ({ ...prev, s: false }));
          break;
        case "a":
          setTeclaPresionada((prev) => ({ ...prev, a: false }));
          break;
        case "d":
          setTeclaPresionada((prev) => ({ ...prev, d: false }));
          break;
        default:
          break;
      }
    };

    document.addEventListener("keydown", manejarKeyDown);
    document.addEventListener("keyup", manejarKeyUp);
    return () => {
      document.removeEventListener("keydown", manejarKeyDown);
      document.removeEventListener("keyup", manejarKeyUp);
    };
  }, [juegoTerminado]);

  const disparar = (e) => {
    if (!juegoTerminado) {
      const rect = e.currentTarget.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const clickY = e.clientY - rect.top;

      const personajeCentroX = posicionPersonaje.x + 15;
      const personajeCentroY = posicionPersonaje.y + 15;

      const dx = clickX - personajeCentroX;
      const dy = clickY - personajeCentroY;
      const angulo = Math.atan2(dy, dx);

      const nuevaBala = {
        x: personajeCentroX,
        y: personajeCentroY,
        angulo: angulo,
      };

      setBalas((actual) => [...actual, nuevaBala]);
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
      const dx = Math.abs(enemigo.left - posicionPersonaje.x);
      const dy = Math.abs(enemigo.top - posicionPersonaje.y);
      const distancia = Math.sqrt(dx * dx + dy * dy);
      if (distancia < 30) {
        return true;
      }
    }
    return false;
  };

  const actualizar = () => {
    if (teclaPresionada.w) {
      setPosicionPersonaje((prev) => ({ ...prev, y: Math.max(prev.y - 5, 0) }));
    }
    if (teclaPresionada.s) {
      setPosicionPersonaje((prev) => ({
        ...prev,
        y: Math.min(prev.y + 5, 570),
      }));
    }
    if (teclaPresionada.a) {
      setPosicionPersonaje((prev) => ({ ...prev, x: Math.max(prev.x - 5, 0) }));
    }
    if (teclaPresionada.d) {
      setPosicionPersonaje((prev) => ({
        ...prev,
        x: Math.min(prev.x + 5, 570),
      }));
    }

    setEnemigos((actual) => {
      const nuevosEnemigos = actual.map((enemigo) => {
        const dx = posicionPersonaje.x - enemigo.left;
        const dy = posicionPersonaje.y - enemigo.top;
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
  }, [juegoTerminado, balas, enemigos, teclaPresionada]);

  return (
    <div className="contenedor" onClick={disparar}>
      <div
        className="personaje"
        style={{ top: posicionPersonaje.y, left: posicionPersonaje.x }}
      ></div>
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
