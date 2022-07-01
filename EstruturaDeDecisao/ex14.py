# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
# conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 9:
    print(f'Com as notas {nota1:.2f} e {nota2:.2f} a média foi de {media},'
          f' o aluno teve aproveitamento A e Conceito: APROVADO!')
elif 7.5 <= media < 9:
    print(f'Com as notas {nota1:.2f} e {nota2:.2f} a média foi de {media}, '
          f'o aluno teve aproveitamento B e Conceito: APROVADO!')
elif 6 <= media < 7.5:
    print(f'Com as notas {nota1:.2f} e {nota2:.2f} a média foi de {media}, '
          f'o aluno teve aproveitamento C e Conceito: APROVADO!')
elif 4 <= media < 6:
    print(f'Com as notas {nota1:.2f} e {nota2:.2f} a média foi de {media}, '
          f'o aluno teve aproveitamento D e Conceito: REPROVADO!')
else:
    print(f'Com as notas {nota1:.2f} e {nota2:.2f} a média foi de {media}, '
          f'o aluno teve aproveitamento E e Conceito: REPROVADO!')
    