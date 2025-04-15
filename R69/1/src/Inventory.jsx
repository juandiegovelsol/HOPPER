// src/Inventory.jsx
import React from "react";

const items = [
  {
    id: 1,
    name: "Health Potion",
    description: "Restores health points",
    amount: 10,
    isConsumable: true,
    isEquipable: false,
    isAgrupable: true,
    price: 50,
    icon: "/images/health_potion_icon.png",
  },
  // Añade más items aquí para simular la lista
];

const Inventory = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Inventario</h1>
      <table style={styles.table}>
        <thead>
          <tr>
            <th style={styles.header}>Nombre</th>
            <th style={styles.header}>Descripción</th>
            <th style={styles.header}>Cantidad</th>
            <th style={styles.header}>Precio</th>
            <th style={styles.header}>Ícono</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr key={item.id}>
              <td style={styles.cell}>{item.name}</td>
              <td style={styles.cell}>{item.description}</td>
              <td style={styles.cell}>{item.amount}</td>
              <td style={styles.cell}>{item.price}</td>
              <td style={styles.cell}>
                <img src={item.icon} alt={item.name} style={styles.icon} />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

const styles = {
  container: {
    width: "80%",
    margin: "0 auto",
    backgroundColor: "#2a2a33",
    padding: "20px",
    borderRadius: "10px",
    color: "#fff",
  },
  title: {
    textAlign: "center",
    color: "#f0c041",
  },
  table: {
    width: "100%",
    borderCollapse: "collapse",
    marginTop: "20px",
  },
  header: {
    backgroundColor: "#55555c",
    color: "#fff",
    padding: "10px",
    textAlign: "center",
  },
  cell: {
    padding: "10px",
    textAlign: "center",
    color: "#fff",
  },
  icon: {
    width: "50px",
    height: "50px",
  },
};

export default Inventory;
