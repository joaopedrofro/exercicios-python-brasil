# coding: utf-8

"""
Faça um Programa que peça um valor e mostre
na tela se o valor é positivo ou negativo.
"""

# Recebendo um valor
valor = float(input('Informe um número: '))

# Estrutura de condição
if valor % 2 == 0:  # Se o resto da divisão do valor por 2 for iguala 0...
    # Informar que o número é positivo
    print('O número é positivo!')
else:   # Se não
    # Informar que o número é negativo
    print('O número é negativo!')