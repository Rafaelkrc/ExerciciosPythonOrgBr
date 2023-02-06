# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor
# que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos
# seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

salarios = []
while True:
    try:
        venda_bruta = int(input('Informe a venda bruta:R$ '))
        comissao = 200 + (venda_bruta * 0.09)
        salarios.append(comissao)
        opcao = str(input('Deseja informar o próximo vendedor [S/N]? ')).upper()
        if opcao == 'N':
            print()
            print('Obrigado!')
            print()
            break
    except ValueError:
        print('Informe um valor válido!')
        continue

contagem_faixa_salarial = [0] * 9
for salario in salarios:
    indice = int(salario // 100 - 2)
    indice_maximo = len(contagem_faixa_salarial) - 1
    indice = min(indice, indice_maximo)
    contagem_faixa_salarial[indice] += 1

print(f'Número de vendedores no intervalo entre $200 - $299 --> '
      f'{len([str(valor) for valor in salarios if 200 <= valor <= 299])}')
print(f'Número de vendedores no intervalo entre $300 - $399 --> '
      f'{len([str(valor) for valor in salarios if 300 <= valor <= 399])}')
print(f'Número de vendedores no intervalo entre $400 - $499 --> '
      f'{len([str(valor) for valor in salarios if 400 <= valor <= 499])}')
print(f'Número de vendedores no intervalo entre $500 - $599 --> '
      f'{len([str(valor) for valor in salarios if 500 <= valor <= 599])}')
print(f'Número de vendedores no intervalo entre $600 - $699 --> '
      f'{len([str(valor) for valor in salarios if 600 <= valor <= 699])}')
print(f'Número de vendedores no intervalo entre $700 - $799 --> '
      f'{len([str(valor) for valor in salarios if 700 <= valor <= 799])}')
print(f'Número de vendedores no intervalo entre $800 - $899 --> '
      f'{len([str(valor) for valor in salarios if 800 <= valor <= 899])}')
print(f'Número de vendedores no intervalo entre $900 - $999 --> '
      f'{len([str(valor) for valor in salarios if 900 <= valor <= 999])}')
print(f'Número de vendedores acima de $1000 --> '
      f'{len([str(valor) for valor in salarios if valor >= 1000])}')
