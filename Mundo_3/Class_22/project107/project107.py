import moedas as md

num = float(input('NÚMERO: '))
print(f'O dobro de {num} é {md.dobro(num)}. Já a metade é {md.metade(num)}')
perc_acima = float(input('% mais: '))
perc_abaixo = float(input('% menor: '))
print(f'Aumentando em {perc_acima}%, temos {md.aumentar(n = num,perc = perc_acima):.2f}. Reduzindo por {perc_abaixo}%, temos {md.reduzir(num, perc_abaixo):.2f}')