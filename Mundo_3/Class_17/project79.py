#AULA 17 - VARIÁVEIS COMPOSTAS -- LISTAS []

#79 - LISTAS, Armazenando vários valores, mostrando em ordem crescente
from time import sleep
print('')
nums = []

while True:
    sleep(0.5)
    adicionando = int(input('Digite um valor: '))
    if adicionando not in nums:
        nums.append(adicionando)
    else:
        print('\033[33mValor já digitado, portanto, desprezado!\033[m')
    continuar = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input(f'Não entendi! Quer continuar ou não? ')).strip().upper()[0]
    print('')
    if continuar == 'N':
        break
sleep(1)
print(sorted(nums))
