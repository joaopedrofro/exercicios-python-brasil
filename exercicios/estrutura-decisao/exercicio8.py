# coding: utf-8

"""
Faça um programa que pergunte o preço de três
produtos e informe qual produto você deve
comprar, sabendo que a decisão é sempre
pelo mais barato.
"""

# Recebendo os valores
produto1 = float(input('Informe o preço do produto 1: '))
produto2 = float(input('Informe o preço do produto 2: '))
produto3 = float(input('Informe o preço do produto 3: '))

# Estrutura de condição
if produto2 >= produto1 <= produto3:
    print('Compre o Produto 1!')
elif produto1 >= produto2 <= produto3:
    print('Compre o Produto 2!')
elif produto1 >= produto3 <= produto2:
    print('Compre o Produto 3!')