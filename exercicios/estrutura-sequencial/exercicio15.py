# coding: utf-8

"""
Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total
do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:
	a. salário bruto.
	b. quanto pagou ao INSS.
	c. quanto pagou ao sindicato.
	d. o salário líquido.
	e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
		+ Salário Bruto : R$
		- IR (11%) : R$
		- INSS (8%) : R$
		- Sindicato ( 5%) : R$
		= Salário Liquido : R$
"""

# Recebendo os dados para o cálculo
valor_hora = float(input('Informe quanto você ganha por hora trabalhada: '))
horas = float(input('Informe quantas horas você trabalhou no mês: '))

# Cáculo do salário bruto
sl_bruto = valor_hora * horas

# Calculando os impostos
ir = sl_bruto * 0.11
inss = sl_bruto * 0.08
sind = sl_bruto * 0.05

# Imprimindo os resultados
print('\
+ Salário Bruto: R$ %.2f\n\
- IR (11%%): R$ %.2f\n\
- INSS (8%%): R$ %.2f\n\
- Sindicato (5%%): R$ %.2f\n\
= Salário Líquido: R$ %.2f' %(sl_bruto, ir, inss, sind, (sl_bruto - ir - inss - sind)))
