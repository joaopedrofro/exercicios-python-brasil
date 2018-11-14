# Coding: utf-8

# Faça um Programa que peça dois números e imprima o maior deles.

# Recebendo os valores
num1 = float(input('Informe um número: '))
num2 = float(input('Informe outro número: '))

# Estrutura de condição se/if
if num1 > num2:     # Se o primeiro número informado for maior que o segundo...
    # Imprimir o primeiro número
    print(num1)
else:               # Se não...
    # Imprimir o segundo número
    print(num2)