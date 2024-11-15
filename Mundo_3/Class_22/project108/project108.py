import mdl108 as md

num = float(input('NÚMERO: '))
print(f'O dobro é {md.moeda(md.dobro(num))}. Já a metade é {md.moeda(md.metade(num))}')
perc_acima = float(input('% mais: '))
perc_abaixo = float(input('% menor: '))
print(f'Aumentando em {perc_acima}%, temos {md.moeda(md.aumentar(n = num,perc = perc_acima))}. Reduzindo por {perc_abaixo}%, temos {md.moeda(md.reduzir(num, perc_abaixo))}')