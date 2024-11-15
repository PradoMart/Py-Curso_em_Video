#AULA 15 - INTERROMPENDO LAÇO DE REPETIÇÃO

#67 - SEM USAR FLAG NO LAÇO, TABUADA

while True:
    multiplicador = int(input('Quer saber a tabuada de qual número? '))
    if multiplicador < 1:
        break
    for x in range(1,11):
        print(f'{multiplicador} * {x} = {multiplicador * x}')
    print('')
