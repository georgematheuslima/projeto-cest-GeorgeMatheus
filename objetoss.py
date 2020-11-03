# RECEBENDO A ENTRADA DO USUÁRIO E ARMAZENANDO NO DICIONARIO.
from tabulate import tabulate
from tarefas import Tarefas
from datas import Data
from random import randint
import pandas as pd


table = [["Adicionar Nova Tarefa: ", "1"],
         ["Realizar Pesquisa: ", "2"],
         ["Ver tarefas cadastradas no Sistema: ", "3"]]
print(tabulate(table))

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    confirma = print('Adicionar Nova tarefa.')

    # identificação numérica da Tarefa a ser cadastrada, dada de forma aleatória ( entre 0 e 100).
    identificacao = randint(1, 100)

    # Descrição da nova tarefa a ser cadastrada.
    descricao = input('Descrição da tarefa: ')

    # Dia em que a tarefa está sendo cadastrada.
    dia_cadastro = Data.dia_atual()

    # Prazo de execução da tarefa
    dia = int(input('Digite o dia da execução: '))
    mes = int(input('Digite o mês: '))
    ano = int(input('Digite o Ano: '))
    dia_execucao = Data.executar_tarefa(dia, mes, ano)

    # Local de execução da tarefa
    local = input('Local da tarefa: ')

    # status da tarefa
    status = input('Status da tarefa: ')

    # Envia todos os imputs para o Objeto Tarefas.
    tarefas = Tarefas(identificacao, descricao, dia_cadastro, dia_execucao, local, status)

    # colocando dados em um arquivo .csv
    arquivo_csv = Tarefas.adicionando_csv(tarefas)

    operacao = input('Deseja realizar outra operação?(Sim / Não):  ')
    if operacao.upper() == 'SIM':
        print(opcao)
    else:
        print('Obrigado por utilizar o sistema.')


elif opcao == 2:
    print('Realizar pesquisa.\n')
    tipo_pesquisa = int(input('Digite [1] para pesquisar por Status,'
                              ' ou [2] para pesquisar por identificação. '))


   # PESQUISA POR STATUS DA TAREFA
    if tipo_pesquisa == 1:
        pesquisar = pd.read_csv("tarefas.csv")
        print(pesquisar['Status'])

        # Alterar algum dado da lista
        alteracao = input('Deseja alterar alguma Tarefa?:' )
        if alteracao.upper() == 'SIM':
            print(pesquisar['identificação'])
            indice = int(input('Digite o número de identificação da Tarefa: '))
        else:
            pass

    # PESQUISA POR IDENTIFICAÇÃO NUMÉRICA DA TAREFA.
    elif tipo_pesquisa == 2:
        pesquisar = pd.read_csv("tarefas.csv")
        print(pesquisar['identificação'])


elif opcao == 3:
    pesquisa = pd.read_csv("tarefas.csv")
    print(pesquisa.head())
else:
    print('Operação não cadastrada')
