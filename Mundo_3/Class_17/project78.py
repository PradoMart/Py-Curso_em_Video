#AULA 17 - VARIÁVEIS COMPOSTAS -- LISTAS []

#78 - LISTAS, Armazenando valores
print('')
values = []
maxi = []
mini = []
for x in range(0,5):
    values.append(int(input('Digite um número: ')))
print('')

for i, v in enumerate(values):
    if v == max(values):
        maxi.append(i+1)
    elif v == min(values):
        mini.append(i+1)
print(f'O maior valor é {max(values)}, posição: {maxi}')
print(f'O menor valor é {min(values)}, posição: {mini}')
#daria pra fazer igual ao guanabara, repetindo o for, mas eu preferi fazer apenas um for e deixar as posições em listas