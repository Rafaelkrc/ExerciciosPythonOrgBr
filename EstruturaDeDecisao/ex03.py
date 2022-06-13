# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
# M - Masculino, Sexo Inválido.

sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()

if sexo == 'F':
    print('Sexo: F - Feminino')
elif sexo == 'M':
    print('Sexo: M - Masculino')
else:
    print('Sexo inválido!')
