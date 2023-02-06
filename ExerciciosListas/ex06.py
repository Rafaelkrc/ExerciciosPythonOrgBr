# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.
soma = media = cont= 0
media_alunos = []
media_maior_que_7 = []
for i in range(10):
    for aluno in range(4):
        notas = float(input(f'Informe a {aluno + 1}° nota do {i + 1}° aluno: '))
        soma += notas
    media = soma / 4
    print(media)
    if media >= 7:
        media_maior_que_7.append(media)
    media_alunos.append(media)
    soma = 0
print(media_maior_que_7)
print(f'Os quantidade de alunos com média igual ou maior que 7 foram: {len(media_maior_que_7)}')

