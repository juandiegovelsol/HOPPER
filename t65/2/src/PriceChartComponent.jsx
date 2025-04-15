import React, { useEffect, useState } from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";
import "./PriceChartComponent.css";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

// Función para generar precios aleatorios (devuelve números)
const generateRandomPrices = () =>
  Array.from({ length: 289 }, () =>
    parseFloat((Math.random() * 100 + 100).toFixed(2))
  );

// Función para calcular la media móvil (trabaja con números)
const calculateMovingAverage = (prices, n = 10) =>
  prices.map((_, idx, arr) =>
    idx >= n - 1
      ? arr.slice(idx - n + 1, idx + 1).reduce((a, b) => a + b, 0) / n
      : null
  );

// Componente principal
const PriceChartComponent = () => {
  const [prices, setPrices] = useState([]);
  const [movingAverages, setMovingAverages] = useState([]);
  const [isMovingAverageVisible, setIsMovingAverageVisible] = useState(false);

  useEffect(() => {
    const initialPrices = generateRandomPrices();
    const initialMovingAverages = calculateMovingAverage(initialPrices);
    setPrices(initialPrices);
    setMovingAverages(initialMovingAverages);
  }, []);

  // Cambia el estado de visibilidad
  const toggleMediaMovilVisibility = () => {
    setIsMovingAverageVisible((prev) => !prev);
  };

  const dataChart = {
    labels: Array.from({ length: prices.length }, (_, i) => i + 1),
    datasets: [
      {
        label: "Precio",
        data: prices,
        borderColor: "blue",
        backgroundColor: "rgba(0, 0, 255, 0.1)",
        fill: false,
        pointRadius: 1,
        tension: 0.1,
      },
      {
        label: "Media Móvil",
        data: movingAverages,
        borderColor: "red",
        backgroundColor: "rgba(255, 0, 0, 0.1)",
        fill: false,
        pointRadius: 1,
        tension: 0.1,
        hidden: !isMovingAverageVisible,
      },
    ],
  };

  const optionsChart = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Gráfico de Precios y Media Móvil",
      },
      tooltip: {
        mode: "index",
        intersect: false,
      },
    },
    scales: {
      y: {
        beginAtZero: false,
      },
    },
    animation: {
      duration: 0,
    },
  };

  return (
    <div>
      <h1>Gráfico de Precios con Media Móvil</h1>
      <button id="toggleButton" onClick={toggleMediaMovilVisibility}>
        {isMovingAverageVisible ? "Ocultar" : "Mostrar"} Media Móvil
      </button>
      <div style={{ position: "relative", height: "400px", width: "800px" }}>
        {prices.length > 0 ? (
          <Line data={dataChart} options={optionsChart} />
        ) : (
          <p>Generando datos...</p>
        )}
      </div>
    </div>
  );
};

export default PriceChartComponent;
