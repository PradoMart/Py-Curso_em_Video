def aumentar(n, perc):
     novo_valor = (n * (perc/100)) + n
     return novo_valor

def reduzir(n, perc):
     novo_valor = n - (n * (perc/100))
     return novo_valor

def dobro(n):
     novo_valor = n * 2
     return novo_valor

def metade(n):
     novo_valor = n / 2
     return novo_valor
