# coding: utf-8

# Faça um Programa que leia três números e mostre o maior deles.

# Recebendo os números
num1 = float(input('Informe um número: '))
num2 = float(input('Informe outro número: '))
num3 = float(input('Informe mais um número: '))

# Estrutura de condição
if num2 <= num1 >= num3:    # Se o primeiro número for maior ou igual que o segundo e o terceiro
    # Informar que o primeiro número é o maior
    print('Maior:', num1)
elif num1 <= num2 >= num3:  # Se o segundo número for maior ou igual que o primeiro e o terceiro
    # Informar que o segundo número é o maior
    print('Maior:', num2)
elif num1 <= num3 >= num2:  # Se o terceiro número for maior ou igual que o primeiro e o segundo
    # Informar que o terceiro número é o maior
    print('Maior:', num3)