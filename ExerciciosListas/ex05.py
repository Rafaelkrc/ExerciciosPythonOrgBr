# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
# PAR e os números IMPARES no vetor impar. Imprima os três vetores.

inteiros = []
par = []
impar = []

try:
    for i in range(20):
        numeros = int(input(f'Informe o {i + 1}° numero: '))
        inteiros.append(numeros)
        if numeros % 2 == 0:
            par.append(numeros)
        else:
            impar.append(numeros)
except ValueError:
    print('Digite somente numeros inteiros!')

print('Os números digitados foram:')
print(', '.join([str(int) for int in inteiros]))
print()
print('Os numeros pares digitados foram:')
print(', '.join([str(pares) for pares in par]))
print()
print('Os números impares digitados foram:')
print(', '.join([str(impares) for impares in impar]))
