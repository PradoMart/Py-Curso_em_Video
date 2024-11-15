    #AULA 08 - DESAFIOS DO 16 AO 21
import math

    #16
'''
from math import ceil
numero = float(input('Digita um número float que eu te falo ele inteiro. '))
print(ceil(numero))
'''

    #17
'''
import math
cat_oposto = float(input('Qual o valor do cosseno? '))
cat_adjacente = float(input('Qual o valor do seno? '))

quadrados = (cat_oposto * cat_oposto) + (cat_adjacente * cat_adjacente)
rq = quadrados ** (1/2)

print(f'O valor da hipotenusa é {math.hypot(cat_oposto, cat_adjacente)}')

print(f' A hipotenusa é {rq}')
'''

    #18
'''
angulo = int(input('Qual o ângulo em análise? '))

print(f'Para o ângulo de {angulo}°, o seno é {math.sin(angulo):.3f}, o cosseno é {math.cos(angulo):.3f} e a tangente é {math.tan(angulo):.3f}.')
'''

    #19
'''
from random import choice
from time import sleep

nome1 = input('Primeiro Nome: ')
nome2 = input('Segundo Nome: ')
nome3 = input('Terceiro Nome: ')
nome4 = input('Quarto Nome: ')

alunos = [nome1, nome2, nome3, nome4]

aleatorio = choice(alunos)

print(f'Os participantes são: {alunos}')
sleep(0.5)
print(f'E o escolhido(a) foi: ')
sleep(0.5)
print('.'*3)
sleep(0.7)
print('.'*2)
sleep(0.9)
print('.'*1)
sleep(1.2)
print(f'O escolhido(a) foi: {aleatorio}.')
'''
    #20
'''
from random import shuffle

nome1 = input('Primeiro Nome: ')
nome2 = input('Segundo Nome: ')
nome3 = input('Terceiro Nome: ')
nome4 = input('Quarto Nome: ')

alunos = [nome1, nome2, nome3, nome4]
shuffle(alunos)

print(f'A ordem de apresentação é: {alunos}')
'''

    #21
'''
import pygame
pygame.init()
pygame.mixer.music.load('stay.mp3')
input('Digite algo para tocar ')
pygame.mixer.music.play()
input('Digite algo para parar ')
'''







