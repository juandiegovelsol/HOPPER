const express = require("express");
const bodyParser = require("body-parser");
const inventoryRoutes = require("./inventory");

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use("/inventory", inventoryRoutes);

app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});
