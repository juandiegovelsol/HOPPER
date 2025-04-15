const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

let invitations = [];
let nextId = 1;

app.post("/invitaciones", (req, res) => {
  const { name, guests, table, phone } = req.body;
  if (!name || !table || !phone || !Number.isInteger(guests) || guests <= 0) {
    return res.status(400).json({ error: "Datos invalidos" });
  }
  const newInvitation = {
    id: nextId++,
    name,
    guests,
    table,
    status: "pendiente",
    invitationSent: false,
    phone,
  };
  invitations.push(newInvitation);
  res.status(201).json(newInvitation);
});

app.get("/invitaciones", (req, res) => {
  res.json(invitations);
});

app.put("/invitaciones/:id", (req, res) => {
  const { id } = req.params;
  const { name, guests, table, phone, status, invitationSent } = req.body;
  const invitation = invitations.find((i) => i.id == id);
  if (
    !invitation ||
    (status && !["confirmado", "pendiente", "rechazado"].includes(status)) ||
    (invitationSent !== undefined && typeof invitationSent !== "boolean") ||
    (name && !table && !phone && !Number.isInteger(guests) && guests <= 0)
  ) {
    return res.status(400).json({ error: "Datos invalidos" });
  }
  invitation.name = name || invitation.name;
  invitation.guests =
    Number.isInteger(guests) && guests > 0 ? guests : invitation.guests;
  invitation.table = table || invitation.table;
  invitation.phone = phone || invitation.phone;
  invitation.status = status || invitation.status;
  invitation.invitationSent =
    invitationSent !== undefined ? invitationSent : invitation.invitationSent;
  res.json(invitation);
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
