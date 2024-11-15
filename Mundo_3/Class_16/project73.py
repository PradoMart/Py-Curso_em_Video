#AULA 16 - VARIÁVEIS COMPOSTAS -- TUPLAS ()

#73 - TUPLAS, tabela do brasileiro
print('')
print('TABELA DO BRASILEIRÃO')
lista = ('Botafogo', 'Flamengo', 'Palmeiras', 'Grêmio', 'Fluminense', 'Bragantino', 'Athlético-PR', 'São Paulo', 'Cuiabá', 'Cruzeiro', 'Fortaleza', 'Internacional', 'Atlético-MG', 'Corinthians', 'Santos', 'Goiás', 'Bahia', 'Coritiba', 'América-MG', 'Vasco da Gama')

qtos = int(input('Quantos times da tabela vc quer ver: '))

print('')
print(f'Esses são os {qtos} melhores: {lista[:qtos]}\n')
print('')
print(f'Os que estão na zona do rebaixamento: {lista[-4:]}')
print('')
print(f'A tabela de A-Z: {sorted(lista)}')
print('')

time = str(input('Digite o nome de um time q eu te mostro em que posição ele está: ')).strip().title()
while time not in lista:
    time = str(input('Time não existente, digite novamente: ')).strip().title()
print(f'O {time} está na {lista.index(time)+1}º posição.')
