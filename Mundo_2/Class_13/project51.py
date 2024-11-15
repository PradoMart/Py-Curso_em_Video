#AULA 13 - LAÇO DE REPETIÇÃO FOR

#51 - PROGRESSÃO ARITMÉTICA - Não consegui fazer sozinho
print('')
inicial = int(input('Qual o valor inicial da Progressão Aritmética? '))
razao = int(input('Qual será a razão? '))
final = int(input('Quantos números você gostaria de ver da Progressão Aritmética? '))
enesimo = inicial + final * razao
print('')
for pa in range(inicial,enesimo,razao):
    print(f'\033[1;30;107m{pa}\033[m', end= ' - ')
print('FIM!')
