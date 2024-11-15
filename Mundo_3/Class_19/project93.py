#AULA 19 - VARIÁVEIS COMPOSTAS -- DICIONÁRIO {}

#93 - DICIONÁRIOS, JOGADOR DE FUTEBOL
print()
dados = {}
gols = []
dados['Jogador'] = str(input('Nome do jogador: ')).title().strip()
jogos = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))

for j in range(1,jogos+1):
    gols.append(int(input(f'Quantos gols na {j}ª partida? ')))
    dados['gols'] = gols
dados['total_gols'] = sum(gols)
média_gols = sum(gols) / jogos
print('-='*20)

#retirei esta parte, pq achei que ficou poluindo demais a resolução
"""for k, v in dados.items():
    print(f'({k}) = {v}')
print('-='*20)"""

print(f'Em {jogos} jogos, {dados["Jogador"]} marcou {dados["total_gols"]} gol(s), tendo uma média de {média_gols:.2f} gol(s) por partida.')
for j in range(0, jogos):
    if dados['gols'][j] == 0: 
        print(f' => Na {j+1}ª partida, \033[1;31mnão marcou.\033[m')
    elif dados['gols'][j] == 1:
        print(f' => Na {j+1}ª partida, \033[1;32mmarcou 1 gol.\033[m')
    else:
        print(f' => Na {j+1}ª partida, \033[1;32mmarcou {dados["gols"][j]} gols.\033[m')
print('-='*20)
print(f'\033[1;34mAnálise do desempenho de {dados["Jogador"]} finalizada!\033[m')
