#AULA 13 - LAÇO DE REPETIÇÃO FOR

#48 - SOMA DOS ÍMPARES MULTIPLOS DE TRÊS
from time import sleep
print('')

print('\033[7;30;107mBRINCANDO COM OS NÚMEROS -- SOMA DOS NMRS ÍMPARES OU PARES DIVISÍVEIS POR UM MÚLTIPLO QUE VC COLOCAR!\033[m')
print('')
inicio = int(input('Digite o valor \033[1;35minicial\033[m: '))
final = int(input('Digite o valor \033[1;36mfinal\033[m: '))
print('')
par_impar = int(input('Quer validar os \033[1;30;107mímpares[1]\033[m ou \033[1;30;107mpares[0]\033[m? '))
while par_impar != 1 and par_impar != 0:
    par_impar = int(input('\033[1;30;41mOpção Inválida\033[m. Digite novamente: '))
    print('')
if par_impar == 1:
    par_impar = "ímpares"
else:
    par_impar = "pares"
print('')
multiplo = int(input('Qual será o \033[1;33mmúltiplo\033[m? '))
print('')

sleep(1)

soma = 0
cont = 0

if par_impar == "ímpares":
    for numeros in range(inicio,final+1):
        if numeros % 2 != 0:
            if numeros % multiplo == 0:
                soma += numeros
                cont += 1
else:
    for numeros in range(inicio, final+1):
        if numeros % 2 == 0:
            if numeros % multiplo == 0:
                soma += numeros
                cont += 1
print(f'A soma dos {cont} números \033[1;30;107m{par_impar}\033[m, de \033[1;35m{inicio}\033[m a \033[1;36m{final}\033[m, sendo múltiplos de \033[1;33m{multiplo}\033[m é: \033[7;30;107m{soma}\033[m.')