from proyecto.interfaz.metodos import desea_continuar
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_desea_continuar_si(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 's')
    assert desea_continuar() == True


def test_desea_continuar_no(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    assert desea_continuar() == False
