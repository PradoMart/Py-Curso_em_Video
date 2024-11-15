#AULA 12 - CONDIÇÕES ANINHADAS

#38 - COMPARAÇÃO DE NÚMEROS
from time import sleep
print('')
sim_nao = str(input(f'Vamos fazer um jogo de comparação? Se quiser jogar digite: "\033[1;30;42mSIM\033[m"! ')).strip().upper()

if sim_nao [0] == 'S':
    print('-=-'*20)
    n1 = int(input('Pra começar, digite o \033[1;34mprimeiro\033[m valor: '))
    n2 = int(input('Agora, digite o \033[1;35msegundo\033[m valor: '))
    print('-=-'*20)
    sleep(1)
    print('\033[1;33mPor favor, aguarde...\nProcessando operação matemática!\033[m')
    sleep(2)
    print('-=-'*20)
    sleep(2)

    if n1 > n2:
        print(f'O primeiro valor (\033[1;34m{n1}\033[m) é maior que o segundo valor (\033[1;35m{n2}\033[m)!')
    elif n2 > n1:
        print(f'O segundo valor (\033[1;35m{n2}\033[m) é maior que o primeiro valor (\033[1;34m{n1}\033[m)!')
    else:
        print(f'Não existe valor maior! O primeiro valor (\033[1;34m{n1}\033[m) é igual ao segundo valor (\033[1;35m{n2}\033[m)!')

else:
    print('')
    print(f':( Ah que pena, foi bom interagir contigo. Até mais!!!')