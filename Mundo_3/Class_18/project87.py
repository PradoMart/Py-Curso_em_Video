#AULA 18 - VARIÁVEIS COMPOSTAS -- LISTAS ANINHADAS []

#87 - LISTAS, MELHORANDO O EXERCÍCIO 86 DE MATRIZ
print('')
geral = [[0,0,0],[0,0,0],[0,0,0]]
for linhas in range(0,3):
    for colunas in range(0,3):
        geral[linhas][colunas] = int(input(f'Digite o valor de [{linhas};{colunas}]: '))
print('')

#sitatuions = [valores pares], [valores da terceira coluna], [valores da segunda linha]
situations = [[],[],[]]

for linhas in range(0,3):
    for colunas in range(0,3):
        print(f'[{geral[linhas][colunas]:^5}]', end='')
        if geral[linhas][colunas] % 2 == 0:
            situations[0].append(geral[linhas][colunas])
        if colunas == 2:
            situations[1].append(geral[linhas][colunas])
        if linhas == 1:
            situations[2].append(geral[linhas][colunas])
    print('')
print('')
print(f'A soma dos valores pares é: [{sum(situations[0])}]')
print(f'A soma dos valores da terceira coluna é: [{sum(situations[1])}]')
print(f'O maior valor da linha 2 é: [{max(situations[2])}]')
print('')
