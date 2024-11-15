#AULA 16 - VARIÁVEIS COMPOSTAS -- TUPLAS ()

#72 - TUPLAS, números por extenso
print('')
print('--- !ESCOLHA UM NÚMERO, EU TE FALO O EXTENSO. PRA PARAR, BASTA ESCOLHER UM NMR < 0 OU > 10! ---')
print('='*30)
num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num_escolhido = int(input('Escolha um número de 0 a 10: '))
    if num_escolhido < 0 or num_escolhido > 10:
        break
    print(num_extenso[num_escolhido])
    print('='*30)
    print('')
