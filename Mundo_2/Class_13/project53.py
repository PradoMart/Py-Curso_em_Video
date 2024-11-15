#AULA 13 - LAÇO DE REPETIÇÃO FOR

#52 - PALÍNDROMO - não consegui sozinho
print('')
print('\033[7;30;107mIDENTIFICADOR DE PALÍNDROMO!\033[m')
print('')

print('Você sabe o que é um palíndromo?')
sabe_naosabe = input('Responda "SIM ou NÃO": ').strip().upper()
while sabe_naosabe.isalpha() == False:
    sabe_naosabe = input('Só vale texto. SIM ou NÃO? ').strip().upper()
print('')

if sabe_naosabe[0] == "N":
    print('Palíndromo é quando uma frase é colocada de trás pra frente e mantém a exata ordem das palavras.')
    print('')

frase = str(input('Digite a frase (sem acentos): ')).strip().replace(' ', '')
frase_reverso = frase[::-1].replace(' ','')
print('')

if frase == frase_reverso:
    print(f'\033[7;30;107mSua frase é um palíndromo\033[m!\nDá uma olhada como ela é \033[1;34mnormal\033[m e de \033[1;33mtrás pra frente\033[m:\n"\033[1;34m{frase}\033[m"\n"\033[1;33m{frase_reverso}\033[m"')
else:
    print(f'\033[7;30;107mSua frase NÃO é um palíndromo\033[m! Dá uma olhada como ela é \033[1;34mnormal\033[m e de \033[1;33mtrás pra frente\033[m:\n"\033[1;34m{frase}\033[m"\n"\033[1;33m{frase_reverso}\033[m"')