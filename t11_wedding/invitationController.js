let invitations = [
  {
    id: 1,
    name: "Juan Perez",
    guests: 2,
    table: "1A",
    status: "confirmado",
    invitationSent: false,
    phone: "555-1234",
  },
  {
    id: 2,
    name: "Maria Lopez",
    guests: 1,
    table: "1B",
    status: "pendiente",
    invitationSent: false,
    phone: "555-5678",
  },
];

let currentId = invitations.length + 1;

const createInvitation = (req, res) => {
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
};

const getInvitations = (req, res) => {
  res.json(invitations);
};

const updateInvitation = (req, res) => {
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
};

const deleteInvitation = (req, res) => {
  const { id } = req.params;
  const invitationIndex = invitations.findIndex(
    (inv) => inv.id === parseInt(id)
  );
  if (invitationIndex === -1) {
    return res.status(404).json({ error: "Invitación no encontrada" });
  }
  invitations.splice(invitationIndex, 1);
  res.status(204).send();
};

const sendInvitation = (req, res) => {
  const { id } = req.params;
  const invitationIndex = invitations.findIndex(
    (inv) => inv.id === parseInt(id)
  );
  if (invitationIndex === -1) {
    return res.status(404).json({ error: "Invitación no encontrada" });
  }
  invitations[invitationIndex].invitationSent = true;
  res.json(invitations[invitationIndex]);
};

module.exports = {
  createInvitation,
  getInvitations,
  updateInvitation,
  deleteInvitation,
  sendInvitation,
};
