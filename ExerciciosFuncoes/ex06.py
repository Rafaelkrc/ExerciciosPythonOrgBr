# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa
# deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
# uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’
# para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def conversao_de_horas(horas, minutos):
    if horas > 12:
        converte = hora - 12
        periodo = 'P'
        resultado(converte, minutos, periodo)
    else:
        converte = horas
        periodo = 'A'
        resultado(converte, minutos, periodo)


def resultado(h, m, p):
    if p == 'P':
        print(f'{h}:{m} P.M.')
        return
    else:
        print(f'{h}:{m} A.M.')
        return


while True:
    while True:
        hora = int(input('Informe a hora: '))
        if 0 <= hora <= 23:
            break
        else:
            print('Digite um valor entre 0 e 23!')
            continue
    while True:
        minuto = int(input('Informe o minuto: '))
        if 0 <= minuto <= 59:
            break
        else:
            print('Digite um valores entre 0 e 59!')

    conversao_de_horas(hora, minuto)
    hora_convertida = resultado
    print()
    opcao = str(input('Deseja continuar [S/N]? ')).upper()
    if opcao in 'N':
        print('Ate Logo!')
        break
    else:
        continue
