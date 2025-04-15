let inventory = [
  { id: 1, name: "Pelota", price: 5000, quantity: 10 },
  { id: 2, name: "Auto de juguete", price: 15000, quantity: 5 },
  { id: 3, name: "Muñeca", price: 12000, quantity: 8 },
  { id: 4, name: "Rompecabezas", price: 8000, quantity: 12 },
  { id: 5, name: "Bloques de construcción", price: 20000, quantity: 3 },
];

let nextId = 6;

const createToy = (req, res) => {
  const { name, price, quantity } = req.body;
  if (!name || !price || !quantity) {
    return res
      .status(400)
      .send({ error: "Nombre, precio y cantidad son requeridos." });
  }
  const newToy = { id: nextId++, name, price, quantity };
  inventory.push(newToy);
  res.status(201).send(newToy);
};

const updateToyQuantity = (req, res) => {
  const toyId = parseInt(req.params.id);
  const { quantity } = req.body;
  if (quantity === undefined) {
    return res.status(400).send({ error: "La cantidad es requerida." });
  }
  const toy = inventory.find((t) => t.id === toyId);
  if (!toy) {
    return res.status(404).send({ error: "Juguete no encontrado." });
  }
  toy.quantity = quantity;
  res.status(200).send(toy);
};

const createOrder = (req, res) => {
  const order = req.body;
  let total = 0;
  for (const itemId in order) {
    const toyId = parseInt(itemId);
    const quantity = order[itemId];
    const toy = inventory.find((t) => t.id === toyId);
    if (!toy) {
      return res
        .status(400)
        .send({ error: `Juguete con ID ${toyId} no encontrado.` });
    }
    if (toy.quantity < quantity) {
      return res.status(400).send({
        error: `No hay suficiente stock para el juguete ${toy.name}.`,
      });
    }
    total += toy.price * quantity;
    toy.quantity -= quantity;
  }
  res.status(200).send({ total });
};

module.exports = {
  createToy,
  updateToyQuantity,
  createOrder,
};
