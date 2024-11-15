#AULA 12 - CONDIÇÕES ANINHADAS

#42 - CATEGORIZANDO OS TRIÂNGULOS

from time import sleep
print('')
a = float(input('Digite o tamanho da \033[1;30;107mprimeira\033[m reta: '))
b = float(input('Digite o tamanho da \033[1;30;45msegunda\033[m reta: '))
c = float(input('Digite o tamanho da \033[1;30;46mterceira\033[m reta: '))

ab = a + b
ac = a + c
bc = b + c

sleep(0.5)
print('')
print('\033[1;33mCalculando Trigonometria! Por favor, aguarde!\033[m')
sleep(1)
print('\033[1;33m...\033[m')
sleep(0.5)
print('\033[1;33m..\033[m')
sleep(0.5)
print('\033[1;33m.\033[m')
sleep(1)
print('')
print('\033[1;34mCÁLCULO FINALIZADO! Obrigado por aguardar!\033[m')
print('')
sleep(2)

if ab > c and ac > b and bc > a:
    print(f'As retas \033[1;30;107m{a:.0f}\033[m,\033[1;30;45m{b:.0f}\033[m,\033[1;30;46m{c:.0f}\033[m \033[1;32mformam\033[m um triângulo!')
    print('')
    if a == b and a == c and b == c:
        print(f'Este triângulo é um \033[1;32mEquilátero\033[m, porque os três lados são iguais.')
    elif a != b and a != c and b != c:
        print(f'Este triângulo é um \033[1;32mEscaleno\033[m, porque os três lados são diferentes.')
    else:
        print(f'Este triângulo é um \033[1;32mIsósceles\033[m, porque dois lados são iguais.')
else:
    print(f'As retas \033[1;30;107m{a:.0f}\033[m,\033[1;30;45m{b:.0f}\033[m,\033[1;30;46m{c:.0f}\033[m \033[1;31mnão formam\033[m um triângulo!')