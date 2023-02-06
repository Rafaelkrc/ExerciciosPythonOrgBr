# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def conta_numero(n):
    tam = len(n)
    return tam


num = conta_numero(str(input('Informe um número inteiro: ')))
print(f'O número informado tem {num} caracteres')