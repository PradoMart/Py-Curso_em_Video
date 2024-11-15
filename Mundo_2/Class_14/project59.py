#AULA 14 - LAÇO DE REPETIÇÃO WHILE

#59 - MENU MATEMÁTICO - não consegui fazer sozinho (opção infinita)
from time import sleep
print('')
num1 = int(input('Digite o \033[35m1º número\033[m: '))
num2 = int(input('Digite o \033[36m2º número\033[m: '))

print('')

print('------- MENU -------')
print(f'''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
------- MENU -------
''')

escolha = 0
while escolha != 5:
    escolha = int(input('\033[1;97mQual sua escolha:\033[m '))
    print('')
    if escolha == 1:
        print(f'A soma de \033[35m{num1}\033[m + \033[36m{num2}\033[m é: \033[1;97m{num1 + num2}\033[m.')
        print('')
    elif escolha == 2:
        print(f'A multiplicação de \033[35m{num1}\033[m * \033[36m{num2}\033[m é: \033[1;97m{num1 * num2}\033[m.')
        print('')
    elif escolha == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O número maior é: \033[1;97m{maior}\033[m.')
        print('')
    elif escolha == 4:
        print('Informe novos números!')
        num1 = int(input('Digite o \033[35m1º número\033[m: '))
        num2 = int(input('Digite o \033[36m2º número\033[m: '))
        print('')
    elif escolha == 5:
        print('\033[1;30;107mPROGRAMA FINALIZADO!\033[m')
    else:
        print('\033[1;33mTENTE NOVAMENTE!\033[m')
    sleep(1)
