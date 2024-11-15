#AULA 12 - CONDIÇÕES ANINHADAS

#43 - CALCULADORA DE IMC
from time import sleep
print('')
print('\033[1;30;107mSEJA BEM-VINDO(A) AO CÁLCULO DE IMC!\033[m')
print('')
sleep(1)
print('Meu nome é Cimão, mas pode me chamar de \033[1;30;107mCIM\033[m! Eu quem vou te ajudar a descobrir seu IMC, ok?!')
print('')
sleep(1)
sabe_imc = str(input('Mas antes de calcularmos, você sabe o que é o Índice de Massa Corporal-IMC? ')).strip().upper()
sabe_imc = sabe_imc[0]
print('')
sleep(1.5)
if sabe_imc == "N":
    print('O índice de massa corporal é uma medida internacional usada para calcular se uma pessoa está no peso ideal.\nO cálculo é feito da seguinte forma: peso / (altura²).')
else:
    print('Aah que ótimo, então vamos direto pro cálculo!')
print('')
sleep(1)

peso = str(input('A primeira variável é o \033[1;30;107mpeso\033[m, quanto você está pesando? ')).replace(',','.')
peso = float(peso)
altura = str(input('Agora, preciso saber a sua \033[1;30;107maltura\033[m? ')).replace(',','.')
altura = float(altura)
imc = peso / (altura * altura)

print('')
sleep(1)

print('\033[1;30;107mCALCULANDO\033[m')

sleep(2)
print('')

if imc < 18.5:
    print(f'Com um IMC de \033[1;30;107m{imc:.2f}\033[m, você está \033[1;33mabaixo do peso\033[m. Cuide-se, pois magreza não é sinônimo de saúde!')
elif imc >= 18.5 and imc < 25:
    print(f'Com um IMC de \033[1;30;107m{imc:.2f}\033[m, você está no \033[1;32mpeso ideal\033[m. Continue se cuidando!')
elif imc >= 25 and imc < 30:
    print(f'Com um IMC de \033[1;30;107m{imc:.2f}\033[m, você está \033[1;33macima do peso ideal\033[m. Procure um nutricionista e cuide da sua saúde!')
elif imc >= 30 and imc < 40:
    print(f'Com um IMC de \033[1;30;107m{imc:.2f}\033[m, você está com \033[1;31mobesidade\033[m. Procure ajuda de um profissional qualificado e mude seus hábitos diários!')
elif imc > 40:
    print(f'Com um IMC de \033[1;30;107m{imc:.2f}\033[m, você está com \033[1;31mobesidade mórbida\033[m. AJA IMEDIATAMENTE! Obesidade mata!')