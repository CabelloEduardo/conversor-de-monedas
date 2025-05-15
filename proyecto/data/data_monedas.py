# data/monedas.py

from moneda import Moneda

USD = Moneda("USD", "$", "Dólar estadounidense")
EUR = Moneda("EUR", "€", "Euro")
JPY = Moneda("JPY", "¥", "Yen japonés")

CATALOGO_MONEDAS = {
    "USD": USD,
    "EUR": EUR,
    "JPY": JPY,
}
