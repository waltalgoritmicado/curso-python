"""
  Primeiros comandos Python
"""
print("Óla Mundo")
print('Hello World')


# Variáveis
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
peso = input('Qual o seu peso? ')
altura = input('Qual a sua altura? ')

print(nome, idade, peso, altura)


# Desafios
# Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado
print('Desafios')
user_name = input('Qual o seu nome? ')
print(f'Olá {user_name}! Prazer em te conhecer.')


# Crie um script em python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada
dia = 11
mes = 'Abril'
ano = 2005
print(f'Você nasceu no {dia} de {mes} de {ano}. Correto?')

# Crie um script em Python que leia dos números e tenta mostrar a soma entre eles
first_number = input('Digite o primeiro valor: ')
last_number = input('Digite o segundo valor: ')
soma = int(last_number) + int(first_number)
print(soma)