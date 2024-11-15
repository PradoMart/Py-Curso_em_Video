#AULA 20 - FUNÇÕES

#97 - FUNÇÕES, tamanho adptável
def escreva(smt):
    print('~'*(len(smt)+4))
    print(f'  {smt}  ')
    print('~'*(len(smt)+4))

for i in range(0,3):
    escreva(f'{str(input("Digite uma mensagem: ")).upper()}')