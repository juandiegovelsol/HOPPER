// 67d3d1305d3860772ad4895e

const { object, string, date, number } = require("yup");

const schema = object().shape({
  marca: string().required(),
  modelo: string().required(),
  fecha_adquisicion: date().required(),
  precio_compra: number().required(),
});

// Validación
const data = {
  marca: "A1",
  modelo: "M1",
  fecha_adquisicion: "03/24/2018",
  precio_compra: 18000,
};

schema
  .validate(data)
  .then(() => {
    console.log("Valid!");
  })
  .catch((err) => {
    console.log("Invalid!", err.errors);
  });
