# coding: utf-8

"""
Faça um programa para uma loja de tintas. O programa
deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 3 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total.
"""

# Recebendo o valor da área
area = float(input('Informe o tamanho da área a ser pintada (m²): '))

# Calculando os litros de tinta necessários
litros_tinta = area / 3

# Com base nos litros de tinta, calculando as latas necessárias
latas_tinta = litros_tinta // 18

print('\
Qtd. de Latas: %.0f \n\
Preço Total: R$ %.2f' %(latas_tinta, latas_tinta * 80))