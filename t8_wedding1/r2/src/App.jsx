import React, { useState } from "react";
import "./App.css";

function App() {
  const [invitations, setInvitations] = useState([
    {
      id: 1,
      name: "Juan Pérez",
      guests: 2,
      table: 1,
      status: "pendiente",
      phone: "123-456-789",
      invitationSent: false,
    },
    {
      id: 2,
      name: "Ana López",
      guests: 1,
      table: 2,
      status: "confirmado",
      phone: "987-654-321",
      invitationSent: true,
    },
    {
      id: 3,
      name: "Carlos García",
      guests: 3,
      table: 1,
      status: "rechazado",
      phone: "555-555-555",
      invitationSent: false,
    },
  ]);

  const handleSendInvitation = (id) => {
    console.log(`Invitación enviada a invitado con ID ${id}`);
    setInvitations(
      invitations.map((inv) =>
        inv.id === id ? { ...inv, invitationSent: true } : inv
      )
    );
  };

  const handleEditInvitation = (id, newData) => {
    setInvitations(
      invitations.map((inv) =>
        inv.id === id ? { ...newData, id: inv.id } : inv
      )
    );
  };

  const handleDeleteInvitation = (id) => {
    setInvitations(invitations.filter((inv) => inv.id !== id));
  };

  const countGuests = () => {
    const confirmed = invitations.filter(
      (inv) => inv.status === "confirmado"
    ).length;
    const pending = invitations.filter(
      (inv) => inv.status === "pendiente"
    ).length;
    const rejected = invitations.filter(
      (inv) => inv.status === "rechazado"
    ).length;
    const total = invitations.length - rejected;

    return { confirmed, pending, total, rejected };
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="count-box" style={{ backgroundColor: "green" }}>
          <span>Confirmados</span>
          <br />
          <span>{countGuests().confirmed}</span>
        </div>
        <div className="count-box" style={{ backgroundColor: "yellow" }}>
          <span>Pendientes</span>
          <br />
          <span>{countGuests().pending}</span>
        </div>
        <div className="count-box" style={{ backgroundColor: "blue" }}>
          <span>Total</span>
          <br />
          <span>{countGuests().total}</span>
        </div>
        <div className="count-box" style={{ backgroundColor: "red" }}>
          <span>Rechazados</span>
          <br />
          <span>{countGuests().rejected}</span>
        </div>
      </header>
      <main>
        <table>
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Invitados</th>
              <th>Mesa</th>
              <th>Estado</th>
              <th>Operaciones</th>
              <th>Invitación enviada</th>
              <th>Teléfono</th>
            </tr>
          </thead>
          <tbody>
            {invitations.map((inv) => (
              <tr key={inv.id}>
                <td>{inv.name}</td>
                <td>{inv.guests}</td>
                <td>{inv.table}</td>
                <td>{inv.status}</td>
                <td>
                  <button onClick={() => handleSendInvitation(inv.id)}>
                    Enviar invitación
                  </button>
                  <button
                    onClick={() =>
                      handleEditInvitation(inv.id, {
                        name: "Nuevo Nombre",
                        guests: 4,
                        table: 5,
                        status: "pendiente",
                        phone: "111-111-111",
                        invitationSent: false,
                      })
                    }
                  >
                    Editar
                  </button>
                  <button onClick={() => handleDeleteInvitation(inv.id)}>
                    Borrar
                  </button>
                </td>
                <td>{inv.invitationSent ? "Sí" : "No"}</td>
                <td>{inv.phone}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </main>
    </div>
  );
}

export default App;
