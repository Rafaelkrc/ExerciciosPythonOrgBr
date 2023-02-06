# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.
while True:
    while True:
        try:
            populacao_a = int(input('Informe a população inicial de A: '))
            populacao_b = int(input('Informe a população inicial de B: '))
            if populacao_a and populacao_b <= 0:
                print('Informe valores maiores que 0(zero)!')
                continue
            break
        except ValueError:
            print('Informe um numero inteiro!')
    while True:
        try:
            taxa_de_crescimento_a = float(input('Informe a taxa de crescimento inicial de A: '))
            taxa_de_crescimento_b = float(input('Informe a taxa de crscimento inicial de B: '))
            if taxa_de_crescimento_a and taxa_de_crescimento_b <= 0:
                print('Informe valores maiores que 0(zero)!')
                continue
            break
        except ValueError:
            print('Informe um valor percentual valido')
    anos = 0
    taxa_de_crescimento_a = (taxa_de_crescimento_a/100) + 1
    taxa_de_crescimento_b = (taxa_de_crescimento_b/100) + 1

    while populacao_a < populacao_b:
        anos += 1
        populacao_a = int(populacao_a * taxa_de_crescimento_a)
        populacao_b = int(populacao_b * taxa_de_crescimento_b)

    print(f'População de A ultrapassará a população de B em {anos} anos.')
    print(f'População de A será de {populacao_a} habitantes.')
    print(f'População de B será de {populacao_b} habitantes!')
    print()
    continua = str(input('Deseja continuar [S/N]? ')).upper()
    if continua in 'N':
        print('Obrigado!')
        break
    else:
        continue
