#AULA 20 - FUNÇÕES

#98 - FUNÇÕES, contador
#não tinha conseguido aplicar os sleep por conta do flush.

from time import sleep
def contagem(início, fim, passo):
    print()
    if passo == 0:
        passo = int(1)
    if início > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
        passo1 = passo
        if passo < 0:
            passo1 = passo * -1
        print(f'Contagem de {início} até {fim+1}, de {passo1} em {passo1}:')
    if início < fim:
        fim += 1
        if passo < 0:
            passo *= -1
        passo1 = passo
        print(f'Contagem de {início} até {fim-1}, de {passo} em {passo}:')
    for i in range(início, fim, passo):
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')
    print('-='*20)
    
contagem(1,10,1)
contagem(10,0,-2)
print()
print(f'-='*2,'AGORA É SUA VEZ, PERSONALIZE A CONTAGEM!', '-='*2)
while True:
    print()
    contagem(
        int(input(f'{"INÍCIO: ":<8}')), int(input(f'{"FIM: ":<8}')), int(input(f'{"PASSO: ":<8}'))
        )
    verificação = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while verificação not in 'SN':
        verificação = str(input('OPÇÃO INVÁLIDA! Digite [S/N]: ')).upper().strip()[0]
    if verificação == 'N':
        print('-='*2,'FIM', '-='*2)
        break