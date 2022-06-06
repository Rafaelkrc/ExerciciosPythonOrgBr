#Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Informe sua altura: '))
pesoIdeal = (72.7 * altura) - 58
print(f'Pela sua altura de {altura:.2f}mt seu peso Ideal seria: {pesoIdeal:.2f}kg')
