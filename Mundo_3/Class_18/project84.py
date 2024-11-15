#AULA 18 - VARIÁVEIS COMPOSTAS -- LISTAS ANINHADAS []

#84 - LISTAS, Colocar nome e peso dentro de uma lista aninhada
# Não consegui fazer sozinho, me embananei pra descobrir o maior/menor peso. Não fazia ideia que era pra fazer dentro do while.

print('')
nome_peso = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Digite seu nome: ')).strip().title())
    dados.append(float(input('Digite seu peso: ')))
    if len(nome_peso) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    nome_peso.append(dados[:])
    dados.clear()
    verificação = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while verificação not in 'SN':
        verificação = str(input('Valor inválido! Digite novamente: ')).strip().upper()[0]
    if verificação == 'N':
        break
    print('')

print('')
print(f'Foram cadastradas {len(nome_peso)} pessoas.')
print(f'O maior peso é {maior}Kg, que é o peso de: ', end='')
for n in nome_peso:
    if n[1] == maior:
        print(f'[{n[0]}]', end='')
print('')
print(f'O menor peso é {menor}Kg, que é o peso de: ', end='')
for n in nome_peso:
    if n[1] == menor:
        print(f'[{n[0]}]', end='')
print('')
