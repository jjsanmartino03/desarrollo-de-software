"""
Club deportivo

Un club deportivo tiene 4 categorías de asociados según la edad:

    infantiles (desde 13 a 15 años)
    cadetes (a partir de los 15 y hasta 17)
    juveniles (desde los 17 hasta los 19)
    mayores (de 19 años en adelante)

Escriba un programa que permita al usuario ingresar el nombre y la edad de un
socio y muestre su el nombre de la categoría en la que le corresponde estar.
"""

nombre = input('Ingrese el nombre del socio: ')
edad = int(input('Ingrese la edad del socio: '))

categoria = None

if edad >= 13 and edad < 15:
    categoria = 'infantiles'
elif edad >= 15 and edad < 17:
    categoria = 'cadetes'
elif edad >= 17 and edad < 19:
    categoria = 'juveniles'
elif edad >= 19:
    categoria = 'mayores'

if not categoria:
    print(f'El socio {nombre} no pertenece a ninguna categoría')
else:
    print(f'El socio {nombre} pertenece a la categoría de {categoria}')
