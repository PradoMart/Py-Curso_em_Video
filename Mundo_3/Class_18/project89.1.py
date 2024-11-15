#AULA 18 - VARIÁVEIS COMPOSTAS -- LISTAS ANINHADAS []

#89 - LISTAS, BOLETIN

nome_notas = []
notas = []
print()
while True:
    nome = str(input('Nome do aluno: ')).strip().title()
    qtde_notas = int(input('Quantas notas? '))
    for n in range (1, qtde_notas+1):
        notas.append(float(input(f'Qual a {n}ª nota? ')))
    media = sum(notas) / qtde_notas
    nome_notas.append([nome, notas[:], media])
    notas.clear()
    verification = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while verification not in 'SN':
        verification = str(input(f'NÃO COMPREENDI! Quer continuar? [S/N] ')).strip().upper()[0]
    if verification == 'N':
        print()
        break
    print()
print()
print(f'\033[1m{"Nº":<3} {"NOME":<10} {"MÉDIA":>5}\033[m')
for i, a in enumerate(nome_notas):
    print(f'{i:<3} {a[0]:<10} {a[2]:>4.1f}')

while True:
    print()
    aluno = int(input(f'Quer ver a nota de qual aluno? \033[1m[P/ SAIR: 999] \033[m'))
    while aluno > len(nome_notas) -1 and aluno != 999:
        aluno = int(input(f'Aluno não identificado! DIGITE NOVAMENTE: '))
    if aluno == 999:
        print()
        print(f'\033[1m{"<"*5} VOLTE SEMPRE {">"*5}\033[m')
        break
    else:
        print(f'As notas de {nome_notas[aluno][0]} foram: {nome_notas[aluno][1]}')
