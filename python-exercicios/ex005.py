"""
DESAFIO 005

Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor
"""

n = int(input('Digite um número: '))
sucessor = n + 1
antecessor = n - 1

print(f'O número digitado foi {n}. A antecessor de {n} é {antecessor}, e seu sucessor é {sucessor}.')
