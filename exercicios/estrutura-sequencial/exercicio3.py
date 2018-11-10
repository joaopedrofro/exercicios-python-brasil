# coding: utf-8

# Faça um Programa que peça dois números e imprima a soma.

# Atribuindo o VALOR informado pelo usuário à variável
# A função input pode receber um texto que será impresso antes do usuário digitar algo
numero1 = float(input("Informe um número: "))
# Atribuindo o VALOR informado pelo usuário à variável
# A função input pode receber um texto que será impresso antes do usuário digitar algo
numero2 = float(input("Informe outro número: "))

# Imprimindo um texto com os valores guardados nas variáveis
print("A soma entre %.2f e %f é igual a: %.2f" %(numero1, numero2, (numero1 + numero2)))
