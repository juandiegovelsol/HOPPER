// app.js
const API_URL =
  "https://raw.githubusercontent.com/fjgonzalez25691/datos-embarazo-API/main/datos.json";
let incrementosPeso = [];

async function cargarDatos() {
  try {
    mostrarCarga();
    const response = await fetch(API_URL);

    if (!response.ok) {
      throw new Error(
        `Error ${response.status}: No se pudieron obtener los datos`
      );
    }

    const data = await response.json();
    incrementosPeso = data.incrementos;
    ocultarMensajes();
    return true;
  } catch (error) {
    console.error("Error fatal:", error);
    mostrarError(error.message);
    return false;
  } finally {
    ocultarCarga();
  }
}

function mostrarCarga() {
  document.getElementById("loading").style.display = "block";
  document.getElementById("error-api").style.display = "none";
  document.getElementById("resultado").style.display = "none";
}

function ocultarCarga() {
  document.getElementById("loading").style.display = "none";
}

function mostrarError(mensaje) {
  const errorDiv = document.getElementById("error-api");
  errorDiv.innerHTML = `⛔ Error grave: ${mensaje}<br>La aplicación no puede funcionar sin los datos.`;
  errorDiv.style.display = "block";
  document.querySelector("button").disabled = true;
}

function ocultarMensajes() {
  document.getElementById("loading").style.display = "none";
  document.getElementById("error-api").style.display = "none";
}

document.addEventListener("DOMContentLoaded", async () => {
  const exito = await cargarDatos();

  if (!exito) {
    document.getElementById("semana").disabled = true;
    document.getElementById("peso-inicial").disabled = true;
    document.getElementById("peso-actual").disabled = true;
    return;
  }

  // Generar opciones de semanas solo si la API funcionó
  const selectSemana = document.getElementById("semana");
  for (let i = 1; i <= 40; i++) {
    const option = document.createElement("option");
    option.value = i;
    option.textContent = `Semana ${i}`;
    selectSemana.appendChild(option);
  }

  document.getElementById("calcular").addEventListener("click", calcularPeso);
});

function calcularPeso() {
  const pesoInicial = parseFloat(document.getElementById("peso-inicial").value);
  const semana = parseInt(document.getElementById("semana").value);
  const pesoActual = parseFloat(document.getElementById("peso-actual").value);

  // Validaciones
  if (isNaN(pesoInicial) || isNaN(semana) || isNaN(pesoActual)) {
    alert("Por favor, completa todos los campos correctamente.");
    return;
  }

  if (semana < 1 || semana > 40) {
    alert("La semana de gestación debe estar entre 1 y 40.");
    return;
  }

  const datosSemana = incrementosPeso.find((item) => item.semana === semana);

  if (!datosSemana) {
    alert("No se encontraron datos para esta semana");
    return;
  }

  const gananciaPeso = pesoActual - pesoInicial;
  const gananciaMinima = datosSemana.min;
  const gananciaMedia = datosSemana.medio;
  const gananciaMaxima = datosSemana.max;

  const pesoMinimo = pesoInicial + gananciaMinima;
  const pesoMedio = pesoInicial + gananciaMedia;
  const pesoMaximo = pesoInicial + gananciaMaxima;

  let percentil, estado, clase;

  if (gananciaPeso < gananciaMinima) {
    percentil = "Por debajo del percentil 10";
    estado = "Fuera del rango (por debajo)";
    clase = "extreme-below";
  } else if (
    gananciaPeso >= gananciaMinima &&
    gananciaPeso < gananciaMedia * 0.9
  ) {
    percentil = "Entre percentil 10 y 25";
    estado = "Por debajo de la media pero dentro del rango";
    clase = "below";
  } else if (
    gananciaPeso >= gananciaMedia * 0.9 &&
    gananciaPeso <= gananciaMedia * 1.1
  ) {
    percentil = "Alrededor del percentil 50";
    estado = "En la media";
    clase = "normal";
  } else if (
    gananciaPeso > gananciaMedia * 1.1 &&
    gananciaPeso <= gananciaMaxima
  ) {
    percentil = "Entre percentil 75 y 90";
    estado = "Por encima de la media pero dentro del rango";
    clase = "above";
  } else {
    percentil = "Por encima del percentil 90";
    estado = "Fuera del rango (por encima)";
    clase = "extreme-above";
  }

  // Mostrar resultados
  document.getElementById("res-peso-inicial").textContent =
    pesoInicial.toLocaleString("es-ES");
  document.getElementById("res-semana").textContent = semana;
  document.getElementById("res-peso-actual").textContent =
    pesoActual.toLocaleString("es-ES");
  document.getElementById("res-ganancia").textContent =
    gananciaPeso.toLocaleString("es-ES", { maximumFractionDigits: 1 });

  const percentilElement = document.getElementById("percentil-resultado");
  percentilElement.innerHTML = `<p><strong>${percentil}</strong></p><p>${estado}</p>`;
  percentilElement.className = `percentil ${clase}`;

  document.getElementById("peso-minimo").textContent =
    pesoMinimo.toLocaleString("es-ES", { maximumFractionDigits: 1 });
  document.getElementById("ganancia-minima").textContent =
    gananciaMinima.toLocaleString("es-ES", { maximumFractionDigits: 1 });

  document.getElementById("peso-medio").textContent = pesoMedio.toLocaleString(
    "es-ES",
    { maximumFractionDigits: 1 }
  );
  document.getElementById("ganancia-media").textContent =
    gananciaMedia.toLocaleString("es-ES", { maximumFractionDigits: 1 });

  document.getElementById("peso-maximo").textContent =
    pesoMaximo.toLocaleString("es-ES", { maximumFractionDigits: 1 });
  document.getElementById("ganancia-maxima").textContent =
    gananciaMaxima.toLocaleString("es-ES", { maximumFractionDigits: 1 });

  document.getElementById("resultado").style.display = "block";
}
