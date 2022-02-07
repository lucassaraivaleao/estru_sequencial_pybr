"""
Exercicio-14:João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o
valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

Autor: Lucas Leão

"""

limite_peso = 50
multa = 4.00

peso_peixe = float(input('Informe a o total em quilos de peixe: '))
if (peso_peixe <= limite_peso):
    print('Liberado sem multa !')
else:
    excesso = peso_peixe - limite_peso
    total_pagar = excesso * multa
    print(f'Pescador multado ! \nPeixe pescado: {peso_peixe}\nExedente: {excesso}\nTotal a pagar: R$:{total_pagar}')