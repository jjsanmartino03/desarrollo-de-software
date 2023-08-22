"""
Franco está organizando un asado con sus amigos y necesita de tu ayuda.
Para estimar cuánta carne necesita comprar, va a suponer que cada invitado
come 0.7 Kg de carne. Ayuda a Franco escribiendo un programa que permita al
usuario ingresar la cantidad de invitados y el precio de 1Kg. de carne, y
muestre cuántos Kg de carne en total debe pedir al carnicero y cuánto dinero necesita para pagar.
"""

carne_por_invitado = 0.7

invitados = int(input('Ingrese la cantidad de invitados: '))
precio_por_kg = float(input('Ingrese el precio de 1Kg de carne: '))

kg_totales = invitados * carne_por_invitado

print(f'Debe comprar {kg_totales} kg de carne, y deberá pagar {kg_totales * precio_por_kg}')
