let users = [];
let nextId = 1;

const createUser = (req, res) => {
  const { username, password, email, name, permission } = req.body;
  if (
    !username ||
    !password ||
    !email ||
    !name ||
    typeof permission !== "boolean"
  ) {
    return res.status(400).send({
      error: "Todos los campos son requeridos y deben tener valores válidos.",
    });
  }
  const newUser = { id: nextId++, username, password, email, name, permission };
  users.push(newUser);
  res.status(201).send(newUser);
};

const getUserById = (req, res) => {
  const userId = parseInt(req.params.id);
  const user = users.find((u) => u.id === userId);
  if (!user) {
    return res.status(404).send({ error: "Usuario no encontrado" });
  }
  res.status(200).send(user);
};

const getAllUsers = (req, res) => {
  const requesterId = parseInt(req.headers["requester-id"]);
  if (isNaN(requesterId)) {
    return res
      .status(400)
      .send({ error: "El ID del solicitante es requerido en el encabezado." });
  }
  const requester = users.find((u) => u.id === requesterId);
  if (!requester) {
    return res.status(404).send({ error: "Solicitante no encontrado." });
  }
  if (!requester.permission) {
    return res
      .status(403)
      .send({ error: "No permitido. Permisos insuficientes." });
  }
  res.status(200).send(users);
};

module.exports = {
  createUser,
  getUserById,
  getAllUsers,
};
