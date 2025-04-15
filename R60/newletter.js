const validator = require("validator");
const { v4: uuidv4 } = require("uuid");
const moment = require("moment");

let suscriptores = [];

function registrarSuscripcion(email, preferencias = []) {
  if (!validator.isEmail(email)) {
    throw new Error("Email no válido");
  }

  if (suscriptores.some((s) => s.email === email)) {
    throw new Error("El email ya está suscrito");
  }

  if (
    !Array.isArray(preferencias) ||
    preferencias.some((p) => typeof p !== "string")
  ) {
    throw new Error("Las preferencias deben ser un array de strings");
  }

  const nuevoSuscriptor = {
    id: uuidv4(),
    email,
    preferencias: [...new Set(preferencias)],
    fechaAlta: moment().format("YYYY-MM-DD HH:mm:ss"),
  };

  suscriptores.push(nuevoSuscriptor);
  return nuevoSuscriptor;
}

module.exports = { registrarSuscripcion, _test: () => (suscriptores = []) };
