function esEspacio(c) {
  const codigo = c.charCodeAt(0);
  return codigo <= 32;
}

function esDigito(c) {
  const codigo = c.charCodeAt(0);
  return codigo >= 48 && codigo <= 57;
}

function compararDerecha(a, b) {
  let sesgo = 0;
  let ia = 0,
    ib = 0;
  let ca, cb;

  while (true) {
    ca = a.charAt(ia);
    cb = b.charAt(ib);

    if (!esDigito(ca) && !esDigito(cb)) {
      return sesgo;
    } else if (!esDigito(ca)) {
      return -1;
    } else if (!esDigito(cb)) {
      return +1;
    } else if (ca < cb) {
      if (sesgo === 0) sesgo = -1;
    } else if (ca > cb) {
      if (sesgo === 0) sesgo = 1;
    } else if (ca === 0 && cb === 0) {
      return sesgo;
    }

    ia++;
    ib++;
  }
}

function comparar(a, b) {
  let ia = 0,
    ib = 0;
  let nza = 0,
    nzb = 0;
  let ca, cb;
  let resultado;

  while (true) {
    nza = nzb = 0;
    ca = a.charAt(ia);
    cb = b.charAt(ib);

    while (esEspacio(ca) || ca == "0") {
      if (ca == "0") nza++;
      else nza = 0;

      ca = a.charAt(++ia);
    }

    while (esEspacio(cb) || cb == "0") {
      if (cb == "0") nzb++;
      else nzb = 0;

      cb = b.charAt(++ib);
    }

    if (esDigito(ca) && esDigito(cb)) {
      if ((resultado = compararDerecha(a.substring(ia), b.substring(ib))) != 0)
        return resultado;
    }

    if (ca == 0 && cb == 0) return nza - nzb;

    if (ca < cb) return -1;
    else if (ca > cb) return 1;

    ++ia;
    ++ib;
  }
}

let lista = ["apple", "apricot", "banana"];
lista.sort(comparar);
console.log(lista); // Debería mostrar ["archivo1", "archivo2", "archivo3", "archivo10", "archivo20"]
