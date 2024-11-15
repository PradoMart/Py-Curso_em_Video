from Mundo_3.Class_22.project111new.utilitários import moeda
from Mundo_3.Class_22.project111new.utilitários import dado

num = dado.leia_dinheiro('NÚMERO: ')
abaixo = dado.leia_dinheiro('REDUÇÃO: ')
acima = dado.leia_dinheiro('AUMENTO: ')
moeda.resumo(num,abaixo,acima,True)