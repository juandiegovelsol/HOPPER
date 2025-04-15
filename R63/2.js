function gestionarTareas(accion, tarea, identificador) {
  // Lista de tareas
  const listaTareas = [];

  // Función para añadir una nueva tarea
  function añadirTarea(id, descripcion) {
    const nuevaTarea = {
      identificador: id,
      descripcion: descripcion,
      estaCompletada: false,
    };
    listaTareas.push(nuevaTarea);
    return listaTareas;
  }

  // Función para marcar una tarea como completada
  function completarTarea(id, estaCompletada) {
    const tareaIndex = listaTareas.findIndex(
      (tarea) => tarea.identificador === id
    );
    if (tareaIndex !== -1) {
      listaTareas[tareaIndex].estaCompletada = estaCompletada;
      return listaTareas;
    } else {
      throw new Error("Tarea no encontrada");
    }
  }

  // Función para eliminar una tarea por su identificador
  function eliminarTarea(id) {
    const tareaIndex = listaTareas.findIndex(
      (tarea) => tarea.identificador === id
    );
    if (tareaIndex !== -1) {
      listaTareas.splice(tareaIndex, 1);
      return listaTareas;
    } else {
      throw new Error("Tarea no encontrada");
    }
  }

  // Función para listar todas las tareas no completadas
  function listarTareasNoCompletadas() {
    return listaTareas.filter((tarea) => !tarea.estaCompletada);
  }

  // Manejo de la acción recibida
  switch (accion) {
    case "añadir":
      if (
        typeof identificador === "number" &&
        typeof descripcion === "string"
      ) {
        return añadirTarea(identificador, descripcion);
      } else {
        throw new Error("Parámetros de añadir no válidos");
      }
    case "completar":
      if (
        typeof identificador === "number" &&
        typeof estaCompletada === "boolean"
      ) {
        return completarTarea(identificador, estaCompletada);
      } else {
        throw new Error("Parámetros de completar no válidos");
      }
    case "eliminar":
      if (typeof identificador === "number") {
        return eliminarTarea(identificador);
      } else {
        throw new Error("Parámetro de eliminar no válido");
      }
    case "listar":
      return listarTareasNoCompletadas();
    default:
      throw new Error("Acción no reconocida");
  }
}

// Uso de la función
try {
  const tareas = gestionarTareas("añadir", {
    identificador: 1,
    descripcion: "Comprar leche",
  });
  console.log(tareas);

  const tareasActualizadas = gestionarTareas(
    "completar",
    { identificador: 1, descripcion: "" },
    true
  );
  console.log(tareasActualizadas);

  const tareasDespuésDeEliminar = gestionarTareas(
    "eliminar",
    { identificador: 1, descripcion: "" },
    1
  );
  console.log(tareasDespuésDeEliminar);

  const tareasPendientes = gestionarTareas(
    "listar",
    { identificador: 1, descripcion: "" },
    1
  );
  console.log(tareasPendientes);
} catch (error) {
  console.error(error.message);
}

// Nota: Las funciones internas podrían ser modificadas para aceptar diferentes tipos de entradas y manejar errores de forma más específica. Por ejemplo, se podría utilizar try catch dentro de las funciones para manejar errores de tipo y devolver códigos más específicos en lugar de lanzar errores. Esto mejoraría la robustez del código principal.
