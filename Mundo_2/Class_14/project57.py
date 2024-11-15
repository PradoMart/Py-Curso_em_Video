#AULA 14 - LAÇO DE REPETIÇÃO WHILE

#57 - NOME, IDADE E SEXO
print('')
sexo = str(input('Digite seu gênero [M] ou [F] ')).strip().upper()[0]
while sexo != "M" and sexo != "F":
    print('')
    print('Opção errada!')
    sexo = str(input('Digite [M] ou [F]: ')).strip().upper()[0]
nome = str(input('Digite seu nome: ')).title().strip().split()[0]
idade = int(input('Digite sua idade: '))

if sexo == 'M':
    sexo = 'masculino'
else:
    sexo = 'feminino'
print('')
print(f'\033[30;107mPrazer, {nome}! Obrigado por dizer que se identifica com o gênero {sexo} e que tem {idade} anos.\033[m')