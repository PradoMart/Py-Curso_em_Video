#AULA 19 - VARIÁVEIS COMPOSTAS -- DICIONÁRIO {}

#90 - DICIONÁRIOS, NOME E MÉDIA
print()
dados = {}

dados['Nome'] = str(input('Nome: ')).title().strip()
dados['Média'] = float(input(f'A média de {dados["Nome"]} é: '))
if dados['Média'] < 7:
    dados['Situação'] = '\033[1;31mReprovado\033[m'
else:
    dados['Situação'] = '\033[1;32mAprovado\033[m'
print('-='*10)
for k, v in dados.items():
    print(f'{k} é {v}')
print()
