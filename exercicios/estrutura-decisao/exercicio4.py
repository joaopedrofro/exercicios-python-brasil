# coding: utf-8

"""
Faça um Programa que verifique se uma
letra digitada é vogal ou consoante
"""

# Recebendo uma string
letra = str(input('Informe uma letra: '))

# Estrutura de condição
if letra in ('a', 'e', 'i', 'o', 'u'):  # Se a letra está contida na lista de letras...
    # Informar que a letra é uma vogal
    print('É uma vogal!')
else:   # Se não estiver...
    # Informar que a letra é uma consoante
    print('É uma consoante!')