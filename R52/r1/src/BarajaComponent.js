import React, { useState } from "react";

const generarNumeroAleatorio = () => {
  return Math.floor(Math.random() * 13) + 1; // Genera un número entre 1 y 13
};

const generarPaloAleatorio = () => {
  const palos = ["espadas", "corazones", "diamantes", "picas"];
  return palos[Math.floor(Math.random() * palos.length)]; // Elige un palo al azar
};

const BarajaComponent = () => {
  const numeroAleatorio = generarNumeroAleatorio();
  const paloAleatorio = generarPaloAleatorio();
  const carta = { numero: numeroAleatorio, palo: paloAleatorio };

  return carta;
};

export default BarajaComponent;
