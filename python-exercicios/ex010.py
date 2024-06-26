"""
DESAFIO 010

Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos dolares ela pode comprar 
"""

d_na_carteira = float(input('Quanto dinheiro você tem na carteira? '))
conversao_dolar = d_na_carteira / 3.27

print(f'Você tem R$ {d_na_carteira} pode comprar US$ {round(conversao_dolar, 2)}')