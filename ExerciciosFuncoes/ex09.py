# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(n):
    rev = int(str(n)[::-1])
    return rev


num = reverso(int(input('Informe um número: ')))
print(f'O Reverso do número informado é {num}')
