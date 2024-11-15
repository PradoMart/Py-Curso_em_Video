#AULA 13 - LAÇO DE REPETIÇÃO FOR

#55 - QUEM É O MAIS PESADO?
print('')

nmr_pessoas = int(input('Quantas pessoas vai me falar o peso? '))
print('')
print('\033[7;30;107m-=\033[m' * 25)

coleta = []

for repete in range(1,nmr_pessoas+1):
    peso = input(f'Qual o {repete}º peso? ').strip().replace(',','.')
    coleta += [peso]
coleta.sort()

print('\033[7;30;107m-=\033[m'*25)
print('')
print(f'O menor peso é: \033[1;33m{coleta[0]}\033[m. Enquanto o maior é: \033[1;34m{coleta[-1]}\033[m.')
