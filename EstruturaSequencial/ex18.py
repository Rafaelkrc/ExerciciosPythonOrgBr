# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
# Arredonde o tempo em minutos

tamanho_arquivo = int(input('Informe o tamanho do arquivo em MB: '))
velocidade = int(input('Informe a velocidade do link em Mbps: '))
tempo = (tamanho_arquivo / (velocidade / 8)) / 60
print(f'O tempo aproximado do Download é: {round(tempo)} minuto(s)')
