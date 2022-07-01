# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = float(input('Informe o 1° lado do triângulo: '))
lado2 = float(input('Informe o 2° lado do triângulo: '))
lado3 = float(input('Informe o 3° lado do triângulo: '))

if ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado2 + lado3) > lado1):
    if lado1 == lado2 == lado3:
        print('Esses valores formam um triângulo EQUILÁTERO!')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Esses valores formam um triângulo ISÓSCELES!')
    elif lado1 != lado2 != lado3:
        print('Esses valores formam um triângulo ESCALENO!')
else:
    print('Esse valores não formam um triângulo')
