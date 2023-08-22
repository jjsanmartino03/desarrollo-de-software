"""
Durante los 5 días de una semana se tomaron mediciones de temperatura en la ciudad.
Se desea conocer cuál fue la temperatura promedio de la semana.
Escriba un programa que permita calcularla a partir de 5 valores de temperatura que ingresará el usuario.
"""
temperatures = []

for i in range(5):
    temperatures.append(int(input(f'Ingrese la temperatura del día {i + 1}: ')))

print(f'La temperatura promedio de la semana fue de {sum(temperatures) / len(temperatures)} grados')
