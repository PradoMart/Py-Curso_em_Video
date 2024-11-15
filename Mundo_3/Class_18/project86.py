#AULA 18 - VARIÁVEIS COMPOSTAS -- LISTAS ANINHADAS []

#86 - LISTAS, MATRIZ
#fiquei muito feliz, pq consegui fazer. Não do mesmo jeito do Guanabara, mas consegui entregar o que foi solicitado no enunciado do exercício.
'''
print('')
matriz = [[],[],[]]
x = y = 0
for n in range(0,9):
    num = int(input(f'Digite o valor [{x};{y}]: '))
    y += 1
    if y == 3:
        x +=1
        y -= 3
    if n < 3:
        matriz[0].append(num)
    elif n < 6:
        matriz[1].append(num)
    else:
        matriz[2].append(num)
print('')
print(matriz,'\n')

z = k = 0
for x in range(0,9):
    print(f'[{matriz[z][k]:^5}]', end=' ')
    k += 1
    if k == 3:
        z += 1
        k -= 3
    if x == 2 or x == 5:
        print('')
'''
#A Solução do Guanabara é bem mais simples e mais curta. Nem passou pela minha cabeça em usar for aninhado e colocar o valor lido pelo input direto na lista. 

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linhas in range(0,3):
    for colunas in range(0,3):
        matriz[linhas][colunas] = int(input(f'Digite o valor para [{linhas};{colunas}]: '))
print('')
for linhas in range(0,3):
    for colunas in range(0,3):
        print(f'[{matriz[linhas][colunas]:^5}]', end='')
    print('')
print('')
