#AULA 13 - LAÇO DE REPETIÇÃO FOR

#46 - CONTAGEM FOGUETE
from time import sleep
import emoji
print('')

print('\033[7;30;107mQUE COMECE A CONTAGEM REGRESSIVA PROS FOGOS DE ARTIFÍCIOS\033[m',emoji.emojize(':fireworks:'))
print('')
sleep(1)

for contagem in range(10,-1,-1):
    print(contagem)
    sleep(0.5)
print('')
print(f'\033[7;30;107mFELIZ ANO NOVO!\033[m {emoji.emojize(":fireworks:") * 5}')
