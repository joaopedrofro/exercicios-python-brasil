# coding: utf-8

"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50
quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
você faça um programa que leia a variável peso (peso de peixes) e verifique
se há excesso. Se houver, gravar na variável excesso e na variável multa o
valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis
com o conteúdo ZERO.
"""

# Recebendo o peso em kilos
peso = float(input('Informe o peso dos peixes em kg: '))

# Declarando as variáveis para que possam ser usadas fora do escopo
multa = 0
excesso = 0

# Estrutura condicional se
if peso > 50:		# Se o peso for maior que 50...
	# Cálcula o execesso e a multa
	excesso = peso - 50
	multa = excesso * 4

# Imprime os resultados
print('Excesso: %.2f kg\nMulta: R$ %.2f' %(excesso, multa))
