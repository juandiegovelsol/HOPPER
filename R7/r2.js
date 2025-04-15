const fs = require("fs");
const path = require("path");
const { performance } = require("perf_hooks");
const { parse } = require("json2csv");
const Cryptocurrencies_Data = require("./Cryptocurrencies_Data.json");
//const Cryptocurrencies_Data = jsonData; //Use this line to use data directly

// Función para calcular la rentabilidad
const calculateProfitability = (currentPrice, projection) => {
  return ((projection - currentPrice) / currentPrice) * 100;
};

// Función para generar un gráfico de barras usando Chart.js
const generateBarChart = (data) => {
  const ctx = document.getElementById("myChart").getContext("2d");
  const myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: data.map((crypto) => crypto.name),
      datasets: [
        {
          label: "Rentabilidad (%)",
          data: data.map((crypto) => crypto.profitability),
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        x: {
          title: {
            display: true,
            text: "Criptomonedas (Rotadas a 30°)",
          },
          font: {
            size: 12,
          },
          // Rota el texto del eje X a 30 grados
          // Este ajuste ayuda a mejorar la legibilidad cuando hay muchas etiquetas
          ticks: {
            // Se aplica la rotación a las etiquetas del eje X
            rotate: 30,
            // Se establece un límite máximo para la cantidad de etiquetas visibles
            maxRotation: 30,
            // Se establece un callback para generar las etiquetas
            callback: (value) => `${value}`,
          },
        },
        y: {
          title: {
            display: true,
            text: "Rentabilidad (%)",
          },
          beginAtZero: true, // Comienza en cero
          ticks: {
            stepSize: 10, // Incremento de 10 en 10
            min: -30, // Mínimo de -30 para incluir valores negativos
            max: 100, // Máximo de 100 para valores positivos
          },
        },
      },
      plugins: {
        tooltip: {
          callbacks: {
            title: function (context) {
              // Se obtiene el índice del elemento actual
              const index = context[0].raw;
              // Se retorna el nombre de la criptomoneda como título
              return `Criptomoneda: ${context[0].label}`;
            },
            label: function (context) {
              // Formateo del valor para mostrar el porcentaje con dos decimales
              return `Rentabilidad: ${context.raw.toFixed(2)}%`;
            },
          },
        },
      },
    },
  });
};

// Cálculo de rentabilidad y almacenamiento de resultados en un array
const cryptocurrencies = Cryptocurrencies_Data.map((crypto) => {
  const profitability = calculateProfitability(
    crypto.PrecioActual,
    crypto.Proyeccion
  );
  return {
    name: crypto.Nombre,
    profitability: profitability,
  };
});

// Ordenar por rentabilidad de menor a mayor
cryptocurrencies.sort((a, b) => a.profitability - b.profitabilidad);

// Generación del gráfico de barras con Chart.js
generateBarChart(cryptocurrencies);
