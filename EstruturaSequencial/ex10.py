#Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit.


tempC = float(input('Informe a temperatura em graus Celsius(°C): '))
tempF = ((tempC * 9/5) + 32)
print(f'A temperatura {tempC:.2f}°C equivale a {tempF:.2f}°F.')
