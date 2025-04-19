// script.js
// Al inicio del archivo
document
  .getElementById("btnAgregar")
  .addEventListener("click", agregarEmpleado);

// Datos Iniciales
const dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"];
const turnosDiarios = ["08:00-12:00", "12:00-16:00", "16:00-20:00"];
let empleados = [];
let horario = {};

// Inicialización
document.addEventListener("DOMContentLoaded", () => {
  inicializarHorario();
  actualizarUI();
});

// ========== FUNCIONES PRINCIPALES ========== //

function inicializarHorario() {
  dias.forEach((dia) => {
    horario[dia] = {};
    turnosDiarios.forEach((turno) => {
      horario[dia][turno] = { empleado: null, requiere: "general" };
    });
  });
}

function renderizarTurnos() {
  const contenedor = document.getElementById("turnos");
  contenedor.innerHTML = "";

  // Cabeceras
  contenedor.appendChild(crearCelda("Turno/Día", true));
  dias.forEach((dia) => contenedor.appendChild(crearCelda(dia, true)));

  // Filas
  turnosDiarios.forEach((turno) => {
    contenedor.appendChild(crearCelda(turno, true));
    dias.forEach((dia) => {
      const celda = crearCelda(
        horario[dia][turno].empleado || "[Asignar]",
        false,
        horario[dia][turno].empleado
      );
      celda.onclick = () => gestionarAsignacion(dia, turno);
      contenedor.appendChild(celda);
    });
  });
}

// ========== GESTIÓN DE EMPLEADOS ========== //

function agregarEmpleado() {
  const nombre = prompt("Nombre completo:");
  const habilidades =
    prompt("Habilidades (separadas por coma):")
      ?.split(",")
      .map((h) => h.trim()) || [];

  if (nombre) {
    empleados.push({
      nombre,
      habilidades,
      horasAsignadas: 0,
      maxHoras: parseInt(document.getElementById("maxHoras").value),
    });
    actualizarUI();
  }
}

function gestionarAsignacion(dia, turno) {
  const empleado = prompt("Nombre del empleado:");
  const habilidadRequerida = prompt("Habilidad requerida para este turno:");

  if (!empleado) return;

  const empleadoObj = empleados.find((e) => e.nombre === empleado);
  const turnoObj = horario[dia][turno];

  // Validación 1: Habilidades
  if (!empleadoObj?.habilidades.includes(habilidadRequerida)) {
    mostrarError(`❌ ${empleado} no tiene la habilidad: ${habilidadRequerida}`);
    return;
  }

  // Validación 2: Horas Máximas
  if (empleadoObj.horasAsignadas + 4 > empleadoObj.maxHoras) {
    mostrarError(
      `⏰ ${empleado} excedería su jornada máxima (${empleadoObj.maxHoras}h)`
    );
    return;
  }

  // Asignación
  turnoObj.empleado = empleado;
  empleadoObj.horasAsignadas += 4; // 4h por turno
  actualizarUI();
}

// ========== AUXILIARES ========== //

function crearCelda(contenido, esCabecera = false, tieneDatos = false) {
  const celda = document.createElement("div");
  celda.className = `celda ${esCabecera ? "cabecera" : ""} ${
    tieneDatos ? "turno-asignado" : ""
  }`;
  celda.textContent = contenido;
  return celda;
}

function actualizarUI() {
  renderizarTurnos();
  actualizarListaEmpleados();
  actualizarEstadisticas();
}

function actualizarListaEmpleados() {
  const lista = document.getElementById("listaEmpleados");
  lista.innerHTML = empleados
    .map(
      (e) => ` 
        <li> 
            <strong>${e.nombre}</strong><br> 
            <em>Habilidades:</em> ${e.habilidades.join(", ")}<br> 
            <em>Horas:</em> ${e.horasAsignadas}/${e.maxHoras}h 
        </li> 
    `
    )
    .join("");
}

function actualizarEstadisticas() {
  const totalHoras = empleados.reduce((acc, e) => acc + e.horasAsignadas, 0);
  const maxHoras = empleados.reduce((acc, e) => acc + e.maxHoras, 0);
  const utilizacion = ((totalHoras / maxHoras) * 100 || 0).toFixed(1);

  document.getElementById("horasAsignadas").textContent = totalHoras;
  document.getElementById("maxHorasUI").textContent =
    document.getElementById("maxHoras").value;
  document.getElementById("utilizacion").textContent = utilizacion;
}

function mostrarError(mensaje) {
  const errores = document.getElementById("errores");
  errores.textContent = mensaje;
  errores.style.display = "block";
  setTimeout(() => (errores.style.display = "none"), 3000);
}
