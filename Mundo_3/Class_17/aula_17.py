#PRIMEIROS PASSOS COM LISTAS
'''num = [2,34,6,7]

num.insert(2,5)
num.append(80)
num.pop(3) #removeu o nmr 6 que tava na posição 3.
num.remove(80) #remove o elemento
num.sort(reverse=True)
print(num)'''

#BRINCANDO COM APPEND COM ALEATORIO E INPUT
'''from random import randint
valores = []

for smt in range(0,2):
    valores.append(randint(0,5))
    valores.append(int(input('Digite um valor: ')))
print(valores)

for position, number in enumerate(valores):
    print(f'Na posição {position+1} encontra-se o número {number}.')'''

#COPIANDO E CONECTANDO A UMA LISTA
from random import randint
valores = []

for smt in range(0,4):
    #valores.append(randint(0,5))
    valores.append(int(input('Digite um valor: ')))

valores_conexão = valores[:]
valores_conexão[3] = 7
print(f'Os números da lista VALORES são: {valores}')
print(f'Os números da lista VALORES_CONEXÃO são: {valores_conexão}')