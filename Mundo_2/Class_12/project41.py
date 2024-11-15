#AULA 12 - CONDIÇÕES ANINHADAS

#41 - CATEGORIAS DE NATAÇÃO
from datetime import date
from time import sleep

print('')
print('\033[1;30;42m*** Bem-vindo(a), ao sistema de classificação da Confederação Nacional de Natação! ***\033[m')
print('')
mes_ano_nascimento = str(input('Em que \033[1;30;107mmês e ano\033[m você nasceu?\nDigite no seguinte formato: \033[1;30;107m"MM/AAAA"\033[m ')).strip()
print('')
sleep(1.5)
print('')
print('***\033[1;30;107mCLASSIFICANDO\033[m***')
print('')
sleep(3)

mes_nascimento = int(mes_ano_nascimento[:2])
ano_nascimento = int(mes_ano_nascimento[3:])

if mes_nascimento <= date.today().month:
    idade = date.today().year - ano_nascimento
else:
    idade = (date.today().year - ano_nascimento) - 1

if idade <= 9:
    print(f'Tendo apenas \033[1;36m{idade} anos\033[m, você é um competidor \033[1;36mmirim\033[m!')
elif idade > 9 and idade <= 14:
    print(f'Tendo \033[1;35m{idade} anos\033[m, você é um competidor \033[1;35minfantil\033[m!')
elif idade > 14 and idade <= 19:
    print(f'Tendo \033[1;33m{idade} anos\033[m, você é um competidor \033[1;33mjunior\033[m!')
elif idade < 19 and idade <= 20:
    print(f'Tendo \033[1;34m{idade} anos\033[m, você é um competidor \033[1;34msênior\033[m!')
else:
    print(f'Tendo \033[1;32m{idade} anos\033[m, você é um competidor \033[1;32mmaster\033[m!')
