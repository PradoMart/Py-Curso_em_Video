# DESAFIOS

    #22
'''
nome = input('Digite seu nome completo: ')
nome = nome.strip()


print(nome.upper())
print(nome.lower())
print(nome.title())

tamanho = len(nome)
espacos = nome.count(' ')
tam_sem_espacos = tamanho - espacos

print(f'Seu nome completo tem {tam_sem_espacos} letras.')

nome = nome.split()

print(f'Já o seu primeiro nome tem {len(nome[0])} letras.')
'''

    #23
'''
#jeito guanabara
numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')

#jeito comentário
n=input('Digite um número inteiro de 0 até 9999: ')
m=f'{n:0>4}'
    #aqui eu to falando pra "n" ter 4 casas e preencher com 0 as casas vazias.
print(f'Unidade: {m[3]}\nDezena: {m[2]}\nCentena: {m[1]}\nMilhar: {m[0]}')
'''

    #24
'''
cidade = str(input('Digite o nome de uma cidade: ')).strip().title()

cidade = cidade.split()

santo = 'Santo' in cidade[0]

if santo == True:
    print('A cidade que digitou começa com Santo!')
else:
    print('A cidade que digitou NÃO começa com Santo!')
'''

    #25
'''
from random import choice

apelido = str(input('Oie, como posso te chamar? ')).title()
nome_completo = str(input(f'{apelido}, qual seu nome completo? ')).strip().title()

sobrenomes = ['Silva', 'Gomes', 'Martins', 'Oliveira', 'Costa', 'Santos', 'Souza', 'Alves']
aleatoriedade = choice(sobrenomes)

verifica = aleatoriedade in nome_completo

if verifica == True:
    print(f'{apelido}, você tem {aleatoriedade} no seu nome, né?!')
else:
    print(f'{apelido}, você não tem {aleatoriedade} no nome!')
'''

    #26
'''
frase = str(input('Digite uma frase: ')).strip().lower()
frase = frase.replace('á','a')
frase = frase.replace('ã','a')
frase = frase.replace('à','a')
frase = frase.replace('â','a')

conta_a = frase.count('a')
posicao_a = frase.find('a')+1

print(f'A letra "A" aparece na sua frase por {conta_a} vezes.\nA primeira a aparecer é na posição {posicao_a}.\nE a última é na posição {frase.rfind("a")+1}.')
'''

    #27
'''
nome = str(input('Digite seu nome: ')).title().strip()

nome = nome.split()

print(f'O primeiro nome é {nome[0]}. Já o último é: {nome[-1]}.')
'''
