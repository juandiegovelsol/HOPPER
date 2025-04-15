function buscarCoincidentes(a, b) {
  if (typeof a !== "string" || typeof b !== "string") {
    console.error("a y b deben ser strings");
    return undefined;
  }

  const longitudMinima = Math.min(a.length, b.length);
  let suma = 0;

  for (let i = 0; i < longitudMinima - 1; i++) {
    const subA = a.substring(i, i + 2);
    const subB = b.substring(i, i + 2);

    if (subA === subB) suma++;
  }

  return suma;
}

console.log(buscarCoincidentes((a = "uuucaabb"), (b = "uuubaab")));
console.log(buscarCoincidentes((a = "xyz"), (b = "xyz")));
console.log(buscarCoincidentes((a = "asc"), (b = "abc")));
console.log(buscarCoincidentes((a = "107"), (b = 107)));
console.log(buscarCoincidentes((a = "a"), (b = "a")));
