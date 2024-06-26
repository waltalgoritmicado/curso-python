"""
DESAFIO 008

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

valor_m = float(input('Digite uma distância em m: '))
covnersao_em_km = valor_m / 1000
conversao_em_hm = valor_m / 100
conversao_em_dam = valor_m / 10
conversao_em_dm = valor_m * 10
conversao_em_cm = valor_m * 100
conversao_em_mm = valor_m * 1000 

print(f'{valor_m} m equivale a {round(conversao_em_cm, 2)} cm e {round(conversao_em_mm, 2)} mm')

print(f'{valor_m} em todas as medidas\n{covnersao_em_km} km\n{conversao_em_hm} hm\n{conversao_em_dam} dam\n{conversao_em_dm} dm\n{conversao_em_cm} cm\n{conversao_em_mm} mm')