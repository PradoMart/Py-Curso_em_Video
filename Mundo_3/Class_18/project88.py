#AULA 18 - VARIÁVEIS COMPOSTAS -- LISTAS ANINHADAS []

#88 - LISTAS, MEGASENA
from random import sample
from time import sleep
print()
print('NÚMEROS ALEATÓRIOS PRA MEGASENA')
print()
qtde_jogos = int(input('Quantos jogos você vai querer? '))
jogos = []

for j in range(0, qtde_jogos):
    jogos.append(sample(range(1,61),6))

for i, j in enumerate(jogos):
    print(f'Jogo {i+1}: {sorted(j)}')
    sleep(0.5)
print()
