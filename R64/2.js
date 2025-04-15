function generarInformeFinanciero(transacciones) {
  const meses = {};
  let totalGeneral = 0;

  transacciones.forEach((transaccion) => {
    const { fecha, monto, categoria } = transaccion;
    const [dia, mes, anio] = fecha.split("/").map(Number);
    const mesFormateado = `${mes.toString().padStart(2, "0")}/${anio}`;

    // Actualizar total de la transacción
    totalGeneral += monto;

    // Inicializar el mes si no existe
    if (!meses[mesFormateado]) {
      meses[mesFormateado] = {};
    }

    // Inicializar la categoría si no existe en el mes
    if (!meses[mesFormateado][categoria]) {
      meses[mesFormateado][categoria] = 0;
    }

    // Acumular el monto en la categoría correspondiente del mes
    meses[mesFormateado][categoria] += monto;
  });

  // Ordenar los meses y categorías
  const mesesOrdenados = Object.keys(meses).sort();
  const informe = {};

  mesesOrdenados.forEach((mes) => {
    informe[mes] = Object.keys(meses[mes])
      .sort()
      .reduce((acc, categoria) => {
        acc[categoria] = meses[mes][categoria];
        return acc;
      }, {});
  });

  // Incluir el total general
  informe.totalGeneral = totalGeneral;

  return informe;
}

// Ejemplo de uso:
const transacciones = [
  { fecha: "15/03/2023", monto: 150.5055, categoria: "Alimentación" },
  { fecha: "15/03/2023", monto: 150.5056, categoria: "Alimentación" },
  { fecha: "20/03/2023", monto: 50.0, categoria: "Transporte" },
  { fecha: "10/02/2023", monto: 200.0, categoria: "Alquiler" },
  { fecha: "05/04/2023", monto: 100.0, categoria: "Ocio" },
  { fecha: "12/04/2023", monto: 120.0, categoria: "Alimentación" },
];

console.log(generarInformeFinanciero(transacciones));
