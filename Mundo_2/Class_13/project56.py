#AULA 13 - LAÇO DE REPETIÇÃO FOR

#56 - NOME, IDADE E SEXO
from time import sleep
print('')
print('\033[1;35;40m*** ANÁLISE DE DADOS ***\033[m')
print('')
pessoas = int(input('Quantas pessoas estão no grupo? '))
print('')
soma_idades = 0
media_idades = 0
nome_velho = ''
idade_velho = 0
total_mulheres_under20 = 0
sleep(0.5)
for repete in range(1, pessoas+1):
    print(f'\033[1;30;107m--- {repete}ª PESSOA ---\033[m')
    nome = str(input('Nome: ').strip().title())
    idade = int(input('Idade: '))
    genero = str(input('Gênero - [M/F]: ').strip().upper())
    soma_idades += idade
    if repete == 1 and genero[0] == 'M':
        idade_velho = idade
        nome_velho = nome
    if genero[0] == 'M' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if genero[0] == 'F' and idade < 20:
        total_mulheres_under20 += 1
    print('')

media_idades = soma_idades / pessoas
sleep(0.5)
print(f'A média de idade do grupo é de {media_idades:.2f} anos.')
sleep(0.5)
print(f'O homem mais velho é o {nome_velho}, ele tem {idade_velho} anos.')
sleep(0.5)
print(f'No grupo, há {total_mulheres_under20} mulheres com menos de vinte anos.')
