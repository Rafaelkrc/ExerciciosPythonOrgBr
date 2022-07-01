# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
# os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
# demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math
a = float(input('Informe o valor de A: '))
if a == 0:
    print('Quando a é igual a zero não é uma equação do segundo grau!')
else:
    b = float(input('Informe o valor de B: '))
    c = float(input('Informe o valor de C: '))
    d = (b**2) - (4 * a * c)
    if d < 0:
        print('A equação não possui raízes reais.')
    elif d == 0:
        x1 = (-b + d ** (1 / 2)) / (2 * a)
        x2 = (-b - d ** (1 / 2)) / (2 * a)
        if x1 > 0:
            print(f'A equação possui apenas uma raiz real que para x1 é {x1}')
        elif x2 > 0:
            print(f'A equação possui apenas uma raiz real que para x2 é {x2}')
    elif d > 0:
        x1 = (-b + d**(1/2)) / (2*a)
        x2 = (-b - d**(1/2)) / (2*a)
        print(f'A raiz de x1 é {x1}')
        print(f'A raiz de x2 é {x2}')
