# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
#
# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!
#
# Digite uma letra: O
# A palavra é: _ _ _ _ O
#
# Digite uma letra: E
# A palavra é: _ E _ _ O
#
# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

palavra = 'Rafael'.upper()

print('Jogo da Forca!')
print('Descubra a palavra!')
print()

print('A palavra é: ', end='')
for letras in palavra:
    print('_ ', end='')

conjunto_de_palavras = set(palavra)
conjunto_de_letras_digitadas = set()
erro = 0

while (not conjunto_de_palavras.issubset(conjunto_de_letras_digitadas)) and erro < 7:
    print()
    print()
    letras_digitadas = input('Digite uma letra: ').upper()
    conjunto_de_letras_digitadas.add(letras_digitadas)
    if letras_digitadas in conjunto_de_palavras:
        print('A palavra é: ', end='')
        for letras in palavra:
            if letras in conjunto_de_letras_digitadas:
                print(f'{letras} ', end='')
            else:
                print('_ ', end='')
    else:
        erro += 1
        print(f'-> Você errou pela {erro}ª vez. Tente de novo!')

print()
if erro < 7:
    print('Parabéns você GANHOU!!!')
else:
    print('Você PERDEU! Até a próxima!')
