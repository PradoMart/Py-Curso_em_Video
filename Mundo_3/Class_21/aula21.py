#INTERACTIVE HELP
'''help(print())'''
#mais uma forma de pedir a documentação de um método
'''print(input.__doc__)'''

#DOCSTRINGS
'''def contador(i,f,p):
    """_summary_
    -> faz contagem e mostra na tela.
    Args:
        i (_type_): início da contagem
        f (_type_): fim da contagem
        p (_type_): passo da contagem
    """
    for i in range(i,f,p):
        print(f'{i} ',end='')
    print('fim!')

contador(3,15,3)
help(contador)'''

#ARGUMENTOS OPCIONAIS
'''def somar(a=0,b=0,c=0):
    """_summary_ Função que soma 3 números
    Args:
        a (_type_): n1
        b (_type_): n2
        c (_type_): n3
    """
    s = a + b + c
    print(f'A soma de {a,b,c} é {s}.')

somar(4,6)'''

#ESCOPO DE VARIÁVEIS
'''
Localidade de funcionamento da variável (GLOBAL / LOCAL)
Se tiver dentro da função é LOCAL.
Se tiver fora da função é GLOBAL.
Pra mudar o valor de uma global dentro da função, usar o atributo "GLOBAL" #variável

'''

#RETORNO DE RESULTADOS - RETURN
'''
Ideal pra personalizar a resposta. Não usa o print dentro da função.

def somar(a=0, b=0, c=0):
    s = a+b+c
    return s

r1 = somar(3,4,2)
r2 = somar(22,44)
print(f'A soma foi {r1} e {r2}')
'''
