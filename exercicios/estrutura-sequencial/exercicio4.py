# coding: utf-8

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# Atribuindo o VALOR informado pelo usuário à variável
# A função input pode receber um texto que será impresso antes do usuário digitar algo
nota1 = float(input("Informe a nota do primeiro bimestre: "))
nota2 = float(input("Informe a nota do segundo bimestre: "))
nota3 = float(input("Informe a nota do terceiro bimestre: "))
nota4 = float(input("Informe a nota do quarto bimestre: "))

# Cálculando a média aritimética das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Imprimindo a média das notas
print("Média: %.2f" %media)
