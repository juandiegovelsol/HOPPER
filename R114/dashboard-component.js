// dashboard-component.js - Web Component
class DashboardComponent extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this.price = "0.00 €";
    this.timestamp = "";

    this.render();
  }

  render() {
    this.shadowRoot.innerHTML = `
            <style>
                :host {
                    display: block;
                    font-family: Arial, sans-serif;
                    border: 1px solid #ccc;
                    padding: 16px;
                }
            </style>
            <div>
                <h2>Dashboard de Precios</h2>
                <p>Precio actual: <span id="price">${this.price}</span></p>
                <p>Última actualización: <span id="timestamp">${this.timestamp}</span></p>
            </div>
        `;
  }

  updateData(data) {
    // Manejo de errores
    if (!data || typeof data.formattedPrice !== "string") {
      console.error("Datos incorrectos:", data);
      return;
    }

    this.price = data.formattedPrice;
    this.timestamp = data.timestamp;

    // Actualizar la visualización
    this.render();
  }
}

customElements.define("dashboard-component", DashboardComponent);
