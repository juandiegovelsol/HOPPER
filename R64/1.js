function generarInformeFinanciero(transacciones) {
  const informe = {};
  const totalGeneral = {
    monto: 0,
  };

  transacciones.forEach((transaccion) => {
    const { fecha, monto, categoria } = transaccion;
    const [dia, mes, anio] = fecha.split("/").map(Number);
    const mesFormateado = `${mes.toString().padStart(2, "0")}/${anio}`;

    // Actualizar el total general
    totalGeneral.monto += monto;

    // Inicializar la estructura del mes si no existe
    if (!informe[mesFormateado]) {
      informe[mesFormateado] = {};
    }

    // Agrupar por categoría dentro del mes
    if (!informe[mesFormateado][categoria]) {
      informe[mesFormateado][categoria] = { monto: 0 };
    }

    // Acumular el monto por categoría
    informe[mesFormateado][categoria].monto += monto;
  });

  // Crear una copia ordenada de los meses
  const mesesOrdenados = Object.keys(informe).sort((a, b) => {
    const [mesA, anioA] = a.split("/").map(Number);
    const [mesB, anioB] = b.split("/").map(Number);

    if (anioA !== anioB) return anioA - anioB;
    return mesA - mesB;
  });

  // Construir el informe final con categorías ordenadas
  const informeFinal = {};
  mesesOrdenados.forEach((mes) => {
    const categoriasOrdenadas = Object.keys(informe[mes]).sort();
    informeFinal[mes] = {};
    categoriasOrdenadas.forEach((categoria) => {
      informeFinal[mes][categoria] = informe[mes][categoria].monto;
    });
  });

  // Añadir el total general
  informeFinal.totalGeneral = totalGeneral.monto;

  return informeFinal;
}

// Ejemplo de uso:
const transacciones = [
  { fecha: "01/01/2023", monto: 150.555555, categoria: "Alimentación'" },
  { fecha: "05/01/2023", monto: 250.0, categoria: "Alimentación" },
  { fecha: "15/01/2023", monto: 200.0, categoria: "Transporte" },
  { fecha: "05/02/2023", monto: 100.0, categoria: "Alimentación" },
  { fecha: "20/02/2023", monto: 300.0, categoria: "Lúdica" },
  { fecha: "10/03/2023", monto: 250.0, categoria: "Alimentación" },
  { fecha: "25/03/2023", monto: 150.0, categoria: "Transporte" },
];

console.log(generarInformeFinanciero(transacciones));
