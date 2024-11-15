#treinando um pouco de dicinoários

pessoas = {'nome': 'Armando', 'idade': 25, 'genero': 'M'}

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print()

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 60
pessoas['idade'] = 22
print(pessoas.items())
