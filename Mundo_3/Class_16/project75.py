#AULA 16 - VARIÁVEIS COMPOSTAS -- TUPLAS ()

#75 - TUPLAS, numeros armazenados

# na minha solução abaixo fiz sem os atributos count e index.
'''print('')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))

lista = (n1, n2, n3, n4)

print(lista)
cont9 = 0
list3 = 10
pares = []
for l, n in enumerate(lista):
    if n == 9:
        cont9 += 1
    if n % 2 == 0:
        pares.append(n)

for l, n in enumerate(lista):
    if n == 3:
        list3 = l

if list3 == 10:
    list3 = 'N/A'
print('')
print(f'O número 9 apareceu {cont9} vez(es).\nO primeiro número 3 foi digitado na posição: {list3}.\nDentre os digitados, os seguintes são pares: {sorted(pares)}.')'''

# Programa refeito com count, index e colocando as variáveis já dentro da tupla
print('')
lista = (
         int(input('Digite o primeiro número: ')),
         int(input('Digite o segundo número: ')),
         int(input('Digite o terceiro número: ')),
         int(input('Digite o quarto número: '))
         )
print('')
if 9 in lista:
    print(f'O número 9 apareceu {lista.count(9)} vez(es).')
else:
    print(f'O número 9 não foi digitado.')
if 3 in lista:
    print(f'Já o número 3 apareceu na {lista.index(3)+1}ª posição.')
else:
    print(f'O número 3 não foi digitado.')

pares = []

for n in lista:
    if n % 2 == 0:
        pares.append(n)
if len(pares) == 1:
    print(f'O número par digitado foi: ', end='')
    for n in pares:
        print(n)
else:
    print(f'Os números pares digitados são: ', end='')
    for n in pares:
        print(f'{n}', end=' ')
