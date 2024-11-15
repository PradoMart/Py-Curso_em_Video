#AULA 16 - VARIÁVEIS COMPOSTAS -- TUPLAS ()

#74 - TUPLAS, numeros aleatórios
from random import randint
print('')
lista = (randint(0,5), randint(0,10), randint(0,15), randint(0,20), randint(0,25))

print(f'\033[1mEsses são os números aleatórios gerados: {lista}.\033[m\n\033[31mO menor é: {min(lista)}\033[m / \033[34mO maior é: {max(lista)}\033[m')


#solução encontrada nos comentários
'''from random import sample

a = tuple(sample(range(10),5))
print(f'{a}. O maior {max(a)}, o menor {min(a)}')'''

