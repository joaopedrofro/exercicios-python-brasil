# coding: utf-8

"""
Faça um Programa que calcule a área de um quadrado, em seguida
mostre o dobro desta área para o usuário.
"""

# Recebendo o valor da área do quadrado
lado = float(input('Informe o valor do lado do quadrado em cm: '))

# Calculando e atribuindo a área do quadrado
dobro_area = lado**2 * 2

# Imprimindo  área do quadrado
print('O dobro da área do quadrado é: %.2f cm²' %(dobro_area))
