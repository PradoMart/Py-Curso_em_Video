import mdl109 as md

num = float(input('NÚMERO: '))
print(f'O dobro é {md.dobro(num, True)}. Já a metade é {md.metade(num, True)}')
perc_acima = float(input('% mais: '))
perc_abaixo = float(input('% menor: '))
print(f'Aumentando em {perc_acima}%, temos {md.aumentar(n = num, perc = perc_acima, form = True)}.\nReduzindo em {perc_abaixo}%, temos {md.reduzir(num, perc_abaixo, True)}.')
