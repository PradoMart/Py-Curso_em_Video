#AULA 14 - LAÇO DE REPETIÇÃO WHILE

#63 SEQUENCIA DE FIBONACCI
#0 1 1 2 3 5 8 --> O valor do próximo número é o resultado da soma do último e do penúltimo.
# Não consegui fazer sozinho, pq eu tava considerando o contador como 0 e os prints do inicial e próximo (antes do while) estavam dentro do while.
print('')
termos = int(input('Quantos termos você quer ver? '))
inicial = 0
proximo = 1

print('~'*30)
print(f'{inicial} - {proximo}', end=' - ')

contador = 3
while contador <= termos:
    fib = inicial + proximo
    print(fib, end= ' - ')
    inicial = proximo
    proximo = fib
    contador += 1
print('FIM!')
print('~' * 30)