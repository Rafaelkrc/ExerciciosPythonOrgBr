# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
#
# FULANO
# FULAN
# FULA
# FUL
# FU
# F

nome = input('Digite seu nome: ').upper()

while nome != '':
    print(nome)
    nome = nome[:-1]
