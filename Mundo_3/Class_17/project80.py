#AULA 17 - VARIÁVEIS COMPOSTAS -- LISTAS []

#80 - LISTAS, Armazenando vários valores, mostrando em ordem crescente sem usar o sort
#não consegui fazer sozinho, pq não sabia como poderia resolver o B.O dos números que eram menores dos que já estavam na lista.

print('')

lista_nums = []

for x in range(0,5):
    nums = int(input('Digite um valor: '))
    if len(lista_nums) == 0 or nums >= max(lista_nums):
        lista_nums.append(nums)
    else:
        posição = 0 
        while posição < len(lista_nums):
            if nums <= lista_nums[posição]:
                lista_nums.insert(posição, nums)
                break
            posição += 1

print(lista_nums)