class CLMM {
  constructor(token0, token1) {
    this.token0 = token0;
    this.token1 = token1;
    this.precioActual = 1;
    this.espaciamientoTick = 1;
    this.ticks = {};

    this.proveedores = {};

    this.liquidez = { token0: 0, token1: 0 };
  }

  agregarLiquidez(
    proveedor,
    cantidadToken0,
    cantidadToken1,
    tickInferior,
    tickSuperior
  ) {
    if (tickInferior >= tickSuperior)
      throw new Error("Rango de ticks inválido");
    this.proveedores[proveedor] = this.proveedores[proveedor] || [];
    this.proveedores[proveedor].push({
      tickInferior,
      tickSuperior,
      cantidadToken0,
      cantidadToken1,
    });

    for (let tick = tickInferior; tick <= tickSuperior; tick++) {
      if (!this.ticks[tick]) this.ticks[tick] = { token0: 0, token1: 0 };
      this.ticks[tick].token0 += cantidadToken0;
      this.ticks[tick].token1 += cantidadToken1;
    }
    this.liquidez.token0 += cantidadToken0;
    this.liquidez.token1 += cantidadToken1;
  }

  disminuirLiquidez(proveedor, indicePosicion) {
    const posiciones = this.proveedores[proveedor];
    if (!posiciones || !posiciones[indicePosicion])
      throw new Error("Proveedor o posición inválida");
    const { tickInferior, tickSuperior, cantidadToken0, cantidadToken1 } =
      posiciones[indicePosicion];

    for (let tick = tickInferior; tick <= tickSuperior; tick++) {
      if (!this.ticks[tick]) throw new Error(`No hay liquidez en tick ${tick}`);
      this.ticks[tick].token0 -= cantidadToken0;
      this.ticks[tick].token1 -= cantidadToken1;
    }
    this.liquidez.token0 -= cantidadToken0;
    this.liquidez.token1 -= cantidadToken1;
    posiciones.splice(indicePosicion, 1);
  }

  calcularComision(cantidadEntrada, direccion) {
    const tamanoFondo =
      direccion === "token0->token1"
        ? this.liquidez.token0
        : this.liquidez.token1;
    const utilizacion = cantidadEntrada / (tamanoFondo || 1);
    const comisionBase = 0.003;
    const comisionVariable = Math.min(utilizacion, 1) * 0.01;
    return comisionBase + comisionVariable;
  }

  // Intercambiar tokens con comisión dinámica
  intercambiar(cantidadEntrada, direccion) {
    const pctComision = this.calcularComision(cantidadEntrada, direccion);
    const cantidadDespuesComision = cantidadEntrada * (1 - pctComision);
    let cantidadSalida;

    if (direccion === "token0->token1") {
      cantidadSalida = cantidadDespuesComision * this.precioActual;
      this.liquidez.token0 += cantidadDespuesComision;
      this.liquidez.token1 -= cantidadSalida;
    } else if (direccion === "token1->token0") {
      cantidadSalida = cantidadDespuesComision / this.precioActual;
      this.liquidez.token1 += cantidadDespuesComision;
      this.liquidez.token0 -= cantidadSalida;
    } else {
      throw new Error("Dirección de swap inválida");
    }

    this.precioActual = this.liquidez.token1 / this.liquidez.token0;
    return {
      cantidadEntrada,
      cantidadDespuesComision,
      cantidadSalida,
      pctComision,
      nuevoPrecio: this.precioActual,
    };
  }

  obtenerInfoProveedor(proveedor) {
    return this.proveedores[proveedor] || [];
  }

  obtenerEstadoFondo() {
    return {
      precio: this.precioActual,
      liquidez: this.liquidez,
      ticks: this.ticks,
    };
  }
}

// Ejemplo de uso:
const fondo = new CLMM("Token0", "Token1");

fondo.agregarLiquidez("Alice", 1000, 5000, 1, 5);
fondo.agregarLiquidez("Alice", 500, 2000, 8, 12);

fondo.agregarLiquidez("Bob", 500, 2000, 3, 7);

console.log("Posiciones de Alice:", fondo.obtenerInfoProveedor("Alice"));

const resultadoSwap = fondo.intercambiar(200, "token0->token1");
console.log("Resultado del swap:", resultadoSwap);
