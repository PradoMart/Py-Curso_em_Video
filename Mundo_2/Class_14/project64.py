#AULA 14 - LAÇO DE REPETIÇÃO WHILE

#64 - LENDO VÁRIOS NÚMEROS
from time import sleep
print('')
print('--- \033[1;35mARMAZENANDO VÁRIOS NÚMEROS\033[m ---', end=' ')
print('\033[1mCaso queria parar é só digitar \033[40m999\033[m.\033[m')
print('')
algo = int(0)
contador = int(0)
soma = int(0)

while algo != 999:
    algo = int(input('Digite um número: '))
    if algo != 999:
        contador += 1
        soma += algo
print('')
sleep(1)

if contador == 1:
    print(f'Foi digitado \033[1;30;45mapenas 1 número\033[m. E o valor dele é \033[1;30;45m{soma}\033[m.')
else:
    print(f'Foram digitados \033[1;30;45m{contador} números\033[m. A soma deles é: \033[1;30;45m{soma}\033[m.')
