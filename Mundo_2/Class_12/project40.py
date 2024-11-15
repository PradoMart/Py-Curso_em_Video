#AULA 12 - CONDIÇÕES ANINHADAS

#40 - MÉDIA DE ALUNO

from time import sleep
nota_1 = float(input('Qual o valor da primeira nota? '))
nota_2 = float(input('Qual o valor da segunda nota? '))

media = (nota_1 + nota_2) / 2
print('')
sleep(1)
print('\033[1;30;107mCalculando média, por favor, aguarde!\033[m')
print('')
sleep(1)
print('\033[1;30;107m...\033[m')
sleep(1)
print('')
print('\033[1;30;107m..\033[m')
sleep(1)
print('')
print('\033[1;30;107m.\033[m')
sleep(3)
print('')

if media < 5:
    print(f'Com a média de \033[1;31m{media:.2f}\033[m você está \033[1;31mreprovado(a)\033[m!')
elif media >= 5 and media <= 6.9:
    print(f'Sua média é de \033[1;33m{media:.2f}\033[m pontos. Você está de \033[1;33mrecuperação\033[m!')
else:
    print(f'Sua média ficou em \033[1;32m{media:.2f}\033[m. Você está \033[1;32maprovado(a)!\033[m')