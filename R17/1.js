const readline = require("readline");

// Crear una interfaz para leer datos desde la entrada estándar
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Función para generar contraseñas
function generarContrasena(
  longitud,
  incluirMayus,
  incluirMinus,
  incluirNumeros,
  incluirSimbolos
) {
  const caracteres = {
    mayusculas: "ABCDEFGHJKLMNPQRSTUVWXYZ", // Se excluyen caracteres ambiguos
    minusculas: "abcdefghijkmnpqrstuvwxyz", // Se excluyen caracteres ambiguos
    numeros: "23456789", // Se excluyen caracteres ambiguos
    simbolos: "!#$%&()*+-:;<=>?@[\\]_^",
  };

  let conjunto = "";

  if (incluirMayus) conjunto += caracteres.mayusculas;
  if (incluirMinus) conjunto += caracteres.minusculas;
  if (incluirNumeros) conjunto += caracteres.numeros;
  if (incluirSimbolos) conjunto += caracteres.simbolos;

  if (conjunto.length === 0) {
    console.log("Debes seleccionar al menos un tipo de carácter.");
    return null;
  }

  // Asegurarse de que la contraseña tenga al menos un carácter de cada tipo seleccionado
  const contrasena = [];

  if (incluirMayus)
    contrasena.push(
      caracteres.mayusculas[
        Math.floor(Math.random() * caracteres.mayusculas.length)
      ]
    );
  if (incluirMinus)
    contrasena.push(
      caracteres.minusculas[
        Math.floor(Math.random() * caracteres.minusculas.length)
      ]
    );
  if (incluirNumeros)
    contrasena.push(
      caracteres.numeros[Math.floor(Math.random() * caracteres.numeros.length)]
    );
  if (incluirSimbolos)
    contrasena.push(
      caracteres.simbolos[
        Math.floor(Math.random() * caracteres.simbolos.length)
      ]
    );

  // Completar la contraseña con caracteres aleatorios
  for (let i = contrasena.length; i < longitud; i++) {
    const randomIndex = Math.floor(Math.random() * conjunto.length);
    contrasena.push(conjunto[randomIndex]);
  }

  // Mezclar los caracteres de la contraseña
  return contrasena.sort(() => Math.random() - 0.5).join("");
}

// Función principal para interactuar con el usuario
function solicitarDatos() {
  rl.question(
    "Ingresar la longitud de la contraseña (mínimo 8): ",
    (longitud) => {
      longitud = parseInt(longitud, 10);
      if (isNaN(longitud) || longitud < 8) {
        console.log(
          "Longitud inválida. Debe ser un número mayor o igual a 8.\n"
        );
        return solicitarDatos();
      }

      rl.question("Incluir mayúsculas (s/n): ", (mayus) => {
        const incluirMayus = mayus.toLowerCase() === "s";

        rl.question("Incluir minúsculas (s/n): ", (minus) => {
          const incluirMinus = minus.toLowerCase() === "s";

          rl.question("Incluir números (s/n): ", (numeros) => {
            const incluirNumeros = numeros.toLowerCase() === "s";

            rl.question("Incluir símbolos (s/n): ", (simbolos) => {
              const incluirSimbolos = simbolos.toLowerCase() === "s";

              const contrasena = generarContrasena(
                longitud,
                incluirMayus,
                incluirMinus,
                incluirNumeros,
                incluirSimbolos
              );
              if (contrasena) {
                console.log(`Contraseña generada: ${contrasena}`);
              }

              // Preguntar nuevamente si se desea generar otra contraseña
              rl.question(
                "¿Deseas generar otra contraseña? (s/n): ",
                (respuesta) => {
                  if (respuesta.toLowerCase() === "s") {
                    solicitarDatos();
                  } else {
                    console.log(
                      "Gracias por usar el generador de contraseñas."
                    );
                    rl.close();
                  }
                }
              );
            });
          });
        });
      });
    }
  );
}

// Iniciar la solicitud de datos al usuario
solicitarDatos();
