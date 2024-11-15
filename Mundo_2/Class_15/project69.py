#AULA 15 - INTERROMPENDO LAÇO DE REPETIÇÃO

#69 - SEM USAR FLAG NO LAÇO
print('')
maior18 = []
homens = []
mulheres20 = []
while True:
    idade = int(input('Digite sua idade: '))
    while idade < 0:
        print('NÃO EXISTE IDADE NEGATIVA, BENJAMIN BUTTON!')
        idade = int(input('Digite sua idade: '))
    genero = str(input('Com qual gênero você se identifica: [M/F]? ')).strip().upper()[0]
    while genero != 'M' and genero != 'F':
        print('GÊNERO NÃO ACEITO!')
        genero = str(input('Digite novamente o seu gênero [M/F]: ')).strip().upper()[0]
    continuar = str(input('Quer continuar: [S/N]? ')).strip().upper()[0]
    while continuar not in 'SN':
        print('OPÇÃO INVÁLIDA!')
        continuar = str(input('Quer continuar: [S/N]? ')).strip().upper()[0]
    print('')
    if idade > 18:
        maior18.append(idade)
    if genero == 'M':
        homens.append(genero)
    if genero == 'F' and idade < 20:
        mulheres20.append(idade)
    if continuar == 'N':
        break
#if len(maior18) and len(homens) and len(mulheres20) > 1:
print(f'Há {len(maior18)} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {len(homens)} homens.')
print(f'E há {len(mulheres20)} mulheres com menos de 20 anos.')
