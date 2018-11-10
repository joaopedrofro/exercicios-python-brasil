# coding: utf-8

"""
Faça um programa que peça o tamanho de um arquivo
para download (em MB) e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo aproximado
de download do arquivo usando este link (em minutos).
"""

# Recebendo os dados para cálculo
tamanho_arquivo = float(input('Informe o tamanho do arquivo (MB): '))
velocidade_link = float(input('Informe a velocidade do link de download (Mbps): '))

# Calculando o tempo de download em minutos
tempo_download = ((tamanho_arquivo * 8) / velocidade_link) / 60

# Imprimindo o tempo de download em minnutos
print('Tempo de download: %.0f minutos' %tempo_download)