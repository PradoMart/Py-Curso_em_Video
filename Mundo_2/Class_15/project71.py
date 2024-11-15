#AULA 15 - INTERROMPENDO LAÇO DE REPETIÇÃO

#70 - SEM USAR FLAG NO LAÇO, caixa eletronico
print('')
nota_cem = nota_cinquenta = nota_vinte = nota_dez = nota_um = 0

saque = int(input('Quanto vai sacar? '))
saque_original = saque
divisao_cem = divisao_cin = divisao_vin = divisao_dez = divisao_cinco = divisao_um = 0
while saque != 0:
    if saque >= 100:
        divisao_cem = (saque // 100) - 1
        saque = saque - (100 * divisao_cem)
    if saque >= 50:
        divisao_cin = (saque // 50) - 1
        saque = saque - (50 * divisao_cin)
    if saque >= 20:
        divisao_vin = (saque // 20) - 1
        saque = saque - (20 * divisao_vin)
    if saque >= 10:
        divisao_dez = (saque // 10) - 1
        saque = saque - (10 * divisao_dez)
    if saque >= 5:
        divisao_cinco = (saque // 5) - 1
        saque = saque - (5 * divisao_cinco)
    if saque >= 1:
        divisao_um = (saque // 1)
        saque = saque - divisao_um
    print(f'''Do seu saque de R${saque_original},00, separei-o em:\n
{divisao_cem} nota(s) de 100 = R${divisao_cem * 100},00;
{divisao_cin} nota(s) de 50 = R${divisao_cin * 50},00; 
{divisao_vin} nota(s) de 20 = R${divisao_vin * 20},00;
{divisao_dez} nota(s) de 10 = R${divisao_dez * 10},00;
{divisao_cinco} nota(s) de 5 = R${divisao_cinco * 5},00;
{divisao_um} nota(s) de 1 = R${divisao_um * 1},00.''')
    break




