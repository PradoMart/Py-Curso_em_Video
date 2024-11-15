#AULA 13 - LAÇO DE REPETIÇÃO FOR

#54 - ANO DE NASCIMENTO
from datetime import date
print('')
print('SOFTWARE DE MAIORIDADE PRA RESTAURANTES!')
print('')

ano_atual = date.today().year
mes_atual = date.today().month
dia_atual = date.today().day

contador = 0

qtde_pessoas = int(input('Quantas pessoas estarão na mesa? '))
print('')

for ano in range(1,qtde_pessoas+1):
    mes_ano_nascimento = str(input(f'Qual a {ano}ª data de nascimento? Digite no formato "DD/MM/AAAA" : '))
    if ano_atual - int(mes_ano_nascimento[6:]) < 21:
        contador += 1
    elif ano_atual - int(mes_ano_nascimento[6:]) == 21:
        if int(mes_ano_nascimento[3:5]) > mes_atual:
            contador += 1
        elif int(mes_ano_nascimento[3:5]) == mes_atual:
            if int(mes_ano_nascimento[:2]) <= dia_atual:
                contador += 1

print('')
if contador > 1 and qtde_pessoas - contador > 1:
    print(f'{contador} pessoas são menores de idade! Enquanto {qtde_pessoas - contador} já são maiores de idade.')
elif contador > 1 and qtde_pessoas - contador == 1:
    print(f'{contador} pessoas são menores de idade! Enquanto apenas {qtde_pessoas - contador} é maior de idade.')
elif contador == 1 and qtde_pessoas - contador > 1:
    print(f'Apenas {contador} pessoa é menor de idade! Enquanto {qtde_pessoas - contador} já são maiores de idade!')
elif contador == 1 and qtde_pessoas - contador == 1:
    print(f'Apenas {contador} pessoa é menor de idade! Assim como há também apenas {qtde_pessoas - contador} maior de idade!')
