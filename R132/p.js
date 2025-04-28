// Ejemplo de uso de .reduce para contar accesos por ruta
const logs = [
  { route: "/home", accesses: 1 },
  { route: "/about", accesses: 1 },
  { route: "/home", accesses: 1 },
];

const accessesByRoute = logs.reduce((acc, log) => {
  acc[log.route] = (acc[log.route] || 0) + log.accesses;
  return acc;
}, {});

console.log(accessesByRoute);
