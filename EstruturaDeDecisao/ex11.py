# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para
# desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado
# no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Informe o salario do colaborador: R$ '))

if salario <= 280:
    aumento = salario * 0.2
    print(f'O Salário de R${salario:.2f} teve um aumento de 20% no valor de R${aumento:.2f} e o novo salário será de R${salario + aumento:.2f}')
elif 280 < salario <= 700:
    aumento = salario * 0.15
    print(f'O Salário de R${salario:.2f} teve um aumento de 15% no valor de R${aumento:.2f} e o novo salário será de R${salario + aumento:.2f}')
elif 700 < salario <= 1500:
    aumento = salario * 0.1
    print(f'O Salário de R${salario:.2f} teve um aumento de 10% no valor de R${aumento:.2f} e o novo salário será de R${salario + aumento:.2f}')
else:
    aumento = salario * 0.05
    print(f'O Salário de R${salario:.2f} teve um aumento de 5% no valor de R${aumento:.2f} e o novo salário será de R${salario + aumento:.2f}')
