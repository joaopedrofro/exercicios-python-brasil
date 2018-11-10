# coding: utf-8

"""
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
	a. Para homens: (72.7*h) - 58
	b. Para mulheres: (62.1*h) - 44.7 (h = altura)
	c. Peça o peso da pessoa e informe se ela está dentro,
	acima ou abaixo do peso.
"""

# Recebendo os valores para cálculo
altura = float(input('Informe sua altura: '))
sexo = input('Informe seu sexo(m/f): ')

# Declarando a variável antes do cálculo para poder utiliza-la fora do escpopo
peso_ideal = 0

# Estrutura e condição 'se'
if sexo == 'f':		# Se o sexo for igual a feminino...
	# Fórmula do peso ideal para o sexo feminino
	peso_ideal = (62.1 * altura) - 44.7
elif sexo == 'm':	# Se não, verificar se o sexo é igual a masculino
	# Fórmula do peso ideal para o sexo masculino
	peso_ideal = (72.7 * altura) - 58

# Imprimindo o peso ideal com base no sexo
print('Peso ideal: {:.2f} kg'.format(peso_ideal))
