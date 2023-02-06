# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
#
# F
# FU
# FUL
# FULA
# FULAN
# FULANO


nome = input('Digite seu nome: ').upper()
t = len(nome)
for c in range(t):
    print(nome[:c + 1])
