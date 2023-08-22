# -*- coding: utf-8 -*-
import db_productos

productos = []


def mostrar_productos(productos):
    for producto in productos:
        print(f'Producto {producto["id"]}')
        print(f'{producto["nombre"]} ${producto["precio"]}')
        print('---')


mostrar_productos(productos)


def calcular_precio_actualizado(precio_anterior, porcentaje):
    return precio_anterior * (1 + (porcentaje / 100))


def actualizar_precios(productos, porcentaje_aumento):
    for i in range(len(productos)):
        productos[i]['precio'] = calcular_precio_actualizado(productos[i]['precio'], porcentaje_aumento)


if __name__ == '__main__':
    productos = db_productos.cargar_productos()
    mostrar_productos(productos)

    porcentaje_aumento = float(input('Ingrese el porcentaje de aumento, (por ejemplo 37.5): '))

    actualizar_precios(productos,porcentaje_aumento)

    mostrar_productos(productos)
