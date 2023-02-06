# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input('Digite seu nome: ')
    if len(nome) <= 3:
        print('Digite mais de 3 caracteres!')
        continue
    break
while True:
    try:
        idade = int(input('Informe sua Idade: '))
        if idade < 0 or idade > 150:
            print('Digite a idade entre 0 e 150 anos!')
            continue
        break
    except ValueError:
        print('Informe uma idade válida!')
while True:
    try:
        salario = float(input('Informe seu salário:R$ '))
        if salario <= 0:
            print('Digite o salario maior que zero!')
            continue
        break
    except ValueError:
        print('Informa um salário válido!')
while True:
    sexo = str(input('Informe o Genero [M/F]: ')).upper()
    if sexo in 'MF':
        break
    else:
        print('Digite M - Masculino ou F - Feminino!')
while True:
    estado_civil = str(input('Informe o Estado civil [S/C/V/D]: ')).upper()
    if estado_civil in 'SCVD':
        break
    else:
        print('Digite S-Solteiro; C-Casado; V-Viúvo ou D-Divorciado!')

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: R$ {salario:.2f}')
print(f'Genero: {sexo}')
print(f'Estado Civil: {estado_civil}')


