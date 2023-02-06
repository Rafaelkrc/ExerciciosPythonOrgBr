# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = []
while len(lista) < 10:
    try:
        num = str(input('Informe uma letra: ')).lower()
        if num.isalpha():
            lista.append(num)
        else:
            print('Informe uma letra!')
            continue
    except ValueError:
        print('Digite uma letra válida!')
        continue
consoantes = []
cont = 0
for c in lista:
    if c not in 'aeiou':
        cont += 1
        consoantes.append(c)
print(f'Foram lidas {cont} consoantes')
print(f'As consoantes informadas foram:')
print(', '.join([str(cons) for cons in consoantes]))
