# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

dia = int(input('Digito um número de 1 a 7: '))

if dia == 1:
    print('1-Domingo')
elif dia == 2:
    print('2-Segunda-Feira')
elif dia == 3:
    print('3-Terça-Feira')
elif dia == 4:
    print('4-Quarta-Feira')
elif dia == 5:
    print('5-Quinta-Feira')
elif dia == 6:
    print('6-Sexta-Feira')
elif dia == 7:
    print('7-Sábado')
else:
    print('Valor Inválido')

    