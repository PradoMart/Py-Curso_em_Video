#AULA 14 - LAÇO DE REPETIÇÃO WHILE

#62 - MELHORANDO O EXERCÍCIO 61 - PROGRESSÃO ARITMÉTICA
print('')
print('\033[1;30;107m---PROGRESSÃO ARITMÉTICA---\033[m')
print('')
inicial = int(input('Qual o valor inicial da PA: '))
razão = int(input('Qual é a razão: '))
termo = inicial
contador = 1
total = 0
mais = int(input('Quantos termos você quer ver: '))

while mais == 0:
    print('\033[33mNesse momento, o ZERO não é válido!\033[m')
    mais = int(input('\033[1mDigite um novo valor:\033[m '))
print('')

while mais > 0:
    total += mais
    while contador <= total:
        print(termo, end= ' - ')
        termo += razão
        contador += 1
    print('PAUSA')
    print('')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
    print('')
print(f'\033[1;30;107mPROGRESSÃO FINALIZADA! Foi exibido {total} termos.\033[m')
