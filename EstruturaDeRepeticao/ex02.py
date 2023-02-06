# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('Informe seu nome de usuário: ')
while True:
    senha = input('Informe sua senha: ')
    if senha == nome:
        print('Nome de usuário e senha são iguai!')
        continue
    else:
        break
print('Usuario e senha são diferentes!')
