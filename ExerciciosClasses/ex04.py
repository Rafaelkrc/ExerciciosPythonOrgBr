# Classe Pessoa: Crie uma classe que modele uma pessoa:
#
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome='A', idade=1, peso=1, altura=1):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        return self.idade

    def engordar(self, peso):
        self.peso += peso
        return self.peso

    def emagrecer(self, peso):
        self.peso -= peso
        return self.peso

    def crescer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1


pessoa = Pessoa('Rafael', 10, 60, 170)
print(pessoa.nome, pessoa.idade, pessoa.altura, pessoa.peso)

for _ in range(22):
    pessoa.crescer()
    print(f'Idade de {pessoa.nome} é: {pessoa.idade} anos. E sua Altura é {pessoa.altura} cm.')

