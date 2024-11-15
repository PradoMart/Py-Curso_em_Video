#AULA 17 - VARIÁVEIS COMPOSTAS -- LISTAS []

#83 - LISTAS, Verificador de expressões matemática
print('')

expression = str(input('Type the math function: ')).strip().lower()
left_brackets = expression.count('(')
right_brackets = expression.count(')')

if left_brackets != right_brackets:
    print('\033[1;31mInvalid Expression!\033[m')
else:
    print('\033[1;32mCorrect Expression!\033[m')
