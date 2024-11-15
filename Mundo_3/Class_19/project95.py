#AULA 19 - VARIÁVEIS COMPOSTAS -- DICIONÁRIO {}

#95 - DICIONÁRIOS, MELHORANDO O EXERCÍCIO 93 JOGADOR DE FUTEBOL

print()
dados = {}
gols = []
dados_list = []
while True:
    dados.clear()
    dados['Jogador'] = str(input('Nome do jogador: ')).title().strip()
    jogos = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))

    for j in range(1,jogos+1):
        gols.append(int(input(f'Quantos gols na {j}ª partida? ')))
        dados['gols'] = gols[:]
    dados['total_gols'] = sum(gols[:])
    dados['média_gols'] = sum(gols[:]) / jogos
    gols.clear()
    dados_list.append(dados.copy())
    

    verificação = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while verificação not in 'SN':
        verificação = str(input('OPÇÃO INVÁLIDA! Quer continuar [S/N] ?')).strip().upper()[0]
    if verificação == 'N':
        print()
        break
    print()

print(dados_list)

#não tinha conseguido fazer esta parte sozinho, pq não pensei em usar .keys() e jogar a iteração sendo um str (tanto pro cabeçalho quanto pros resultados)
print('-='*40)
print(f'{"CÓD":<5}', end='')
for i in dados.keys():
    print(f'{str(i).upper():<15}', end='')
print()
for k, v in enumerate(dados_list):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
    
print('-='*40)
while True:
    detalhamento = int(input('Mostrar dados de qual jogador? (TO STOP: 999) '))
    if detalhamento == 999:
        break
    if detalhamento > len(dados_list):
        detalhamento = int(input('JOGADOR INEXISTENTE! Mostrar dados de qual jogador? '))
    print()
    print(f'DESEMPENHO DE \033[1m{dados_list[detalhamento]["Jogador"].upper()}\033[m: ')
    for i, g1 in enumerate(dados_list[detalhamento]["gols"]):
        if g1 > 1:
            print(f'\033[32mNa {i+1}ª partida, fez {g1} gols;\033[m')
        elif g1 == 1:
            print(f'\033[33mNa {i+1}ª partida, fez 1 gol;\033[m')
        else:
            print(f'\033[31mNa {i+1}ª partida, não fez gol;\033[m')
    print(f'A média de {dados_list[detalhamento]["Jogador"]} é {dados_list[detalhamento]["média_gols"]:.2f} gol(s) por partida.')
    print()
print('\033[1mANÁLISE FINALIZADA\033[m')