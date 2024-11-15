#AULA 21 - FUNÇÕES

#102 - FUNÇÕES, fatorial
def fatorial(número, show=False):
    """_summary_
    Args:
        n (_type_): É o número a ser fatorado
        show (bool, optional): A lógica booleana linkada à opção de ver, ou não, a operação matemática.
    """
    if show == 'S':
        show = True
    else:
        show = False
    fatorado = número
    cont = número-1
    while cont > 0:
        fatorado = fatorado * cont
        cont -= 1
    if show == False:
        print(fatorado)
    else:
        for i in range(número, 0, -1):
            if i > 1:   
                print(f'{i} X ', end='')
            else:
                print(f'{i} = ', end='')
        print(f'{fatorado}')
    print()
help(fatorial)
while True:    
    fatorial(int(input('Qual número quer fatorar? ')), input('Quer mostrar o cálculo? [S/N] ').upper())
    verifica = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if verifica == 'N':
        break
