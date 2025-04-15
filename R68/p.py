import pytest
from unittest.mock import MagicMock
from adapters import InsertNewProjectAdapter
from models import Proyectos
from config import set_dsn
from connection_migrates import connect, disconnect
from queries import delete_project_by_id

@pytest.fixture
def setup_database():
    set_dsn("root:safraroot@tcp(localhost:3306)/?charset=utf8mb4&parseTime=True&loc=Local")

@pytest.fixture
def test_project():
    return Proyectos(
        name="Proyecto de Ejemplo",
        descripcion="Descripción del proyecto",
        valor=100000.00,
        tipo_obra="Construcción",
        usuario_id="usuario_prueba_id"
    )

def test_insert_new_project_adapter_successful(setup_database, test_project, mocker):
    # Mock de la inserción del proyecto
    mock_insert = mocker.patch("adapters.InsertNewProjectAdapter", return_value=(None, test_project))

    err, inserted_project = InsertNewProjectAdapter(test_project)

    # Verificaciones
    assert err is None, "No se esperaba un error al insertar el proyecto"
    assert inserted_project is not None, "Se esperaba que el proyecto insertado no fuera nulo"
    assert inserted_project.id_proyecto is not None, "Se esperaba que el ID del proyecto insertado no estuviera vacío"
    assert inserted_project.name == test_project.name, "El nombre del proyecto insertado no coincide con el esperado"
    assert inserted_project.descripcion == test_project.descripcion, "La descripción del proyecto insertado no coincide con la esperada"

    # Simulación de la conexión a la base de datos y limpieza de datos
    mock_connect = mocker.patch("connection_migrates.connect", return_value=MagicMock())
    mock_delete = mocker.patch("queries.delete_project_by_id", return_value=None)
    mock_disconnect = mocker.patch("connection_migrates.disconnect")

    db = connect()
    delete_project_by_id(db, inserted_project.id_proyecto)
    disconnect(db)

    # Verificaciones de limpieza
    mock_connect.assert_called_once()
    mock_delete.assert_called_once_with(db, inserted_project.id_proyecto)
    mock_disconnect.assert_called_once()