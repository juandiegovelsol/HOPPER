const fs = require("fs");

fs.readFile("datos.json", "utf8", (err, data) => {
  if (err) throw err;

  try {
    const jsonData = JSON.parse(data);

    // Validación de la estructura y formato de los datos
    for (const [timestamp, sensors] of Object.entries(jsonData)) {
      // Validar que la fecha esté en el formato correcto y no sea vacía
      const validateTimestamp = /^\d{2}\/\d{2}\/\d{4}\/\d{2}\/\d{2}\/\d{2}$/;
      if (!validateTimestamp.test(timestamp)) {
        console.error(`Formato de fecha inválido en la clave: ${timestamp}`);
        continue; // Ignora el registro actual si la fecha es inválida
      }

      // Validar que cada valor de sensor sea un número positivo
      for (const [sensorId, measurement] of Object.entries(sensors)) {
        if (typeof measurement !== "number" || measurement < 0) {
          console.error(
            `Valor de medición inválido en el sensor ${sensorId} a las ${timestamp}`
          );
          continue; // Ignora el registro actual si la medición es inválida
        }
      }
    }

    // Procesamiento de datos después de la validación
    const sensorData = {};
    for (const [timestamp, sensors] of Object.entries(jsonData)) {
      for (const [sensorId, measurement] of Object.entries(sensors)) {
        if (sensorData[sensorId]) {
          const lastMeasurement = sensorData[sensorId];
          if (measurement < lastMeasurement * 0.5) {
            console.log(
              `Corte detectado en sensor ${sensorId} a las ${timestamp}`
            );
          }
        }
        sensorData[sensorId] = measurement;
      }
    }
  } catch (err) {
    console.error("Error al procesar los datos JSON:", err);
  }
});
