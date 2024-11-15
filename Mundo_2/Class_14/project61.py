#AULA 14 - LAÇO DE REPETIÇÃO WHILE

#61 - REFAZENDO EXERCÍCIO 51 PROGRESSÃO ARITMÉTICA

#51 - PROGRESSÃO ARITMÉTICA
'''print('')
inicial = int(input('Qual o valor inicial da Progressão Aritmética? '))
razao = int(input('Qual será a razão? '))
final = int(input('Quantos números você gostaria de ver da Progressão Aritmética? '))
enesimo = inicial + final * razao
print('')
for pa in range(inicial,enesimo,razao):
    print(f'\033[1;30;107m{pa}\033[m', end= ' - ')
print('FIM!')'''

print('')
inicial = int(input('Qual o valor inicial da PA? '))
razao = int(input('Qual será a razão? '))
final = int(input('Quantos termos você quer ver da PA? '))
termo = inicial
contador = 1
print('')

while contador <= final:
    print(f'{termo}', end=' - ')
    termo += razao
    contador += 1
print('FIM!')
