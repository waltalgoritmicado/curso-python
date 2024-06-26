"""
DESAFIO 006

Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.
"""

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz_quadrada = n ** (1/2)

# pow para calcular a raiz quadrada pow(n, (1/2))

print(f'O dobro de {n} é {dobro}, o triplo é {triplo} e a raiz_quadrada é {round(raiz_quadrada, 2)}')