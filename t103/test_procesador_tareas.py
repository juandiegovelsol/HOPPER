import json
from procesador_tareas import main

JSON_VALIDO = [
  {
    "descripcion": "Resolver problema del usuario 34",
    "asignado_a": "Luis",
    "entregada": True
  },
  {
    "descripcion": "Configurar entorno de desarrollo",
    "asignado_a": "Mariela",
    "entregada": False
  },
  {
    "descripcion": "Revisar código de Ana",
    "asignado_a": "Roberto",
    "entregada": True
  },
  {
    "descripcion": "Subir aplicación a producción",
    "asignado_a": "Luis",
    "entregada": False
  },
  {
    "descripcion": "Documentar el proyecto",
    "asignado_a": "Ana",
    "entregada": False
  }
]

JSON_INVALIDO = [
  {
    "descripcion": "Tarea sin entrega",
    "asignado_a": "Nadie",
    "entregada": True
  },
  {
    "descripcion": "Tarea con entrega mal",
    "asignado_a": "Otro",
    "entregada": "sí"
  },
  {
    "descripcion": "",
    "asignado_a": "Vacio",
    "entregada": False
  },
  {
    "descripcion": "Tarea sin asignado",
    "entregada": False
  }
]

def crear_archivo_json_temporal(tmp_path, nombre_archivo, datos):
    ruta_archivo = tmp_path / nombre_archivo
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    return ruta_archivo

def test_flujo_exitoso_completo(tmp_path, monkeypatch, capsys):
    nombre_archivo = "tareas.json"
    crear_archivo_json_temporal(tmp_path, nombre_archivo, JSON_VALIDO)

    monkeypatch.chdir(tmp_path)

    main()

    captured = capsys.readouterr()
    output = captured.out

    assert "Cargando tareas desde 'tareas.json'..." in output
    assert "Se encontraron 5 tareas válidas." in output
    assert "RESUMEN DE TAREAS" in output
    assert "Tareas totales: 5" in output
    assert "Tareas entregadas: 2" in output
    assert "Tareas pendientes: 3" in output
    assert "Personas con tareas pendientes:" in output
    assert "- Ana: 1 tarea pendiente/s" in output
    assert "- Luis: 1 tarea pendiente/s" in output
    assert "- Mariela: 1 tarea pendiente/s" in output
    assert "Error:" not in output

def test_solo_tareas_invalidas(tmp_path, monkeypatch, capsys):
    nombre_archivo = "tareas.json"
    crear_archivo_json_temporal(tmp_path, nombre_archivo, JSON_INVALIDO)

    monkeypatch.chdir(tmp_path)

    main()

    captured = capsys.readouterr()
    output = captured.out

    assert "Cargando tareas desde 'tareas.json'..." in output
    assert "Error: Rechazado - Clave 'entregada' no es booleana:" in output
    assert "Error: Rechazado - Clave 'descripcion' está vacía:" in output
    assert "Error: Rechazado - Falta clave 'asignado_a':" in output
    assert "Se encontraron 1 tareas válidas." in output
    assert "RESUMEN DE TAREAS" in output
    assert "Tareas totales: 1" in output
    assert "Tareas entregadas: 1" in output
    assert "Tareas pendientes: 0" in output
    assert "No hay tareas pendientes asignadas." in output