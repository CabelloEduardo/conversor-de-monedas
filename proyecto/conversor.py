class Conversor:
    def __init__(self, tasas):
        self.tasas = tasas  # dict como {'USD_EUR': 0.91}

    def convertir(self, cantidad, moneda_origen, moneda_destino):
        clave = f"{moneda_origen.codigo}_{moneda_destino.codigo}"
        if clave in self.tasas:
            tasa = self.tasas[clave]
            return cantidad * tasa
        else:
            raise ValueError("No se encontró la tasa de cambio.")
