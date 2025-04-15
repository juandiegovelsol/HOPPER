// Definir y exportar constantes globales necesarias
const DENSIDAD_AGUA = 1025;
const GRAVEDAD = 9.81;

// Función para calcular la fuerza de las olas en función de varios parámetros
function calcularFuerza(altura, velocidadViento, direccionViento, profundidad) {
  let fuerzaBase = altura * velocidadViento;

  if (direccionViento.includes("Este")) {
    fuerzaBase *= 1.2;
  } else if (direccionViento.includes("Oeste")) {
    fuerzaBase *= 0.8;
  }

  if (profundidad < 20) {
    fuerzaBase *= 0.9;
  } else if (profundidad > 30) {
    fuerzaBase *= 1.1;
  }

  if (fuerzaBase < 10) {
    return "Débil";
  } else if (fuerzaBase >= 10 && fuerzaBase < 20) {
    return "Moderada";
  } else if (fuerzaBase >= 20 && fuerzaBase < 30) {
    return "Fuerte";
  } else {
    return "Muy Fuerte";
  }
}

// Función para calcular la energía generada por las olas
function calcularEnergia(altura) {
  const longitudOla = altura * 10;
  return (DENSIDAD_AGUA * GRAVEDAD * Math.pow(altura, 2) * longitudOla) / 8;
}

// Función para procesar los datos de las olas y mostrar resultados
function procesarDatosOlas(datosOlas) {
  datosOlas.forEach((ola) => {
    const fuerza = calcularFuerza(
      ola.altura,
      ola.velocidadViento,
      ola.direccionViento,
      ola.profundidad
    );
    const energia = calcularEnergia(ola.altura);

    console.log(`Fecha: ${ola.fecha}`);
    console.log(`- Altura: ${ola.altura}m`);
    console.log(`- Velocidad del viento: ${ola.velocidadViento} m/s`);
    console.log(`- Dirección del viento: ${ola.direccionViento}`);
    console.log(`- Profundidad: ${ola.profundidad}m`);
    console.log(`- Fuerza de las olas: ${fuerza}`);
    console.log(`- Energía generada: ${energia.toFixed(2)} joules`);
    console.log("----------------------------------------");
  });
}

// Función principal para ejecutar el cálculo completo del análisis de olas
function hacerCalculo() {
  const datosOlas = [
    {
      fecha: "01/10/2023",
      altura: 1.5,
      velocidadViento: 10,
      direccionViento: "Norte",
      profundidad: 20,
    },
    {
      fecha: "02/10/2023",
      altura: 2.0,
      velocidadViento: 15,
      direccionViento: "Noreste",
      profundidad: 25,
    },
    {
      fecha: "03/10/2023",
      altura: 2.5,
      velocidadViento: 20,
      direccionViento: "Este",
      profundidad: 30,
    },
    {
      fecha: "04/10/2023",
      altura: 1.8,
      velocidadViento: 12,
      direccionViento: "Sur",
      profundidad: 18,
    },
    {
      fecha: "05/10/2023",
      altura: 3.0,
      velocidadViento: 25,
      direccionViento: "Suroeste",
      profundidad: 35,
    },
  ];

  procesarDatosOlas(datosOlas);

  const fechaActual = "06/10/2023";
  const precioEnEuros = 150.75;
  console.log(`\nFecha: ${fechaActual}, Precio: ${precioEnEuros} EUR`);
}

// Ejecutar la función principal
hacerCalculo();
