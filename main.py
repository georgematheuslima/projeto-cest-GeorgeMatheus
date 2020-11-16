from tabulate import tabulate
from tarefas import Tarefas
from datas import Data
from random import randint
import pandas as pd


def menu_opcoes():
    table = [["Adicionar Nova Tarefa: ", "1"],
             ["Realizar Pesquisa: ", "2"],
             ["Ver tarefas cadastradas no Sistema: ", "3"]]
    apresentar_menu = print(tabulate(table))
    return apresentar_menu


def opcoes():
    opcao_menu = int(input('Digite a opção desejada: '))

    if opcao_menu == 1:

        # identificação numérica da Tarefa a ser cadastrada, dada de forma aleatória ( entre 0 e 100).
        identificacao_numerica_aletoria = randint(1, 100)

        # Descrição da nova tarefa a ser cadastrada.
        descricao_da_tarefa = input('Descrição da tarefa: ')

        # Dia em que a tarefa está sendo cadastrada.
        dia_do_cadastro = Data.dia_atual()

        # Prazo de execução da tarefa
        dia = int(input('Digite o dia da execução: '))
        mes = int(input('Digite o mês: '))
        ano = int(input('Digite o Ano: '))
        dia_da_execucao = Data.executar_tarefa(dia, mes, ano)

        # Local de execução da tarefa
        local_da_tarefa = input('Local da tarefa: ')

        # status da tarefa
        status_da_tarefa = int(input('Status da tarefa:\n [1] Pendente \n [2] Realizado:   '))

        def status_inicial_tarefa(input_usuario):
            if status_da_tarefa == 1:
                status = "Pendente"
                return status
            elif status_da_tarefa == 2:
                status = "Realizado"
                return status
            else:
                raise ValueError('Operação inválida')

        coluna_do_status = status_inicial_tarefa(status_da_tarefa)

        # Envia todos os inputs para o Objeto Tarefas.
        inserindo_tarefas_arquivocsv = Tarefas(identificacao_numerica_aletoria, descricao_da_tarefa, dia_do_cadastro,
                                               dia_da_execucao, local_da_tarefa, coluna_do_status)

        # colocando dados em um arquivo .csv
        arquivo_csv = Tarefas.adicionando_csv(inserindo_tarefas_arquivocsv)

        nova_operacao = input('Deseja realizar outra operação?(Sim / Não):  ')
        if nova_operacao.upper() == 'SIM':
            menu_opcoes()
            opcoes()
        else:
            Tarefas.encerrar_sistema()


    elif opcao_menu == 2:
        print('Realizar pesquisa.\n')
        tipo_da_pesquisa = int(input('Digite [1] para pesquisar por Status,'
                                     ' ou [2] para pesquisar por identificação. '))

        # PESQUISA POR STATUS DA TAREFA
        if tipo_da_pesquisa == 1:
            pesquisar = pd.read_csv("tarefas.csv")
            apresentar_colunas = pd.DataFrame(data=pesquisar, columns=['Descrição', 'Status'])
            print(apresentar_colunas)

            # Alterar o Status de alguma Tarefa:
            altera_status = input('Deseja alterar o status de alguma tarefa(SIM/NÃO): ')
            if altera_status.upper() == 'SIM':
                indice_tarefa = int(input('Digite o índice ao lado da tarefa: '))
                linha = apresentar_colunas.loc[indice_tarefa]  # seleciona a linha do arquivo csv escolhido pelo usuário
                # status_tarefa =
                print(linha)

            # Alterar algum dado da lista
            alteracao = input('Deseja alterar alguma Tarefa?:')
            if alteracao.upper() == 'SIM':
                print(pesquisar['identificação'])
                indice = int(input('Digite o número de identificação da Tarefa: '))

            else:
                pass

        # PESQUISA POR IDENTIFICAÇÃO NUMÉRICA DA TAREFA.
        elif tipo_da_pesquisa == 2:
            pesquisar = pd.read_csv("tarefas.csv")
            print(pesquisar['identificação'])


    elif opcao_menu == 3:
        apresenta_tabela = pd.read_csv("tarefas.csv")
        table_apresenta_tabela = pd.DataFrame(data=apresenta_tabela, columns=['identificação', 'Descrição', 'Local',
                                                                              'Dia da execução', 'Status'])

        print(tabulate(table_apresenta_tabela))
    else:
        print('Operação não cadastrada')


menu_opcoes()
opcoes()
