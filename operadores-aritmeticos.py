"""
OPERADORES
 + = adição
 - = subtração
 * = multiplicação 
 / = divisão
 ** = potência
 // = divisão inteira
 % = resto 
"""

print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(5 // 2)
print(5 % 1)

"""
Ordem de precedência
1 ()
2 **
3 * ou / ou // ou %
4 + ou -
"""

print( 5 + 3 * 2)
print( 3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)


nome = input('Qual o seu nome? ')
print(f'Prazer em te conhecer {nome:=^20}')

n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))

print(f'A soma vale {n1+n2}')
