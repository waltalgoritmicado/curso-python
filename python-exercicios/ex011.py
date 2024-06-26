"""
DESAFIO 011

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e quantidade de tinta necessária para pintá-la,
sabendo que cada litro de de tinta pinta uma área de 2m²
"""

largura = float(input('Digite a largura da parede em: '))
altura = float(input('Digite a altuta da parede em: '))
calc_area = largura * altura
qnd_tinta = calc_area / 2 * 1

print(f'A área da parede em m² é: {calc_area}, serão necessários {qnd_tinta} litros de tintas para pintá-la')

