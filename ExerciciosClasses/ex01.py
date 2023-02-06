# Classe Bola: Crie uma classe que modele uma bola:
#
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self):
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Papel'

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, cor):
        self.cor = cor


bola_primeiro = Bola()
bola_segunda = Bola()
bola_segunda.cor = 'Amarelo'
print(type(bola_primeiro))
print(bola_primeiro is bola_segunda)
print(id(bola_primeiro), bola_primeiro.mostra_cor())
print(id(bola_segunda), bola_segunda.mostra_cor())
print(bola_primeiro.cor, bola_segunda.cor)
