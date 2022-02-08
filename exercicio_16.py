"""
Exercicio-16:
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da
tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de
latas de tinta a serem compradas e o preço total.

Autor: Lucas Leão

"""

import math

metros_pintura = int(input('Informe o tamanho em metros a ser pintado: '))
litros = round(metros_pintura / 3)
galoes_necessarios = litros / 18
galoes = ((galoes_necessarios))
valor_a_ser_pago = galoes * 80
print(f'Para que sejam pintados {metros_pintura}m2,'
      f' serão necessários {math.ceil(galoes)} galões\nTotal: {round(valor_a_ser_pago,2)}')