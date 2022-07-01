# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
print('-' * 30)
print("""Escolha um Operação:
1 - Para Somar;
2 - Para Subtrair
3 - Para Multiplicar
4 - Para Dividir""")
print('-' * 30)
opcao = int(input('Informe a opção desejada: '))
resultado = 0
par_str = pos_str = int_str = ''

if opcao == 1:
    resultado = num1 + num2
elif opcao == 2:
    resultado = num1 - num2
elif opcao == 3:
    resultado = num1 * num2
elif opcao == 4:
    resultado = num1 / num2
elif opcao != 1 or 2 or 3 or 4:
    print('Opção inválida! Tente novamente!')

if resultado % 2 == 0:
    par_str = 'par'
else:
    par_str = 'impar'

if resultado >= 0:
    pos_str = 'positivo'
else:
    pos_str = 'negativo'

if int(resultado) == resultado:
    int_str = 'inteiro'
else:
    int_str = 'decimal'

print(f'O resultado da opçao foi {resultado} e é um numero {par_str}, {pos_str} e {int_str}!')
