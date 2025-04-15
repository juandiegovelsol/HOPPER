import React from "react";
import styles from "./Inventory.module.css";

// Ejemplo de items en el inventario, simulando la respuesta de la API
const items = [
  {
    id: 1,
    name: "Health Potion",
    description: "Restores health points",
    ammount: 10,
    isConsumable: true,
    isEquipable: false,
    isAgrupable: true,
    price: 50,
    icon: "health_potion_icon.png",
  },
  // Añade más items como ejemplo...
];

function Inventory() {
  return (
    <div className={styles.inventoryContainer}>
      <h1>Inventario del Jugador</h1>
      <table className={styles.inventoryTable}>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Cantidad</th>
            <th>Precio</th>
            <th>Icon</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr key={item.id}>
              <td>{item.name}</td>
              <td>{item.description}</td>
              <td>{item.ammount}</td>
              <td>{item.price}</td>
              <td>
                <img
                  src={`/images/${item.icon}`}
                  alt={`${item.name}-icon`}
                  className={styles.icon}
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Inventory;
