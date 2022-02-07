"""
Exercicio-10: Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
Autor: Lucas Leão

"""

gr_c = float(input('Informe a temeratura em °C: '))
gr_f = (gr_c * 1.8) + 32
print(f'{gr_c}°C é equivalente a {gr_f}°F')