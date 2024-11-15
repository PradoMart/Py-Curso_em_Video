#AULA 17 - VARIÁVEIS COMPOSTAS -- LISTAS []

#81 - LISTAS, Armazenando vários valores, ordem decrescente e falar se tem o 5
print('')
lista = []
while True:
    nums = int(input('Digite um número: '))
    lista.append(nums)
    verificação = str(input('Quer continuar? [S/N] ')).strip().upper()
    while verificação not in 'SN':
        verificação = str(input('O quê?! Eu te perguntei se quer continuar. É pra responder SIM ou NÃO! ')).strip().upper()
    if verificação == 'N':
        break
print('')
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os números digitados em ordem decrescente: {lista}.')

if 5 in lista:
    if lista.count(5) > 1:
        print(f'Os números [5] estão nas posições:', end='')
    else:
        print(f'O número [5] está na posição:', end='')
    for posição, numero in enumerate(lista):
        if numero == 5:
            print(f' [{posição+1}] ', end='')
else:
    print('O número 5 não foi digitado.')