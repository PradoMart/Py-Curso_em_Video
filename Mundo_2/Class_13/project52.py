#AULA 13 - LAÇO DE REPETIÇÃO FOR

#52 - NÚMERO PRIMO - não consegui fazer sozinho
#numeros primos são aqueles que são divisíveis apenas por um e por ele mesmo.
print('')

num = int(input('Digite o número: '))
tot = 0
print('')
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end = '')
        tot += 1
    else:
        print('\033[31m', end = '')
    print(f'{c}', end=' ')
print('')
print(f'\n\033[mO número {num} foi divisível {tot} vezes,', end = ' ')
if tot == 2:
    print(f'portanto ele \033[34mÉ PRIMO\033[m!')
else:
    print('portanto ele \033[31mNÃO É PRIMO\033[m!')
