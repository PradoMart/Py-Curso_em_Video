#AULA 12 - CONDIÇÕES ANINHADAS

#37 - CONVERSOR DE NÚMEROS (tive que olhar)
from time import sleep
print('')
print('\033[1;30;107mSEJA BEM-VINDO(A) AO CONVERSOR DE NÚMEROS!\033[m')
print('')
numero = int(input('Pra começarmos, digite um número que queira converter: '))
print('')
print('''Escolha uma das opções para conversão:
[1] converter para \033[35mBINÁRIO\033[m
[2] converter para \033[36mOCTAL\033[m
[3] converter para \033[34mHEXADECIMAL\033[m''')
print('')
escolha = int(input('Qual sua escolha para conversão? '))
print('')

while escolha != 1 and escolha != 2 and escolha != 3:
    escolha = int(input('\033[1;30;43mNÚMERO INVÁLIDO!\033[m Escolha novamente: '))
print('')
sleep(1)

if escolha == 1:
    print(f'{numero} convertido pra \033[1;35mBINÁRIO\033[m é \033[7;30;107m{bin(numero)[2:]}\033[m.')
elif escolha == 2:
    print(f'{numero} convertido pra \033[1;36mOCTAL\033[m é \033[7;30;107m{oct(numero)[2:]}\033[m.')
elif escolha == 3:
    print(f'{numero} convertido pra \033[1;34mHEXADECIMAL\033[m é \033[7;30;107m{hex(numero)[2:]}\033[m.')
