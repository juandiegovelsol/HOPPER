import React, { useState } from "react";
import "./App.css";

function App() {
  const [invitations, setInvitations] = useState([
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
    {
      id: 3,
      name: "Carlos Ramirez",
      guests: 3,
      table: "2A",
      status: "rechazado",
      invitationSent: false,
      phone: "555-8765",
    },
    {
      id: 4,
      name: "Ana Torres",
      guests: 2,
      table: "2B",
      status: "confirmado",
      invitationSent: false,
      phone: "555-4321",
    },
  ]);

  const sendInvitation = (phone) => {
    console.log(`Invitación enviada a ${phone}`);
    setInvitations(
      invitations.map((inv) =>
        inv.phone === phone ? { ...inv, invitationSent: true } : inv
      )
    );
  };

  const editInvitation = (id) => {
    let updatedName = prompt("Nuevo nombre:");
    while (!updatedName || updatedName.trim() === "") {
      updatedName = prompt("Nombre inválido. Ingrese un nombre no vacío:");
    }
    let guestsInput = prompt("Nuevo número de invitados:");
    let updatedGuests = parseInt(guestsInput, 10);
    while (isNaN(updatedGuests) || updatedGuests <= 0) {
      guestsInput = prompt(
        "Número de invitados inválido. Ingrese un entero positivo:"
      );
      updatedGuests = parseInt(guestsInput, 10);
    }
    let updatedTable = prompt("Nueva mesa:");
    while (!updatedTable || updatedTable.trim() === "") {
      updatedTable = prompt("Mesa inválida. Ingrese una mesa no vacía:");
    }
    let updatedStatus = prompt(
      "Nuevo estado (confirmado/pendiente/rechazado):"
    );
    const validStatuses = ["confirmado", "pendiente", "rechazado"];
    while (!validStatuses.includes(updatedStatus)) {
      updatedStatus = prompt(
        "Estado inválido. Ingrese: confirmado, pendiente o rechazado:"
      );
    }
    let invitationSentInput = prompt("Invitation Sent (Si/No):");
    while (invitationSentInput !== "Si" && invitationSentInput !== "No") {
      invitationSentInput = prompt(
        "Valor inválido. Ingrese 'Si' o 'No' para Invitation Sent:"
      );
    }
    const updatedInvitationSent = invitationSentInput === "Si";
    let updatedPhone = prompt("Nuevo teléfono:");
    while (!updatedPhone || updatedPhone.trim() === "") {
      updatedPhone = prompt("Teléfono inválido. Ingrese un teléfono no vacío:");
    }
    setInvitations(
      invitations.map((inv) =>
        inv.id === id
          ? {
              ...inv,
              name: updatedName,
              guests: updatedGuests,
              table: updatedTable,
              status: updatedStatus,
              invitationSent: updatedInvitationSent,
              phone: updatedPhone,
            }
          : inv
      )
    );
  };

  const deleteInvitation = (id) => {
    setInvitations(invitations.filter((inv) => inv.id !== id));
  };

  const stats = {
    confirmed: invitations
      .filter((inv) => inv.status === "confirmado")
      .reduce((sum, inv) => sum + inv.guests, 0),
    pending: invitations
      .filter((inv) => inv.status === "pendiente")
      .reduce((sum, inv) => sum + inv.guests, 0),
    rejected: invitations
      .filter((inv) => inv.status === "rechazado")
      .reduce((sum, inv) => sum + inv.guests, 0),
  };

  return (
    <div className="App">
      <div className="stats">
        <div className="stat confirmed">{stats.confirmed} Confirmados</div>
        <div className="stat pending">{stats.pending} Pendientes</div>
        <div className="stat total">
          {stats.confirmed + stats.pending} Total
        </div>
        <div className="stat rejected">{stats.rejected} Rechazados</div>
      </div>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Invitados</th>
            <th>Mesa</th>
            <th>Estado</th>
            <th>Operaciones</th>
            <th>Invitación enviada</th>
            <th>Número de teléfono</th>
          </tr>
        </thead>
        <tbody>
          {invitations.map(
            ({ id, name, guests, table, status, invitationSent, phone }) => (
              <tr key={id}>
                <td>{name}</td>
                <td>{guests}</td>
                <td>{table}</td>
                <td>{status}</td>
                <td>
                  <button onClick={() => sendInvitation(phone)}>
                    Enviar invitación
                  </button>
                  <button onClick={() => editInvitation(id)}>Editar</button>
                  <button onClick={() => deleteInvitation(id)}>Borrar</button>
                </td>
                <td>{invitationSent ? "Si" : "No"}</td>
                <td>{phone}</td>
              </tr>
            )
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;
