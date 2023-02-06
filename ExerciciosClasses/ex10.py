# Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
#
# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# tipoCombustivel.
# valorLitro
# quantidadeCombustivel
# Possua no mínimo esses métodos:
# abastecerPorValor()– método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi
# colocada no veículo
# abastecerPorLitro()– método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago
# pelo cliente.
# alterarValor()– altera o valor do litro do combustível.
# alterarCombustivel()– altera o tipo do combustível.
# alterarQuantidadeCombustivel()– altera a quantidade de combustível restante na bomba.
# OBS:Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.


class BombaCombustivel:
    def __init__(self, tipocombustivel: str, valorlitro: float, quantidadecombustivel: float):
        self.tipocombustivel = tipocombustivel
        self.valorlitro = valorlitro
        self.quantidadecombustivel = quantidadecombustivel

    def abastecerporvalor(self, valor):
        litros_abatecidos = valor / self.valorlitro
        self._mostrar_abatecimento_se_possivel(litros_abatecidos, valor)

    def _mostrar_abatecimento_se_possivel(self, litros_abastecidos, valor):
        if litros_abastecidos > self.quantidadecombustivel:
            print(f'Não é possível abastercer, faltam {litros_abastecidos - self.quantidadecombustivel} litros.')
            print('Reabasteça a bomba!')
        else:

            self.quantidadecombustivel -= litros_abastecidos
            print(f'Foram abastecidos {litros_abastecidos:.2f} litros de a um valor de R$ {valor:.2f} {self.tipocombustivel}.')
            print(f'Sobraram na bomba {self.quantidadecombustivel:.2f} litros de {self.tipocombustivel}.')

    def abastecerporlitro(self, litros_abastecidos: float):
        valor = litros_abastecidos * self.valorlitro
        self._mostrar_abatecimento_se_possivel(litros_abastecidos, valor)

    def adicionar_combustivel(self, litros: float):
        if litros >= 0:
            self.quantidadecombustivel += litros
        else:
            print('Não pode roubar combustivel da bomba, Malandrinho!')


bomba = BombaCombustivel('Gasolina', 5, 100)

bomba.abastecerporvalor(100)
bomba.abastecerporlitro(50)
bomba.valorlitro = 6
bomba.abastecerporlitro(50)
bomba.adicionar_combustivel(75)
bomba.abastecerporlitro(50)

bomba.adicionar_combustivel(-5)
