#AULA 21 - FUNÇÕES

#103 - FUNÇÕES, jogador

def ficha(nome=0, gols=0, partidas=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    else:
        gols = int(gols)
    if partidas == '':
        partidas = 0
    else:
        partidas = int(partidas)
    média_gols = gols / partidas
    print(f'O jogador {nome} fez {gols} gol(s) em {partidas} partidas, portanto sua média é {média_gols:.2f} gols por partida.')

ficha(str(input('Jogador: ').title().strip()), input('Nmr Gols: '), input('Partidas: '))