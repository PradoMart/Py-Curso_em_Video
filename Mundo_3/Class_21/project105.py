#AULA 21 - FUNÇÕES

#105 - FUNÇÕES, dicionários
dicionario = {}

def notas(*num, sit=False):
    """_summary_
        --> Função para analisar notas e situações de vários alunos
    Args:
        *n = as notas do aluno;
        sit = valor opcional, indicando se deve, ou não, adicionar a situação
    Returns:
        --> Dicionário com várias informações sobre a situação da turma
    """
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['média'] = float((f'{sum(num) / len(num):.2f}'))
    if sit == True:
        if dicionario['média'] < 7:
            dicionario['situação'] = 'Reprovado'
        elif dicionario['média'] < 9:
            dicionario['situação'] = 'Aprovado'
        elif dicionario['média'] >= 9:
            dicionario['situação'] = 'Parabéns!'
    return dicionario

resp = notas(5,6,7.8, sit = True)
print(resp)
#help(notas)