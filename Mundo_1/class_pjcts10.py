#AULA 10 - CONDIÇÕES // SIMPLES, COMPOSTA e SIMPLIFICADA


#treino durante a aula
'''
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

imc = peso / (altura * altura)

#print('imc bom ' if imc <=18 else 'vai emagrecer!')
if imc <= 18:
    print('\033[1;30;42mIMC bom!\033[m')
else:
    print('\033[1;30;41mVai emagrecer!\033[m')
print(f'Seu IMC tá em: \033[1;30;107m{imc:.2f}\033[m')
'''

#DESAFIOS 28 - 34
    
    #28
'''
from random import randint
aleatorio = randint(0,5)

palpite = int(input('Chute um número: '))

#if palpite == aleatorio:
#   print('ACERTOU!')
#else:
#   print('ERROU!')

while palpite != aleatorio:
    palpite = int(input('\033[1;30;41mErrou!\033[m Chute um novo número: '))
else:
    print(f'\033[1;30;42mACERTOU!\033[m O número era {aleatorio}!')
'''


    #29
'''
from time import sleep
velocidade = float(input('\033[7;30;107mQual é a velocidade?\033[m '))
multa = (velocidade - 80) * 7

sleep(0.5)
print('\033[30;45m...\033[m')
sleep(0.5)
print('\033[30;46m..\033[m')
sleep(0.5)
print('\033[30;43m.\033[m')
sleep(0.5)
print('')

if velocidade <= 80:
    print(f'\033[1;32mCondução segura!\033[m Velocidade dentro do limite da via!')
else:
    print(f'\033[1;31mVelocidade acima do limite da via!\033[m \033[1;30;41mA multa é de R${multa}\033[m')
'''

    #30
'''
#se um número é divisivel por 2 e não sobra nada, ele é par! Se sobrar, é impar!
numero = int(input('Digite um número: '))

verifica = (numero % 2)

if verifica == 0:
    print('\033[1;30;45mEste número é par!\033[m')
else:
    print('\033[1;30;46mEste número é ímpar!\033[m')
    '''

    #31
'''
km_viagem = float(input('Quantos km dará sua viagem? '))

if km_viagem <= 200:
    print(f'O preço da passagem é \033[1;33mR${km_viagem * 0.50:.2f}\033[m.')
else:
    print(f'O preço da passagem é \033[1;33mR${km_viagem * 0.45:.2f}\033[m')
'''

    #32
'''
ano = input('Qual ano você quer verificar? ')

verifica = int(ano[2:])
dezena_ano = verifica % 4
#print(verifica,dezena_ano)

verifica__ = int(ano) % 400

if verifica != 00 and dezena_ano == 0:
    print(f'O ano {ano} \033[1;32mÉ\033[m um ano bissexto.')
elif verifica == 00 and verifica__ == 0:
    print(f'O ano {ano} \033[1;32mÉ\033[m um ano bissexto.')
else:
    print(f'O ano {ano} \033[1;31mNÃO É\033[m bissexto.')

#Módulo Calendar pra saber se um ano é bissexto sem fórmular
#import calendar
#ano = int(input('ano ' ))
#ano6 = calendar.isleap(ano)
#print(ano6)
'''

    #33 -- não consegui resolver sozinho, olhei os comentários e tinha ficado faltando o and no if.
'''
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

#qual é o maior dos três? E o menor?

lista = [n1,n2,n3]
lista.sort()
print(f'O menor valor é: \033[1;30;41m{lista[0]}\033[m Já o maior é: \033[1;30;42m{lista[2]}\033[m')


#jeito mais complicado!
#if n1 > n2 and n1 > n3:
#    print(f'O maior número é: {n1}')
#elif n2 > n1 and n2 > n3:
#    print(f'O maior número é: {n2}')
#elif n3 > n2 and n3 > n1:
#    print(f'O maior número é: {n3}')

#if n1 < n2 and n1 < n3:
#    print(f'O menor número é: {n1}')
#elif n2 < n3 and n2 < n1:
#    print(f'O menor número é: {n2}')
#elif n3 < n1 and n3 < n2:
#    print(f'O menor número é: {n3}')
'''

    #34
'''
salario = float(input('Qual seu salário? '))

if salario <= 1250:
    print(f'Seu aumento será de \033[1;34mR${salario * 0.15:.2f}\033[m e o novo salário será \033[1;32mR${(salario * 0.15) + salario:.2f}\033[m.')
else:
    print(f'Seu aumento será de \033[1;34mR${salario * 0.10:.2f}\033[m e o novo salário será \033[1;32mR${(salario * 0.10) + salario:.2f}\033[m')
'''

    #35 - não consegui fazer sozinho, ohei nos comentários.
from time import sleep

a = float(input('Digite o tamanho da \033[1;30;107mprimeira\033[m reta: '))
b = float(input('Digite o tamanho da \033[1;30;45msegunda\033[m reta: '))
c = float(input('Digite o tamanho da \033[1;30;46mterceira\033[m reta: '))

ab = a + b
ac = a + c
bc = b + c

sleep(0.5)
print('\033[1;33mCalculando Trigonometria! Por favor, aguarde!\033[m')
sleep(1)
print('\033[1;33m...\033[m')
sleep(0.5)
print('\033[1;33m..\033[m')
sleep(0.5)
print('\033[1;33m.\033[m')
sleep(1)

print('\033[1;33mCÁLCULO FINALIZADO! Obrigado por aguardar!\033[m')
print('')
sleep(2)

if ab > c and ac > b and bc > a:
    print(f'As retas \033[1;30;107m{a:.0f}\033[m,\033[1;30;45m{b:.0f}\033[m,\033[1;30;46m{c:.0f}\033[m \033[1;32mformam\033[m um triângulo!')
else:
    print(f'As retas \033[1;30;107m{a:.0f}\033[m,\033[1;30;45m{b:.0f}\033[m,\033[1;30;46m{c:.0f}\033[m \033[1;31mnão formam\033[m um triângulo!')
