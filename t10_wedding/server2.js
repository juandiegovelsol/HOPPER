const express = require("express");
const app = express();
app.use(express.json());

let invitations = [];
let currentId = 1;

app.post("/invitations", (req, res) => {
  const {
    name,
    guests,
    table,
    phone,
    status = "pendiente",
    invitationSent = false,
  } = req.body;

  if (!name || !table || !phone || guests <= 0 || !Number.isInteger(guests)) {
    return res.status(400).json({ error: "Datos inválidos" });
  }

  const invitation = {
    id: currentId++,
    name,
    guests,
    table,
    status,
    invitationSent,
    phone,
  };
  invitations.push(invitation);
  res.status(201).json(invitation);
});

app.get("/invitations", (req, res) => {
  res.json(invitations);
});

app.put("/invitations/:id", (req, res) => {
  const { id } = req.params;
  const { name, guests, table, phone, status, invitationSent } = req.body;

  const invitationIndex = invitations.findIndex(
    (inv) => inv.id === parseInt(id)
  );
  if (invitationIndex === -1) {
    return res.status(404).json({ error: "Invitación no encontrada" });
  }

  if (!name || !table || !phone || guests <= 0 || !Number.isInteger(guests)) {
    return res.status(400).json({ error: "Datos inválidos" });
  }

  if (status && !["confirmado", "pendiente", "rechazado"].includes(status)) {
    return res.status(400).json({ error: "Status inválido" });
  }

  if (invitationSent !== undefined && typeof invitationSent !== "boolean") {
    return res
      .status(400)
      .json({ error: "InvitationSent debe ser un booleano" });
  }

  invitations[invitationIndex] = {
    ...invitations[invitationIndex],
    name,
    guests,
    table,
    phone,
    status: status || invitations[invitationIndex].status,
    invitationSent:
      invitationSent !== undefined
        ? invitationSent
        : invitations[invitationIndex].invitationSent,
  };

  res.json(invitations[invitationIndex]);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
});
