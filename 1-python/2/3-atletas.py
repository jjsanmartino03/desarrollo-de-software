import random


def generar_lista_de_atletas():
    """
    Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
    Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
        - nombre: el nombre del atleta
        - numero: el número con el que participó en la maratón
        - tiempo_llegada: la cantidad de segundos que tardó en llegar
    """
    lista_atletas = []
    nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
    apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')
    for i in range(1, 21):
        atleta = {
            "nombre": random.choice(nombres) + " " + random.choice(apellidos),
            "numero": i,
            "tiempo_llegada": random.random() * 120
        }
        lista_atletas.append(atleta)
    return lista_atletas


"""

Utilizar la función anterior para generar y almacenar una lista de atletas
Escribir una función que reciba la lista de atletas e imprima una línea por cada atleta 
respetando el siguiente formato: "<num_atleta> - : (<tiempo_llegada> segundos)", 
donde <num_atleta> es el número del atleta, su nombre y <tiempo_llegadad> su tiempo de llegada.
Escribir una función que devuelva el número del atleta que resultó ganador.
Escribir una función que, recibiendo el número de atleta de un competidor, devuelva todos sus datos (nombre, número y tiempo de llegadad).
OPCIONAL: Escribir una función que devuelva una tupla con los números de los 3 atletas que entraron al podio de ganadores en orden de llegada.

"""

atletas = generar_lista_de_atletas()


def show_atletas(atletas):
    for atleta in atletas:
        print(f'{atleta["numero"]} - : ({atleta["tiempo_llegada"]:.2f} segundos)')


show_atletas(atletas)


def get_numero_atleta_ganador(atletas):
    min_time = atletas[0]['tiempo_llegada']
    min_num = atletas[0]['numero']

    for atleta in atletas:
        if atleta['tiempo_llegada'] < min_time:
            min_time = atleta['tiempo_llegada']
            min_num = atleta['numero']

    return min_num


num_ganador = get_numero_atleta_ganador(atletas)
print(f'El número del atleta ganador es {num_ganador}')


def get_datos_from_numero(atletas, num):
    for atleta in atletas:
        if num == atleta['numero']:
            return atleta


atleta_ganador = get_datos_from_numero(atletas, num_ganador)

print(
    f'El atleta ganador tiene el número {atleta_ganador["numero"]}, se llama {atleta_ganador["nombre"]},'
    f' y su tiempo de llegada fue {atleta_ganador["tiempo_llegada"]:.2f} segundos')


def get_numeros_podio(atletas):
    podio = sorted(atletas, key=lambda x: x["tiempo_llegada"])[:3]

    return tuple(map(lambda x: x['numero'],podio))



print(f'Los números de los tres ganadores, en orden de llegada, son:',get_numeros_podio(atletas))
