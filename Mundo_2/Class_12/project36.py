#AULA 12 - CONDIÇÕES ANINHADAS

#36 - EMPRÉSTIMO BANCÁRIO
from time import sleep

print('')
nome = str(input('Oi, tudo bem? Que bom ter você aqui! Pra começarmos, me conta seu nome? ')).strip().title()
print('')
valor_casa = float(input('Qual o valor da casa que está querendo? '))
print('')
salario = float(input('E quanto você tá ganhando por mês? '))
print('')
tempo_parcelas = int(input('Em quantos anos você tá pensando em financiar? '))
print('')
sleep(1.5)

valor_parcela = (valor_casa / tempo_parcelas) / 12
limite_parcela_salario = (valor_parcela / salario) * 100

if limite_parcela_salario <= 30:
    print(f'{nome}, seu crédito foi \033[1;32mAPROVADO\033[m! A sua casa de R${int(valor_casa)} mil será paga em {tempo_parcelas} anos, com uma parcela de R${valor_parcela:.2f} por mês, que corresponde a {limite_parcela_salario:.2f}% do seu salário.')
elif limite_parcela_salario > 30 and limite_parcela_salario <= 40:
    print(f'{nome}, no momento, \033[1;33mnão conseguimos aprovar seu crédito\033[m, porque ele excede \033[1;33m{limite_parcela_salario - 30:.2f}%\033[m do limite de desconto da parcela sobre o seu salário.\n Nossa sugestão é: Escolher outro imóvel ou Aumentar sua renda.')
else:
    print(f'Infelizmente, {nome}, \033[1;31mnão podemos aprovar seu crédito\033[m, porque a parcela consome \033[1;31m{limite_parcela_salario:.2f}%\033[m do seu salário.')

