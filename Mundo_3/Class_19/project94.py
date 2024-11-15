#AULA 19 - VARIÁVEIS COMPOSTAS -- DICIONÁRIO {}

#94 - DICIONÁRIOS, O mais complexo até agora
from time import sleep
#declarando a lista e dicionário
dados_dic = {}
dados_lis = []
#loop solicitando dados (nome, genero e idade). adiciona os dados do dicionário na lista e limpa o dicionário.
while True:
    dados_dic['Nome'] = str(input('Nome: ')).title().strip()
    dados_dic['Gênero'] = str(input('Gênero [F/M]: ')).title().strip()[0]
    while dados_dic['Gênero'] not in 'FM':
        dados_dic['Gênero'] = str(input('GÊNERO NÃO IDENTIFICADO! Por favor, digite [F/M]: ')).title().strip()[0]
    dados_dic['Idade'] = int(input('Idade: '))
    dados_lis.append(dados_dic.copy())
    dados_dic.clear
    verification = str(input('Quer continuar [S/N]: ')).title().strip()[0]
    while verification not in 'SN':
        verification = str(input('OPÇÃO INVÁLIDA! Quer continuar [S/N]: ')).title().strip()[0]
    if verification == 'N':
        print()
        break
    print( )
sleep(1)
print('\033[1;43m-='*6, 'ANÁLISE DE DADOS', '-='*6,'\033[m')
sleep(0.5)
print(f'- Há {len(dados_lis)} pessoa(s) no grupo.')
#usando for pra achar a média das idades e quais são as mulheres do grupo. depois mostra a informação
média = []
mulheres = []
for m in dados_lis:
    média.append(m['Idade'])
    if m['Gênero'] == 'F':
        mulheres.append(m['Nome'])

média_calculada = sum(média) / len(dados_lis)
sleep(0.5)
print(f'- A média de idade é {média_calculada:.2f} anos.')
sleep(0.5)
if len(mulheres) != 0:
    print(f'- Há {len(mulheres)} mulher(es) cadastrada(s): {mulheres}.')
else:
    print(f'- Não há mulheres cadastradas.')
#analisando quem está acima da média. adicionando as idades de quem tá acima da média na lista e mostrando os dados de cada uma delas.
acima_média = []
for m in dados_lis:
    if m['Idade'] > média_calculada:
        acima_média.append(m.copy())
sleep(0.5)
if len(acima_média) != 0:
    print(f'- Há {len(acima_média)} pessoa(s) com idade acima da média:')  
    for v in acima_média:
        for i, k in v.items():
            if i == 'Nome':
                print(f'  --> ', end='')
            print(f'{i} = {k}; ', end='')
        print()
else:
    print(f'- Não há pessoas com idade acima da média.')
print('\033[1;43m-='*6, 'ANÁLISE FINALIZADA', '-='*6,'\033[m')
print()