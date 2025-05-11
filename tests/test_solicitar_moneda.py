import sys
import os

# Agrega la carpeta raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.proyecto.metodos import solicitar_moneda, desea_continuar


def test_desea_continuar(monkeypatch):
    # Simulamos que el usuario ingresa 's'
    monkeypatch.setattr('builtins.input', lambda _: 's')
    assert desea_continuar() == True

    # Ahora simulamos que el usuario ingresa 'n'
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    assert desea_continuar() == False