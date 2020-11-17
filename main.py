from tabulate import tabulate
from tarefas import Tarefas
from datas import Data
from pesquisas import Pesquisa
from random import randint
import pandas as pd


def menu_opcoes():
    table = [["Adicionar Nova Tarefa: ", "1"],
             ["Realizar Pesquisa: ", "2"],
             ["Ver tarefas cadastradas no Sistema: ", "3"]]
    print(tabulate(table))

def opcoes():
    opcao_menu = int(input('Digite a opção desejada: '))

    if opcao_menu == 1:
        identificacao_numerica_aletoria = randint(1, 100)

        descricao_da_tarefa = input('Descrição da tarefa: ')

        dia_do_cadastro = Data.dia_atual()

        # Prazo de execução da tarefa
        print('Insira a data de Execução da tarefa de acordo com o for pedido.')
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
        Pesquisa.apresentar_tarefas()

        # PESQUISA POR STATUS DA TAREFA
        indice_da_pesquisa = int(input('Digite o Índice da tarefa que deseja verificar: '))
        Pesquisa.pesquisa_tarefas(indice_da_pesquisa)

        # Alterar o Status de alguma Tarefa:
        altera_status = input('Deseja alterar o status de alguma tarefa(SIM/NÃO): ')
        if altera_status.upper() == 'SIM':
            indice_tarefa = int(input('Digite o índice ao lado da tarefa: '))
            #linha = apresentar_colunas.loc[indice_tarefa]  # seleciona a linha do arquivo csv escolhido pelo usuário
            # status_tarefa =
            #print(linha)

        # Alterar algum dado da lista
        alteracao = input('Deseja alterar alguma Tarefa?:')
        if alteracao.upper() == 'SIM':
            print(pesquisar_tarefas['identificação'])
            indice = int(input('Digite o número de identificação da Tarefa: '))

        else:
            pass


    elif opcao_menu == 3:
        apresenta_tabela = pd.read_csv("tarefas.csv")
        table_apresenta_tabela = pd.DataFrame(data=apresenta_tabela, columns=['identificação', 'Descrição', 'Local',
                                                                              'Dia da execução', 'Status'])

        print(tabulate(table_apresenta_tabela))
    else:
        print('Operação não cadastrada')


menu_opcoes()
opcoes()
