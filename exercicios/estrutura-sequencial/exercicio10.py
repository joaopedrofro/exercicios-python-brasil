# coding: utf-8

"""
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.
"""

# Recebendo o valor da temperatura
graus_celsius = float(input('Informe a temperatura em Celsius: '))

# Convertendo a temperatura para graus Farenheit
graus_farenheit = ((graus_celsius * 9) / 5) - 32

# Imprimindo a temperatura
print('%.2f °C é igual a %.2f °F' %(graus_celsius, graus_farenheit))
