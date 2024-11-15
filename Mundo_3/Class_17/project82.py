#AULA 17 - VARIÁVEIS COMPOSTAS -- LISTAS []

#82 - LISTAS, Armazenando vários valores, separando ímpares e pares em listas diferentes
print('')

all = []
even = []
odd = []

while True:
    all.append(int(input('Type a number: ')))
    verification = str(input('Would you like to continue? [Y/N] ')).strip().upper()
    while verification not in 'YN':
        verification = str(input('I couldnt understand, please type [Y/N]: ')).strip().upper()
    if verification == 'N':
        break
print('')
print(f'The \033[1mfull\033[m list in descending order is: {sorted(all)}')
for nums in all:
    if nums % 2 == 0:
        even.append(nums)
    else:
        odd.append(nums)
print(f'The \033[1meven\033[m list is: {sorted(even)}')
print(f'The \033[1modd\033[m list is: {sorted(odd)}')
