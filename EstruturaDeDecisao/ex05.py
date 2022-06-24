# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
# aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input('Digita a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A média do aluno foi: {media}')
if 7 <= media <= 9.9:
    print('APROVADO')
elif media < 7:
    print('REPROVADO')
elif media == 10:
    print('APROVADO COM DISTINCAO!')
