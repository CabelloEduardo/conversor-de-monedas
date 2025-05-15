from proyecto.interfaz.metodos import solicitar_moneda


def test_solicitar_moneda(monkeypatch):
    catalogo = {"USD", "EUR", "JPY"}

    # Simulamos que el usuario ingresa primero "abc" (inválido), luego "usd" (válido)
    inputs = iter(["abc", "usd"])

    # Monkeypatch para reemplazar input() y devolver valores del iterador
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Capturamos la salida estándar para verificar el mensaje de error
    from io import StringIO
    import sys

    salida = StringIO()
    sys.stdout = salida

    resultado = solicitar_moneda("Ingresa moneda: ", catalogo)

    sys.stdout = sys.__stdout__  # Restaurar salida estándar

    # El resultado debe ser "USD" (convertido a mayúsculas)
    assert resultado == "USD"

    # Verificamos que el mensaje de error apareció en la salida
    assert "Moneda no válida" in salida.getvalue()
