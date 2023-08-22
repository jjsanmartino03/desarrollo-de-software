"""
Escriba un programa que permita a una persona conocer a cuántos Pesos Argentinos equivalen
hoy los Bitcoins (BTC) que encontró guardados en un disco rígido viejo.
El usuario del programa debe ingresar una cantidad en Bitcoins.
"""

# 22/09/2023
# 1 BTC = 25851,51
# 1 USD = 727 ARS

bitcoins = float(input('Ingrese la cantidad de Bitcoins encontrados: '))

print(f'Los {bitcoins} Bitcoins equivalen a {bitcoins * 25851.51 * 727:,} ARS')
