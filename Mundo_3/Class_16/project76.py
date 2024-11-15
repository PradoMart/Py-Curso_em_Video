#AULA 16 - VARIÁVEIS COMPOSTAS -- TUPLAS ()

#76 - TUPLAS, nomes dos produtos
#não consegui fazer sozinho, pq não sabia fazer o tratamento de string em alinhado a esquerda, direita e centro
print('')
produto = ('Lápis', 1.75, 'Borracha', 2.50, 'Caderno', 10.87, 'Estojo', 4.76, 'Transferidor', 9.78, 'Compasso', 3.50, 'Mochila', 200.99, 'Canetas', 1.99, 'Livro', 43.99)

print('\033[1;35;40m-=\033[m'*19)
print(f'\033[1;30;45m{"LISTAGEM DE PRODUTOS":^38}\033[m')
print('\033[1;35;40m-=\033[m'*19)
for posicao in range(0, len(produto)):
    if posicao % 2 == 0:
        print(f'{produto[posicao]:.<30}', end='')
    else:
        print(f'R${produto[posicao]:>6.2f}')
print('\033[1;35;40m-=\033[m'*19)
