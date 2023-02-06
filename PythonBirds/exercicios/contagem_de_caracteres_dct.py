def contar_caracteres(s):
    """Função para contar os caracteres de uma string

    Ex:

    >>> contar_caracteres('coelho')
    {'c': 1, 'e': 1, 'h': 1, 'l': 1, 'o': 2}
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}


    :param s: string a ser contada

    """
    ordenar = sorted(s)
    resultado = {}

    for caracter in ordenar:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado


if __name__ == '__main__':
    print(contar_caracteres('coelho'))
    print()
    print(contar_caracteres('banana'))
