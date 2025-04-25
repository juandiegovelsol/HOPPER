import json
import os
import pytest
from tareas1 import cargar_tareas, generar_resumen, mostrar_resumen

@pytest.fixture
def archivo_json_exitoso(tmp_path):
    contenido = [
        {
            "descripcion": "Resolver problema del usuario 34",
            "asignado_a": "Luis",
            "entregada": True
        },
        {
            "descripcion": "Configurar entorno de desarrollo",
            "asignado_a": "Mariela",
            "entregada": False
        }
    ]
    archivo = tmp_path / "tareas_exitosas.json"
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(contenido, f)
    return str(archivo)

@pytest.fixture
def archivo_json_invalido(tmp_path):
    contenido = [
        {"descripcion": "Tarea sin asignado", "entregada": True},
        {"asignado_a": "Luis", "entregada": True}
    ]
    archivo = tmp_path / "tareas_invalidas.json"
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(contenido, f)
    return str(archivo)

def test_cargar_tareas_exitoso(archivo_json_exitoso):
    tareas = cargar_tareas(archivo_json_exitoso)
    assert len(tareas) == 2

def test_cargar_tareas_invalido(archivo_json_invalido):
    tareas = cargar_tareas(archivo_json_invalido)
    assert len(tareas) == 0