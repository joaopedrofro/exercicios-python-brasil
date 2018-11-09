"""
Faça um algoritmo que solicite ao usuário informar 2 números.
Em seguida, some os valores e envie para a saída padrão a
seguinte frase: "A soma entre <X> e <Y> é igual <total>".
"""

num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))

print("A soma entre %.2f e %.2f é igual a %.2f" %(num1, num2, (num1 + num2)))
