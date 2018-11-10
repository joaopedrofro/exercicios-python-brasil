# coding: utf-8

"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""

# Recebendo o valor da altura
altura = float(input('Informe sua altura: '))

# Calculando o peso ideal
peso_ideal = 72.7 * altura - 58

print('Peso ideal: %.2f Kg' %peso_ideal)
