# RECEBENDO A ENTRADA DO USUÁRIO E ARMAZENANDO NO DICIONARIO.
from tabulate import tabulate
from tarefas import Tarefas
from datas import Data
from random import randint
import pandas as pd

def menu_opcoes():
    table = [["Adicionar Nova Tarefa: ", "1"],
             ["Realizar Pesquisa: ", "2"],
             ["Ver tarefas cadastradas no Sistema: ", "3"]]
    print(tabulate(table))
menu_opcoes()
opcao_menu = int(input('Digite a opção desejada: '))

if opcao_menu == 1:
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
    status_tarefa = int(input('Status da tarefa:\n [1] Pendente \n [2] Realizado:   '))
    def status_inicial_tarefa(n):
        if status_tarefa == 1:
            status = "Pendente"
            return status
        elif status_tarefa == 2:
            status = "Realizado"
            return status
        else:
            raise ValueError ('Operação inválida')

    coluna_status = status_inicial_tarefa(status_tarefa)


    # Envia todos os inputs para o Objeto Tarefas.
    tarefas = Tarefas(identificacao, descricao, dia_cadastro, dia_execucao, local, coluna_status)

    # colocando dados em um arquivo .csv
    arquivo_csv = Tarefas.adicionando_csv(tarefas)

    operacao = input('Deseja realizar outra operação?(Sim / Não):  ')
    if operacao.upper() == 'SIM':
        menu_opcoes()
    else:
        print('Obrigado por utilizar o sistema.')


elif opcao_menu == 2:
    print('Realizar pesquisa.\n')
    tipo_pesquisa = int(input('Digite [1] para pesquisar por Status,'
                              ' ou [2] para pesquisar por identificação. '))


   # PESQUISA POR STATUS DA TAREFA
    if tipo_pesquisa == 1:
        pesquisar = pd.read_csv("tarefas.csv")
        apresentar_colunas = pd.DataFrame(data=pesquisar, columns=['Descrição', 'Status'])
        print(apresentar_colunas)

        # Alterar o Status de alguma Tarefa:
        altera_status = input('Deseja alterar o status de alguma tarefa(SIM/NÃO): ')
        if altera_status.upper() == 'SIM':
            indice_tarefa = int(input('Digite o índice ao lado da tarefa: '))
            linha = apresentar_colunas.loc[indice_tarefa] # seleciona a linha do arquivo csv escolhido pelo usuário
            #status_tarefa =
            print(linha)


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


elif opcao_menu == 3:
    apresenta_tabela = pd.read_csv("tarefas.csv")
    tabela = pd.DataFrame(data=apresenta_tabela, columns=['identificação', 'descrição','Local','Dia da execução' ,
                                                          'Status' ])
    print(tabela)
else:
    print('Operação não cadastrada')

