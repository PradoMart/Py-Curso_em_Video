def aumentar(n, perc, form = False):
     novo_valor = (n * (perc/100)) + n
     if form == True:
          novo_valor = moeda(novo_valor)
     return novo_valor

def reduzir(n, perc, form = False):
     novo_valor = n - (n * (perc/100))
     if form == True:
          novo_valor = moeda(novo_valor)
     return novo_valor

def dobro(n, form = False):
     novo_valor = n * 2
     if form == True:
          novo_valor = moeda(novo_valor)
     return novo_valor

def updt_value(n, form = False):
     novo_valor = n
     if form == True:
          novo_valor = moeda(novo_valor)
     return novo_valor

def metade(n, form = False):
     novo_valor = n / 2
     if form == True:
          novo_valor = moeda(novo_valor)
     return novo_valor

def moeda(n = 0, formato = "R$"):
     return str(f'{formato}{n:.2f}').replace('.',',')

def resumo(n=0, perc_abaixo=0, perc_acima=0, form = False):
     print('-' * 30)
     print('RESUMO DO VALOR'.center(30))
     print('-' * 30)
     
     print(f'{"Preço analisado: ":<20} {updt_value(n, form)}')
     print(f'{"Dobro  do preço:":<20} {dobro(n,form)}')
     print(f'{"Metade do preço:":<20} {metade(n,form)}')
     print(f'{perc_abaixo}{"% de redução:":<17} {reduzir(n,perc_abaixo,form)}')
     print(f'{perc_acima}{"% de aumento:":<17} {aumentar(n,perc_acima,form)}')
     print('-' * 30)
     print()
     