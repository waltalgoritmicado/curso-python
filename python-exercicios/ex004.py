"""
  Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele
"""

algo = input('Digite algo: ')
print(type(algo))
print(f'{algo} é aplhanúmerico?')
print(algo.isalpha())
print(f'{algo} é númerico?')
print(algo.isnumeric())
print(f'{algo} é UPPERCASE')
print(algo.isupper())
print(f'{algo} é space')
print(algo.isspace())