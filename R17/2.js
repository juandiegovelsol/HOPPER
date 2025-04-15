const crypto = require("crypto");

// Función para generar una contraseña segura con opciones personalizadas
function generarContrasena(
  longitud = 8,
  usarMayusculas = true,
  usarMinusculas = true,
  usarNumeros = true,
  usarSimbolos = true
) {
  // Definir el juego de caracteres según las opciones elegidas
  let caracteresPosibles = "";
  if (usarMayusculas) caracteresPosibles += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  if (usarMinusculas) caracteresPosibles += "abcdefghijklmnopqrstuvwxyz";
  if (usarNumeros) caracteresPosibles += "0123456789";
  if (usarSimbolos) caracteresPosibles += "!@#$%^&*()_+-=[]{}|;:,.<>?";

  // Función interna para evitar caracteres ambiguos
  function evitarCaracteresAmbiguos(caracter) {
    const caracteresAmbiguos = ["l", "1", "O", "0", "@"];
    return !caracteresAmbiguos.includes(caracter);
  }

  // Filtro de caracteres para excluir los ambiguos
  const caracteresPosiblesFiltrados = caracteresPosibles.filter(
    evitarCaracteresAmbiguos
  );

  // Verificar que existan opciones válidas
  if (caracteresPosiblesFiltrados.length === 0) {
    console.error(
      "No hay caracteres válidos disponibles. Por favor, selecciona al menos un tipo de carácter."
    );
    return null;
  }

  // Generar la contraseña con una distribución aleatoria y cumplir con la longitud solicitada
  let contrasena = "";
  while (contrasena.length < longitud) {
    const caracterAleatorio =
      caracteresPosiblesFiltrados[
        Math.floor(Math.random() * caracteresPosiblesFiltrados.length)
      ];
    contrasena += caracterAleatorio;
  }

  // Mezclar la contraseña generada para evitar patrones predecibles
  return contrasena
    .split("")
    .sort(() => 0.5 - Math.random())
    .join("");
}

// Función principal para ejecutar en consola
function ejecutarGenerador() {
  const prompt = require("prompt-sync")();

  while (true) {
    try {
      // Solicitar al usuario la longitud de la contraseña y las opciones de caracteres
      console.log("\n--- Generador de Contraseñas Seguras ---");

      let longitud = parseInt(
        prompt("Ingrese la longitud de la contraseña (mínimo 8): "),
        10
      );
      if (isNaN(longitud) || longitud < 8) {
        throw new Error(
          "Longitud inválida. Debe ser un número igual o mayor a 8."
        );
      }

      // Preguntar por cada tipo de carácter
      const usarMayusculas =
        prompt("¿Incluir letras mayúsculas? (s/n) ").toLowerCase() === "s";
      const usarMinusculas =
        prompt("¿Incluir letras minúsculas? (s/n) ").toLowerCase() === "s";
      const usarNumeros =
        prompt("¿Incluir números? (s/n) ").toLowerCase() === "s";
      const usarSimbolos =
        prompt("¿Incluir símbolos? (s/n) ").toLowerCase() === "s";

      // Validación de que se seleccionen al menos algunos tipos de caracteres
      if (!usarMayusculas && !usarMinusculas && !usarNumeros && !usarSimbolos) {
        throw new Error("Debe seleccionar al menos un tipo de carácter.");
      }

      // Generar y mostrar la contraseña
      const contrasena = generarContrasena(
        longitud,
        usarMayusculas,
        usarMinusculas,
        usarNumeros,
        usarSimbolos
      );
      if (contrasena) {
        console.log(`\nContraseña generada: ${contrasena}`);
        console.log("Contraseña copiada al portapapeles!");
        // Copia la contraseña al portapapeles automáticamente
        require("clipboardy").write(contrasena); // Línea comentada para evitar uso de clipboard en ambientes controlados
      }

      // Preguntar si se desea generar otra contraseña
      const otra = prompt(
        "\n¿Deseas generar otra contraseña? (s/n) "
      ).toLowerCase();
      if (otra !== "s") {
        break; // Salir del ciclo si el usuario no quiere generar otra contraseña
      }
    } catch (error) {
      console.error(`Error: ${error.message}`);
    }
  }
}

// Ejecutar el generador de contraseñas
ejecutarGenerador();
