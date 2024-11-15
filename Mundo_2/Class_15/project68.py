#AULA 15 - INTERROMPENDO LAÇO DE REPETIÇÃO

#68 - SEM USAR FLAG NO LAÇO, JOGO PAR OU ÍMPAR
from random import randint

contador = soma = 0
print('')
print('\033[1;30;46mVAMOS JOGAR PAR OU ÍMPAR?\033[m')
print('')
while True:
    randomização = randint(0, 10)
    soma = randomização
    numero = int(input('Digite um número: '))
    while numero < 0 or numero > 10:
        print('\033[33mNÚMEROS NEGATIVOS OU MAIORES QUE DEZ NÃO SÃO PERMITIDOS!\033[m')
        numero = int(input('Digite um novo número: '))
    par_impar = str(input('Par ou ímpar? ')).strip().upper()[0]
    while par_impar != 'P' and par_impar != 'Í' and par_impar != 'I':
        par_impar = str(input('\033[33mINVÁLIDO!\033[m Par ou ímpar? ')).strip().upper()[0]
    soma += numero
    print(f'Eu escolhi: \033[1m{randomização}\033[m e você: \033[1m{numero}\033[m. A soma é: \033[1m{soma}\033[m.')
    if soma % 2 == 0:
        if par_impar == 'P':
            print(f'{soma} é par. \033[32mVOCÊ GANHOU!\033[m')
            contador += 1
        else:
            print(f'{soma} é par. \033[31mVOCÊ PERDEU!\033[m')
            break
    elif soma % 2 != 0:
        if par_impar == 'Í' or par_impar == 'I':
            print(f'{soma} é ímpar. \033[32mVOCÊ GANHOU!\033[m')
            contador += 1
        else:
            print(f'{soma} é ímpar. \033[31mVOCÊ PERDEU!\033[m')
            break
    soma = 0
    print('')
print('')
if contador > 1:
    print(f'Você teve \033[1;32m{contador}\033[m vitórias!')
elif contador == 1:
    print(f'Você teve \033[1;33mapenas uma\033[m vitória!')
else:
    print(f'Xiii, você \033[1;31mnão ganhou nenhuma!\033[m')
