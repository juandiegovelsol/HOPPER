// dashboard.js - Web Worker
self.onmessage = (event) => {
  const data = event.data;

  // Transformación de datos (aquí puedes incluir más lógica)
  const transformedData = {
    formattedPrice: `${data.price} €`,
    timestamp: new Date().toLocaleTimeString(),
  };

  // Enviar los datos transformados de vuelta al hilo principal
  self.postMessage(transformedData);
};
