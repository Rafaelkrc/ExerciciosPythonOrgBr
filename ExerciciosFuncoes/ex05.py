# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaimposto(taxaimposto, custo):
    taxaimpostodecimal = taxaimposto / 100
    novo_custo = (taxaimpostodecimal * custo) + custo
    print(f'O Novo custo é de R${novo_custo:.2f}')


somaimposto(50, 100)
