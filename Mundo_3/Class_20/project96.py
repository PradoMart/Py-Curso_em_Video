#AULA 20 - FUNÇÕES

#96 - FUNÇÕES, Terreno
def molde (smt):
    print('-='*15)
    print(smt)
    print('-='*15)

def terreno (l,c):
    t = l * c
    print(f'Tendo {l} de largura e {c} de comprimento, a área do terreno é: {t:.2f}m².')

molde(f'{"MEDIÇÃO DE TERRENO":^30}')
while True:
    largura = float(input('Qual a largura (m²)? '))
    comprimento = float(input('Qual o comprimento (m²)? '))
    terreno(largura, comprimento)
    verificação = str(input('Quer continuar? [S/N] ')).upper()[0]
    while verificação not in 'SN':
        verificação = str(input('OPÇÃO INCORRETA! Quer continuar? [S/N] ')).upper()[0]
    if verificação == 'N':
        print()
        break
    print()
molde(f'{"FIM DA ANÁLISE":^30}')