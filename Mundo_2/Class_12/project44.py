#AULA 12 - CONDIÇÕES ANINHADAS

#44 - VALOR A SER PAGO POR PRODUTO
from time import sleep
print('')
print('\033[1;30;46mSEJA BEM-VINDO À NMATOS OUTLET!\033[m')
print('-'*31)
sleep(1)
print('\033[1;30;46mAqui você encontra tudo no precin!\033[m')
print('')
sleep(1)

preco_produto = str(input('\033[1mQual o valor total dos produtos que pegou?\033[m ')).strip().replace(',','.')
preco_produto = float(preco_produto)
sleep(1)
print('')

print(f'Aqui na loja temos os seguintes modos de pagamento:')
sleep(1)
print(' \033[1;30;42m1) à vista, no dinheiro ou cheque, com desconto de 10%;\033[m')
sleep(1.5)
print('  \033[1;30;44m2) à vista no cartão com desconto de 5%;\033[m')
sleep(1.5)
print('   \033[1;30;43m3) em até 2x sem juros no cartão de crédito;\033[m')
sleep(1.5)
print('    \033[1;30;41m4) 3x ou mais no cartão, com juros de 20%;\033[m')
print('')
sleep(2)

pagamento = str(input('Qual o método que mais te atende pra pagar esta conta? \033[1;30;107mDigite o número da opção!\033[m ')).strip()
pagamento = int(pagamento)
print('')
sleep(1.5)

if pagamento == 1:
    desconto = (preco_produto * 0.1)
    preco_produto = preco_produto - desconto
    print(f'Você ganhou \033[1;32mR${desconto:.2f}\033[m de desconto. O preço a ser pago é de \033[1;30;42mR${preco_produto:.2f}\033[m!')
elif pagamento == 2:
    desconto = (preco_produto * 0.05)
    preco_produto = preco_produto - desconto
    print(f'Você ganhou \033[1;34mR${desconto:.2f}\033[m de desconto. O preço a ser pago é de \033[1;30;44mR${preco_produto:.2f}\033[m!')
elif pagamento == 3:
    print(f'O preço a ser pago é de \033[1;30;43mR${preco_produto:.2f}\033[m, você pode dividir esse valor em até \033[1;33m2x sem juros\033[m!')
elif pagamento == 4:
    juros = (preco_produto * 0.2)
    preco_produto = preco_produto + juros
    nmr_parcelas = int(input('Em quantas vezes você quer dividir esta compra? '))
    while 1 <= nmr_parcelas < 3:
        print(f'Não podemos parcelar em {nmr_parcelas}x, porque é menor que 3x.', end=' ')
        nmr_parcelas = int(input('Por favor, insira um novo número de parcelas: '))
    print('')
    print(f'Dividindo em 3x ou mais, há um juros de \033[1;31mR${juros:.2f}\033[m. O preço total a ser pago é de \033[1;30;41mR${preco_produto:.2f}\033[m! A parcela mensal fica em \033[1;31mR${preco_produto / nmr_parcelas:.2f}\033[m.')
