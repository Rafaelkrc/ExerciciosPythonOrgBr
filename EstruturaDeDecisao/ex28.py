# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
# cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
# e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
print('-' * 30)
print('''Selecione o Produto:

1 - File Duplo
2 - Alcatra
3 - Picanha''')
print('-' * 30)

produto = int(input('Informe o produto: '))
qtd = float(input('Informe o peso em Kg: '))
total = 0
if produto == 1:
    produto = 'File Duplo'
    if qtd <= 5:
        total = qtd * 4.9
    else:
        total = qtd * 5.8

elif produto == 2:
    produto = 'Alcatra'
    if qtd <= 5:
        total = qtd * 5.9
    else:
        total = qtd * 6.8

elif produto == 3:
    produto = 'Picanha'
    if qtd <= 5:
        total = qtd * 6.9
    else:
        total = qtd * 7.8

print('-' * 30)
print('''Forma de Pagamento
1-Dinheiro
2-Cheque
3-Cartão
4-Cartão Tabajara
5-Pix''')
print('-' * 30)
forma = int(input('Forma de pagamento: '))
desconto = 0
totaldes = 0
if forma == 1:
    forma = 'Dinheiro'
elif forma == 2:
    forma = 'Cheque'
elif forma == 3:
    forma = 'Cartao'
elif forma == 4:
    forma1 = 'Cartao Tabajara'
    desconto = total * 0.05
    totaldes = total - desconto
elif forma == 5:
    forma = 'Pix'
else:
    print('Digite uma forma de pagamento Válida!')
print('-' * 40)
print(f'{"HIPERMERCADO TABAJARA":^40}')
print('-' * 40)
print(f'{"Qtdade":<10}{"Descrição":23}{"TOTAL":>7}')
print('-' * 40)
print(f'{qtd:<10.2f}{produto:23}{total:>7.2f}')

if forma == 4:
    print(f'{"Desconto: (5%)":<33}{desconto:>7.2f}')
    print(f'{"Total:":<33}{totaldes:>7.2f}')
    print('-' * 40)
    print(f'{"Forma de pagamento:":<25}{forma1:>7}')
    print('-' * 40)
    print(f'{"OBRIGADO PELA PREFERENCIA!":^40}')
    print(f'{"VOLTE SEMPRE":^40}')
    print('-' * 40)
else:
    print(f'{"Total:":<33}{total:>7.2f}')
    print('-' * 40)
    print(f'{"Forma de pagamento:":<33}{forma:>7}')
    print('-' * 40)
    print(f'{"OBRIGADO PELA PREFERENCIA!":^40}')
    print(f'{"VOLTE SEMPRE":^40}')
    print('-' * 40)

