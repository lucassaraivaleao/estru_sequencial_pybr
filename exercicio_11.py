"""
Exercicio-11: Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.

Autor: Lucas Leão

"""

num_int1 = int(input('Informe com o primeiro numero inteiro: '))
num_int2 = int(input('Informe com o segundo numero inteiro: '))
num_real = float(input('Informe um número real: '))

calc1 = ((num_int1**2) * (num_int2/2))
calc2 = ((num_int1 ** 3) + num_real)
calc3 = (num_real **3)

print(f'O produto do dobro do primeiro com metade do segundo: {calc1}'
      f'\nA soma do triplo do primeiro com o terceiro: {calc2}\nO terceiro elevado ao cubo: {calc3}')