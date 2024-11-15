#AULA 12 - CONDIÇÕES ANINHADAS

#45 - JOKENPÔ
from random import randint
from time import sleep
print('')

print('--- \033[7;30;107mSERÁ QUE VOCÊ CONSEGUE ME VENCER NO JOKENPÔ?\033[m ---')
print('')
sleep(1)

gera_numero = randint(1,3)
print('Aqui estão sua opções: \033[1;30;45m(1) Pedra\033[m  \033[1;30;44m(2) Papel\033[m  \033[1;30;107m(3) Tesoura\033[m')
palpite = int(input('Vai lá, tenta a sorte e coloca um número: '))
print('')

while palpite != 1 and palpite != 2 and palpite != 3:
    palpite = int(input('\033[1;30;43mPalpite Inválido!\033[m Digite um novo palpite: '))
    print('')

sleep(1)
print('\033[7;30;107mJO\033[m')
sleep(1)
print('\033[7;30;107mKEN\033[m')
sleep(1)
print('\033[7;30;107mPÔ!\033[m')
sleep(1)
print('')

if gera_numero == palpite:
    if gera_numero == 1:
        gera_numero = 'Pedra'
        print(f'\033[1;33mEMPATE!\033[m Você e eu colocamos \033[1;30;45m{gera_numero}\033[m.')
    elif gera_numero == 2:
        gera_numero = 'Papel'
        print(f'\033[1;33mEMPATE!\033[m Você e eu colocamos \033[1;30;44m{gera_numero}\033[m.')
    elif gera_numero == 3:
        gera_numero = 'Tesoura'
        print(f'\033[1;33mEMPATE!\033[m Você e eu colocamos \033[1;30;107m{gera_numero}\033[m.')
elif gera_numero == 1 and palpite == 2:
    if gera_numero == 1:
        gera_numero = 'Pedra'
    print(f'Você \033[1;32mGANHOU!\033[m Eu coloquei \033[1;30;45m{gera_numero}\033[m.')
elif gera_numero == 1 and palpite == 3:
    if gera_numero == 1:
        gera_numero = 'Pedra'
    print(f'Você \033[1;31mPERDEU!\033[m Eu coloquei \033[1;30;45m{gera_numero}\033[m.')
elif gera_numero == 2 and palpite == 1:
    if gera_numero == 2:
        gera_numero ='Papel'
    print(f'Você \033[1;31mPERDEU!\033[m Eu coloquei \033[1;30;44m{gera_numero}\033[m.')
elif gera_numero == 2 and palpite == 3:
    if gera_numero == 2:
        gera_numero = 'Papel'
    print(f'Você \033[1;32mGANHOU!\033[m Eu coloquei \033[1;30;44m{gera_numero}\033[m.')
elif gera_numero == 3 and palpite == 1:
    if gera_numero == 3:
        gera_numero = 'Tesoura'
    print(f'Você \033[1;32mGANHOU!\033[m Eu coloquei \033[1;30;107m{gera_numero}\033[m.')
elif gera_numero == 3 and palpite == 2:
    if gera_numero == 3:
        gera_numero = 'Tesoura'
    print(f'Você \033[1;31mPERDEU!\033[m Eu coloquei \033[1;30;107m{gera_numero}\033[m.')
