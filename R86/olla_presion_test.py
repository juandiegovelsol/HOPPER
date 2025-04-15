# test_olla_presion.py
import pytest
from io import StringIO
from unittest.mock import patch
import olla_presion as main_module

@pytest.fixture(autouse=True)
def reset_globals():
    main_module.config.update(main_module.cargar_configuracion())
    main_module.presion_acumulada = 0
    main_module.muestras = 0
    main_module.max_historico = 0
    main_module.valvula_activa = False
    main_module.eventos.clear()
    main_module.tendencia.clear()
    main_module.receta_actual = None

def test_valvula_activa_sobre_umbral():
    main_module.config['critico'] = 95
    resultado = main_module.controlar_valvula(100)
    assert resultado == 60
    assert main_module.valvula_activa is True

def test_valvula_no_activa_bajo_umbral():
    main_module.config['critico'] = 95
    resultado = main_module.controlar_valvula(90)
    assert resultado == 90
    assert main_module.valvula_activa is False

def test_actualizacion_estadisticas():
    main_module.actualizar_estadisticas(80)
    assert main_module.presion_acumulada == 80
    assert main_module.muestras == 1
    assert main_module.max_historico == 80

def test_alarma_presion_critica():
    with patch('sys.stdout', new_callable=StringIO) as mock_output:
        main_module.mostrar_alarma("¡PRESIÓN CRÍTICA!")
        output = mock_output.getvalue()
        assert "¡PRESIÓN CRÍTICA!" in output

def test_deteccion_picos():
    main_module.config['umbral_pico'] = 15
    alerta = main_module.detectar_pico(50, 30)
    assert "Δ20" in alerta

def test_configuracion_valida(monkeypatch):
    inputs = iter(['80', '90'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main_module.configurar_umbrales_interactivo()
    assert main_module.config['max_seguro'] == 80
    assert main_module.config['critico'] == 90

def test_configuracion_invalida(monkeypatch):
    inputs = iter(['95', '80'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(ValueError):
        main_module.configurar_umbrales_interactivo()