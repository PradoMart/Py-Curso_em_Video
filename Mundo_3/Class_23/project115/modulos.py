def cabeçalho(mensagem):
    print()
    print(f'-'*30)
    print(str(mensagem).center(30)) 
    print(f'-'*30)

def cores(msg, cor):
    cor = str(cor).strip().upper()
    if cor == 'AMARELO':
        print(f'\033[1;33m{str(msg)}\033[m', end='')
    elif cor == 'VERMELHO':
        print(f'\033[1;31m{msg}\033[m', end='')

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c +=1
    print(f'-'*30)


def leia_int(num):
    while num.isnumeric() == False:
        num = (input(f'Idade: '))

def arquivo_existe(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt') #rt --> read text
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'wt+') #rt --> write text
        arquivo.close()
    except:
        cores('ERRO AO CRIAR ARQUIVO!', 'vermelho')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso!')

def limpar_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo,'w')
        arquivo.write('')
    except:
        cores('ERRO AO APAGAR CONTEÚDO DO ARQUIVO!', 'vermelho')
        

def ler_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt') #rt --> read text
    except:
        cores('ERRO AO LER ARQUIVO!', 'vermelho')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(f'{"NAME":<24} {"AGE":>3}')
        for item in (arquivo):
            dado = item.split(';')
            dado[1] = dado[1].replace('\n','')           
            print(f'{dado[0]:<25}{dado[1]:>3}')
    finally:
        arquivo.close()

def cadastrar(nome_arquivo, nome ='Desconhecido', idade = 0):
    try:
        arquivo = open(nome_arquivo, 'at') #at --> append text
    except:
        cores('ERRO AO ABRIR O ARQUIVO!')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            cores('ERRO AO ESCREVER NO ARQUIVO!')
        else:
            print(f'\n{nome} cadastrado(a) com sucesso!')
            arquivo.close()