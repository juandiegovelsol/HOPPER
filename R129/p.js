class Cocinero {
  constructor(nombre, salarioMensual, fechaIngreso, fechaEgreso = null) {
    if (!nombre || typeof nombre !== "string")
      throw new Error("Nombre inválido");
    if (typeof salarioMensual !== "number" || salarioMensual <= 0)
      throw new Error("Salario mensual inválido");
    if (!Cocinero.validarFecha(fechaIngreso))
      throw new Error("Fecha de ingreso inválida");
    if (fechaEgreso && !Cocinero.validarFecha(fechaEgreso))
      throw new Error("Fecha de egreso inválida");
    if (fechaEgreso && !Cocinero.compararFechas(fechaIngreso, fechaEgreso))
      throw new Error("Fecha de egreso anterior a la de ingreso");

    this.nombre = nombre;
    this.salarioMensual = salarioMensual;
    this.fechaIngreso = fechaIngreso;
    this.fechaEgreso = fechaEgreso;
  }

  static validarFecha(fecha) {
    const regex = /^([0-2][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{4}$/;
    if (!regex.test(fecha)) return false;
    const [d, m, y] = fecha.split("/").map(Number);
    const date = new Date(y, m - 1, d);
    return (
      date &&
      date.getDate() === d &&
      date.getMonth() === m - 1 &&
      date.getFullYear() === y
    );
  }

  static compararFechas(inicio, fin) {
    const [d1, m1, y1] = inicio.split("/").map(Number);
    const [d2, m2, y2] = fin.split("/").map(Number);
    const f1 = new Date(y1, m1 - 1, d1);
    const f2 = new Date(y2, m2 - 1, d2);
    return f2 >= f1;
  }

  obtenerSalarioFormateado() {
    return new Intl.NumberFormat("es-ES", {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
      style: "currency",
      currency: "EUR",
      useGrouping: true,
    }).format(this.salarioMensual);
  }

  totalCobradoFormateado() {
    return new Intl.NumberFormat("es-ES", {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
      style: "currency",
      currency: "EUR",
      useGrouping: true,
    }).format(this.totalCobrado());
  }

  estaActivo() {
    return this.fechaEgreso === null;
  }

  mesesTrabajados() {
    const [di, mi, yi] = this.fechaIngreso.split("/").map(Number);
    const [df, mf, yf] = this.fechaEgreso
      ? this.fechaEgreso.split("/").map(Number)
      : [
          new Date().getDate(),
          new Date().getMonth() + 1,
          new Date().getFullYear(),
        ];
    console.log(df, mf, yf);
    const inicio = new Date(yi, mi - 1, di);
    const fin = new Date(yf, mf - 1, df);
    let meses =
      (fin.getFullYear() - inicio.getFullYear()) * 12 +
      (fin.getMonth() - inicio.getMonth());
    if (fin.getDate() >= inicio.getDate()) meses++;
    return Math.max(0, meses);
  }

  totalCobrado() {
    return this.salarioMensual * this.mesesTrabajados();
  }

  resumen() {
    return (
      `Nombre: ${this.nombre}\n` +
      `Estado: ${this.estaActivo() ? "Activo" : "Inactivo"}\n` +
      `Ingreso: ${this.fechaIngreso}\n` +
      `Egreso: ${this.fechaEgreso ?? "Actualmente activo"}\n` +
      `Salario mensual: ${this.obtenerSalarioFormateado()}\n` +
      `Meses trabajados: ${this.mesesTrabajados()}\n` +
      `Total cobrado: ${this.totalCobradoFormateado()}\n`
    );
  }
}

const cocineros = [];

function agregarCocinero(
  nombre,
  salarioMensual,
  fechaIngreso,
  fechaEgreso = null
) {
  const nuevo = new Cocinero(nombre, salarioMensual, fechaIngreso, fechaEgreso);
  cocineros.push(nuevo);
  imprimirResumen();
}

function imprimirResumen() {
  const resumen = cocineros
    .map((c) => c.resumen())
    .join("\n-------------------------\n");
  console.log(resumen);
}

agregarCocinero("Luis García", 1350.75, "10/03/2022");
agregarCocinero("María Torres", 1500.0, "05/06/2021", "12/0/2023");
agregarCocinero(1425.5, "10/10/2024");
agregarCocinero("Ana Sánchez", -1600.0, "15/08/2020", "01/01/2021");
