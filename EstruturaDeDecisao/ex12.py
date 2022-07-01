# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
# descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

linha = '=' * 40
cabecalho = 'FOLHA DE PAGAMENTO'

vlrhora = float(input('Informe o valor de sua hora trabalhada:R$ '))
hrtrab = float(input('Informe a quantidade de horas trabalhadas no mês: '))
salario = vlrhora * hrtrab
fgts = salario * 0.11
inss = salario * 0.10
sindicato = salario * 0.03

ir = 0
irperc = ''
if salario <= 900:
    ir = 0
    irperc = 'ISENTO'
elif salario <= 1500:
    ir = salario * 0.05
    irperc = '5%'
elif salario <= 2500:
    ir = salario * 0.10
    irperc = '10%'
else:
    ir = salario * 0.20
    irperc = '20%'

totaldesconto = ir + inss + sindicato
salarioliquido = salario - totaldesconto

print(linha)
print(cabecalho.center(40))
print(linha)
print(f'   Salário Bruto: ({vlrhora:.0f}x{hrtrab:.0f})\t :R$ {salario:.2f}')
print(f'   (-)IR {irperc}\t\t\t\t\t :R$   {ir:.2f}')
print(f'   (-)INSS (10%)\t\t\t :R$  {inss:.2f}')
print(f'   (-)Sindicato (3%)\t\t :R$   {sindicato:.2f}')
print(f'   FGTS (11%)\t\t\t\t :R$  {fgts:.2f}')
print(f'   Total de desconto\t\t :R$  {totaldesconto:.2f}')
print(f'   Salário Líquido\t\t\t :R$  {salarioliquido:.2f}')
print(linha)
