"""
Faça um algoritmo que solicite a nota das 4 provas semestrais
do usuário. Em seguida, calcule e envie para a saída padrão a média:
"""

nota1 = float(input("Informe a nota do primeiro semestre: "))
nota2 = float(input("Informe a nota do segundo semestre: "))
nota3 = float(input("Informe a nota do terceiro semestre: "))
nota4 = float(input("Informe a nota do quarto semestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A média é igual a: %.2f" %media)
