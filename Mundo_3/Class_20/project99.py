#AULA 20 - FUNÇÕES

#99 - FUNÇÕES, analisando números
from time import sleep
from random import randint, sample
def maior(* núm):
    print(f'Analisando os valores passados...', flush=True)
    sleep(0.5)
    if len(núm) == 0:
        print(f'Não foram informados valores!')
        print()
    else:
        for v in núm:
            print(v, end=' ', flush=True)
            sleep(0.5)
        print('FIM!', end='')
        print(f' -- Você digitou {len(núm)} números, o maior é {max(núm)}.')
        print()

maior(randint(0,10),randint(5,15),randint(10,20),randint(15,25))
maior(randint(102,304),randint(402,672),randint(243,876))
maior(randint(450,983), randint(500,1890))
maior(randint(2039,3404))
maior()
