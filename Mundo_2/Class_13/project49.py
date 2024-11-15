#AULA 13 - LAÇO DE REPETIÇÃO FOR

#49 - REFAZENDO DESAFIO DA TABUADA
from time import sleep

print('')
multiplicador = input('\033[7;35;40mQuer ver a tabuada de qual número?\033[m ')
while multiplicador.isnumeric() == False:
    multiplicador = input('O multiplicador precisar ser um \033[7;35;40mNÚMERO\033[m: ')
multiplicador = int(multiplicador)
print('\033[35m-=\033[m'*6)
sleep(0.5)
for tabuada in range(0,11):
    print(f'{multiplicador} * {tabuada} = {multiplicador * tabuada}')
    sleep(0.5)
print('\033[35m-=\033[m'*6)
print('')

rq = str(input(f'Gostaria de saber a \033[30;107mraiz quadrada\033[m de {multiplicador} [Sim ou Não]? ')).strip().upper()
print('')
sleep(0.5)
if rq[0] == "S":
    print(f'A raiz quadrada de {multiplicador} é \033[30;107m{multiplicador ** (1/2):.2f}\033[m.')
    print('')
sleep(0.5)
print('\033[7;35;40mFoi bom ter você aqui! Tchau tchau.\033[m')