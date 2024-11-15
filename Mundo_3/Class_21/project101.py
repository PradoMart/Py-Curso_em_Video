#AULA 21 - FUNÇÕES

#101 - FUNÇÕES, voto
from datetime import date
print()
def voto(ano):
    global idade
    ano_atual = date.today().year
    idade = ano_atual - ano
    
    if idade < 16:
        return "NEGADO"
    elif 16 <= idade < 18 or idade > 65 :
        return "OPCIONAL"
    else:
        return  "OBRIGATÓRIO"

resultado = voto(int(input('Em que ano você nasceu? ')))
print(f'Com {idade} anos, VOTO {resultado}.')