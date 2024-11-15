#AULA 21 - FUNÇÕES

#105 - FUNÇÕES, sistema de ajuda pyHELP
from time import sleep
def cabeçalho(frase):
    print()
    print('\033[1;97;46m~'*(len(frase)+4))
    print(f'  {frase}  ')
    print('~'*(len(frase)+4), end='\033[m')
    print()
    sleep(0.3)

def manual(frase):
    print('\033[1;30;43m~'*(len(frase)+4))
    print(f'  {frase}  ')
    print('~'*(len(frase)+4), end= '\033[m')
    print()
    sleep(0.3)

def despedida(frase):
    print('\033[1;30;41m~'*(len(frase)+4))
    print(f'  {frase}  ')
    print('~'*(len(frase)+4), end= '\033[m')
    print()
    sleep(0.3)

def ajuda():
    escolha = ''
    while escolha != 'fim':
        cabeçalho('SISTEMA DE AJUDA PyHELP')
        escolha = str(input(f'Função ou Biblioteca: ').lower().strip())
        if escolha == 'fim':
            despedida('ATÉ LOGO!')
            break
        manual(f'{"Acessando o manual do comando"} {escolha.upper()}')
        print('\033[1;30;107m')
        print(f'{help(escolha)}', end='\033[m')
        print()
    return 

ajuda()