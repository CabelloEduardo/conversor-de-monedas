class Moneda:
    def __init__(self, codigo, simbolo, nombre):
        self.codigo = codigo
        self.simbolo = simbolo
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
