#AULA 19 - VARIÁVEIS COMPOSTAS -- DICIONÁRIO {}

#92 - DICIONÁRIOS, CTPS
from datetime import date
from time import sleep
print()
ano_atual = int(date.today().year)

dados = {}

dados['Nome'] = str(input('Nome: ')).title().strip()
ano_nascimento = int(input('Ano nascimento: '))
dados['Idade'] = ano_atual - ano_nascimento
dados['CTPS'] = int(input('Número CTPS - [Digite 0, caso não tenha.] - : '))

if dados['CTPS'] != 0:
    dados['Ano_Contratação'] = int(input('Ano contratação: '))
    while dados['Ano_Contratação'] <= ano_nascimento:
        dados['Ano_Contratação'] = int(input('ANO CONTRATAÇÃO INFERIOR AO NASCIMENTO! Digite novamente: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Idade_Aposentadoria'] = dados['Idade'] + ((dados['Ano_Contratação'] +  35) - date.today().year)
print()
print(f'\033[1m<'*5, 'RESULTADO', '>\033[m'*5)
for k, v in dados.items():
    sleep(0.5)
    print(f'[{k}] = {v}')
print()
