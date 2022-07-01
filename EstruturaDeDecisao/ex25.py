# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
# "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será
# classificado como "Inocente".

perg = 'N'
cont = 0
for p in perg:
    perg = str(input('Telefonou para a vítima? [S/N]: ')).upper()
    if perg == 'S':
        cont += 1
    perg = str(input('Esteve no local do crime? [S/N]: ')).upper()
    if perg == 'S':
        cont += 1
    perg = str(input('Mora perto da vítima? [S/N]: ')).upper()
    if perg == 'S':
        cont += 1
    perg = str(input('Devia para a vítima? [S/N]: ')).upper()
    if perg == 'S':
        cont += 1
    perg = str(input('Já trabalhou com a vítima? [S/N]: ')).upper()
    if perg == 'S':
        cont += 1
    if cont == 2:
        print('Suspeito!')
    elif 3 <= cont <= 4:
        print('Cumplice!')
    elif cont == 5:
        print('Culpado!')
    else:
        print('Inocente!')
