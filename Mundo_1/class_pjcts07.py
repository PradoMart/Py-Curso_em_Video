#AULA 07
'''
nome = input('Digite seu nome: ')

print(f'Prazer {nome:=^20}'.upper())
'''

'''
n1 = int(input('Digite um número: '))
n2 = int(input('Agr o outro: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2

print(f'A soma é: {a} -- A subtração é: {s}  -- A divisão é: {d:.2f} -- A multiplicação é: {m} -- A divisão inteira é: {di} -- A potencia é: {e} -- O resto da dvisão é: {r}')
'''

# DESAFIOS DA AULA 07 -- DO 5 AO 13
    #05 e 06
'''
n = int(input('Coloque um número: '))
a = n - 1
s = n + 1
d = n * 2
t = n * 3
rq = n ** (1/2)

print(f'O antecessor de {n} é: {a} e o sucessor é: {s}')
print((f'O dobro de {n} é: {d}, o triplo é: {t} e a raiz quadrada é: {rq:.2f}'))
'''

    #07
'''
nome = input('Oi, com quem eu tô conversando? ')
nota1 = float(input(f'{nome}, qual é o valor da primeira nota? '))
nota2 = float(input(f'E a segunda foi quanto, {nome}? '))
media = (nota1 + nota2) / 2

if media >= 9:
    print(f'Parabéns, {nome}! Sua média foi: {media:.2f}. Vc tá super bem!');
elif media < 9 and media >= 7:
    print(f'{nome}, sua média está OK! Ela foi: {media:.2f}')
elif media < 7:
    print(f'Putz, você reprovou, {nome}! Sua média foi: {media:.2f}')
'''

    #08
'''
n = int(input('Digite o valor do metro: '))
c = n * 100
m = n * 1000

print(f'O valor de {n} metro(s) em centímetros é: {c} e {m} em milímetros.')
'''

    #09
'''
n = int(input('Oi, de qual número vc quer saber a tabuada?'))
rq = n ** (1/2)

print(f'{n} X 1 = {n*1}')
print(f'{n} X 2 = {n*2}')
print(f'{n} X 3 = {n*3}')
print(f'{n} X 4 = {n*4}')
print(f'{n} X 5 = {n*5}')
print(f'{n} X 6 = {n*6}')
print(f'{n} X 7 = {n*7}')
print(f'{n} X 8 = {n*8}')
print(f'{n} X 9 = {n*9}')
print(f'{n} X 10 = {n*10}')

irq = input(f'Você gostaria de saber a raiz quadrada de {n}? ')

if irq == 'S' or irq == 's' or irq == 'Sim' or irq == 'SIM' or irq == 'sim':
    print(f'A raiz quadrada de {n} é {rq:.2f}')
elif irq != 'S' or irq != 's' or irq != 'Sim' or irq != 'SIM' or irq != 'sim':
    print('Cálculo finalizado! Foi um prazer.')
'''
    #10
'''
dinheiro = float(input('Tem quanto no banco?'))
dolar = float(4.93)
conversao = dinheiro / dolar

print(f'Com R${dinheiro} você consegue comprar US${conversao:.2f}, porque o dólar hoje tá {dolar}.')
'''
    #11
'''
largura = float(input('Me diga, em metros, qual é a largura da sua parede? '))
altura = float(input('E a altura? Tbm em metros.'))
area = largura * altura
litro = area / 2

print(f'A área da sua parede é de: {area:.2f} metros². Pra pintá-la, você precisará de {litro:.2f} litros de tinta.')
'''

    #12
'''
preco = float(input('Qual o preço original do produto? '))
liquidacao = preco - (preco * 0.05)

print(f'O preço promocional do produto é R${liquidacao:.2f}. ')
'''

    #13
'''
salario = float(input('Quanto vc ganha hoje? '))
aumento = salario + (salario * 0.15)

print(f'O seu novo salário, com acréscimo de 15%, é de R${aumento:.2f}.')
'''

    #14
'''
c = float(input('Qual a temperatura em ºCelsius? '))
f = (c * 9/5) + 32

print(f'A temperatura em Fahrenheit é {f:.1f}. ')
'''

    #15
km_Rodados = float(input('Quantos km você rodou? '))
dias_Aluguel = int(input('E você ficou com o carro por quantos dias?'))

valor_Aluguel = dias_Aluguel * 60
valor_km_Rodados = km_Rodados * 0.15

soma_valor_total = valor_Aluguel + valor_km_Rodados

print(f'O valor a pagar por {dias_Aluguel} dias de aluguel mais {km_Rodados:.1f}km rodados é de: R${soma_valor_total}. ')



