#AULA 14 - LAÇO DE REPETIÇÃO WHILE

#58 - MELHORANDO JOGO 28
from time import sleep
from random import randint
aleatorio = randint(0,10)

print('')
print('\033[7;30;107mCHUTE UM NÚMERO DE 0 A 10 E TENTE ADIVINHAR QUAL EU ESCOLHI. NO FINAL, EU TE CONTO QUANTAS VEZES VC PRECISOU PRA ADIVINHAR.\033[m')
print('')
palpite = int(input('Chute um número: '))
tentativas = 1

while palpite != aleatorio:
    while palpite > aleatorio:
        palpite = int(input('\033[1;30;41mMenos...\033[m Chute um novo número: '))
        tentativas += 1
    while palpite < aleatorio:
        palpite = int(input('\033[1;30;41mMais...\033[m Chute um novo número: '))
        tentativas += 1

else:
    if tentativas == 1:
        print('')
        sleep(1)
        print(f'\033[1;30;42mUAU, ACERTOU DE PRIMEIRA!!!\033[m O número era \033[1;97m{aleatorio}\033[m!')
    else:
        if tentativas >= 7:
            tentativas = (f'\033[1;31m{tentativas}\033[m')
        elif tentativas <= 6 and tentativas > 3:
            tentativas = (f'\033[1;33m{tentativas}\033[m')
        elif tentativas <= 3:
            tentativas = (f'\033[1;32m{tentativas}\033[m')
        print('')
        sleep(1)
        print(f'\033[1;30;42mACERTOU!\033[m O número era \033[1;97m{aleatorio}\033[m! Você precisou de {tentativas} tentativas.')
