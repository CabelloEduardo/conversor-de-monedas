catalogo_monedas = ["USD", "EUR", "MXN"]

def solicitar_moneda(moneda):
    """Solicita una moneda válida al usuario hasta que la entrada sea correcta."""
    while True:
        moneda.upper()
        if moneda in catalogo_monedas:
            return moneda
        else:
            print(f"❌ Moneda no válida. Las opciones válidas son:{catalogo_monedas}")


def desea_continuar():
    """Pregunta al usuario si desea realizar otra operación."""
    respuesta = input("¿Deseas hacer otra operación? (s/n): ").strip().lower()
    return respuesta == 's'
