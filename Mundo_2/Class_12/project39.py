#AULA 12 - CONDIÇÕES ANINHADAS

#39 - ALISTAMENTO NO EXÉRCITO
from datetime import date
from time import sleep
print('')
print('Olá! Meu nome é Escoteiro, sou assistente virtual do Exército Brasileiro!')
print('')
sleep(1)
nome = str(input('Com quem estou falando? ')).strip().title()
print(f'É um prazer ter você aqui, {nome}!')
print('')
sleep(1)

genero = str(input(f'{nome}, com que gênero você se identifica? ')).strip().upper()
genero = genero[0]
sleep(1)
print('')

if genero == "M":
    ano_nascimento = int(input('E em que ano você nasceu? '))
    ano_atual = int(date.today().year)
    idade = ano_atual - ano_nascimento

    if  idade < 18:
        if idade == 17:
            print(f'{nome}, você ainda não precisa se alistar, mas fique de olho, porque falta apenas \033[1;33m{18 - idade} ano\033[m. Você deverá se alista no ano que vem (\033[1;33m{ano_nascimento + 18}\033[m).')
        else:
            print(f'{nome}, você ainda não precisa se preocupar, porque faltam \033[1;33m{18 - idade} anos\033[m pra você se alistar! Você deverá se alistar lá em \033[1;33m{ano_nascimento + 18}\033[m.')

    elif idade == 18:
        alistamento = str(input(f'{nome}, você já se alistou? ')).strip().upper()
        if alistamento == "SIM":
            print(f'Parabéns, agora é só \033[1;32mesperar a evolução do processo\033[m! O Exército Brasileiro agradece sua conduta.')
        else:
            print(f'\033[1;33mJá está na hora de servir seu país.\033[m Acesse o site do Exército Brasileiro e faça já seu alistamento. Contamos com você!')

    elif idade > 18:
        alistamento = str(input(f'{nome}, você já cumpriu com o serviço militar? ')).strip().upper()
        if alistamento == "SIM":
            print(f'Parabéns pela sua conduta. \033[1;32mO Exército Brasileiro agradece e honra o seu esforço!\033[m')
        else:
            if idade == 19:
                print(f'Você está atrasado com o serviço militar em \033[1;31m{idade - 18} ano\033[m.\nPrecisamos que você faça seu cadastro aqui no site e se apresente em uma das nossas bases militares no próximo dia útil.')
            else:
                print(f'Você está atrasado com o serviço militar em \033[1;31m{idade - 18} anos\033[m. Seu alistamento deveria ter sido em \033[1;31m{ano_nascimento + 18}\033[m.\nPrecisamos que você faça seu cadastro aqui no site e se apresente em uma das nossas bases militares no próximo dia útil.')
else:
    alistamento = str(input(f'{nome}, você tem interesse em fazer parte do Exército Brasileiro? ')).strip().upper()
    if alistamento == "SIM":
        print(f'Que honra em ter você conosco! Pra continuar o seu processo de alistamento, basta apenas fazer seu cadastro nesta página e comparecer a uma de nossas bases.')
    else:
        print(f'Acredito que não podemos auxiliá-la em algo mais, {nome}. Foi um prazer ter você aqui!')
