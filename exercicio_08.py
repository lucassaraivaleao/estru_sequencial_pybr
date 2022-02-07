"""
Exercicio-08: Faça um Programa que pergunte quanto você ganha
 por hora e o número de horas trabalhadas no mês. Calcule e
 mostre o total do seu salário no referido mês.
 Autor: Lucas Leão

"""

salario = float(input('Informe seu salário: '))
valor_horas = float(input('Informe quanto você ganha por hora trabalhada: '))
horas_mensais = float(input('Informe a quantidade de horas trabalhadas neste mês: '))

salario_final = salario + (horas_mensais * valor_horas)

print(f'Seu salário no final do mês será: {salario_final}')