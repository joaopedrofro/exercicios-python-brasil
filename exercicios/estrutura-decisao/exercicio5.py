# coding: utf-8

"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

# Recebendo as notas
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

# Calculando a média
media = (nota1 + nota2) / 2

# Estrutura de condição
if media >= 7 and media < 10:   # Se a média for maior ou igual a 7 e menor que 10...
    # Informar que o aluno está aprovado
    print('Aprovado')
elif media == 10:   # Se a média for igual a 10...
    # Informar que o aluno está aprovado com distinção
    print('Aprovado com Distinção')
elif media < 7 and media >= 0:  # Se a média for menor que 7 e maior ou igual a 0...
    # Informar que o aluno está reprovado
    print('Reprovado')