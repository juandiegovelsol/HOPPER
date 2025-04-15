import React, { useState } from "react";
import "./App.css";

function App() {
  const [appliances, setAppliances] = useState([]);
  const [applianceName, setApplianceName] = useState("");
  const [applianceQuantity, setApplianceQuantity] = useState("");
  const [applianceConsumption, setApplianceConsumption] = useState("");
  const [applianceHours, setApplianceHours] = useState("");
  const [costPerKWh, setCostPerKWh] = useState("");

  const addAppliance = () => {
    const quantity = parseInt(applianceQuantity, 10);
    const consumption = parseFloat(applianceConsumption);
    const hours = parseFloat(applianceHours);

    if (!applianceName || quantity <= 0 || consumption <= 0 || hours <= 0) {
      return;
    }

    const newAppliance = {
      name: applianceName,
      quantity,
      consumption,
      hours,
    };

    setAppliances([...appliances, newAppliance]);
    setApplianceName("");
    setApplianceQuantity("");
    setApplianceConsumption("");
    setApplianceHours("");
  };

  const totalMonthlyKWh = appliances.reduce((total, appliance) => {
    return (
      total +
      (appliance.quantity * appliance.consumption * appliance.hours * 30) / 1000
    );
  }, 0);

  const calculateCost = (kWh) => {
    return costPerKWh ? parseFloat(costPerKWh) * kWh : 0;
  };

  return (
    <div className="App">
      <h1>Calculadora de Consumo Eléctrico</h1>
      <div className="form">
        <input
          type="text"
          placeholder="Nombre del Electrodoméstico"
          value={applianceName}
          onChange={(e) => setApplianceName(e.target.value)}
        />
        <input
          type="number"
          placeholder="Cantidad"
          value={applianceQuantity}
          onChange={(e) => setApplianceQuantity(e.target.value)}
        />
        <input
          type="number"
          placeholder="Consumo Unitario en Wh"
          value={applianceConsumption}
          onChange={(e) => setApplianceConsumption(e.target.value)}
        />
        <input
          type="number"
          placeholder="Horas al día"
          value={applianceHours}
          onChange={(e) => setApplianceHours(e.target.value)}
        />
        <button onClick={addAppliance}>Agregar</button>
      </div>
      <input
        type="number"
        placeholder="Costo del KWh en CLP"
        value={costPerKWh}
        onChange={(e) => setCostPerKWh(e.target.value)}
      />
      <table>
        <thead>
          <tr>
            <th>Electrodoméstico</th>
            <th>Consumo Mensual (KWh)</th>
            <th>Consumo Mensual (CLP)</th>
          </tr>
        </thead>
        <tbody>
          {appliances.map((appliance, index) => {
            const monthlyKWh =
              (appliance.quantity *
                appliance.consumption *
                appliance.hours *
                30) /
              1000;
            return (
              <tr key={index}>
                <td>{appliance.name}</td>
                <td>{monthlyKWh.toFixed(2)}</td>
                <td>{calculateCost(monthlyKWh).toFixed(2)}</td>
              </tr>
            );
          })}
        </tbody>
        <tfoot>
          <tr>
            <td>Total</td>
            <td>{totalMonthlyKWh.toFixed(2)}</td>
            <td>{calculateCost(totalMonthlyKWh).toFixed(2)}</td>
          </tr>
        </tfoot>
      </table>
    </div>
  );
}

export default App;
