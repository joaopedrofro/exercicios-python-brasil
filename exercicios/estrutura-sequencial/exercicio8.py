# coding: utf-8

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

# Recebendo os valores para o cálculo do salário
valor_hora = float(input('Informe o valor da hora de trabalho: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas: '))

# Calculando o salário
salario = valor_hora * horas_trabalhadas

# Imprimindo o salário
print('Salário do mês: R$ %.2f' %salario)
