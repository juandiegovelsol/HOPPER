//Lista de tareas persistente fuera de la función
const listaTareas = [];
function gestionarTareas(accion, tarea) {
  // Función para añadir una nueva tarea
  function añadirTarea(tarea) {
    listaTareas.push(tarea);
    return listaTareas;
  }

  // Función para completar una tarea existente
  function completarTarea(identificador) {
    const indiceTarea = listaTareas.findIndex(
      (t) => t.identificador === identificador
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
      (t) => t.identificador === identificador
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
    return listaTareas.filter((t) => !t.estáCompletada);
  }

  // Manejo de la acción recibida
  switch (accion) {
    case "añadir":
      if (tarea && "identificador" in tarea && "descripción" in tarea) {
        tarea.estáCompletada = false; // Asumir que la tarea no está completada al añadir
        return añadirTarea(tarea);
      } else {
        console.error("Error: Propiedades faltantes en la tarea al añadir.");
        return null;
      }
    case "completar":
      if (tarea && "identificador" in tarea) {
        return completarTarea(tarea.identificador);
      } else {
        console.error(
          "Error: Propiedades identificador faltante o inválida en la tarea al completar."
        );
        return null;
      }
    case "eliminar":
      if (tarea && typeof tarea.identificador === "number") {
        return eliminarTarea(tarea.identificador);
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
console.log(
  gestionarTareas("añadir", { identificador: 1, descripción: "comprar leche" })
);
console.log(
  gestionarTareas("añadir", {
    identificador: 2,
    descripción: "pasear al perro",
  })
);

// Completando una tarea
console.log(gestionarTareas("completar", { identificador: 1 }));

// Eliminando una tarea
console.log(gestionarTareas("eliminar", { identificador: 2 }));

// Listando tareas no completadas
console.log(gestionarTareas("listar"));
