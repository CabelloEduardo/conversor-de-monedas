from metodos import solicitar_moneda, desea_continuar
from metodos import catalogo_monedas

def main():
    mensaje_solicitar_moneda_origen = f"Por favor elija la mondeda de origen {catalogo_monedas}:"
    mensaje_solicitar_moneda_destino = f"Por favor elija la moneda de destino {catalogo_monedas}:"
    print("💵💶 Bienvenido al conversor de monedas 💴💷")

    while True:
        moneda_origen = solicitar_moneda(input(f"Por favor elija la mondeda de origen {catalogo_monedas}:"))
        moneda_destino = solicitar_moneda(input(f"Por favor elija la moneda de destino {catalogo_monedas}"))

        if not desea_continuar():
            print("👋 ¡Gracias por usar la calculadora!")
            break

if __name__ == "__main__":
    main()