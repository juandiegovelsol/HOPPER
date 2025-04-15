import React, { useState } from "react";

function App() {
  const [appliances, setAppliances] = useState([]);
  const [name, setName] = useState("");
  const [quantity, setQuantity] = useState("");
  const [consumption, setConsumption] = useState("");
  const [hours, setHours] = useState("");
  const [costPerKWh, setCostPerKWh] = useState("");

  const handleAddAppliance = () => {
    if (
      name &&
      quantity > 0 &&
      Number.isInteger(+quantity) &&
      consumption > 0 &&
      hours > 0
    ) {
      const newAppliance = {
        name,
        quantity: parseInt(quantity),
        consumption: parseFloat(consumption),
        hours: parseFloat(hours),
      };
      setAppliances([...appliances, newAppliance]);
      setName("");
      setQuantity("");
      setConsumption("");
      setHours("");
    }
  };

  const totalConsumptionKWh = appliances.reduce(
    (acc, appliance) =>
      acc +
      (appliance.quantity * appliance.consumption * appliance.hours * 30) /
        1000,
    0
  );
  const totalCost = totalConsumptionKWh * parseFloat(costPerKWh);

  return (
    <div className="App">
      <h1>Calculadora de Consumo Eléctrico</h1>
      <div className="form">
        <input
          type="text"
          placeholder="Nombre del electrodoméstico"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="number"
          placeholder="Cantidad"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
        />
        <input
          type="number"
          step="0.1"
          placeholder="Consumo en Wh"
          value={consumption}
          onChange={(e) => setConsumption(e.target.value)}
        />
        <input
          type="number"
          step="0.1"
          placeholder="Horas de uso diario"
          value={hours}
          onChange={(e) => setHours(e.target.value)}
        />
        <button onClick={handleAddAppliance}>Agregar</button>
      </div>
      <div className="cost-input">
        <input
          type="number"
          step="0.01"
          placeholder="Costo del KWh en CLP"
          value={costPerKWh}
          onChange={(e) => {
            const value = parseFloat(e.target.value);
            setCostPerKWh(value > 0 ? value : "");
          }}
        />
      </div>
      <table>
        <thead>
          <tr>
            <th>Electrodoméstico</th>
            <th>Cantidad</th>
            <th>Consumo Mensual KWh</th>
            <th>Costo Mensual CLP</th>
          </tr>
        </thead>
        <tbody>
          {appliances.map((appliance, index) => {
            const monthlyConsumptionKWh =
              (appliance.quantity *
                appliance.consumption *
                appliance.hours *
                30) /
              1000;
            const monthlyCost = monthlyConsumptionKWh * parseFloat(costPerKWh);
            return (
              <tr key={index}>
                <td>{appliance.name}</td>
                <td>{appliance.quantity}</td>
                <td>{monthlyConsumptionKWh.toFixed(2)}</td>
                <td>{monthlyCost.toFixed(2)}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <div className="totals">
        <p>Total Consumo Mensual: {totalConsumptionKWh.toFixed(2)} KWh</p>
        <p>
          Total Costo Mensual: {totalCost ? totalCost.toFixed(2) : "0.00"} CLP
        </p>
      </div>
    </div>
  );
}

export default App;
