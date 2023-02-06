# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para
# a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa
# deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de
# prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa
# deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no
# dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorpagamento(v, d):
    if d == 0:
        valor = v
        return valor
    else:
        juros = (v * 0.001) * d
        multa = v * 0.03
        valor = v + juros + multa
        return valor


cont = soma = 0
while True:
    prestacao = float(input('Informe o valor da prestação ou 0(zero) para sair: '))
    if prestacao == 0:
        break
    else:
        dias = int(input('Informe quantidade de dias vencidos: '))
        valortotal = valorpagamento(prestacao, dias)
        cont += 1
        soma += prestacao
        print(f'O valor total da prestação foi de R$: {valortotal:.2f}')

print()
print(f'Foram {cont} prestaçoes pagas no valor total de R${soma}')
