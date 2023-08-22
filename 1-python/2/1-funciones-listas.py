"""
Funciones para operar sobre una lista

Generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random). Luego:

    Muestre la lista
    El usuario ingresa debe ingresar un valor un valor. El programa debe informar cuántos valores
    de la lista son mayores a dicho valor, para eso debe utilizar una función. La función debe
    recibir como argumentos la lista y un entero, y debe retornar la cantidad de valores de la
    lista mayores a dicho entero.
    Crear una función que calcule el promedio de la lista y utilizarla.
    Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne.

"""

from random import randint

numbers = [randint(1, 20) for i in range(10)]

print('Lista generada:', numbers)

num = int(input('Ingrese un valor: '))


def find_greater_numbers(numbers_list, num):
    counter = 0

    for number in numbers_list:
        if number > num:
            counter += 1

    return counter


print(f'Hay {find_greater_numbers(numbers, num)} números más grandes que el valor ingresado.')


def get_average(numbers_list):
    return sum(numbers_list) / len(numbers_list)


print(f'El promedio de la lista es {get_average(numbers)}')


def find_max_and_min(numbers_list):
    return {
        'min': min(numbers_list),
        'max': max(numbers_list)
    }


result = find_max_and_min(numbers)

print(f'El mayor número de la lista es {result["max"]}, mientras que el menor es {result["min"]}')
