#Faça um Programa que pergunte quanto você ganha por hora e
# o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês.

salhora = float(input('Quanto você ganha por hora? R$ '))
horatrab = float(input('Quantas horas trabalha por mês? '))
salmes = salhora * horatrab
print(f'Com seu salário de R${salhora:.2f} por hora, trabalhando {horatrab:.0f} hora(s), '
      f'você receberá R${salmes:.2f} por mês.')
