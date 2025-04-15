const fs = require("fs");

function isValidTimestamp(timestamp) {
  const regex =
    /^([0-2]\d|3[01])\/(0\d|1[0-2])\/(\d{4})\/([0-1]\d|2[0-3])\/([0-5]\d)\/([0-5]\d)$/;
  return regex.test(timestamp);
}

function isValidSensorData(sensors) {
  if (typeof sensors !== "object" || sensors === null) return false;
  for (const [sensorId, measurement] of Object.entries(sensors)) {
    if (typeof sensorId !== "string" || !(Number(measurement) >= 0)) {
      return false;
    }
  }
  return true;
}

fs.readFile("datos.json", "utf8", (err, data) => {
  if (err) throw err;
  const jsonData = JSON.parse(data);
  console.log(jsonData, data);
  const sensorData = {};

  for (const [timestamp, sensors] of Object.entries(jsonData)) {
    if (!isValidTimestamp(timestamp) || !isValidSensorData(sensors)) {
      console.error(`Error en el registro con la clave ${timestamp}`);
      continue;
    }

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
