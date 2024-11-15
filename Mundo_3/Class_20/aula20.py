#funções def

#primeiro exemplo --> função sem parametro
'''def lin():
    print('-'*30)
lin()
print(f'{"CURSO EM VÍDO":^30}')
lin()

lin()
print(f'{"CADASTRO DE PESSOAS":^30}')
lin()'''

#segundo exemplo --> função com parametro

'''def mensagem(msg):
    print('-'*30)
    print(f'{msg.upper():^30}')
    print('-'*30)

mensagem(f'{"CURSO EM VÍDEO":^30}')
#me aventurando com um input
mensagem(str(input('DIGITE ALGO: ')))'''


#terceiro exemplo --> função com +1 parametro
'''def calcula(a,b):
    t = a + b
    print(f'A = {a}')
    print(f'B = {b}')
    print(f'A + B = {t}')
    print()

calcula(3,4)
calcula(
    int(input('Digite o primeiro número: ')),
    int(input('Digite o segundo número: '))
)'''

#quarto exemplo --> função com vários parametros (EMPACOTAMENTO), sem saber o tamanho na declaração da função
'''def calc_n (*núm):
    print(f'A soma de ', end='')
    for n in núm:
        print(f'{n} ', end='')
    print(f'é {sum(núm)}')

calc_n(4,5,6,7)'''

#quinto exemplo --> função usando lista no parametro
#5.1
'''def dobra (lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    print(lista)

valores = [5,6,7,8]
dobra(valores)'''

#5.2
def dobra (lista):
    for x, y in enumerate(range(0, len(lista))):
        lista[x] *= 2
    print(lista)

conteúdo = []
while True:
    verificação = (int(input('Qual número que duplicar? [TO STOP: 999] ')))
    if verificação == 999:
        break
    else:
        conteúdo.append(verificação)
dobra(conteúdo)
