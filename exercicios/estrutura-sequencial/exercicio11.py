# coding: utf-8

"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
	a. o produto do dobro do primeiro com metade do segundo .
	b. a soma do triplo do primeiro com o terceiro.
	c. o terceiro elevado ao cubo.
"""

# Recebendo os valores das variáveis
num_int = int(input('Informe um número inteiro: '))
num_int2 = int(input('Informe outro número inteiro: '))
num_real = float(input('Informe um número real: '))

# Calculando e imprimindo o resultado
print('Item a: {}'.format((2 * num_int) * (num_int2 / 2)))
print('Item b: {}'.format((3 * num_int) + num_real))
print('Item c: {:.2f}'.format(num_real**3))
