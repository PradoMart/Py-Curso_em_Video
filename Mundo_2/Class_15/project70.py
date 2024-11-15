#AULA 15 - INTERROMPENDO LAÇO DE REPETIÇÃO

#70 - SEM USAR FLAG NO LAÇO, nome e preço do produto

list = []
list1000 = []
listprod = []

while True:
    produto = str(input('Nome do produto: ')).strip().title()
    preço = float(input('Preço do produto: '))
    list.append(preço)
    listprod.append(produto)
    if preço > 1000:
        list1000.append(preço)
    continuar = str(input('Deseja continuar: [S/N]? ')).strip().upper()[0]
    while continuar != "S" and continuar != "N":
        continuar = str(input('OPÇÃO INVÁLIDA! --> Deseja continuar: [S/N] ? ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('')

print('')
print(f'O total gasto foi de R${sum(list):.2f}. Há {len(list1000)} produto(s) que custa(m) mais de R$1000. O produto mais barato é {listprod[list.index(min(list))]}.')
