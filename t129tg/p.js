const fs = require("fs");

class InventarioValidator {
  constructor() {
    this.inventario = [];
  }

  cargarInventario(filePath) {
    try {
      const data = fs.readFileSync(filePath, "utf8");
      const inventario = JSON.parse(data);

      if (!Array.isArray(inventario)) {
        throw new Error("El archivo JSON debe contener un arreglo de platos");
      }

      this.inventario = inventario.filter((plato) => this.validarPlato(plato));
      return true;
    } catch (error) {
      console.error(`Error al cargar el inventario: ${error.message}`);
      return false;
    }
  }

  validarPlato(plato) {
    if (!plato || typeof plato !== "object") {
      console.error("Alerta: Plato inválido o no es un objeto");
      return false;
    }

    if (!plato.nombre || typeof plato.nombre !== "string") {
      console.error(
        `Alerta: Nombre inválido o vacío: ${JSON.stringify(plato)}`
      );
      return false;
    }

    if (!plato.categoria || typeof plato.categoria !== "string") {
      console.error(
        `Alerta: Categoría inválida o vacía para el plato ${plato.nombre}`
      );
      return false;
    }

    if (typeof plato.precio !== "number" || plato.precio <= 0) {
      console.error(`Alerta: Precio inválido para el plato ${plato.nombre}`);
      return false;
    }

    if (typeof plato.disponible !== "boolean") {
      console.error(
        `Alerta: Estado de disponibilidad inválido para el plato ${plato.nombre}`
      );
      return false;
    }

    if (!Array.isArray(plato.ingredientes) || plato.ingredientes.length === 0) {
      console.error(
        `Alerta: Lista de ingredientes inválida para el plato ${plato.nombre}`
      );
      return false;
    }

    return true;
  }

  getResumenInventario() {
    const total = this.inventario.length;
    const disponibles = this.inventario.filter(
      (plato) => plato.disponible
    ).length;
    const noDisponibles = total - disponibles;

    // Agrupar por categoría
    const categorias = {};
    this.inventario.forEach((plato) => {
      if (!categorias[plato.categoria]) {
        categorias[plato.categoria] = {
          total: 0,
          disponibles: 0,
          precioPromedio: 0,
          platos: [],
        };
      }

      categorias[plato.categoria].total++;
      if (plato.disponible) {
        categorias[plato.categoria].disponibles++;
      }
      categorias[plato.categoria].platos.push(plato);
    });

    // Calcular precio promedio por categoría
    for (const cat in categorias) {
      const totalPrecio = categorias[cat].platos.reduce(
        (sum, plato) => sum + plato.precio,
        0
      );
      categorias[cat].precioPromedio = totalPrecio / categorias[cat].total;
    }

    return {
      total,
      disponibles,
      noDisponibles,
      categorias,
    };
  }

  imprimirResumen() {
    const resumen = this.getResumenInventario();
    console.log("\n--- RESUMEN DE INVENTARIO ---");
    console.log(`Total de platos: ${resumen.total}`);
    console.log(`Platos disponibles: ${resumen.disponibles}`);
    console.log(`Platos no disponibles: ${resumen.noDisponibles}`);

    console.log("\n--- DESGLOSE POR CATEGORÍA ---");
    for (const categoria in resumen.categorias) {
      const cat = resumen.categorias[categoria];
      console.log(`\n${categoria}:`);
      console.log(`  Total: ${cat.total} platos`);
      console.log(`  Disponibles: ${cat.disponibles} platos`);
      console.log(`  Precio promedio: $${cat.precioPromedio.toFixed(2)}`);
    }
  }

  /* getPlatosMasCaros(limite = 3) {
    return [...this.inventario]
      .sort((a, b) => b.precio - a.precio)
      .slice(0, limite);
  }

  getPlatosConMasIngredientes(limite = 3) {
    return [...this.inventario]
      .sort((a, b) => b.ingredientes.length - a.ingredientes.length)
      .slice(0, limite);
  } */
}

const validator = new InventarioValidator();
const cargado = validator.cargarInventario("inventario.json");

if (cargado) {
  validator.imprimirResumen();

  /* console.log("\n--- PLATOS MÁS CAROS ---");
    const platosMasCaros = validator.getPlatosMasCaros();
    platosMasCaros.forEach((plato) => {
      console.log(`${plato.nombre}: $${plato.precio.toFixed(2)}`);
    });

    console.log("\n--- PLATOS CON MÁS INGREDIENTES ---");
    const platosComplejos = validator.getPlatosConMasIngredientes();
    platosComplejos.forEach((plato) => {
      console.log(`${plato.nombre}: ${plato.ingredientes.length} ingredientes`);
    }); */
}

module.exports = InventarioValidator;
