def leia_dinheiro(valor):
    valido = True
    while valido:
        v = str(input(valor)).strip().replace(',','.')
        if v.isalpha() or v == "":
            print(f"ERRO! '{v.upper()}' não é um número.")
        else:
            valido = False
            return float(v)