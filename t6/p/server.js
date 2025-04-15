const express = require("express");
const bodyParser = require("body-parser");
const userRoutes = require("./users");

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.use("/users", userRoutes);

app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});
