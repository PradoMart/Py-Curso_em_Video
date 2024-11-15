#AULA 15 - INTERROMPENDO LAÇO DE REPETIÇÃO

#66 - SEM USAR FLAG NO LAÇO, MOSTRAR QTDE DE NÚMEROS DIGITADOS E A SOMA DELES
from time import sleep
print('')
print('\033[1mDIGITE ALGUNS NÚMEROS, NO FINAL, TE MOSTRO QUANTOS VOCÊ DIGITOU E A SOMA DELES. \n\033[33mPRA PARAR, É SÓ DIGITAR: 999\033[m\033[m')
print('')
lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    lista.append(numero)
print('')
sleep(1)
print(f'Foram digitados {len(lista)} números, a soma deles é {sum(lista)}. O maior número digitado foi {max(lista)} e o menor foi {min(lista)}.')
