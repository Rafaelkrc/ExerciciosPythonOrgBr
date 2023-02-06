# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256
# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
#
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256
def validar(ip: str) -> bool:
    numeros = ip.split('.')

    if len(numeros) != 4:
        return False

    for num in numeros:
        if not (0 <= int(num) <= 255):
            return False
    return True


ips_validos = []
ips_invalidos = []
with open('P:\ExerciciosPython\ExerciciosArquivos\ips.txt', 'r') as arquivo:
    for linha in arquivo:
        ip = linha.strip()
        if validar(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)


with open('P:\ExerciciosPython\ExerciciosArquivos\ips_lista.txt', 'w') as arquivo:
    arquivo.writelines('[Endereços válidos:]\n')
    for ips in ips_validos:
        arquivo.writelines(f'{ips}\n')

    arquivo.writelines('\n')
    arquivo.writelines('\n')
    arquivo.writelines('[Endereços inválidos:]\n')
    for ips in ips_invalidos:
        arquivo.writelines(f'{ips}\n')
