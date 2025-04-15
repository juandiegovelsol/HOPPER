// Datos de entrada
const atracciones = [
  {
    ID: "001",
    Atracción: "Torre Eiffel",
    VisitantesAdicionales: 30000,
    VisitantesIniciales: 120000,
    TarifaEntrada: 12000,
  },
  {
    ID: "002",
    Atracción: "Museo del Louvre",
    VisitantesAdicionales: 25000,
    VisitantesIniciales: 180000,
    TarifaEntrada: 10500,
  },
  {
    ID: "003",
    Atracción: "Catedral de Notre Dame",
    VisitantesAdicionales: 12000,
    VisitantesIniciales: 95000,
    TarifaEntrada: 8000,
  },
  {
    ID: "004",
    Atracción: "Arco de Triunfo",
    VisitantesAdicionales: 10000,
    VisitantesIniciales: 85000,
    TarifaEntrada: 7500,
  },
  {
    ID: "005",
    Atracción: "Palacio de Versalles",
    VisitantesAdicionales: 35000,
    VisitantesIniciales: 140000,
    TarifaEntrada: 11000,
  },
  {
    ID: "006",
    Atracción: "Montmartre",
    VisitantesAdicionales: 9000,
    VisitantesIniciales: 75000,
    TarifaEntrada: 5000,
  },
  {
    ID: "001",
    Atracción: "Torre Eiffel",
    VisitantesAdicionales: 28000,
    VisitantesIniciales: 115000,
    TarifaEntrada: 12000,
  },
  {
    ID: "002",
    Atracción: "Museo del Louvre",
    VisitantesAdicionales: 27000,
    VisitantesIniciales: 175000,
    TarifaEntrada: 10500,
  },
  {
    ID: "003",
    Atracción: "Catedral de Notre Dame",
    VisitantesAdicionales: 11000,
    VisitantesIniciales: 94000,
    TarifaEntrada: 8000,
  },
  {
    ID: "004",
    Atracción: "Arco de Triunfo",
    VisitantesAdicionales: 12000,
    VisitantesIniciales: 86000,
    TarifaEntrada: 7500,
  },
  {
    ID: "005",
    Atracción: "Palacio de Versalles",
    VisitantesAdicionales: 37000,
    VisitantesIniciales: 138000,
    TarifaEntrada: 11000,
  },
  {
    ID: "006",
    Atracción: "Montmartre",
    VisitantesAdicionales: 9500,
    VisitantesIniciales: 73000,
    TarifaEntrada: 5000,
  },
  {
    ID: "001",
    Atracción: "Torre Eiffel",
    VisitantesAdicionales: 31000,
    VisitantesIniciales: 122000,
    TarifaEntrada: 12000,
  },
  {
    ID: "002",
    Atracción: "Museo del Louvre",
    VisitantesAdicionales: 26000,
    VisitantesIniciales: 185000,
    TarifaEntrada: 10500,
  },
  {
    ID: "003",
    Atracción: "Catedral de Notre Dame",
    VisitantesAdicionales: 11500,
    VisitantesIniciales: 93000,
    TarifaEntrada: 8000,
  },
];

// 1. Calcular total de visitantes por atracción
function calcularTotalVisitantes(atracciones) {
  const mapaVisitantes = {};

  atracciones.forEach(
    ({ ID, Atracción, VisitantesIniciales, VisitantesAdicionales }) => {
      if (!mapaVisitantes[ID]) {
        mapaVisitantes[ID] = { Atracción, TotalVisitantes: 0 };
      }
      mapaVisitantes[ID].TotalVisitantes +=
        VisitantesIniciales + VisitantesAdicionales;
    }
  );

  return mapaVisitantes;
}

// 2. Calcular ingresos generados por atracción
function calcularIngresos(mapaVisitantes, atracciones) {
  const resultado = [];

  for (const key in mapaVisitantes) {
    const { Atracción, TotalVisitantes } = mapaVisitantes[key];
    const { TarifaEntrada } = atracciones.find(
      (atraccion) => atraccion.ID === key
    );

    const IngresosGenerados = TotalVisitantes * TarifaEntrada;
    resultado.push({
      ID: key,
      Atracción,
      TotalVisitantes,
      IngresosGenerados,
      TarifaEntrada,
    });
  }

  return resultado;
}

// 3. Ordenar por rentabilidad
function ordenarPorRentabilidad(atraccionesConIngresos) {
  return atraccionesConIngresos.sort(
    (a, b) => b.IngresosGenerados - a.IngresosGenerados
  );
}

// Uso de las funciones
const mapaVisitantes = calcularTotalVisitantes(atracciones);
const atraccionesConIngresos = calcularIngresos(mapaVisitantes, atracciones);
const atraccionesOrdenadas = ordenarPorRentabilidad(atraccionesConIngresos);

// Mostrar resultados
console.table(atraccionesOrdenadas, [
  "ID",
  "Atracción",
  "TarifaEntrada",
  "TotalVisitantes",
  "IngresosGenerados",
]);
