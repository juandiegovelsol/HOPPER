import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [invitations, setInvitations] = useState([]);
  const [editingInvitationId, setEditingInvitationId] = useState(null);
  const [editedInvitation, setEditedInvitation] = useState({});
  const [newInvitation, setNewInvitation] = useState({
    name: "",
    guests: "",
    table: "",
    phone: "",
  });
  const [filters, setFilters] = useState({
    name: "",
    table: "",
    status: "",
    invitationSent: "",
  });
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    setInvitations([
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
  }, []);

  const sendInvitation = (phone) => {
    setInvitations((prev) =>
      prev.map((inv) =>
        inv.phone === phone ? { ...inv, invitationSent: true } : inv
      )
    );
  };

  const deleteInvitation = (id) => {
    setInvitations((prev) => prev.filter((inv) => inv.id !== id));
  };

  const handleEditClick = (invitation) => {
    setEditingInvitationId(invitation.id);
    setEditedInvitation({
      ...invitation,
      invitationSent: invitation.invitationSent ? "Si" : "No",
    });
  };

  const handleChange = (field, value) => {
    setEditedInvitation((prev) => ({ ...prev, [field]: value }));
  };

  const handleSave = (id) => {
    const validStatuses = ["confirmado", "pendiente", "rechazado"];
    if (
      !editedInvitation.name.trim() ||
      isNaN(parseInt(editedInvitation.guests, 10)) ||
      parseInt(editedInvitation.guests, 10) <= 0 ||
      !editedInvitation.table.trim() ||
      !validStatuses.includes(editedInvitation.status) ||
      !editedInvitation.phone.trim() ||
      (editedInvitation.invitationSent !== "Si" &&
        editedInvitation.invitationSent !== "No")
    ) {
      return;
    }
    setInvitations((prev) =>
      prev.map((inv) =>
        inv.id === id
          ? {
              ...editedInvitation,
              guests: parseInt(editedInvitation.guests, 10),
              invitationSent: editedInvitation.invitationSent === "Si",
            }
          : inv
      )
    );
    setEditingInvitationId(null);
    setEditedInvitation({});
  };

  const handleNewChange = (field, value) => {
    setNewInvitation((prev) => ({ ...prev, [field]: value }));
  };

  const addNewInvitation = () => {
    if (
      !newInvitation.name.trim() ||
      isNaN(parseInt(newInvitation.guests, 10)) ||
      parseInt(newInvitation.guests, 10) <= 0
    ) {
      return;
    }
    setInvitations((prev) => [
      ...prev,
      {
        ...newInvitation,
        id: prev.length + 1,
        guests: parseInt(newInvitation.guests, 10),
        status: "pendiente",
        invitationSent: false,
        table: newInvitation.table || "",
        phone: newInvitation.phone || "",
      },
    ]);
    setNewInvitation({ name: "", guests: "", table: "", phone: "" });
    setShowModal(false);
  };

  const handleFilterChange = (field, value) => {
    setFilters((prev) => ({ ...prev, [field]: value }));
  };

  const resetFilters = () => {
    setFilters({ name: "", table: "", status: "", invitationSent: "" });
  };

  const filteredInvitations = invitations
    .filter((inv) =>
      inv.name.toLowerCase().includes(filters.name.toLowerCase())
    )
    .filter((inv) => (filters.table ? inv.table === filters.table : true))
    .filter((inv) => (filters.status ? inv.status === filters.status : true))
    .filter((inv) =>
      filters.invitationSent
        ? inv.invitationSent === (filters.invitationSent === "Si")
        : true
    );

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

  const openModal = () => {
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
    setNewInvitation({ name: "", guests: "", table: "", phone: "" });
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

      <button className="add-button" onClick={openModal}>
        Agregar Invitado
      </button>

      {showModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Agregar Nuevo Invitado</h3>
            <div className="form-group">
              <label>Nombre*</label>
              <input
                type="text"
                placeholder="Nombre"
                value={newInvitation.name}
                onChange={(e) => handleNewChange("name", e.target.value)}
              />
            </div>
            <div className="form-group">
              <label>Invitados*</label>
              <input
                type="number"
                min="1"
                placeholder="Invitados"
                value={newInvitation.guests}
                onChange={(e) => handleNewChange("guests", e.target.value)}
              />
            </div>
            <div className="form-group">
              <label>Mesa</label>
              <input
                type="text"
                placeholder="Mesa"
                value={newInvitation.table}
                onChange={(e) => handleNewChange("table", e.target.value)}
              />
            </div>
            <div className="form-group">
              <label>Teléfono</label>
              <input
                type="text"
                placeholder="Teléfono"
                value={newInvitation.phone}
                onChange={(e) => handleNewChange("phone", e.target.value)}
              />
            </div>
            <div className="modal-actions">
              <button onClick={addNewInvitation}>Agregar</button>
              <button className="cancel-button" onClick={closeModal}>
                Cancelar
              </button>
            </div>
          </div>
        </div>
      )}

      <button onClick={resetFilters}>Restablecer Filtros</button>

      <table>
        <thead>
          <tr>
            <th>
              Nombre
              <br />
              <input
                type="text"
                placeholder="Buscar por nombre"
                value={filters.name}
                onChange={(e) => handleFilterChange("name", e.target.value)}
              />
            </th>
            <th>Invitados</th>
            <th>
              Mesa
              <br />
              <select
                value={filters.table}
                onChange={(e) => handleFilterChange("table", e.target.value)}
              >
                <option value="">Todas las mesas</option>
                {Array.from(new Set(invitations.map((inv) => inv.table)))
                  .filter((table) => table)
                  .sort()
                  .map((table) => (
                    <option key={table} value={table}>
                      {table}
                    </option>
                  ))}
              </select>
            </th>
            <th>
              Estado
              <br />
              <select
                value={filters.status}
                onChange={(e) => handleFilterChange("status", e.target.value)}
              >
                <option value="">Todos los estados</option>
                <option value="confirmado">Confirmado</option>
                <option value="pendiente">Pendiente</option>
                <option value="rechazado">Rechazado</option>
              </select>
            </th>
            <th>Operaciones</th>
            <th>
              Invitación enviada
              <br />
              <select
                value={filters.invitationSent}
                onChange={(e) =>
                  handleFilterChange("invitationSent", e.target.value)
                }
              >
                <option value="">Invitaciones Enviadas</option>
                <option value="Si">Si</option>
                <option value="No">No</option>
              </select>
            </th>
            <th>Número de teléfono</th>
          </tr>
        </thead>
        <tbody>
          {filteredInvitations.map(
            ({ id, name, guests, table, status, invitationSent, phone }) => (
              <tr key={id}>
                <td>
                  {editingInvitationId === id ? (
                    <input
                      type="text"
                      value={editedInvitation.name}
                      onChange={(e) => handleChange("name", e.target.value)}
                    />
                  ) : (
                    name
                  )}
                </td>
                <td>
                  {editingInvitationId === id ? (
                    <input
                      type="number"
                      min="1"
                      value={editedInvitation.guests}
                      onChange={(e) => handleChange("guests", e.target.value)}
                    />
                  ) : (
                    guests
                  )}
                </td>
                <td>
                  {editingInvitationId === id ? (
                    <input
                      type="text"
                      value={editedInvitation.table}
                      onChange={(e) => handleChange("table", e.target.value)}
                    />
                  ) : (
                    table
                  )}
                </td>
                <td>
                  {editingInvitationId === id ? (
                    <select
                      value={editedInvitation.status}
                      onChange={(e) => handleChange("status", e.target.value)}
                    >
                      <option value="confirmado">Confirmado</option>
                      <option value="pendiente">Pendiente</option>
                      <option value="rechazado">Rechazado</option>
                    </select>
                  ) : (
                    status
                  )}
                </td>
                <td>
                  {editingInvitationId === id ? (
                    <button onClick={() => handleSave(id)}>Guardar</button>
                  ) : (
                    <button
                      onClick={() =>
                        handleEditClick({
                          id,
                          name,
                          guests,
                          table,
                          status,
                          invitationSent,
                          phone,
                        })
                      }
                    >
                      Editar
                    </button>
                  )}
                  {editingInvitationId !== id && (
                    <>
                      <button onClick={() => sendInvitation(phone)}>
                        Enviar invitación
                      </button>
                      <button onClick={() => deleteInvitation(id)}>
                        Borrar
                      </button>
                    </>
                  )}
                </td>
                <td>
                  {editingInvitationId === id ? (
                    <select
                      value={editedInvitation.invitationSent}
                      onChange={(e) =>
                        handleChange("invitationSent", e.target.value)
                      }
                    >
                      <option value="Si">Si</option>
                      <option value="No">No</option>
                    </select>
                  ) : invitationSent ? (
                    "Si"
                  ) : (
                    "No"
                  )}
                </td>
                <td>
                  {editingInvitationId === id ? (
                    <input
                      type="text"
                      value={editedInvitation.phone}
                      onChange={(e) => handleChange("phone", e.target.value)}
                    />
                  ) : (
                    phone
                  )}
                </td>
              </tr>
            )
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;
