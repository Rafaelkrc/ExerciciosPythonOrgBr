#João Papo-de-Pescador, homem de bem, comprou um
# microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido
# pelo regulamento de pesca do estado de São Paulo (50 quilos) deve
# pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
# você faça um programa que leia a variável peso (peso de peixes) e
# calcule o excesso. Gravar na variável excesso a quantidade de quilos
# além do limite e na variável multa o valor da multa que João deverá
# pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Informe o peso dos peixes em KG: '))
excesso = peso - 50
multa = excesso * 4

if excesso <= 0:
    print(f'Você pescou hoje {peso:.2f}Kg de peixe: VOCÊ FICOU DENTRO DO LIMITE!')
else:
    excesso > 0
    print(f'Você excedeu o limite de pesca de 50kg em {excesso:.2f}kg,\n'
          f'esse excesso lhe custará R${multa:.2f}.')
