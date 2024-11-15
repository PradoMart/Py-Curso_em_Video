def teste(*num, sit=bool):
    if sit == 'N':
        sit = False
    else:
        sit = True
    print(num, sit)

n = int(input(f'Quantas vezes? '))
for i in range(0,n):
    teste(input(f'Qual o número? '))

'''while True:
    resp = teste(input('Qual número? '))
    verificação = input('Continua? ')
    if verificação in 'nN':
        teste(sit = input('Quer mostrar? [S/N] '))
        break'''
