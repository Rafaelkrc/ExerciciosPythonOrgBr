# Classe Quadrado: Crie uma classe que modele um quadrado:
#
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado=1):
        self.lado = lado

    def muda_lado(self, lado):
        self.lado = lado

    def retorna_valor_lado(self):
        return self.lado

    def calcula_area(self):
        return self.lado ** 2


quadrado = Quadrado(4)
quadrado.muda_lado(5)
print(id(quadrado))
print(quadrado.retorna_valor_lado())
print(quadrado.calcula_area())
