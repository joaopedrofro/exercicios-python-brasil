# coding: utf-8

"""
Faça um Programa que leia três números
e mostre o maior e o menor deles.
"""

# Recebendo os números
num1 = float(input('Informe um número: '))
num2 = float(input('Informe outro número: '))
num3 = float(input('Informe mais um número: '))

# Estrutura de condição
# Se o primeiro número for maior ou igual que o segundo e o terceiro...
if num2 <= num1 >= num3:
    # Informar que o primeiro número é o maior
    print('Maior:', num1)
    # Se o segundo número for menor ou igual ao terceiro...
    if num2 <= num3:
        # Informar que o segundo número é o menor
        print('Menor:', num2)
    # Se não...
    else:
        # Informar que o terceiro número é o menor
        print('Menor:', num3)
# Se o segundo número for maior ou igual que o primeiro e o terceiro...
elif num1 <= num2 >= num3:
    # Informar que o segundo número é o maior
    print('Maior:', num2)
    # Se o primeiro número for menor ou igual ao terceiro...
    if num1 <= num3:
        # Informar que o primeiro número é o menor
        print('Menor:', num1)
    # Se não...
    else:
        # Informar que o terceiro número é o menor
        print('Menor:', num3)
# Se o terceiro número for maior ou igual que o primeiro e o segundo...
elif num1 <= num3 >= num2:
    # Informar que o terceiro número é o maior
    print('Maior:', num3)
    # Se o primeiro número é menor ou igual ao segundo
    if num1 <= num2:
        # Informar que o primeiro número é o menor
        print('Menor:', num1)
    else:
        # Informar que o terceiro número é o menor
        print('Menor:', num3)