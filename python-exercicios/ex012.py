"""
DESADIO 012

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
"""

preco_produto = float(input('Qual o preço do produto R$: '))
calc_desconto_produto = preco_produto * 0.05
novo_preco = preco_produto - calc_desconto_produto

print(f'O produto que custa R$ {preco_produto} com desconto de 5%, custa R$ {round(novo_preco, 2)}')
