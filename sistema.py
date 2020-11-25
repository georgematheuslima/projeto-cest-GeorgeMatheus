from tarefas import Tarefas
from datas import Data
from random import randint


Tarefas.menu_opcoes()

def opcoes():
    opcao_menu = int(input('Digite a opção desejada: '))

    if opcao_menu == 1:
        identificacao_numerica_aletoria = randint(1, 100)

        descricao_da_tarefa = input('Descrição da tarefa: ')

        dia_do_cadastro = Data.dia_atual()

        # Prazo de execução da tarefa
        print('Insira a data de Execução da tarefa de acordo com o for pedido.')
        dia = int(input('Digite o dia da execução (Número): '))
        mes = int(input('Digite o mês da execução (Número): '))
        ano = int(input('Digite o Ano da execução (Número): '))
        data_da_execucao = Data.executar_tarefa(dia, mes, ano)

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
                                               data_da_execucao, local_da_tarefa, coluna_do_status)

        # colocando dados em um arquivo .csv
        arquivo_csv = Tarefas.adicionando_csv(inserindo_tarefas_arquivocsv)

        nova_operacao = input('Deseja realizar outra operação?(Sim / Não):  ')
        Tarefas.nova_operacao(nova_operacao)
        opcoes()

    elif opcao_menu == 2:
        print('Realizar pesquisa.\n')
        Tarefas.apresentar_tarefas()

        # PESQUISA POR STATUS DA TAREFA
        indice_da_pesquisa = int(input('Digite o Índice da tarefa que deseja verificar: '))
        Tarefas.pesquisa_tarefas(indice_da_pesquisa)

        nova_operacao = input('Deseja realizar outra operação?(Sim / Não):  ')
        Tarefas.nova_operacao(nova_operacao)
        opcoes()


    elif opcao_menu == 3:
        Tarefas.apresenta_tarefas_cadastradas()
        nova_operacao = input('Deseja realizar outra operação?(Sim / Não):  ')
        Tarefas.nova_operacao(nova_operacao)
        opcoes()


    else:
        print('Operação não cadastrada')
        nova_operacao = input('Deseja realizar outra operação?(Sim / Não):  ')
        Tarefas.nova_operacao(nova_operacao)
        opcoes()


opcoes()
