#AULA 14 - LAÇO DE REPETIÇÃO WHILE

#65 - LENDO VÁRIOS NÚMEROS, DIZENDO A MÉDIA E IMPLEMENTANDO LOOP (só não consegui fazer o maior/menor)
print('')
numero = média = contagem = limitador = 0
set = 1
lista = []
repetições = int(input('Quantos números você quer colocar? '))
print('')

while repetições != 999:
    limitador += repetições
    while set <= limitador:
        numero = int(input('Digite um número: '))
        média += numero
        contagem += 1
        set += 1
        lista.append(numero)
    calc_média = média / contagem
    print('')
    print(f'Você digitou {contagem} números, a média entre eles é: {calc_média:.2f}. O maior número digitado foi {max(lista)}, já o menor foi {min(lista)}.')
    print('')
    repetições = int(input('Quer analisar mais quantos números? \nSe preferir sair, digite 999: '))
    print('')
    média = 0
    contagem = 0
    lista.clear()
else:
    print('PROGRAMA FINALIZADO!')
