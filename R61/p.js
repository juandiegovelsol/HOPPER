class Encriptador {
  constructor(desplazamiento) {
    this.desplazamiento = desplazamiento % 26;
  }

  encriptar(texto) {
    return texto
      .split("")
      .map((c) => this._cifrarCaracter(c))
      .join("");
  }

  desencriptar(texto) {
    return texto
      .split("")
      .map((c) => this._descifrarCaracter(c))
      .join("");
  }

  _cifrarCaracter(c) {
    let codigo = c.charCodeAt(0);

    if (codigo >= 65 && codigo <= 90) {
      return String.fromCharCode(
        ((codigo - 65 + this.desplazamiento) % 26) + 65
      );
    }

    if (codigo >= 97 && codigo <= 122) {
      return String.fromCharCode(
        ((codigo - 97 + this.desplazamiento) % 26) + 97
      );
    }

    return c;
  }

  _descifrarCaracter(c) {
    let codigo = c.charCodeAt(0);

    if (codigo >= 65 && codigo <= 90) {
      return String.fromCharCode(
        ((codigo - 65 - this.desplazamiento + 26) % 26) + 65
      );
    }

    if (codigo >= 97 && codigo <= 122) {
      return String.fromCharCode(
        ((codigo - 97 - this.desplazamiento + 26) % 26) + 97
      );
    }

    return c;
  }
}

function prueba(nombre, valorEsperado, valorObtenido) {
  const resultado =
    valorEsperado === valorObtenido
      ? "✅ OK"
      : `❌ ERROR: se esperaba "${valorEsperado}", pero se obtuvo "${valorObtenido}"`;
  console.log(`${nombre}: ${resultado}`);
}
const encriptador = new Encriptador(3);

prueba("Encriptar 'hola'", "krod", encriptador.encriptar("hola"));
prueba(
  "Encriptar 'Hola Mundo'",
  "Krod Pxqgr",
  encriptador.encriptar("Hola Mundo")
);
prueba("Encriptar 'Zorro'", "Cruur", encriptador.encriptar("Zorro"));

prueba("Desencriptar 'krod'", "hola", encriptador.desencriptar("krod"));
prueba(
  "Desencriptar 'Krod Pxqgr'",
  "Hola Mundo",
  encriptador.desencriptar("Krod Pxqgr")
);
prueba("Desencriptar 'Cruur'", "Zorro", encriptador.desencriptar("Cruur"));

const otro = new Encriptador(13);
prueba("Encriptar 'abc' con desplazamiento 13", "nop", otro.encriptar("abc"));
prueba(
  "Desencriptar 'nop' con desplazamiento 13",
  "abc",
  otro.desencriptar("nop")
);
