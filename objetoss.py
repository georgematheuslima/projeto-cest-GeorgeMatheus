from tabulate import tabulate
from datas import Cadastro_dia
#   CRIANDO O MENU DE INTERAÇÃO COM O USUÁRIO
table = [

    ['1 ' 'Adicionar nova tarefa'],
    ['2 ' 'Pesquisar tarefas'],
    ['3 ' 'Mostrar tarefas cadastradas']

]
print(tabulate(table))


# RECEBENDO A ENTRADA DO USUÁRIO

opcao = int(input('Digite a opção correspondente a operação que deseja realizar: '))

if opcao == 1:
    print('Adicionar nova tarefa. ')
    tarefa = []
    descrever = input('Descrição da tarefa: ')
    tarefa.append(descrever)
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mês: '))
    ano = int(input('Digite o ano: '))
    Cadastro_dia(dia, mes, ano)