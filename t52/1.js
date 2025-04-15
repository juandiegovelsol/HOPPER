const fs = require("fs");

fs.readFile("datos.json", "utf8", (err, data) => {
  if (err) throw err;
  const jsonData = JSON.parse(data);
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
});
