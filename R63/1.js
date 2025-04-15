function gestionarTareas(accion, tarea, identificador) {
  // Propiedades iniciales de la lista de tareas
  const listaTareas = [];

  // Función para añadir una nueva tarea
  function añadirTarea(tarea) {
    listaTareas.push(tarea);
    console.log("Lista", listaTareas);
    return listaTareas;
  }

  // Función para completar una tarea existente
  function completarTarea(identificador) {
    const indiceTarea = listaTareas.findIndex(
      (tarea) => tarea.identificador === identificador
    );
    if (indiceTarea !== -1) {
      listaTareas[indiceTarea].estáCompletada = true;
    } else {
      console.error(
        `Error: No se encontró una tarea con el identificador ${identificador}`
      );
    }
    return listaTareas;
  }

  // Función para eliminar una tarea existente
  function eliminarTarea(identificador) {
    const indiceTarea = listaTareas.findIndex(
      (tarea) => tarea.identificador === identificador
    );
    if (indiceTarea !== -1) {
      listaTareas.splice(indiceTarea, 1);
    } else {
      console.error(
        `Error: No se encontró una tarea con el identificador ${identificador}`
      );
    }
    return listaTareas;
  }

  // Función para listar todas las tareas no completadas
  function listarTareasNoCompletadas() {
    return listaTareas.filter((tarea) => !tarea.estáCompletada);
  }

  // Manejo de la acción recibida
  switch (accion) {
    case "añadir":
      if ("identificador" in tarea && "descripción" in tarea) {
        tarea.estáCompletada = false; // Asumir que la tarea no está completada al añadir
        return añadirTarea(tarea);
      } else {
        console.error("Error: Propiedades faltantes en la tarea al añadir.");
        return null;
      }
    case "completar":
      if (
        "identificador" in tarea &&
        typeof tarea.estáCompletada === "boolean"
      ) {
        return completarTarea(tarea.identificador);
      } else {
        console.error(
          "Error: Propiedades faltantes o inválidas en la tarea al completar."
        );
        return null;
      }
    case "eliminar":
      if (typeof identificador === "number") {
        return eliminarTarea(identificador);
      } else {
        console.error("Error: El identificador debe ser un número.");
        return null;
      }
    case "listar":
      return listarTareasNoCompletadas();
    default:
      console.error("Error: Acción no reconocida.");
      return null;
  }
}

// Ejemplo de uso
const tarea1 = {
  identificador: 1,
  descripción: "Comprar leche",
  estáCompletada: false,
};
const tarea2 = {
  identificador: 2,
  descripción: "Pasear al perro",
  estáCompletada: false,
};

// Añadiendo tareas
gestionarTareas("añadir", tarea1);
gestionarTareas("añadir", tarea2);

// Completando una tarea
gestionarTareas("completar", { identificador: 1, estáCompletada: true });

// Eliminando una tarea
gestionarTareas("eliminar", null, 2);

// Listando tareas no completadas
gestionarTareas("listar", null, null);
