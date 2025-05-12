import sys
import os

# Agrega la carpeta raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import patch
from src.proyecto.metodos import solicitar_moneda, solicitar_cantidad, desea_continuar

def test_desea_continuar_si(monkeypatch):
    # Simulamos que el usuario ingresa 's'
    monkeypatch.setattr('builtins.input', lambda _: 's')
    assert desea_continuar() == True

def test_desea_continuar_no(monkeypatch):
    # Ahora simulamos que el usuario ingresa 'n'
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    assert desea_continuar() == False

### 

def test_solicitar_moneda_valid_input():
    """Test that a valid currency is accepted."""
    with patch('builtins.input', side_effect=["USD"]):
        assert solicitar_moneda("Introduce una moneda: ") == "USD"

def test_solicitar_moneda_invalid_then_valid_input():
    """Test that an invalid currency is rejected and a valid one is accepted."""
    with patch('builtins.input', side_effect=["ABC", "EUR"]):
        with patch('builtins.print') as mock_print:
            assert solicitar_moneda("Introduce una moneda: ") == "EUR"
            mock_print.assert_called_with("❌ Moneda no válida. Las opciones válidas son: ['USD', 'EUR', 'MXN']")

def test_solicitar_moneda_multiple_invalid_then_valid_input():
    """Test that multiple invalid inputs are rejected until a valid one is provided."""
    with patch('builtins.input', side_effect=["XYZ", "123", "MXN"]):
        with patch('builtins.print') as mock_print:
            assert solicitar_moneda("Introduce una moneda: ") == "MXN"
            assert mock_print.call_count == 2
            mock_print.assert_any_call("❌ Moneda no válida. Las opciones válidas son: ['USD', 'EUR', 'MXN']")

###

def test_solicitar_cantidad(monkeypatch):
    with patch('builtins.input', side_effect=["abc", 12]):
        with patch('builtins.print') as mock_print:
            assert type(solicitar_cantidad()) == float
            mock_print.assert_called_with("❌ Cantidad inválida. Por favor, introduce una cantidad válida.")

''' 
def test_solicitar_moneda_valida_minuscula(monkeypatch):
    # Simulamos que el usuario ingresa una opción válida pero en minusculas
    entrada_valida_minuscula = "mxn"
    monkeypatch.setattr('builtins.input', lambda _: entrada_valida_minuscula)
    assert solicitar_moneda(entrada_valida_minuscula) == "MXN"

def test_solicitar_monedas_invalida(monkeypatch):
    # Simulamos que el usuario ingresa una opción inválida
    entrada_invalida = "jpn"
    monkeypatch.setattr('builtins.input', lambda _: entrada_invalida)
    assert solicitar_moneda(entrada_invalida) == False
'''