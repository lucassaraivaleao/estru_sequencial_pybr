"""
Exercicio-15:Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu salário
 no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
* salário bruto.
* quanto pagou ao INSS.
* quanto pagou ao sindicato.
* o salário líquido.

Autor: Lucas Leão

"""

valor_hora = float(input('Informe quanto você ganha por hora: '))
horas_trabalhadas = float(input('Informe as horas trabalhadas: '))
salario = float(input('Informe seu salário bruto: '))

valor_horas = horas_trabalhadas * valor_hora
salario_bruto = salario + valor_horas

imposto_renda = (salario_bruto * 0.11)
inss = (salario_bruto * 0.08)
sindicato = (salario_bruto * 0.05)
descontos = (imposto_renda + inss + sindicato)
salario_liquido = salario_bruto - descontos

print(f'Salário Bruto: {round(salario_liquido,2)}')