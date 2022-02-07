"""
Exercicio-09: Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
Autor: Lucas Leão

"""

graus_fah = float(input('Informe a temeperatua em F°: '))
graus_c = 5 * ((graus_fah-32)/9)
print(f'{graus_fah}°F é equivalente a {graus_c}°C')