#AULA 20 - FUNÇÕES

#100 - FUNÇÕES, contador pares
#não passei parametros na função, daí vi o vídeo e mudei o código.
from random import randint, sample

números = []

def sorteia(lista):
    #números.append(sample(range(1,101),5))
    for i in range(0,5):
        sorteado = randint(1,10)
        while sorteado in números:
            sorteado = randint(1,10)
        lista.append(sorteado)
    print(lista)

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos valores pares é: {soma}.')

sorteia(números)
somaPar(números)