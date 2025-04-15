const atracciones = [
  {
    ID: "001",
    Atraccion: "Torre Eiffel",
    VisitantesAdicionales: 30000,
    VisitantesIniciales: 120000,
    TarifaEntradaCLP: 12000,
  },
  {
    ID: "002",
    Atraccion: "Museo del Louvre",
    VisitantesAdicionales: 25000,
    VisitantesIniciales: 180000,
    TarifaEntradaCLP: 10500,
  },
  {
    ID: "003",
    Atraccion: "Catedral de Notre Dame",
    VisitantesAdicionales: 12000,
    VisitantesIniciales: 95000,
    TarifaEntradaCLP: 8000,
  },
  {
    ID: "004",
    Atraccion: "Arco de Triunfo",
    VisitantesAdicionales: 10000,
    VisitantesIniciales: 85000,
    TarifaEntradaCLP: 7500,
  },
  {
    ID: "005",
    Atraccion: "Palacio de Versalles",
    VisitantesAdicionales: 35000,
    VisitantesIniciales: 140000,
    TarifaEntradaCLP: 11000,
  },
  {
    ID: "006",
    Atraccion: "Montmartre",
    VisitantesAdicionales: 9000,
    VisitantesIniciales: 75000,
    TarifaEntradaCLP: 5000,
  },
  {
    ID: "001",
    Atracción: "Torre Eiffel",
    VisitantesAdicionales: 28000,
    VisitantesIniciales: 115000,
    TarifaEntradaCLP: 12000,
  },
  {
    ID: "002",
    Atracción: "Museo del Louvre",
    VisitantesAdicionales: 27000,
    VisitantesIniciales: 175000,
    TarifaEntradaCLP: 10500,
  },
  {
    ID: "003",
    Atracción: "Catedral de Notre Dame",
    VisitantesAdicionales: 11000,
    VisitantesIniciales: 94000,
    TarifaEntradaCLP: 8000,
  },
  {
    ID: "004",
    Atracción: "Arco de Triunfo",
    VisitantesAdicionales: 12000,
    VisitantesIniciales: 86000,
    TarifaEntradaCLP: 7500,
  },
  {
    ID: "005",
    Atracción: "Palacio de Versalles",
    VisitantesAdicionales: 37000,
    VisitantesIniciales: 138000,
    TarifaEntradaCLP: 11000,
  },
  {
    ID: "006",
    Atracción: "Montmartre",
    VisitantesAdicionales: 9500,
    VisitantesIniciales: 73000,
    TarifaEntradaCLP: 5000,
  },
  {
    ID: "001",
    Atracción: "Torre Eiffel",
    VisitantesAdicionales: 31000,
    VisitantesIniciales: 122000,
    TarifaEntradaCLP: 12000,
  },
  {
    ID: "002",
    Atracción: "Museo del Louvre",
    VisitantesAdicionales: 26000,
    VisitantesIniciales: 185000,
    TarifaEntradaCLP: 10500,
  },
  {
    ID: "003",
    Atracción: "Catedral de Notre Dame",
    VisitantesAdicionales: 11500,
    VisitantesIniciales: 93000,
    TarifaEntradaCLP: 8000,
  },
];

const calcularVisitantesTotales = (atracciones) => {
  const visitantesPorAtraccion = {};

  atracciones.forEach((atraccion) => {
    if (!visitantesPorAtraccion[atraccion.ID]) {
      visitantesPorAtraccion[atraccion.ID] = {
        Atraccion: atraccion.Atraccion,
        TotalVisitantes: 0,
        IngresosGenerados: 0,
      };
    }

    visitantesPorAtraccion[atraccion.ID].TotalVisitantes +=
      atraccion.VisitantesIniciales + atraccion.VisitantesAdicionales;
  });
  return visitantesPorAtraccion;
};

const calcularIngresosGenerados = (visitantesPorAtraccion) => {
  Object.keys(visitantesPorAtraccion).forEach((idAtraccion) => {
    visitantesPorAtraccion[idAtraccion].IngresosGenerados =
      visitantesPorAtraccion[idAtraccion].TotalVisitantes *
      visitantesPorAtraccion[idAtraccion].TarifaEntradaCLP;
  });
  console.log(visitantesPorAtraccion);
  return visitantesPorAtraccion;
};

const rankingAtracciones = (visitantesPorAtraccion) => {
  return Object.values(visitantesPorAtraccion).sort(
    (a, b) => b.IngresosGenerados - a.IngresosGenerados
  );
};

const mostrarResultados = (rankingAtracciones) => {
  console.log(
    "ID\tAtracción\tVisitantes Iniciales\tVisitantes Adicionales\tTarifa de Entrada (CLP)\tTotal Visitantes\tIngresos Generados"
  );
  rankingAtracciones.forEach((atraccion) => {
    console.log(
      `${atraccion.ID}\t${atraccion.Atraccion}\t\t${atraccion.VisitantesIniciales}\t\t${atraccion.VisitantesAdicionales}\t\t${atraccion.TarifaEntradaCLP}\t\t${atraccion.TotalVisitantes}\t\t${atraccion.IngresosGenerados}`
    );
  });
};

// Calcular el total de visitantes por atracción
const visitantesPorAtraccion = calcularVisitantesTotales(atracciones);

// Calcular los ingresos generados por cada atracción
const ingresosPorAtraccion = calcularIngresosGenerados(visitantesPorAtraccion);

// Ordenar las atracciones por rentabilidad
const ranking = rankingAtracciones(ingresosPorAtraccion);
console.log(ranking);
// Mostrar los resultados
mostrarResultados(ranking);
