# coding: utf-8

"""
Faça um Programa que verifique se uma letra
digitada é "F" ou "M". Conforme a letra
escrever: F - Feminino, M - Masculino,
Sexo Inválido.
"""

# Recebe uma string
sexo = str(input('Informe seu sexo [M/F]: '))

# Estrutura de condição
if sexo == 'M':     # Se a letra informada for igual a letra 'M'...
    # Informar que o sexo é masculino
    print('M - Masculino')
elif sexo == 'F':   # Se não, caso a letra informada for igual a letra 'F'...
    # Informar que o sexo é feminino
    print('F - Feminino')
else:   # Se nenhuma das opções é válida...
    # Informar que a opção é inválida
    print('Opção inválida')