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

def metade(n, form = False):
     novo_valor = n / 2
     if form == True:
          novo_valor = moeda(novo_valor)
     return novo_valor

def moeda(n = 0, formato = "R$"):
     return str(f'{formato}{n:.2f}').replace('.',',')