const readline = require("readline");

class Factura {
  constructor(servicio, monto, vencimiento) {
    this.servicio = servicio;
    this.monto = monto;
    this.vencimiento = new Date(vencimiento);
  }
}

let facturas = [];

function validarFecha(fecha) {
  const regex = /^(0[1-9]|1[0-2])\/([0-2][0-9]|3[01])\/\d{4}$/;
  return regex.test(fecha);
}

function agregarFactura(servicio, monto, vencimiento) {
  if (!servicio || isNaN(monto)) {
    console.log("Datos inválidos.");
    return false;
  }

  if (!validarFecha(vencimiento)) {
    console.log("Formato de fecha incorrecto. Debe ser MM/DD/YYYY.");
    return false;
  }

  const [mes, dia, año] = vencimiento.split("/");
  const fechaFormateada = new Date(año, mes - 1, dia);

  facturas.push(new Factura(servicio, monto, fechaFormateada));
  return true;
}

function mostrarFacturas() {
  facturas.sort((a, b) => a.vencimiento - b.vencimiento);

  let total = 0;
  console.log("\nFacturas:");
  facturas.forEach((f) => {
    console.log(
      `${f.servicio} - $${f.monto.toFixed(
        2
      )} - Vence: ${f.vencimiento.toLocaleDateString()}`
    );
    total += f.monto;
  });
  console.log(`Total: $${total.toFixed(2)}\n`);
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

/* agregarFactura("Luz", 3500, "05/10/2025");
agregarFactura("Agua", 2400, "04/28/2025");
agregarFactura("Internet", 5200, "05/05/2025");
agregarFactura("Gas", 3000, "04/25/2025");

mostrarFacturas(); */

agregarFactura("Luz", 500, "05/10/2024");
agregarFactura("Agua", 200, "04/28/2025");
agregarFactura("Internet", 5200, "05/26/2025");
agregarFactura("Gas", 300, "02/25/2025");

mostrarFacturas();
