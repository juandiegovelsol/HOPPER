import React, { useState, useEffect } from "react";
import styled from "styled-components";
import { Chart } from "chart.js/auto";

// Estilos para el contenedor del componente
const Container = styled.div`
  font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const Button = styled.button`
  margin: 20px;
  padding: 10px;
  cursor: pointer;
`;

const Canvas = styled.canvas`
  max-width: 90%;
`;

// Función para generar precios aleatorios
const generateRandomPrices = () =>
  Array.from({ length: 289 }, () => (Math.random() * 100 + 100).toFixed(2));

// Función para calcular la media móvil
const calculateMovingAverage = (prices, n = 10) =>
  prices.map((_, idx, arr) =>
    idx >= n
      ? arr
          .slice(idx - n, idx)
          .reduce((a, b) => parseFloat(a) + parseFloat(b), 0) / n
      : null
  );

const PriceChartWithMovingAverage = () => {
  const [showMovingAverage, setShowMovingAverage] = useState(false);
  const [priceChart, setPriceChart] = useState(null);

  // Hook useEffect para inicializar el gráfico al montar el componente
  useEffect(() => {
    const prices = generateRandomPrices();
    const movingAverages = calculateMovingAverage(prices).map((val) =>
      val ? val.toFixed(2) : val
    );

    const ctx = document.getElementById("priceChart").getContext("2d");
    const chartInstance = new Chart(ctx, {
      type: "line",
      data: {
        labels: Array.from({ length: prices.length }, (_, i) => i + 1),
        datasets: [
          {
            label: "Precio",
            data: prices,
            borderColor: "blue",
            fill: false,
            pointRadius: 2,
          },
          {
            label: "Media Móvil",
            data: movingAverages,
            borderColor: "red",
            fill: false,
            pointRadius: 2,
            hidden: true,
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          x: { display: true, title: { display: true, text: "Días" } },
          y: {
            display: true,
            title: { display: true, text: "Precio (USD)" },
          },
        },
      },
    });
    setPriceChart(chartInstance);
  }, []);

  // Función para manejar el toggle de la media móvil
  const handleToggleMovingAverage = () => {
    if (priceChart) {
      const dataset = priceChart.data.datasets[1];
      dataset.hidden = !dataset.hidden;
      priceChart.update();

      setShowMovingAverage(!showMovingAverage);
    }
  };

  return (
    <Container>
      <h1>Gráfico de Precios con Media Móvil</h1>
      <Button onClick={handleToggleMovingAverage}>
        {showMovingAverage ? "Ocultar Media Móvil" : "Mostrar Media Móvil"}
      </Button>
      <Canvas id="priceChart" width="800" height="400"></Canvas>
    </Container>
  );
};

export default PriceChartWithMovingAverage;
