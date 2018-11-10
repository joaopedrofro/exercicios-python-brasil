# coding: utf-8

"""
Faça um Programa para uma loja de tintas. O programa
deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 6 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 3,6 litros, que custam R$ 25,00. Informe
ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja
    o menor. Acrescente 10% de folga e sempre arredonde
    os valores para cima, isto é, considere latas cheias.
"""

area = float(input('Informe o tamanho da área a ser pintada (m²): '))

litros_tinta = area / 6

latas_tinta = litros_tinta // 18
galoes_tinta = litros_tinta // 3.6

print('Litros de tinta: {:.2f}\n\
Latas de tinta: {}\n\
Galões de tinta: {}\n\
Misturado: {}'.format(litros_tinta, latas_tinta, galoes_tinta, 0))