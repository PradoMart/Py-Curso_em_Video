#AULA 13 - LAÇO DE REPETIÇÃO FOR

#47 - NÚMEROS PARES
from time import sleep
print('')

inicio = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))
print('')

for numeros in range(inicio,fim+1):
    if numeros % 2 == 0:
        print(numeros, end=', ')
print('FIM!')
