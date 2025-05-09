aircraft_list = []
movement_log = []

def manage_aircraft(modelo, duenio, fecha, hora, tipo_movimiento):
    """Gestiona el ingreso o egreso de una aeronave. En ingreso, añade la aeronave si no existe."""
    mov = tipo_movimiento.lower()
    if mov not in ('ingreso', 'egreso'):
        print("Error: tipo de movimiento inválido. Use 'ingreso' o 'egreso'.")
        return

    if mov == 'ingreso':
        existe = any(ac['modelo'] == modelo and ac['dueño'] == duenio for ac in aircraft_list)
        if not existe:
            aircraft_list.append({'modelo': modelo, 'dueño': duenio})
        movement_log.append({'modelo': modelo, 'dueño': duenio, 'fecha': fecha, 'hora': hora, 'tipo': mov})
        print(f"Ingreso registrado: Modelo={modelo}, Dueño={duenio}, Fecha={fecha}, Hora={hora}")
    else:
        existe = any(ac['modelo'] == modelo and ac['dueño'] == duenio for ac in aircraft_list)
        if not existe:
            print(f"Error: no se puede egresar. La aeronave Modelo={modelo}, Dueño={duenio} no está registrada.")
            return
        movement_log.append({'modelo': modelo, 'dueño': duenio, 'fecha': fecha, 'hora': hora, 'tipo': mov})
        print(f"Egreso registrado: Modelo={modelo}, Dueño={duenio}, Fecha={fecha}, Hora={hora}")

def list_aircrafts():
    """Imprime listado de aeronaves registradas."""
    print("Listado de aeronaves registradas:")
    for ac in aircraft_list:
        print(f"- Modelo={ac['modelo']}, Dueño={ac['dueño']}")

def list_movements():
    """Imprime registro de movimientos."""
    print("Registro de movimientos:")
    for mv in movement_log:
        tipo = mv['tipo'].title()
        print(f"- {tipo} | Modelo={mv['modelo']}, Dueño={mv['dueño']}, Fecha={mv['fecha']}, Hora={mv['hora']}")

def manager(accion, **kwargs):
    """Despacha acciones: 'manage', 'list_aircrafts', 'list_movements'."""
    if accion == 'manage':
        manage_aircraft(kwargs.get('modelo'), kwargs.get('duenio'), kwargs.get('fecha'), kwargs.get('hora'), kwargs.get('tipo_movimiento'))
    elif accion == 'list_aircrafts':
        list_aircrafts()
    elif accion == 'list_movements':
        list_movements()
    else:
        print(f"Acción desconocida: {accion}")

manage_aircraft('PA-200', 'María López', '08/05/2025', '09:00', 'ingreso')
manage_aircraft('tronador 54', 'Carlos García', '06/05/2025', '10:15', 'ingreso')
manage_aircraft('Pipa PA-28', 'María López', '07/05/2025', '14:30', 'egreso')
manage_aircraft('Diamante DA40', 'Luis Fernández', '07/05/2025', '16:45', 'egreso')