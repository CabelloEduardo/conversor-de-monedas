
def solicitar_moneda(mensaje: str, catalogo_monedas) -> str:
    """Solicita una moneda válida al usuario hasta que la entrada sea correcta."""
    while True:
        moneda = input(mensaje).upper()
        if moneda in catalogo_monedas:
            return moneda
        else:
            print(
                f"❌ Moneda no válida. Las opciones válidas son: {catalogo_monedas}")


def solicitar_cantidad():
    """Solicita una cantidad flotante"""
    while True:
        try:
            cantidad = float(input("Escribe la cantidad: "))
            return cantidad
        except Exception as e:
            print(f"❌ Cantidad inválida. Por favor, introduce una cantidad válida.")


def desea_continuar() -> bool:
    """Pregunta al usuario si desea realizar otra operación."""
    return input("¿Deseas hacer otra operación? (s/n): ").strip().lower() == 's'
