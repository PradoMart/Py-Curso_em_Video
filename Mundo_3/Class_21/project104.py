#AULA 21 - FUNÇÕES

#104 - FUNÇÕES, leiaint()
#não tinha conseguido fazer, mas na resolução do 103, o guanabara usou o '.isnumeric()', daí apliquei ele aqui no programa.
def leiaint(numero):
    global n
    n = input(f'{numero}')
    while n.isnumeric() == False:
        n = input(f'\033[1;31mERRO! Digite novamente: \033[m')
    return n

n =  leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: \033[1;32m{n}\033[m')