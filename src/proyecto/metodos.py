catalogo_monedas = ["USD", "EUR", "MXN"]

def solicitar_moneda(mensaje: str) -> str:
    """Solicita una moneda válida al usuario hasta que la entrada sea correcta."""
    while True:
        moneda = input(mensaje).upper()
        if moneda in catalogo_monedas:
            return moneda
        else:
            print(f"❌ Moneda no válida. Las opciones válidas son: {catalogo_monedas}")

def desea_continuar() -> bool:
    """Pregunta al usuario si desea realizar otra operación."""
    return input("¿Deseas hacer otra operación? (s/n): ").strip().lower() == 's'
