from metodos import solicitar_moneda, desea_continuar
from metodos import catalogo_monedas

def main():
    mensaje_solicitar_moneda_origen = f"Por favor elija la mondeda de origen {catalogo_monedas}: "
    mensaje_solicitar_moneda_destino = f"Por favor elija la moneda de destino {catalogo_monedas}: "
    print("💵💶 Bienvenido al conversor de monedas 💴💷")

    while True:
        moneda_origen = solicitar_moneda(mensaje_solicitar_moneda_origen)
        moneda_destino = solicitar_moneda(mensaje_solicitar_moneda_destino)

        if not desea_continuar():
            print("👋 ¡Gracias por usar el conversor de monedas!")
            break

if __name__ == "__main__":
    main()