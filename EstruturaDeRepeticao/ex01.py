# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.


while True:
    try:
        numero = int(input('Digite um número de 0 a 10: '))
    except ValueError:
        print('Deve ser digitado um valor inteiro!')
    else:
        if 0 <= numero <= 10:
            print(f'O número digitado foi {numero}!')
            break
        else:
            print('O número deve estar entre 0 e 10!')

