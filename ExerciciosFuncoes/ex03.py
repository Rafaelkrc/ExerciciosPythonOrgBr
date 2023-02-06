# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def numeros(a, b, c: int):
    soma = a + b + c
    print(f'A soma dos argumentos são: {soma}')


numeros(10, 20, 30)
