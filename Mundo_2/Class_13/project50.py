#AULA 13 - LAÇO DE REPETIÇÃO FOR

#50 - REFAZENDO DESAFIO DA TABUADA
from time import sleep
print('')

print('\033[1;30;107mO PROGRAMA TE PEDIRÁ SEIS NÚMEROS E TE MOSTRARÁ A SOMA DOS ÍMPARES OU PARES, VOCÊ ESCOLHE!\033[m')
sleep(1)
print('-='*7)
soma_par = 0
cont_par = 0
soma_impar = 0
cont_impar = 0
for x in range(1,7):
    numeros = int(input('Digite um número: '))
    if numeros % 2 == 0:
        soma_par += numeros
        cont_par += 1
    else:
        soma_impar += numeros
        cont_impar += 1

print('-='*7)

par_impar = str(input('Você quer ver a soma dos \033[1;30;107mímpares\033[m ou \033[1;30;107mpares\033[m? ')).strip().upper()
sleep(1)
print('')
if par_impar[0] == "P":
    print(f'A soma dos {cont_par} números pares é \033[1;30;107m{soma_par}\033[m!')
else:
    print(f'A soma dos {cont_impar} números ímpares é \033[1;30;107m{soma_impar}\033[m!')

