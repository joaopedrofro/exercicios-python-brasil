"""
Faça um algoritmo em que o usuário informe uma medida em metros. Em seguida,
converta essa medida para centímetros e envie para a saída padrão:
"""

metros = float(input("Informe uma medida em metros: "))

print("%f metros é igual a %.2f centímetros" %(metros, (metros*100)))