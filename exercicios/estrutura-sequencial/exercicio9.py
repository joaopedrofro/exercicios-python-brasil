# coding: utf-8

"""
Faça um Programa que peça a temperatura em graus Farenheit, transforme
e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
"""

# Recebendo o valor da temperatura
graus_farenheit = float(input('Informe a temperatura em Farenheit: '))

# Convertendo a temperatura para graus Celsius
graus_celsius = 5 * (graus_farenheit - 32) / 9

# Imprimindo a temperatura
print('%.2f °F é igual a %.2f °C' %(graus_farenheit, graus_celsius))
