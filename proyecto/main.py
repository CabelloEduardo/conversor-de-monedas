from interfaz.metodos import solicitar_moneda, solicitar_cantidad, desea_continuar
from data.data_monedas import CATALOGO_MONEDAS


def main():
    catalogo_monedas = list(CATALOGO_MONEDAS.keys())
    mensaje_solicitar_moneda_origen = f"Por favor elija la mondeda de origen {catalogo_monedas}: "
    mensaje_solicitar_moneda_destino = f"Por favor elija la moneda de destino {catalogo_monedas}: "
    print("💵💶 Bienvenido al conversor de monedas 💴💷")

    while True:
        moneda_origen = solicitar_moneda(
            mensaje_solicitar_moneda_origen,
            catalogo_monedas
        )
        moneda_destino = solicitar_moneda(
            mensaje_solicitar_moneda_destino,
            catalogo_monedas
        )
        cantidad_a_convertir = solicitar_cantidad()
        if not desea_continuar():
            print("👋 ¡Gracias por usar el conversor de monedas!")
            break


if __name__ == "__main__":
    main()
