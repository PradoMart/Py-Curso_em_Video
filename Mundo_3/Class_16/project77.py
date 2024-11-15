#AULA 16 - VARIÁVEIS COMPOSTAS -- TUPLAS ()

#77 - TUPLAS, palavras armazenadas
#não consegui fazer sozinho, a lógica do for aninhado me pegou, além do atributo (in)
words = ('sao paulo', 'garrafa', 'mouse', 'celular', 'poltrona', 'mesa', 'vidro', 'tampa', 'notebook', 'fio', 'chave', 'mochila', 'toalha', 'capinha', 'quadro', 'sofa', 'televisao', 'oculos', 'janela')

for w in (words):
    print(f'\nNa palavra \033[1m{w.upper():^10}\033[mhá as vogais: ', end='')
    for letters in w:
        if letters.lower() in 'aeiou':
            print(letters, end=' ')

#o que eu queria era tirar as vogais repetidas, mas não consegui.
