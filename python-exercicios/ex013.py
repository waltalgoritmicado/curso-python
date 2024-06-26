"""
DESAFIO 013

Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo sálario com 15% de aumento
"""

salario = float(input('Qual o seu sálario atual? '))
calc_aumento_salario = salario * 0.15
novo_salario = salario + calc_aumento_salario
print(f'O seu salário era de R$ {round(salario, 2)}, teve um aumento de {round(calc_aumento_salario, 2)}, agora o seu salário é de R$ {round(novo_salario, 2)} ')