"""
Exercicio-06:  Faça um Programa que peça o raio de um círculo, calcule e
mostre sua área. Obs: A área de um círculo é pi vezes o raio elevado ao quadrado (A = π r²)
Autor: Lucas Leão

"""

import math
raio = float(input('Informe o raio do círculo: '))
area_circulo = math.pi * (raio * raio)
print(area_circulo)

