"""
Exercicio-04: Faça um Programa que peça as 4 notas bimestrais e mostre a média.
Autor: Lucas Leão
"""

notas_bimestrais = 0
for i in range(4):
    i = float(input(f'Insira a nota do {i+1} bimestre: '))
    notas_bimestrais+=i
media_bimestre = notas_bimestrais / 4
print(media_bimestre)