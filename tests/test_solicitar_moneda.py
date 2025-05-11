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