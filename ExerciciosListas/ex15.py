# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de
# dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

notas = []
nota_maior_media = []
notas_abaixo7 = []
soma = 0
while True:
    try:
        nota = float(input('Informe a nota do Aluno: '))
        if nota == -1:
            break
        else:
            notas.append(nota)
            soma += nota
        if nota < 7:
            notas_abaixo7.append(nota)
    except ValueError:
        print('Digite um numero Real!')
        continue
media = soma / len(notas)
for i in notas:
    if i > media:
        nota_maior_media.append(i)

print(f'Foram lidas {len(notas)} notas!')
print('As notas lidas foram: ')
print('; '.join([str(nota) for nota in notas]))
notas.reverse()
print(f'As notas informadas de forma inversa são:')
for nota in notas:
    print(nota)
print(f'A soma das notas foi de {soma}')
print(f'A média das notas foi de {media}')
print(f'As notas acima da média foram: {nota_maior_media}')
print(f'As notas abaixo de 7 foram: {notas_abaixo7}')
print('Encerrando o programa de notas! Obrigado!')


