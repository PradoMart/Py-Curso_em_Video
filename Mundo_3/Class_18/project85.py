#AULA 18 - VARIÁVEIS COMPOSTAS -- LISTAS ANINHADAS []

#85 - LISTAS, separar números pares e ímpares, colocando-os em apenas UMA LISTA.
#eu tinha feito de uma forma diferente, criado 2 listas pros pares/impares. Não sabia que dava pra criar listas dentro de listas já na declaração da variável.

print('')

numbers = [[],[]]
for n in range(1,8):
    nums = int(input(f'Digite o {n}º valor: '))
    if nums % 2 == 0:
        numbers[0].append(nums)
    else:
        numbers[1].append(nums)

print(f'Os valores pares digitados são: {sorted(numbers[0])}.')
print(f'Os valores ímpares digitados são: {sorted(numbers[1])}.')
