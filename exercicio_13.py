"""
Exercicio-13: Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
* Para homens: (72.7*h) - 58
* Para mulheres: (62.1*h) - 44.7

Autor: Lucas Leão

"""

altura = float(input('Informe a altura da pessoa: '))
sexo = input('Sexo(m)/(f): ')
if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44
print(f'Seu peso ideal é: {round(peso_ideal, 2)}')