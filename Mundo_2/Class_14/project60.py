#AULA 14 - LAÇO DE REPETIÇÃO WHILE

#60 - FATORIAL, não consegui fazer sozinho
print('')
print('--- FATORIAL ---')
print('')

num = int(input('Qual número deseja fatorar? '))
contador = num
fatorial = 1
print('')
print(f'Calculando {num}! = ', end='')

'''while contador > 0:
    print(f'{contador}', end= '')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -=1
print(fatorial)'''

'''
    Eu não tava conseguindo, pq eu tava colocando o valor da variável fatorial = 0. O número nulo pra multiplicação deve ser = 1.
    A questão da multiplicação eu tbm me embananei todo. 
    
    Dá pra importar a biblioteca from math import factorial.
'''

# FAZENDO COM FOR

for f in range(contador, 0, -1):
    print(f, end='')
    print(' x ' if f > 1 else ' = ', end='')
    fatorial *= f
print(fatorial)

