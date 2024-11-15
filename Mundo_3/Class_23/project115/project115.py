from modulos import*
from time import sleep


arq = 'listagem.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)


while True:
    menu(['Novo Cadastro', 'Visualizar Cadastro', 'Limpar Arquivo', 'Sair do Sistema'])
    cores('Sua opção: ','amarelo')
    user_option = input().strip()
    
    while user_option not in '1234':
        cores('ERRO! Digite um número válido: ', 'vermelho')
        user_option = input().strip()

    if user_option == '4':
        cabeçalho('SAINDO DO SISTEMA. ATÉ LOGO!')
        break
    
    elif user_option == '1':
        cabeçalho('NOVO CADASTRO')
        
        nome = str(input(f'Nome: ')).strip().title()
        idade = input(f'Idade: ')
        leia_int(idade)
        cadastrar(arq,nome,idade)            
        
    elif user_option == '3':
        limpar_arquivo(arq)

    else:
        ler_arquivo(arq)

    