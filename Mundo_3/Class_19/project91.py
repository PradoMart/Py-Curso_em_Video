#AULA 19 - VARIÁVEIS COMPOSTAS -- DICIONÁRIO {}

#91 - DICIONÁRIOS, DADO
# Não tinha conseguido fazer sozinho, pq não sabia o itemgetter.
print()
from random import randint
from time import sleep
from operator import itemgetter
jogadas = {}
ranking = []
for n in range(1,5):
    jogadas[f'Jogador{n}'] = randint(1,6)

#print(jogadas)
print('<'*5, 'VALORES SORTEADOS', '>'*5)
for k, v in jogadas.items():
    sleep(0.7)
    print(f'{k} tirou: {v}')
print()
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('<'*5, 'RANKING', '>'*5)
for k, v in enumerate(ranking):
    sleep(0.7)
    print(f'{k+1}º lugar: {v[0]} com {v[1]}')
print()